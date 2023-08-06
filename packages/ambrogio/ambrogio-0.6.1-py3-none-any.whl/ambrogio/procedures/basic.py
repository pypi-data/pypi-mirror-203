from typing import Any
import logging

from ambrogio.procedures import Procedure


class BasicProcedure(Procedure):
    """
    Class for Ambrogio basic procedures.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _execute(self) -> Any:
        """
        Execute the procedure.
        """

        self.logger.info(f'Executing "{self.name}" procedure...')

        result = self.execute()
        self._finished = True
        
        self.logger.info(f'Procedure "{self.name}" executed successfully')

        return result

    def execute(self) -> Any:
        """
        Execute the procedure.
        """
        
        raise NotImplementedError(
            f'{self.__class__.__name__}.execute callback is not defined'
        )