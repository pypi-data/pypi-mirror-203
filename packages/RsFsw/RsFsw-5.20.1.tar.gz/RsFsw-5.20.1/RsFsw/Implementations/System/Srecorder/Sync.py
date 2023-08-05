from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SyncCls:
	"""Sync commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sync", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: SYSTem:SRECorder:SYNC \n
		Snippet: driver.system.srecorder.sync.set(state = False) \n
		If enabled, additional commands are included in the script to synchronize the recorded commands when necessary.
		For instance, when a measurement is started, a *WAI command is inserted to ensure that the next command is only executed
		after the measurement has finished. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:SRECorder:SYNC {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:SRECorder:SYNC \n
		Snippet: value: bool = driver.system.srecorder.sync.get() \n
		If enabled, additional commands are included in the script to synchronize the recorded commands when necessary.
		For instance, when a measurement is started, a *WAI command is inserted to ensure that the next command is only executed
		after the measurement has finished. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SYSTem:SRECorder:SYNC?')
		return Conversions.str_to_bool(response)
