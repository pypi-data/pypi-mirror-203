from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StatusCls:
	"""Status commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("status", core, parent)

	def get(self) -> bool:
		"""SCPI: FETCh:PSERvoing:OPERation:STATus \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.fetch.pservoing.operation.status.get() \n
		Queries the status of the power servoing operation. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'FETCh:PSERvoing:OPERation:STATus?')
		return Conversions.str_to_bool(response)
