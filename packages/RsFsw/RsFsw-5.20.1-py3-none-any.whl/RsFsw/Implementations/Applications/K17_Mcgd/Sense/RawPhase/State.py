from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:RAWPhase[:STATe] \n
		Snippet: driver.applications.k17Mcgd.sense.rawPhase.state.set(state = False) \n
		If enabled, the raw, unprocessed phase data is displayed in the 'Phase' and 'Phase Difference' result displays. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:RAWPhase:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:RAWPhase[:STATe] \n
		Snippet: value: bool = driver.applications.k17Mcgd.sense.rawPhase.state.get() \n
		If enabled, the raw, unprocessed phase data is displayed in the 'Phase' and 'Phase Difference' result displays. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:RAWPhase:STATe?')
		return Conversions.str_to_bool(response)
