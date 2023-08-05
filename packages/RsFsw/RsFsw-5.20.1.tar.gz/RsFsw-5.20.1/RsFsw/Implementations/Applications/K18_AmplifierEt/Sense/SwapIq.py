from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SwapIqCls:
	"""SwapIq commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("swapIq", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:SWAPiq \n
		Snippet: driver.applications.k18AmplifierEt.sense.swapIq.set(state = False) \n
		This command inverts the I and Q branches of the signal. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:SWAPiq {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:SWAPiq \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.sense.swapIq.get() \n
		This command inverts the I and Q branches of the signal. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:SWAPiq?')
		return Conversions.str_to_bool(response)
