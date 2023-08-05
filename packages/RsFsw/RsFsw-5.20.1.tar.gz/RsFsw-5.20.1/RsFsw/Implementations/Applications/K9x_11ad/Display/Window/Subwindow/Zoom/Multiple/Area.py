from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AreaCls:
	"""Area commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("area", core, parent)

	def set(self, arg_0: float, arg_1: float, arg_2: float, arg_3: float, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, zoomWindow=repcap.ZoomWindow.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:ZOOM:MULTiple<zn>:AREA \n
		Snippet: driver.applications.k9X11Ad.display.window.subwindow.zoom.multiple.area.set(arg_0 = 1.0, arg_1 = 1.0, arg_2 = 1.0, arg_3 = 1.0, window = repcap.Window.Default, subWindow = repcap.SubWindow.Default, zoomWindow = repcap.ZoomWindow.Default) \n
		No command help available \n
			:param arg_0: No help available
			:param arg_1: No help available
			:param arg_2: No help available
			:param arg_3: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param zoomWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Multiple')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('arg_0', arg_0, DataType.Float), ArgSingle('arg_1', arg_1, DataType.Float), ArgSingle('arg_2', arg_2, DataType.Float), ArgSingle('arg_3', arg_3, DataType.Float))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		zoomWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(zoomWindow, repcap.ZoomWindow)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:ZOOM:MULTiple{zoomWindow_cmd_val}:AREA {param}'.rstrip())

	# noinspection PyTypeChecker
	class AreaStruct(StructBase):
		"""Response structure. Fields: \n
			- Arg_0: float: No parameter help available
			- Arg_1: float: No parameter help available
			- Arg_2: float: No parameter help available
			- Arg_3: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Arg_0'),
			ArgStruct.scalar_float('Arg_1'),
			ArgStruct.scalar_float('Arg_2'),
			ArgStruct.scalar_float('Arg_3')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Arg_0: float = None
			self.Arg_1: float = None
			self.Arg_2: float = None
			self.Arg_3: float = None

	def get(self, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, zoomWindow=repcap.ZoomWindow.Default) -> AreaStruct:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:ZOOM:MULTiple<zn>:AREA \n
		Snippet: value: AreaStruct = driver.applications.k9X11Ad.display.window.subwindow.zoom.multiple.area.get(window = repcap.Window.Default, subWindow = repcap.SubWindow.Default, zoomWindow = repcap.ZoomWindow.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param zoomWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Multiple')
			:return: structure: for return value, see the help for AreaStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		zoomWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(zoomWindow, repcap.ZoomWindow)
		return self._core.io.query_struct(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:ZOOM:MULTiple{zoomWindow_cmd_val}:AREA?', self.__class__.AreaStruct())
