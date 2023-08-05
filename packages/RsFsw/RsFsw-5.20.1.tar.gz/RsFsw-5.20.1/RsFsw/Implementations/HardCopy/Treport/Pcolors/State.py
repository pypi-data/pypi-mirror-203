from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: HCOPy:TREPort:PCOLors:STATe \n
		Snippet: driver.hardCopy.treport.pcolors.state.set(state = False) \n
		This command turns the use of printer friendly colors on and off. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'HCOPy:TREPort:PCOLors:STATe {param}')

	def get(self) -> bool:
		"""SCPI: HCOPy:TREPort:PCOLors:STATe \n
		Snippet: value: bool = driver.hardCopy.treport.pcolors.state.get() \n
		This command turns the use of printer friendly colors on and off. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'HCOPy:TREPort:PCOLors:STATe?')
		return Conversions.str_to_bool(response)
