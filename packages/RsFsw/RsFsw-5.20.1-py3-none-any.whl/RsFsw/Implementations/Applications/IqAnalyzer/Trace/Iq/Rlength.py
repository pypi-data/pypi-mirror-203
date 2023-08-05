from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RlengthCls:
	"""Rlength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rlength", core, parent)

	def set(self, record_length: int) -> None:
		"""SCPI: TRACe:IQ:RLENgth \n
		Snippet: driver.applications.iqAnalyzer.trace.iq.rlength.set(record_length = 1) \n
		This command sets the record length for the acquired I/Q data. Increasing the record length also increases the
		measurement time. Note: Alternatively, you can define the measurement time using the SENS:SWE:TIME command. \n
			:param record_length: Number of samples to record. See 'Sample rate and maximum usable I/Q bandwidth for RF input'. For digital input via the 'Digital Baseband' interface (R&S FSW-B17) the valid number of samples is described in 'Sample rates and bandwidths for digital I/Q data'.
		"""
		param = Conversions.decimal_value_to_str(record_length)
		self._core.io.write(f'TRACe:IQ:RLENgth {param}')

	def get(self) -> int:
		"""SCPI: TRACe:IQ:RLENgth \n
		Snippet: value: int = driver.applications.iqAnalyzer.trace.iq.rlength.get() \n
		This command sets the record length for the acquired I/Q data. Increasing the record length also increases the
		measurement time. Note: Alternatively, you can define the measurement time using the SENS:SWE:TIME command. \n
			:return: record_length: No help available"""
		response = self._core.io.query_str(f'TRACe:IQ:RLENgth?')
		return Conversions.str_to_int(response)
