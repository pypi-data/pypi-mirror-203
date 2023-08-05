from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:NR5G:TRACking:TPUT:STATe \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.tracking.tput.state.set(state = False) \n
		This command turns the throuput measurement on and off.
			INTRO_CMD_HELP: Effects of this command \n
			- Number of analyzed frames is set to manual ([SENSe:]NR5G:FRAMe:COUNt:AUTO) . \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:NR5G:TRACking:TPUT:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:NR5G:TRACking:TPUT:STATe \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.nr5G.tracking.tput.state.get() \n
		This command turns the throuput measurement on and off.
			INTRO_CMD_HELP: Effects of this command \n
			- Number of analyzed frames is set to manual ([SENSe:]NR5G:FRAMe:COUNt:AUTO) . \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:NR5G:TRACking:TPUT:STATe?')
		return Conversions.str_to_bool(response)
