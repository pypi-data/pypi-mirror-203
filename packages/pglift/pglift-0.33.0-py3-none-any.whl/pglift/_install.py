from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .pm import PluginManager
    from .settings import Settings


def do(
    pm: "PluginManager",
    settings: "Settings",
    env: Optional[str] = None,
    header: str = "",
) -> None:
    pm.hook.site_configure_install(settings=settings, pm=pm, header=header, env=env)


def undo(pm: "PluginManager", settings: "Settings") -> None:
    pm.hook.site_configure_uninstall(settings=settings, pm=pm)
