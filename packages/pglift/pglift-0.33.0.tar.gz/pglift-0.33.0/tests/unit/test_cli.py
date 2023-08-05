import datetime
import functools
import json
import logging
import os
import re
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Dict, Iterator, List, Tuple, Type
from unittest.mock import MagicMock, patch

import click
import psycopg
import pydantic
import pytest
import rich
import yaml
from click.shell_completion import ShellComplete
from click.testing import CliRunner
from pgtoolkit.ctl import Status

from pglift import (
    _install,
    databases,
    exceptions,
    instances,
    postgresql,
    prometheus,
    roles,
    types,
)
from pglift.cli import cli
from pglift.cli import instance as instance_cli
from pglift.cli.postgres import cli as postgres_cli
from pglift.cli.util import (
    CLIContext,
    Command,
    InvalidSettingsError,
    Obj,
    get_instance,
    pass_component_settings,
    pass_ctx,
)
from pglift.ctx import Context
from pglift.models import helpers, interface, system
from pglift.models.system import Instance
from pglift.pgbackrest import base as pgbackrest
from pglift.pgbackrest import repo_path
from pglift.pgbackrest.cli import pgbackrest as pgbackrest_cli
from pglift.pm import PluginManager
from pglift.prometheus import impl as prometheus_impl
from pglift.prometheus.cli import postgres_exporter as postgres_exporter_cli
from pglift.prometheus.models import Service
from pglift.settings import PostgreSQLVersion, Settings

instance_arg_guessed_or_given = pytest.mark.parametrize(
    "args", [[], ["test"]], ids=["instance:guessed", "instance:given"]
)

all_plugins = PluginManager.all()


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner(mix_stderr=False)


@pytest.fixture
def ctx(settings: Settings) -> CLIContext:
    return CLIContext(settings=settings)


@pytest.fixture
def obj(ctx: CLIContext) -> Obj:
    return Obj(context=ctx)


@contextmanager
def set_console_width(width: int) -> Iterator[None]:
    old_width = rich.get_console().width
    rich.reconfigure(width=width)
    yield
    rich.reconfigure(width=old_width)


@pytest.fixture
def postgresql_running(ctx: Context, instance: Instance) -> Iterator[MagicMock]:
    with patch("pglift.postgresql.running") as m:
        yield m
    m.assert_called_once_with(ctx, instance)


@click.command(cls=Command)
@click.argument("error")
@click.pass_context
def cmd(ctx: click.Context, error: str) -> None:
    if error == "error":
        raise exceptions.CommandError(1, ["bad", "cmd"], "output", "errs")
    if error == "cancel":
        raise exceptions.Cancelled("flop")
    if error == "runtimeerror":
        raise RuntimeError("oups")
    if error == "exit":
        ctx.exit(1)


def test_yaml_site_settings_error(
    tmp_path: Path, site_settings: MagicMock, runner: CliRunner
) -> None:
    configdir = tmp_path / "pglift"
    configdir.mkdir()
    settings_fpath = configdir / "settings.yaml"
    settings_fpath.touch()
    site_settings.return_value = settings_fpath
    with pytest.raises(InvalidSettingsError, match="expecting an object"):
        Obj()


@pytest.mark.parametrize(
    "debug, logpath_exists",
    [
        pytest.param(True, False, id="debug:true, logpath_exists:false"),
        pytest.param(False, True, id="debug:false, logpath_exists:true"),
    ],
    ids=lambda v: f"debug: {v[0]}, logpath_exists: {v[1]}",
)
def test_command_error(
    runner: CliRunner,
    obj: Obj,
    caplog: pytest.LogCaptureFixture,
    debug: bool,
    logpath_exists: bool,
) -> None:
    obj.debug = debug
    logpath = obj.ctx.settings.cli.logpath
    if logpath_exists:
        logpath.mkdir()
    with caplog.at_level(logging.DEBUG, logger="pglift"):
        result = runner.invoke(cmd, ["error"], obj=obj)
    if debug:
        (__, __, record, __) = caplog.records
        assert record.exc_text and record.exc_text.startswith(
            "Traceback (most recent call last):"
        )
    else:
        (__, record) = caplog.records
        assert record.exc_text is None
    assert result.exit_code == 1
    assert (
        result.stderr
        == "Error: Command '['bad', 'cmd']' returned non-zero exit status 1.\nerrs\noutput\n"
    )
    assert not list(logpath.glob("*.log"))
    if logpath_exists:
        assert logpath.exists()
    else:
        assert not logpath.exists()


def test_command_cancelled(runner: CliRunner, obj: Obj) -> None:
    result = runner.invoke(cmd, ["cancel"], obj=obj)
    assert result.exit_code == 1
    assert result.stderr == "Aborted!\n"
    logpath = obj.ctx.settings.cli.logpath
    assert not list(logpath.glob("*.log"))


def test_command_exit(runner: CliRunner, obj: Obj) -> None:
    result = runner.invoke(cmd, ["exit"], obj=obj)
    assert result.exit_code == 1
    assert not result.stdout
    logpath = obj.ctx.settings.cli.logpath
    assert not list(logpath.glob("*.log"))


def test_command_internal_error(runner: CliRunner, obj: Obj) -> None:
    result = runner.invoke(cmd, ["runtimeerror"], obj=obj)
    assert result.exit_code == 1
    logpath = obj.ctx.settings.cli.logpath
    logfile = next(logpath.glob("*.log"))
    logcontent = logfile.read_text()
    assert "an unexpected error occurred" in logcontent
    assert "Traceback (most recent call last):" in logcontent
    assert "RuntimeError: oups" in logcontent


def test_pass_component_settings(runner: CliRunner, obj: Obj) -> None:
    mod = MagicMock()

    @click.command("command")
    @functools.partial(pass_component_settings, mod, "mymod")
    def command(settings: Any, *args: Any) -> None:
        click.echo(f"settings is {settings.id}")

    rv = MagicMock(id="123")
    mod.available.return_value = rv
    r = runner.invoke(command, obj=obj)
    assert r.exit_code == 0
    assert r.stdout == "settings is 123\n"


def test_get_instance(ctx: Context, instance: Instance) -> None:
    assert get_instance(ctx, instance.name, instance.version) == instance

    assert get_instance(ctx, instance.name, None) == instance

    with pytest.raises(click.BadParameter):
        get_instance(ctx, "notfound", None)

    with pytest.raises(click.BadParameter):
        get_instance(ctx, "notfound", instance.version)

    with patch.object(Instance, "system_lookup") as system_lookup:
        with pytest.raises(
            click.BadParameter,
            match="instance 'foo' exists in several PostgreSQL version",
        ):
            get_instance(ctx, "foo", None)
    assert system_lookup.call_count == 2


def test_instance_identifier(runner: CliRunner, obj: Obj, instance: Instance) -> None:
    @click.command(cls=Command)
    @instance_cli.instance_identifier(nargs=1)
    def one(instance: system.Instance) -> None:
        """One"""
        click.echo(instance, nl=False)

    @click.command(cls=Command)
    @instance_cli.instance_identifier(nargs=-1)
    def many(instance: Tuple[system.Instance]) -> None:
        """Many"""
        click.echo(", ".join(str(i) for i in instance), nl=False)

    result = runner.invoke(one, [], obj=obj)
    assert result.exit_code == 0, result.stderr
    assert result.stdout == str(instance)

    result = runner.invoke(many, [], obj=obj)
    assert result.exit_code == 0, result.stderr
    assert result.stdout == str(instance)

    result = runner.invoke(one, [str(instance)], obj=obj)
    assert result.exit_code == 0, result.stderr
    assert result.stdout == str(instance)

    result = runner.invoke(many, [str(instance), instance.name], obj=obj)
    assert result.exit_code == 0, result.stderr
    assert result.stdout == f"{instance}, {instance}"


def test_instance_identifier_all_instances(
    runner: CliRunner, obj: Obj, instance: Instance, instance2: Instance
) -> None:
    @click.command(cls=Command)
    @instance_cli.instance_identifier(nargs=-1)
    @click.option("--all", "all_instances", is_flag=True)
    def all(instance: Tuple[system.Instance], all_instances: bool) -> None:
        """All"""
        click.echo(", ".join(str(i) for i in instance), nl=False)

    result = runner.invoke(all, [str(instance)], obj=obj)
    assert result.exit_code == 0, result.stderr
    assert result.stdout == str(instance)

    result = runner.invoke(all, [str(instance), instance2.name], obj=obj)
    assert result.exit_code == 0, result.stderr
    assert result.stdout == f"{instance}, {instance2}"

    result = runner.invoke(all, ["--all"], obj=obj)
    assert result.exit_code == 0, result.stderr
    assert result.stdout == f"{instance}, {instance2}"


def test_instance_commands_completion(runner: CliRunner, obj: Obj) -> None:
    group = instance_cli.cli
    assert group.name
    comp = ShellComplete(group, {"obj": obj}, group.name, "_CLICK_COMPLETE")
    commands = [c.value for c in comp.get_completions([], "")]
    assert commands == [
        "alter",
        "backup",
        "backups",
        "create",
        "drop",
        "env",
        "exec",
        "get",
        "list",
        "logs",
        "privileges",
        "promote",
        "reload",
        "restart",
        "restore",
        "start",
        "status",
        "stop",
        "upgrade",
    ]


def test_obj(monkeypatch: pytest.MonkeyPatch) -> None:
    with monkeypatch.context() as m:
        m.setenv("SETTINGS", json.dumps({"invalid": None}))
        with pytest.raises(click.ClickException, match="invalid site settings"):
            Obj()


def test_obj_as_root(run_as_non_root: MagicMock) -> None:
    run_as_non_root.return_value = True
    with pytest.raises(click.ClickException, match="unsupported operation"):
        Obj()


def test_cli(runner: CliRunner, obj: Obj) -> None:
    result = runner.invoke(cli, obj=obj)
    assert result.exit_code == 0


def test_non_interactive(runner: CliRunner) -> None:
    @cli.command("confirmme")
    @pass_ctx
    def confirm_me(ctx: Context) -> None:
        if not ctx.confirm("Confirm?", default=True):
            raise click.Abort()
        print("confirmed")

    result = runner.invoke(cli, ["confirmme"], input="n\n")
    assert result.exit_code == 1 and "Aborted!" in result.stderr

    result = runner.invoke(cli, ["--non-interactive", "confirmme"])
    assert result.exit_code == 0 and "confirmed" in result.stdout


def test_version(runner: CliRunner, obj: Obj) -> None:
    result = runner.invoke(cli, ["--version"], obj=obj)
    assert re.match(r"pglift version (\d\.).*", result.stdout)


def test_site_settings(
    runner: CliRunner, ctx: Context, obj: Obj, monkeypatch: pytest.MonkeyPatch
) -> None:
    settings = json.loads(ctx.settings.json())
    assert settings["powa"]
    with set_console_width(500):
        result = runner.invoke(cli, ["site-settings"], obj=obj)
    assert result.exit_code == 0, result.stderr
    assert yaml.safe_load(result.output) == settings

    result = runner.invoke(cli, ["site-settings", "-o", "json"], obj=obj)
    assert result.exit_code == 0, result.stderr
    assert json.loads(result.output) == settings

    with monkeypatch.context() as m:
        m.setenv("PREFIX", "/srv/pglift")
        result_no_option = runner.invoke(cli, ["site-settings", "-o", "json"], obj=obj)
        assert result_no_option.exit_code == 0, result_no_option.stderr
        result_defaults = runner.invoke(
            cli, ["site-settings", "-o", "json", "--defaults"], obj=obj
        )
        assert result_defaults.exit_code == 0, result_defaults.stderr
        result_no_defaults = runner.invoke(
            cli, ["site-settings", "-o", "json", "--no-defaults"], obj=obj
        )
        assert result_no_defaults.exit_code == 0, result_no_defaults.stderr
    no_option_settings = json.loads(result_no_option.output)
    assert no_option_settings == settings
    defaults_settings = json.loads(result_defaults.output)
    assert defaults_settings["prefix"] == "/srv/pglift"
    assert defaults_settings["powa"] is None
    no_defaults_settings = json.loads(result_no_defaults.output)
    # lock_file is not explicitly defined, but is computed from environment
    assert no_defaults_settings["cli"]["lock_file"] == settings["cli"]["lock_file"]
    # powa is defined explicitly (empty)
    assert no_defaults_settings["powa"] != settings["powa"]
    # systemd contains values computed from environment (unit_path) and some
    # not explicitly defined (sudo)
    assert (
        "sudo" not in no_defaults_settings["systemd"] and "sudo" in settings["systemd"]
    )
    assert (
        no_defaults_settings["systemd"]["unit_path"] == settings["systemd"]["unit_path"]
    )


def test_site_settings_schema(runner: CliRunner, ctx: Context, obj: Obj) -> None:
    result = runner.invoke(cli, ["site-settings", "--schema", "-o", "json"], obj=obj)
    assert result.exit_code == 0, result.stderr
    schema = json.loads(result.output)
    schema.pop("title")
    expected = json.loads(ctx.settings.schema_json())
    expected.pop("title")
    assert schema == expected


def test_site_configure(
    runner: CliRunner, pm: PluginManager, settings: Settings, obj: Obj, tmp_path: Path
) -> None:
    with patch.object(_install, "do") as do_install:
        result = runner.invoke(
            cli, ["site-configure", "install", f"--settings={tmp_path}"], obj=obj
        )
    assert result.exit_code == 0, result
    do_install.assert_called_once_with(pm, settings, env=f"SETTINGS=@{tmp_path}")

    with patch.object(_install, "undo") as undo_install:
        result = runner.invoke(cli, ["site-configure", "uninstall"], obj=obj)
    assert result.exit_code == 0, result
    undo_install.assert_called_once_with(pm, settings)


@pytest.mark.parametrize("shell", ["bash", "fish", "zsh"])
def test_completion(runner: CliRunner, shell: str) -> None:
    result = runner.invoke(cli, ["--completion", shell])
    assert result.exit_code == 0, result
    assert "_pglift_completion" in result.output


@pytest.mark.parametrize(
    "objtype", ["instance", "role", "database", "postgresexporter"]
)
def test_argspec(
    datadir: Path, runner: CliRunner, obj: Obj, objtype: str, write_changes: bool
) -> None:
    cmd, args = cli, [objtype, "--ansible-argspec"]
    if objtype == "postgresexporter":
        cmd, args = postgres_exporter_cli, ["--ansible-argspec"]
    result = runner.invoke(cmd, args, obj=obj)
    data = json.loads(result.stdout)
    fpath = datadir / f"ansible-argspec-{objtype}.json"
    expected = json.loads(fpath.read_text())
    assert data == expected


@pytest.mark.parametrize(
    "objtype",
    [
        ("instance", interface.Instance, interface.InstanceApplyResult),
        ("role", interface.Role, interface.ApplyResult),
        ("database", interface.Database, interface.ApplyResult),
        ("postgresexporter", prometheus.models.PostgresExporter, interface.ApplyResult),
    ],
)
def test_ansible_doc(
    datadir: Path,
    obj: Obj,
    objtype: Tuple[str, Type[pydantic.BaseModel], Type[pydantic.BaseModel]],
    write_changes: bool,
) -> None:
    name, m, r = objtype
    if hasattr(m, "composite"):
        model = m.composite(all_plugins)
    else:
        model = m
    data = {
        "options": helpers.argspec_from_model(model),
        "return values": helpers.argspec_from_model(r),
    }
    fpath = datadir / "ansible-doc-fragments" / f"{name}.json"
    fpath.parent.mkdir(parents=True, exist_ok=True)
    if write_changes:
        fpath.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    expected = json.loads(fpath.read_text())
    assert data == expected


def test_instance_create(
    runner: CliRunner,
    ctx: Context,
    obj: Obj,
    instance: Instance,
    composite_instance_model: Type[interface.Instance],
    pg_version: str,
) -> None:
    result = runner.invoke(
        cli,
        ["instance", "create", "in/va/lid", "--pgbackrest-stanza=mystanza"],
        obj=obj,
    )
    assert result.exit_code == 2
    assert (
        "Error: Invalid value for 'NAME': instance name must not contain slashes"
        in result.stderr.splitlines()
    )

    with patch.object(instances, "apply") as apply:
        result = runner.invoke(
            cli,
            [
                "instance",
                "create",
                instance.name,
                f"--version={instance.version}",
                "--pgbackrest-stanza=mystanza",
            ],
            obj=obj,
        )
    assert not apply.call_count
    assert result.exit_code == 1
    assert "instance already exists" in result.stderr

    cmd = [
        "instance",
        "create",
        "new",
        f"--version={pg_version}",
        "--port=1234",
        "--locale=fr_FR.UTF8",
        "--encoding=LATIN1",
        "--data-checksums",
        "--auth-host=ident",
        "--prometheus-port=1212",
        "--temboard-port=2347",
        "--pgbackrest-stanza=mystanza",
    ]
    with patch.object(instances, "apply") as apply:
        result = runner.invoke(cli, cmd, obj=obj)
    expected = {
        "name": "new",
        "version": pg_version,
        "port": 1234,
        "locale": "fr_FR.UTF8",
        "encoding": "LATIN1",
        "data_checksums": True,
        "auth": {
            "local": None,
            "host": "ident",
        },
        "prometheus": {"port": 1212},
        "temboard": {"port": 2347},
        "pgbackrest": {"stanza": "mystanza"},
    }
    e = composite_instance_model.parse_obj(expected)
    apply.assert_called_once_with(ctx, e)
    assert result.exit_code == 0, result


def test_instance_create_standby(
    runner: CliRunner,
    ctx: Context,
    obj: Obj,
    composite_instance_model: Type[interface.Instance],
    pg_version: str,
) -> None:
    result = runner.invoke(
        cli,
        [
            "instance",
            "create",
            "stdby",
            "--standby-for=port 1234",
            "--version",
            pg_version,
            "--pgbackrest-stanza=mystanza",
        ],
        obj=obj,
    )
    assert result.exit_code == 2
    assert (
        """Error: Invalid value for '--standby-for': missing "=" after "port" in connection info string"""
        in result.stderr.splitlines()
    )

    cmd = [
        "instance",
        "create",
        "stdby",
        "--standby-for=port=1234 user=repli",
        "--standby-slot=sloot",
        "--standby-password=replicated",
        "--version",
        pg_version,
        "--pgbackrest-stanza=mystanza",
    ]
    with patch.object(instances, "apply") as apply:
        result = runner.invoke(cli, cmd, obj=obj)
    expected = {
        "name": "stdby",
        "standby": {
            "primary_conninfo": "port=1234 user=repli",
            "slot": "sloot",
            "password": "replicated",
        },
        "prometheus": {"port": 9187},
        "temboard": {"port": 2345},
        "pgbackrest": {"stanza": "mystanza"},
        "version": pg_version,
    }

    e = composite_instance_model.parse_obj(expected)
    apply.assert_called_once_with(ctx, e)
    assert result.exit_code == 0, result


def test_instance_apply(
    tmp_path: Path,
    runner: CliRunner,
    ctx: Context,
    obj: Obj,
    composite_instance_model: Type[interface.Instance],
) -> None:
    result = runner.invoke(cli, ["--debug", "instance", "apply"], obj=obj)
    assert result.exit_code == 2
    assert "Missing option '-f'" in result.stderr

    m = {
        "name": "test",
        "prometheus": {"password": "truite", "port": 1212},
        "temboard": {"port": 2347},
        "pgbackrest": {"stanza": "mystanza"},
    }
    manifest = tmp_path / "manifest.yml"
    content = yaml.dump(m)
    manifest.write_text(content)

    result = runner.invoke(
        cli,
        ["instance", "apply", "-f", str(manifest), "-o", "json", "--dry-run"],
        obj=obj,
    )
    assert result.exit_code == 0
    assert json.loads(result.stdout) == {"change_state": None, "pending_restart": False}

    apply_result = interface.InstanceApplyResult(
        change_state=interface.ApplyChangeState.created, pending_restart=True
    )
    with patch.object(instances, "apply", return_value=apply_result) as apply:
        result = runner.invoke(
            cli,
            ["instance", "apply", "-f", str(manifest), "--output-format=json"],
            obj=obj,
        )
    assert result.exit_code == 0, (result, result.output)
    assert json.loads(result.stdout) == {
        "change_state": "created",
        "pending_restart": True,
    }
    apply.assert_called_once_with(ctx, composite_instance_model.parse_obj(m))


def test_instance_alter(
    runner: CliRunner,
    ctx: Context,
    obj: Obj,
    instance: Instance,
    composite_instance_model: Type[interface.Instance],
) -> None:
    result = runner.invoke(
        cli, ["instance", "alter", "11/notfound", "--port=1"], obj=obj
    )
    assert result.exit_code == 2, result.stderr
    assert "instance '11/notfound' not found" in result.stderr

    actual_obj: Dict[str, Any] = {
        "name": instance.name,
        "prometheus": {"port": 1212},
        "temboard": {"port": 2347},
        "pgbackrest": {"stanza": "mystanza"},
    }
    altered_obj: Dict[str, Any] = {
        "name": instance.name,
        "state": "stopped",
        "prometheus": {"port": 2121},
        "temboard": {"port": 2437},
        "pgbackrest": {"stanza": "mystanza"},
    }
    cmd = [
        "instance",
        "alter",
        str(instance),
        "--state=stopped",
        "--prometheus-port=2121",
        "--temboard-port=2437",
    ]
    actual = composite_instance_model.parse_obj(actual_obj)
    altered = composite_instance_model.parse_obj(altered_obj)
    with patch.object(instances, "apply") as apply, patch.object(
        instances, "_get", return_value=actual
    ) as _get:
        result = runner.invoke(cli, cmd, obj=obj)
    _get.assert_called_once_with(ctx, instance)
    apply.assert_called_once_with(ctx, altered)
    assert result.exit_code == 0, result.output


def test_instance_promote(
    runner: CliRunner, ctx: Context, obj: Obj, instance: Instance
) -> None:
    result = runner.invoke(cli, ["instance", "promote", "notfound"], obj=obj)
    assert result.exit_code == 2, result.stderr
    assert "instance 'notfound' not found" in result.stderr
    with patch.object(instances, "promote") as promote:
        result = runner.invoke(cli, ["instance", "promote", str(instance)], obj=obj)
    assert result.exit_code == 0, result.stderr
    promote.assert_called_once_with(ctx, instance)


def test_instance_schema(runner: CliRunner, obj: Obj) -> None:
    result = runner.invoke(cli, ["instance", "--schema"], obj=obj)
    schema = json.loads(result.output)
    assert schema["title"] == "Instance"
    assert schema["description"] == "PostgreSQL instance"


@instance_arg_guessed_or_given
def test_instance_get(
    runner: CliRunner,
    ctx: Context,
    obj: Obj,
    instance: Instance,
    pg_version: str,
    args: List[str],
) -> None:
    manifest = interface.Instance.parse_obj(
        {
            "name": "test",
            "locale": "C",
            "encoding": "UTF16",
            "surole_password": "ahaha",
            "standby": {"primary_conninfo": "host=primary"},
        }
    )
    with patch.object(instances, "get", return_value=manifest) as get:
        json_result = runner.invoke(
            cli, ["instance", "get", "--output-format=json"] + args, obj=obj
        )
    get.assert_called_once_with(ctx, instance)
    assert json_result.exit_code == 0, (json_result, json_result.output)
    assert '"name": "test"' in json_result.output

    with patch.object(instances, "get", return_value=manifest) as get:
        table_result = runner.invoke(cli, ["instance", "get"] + args, obj=obj)
    get.assert_called_once_with(ctx, instance)
    assert table_result.exit_code == 0, (table_result, table_result.output)
    assert table_result.output.splitlines() == [
        " name  version  port  data_checksums  locale  encoding  pending_restart ",
        " test           5432                  C       UTF16     False           ",
    ]


def test_instance_list(
    runner: CliRunner, instance: Instance, ctx: Context, obj: Obj, tmp_path: Path
) -> None:
    name, version = instance.name, instance.version
    port = instance.config().port
    expected_list_as_json = [
        {
            "name": name,
            "datadir": str(instance.datadir),
            "port": port,
            "status": "not_running",
            "version": version,
        }
    ]
    logfile = tmp_path / "logfile"
    result = runner.invoke(
        cli,
        [
            "--log-level=debug",
            f"--log-file={logfile}",
            "instance",
            "list",
            "--output-format=json",
        ],
        obj=obj,
    )
    assert result.exit_code == 0
    assert json.loads(result.output) == expected_list_as_json

    assert "DEBUG get status of PostgreSQL instance" in logfile.read_text()

    result = runner.invoke(
        cli,
        ["instance", "list", "--output-format=json", f"--version={instance.version}"],
        obj=obj,
    )
    assert result.exit_code == 0
    assert json.loads(result.output) == expected_list_as_json

    other_version = next(
        v.version
        for v in ctx.settings.postgresql.versions
        if v.version != instance.version
    )
    result = runner.invoke(
        cli,
        ["instance", "list", "--output-format=json", f"--version={other_version}"],
        obj=obj,
    )
    assert result.exit_code == 0
    assert json.loads(result.output) == []
    result = runner.invoke(
        cli, ["instance", "list", f"--version={other_version}"], obj=obj
    )
    assert result.exit_code == 0
    assert not result.output

    ver = next(iter(PostgreSQLVersion))
    with patch.object(instances, "list") as list_instances:
        result = runner.invoke(
            cli, ["instance", "list", f"--version={ver.value}"], obj=obj
        )
    list_instances.assert_called_once_with(ctx, version=ver)


@instance_arg_guessed_or_given
def test_instance_drop(
    runner: CliRunner, ctx: Context, obj: Obj, instance: Instance, args: List[str]
) -> None:
    with patch.object(instances, "drop") as patched:
        result = runner.invoke(cli, ["instance", "drop"] + args, obj=obj)
    assert result.exit_code == 0, (result, result.output)
    patched.assert_called_once_with(ctx, instance)


def test_instance_status(runner: CliRunner, instance: Instance, obj: Obj) -> None:
    with patch.object(postgresql, "status", return_value=Status.not_running) as patched:
        result = runner.invoke(cli, ["instance", "status", instance.name], obj=obj)
    assert result.exit_code == 3, (result, result.output)
    assert result.stdout == "not running\n"
    patched.assert_called_once_with(instance)


@pytest.mark.parametrize(
    ["action", "kwargs"],
    [("start", {"foreground": False}), ("stop", {}), ("reload", {}), ("restart", {})],
)
def test_instance_operations(
    runner: CliRunner,
    instance: Instance,
    ctx: Context,
    obj: Obj,
    action: str,
    kwargs: Dict[str, bool],
) -> None:
    with patch.object(instances, action) as patched:
        result = runner.invoke(cli, ["instance", action, str(instance)], obj=obj)
    assert result.exit_code == 0, result
    patched.assert_called_once_with(ctx, instance, **kwargs)


def test_instance_exec(
    runner: CliRunner, instance: Instance, ctx: Context, obj: Obj
) -> None:
    with patch.object(instances, "exec") as instance_exec:
        r = runner.invoke(
            cli,
            ["instance", "exec", instance.name],
            obj=obj,
        )
    assert not instance_exec.called
    assert r.exit_code == 1
    assert r.stderr == "Error: no command given\n"

    with patch.object(instances, "exec") as instance_exec:
        runner.invoke(
            cli,
            ["instance", "exec", instance.name, "--", "psql", "-d", "test"],
            obj=obj,
        )
    instance_exec.assert_called_once_with(ctx, instance, ("psql", "-d", "test"))


def test_instance_env(
    runner: CliRunner, instance: Instance, ctx: Context, obj: Obj
) -> None:
    r = runner.invoke(
        cli,
        ["instance", "env", instance.name],
        obj=obj,
    )
    assert r.exit_code == 0, r
    bindir = instance.bindir
    path = os.environ["PATH"]
    expected = "\n".join(
        [
            f"PATH={bindir}:{path}",
            f"PGBACKREST_CONFIG_PATH={ctx.settings.prefix}/etc/pgbackrest",
            "PGBACKREST_STANZA=test-stanza",
            f"PGDATA={instance.datadir}",
            "PGHOST=/socks",
            f"PGPASSFILE={ctx.settings.postgresql.auth.passfile}",
            "PGPORT=999",
            "PGUSER=postgres",
            f"PSQLRC={instance.psqlrc}",
            f"PSQL_HISTORY={instance.psql_history}",
        ]
    )
    assert r.stdout.rstrip() == expected

    r = runner.invoke(
        cli,
        ["instance", "env", instance.name, "--output-format=json"],
        obj=obj,
    )
    json_r = json.loads(r.stdout)
    assert "PGDATA" in json_r and "PATH" in json_r
    assert r.exit_code == 0, r


def test_instance_logs(runner: CliRunner, instance: Instance, obj: Obj) -> None:
    result = runner.invoke(cli, ["instance", "logs", str(instance)], obj=obj)
    assert result.exit_code == 1, result
    assert (
        result.stderr
        == f"Error: file 'current_logfiles' for instance {instance} not found\n"
    )

    stderr_logpath = instance.datadir / "log" / "postgresql.log"
    stderr_logpath.parent.mkdir()
    stderr_logpath.write_text("log\nged\n")
    (instance.datadir / "current_logfiles").write_text(f"stderr {stderr_logpath}\n")
    result = runner.invoke(cli, ["instance", "logs", str(instance)], obj=obj)
    assert result.exit_code == 0, result.stderr
    assert result.output == "log\nged\n"


def test_instance_backup(runner: CliRunner, instance: Instance, obj: Obj) -> None:
    with patch.object(repo_path, "backup") as backup:
        result = runner.invoke(
            cli,
            ["instance", "backup", str(instance), "--type=diff"],
            obj=obj,
        )
    assert result.exit_code == 0, result
    assert backup.call_count == 1
    assert backup.call_args[1] == {"type": types.BackupType("diff")}


def test_instance_backups(
    runner: CliRunner, instance: Instance, settings: Settings, obj: Obj
) -> None:
    bck = interface.InstanceBackup(
        label="foo",
        size=12,
        repo_size=13,
        date_start=datetime.datetime(2012, 1, 1),
        date_stop=datetime.datetime(2012, 1, 2),
        type="incr",
        databases=["postgres", "prod"],
    )
    with patch.object(pgbackrest, "iter_backups", return_value=[bck]) as iter_backups:
        result = runner.invoke(
            cli,
            ["instance", "backups", str(instance)],
            obj=obj,
        )
    assert result.exit_code == 0, result
    assert iter_backups.call_count == 1

    assert [
        v.strip() for v in result.stdout.splitlines()[-3].split("│") if v.strip()
    ] == [
        "foo",
        "12.0B",
        "13.0B",
        "2012-01-01",
        "2012-01-02",
        "incr",
        "postgres,",
    ]

    assert [
        v.strip() for v in result.stdout.splitlines()[-2].split("│") if v.strip()
    ] == [
        "00:00:00",
        "00:00:00",
        "prod",
    ]

    with patch.object(pgbackrest, "iter_backups", return_value=[bck]) as iter_backups:
        result = runner.invoke(
            cli,
            ["instance", "backups", str(instance), "--output-format=json"],
            obj=obj,
        )
    assert result.exit_code == 0, result
    iter_backups.assert_called_once_with(instance, settings.pgbackrest)
    assert json.loads(result.stdout) == [
        {
            "databases": ["postgres", "prod"],
            "date_start": "2012-01-01T00:00:00",
            "date_stop": "2012-01-02T00:00:00",
            "label": "foo",
            "repo_size": 13,
            "size": 12,
            "type": "incr",
        }
    ]


def test_instance_restore(
    runner: CliRunner, instance: Instance, ctx: Context, obj: Obj
) -> None:
    with patch("pglift.postgresql.ctl.status", return_value=Status.running) as status:
        result = runner.invoke(
            cli,
            ["instance", "restore", str(instance)],
            obj=obj,
        )
    assert result.exit_code == 1, result
    assert "instance is running" in result.stderr
    status.assert_called_once_with(instance)

    with patch.object(pgbackrest, "restore") as restore:
        result = runner.invoke(
            cli,
            ["instance", "restore", str(instance), "--label=xyz"],
            obj=obj,
        )
    assert result.exit_code == 0, result
    assert restore.called_once_with(ctx, instance, label="xyz")


def test_instance_privileges(
    ctx: Context,
    obj: Obj,
    instance: Instance,
    runner: CliRunner,
    postgresql_running: MagicMock,
) -> None:
    with patch(
        "pglift.privileges.get",
        return_value=[
            interface.DefaultPrivilege(
                database="db2",
                schema="public",
                role="rol2",
                object_type="FUNCTION",
                privileges=["EXECUTE"],
            ),
        ],
    ) as privileges_get:
        result = runner.invoke(
            cli,
            [
                "instance",
                "privileges",
                str(instance),
                "--output-format=json",
                "-d",
                "db2",
                "-r",
                "rol2",
                "--default",
            ],
            obj=obj,
        )
    assert result.exit_code == 0, result.stdout
    privileges_get.assert_called_once_with(
        ctx, instance, databases=("db2",), roles=("rol2",), defaults=True
    )
    assert json.loads(result.stdout) == [
        {
            "database": "db2",
            "schema": "public",
            "role": "rol2",
            "object_type": "FUNCTION",
            "privileges": ["EXECUTE"],
        }
    ]


def test_instance_upgrade(
    ctx: Context, obj: Obj, instance: Instance, runner: CliRunner
) -> None:
    new_instance = MagicMock()
    newversion = next(iter(PostgreSQLVersion))
    with patch.object(
        instances, "upgrade", return_value=new_instance
    ) as upgrade, patch.object(instances, "start") as start:
        result = runner.invoke(
            cli,
            [
                "instance",
                "upgrade",
                str(instance),
                "--name=new",
                "--port=12",
                "--jobs=3",
                f"--version={newversion.value}",
            ],
            obj=obj,
        )
    assert result.exit_code == 0, result.stdout
    upgrade.assert_called_once_with(
        ctx, instance, version=newversion, name="new", port=12, jobs=3
    )
    start.assert_called_once_with(ctx, new_instance)


@pytest.mark.parametrize(
    "params, expected",
    [
        ([], ["port = 999", "unix_socket_directories = '/socks'"]),
        (["port"], ["port = 999"]),
        (["backslash_quote"], ["# backslash_quote = 'safe_encoding'"]),
    ],
    ids=["param=<none>", "param=port", "param=backslash_quote(commented)"],
)
def test_pgconf_show(
    runner: CliRunner,
    obj: Obj,
    instance: Instance,
    params: List[str],
    expected: List[str],
) -> None:
    result = runner.invoke(
        cli, ["pgconf", "-i", str(instance), "show"] + params, obj=obj
    )
    assert result.exit_code == 0, result.stderr
    assert result.stdout.strip() == "\n".join(expected)

    result = runner.invoke(
        cli, ["pgconf", "-i", str(instance), "show", "port"], obj=obj
    )
    assert result.exit_code == 0, result.stderr
    assert result.stdout.strip() == "\n".join(["port = 999"])


def test_pgconf_set_validate(runner: CliRunner, obj: Obj, instance: Instance) -> None:
    result = runner.invoke(
        cli,
        ["pgconf", "-i", str(instance), "set", "invalid"],
        obj=obj,
    )
    assert result.exit_code == 2
    assert "Error: Invalid value for '<PARAMETER>=<VALUE>...': invalid" in result.stderr


def test_pgconf_set(
    runner: CliRunner, ctx: Context, obj: Obj, instance: Instance
) -> None:
    manifest = interface.Instance(
        name="test", settings={"port": 123, "cluster_name": "unittests"}
    )
    with patch.object(instances, "_get", return_value=manifest) as _get, patch.object(
        instances, "configure", return_value={"foo": ("baz", "bar")}
    ) as configure:
        result = runner.invoke(
            cli,
            [
                "pgconf",
                "-i",
                str(instance),
                "set",
                "cluster_name=unittests",
                "foo=bar",
            ],
            obj=obj,
        )
    assert result.exit_code == 0
    _get.assert_called_once_with(ctx, instance)
    manifest.settings["foo"] = "bar"
    configure.assert_called_once_with(ctx, manifest)
    assert "foo: baz -> bar" in result.stderr

    with patch.object(instances, "_get", return_value=manifest) as _get, patch.object(
        instances,
        "configure",
        return_value={"bonjour_name": ("test", "changed")},
    ) as configure:
        result = runner.invoke(
            cli,
            [
                "pgconf",
                "-i",
                str(instance),
                "set",
                "foo=bar",
                "bonjour_name=changed",
            ],
            obj=obj,
        )
    assert result.exit_code == 0
    _get.assert_called_once_with(ctx, instance)
    manifest.settings["bonjour_name"] = "changed"
    configure.assert_called_once_with(ctx, manifest)
    assert "bonjour_name: test -> changed" in result.stderr
    assert "foo: baz -> bar" not in result.stderr
    assert "changes in 'foo' not applied" in result.stderr
    assert "\n hint:" in result.stderr


def test_pgconf_remove(
    runner: CliRunner, ctx: Context, obj: Obj, instance: Instance
) -> None:
    result = runner.invoke(
        cli,
        ["pgconf", "-i", str(instance), "remove", "fsync"],
        obj=obj,
    )
    assert result.exit_code == 1
    assert "'fsync' not found in managed configuration" in result.stderr

    manifest = interface.Instance(
        name="test",
        settings={
            "unix_socket_directories": "/socks",
            "cluster_name": "unittests",
        },
    )
    with patch.object(instances, "_get", return_value=manifest) as _get, patch.object(
        instances,
        "configure",
        return_value={"unix_socket_directories": ("/socks", None)},
    ) as configure:
        result = runner.invoke(
            cli,
            ["pgconf", f"--instance={instance}", "remove", "unix_socket_directories"],
            obj=obj,
        )
    assert result.exit_code == 0, result.stderr
    assert "unix_socket_directories: /socks -> None" in result.stderr
    _get.assert_called_once_with(ctx, instance)
    assert "unix_socket_directories" not in manifest.settings
    configure.assert_called_once_with(ctx, manifest)


def test_pgconf_edit(
    runner: CliRunner, ctx: Context, obj: Obj, instance: Instance, postgresql_conf: str
) -> None:
    manifest = interface.Instance(
        name="test",
        settings={
            "unix_socket_directories": "/socks",
            "cluster_name": "unittests",
        },
    )
    with patch("click.edit", return_value="bonjour = bonsoir\n") as edit, patch.object(
        instances, "_get", return_value=manifest
    ) as _get, patch.object(
        instances, "configure", return_value={"bonjour": ("on", "'matin")}
    ) as configure:
        result = runner.invoke(
            cli,
            ["pgconf", f"--instance={instance}", "edit"],
            obj=obj,
        )
    assert result.exit_code == 0, result.stderr
    _get.assert_called_once_with(ctx, instance)
    edit.assert_called_once_with(text=postgresql_conf)
    assert manifest.settings == {"bonjour": "bonsoir"}
    configure.assert_called_once_with(ctx, manifest)
    assert result.stderr == "bonjour: on -> 'matin\n"

    with patch("click.edit", return_value=None) as edit, patch.object(
        instances, "_get"
    ) as _get, patch.object(instances, "configure") as configure:
        result = runner.invoke(
            cli, ["pgconf", f"--instance={instance}", "edit"], obj=obj
        )
    assert not _get.called
    assert not configure.called
    assert result.stderr == "no change\n"


def test_role_create(
    ctx: Context,
    obj: Obj,
    instance: Instance,
    runner: CliRunner,
    postgresql_running: MagicMock,
) -> None:
    with patch.object(roles, "exists", return_value=False) as exists, patch.object(
        roles, "apply"
    ) as apply:
        result = runner.invoke(
            cli,
            [
                "role",
                f"--instance={instance.version}/{instance.name}",
                "create",
                "rob",
                "--password=ert",
                "--pgpass",
                "--login",
                "--no-inherit",
                "--in-role=monitoring",
                "--in-role=backup",
            ],
            obj=obj,
        )
    assert result.exit_code == 0, result
    exists.assert_called_once_with(ctx, instance, "rob")
    role = interface.Role.parse_obj(
        {
            "name": "rob",
            "password": "ert",
            "login": True,
            "pgpass": True,
            "inherit": False,
            "in_roles": ["monitoring", "backup"],
        }
    )
    apply.assert_called_once_with(ctx, instance, role)
    postgresql_running.assert_called_once_with(ctx, instance)

    postgresql_running.reset_mock()

    with patch.object(roles, "exists", return_value=True) as exists:
        result = runner.invoke(
            cli,
            [
                "role",
                f"--instance={instance.version}/{instance.name}",
                "create",
                "bob",
            ],
            obj=obj,
        )
    assert result.exit_code == 1
    assert "role already exists" in result.stderr
    exists.assert_called_once_with(ctx, instance, "bob")
    postgresql_running.assert_called_once_with(ctx, instance)


def test_role_alter(
    runner: CliRunner,
    ctx: Context,
    obj: Obj,
    instance: Instance,
    postgresql_running: MagicMock,
) -> None:
    actual = interface.Role(name="alterme", connection_limit=3, in_roles=["pg_monitor"])
    altered = interface.Role(
        name="alterme",
        connection_limit=30,
        pgpass=True,
        password="blah",
        login=True,
        inherit=False,
        in_roles=["pg_monitor"],
    )

    with patch.object(roles, "get", return_value=actual) as get, patch.object(
        roles, "apply"
    ) as apply:
        result = runner.invoke(
            cli,
            [
                "role",
                "-i",
                str(instance),
                "alter",
                "alterme",
                "--connection-limit=30",
                "--pgpass",
                "--password=blah",
                "--login",
                "--no-inherit",
            ],
            obj=obj,
        )
    get.assert_called_once_with(ctx, instance, "alterme")
    apply.assert_called_once_with(ctx, instance, altered)
    assert result.exit_code == 0, result.output


def test_role_schema(runner: CliRunner) -> None:
    result = runner.invoke(cli, ["role", "--schema"])
    schema = json.loads(result.output)
    assert schema["title"] == "Role"
    assert schema["description"] == "PostgreSQL role"


def test_role_apply(
    runner: CliRunner,
    tmp_path: Path,
    ctx: Context,
    obj: Obj,
    instance: Instance,
    postgresql_running: MagicMock,
) -> None:
    manifest = tmp_path / "manifest.yml"
    m = {"name": "roltest", "pgpass": True}
    content = yaml.dump(m)
    manifest.write_text(content)

    result = runner.invoke(
        cli,
        [
            "role",
            "-i",
            str(instance),
            "apply",
            "-f",
            str(manifest),
            "-o",
            "json",
            "--dry-run",
        ],
        obj=obj,
    )
    assert result.exit_code == 0
    assert json.loads(result.stdout) == {"change_state": None}

    apply_result = interface.ApplyResult(
        change_state=interface.ApplyChangeState.created
    )
    with patch.object(roles, "apply", return_value=apply_result) as apply:
        result = runner.invoke(
            cli,
            [
                "role",
                "-i",
                str(instance),
                "apply",
                "-f",
                str(manifest),
                "--output-format=json",
            ],
            obj=obj,
        )
    assert result.exit_code == 0
    assert json.loads(result.stdout) == {"change_state": "created"}
    apply.assert_called_once_with(ctx, instance, interface.Role.parse_obj(m))
    postgresql_running.assert_called_once_with(ctx, instance)


def test_role_get(
    runner: CliRunner,
    ctx: Context,
    obj: Obj,
    instance: Instance,
    postgresql_running: MagicMock,
) -> None:
    with patch.object(
        roles, "get", side_effect=exceptions.RoleNotFound("absent")
    ) as get:
        result = runner.invoke(
            cli,
            ["role", "-i", str(instance), "get", "absent"],
            obj=obj,
        )
    get.assert_called_once_with(ctx, instance, "absent")
    postgresql_running.assert_called_once_with(ctx, instance)
    assert result.exit_code == 1, (result, result.output)
    assert result.stderr.strip() == "Error: role 'absent' not found"

    postgresql_running.reset_mock()

    with patch.object(
        roles,
        "get",
        return_value=interface.Role.parse_obj(
            {
                "name": "present",
                "pgpass": True,
                "has_password": True,
                "inherit": False,
                "validity": datetime.datetime(2022, 1, 1),
                "connection_limit": 5,
                "in_roles": ["observers", "monitoring"],
            }
        ),
    ) as get:
        result = runner.invoke(
            cli,
            ["role", "-i", instance.name, "get", "present", "--output-format=json"],
            obj=obj,
        )
    get.assert_called_once_with(ctx, instance, "present")
    postgresql_running.assert_called_once_with(ctx, instance)
    assert result.exit_code == 0
    assert json.loads(result.stdout) == {
        "name": "present",
        "pgpass": True,
        "has_password": True,
        "inherit": False,
        "login": False,
        "superuser": False,
        "createdb": False,
        "createrole": False,
        "replication": False,
        "connection_limit": 5,
        "validity": "2022-01-01T00:00:00",
        "in_roles": ["observers", "monitoring"],
    }


def test_role_list(
    runner: CliRunner,
    ctx: Context,
    obj: Obj,
    instance: Instance,
    postgresql_running: MagicMock,
) -> None:
    with patch.object(
        roles,
        "list",
        return_value=[
            interface.Role(
                name="toto",
                connection_limit=30,
                password="blah",
                login=True,
                inherit=False,
                in_roles=["pg_read_all_data", "pg_read_all_settings"],
            )
        ],
    ) as list_:
        result = runner.invoke(
            cli,
            [
                "role",
                "-i",
                instance.name,
                "list",
                "--output-format=json",
            ],
            obj=obj,
        )
    list_.assert_called_once_with(ctx, instance)
    postgresql_running.assert_called_once_with(ctx, instance)
    assert result.exit_code == 0, result.stdout
    rls = json.loads(result.stdout)
    assert rls == [
        {
            "connection_limit": 30,
            "has_password": True,
            "in_roles": ["pg_read_all_data", "pg_read_all_settings"],
            "inherit": False,
            "login": True,
            "name": "toto",
            "replication": False,
            "superuser": False,
            "createdb": False,
            "createrole": False,
            "validity": None,
        }
    ]


def test_role_drop(
    runner: CliRunner,
    ctx: Context,
    obj: Obj,
    instance: Instance,
    postgresql_running: MagicMock,
) -> None:
    with patch.object(
        roles, "drop", side_effect=exceptions.RoleNotFound("bar")
    ) as drop:
        result = runner.invoke(
            cli,
            ["role", f"--instance={instance}", "drop", "bar", "--drop-owned"],
            obj=obj,
        )
    drop.assert_called_once_with(
        ctx, instance, interface.RoleDropped(name="bar", drop_owned=True)
    )
    postgresql_running.assert_called_once_with(ctx, instance)
    assert result.exit_code == 1
    assert result.stderr.splitlines()[-1] == "Error: role 'bar' not found"

    postgresql_running.reset_mock()

    with patch.object(roles, "drop") as drop:
        result = runner.invoke(
            cli,
            ["role", "-i", str(instance), "drop", "foo"],
            obj=obj,
        )
    drop.assert_called_once_with(ctx, instance, interface.RoleDropped(name="foo"))
    postgresql_running.assert_called_once_with(ctx, instance)
    assert result.exit_code == 0

    result = runner.invoke(
        cli,
        [
            "role",
            "drop",
            "foo",
            "--drop-owned",
            "--reassign-owned=bar",
        ],
        obj=obj,
    )
    assert result.exit_code == 2
    assert (
        "Error: Invalid value for '--reassign-owned': drop_owned and reassign_owned are mutually exclusive"
        in result.stderr
    )


def test_role_privileges(
    ctx: Context,
    obj: Obj,
    instance: Instance,
    runner: CliRunner,
    postgresql_running: MagicMock,
) -> None:
    with patch(
        "pglift.privileges.get",
        return_value=[
            interface.DefaultPrivilege(
                database="db2",
                schema="public",
                role="rol2",
                object_type="FUNCTION",
                privileges=["EXECUTE"],
            ),
        ],
    ) as privileges_get, patch.object(roles, "get") as roles_get:
        result = runner.invoke(
            cli,
            [
                "role",
                "-i",
                str(instance),
                "privileges",
                "rol2",
                "--output-format=json",
                "-d",
                "db2",
                "--default",
            ],
            obj=obj,
        )
    assert result.exit_code == 0, result.stdout
    privileges_get.assert_called_once_with(
        ctx, instance, databases=("db2",), roles=("rol2",), defaults=True
    )
    roles_get.assert_called_once_with(ctx, instance, "rol2")
    assert json.loads(result.stdout) == [
        {
            "database": "db2",
            "schema": "public",
            "role": "rol2",
            "object_type": "FUNCTION",
            "privileges": ["EXECUTE"],
        }
    ]


def test_database_create(
    ctx: Context,
    obj: Obj,
    instance: Instance,
    runner: CliRunner,
    postgresql_running: MagicMock,
) -> None:
    with patch.object(databases, "exists", return_value=False) as exists, patch.object(
        databases, "apply"
    ) as apply:
        result = runner.invoke(
            cli,
            [
                "database",
                f"--instance={instance.version}/{instance.name}",
                "create",
                "db_test1",
            ],
            obj=obj,
        )
    assert result.exit_code == 0, result
    exists.assert_called_once_with(ctx, instance, "db_test1")
    database = interface.Database.parse_obj({"name": "db_test1"})
    apply.assert_called_once_with(ctx, instance, database)
    postgresql_running.assert_called_once_with(ctx, instance)

    postgresql_running.reset_mock()

    with patch.object(databases, "exists", return_value=False) as exists, patch.object(
        databases, "apply"
    ) as apply:
        result = runner.invoke(
            cli,
            [
                "database",
                f"--instance={instance.version}/{instance.name}",
                "create",
                "db_test2",
                "--clone-from",
                "postgres://postgres@localhost:5456/db_test1",
            ],
            obj=obj,
        )

    assert result.exit_code == 0, result
    exists.assert_called_with(ctx, instance, "db_test2")
    database = interface.Database.parse_obj(
        {
            "name": "db_test2",
            "clone_from": "postgres://postgres@localhost:5456/db_test1",
        }
    )
    apply.assert_called_with(ctx, instance, database)
    postgresql_running.assert_called_once_with(ctx, instance)

    postgresql_running.reset_mock()

    with patch.object(databases, "exists", return_value=True) as exists:
        result = runner.invoke(
            cli,
            [
                "database",
                f"--instance={instance.version}/{instance.name}",
                "create",
                "db_test2",
            ],
            obj=obj,
        )
    assert result.exit_code == 1
    assert "database already exists" in result.stderr
    exists.assert_called_once_with(ctx, instance, "db_test2")
    postgresql_running.assert_called_once_with(ctx, instance)


def test_database_alter(
    runner: CliRunner,
    ctx: Context,
    obj: Obj,
    instance: Instance,
    postgresql_running: MagicMock,
) -> None:
    actual = interface.Database(name="alterme")
    altered = interface.Database(name="alterme", owner="dba")

    with patch.object(databases, "get", return_value=actual) as get, patch.object(
        databases, "apply"
    ) as apply:
        result = runner.invoke(
            cli,
            [
                "database",
                f"--instance={instance}",
                "alter",
                "alterme",
                "--owner=dba",
            ],
            obj=obj,
        )
    get.assert_called_once_with(ctx, instance, "alterme")
    apply.assert_called_once_with(ctx, instance, altered)
    assert result.exit_code == 0, result.output


def test_database_schema(runner: CliRunner) -> None:
    result = runner.invoke(cli, ["database", "--schema"])
    schema = json.loads(result.output)
    assert schema["title"] == "Database"
    assert schema["description"] == "PostgreSQL database"


def test_database_apply(
    runner: CliRunner,
    tmp_path: Path,
    ctx: Context,
    obj: Obj,
    instance: Instance,
    postgresql_running: MagicMock,
) -> None:
    manifest = tmp_path / "manifest.yml"
    m = {"name": "dbtest"}
    content = yaml.dump(m)
    manifest.write_text(content)

    result = runner.invoke(
        cli,
        [
            "database",
            "-i",
            str(instance),
            "apply",
            "-f",
            str(manifest),
            "-o",
            "json",
            "--dry-run",
        ],
        obj=obj,
    )
    assert result.exit_code == 0
    assert json.loads(result.stdout) == {"change_state": None}

    apply_result = interface.ApplyResult(
        change_state=interface.ApplyChangeState.created
    )
    with patch.object(databases, "apply", return_value=apply_result) as apply:
        result = runner.invoke(
            cli,
            [
                "database",
                "-i",
                str(instance),
                "apply",
                "-f",
                str(manifest),
                "--output-format=json",
            ],
            obj=obj,
        )
    assert result.exit_code == 0
    apply.assert_called_once_with(ctx, instance, interface.Database.parse_obj(m))
    assert json.loads(result.stdout) == {"change_state": "created"}
    postgresql_running.assert_called_once_with(ctx, instance)


def test_database_get(
    runner: CliRunner,
    ctx: Context,
    obj: Obj,
    instance: Instance,
    postgresql_running: MagicMock,
) -> None:
    with patch.object(
        databases, "get", side_effect=exceptions.DatabaseNotFound("absent")
    ) as get:
        result = runner.invoke(
            cli,
            ["database", "-i", str(instance), "get", "absent"],
            obj=obj,
        )
    get.assert_called_once_with(ctx, instance, "absent")
    postgresql_running.assert_called_once_with(ctx, instance)
    assert result.exit_code == 1
    assert result.stderr.strip() == "Error: database 'absent' not found"

    postgresql_running.reset_mock()

    with patch.object(
        databases,
        "get",
        return_value=interface.Database(name="present", owner="dba"),
    ) as get:
        result = runner.invoke(
            cli,
            ["database", "-i", instance.name, "get", "present", "-o", "json"],
            obj=obj,
        )
    get.assert_called_once_with(ctx, instance, "present")
    postgresql_running.assert_called_once_with(ctx, instance)
    assert result.exit_code == 0
    assert json.loads(result.stdout) == {
        "extensions": [],
        "schemas": [],
        "name": "present",
        "owner": "dba",
        "settings": None,
        "clone_from": None,
    }


def test_database_list(
    runner: CliRunner,
    ctx: Context,
    obj: Obj,
    instance: Instance,
    postgresql_running: MagicMock,
) -> None:
    with patch.object(
        databases,
        "list",
        return_value=[
            interface.DetailedDatabase(
                name="template1",
                owner="postgres",
                encoding="UTF8",
                collation="C",
                ctype="C",
                acls=["=c/postgres", "postgres=CTc/postgres"],
                size=8167939,
                description="default template for new databases",
                tablespace=interface.Tablespace(
                    name="pg_default", location="", size=41011771
                ),
            )
        ],
    ) as list_:
        result = runner.invoke(
            cli,
            [
                "database",
                "-i",
                instance.name,
                "list",
                "template1",
                "--output-format=json",
            ],
            obj=obj,
        )
    list_.assert_called_once_with(ctx, instance, dbnames=("template1",))
    postgresql_running.assert_called_once_with(ctx, instance)
    assert result.exit_code == 0, result.stdout
    dbs = json.loads(result.stdout)
    assert dbs == [
        {
            "acls": ["=c/postgres", "postgres=CTc/postgres"],
            "collation": "C",
            "ctype": "C",
            "description": "default template for new databases",
            "encoding": "UTF8",
            "name": "template1",
            "owner": "postgres",
            "size": 8167939,
            "tablespace": {"location": "", "name": "pg_default", "size": 41011771},
        }
    ]


def test_database_drop(
    runner: CliRunner,
    ctx: Context,
    obj: Obj,
    instance: Instance,
    postgresql_running: MagicMock,
) -> None:
    with patch.object(
        databases, "drop", side_effect=exceptions.DatabaseNotFound("bar")
    ) as drop:
        result = runner.invoke(
            cli,
            ["database", "-i", str(instance), "drop", "foo"],
            obj=obj,
        )
    drop.assert_called_once_with(ctx, instance, interface.DatabaseDropped(name="foo"))
    postgresql_running.assert_called_once_with(ctx, instance)
    assert result.exit_code == 1
    assert result.stderr.splitlines()[-1] == "Error: database 'bar' not found"

    postgresql_running.reset_mock()

    with patch.object(databases, "drop") as drop:
        result = runner.invoke(
            cli,
            ["database", "-i", str(instance), "drop", "foo"],
            obj=obj,
        )
    drop.assert_called_once_with(ctx, instance, interface.DatabaseDropped(name="foo"))
    postgresql_running.assert_called_once_with(ctx, instance)
    assert result.exit_code == 0


def test_database_run(
    runner: CliRunner,
    ctx: Context,
    obj: Obj,
    instance: Instance,
    postgresql_running: MagicMock,
) -> None:
    with patch.object(databases, "run", return_value={"db": [{"name": "bob"}]}) as run:
        result = runner.invoke(
            cli,
            [
                "database",
                "-i",
                str(instance),
                "run",
                "--output-format=json",
                "-d",
                "db",
                "some sql",
            ],
            obj=obj,
        )
    run.assert_called_once_with(
        ctx, instance, "some sql", dbnames=("db",), exclude_dbnames=()
    )
    postgresql_running.assert_called_once_with(ctx, instance)
    assert result.exit_code == 0, result.stderr
    dbs = json.loads(result.stdout)
    assert dbs == {"db": [{"name": "bob"}]}


def test_database_run_programmingerror(
    runner: CliRunner,
    ctx: Context,
    obj: Obj,
    instance: Instance,
    postgresql_running: MagicMock,
) -> None:
    with patch.object(
        databases, "run", side_effect=psycopg.ProgrammingError("bingo")
    ) as run:
        result = runner.invoke(
            cli,
            ["database", "-i", str(instance), "run", "some sql"],
            obj=obj,
        )
    run.assert_called_once_with(
        ctx, instance, "some sql", dbnames=(), exclude_dbnames=()
    )
    assert result.exit_code == 1
    assert result.stderr == "Error: bingo\n"


def test_database_privileges(
    ctx: Context,
    obj: Obj,
    instance: Instance,
    runner: CliRunner,
    postgresql_running: MagicMock,
) -> None:
    with patch(
        "pglift.privileges.get",
        return_value=[
            interface.DefaultPrivilege(
                database="db2",
                schema="public",
                role="rol2",
                object_type="FUNCTION",
                privileges=["EXECUTE"],
            ),
        ],
    ) as privileges_get, patch.object(databases, "get") as databases_get:
        result = runner.invoke(
            cli,
            [
                "database",
                "-i",
                str(instance),
                "privileges",
                "db2",
                "--output-format=json",
                "-r",
                "rol2",
                "--default",
            ],
            obj=obj,
        )
    assert result.exit_code == 0, result.stdout
    privileges_get.assert_called_once_with(
        ctx, instance, databases=("db2",), roles=("rol2",), defaults=True
    )
    databases_get.assert_called_once_with(ctx, instance, "db2")
    assert json.loads(result.stdout) == [
        {
            "database": "db2",
            "schema": "public",
            "role": "rol2",
            "object_type": "FUNCTION",
            "privileges": ["EXECUTE"],
        }
    ]


def test_database_dump(
    runner: CliRunner,
    ctx: Context,
    obj: Obj,
    instance: Instance,
    postgresql_running: MagicMock,
) -> None:
    with patch.object(
        databases, "dump", side_effect=exceptions.DatabaseNotFound("bar")
    ) as dump:
        result = runner.invoke(
            cli,
            ["database", "-i", str(instance), "dump", "bar"],
            obj=obj,
        )
    dump.assert_called_once_with(ctx, instance, "bar")
    postgresql_running.assert_called_once_with(ctx, instance)
    assert result.exit_code == 1
    assert result.stderr.splitlines()[-1] == "Error: database 'bar' not found"

    postgresql_running.reset_mock()

    with patch.object(databases, "dump") as dump:
        result = runner.invoke(
            cli,
            ["database", "-i", str(instance), "dump", "foo"],
            obj=obj,
        )
    dump.assert_called_once_with(ctx, instance, "foo")
    postgresql_running.assert_called_once_with(ctx, instance)
    assert result.exit_code == 0


def test_database_dumps(
    runner: CliRunner, ctx: Context, obj: Obj, instance: Instance
) -> None:
    d = datetime.datetime(2002, 3, 11)
    with patch.object(
        databases,
        "list_dumps",
        return_value=[interface.DatabaseDump.build(dbname="mydb", date=str(d))],
    ) as dumps:
        result = runner.invoke(
            cli,
            ["database", "-i", str(instance), "dumps", "mydb", "--output-format=json"],
            obj=obj,
        )
    dumps.assert_called_once_with(ctx, instance, dbnames=("mydb",))
    assert result.exit_code == 0
    assert json.loads(result.output)[0]["id"].startswith("mydb_")
    assert json.loads(result.output)[0]["dbname"] == "mydb"
    assert json.loads(result.output)[0]["date"] == d.isoformat()


def test_database_restore(
    runner: CliRunner,
    ctx: Context,
    obj: Obj,
    instance: Instance,
    postgresql_running: MagicMock,
) -> None:
    dump_id = "mydb_abcdef"
    with patch.object(
        databases,
        "restore",
        side_effect=exceptions.DatabaseDumpNotFound(dump_id),
    ) as restore:
        result = runner.invoke(
            cli,
            ["database", "-i", str(instance), "restore", dump_id],
            obj=obj,
        )
    restore.assert_called_once_with(ctx, instance, dump_id, None)
    postgresql_running.assert_called_once_with(ctx, instance)
    assert result.exit_code == 1
    assert result.stderr.splitlines()[-1] == f"Error: dump '{dump_id}' not found"

    postgresql_running.reset_mock()
    with patch.object(databases, "restore") as restore:
        result = runner.invoke(
            cli,
            ["database", "-i", str(instance), "restore", dump_id],
            obj=obj,
        )
    restore.assert_called_once_with(ctx, instance, dump_id, None)
    postgresql_running.assert_called_once_with(ctx, instance)
    assert result.exit_code == 0

    postgresql_running.reset_mock()
    with patch.object(databases, "restore") as restore:
        result = runner.invoke(
            cli,
            ["database", "-i", str(instance), "restore", dump_id, "newdb"],
            obj=obj,
        )
    restore.assert_called_once_with(ctx, instance, dump_id, "newdb")
    postgresql_running.assert_called_once_with(ctx, instance)
    assert result.exit_code == 0


def test_postgres(
    runner: CliRunner, instance: Instance, obj: Obj, settings: Settings
) -> None:
    result = runner.invoke(postgres_cli, ["no-suchinstance"], obj=obj)
    assert result.exit_code == 2
    assert "Invalid value for 'INSTANCE': 'no' is not a valid" in result.stderr

    result = runner.invoke(postgres_cli, [instance.name], obj=obj)
    assert result.exit_code == 2
    assert (
        "Invalid value for 'INSTANCE': invalid qualified name 'test'" in result.stderr
    )

    with patch("pglift.cli.postgres.execute_program") as p:
        result = runner.invoke(
            postgres_cli, [f"{instance.version}-{instance.name}"], obj=obj
        )
    assert result.exit_code == 0
    p.assert_called_once_with(
        [str(instance.bindir / "postgres"), "-D", str(instance.datadir)]
    )


@pytest.mark.parametrize(
    ("action", "kwargs"),
    [("start", {"foreground": False}), ("stop", {})],
)
def test_postgres_exporter_start_stop(
    runner: CliRunner,
    ctx: Context,
    obj: Obj,
    instance: Instance,
    action: str,
    kwargs: Dict[str, bool],
) -> None:
    with patch.object(prometheus_impl, action) as patched:
        result = runner.invoke(
            postgres_exporter_cli,
            [action, instance.qualname],
            obj=obj,
        )
    assert result.exit_code == 0, result.stderr
    service = instance.service(Service)
    patched.assert_called_once_with(ctx, service, **kwargs)


def test_postgres_exporter_schema(runner: CliRunner, obj: Obj) -> None:
    result = runner.invoke(postgres_exporter_cli, ["--schema"], obj=obj)
    schema = json.loads(result.output)
    assert schema["title"] == "PostgresExporter"
    assert schema["description"] == "Prometheus postgres_exporter service."


def test_postgres_exporter_apply(
    runner: CliRunner, tmp_path: Path, ctx: Context, obj: Obj
) -> None:
    manifest = tmp_path / "manifest.yml"
    content = yaml.dump({"name": "123-exp", "dsn": "dbname=monitoring", "port": 123})
    manifest.write_text(content)

    result = runner.invoke(
        postgres_exporter_cli,
        ["apply", "-f", str(manifest), "-o", "json", "--dry-run"],
        obj=obj,
    )
    assert result.exit_code == 0
    assert json.loads(result.stdout) == {"change_state": None}

    with patch.object(
        prometheus_impl,
        "apply",
        return_value=interface.ApplyResult(
            change_state=interface.ApplyChangeState.created
        ),
    ) as apply:
        result = runner.invoke(
            postgres_exporter_cli,
            ["apply", "-f", str(manifest), "-o", "json"],
            obj=obj,
        )
    assert result.exit_code == 0
    apply.assert_called_once_with(
        ctx,
        prometheus.PostgresExporter(name="123-exp", dsn="dbname=monitoring", port=123),
        ctx.settings.prometheus,
    )
    assert json.loads(result.stdout) == {"change_state": "created"}


def test_postgres_exporter_install(runner: CliRunner, ctx: Context, obj: Obj) -> None:
    with patch.object(prometheus_impl, "apply") as apply:
        result = runner.invoke(
            postgres_exporter_cli,
            ["install", "123-exp", "dbname=monitoring", "123"],
            obj=obj,
        )
    assert result.exit_code == 0
    apply.assert_called_once_with(
        ctx,
        prometheus.PostgresExporter(name="123-exp", dsn="dbname=monitoring", port=123),
        ctx.settings.prometheus,
    )


def test_postgres_exporter_uninstall(runner: CliRunner, ctx: Context, obj: Obj) -> None:
    with patch.object(prometheus_impl, "drop") as drop:
        result = runner.invoke(
            postgres_exporter_cli,
            ["uninstall", "123-exp"],
            obj=obj,
        )
    assert result.exit_code == 0
    drop.assert_called_once_with(ctx, "123-exp")


def test_pgbackrest(
    runner: CliRunner,
    ctx: Context,
    obj: Obj,
    instance: Instance,
    pgbackrest_execpath: Path,
) -> None:
    with patch("pglift.cmd.run") as run:
        result = runner.invoke(
            pgbackrest_cli,
            ["-i", str(instance), "info", "--output-format=json"],
            obj=obj,
        )
    assert result.exit_code == 0, result.stderr
    run.assert_called_once_with(
        [
            str(pgbackrest_execpath),
            f"--config-path={ctx.settings.prefix}/etc/pgbackrest",
            "--log-level-stderr=info",
            "--stanza=test-stanza",
            "info",
            "--output-format=json",
        ],
        capture_output=False,
        check=True,
    )
