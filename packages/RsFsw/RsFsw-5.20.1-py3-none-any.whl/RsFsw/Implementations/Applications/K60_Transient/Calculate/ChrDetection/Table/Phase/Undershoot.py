from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UndershootCls:
	"""Undershoot commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("undershoot", core, parent)

	def set(self, state: bool, scaling: enums.TimeScaling = None, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:CHRDetection:TABLe:PHASe:UNDershoot \n
		Snippet: driver.applications.k60Transient.calculate.chrDetection.table.phase.undershoot.set(state = False, scaling = enums.TimeScaling.MS, window = repcap.Window.Default) \n
		No command help available \n
			:param state: 1..n
			:param scaling: S | MS | US | NS
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Boolean), ArgSingle('scaling', scaling, DataType.Enum, enums.TimeScaling, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:CHRDetection:TABLe:PHASe:UNDershoot {param}'.rstrip())

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:CHRDetection:TABLe:PHASe:UNDershoot \n
		Snippet: value: bool = driver.applications.k60Transient.calculate.chrDetection.table.phase.undershoot.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:CHRDetection:TABLe:PHASe:UNDershoot?')
		return Conversions.str_to_bool(response)
