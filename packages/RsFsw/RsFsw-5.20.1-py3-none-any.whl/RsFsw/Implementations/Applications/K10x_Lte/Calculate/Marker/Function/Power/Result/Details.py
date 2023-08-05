from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DetailsCls:
	"""Details commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("details", core, parent)

	def set(self, mode: enums.MarkerFunctionA, window=repcap.Window.Default, marker=repcap.Marker.Default, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer<sb>:RESult:DETails \n
		Snippet: driver.applications.k10Xlte.calculate.marker.function.power.result.details.set(mode = enums.MarkerFunctionA.ACPower, window = repcap.Window.Default, marker = repcap.Marker.Default, subBlock = repcap.SubBlock.Default) \n
		No command help available \n
			:param mode: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Power')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.MarkerFunctionA)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer{subBlock_cmd_val}:RESult:DETails {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default, subBlock=repcap.SubBlock.Default) -> enums.MarkerFunctionA:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer<sb>:RESult:DETails \n
		Snippet: value: enums.MarkerFunctionA = driver.applications.k10Xlte.calculate.marker.function.power.result.details.get(window = repcap.Window.Default, marker = repcap.Marker.Default, subBlock = repcap.SubBlock.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Power')
			:return: mode: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str_with_opc(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer{subBlock_cmd_val}:RESult:DETails?')
		return Conversions.str_to_scalar_enum(response, enums.MarkerFunctionA)
