from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RangeCls:
	"""Range commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)

	def set(self, range_py: float) -> None:
		"""SCPI: DIAGnostic:SERVice:INPut:MC:RANGe \n
		Snippet: driver.diagnostic.service.inputPy.mc.range.set(range_py = 1.0) \n
		For R&S FSW85 models using a microwave calibration signal (DIAG:SERV:INP MCAL) . Defines the spectrum of the calibration
		as 43.5 GHz, or a wideband signal that covers the complete 85 GHz bandwidth. You can define the frequency of the
		microwave calibration signal using method RsFsw.Diagnostic.Service.InputPy.Mc.Cfrequency.set. \n
			:param range_py: 43.5 GHz | 85 GHz Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(range_py)
		self._core.io.write(f'DIAGnostic:SERVice:INPut:MC:RANGe {param}')

	def get(self) -> float:
		"""SCPI: DIAGnostic:SERVice:INPut:MC:RANGe \n
		Snippet: value: float = driver.diagnostic.service.inputPy.mc.range.get() \n
		For R&S FSW85 models using a microwave calibration signal (DIAG:SERV:INP MCAL) . Defines the spectrum of the calibration
		as 43.5 GHz, or a wideband signal that covers the complete 85 GHz bandwidth. You can define the frequency of the
		microwave calibration signal using method RsFsw.Diagnostic.Service.InputPy.Mc.Cfrequency.set. \n
			:return: range_py: 43.5 GHz | 85 GHz Unit: HZ"""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:INPut:MC:RANGe?')
		return Conversions.str_to_float(response)
