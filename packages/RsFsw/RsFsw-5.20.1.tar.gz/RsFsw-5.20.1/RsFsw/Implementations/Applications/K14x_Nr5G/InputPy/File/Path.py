from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PathCls:
	"""Path commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("path", core, parent)

	def set(self, filename: str, bandwidth: float = None) -> None:
		"""SCPI: INPut:FILE:PATH \n
		Snippet: driver.applications.k14Xnr5G.inputPy.file.path.set(filename = '1', bandwidth = 1.0) \n
		This command selects the I/Q data file to be used as input for further measurements.
			INTRO_CMD_HELP: The I/Q data file must be in one of the following supported formats: \n
			- .iq.tar
			- .iqw
			- .csv
			- .mat
			- .wv
			- .aid
		Only a single data stream or channel can be used as input, even if multiple streams or channels are stored in the file.
		For some file formats that do not provide the sample rate and measurement time or record length, you must define these
		parameters manually. Otherwise the traces are not visible in the result displays. For details, see 'Basics on Input from
		I/Q Data Files'. \n
			:param filename: String containing the path and name of the source file. The file extension is *.iq.tar.
			:param bandwidth: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filename', filename, DataType.String), ArgSingle('bandwidth', bandwidth, DataType.Float, None, is_optional=True))
		self._core.io.write(f'INPut:FILE:PATH {param}'.rstrip())

	# noinspection PyTypeChecker
	class PathStruct(StructBase):
		"""Response structure. Fields: \n
			- Filename: str: String containing the path and name of the source file. The file extension is *.iq.tar.
			- Bandwidth: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Filename'),
			ArgStruct.scalar_float('Bandwidth')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Filename: str = None
			self.Bandwidth: float = None

	def get(self) -> PathStruct:
		"""SCPI: INPut:FILE:PATH \n
		Snippet: value: PathStruct = driver.applications.k14Xnr5G.inputPy.file.path.get() \n
		This command selects the I/Q data file to be used as input for further measurements.
			INTRO_CMD_HELP: The I/Q data file must be in one of the following supported formats: \n
			- .iq.tar
			- .iqw
			- .csv
			- .mat
			- .wv
			- .aid
		Only a single data stream or channel can be used as input, even if multiple streams or channels are stored in the file.
		For some file formats that do not provide the sample rate and measurement time or record length, you must define these
		parameters manually. Otherwise the traces are not visible in the result displays. For details, see 'Basics on Input from
		I/Q Data Files'. \n
			:return: structure: for return value, see the help for PathStruct structure arguments."""
		return self._core.io.query_struct(f'INPut:FILE:PATH?', self.__class__.PathStruct())
