"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Annotated
from typing import Optional

from encommon.types import BaseModel

from pydantic import Field

from .zone import NamedZoneParams



class NamedHorizonParams(BaseModel, extra='forbid'):
    """
    Process and validate the Orche configuration parameters.
    """

    name: Annotated[
        str,
        Field(...,
              description='Proper name for the DNS view',
              min_length=1)]

    access: Annotated[
        Optional[list[str]],
        Field(None,
              description='Horizon restriction access list',
              min_length=1)]

    recurse: Annotated[
        bool,
        Field(False,
              description='Whether recursion is permitted')]

    zones: Annotated[
        Optional[dict[str, NamedZoneParams]],
        Field(None,
              description='Specific DNS zone parameters')]
