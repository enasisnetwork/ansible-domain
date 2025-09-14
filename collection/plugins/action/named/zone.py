"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Annotated
from typing import Optional

from encommon.types import BaseModel

from pydantic import Field



class NamedZoneParams(BaseModel, extra='forbid'):
    """
    Process and validate the Orche configuration parameters.
    """

    name: Annotated[
        str,
        Field(...,
              description='Proper name for the DNS zone',
              min_length=1)]

    forward: Annotated[
        Optional[list[str]],
        Field(None,
              description='Specific forwarders for recursion',
              min_length=1)]
