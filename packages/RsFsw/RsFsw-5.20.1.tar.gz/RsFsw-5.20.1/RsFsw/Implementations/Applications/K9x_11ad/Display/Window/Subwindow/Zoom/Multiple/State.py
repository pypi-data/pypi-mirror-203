from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, arg_0: bool, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, zoomWindow=repcap.ZoomWindow.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:ZOOM:MULTiple<zn>[:STATe] \n
		Snippet: driver.applications.k9X11Ad.display.window.subwindow.zoom.multiple.state.set(arg_0 = False, window = repcap.Window.Default, subWindow = repcap.SubWindow.Default, zoomWindow = repcap.ZoomWindow.Default) \n
		No command help available \n
			:param arg_0: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param zoomWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Multiple')
		"""
		param = Conversions.bool_to_str(arg_0)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		zoomWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(zoomWindow, repcap.ZoomWindow)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:ZOOM:MULTiple{zoomWindow_cmd_val}:STATe {param}')

	def get(self, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, zoomWindow=repcap.ZoomWindow.Default) -> bool:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:ZOOM:MULTiple<zn>[:STATe] \n
		Snippet: value: bool = driver.applications.k9X11Ad.display.window.subwindow.zoom.multiple.state.get(window = repcap.Window.Default, subWindow = repcap.SubWindow.Default, zoomWindow = repcap.ZoomWindow.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param zoomWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Multiple')
			:return: arg_0: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		zoomWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(zoomWindow, repcap.ZoomWindow)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:ZOOM:MULTiple{zoomWindow_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
