from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CountCls:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:NR5G:FEVents:COUNt \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.nr5G.fevents.count.get() \n
		This command queries the number of filtered events for combined measurements.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Define and turn on an event filter. \n
			:return: count: No help available"""
		response = self._core.io.query_str(f'SENSe:NR5G:FEVents:COUNt?')
		return Conversions.str_to_float(response)
