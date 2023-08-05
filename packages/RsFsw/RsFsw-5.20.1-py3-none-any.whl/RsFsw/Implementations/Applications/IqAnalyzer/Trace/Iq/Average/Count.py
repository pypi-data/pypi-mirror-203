from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CountCls:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, count: int) -> None:
		"""SCPI: TRACe:IQ:AVERage:COUNt \n
		Snippet: driver.applications.iqAnalyzer.trace.iq.average.count.set(count = 1) \n
		This command defines the number of I/Q data sets that the averaging is based on. \n
			:param count: Range: 0 to 32767
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'TRACe:IQ:AVERage:COUNt {param}')

	def get(self) -> int:
		"""SCPI: TRACe:IQ:AVERage:COUNt \n
		Snippet: value: int = driver.applications.iqAnalyzer.trace.iq.average.count.get() \n
		This command defines the number of I/Q data sets that the averaging is based on. \n
			:return: count: No help available"""
		response = self._core.io.query_str(f'TRACe:IQ:AVERage:COUNt?')
		return Conversions.str_to_int(response)
