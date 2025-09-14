"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Annotated
from typing import Any
from typing import Optional

from encommon.types import BaseModel

from pydantic import Field
from pydantic import field_validator

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
        Optional[list[NamedZoneParams]],
        Field(None,
              description='Specific DNS zone parameters')]


    @field_validator(
        'access',
        mode='before')
    @classmethod
    def parse_access(
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


    @field_validator(
        'zones',
        mode='before')
    @classmethod
    def parse_zones(
        # NOCVR
        cls,
        value: Any,  # noqa: ANN401
    ) -> Any:  # noqa: ANN401
        """
        Perform advanced validation on the parameters provided.
        """

        if (isinstance(value, list)
                or value is None):
            return value

        model = NamedZoneParams

        returned: list[NamedZoneParams] = []


        assert isinstance(value, dict)

        items = value.items()

        for key, value in items:

            value = dict(value)
            name = value.get('name')

            if name is None:
                value['name'] = key

            item = model(**value)

            returned.append(item)


        return returned
