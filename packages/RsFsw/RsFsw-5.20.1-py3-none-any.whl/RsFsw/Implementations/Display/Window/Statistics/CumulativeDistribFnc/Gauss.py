from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GaussCls:
	"""Gauss commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gauss", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:STATistics:CCDF:GAUSs \n
		Snippet: driver.display.window.statistics.cumulativeDistribFnc.gauss.set(state = False, window = repcap.Window.Default) \n
		Enables or disables the red trace in the CCDF display indicating the normal distribution. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:STATistics:CCDF:GAUSs {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: DISPlay[:WINDow<n>]:STATistics:CCDF:GAUSs \n
		Snippet: value: bool = driver.display.window.statistics.cumulativeDistribFnc.gauss.get(window = repcap.Window.Default) \n
		Enables or disables the red trace in the CCDF display indicating the normal distribution. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:STATistics:CCDF:GAUSs?')
		return Conversions.str_to_bool(response)
