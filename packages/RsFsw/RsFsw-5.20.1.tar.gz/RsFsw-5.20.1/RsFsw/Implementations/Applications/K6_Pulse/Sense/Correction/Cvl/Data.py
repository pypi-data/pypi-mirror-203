from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DataCls:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, freq: List[float], level: List[float]) -> None:
		"""SCPI: [SENSe]:CORRection:CVL:DATA \n
		Snippet: driver.applications.k6Pulse.sense.correction.cvl.data.set(freq = [1.1, 2.2, 3.3], level = [1.1, 2.2, 3.3]) \n
		No command help available \n
			:param freq: No help available
			:param level: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('freq', freq, DataType.FloatList, None), ArgSingle.as_open_list('level', level, DataType.FloatList, None))
		self._core.io.write(f'SENSe:CORRection:CVL:DATA {param}'.rstrip())

	# noinspection PyTypeChecker
	class DataStruct(StructBase):
		"""Response structure. Fields: \n
			- Freq: List[float]: No parameter help available
			- Level: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Freq', DataType.FloatList, None, False, True, 1),
			ArgStruct('Level', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Freq: List[float] = None
			self.Level: List[float] = None

	def get(self) -> DataStruct:
		"""SCPI: [SENSe]:CORRection:CVL:DATA \n
		Snippet: value: DataStruct = driver.applications.k6Pulse.sense.correction.cvl.data.get() \n
		No command help available \n
			:return: structure: for return value, see the help for DataStruct structure arguments."""
		return self._core.io.query_struct(f'SENSe:CORRection:CVL:DATA?', self.__class__.DataStruct())
