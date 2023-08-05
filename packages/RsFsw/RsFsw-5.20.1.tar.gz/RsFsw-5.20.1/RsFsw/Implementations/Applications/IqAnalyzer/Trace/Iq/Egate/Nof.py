from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NofCls:
	"""Nof commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nof", core, parent)

	def set(self, periods_count: int) -> None:
		"""SCPI: TRACe:IQ:EGATe:NOF \n
		Snippet: driver.applications.iqAnalyzer.trace.iq.egate.nof.set(periods_count = 1) \n
		This command defines the number of gate periods after the trigger signal for gated measurements with the I/Q analyzer. \n
			:param periods_count: Range: 1 to 1023
		"""
		param = Conversions.decimal_value_to_str(periods_count)
		self._core.io.write(f'TRACe:IQ:EGATe:NOF {param}')

	def get(self) -> int:
		"""SCPI: TRACe:IQ:EGATe:NOF \n
		Snippet: value: int = driver.applications.iqAnalyzer.trace.iq.egate.nof.get() \n
		This command defines the number of gate periods after the trigger signal for gated measurements with the I/Q analyzer. \n
			:return: periods_count: No help available"""
		response = self._core.io.query_str(f'TRACe:IQ:EGATe:NOF?')
		return Conversions.str_to_int(response)
