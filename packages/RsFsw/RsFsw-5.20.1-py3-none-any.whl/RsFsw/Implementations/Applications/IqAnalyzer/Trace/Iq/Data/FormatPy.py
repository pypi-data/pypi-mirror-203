from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPyCls:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, data_format: enums.IqResultDataFormat) -> None:
		"""SCPI: TRACe:IQ:DATA:FORMat \n
		Snippet: driver.applications.iqAnalyzer.trace.iq.data.formatPy.set(data_format = enums.IqResultDataFormat.COMPatible) \n
		This command selects the order of the I/Q data. For details see 'Reference: format description for I/Q data files'. For
		traces captured using the optional 2 GHz / 5 GHz bandwidth extension (R&S FSW-B2000/B5000) , only 'IQPair' format is
		available. \n
			:param data_format: (enum or string) COMPatible | IQBLock | IQPair COMPatible I and Q values are separated and collected in blocks: A block (512k) of I values is followed by a block (512k) of Q values, followed by a block of I values, followed by a block of Q values etc. (I,I,I,I,Q,Q,Q,Q,I,I,I,I,Q,Q,Q,Q...) IQBLock First all I-values are listed, then the Q-values (I,I,I,I,I,I,...Q,Q,Q,Q,Q,Q) This option is not available for input from SnP files (see 'Compensating for Frequency Response Using SnP Files (R&S FSW-K544) ') . IQPair One pair of I/Q values after the other is listed (I,Q,I,Q,I,Q...) . This option is the default for input from SnP files (see 'Compensating for Frequency Response Using SnP Files (R&S FSW-K544) ') .
		"""
		param = Conversions.enum_ext_scalar_to_str(data_format, enums.IqResultDataFormat)
		self._core.io.write(f'TRACe:IQ:DATA:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.IqResultDataFormat:
		"""SCPI: TRACe:IQ:DATA:FORMat \n
		Snippet: value: enums.IqResultDataFormat = driver.applications.iqAnalyzer.trace.iq.data.formatPy.get() \n
		This command selects the order of the I/Q data. For details see 'Reference: format description for I/Q data files'. For
		traces captured using the optional 2 GHz / 5 GHz bandwidth extension (R&S FSW-B2000/B5000) , only 'IQPair' format is
		available. \n
			:return: data_format: (enum or string) No help available"""
		response = self._core.io.query_str(f'TRACe:IQ:DATA:FORMat?')
		return Conversions.str_to_scalar_enum_ext(response, enums.IqResultDataFormat)
