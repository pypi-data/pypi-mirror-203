from pathlib import Path
from typing import Optional

import attr
from pydantic import Field, SecretStr

from .. import types


@attr.s(auto_attribs=True, frozen=True, slots=True)
class Service:
    """A pgbackrest service bound to a PostgreSQL instance."""

    stanza: str
    """Name of the stanza"""

    path: Path
    """Path to configuration file for this stanza"""

    index: int = 1
    """index of pg-path option in the stanza"""


class ServiceManifest(types.ServiceManifest, service_name="pgbackrest"):
    class RestoreManifest(types.Manifest):
        stanza: str = Field(
            description="pgBackRest stanza of the primary instance to restore from."
        )

    stanza: str = Field(
        description=(
            "Name of pgBackRest stanza. "
            "Something describing the actual function of the instance, such as 'app'."
        ),
        readOnly=True,
    )
    password: Optional[SecretStr] = Field(
        default=None,
        description="Password of PostgreSQL role for pgBackRest.",
        exclude=True,
    )
    restore: Optional[RestoreManifest] = Field(
        default=None,
        description="Options used when restoring a backup.",
        readOnly=True,
        writeOnly=True,
        exclude=True,
    )
