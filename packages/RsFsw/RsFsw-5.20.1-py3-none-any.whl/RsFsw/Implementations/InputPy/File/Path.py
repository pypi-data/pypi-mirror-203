from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.Utilities import trim_str_response
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PathCls:
	"""Path commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("path", core, parent)

	def set(self, file_path: str, analysis_bw: float) -> None:
		"""SCPI: INPut:FILE:PATH \n
		Snippet: driver.inputPy.file.path.set(file_path = '1', analysis_bw = 1.0) \n
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
			:param file_path: No help available
			:param analysis_bw: Optionally: The analysis bandwidth to be used by the measurement. The bandwidth must be smaller than or equal to the bandwidth of the data that was stored in the file. Unit: HZ
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('file_path', file_path, DataType.String), ArgSingle('analysis_bw', analysis_bw, DataType.Float))
		self._core.io.write_with_opc(f'INPut:FILE:PATH {param}'.rstrip())

	def get(self) -> str:
		"""SCPI: INPut:FILE:PATH \n
		Snippet: value: str = driver.inputPy.file.path.get() \n
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
			:return: file_path: No help available"""
		response = self._core.io.query_str_with_opc(f'INPut:FILE:PATH?')
		return trim_str_response(response)
