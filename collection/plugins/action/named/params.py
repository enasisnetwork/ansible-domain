"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



# NOTE Do not forget roles/params.yml
# NOTE Remember to update README file



from typing import Annotated
from typing import Optional

from ansible.plugins.action import ActionBase  # type: ignore

from encommon.types import BaseModel
from encommon.types import DictStrAny
from encommon.types import sort_dict

from pydantic import Field

from .horizon import NamedHorizonParams



class RoleParams(BaseModel, extra='forbid'):
    """
    Process and validate the Orche configuration parameters.
    """

    forward: Annotated[
        Optional[list[str]],
        Field(None,
              description='Default forwarders for recursion',
              min_length=1)]

    access: Annotated[
        Optional[dict[str, list[str]]],
        Field(None,
              description='Horizon restriction access list',
              min_length=1)]

    horizon: Annotated[
        Optional[dict[str, NamedHorizonParams]],
        Field(None,
              description='Configuraiton for split horizon')]



class ActionModule(ActionBase):  # type: ignore
    """
    Perform whatever operation is associated with the file.
    """


    def run(
        # NOCVR
        self,
        tmp: Optional[str] = None,
        task_vars: Optional[DictStrAny] = None,
    ) -> DictStrAny:
        """
        Perform whatever operation is associated with the file.

        :param tmp: Placeholder for since deprecated parameter.
        :param task_vars: Variables associated around this task.
        :returns: Dictionary of results for the module process.
        """

        result: DictStrAny = {
            'params': None,
            'changed': False}

        args = self._task.args

        assert task_vars is not None

        prefix = args['prefix']
        source = task_vars


        source = {
            k[len(prefix):]: v
            for k, v in source.items()
            if k.startswith(prefix)
            and v not in [None, '']}


        try:

            params = (
                RoleParams(**source)
                .endumped)

            result['params'] = (
                sort_dict(params))


        except Exception as reason:
            result |= {
                'failed': True,
                'exception': reason}


        return sort_dict(result)
