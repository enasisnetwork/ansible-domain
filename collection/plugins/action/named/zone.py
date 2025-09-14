"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Annotated
from typing import Any

from encommon.types import BaseModel

from pydantic import Field
from pydantic import field_validator



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
        list[str],
        Field(...,
              description='Specific forwarders for recursion',
              min_length=1)]


    @field_validator(
        'forward',
        mode='before')
    @classmethod
    def parse_forward(
        # NOCVR
        cls,
        value: Any,  # noqa: ANN401
    ) -> Any:  # noqa: ANN401
        """
        Perform advanced validation on the parameters provided.
        """

        if isinstance(value, str):
            return [value]

        return value
