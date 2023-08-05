from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, state: bool, scaling: enums.FrequencyScaling = None, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:CHRDetection:TABLe:FREQuency:FREQuency \n
		Snippet: driver.applications.k60Transient.calculate.chrDetection.table.frequency.frequency.set(state = False, scaling = enums.FrequencyScaling.GHZ, window = repcap.Window.Default) \n
		No command help available \n
			:param state: 1..n
			:param scaling: GHZ | MHZ | KHZ | HZ
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Boolean), ArgSingle('scaling', scaling, DataType.Enum, enums.FrequencyScaling, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:CHRDetection:TABLe:FREQuency:FREQuency {param}'.rstrip())

	# noinspection PyTypeChecker
	class FrequencyStruct(StructBase):
		"""Response structure. Fields: \n
			- State: bool: No parameter help available
			- Scaling: enums.FrequencyScaling: GHZ | MHZ | KHZ | HZ"""
		__meta_args_list = [
			ArgStruct.scalar_bool('State'),
			ArgStruct.scalar_enum('Scaling', enums.FrequencyScaling)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State: bool = None
			self.Scaling: enums.FrequencyScaling = None

	def get(self, window=repcap.Window.Default) -> FrequencyStruct:
		"""SCPI: CALCulate<n>:CHRDetection:TABLe:FREQuency:FREQuency \n
		Snippet: value: FrequencyStruct = driver.applications.k60Transient.calculate.chrDetection.table.frequency.frequency.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: structure: for return value, see the help for FrequencyStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:CHRDetection:TABLe:FREQuency:FREQuency?', self.__class__.FrequencyStruct())
