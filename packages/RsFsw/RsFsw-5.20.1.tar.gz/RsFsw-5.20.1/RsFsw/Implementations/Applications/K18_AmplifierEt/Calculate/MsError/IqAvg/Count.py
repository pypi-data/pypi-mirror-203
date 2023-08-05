from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CountCls:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, count: float) -> None:
		"""SCPI: CALCulate:MSERror:IQAVg:COUNt \n
		Snippet: driver.applications.k18AmplifierEt.calculate.msError.iqAvg.count.set(count = 1.0) \n
		No command help available \n
			:param count: No help available
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'CALCulate:MSERror:IQAVg:COUNt {param}')

	def get(self) -> float:
		"""SCPI: CALCulate:MSERror:IQAVg:COUNt \n
		Snippet: value: float = driver.applications.k18AmplifierEt.calculate.msError.iqAvg.count.get() \n
		No command help available \n
			:return: count: No help available"""
		response = self._core.io.query_str(f'CALCulate:MSERror:IQAVg:COUNt?')
		return Conversions.str_to_float(response)
