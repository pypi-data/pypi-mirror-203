from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StepCls:
	"""Step commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("step", core, parent)

	def set(self, input_power_step: float) -> None:
		"""SCPI: [SENSe]:PSERvoing:INPut:STEP \n
		Snippet: driver.applications.k18AmplifierEt.sense.pservoing.inputPy.step.set(input_power_step = 1.0) \n
		Defines the input power step size. \n
			:param input_power_step: numeric value
		"""
		param = Conversions.decimal_value_to_str(input_power_step)
		self._core.io.write(f'SENSe:PSERvoing:INPut:STEP {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:PSERvoing:INPut:STEP \n
		Snippet: value: float = driver.applications.k18AmplifierEt.sense.pservoing.inputPy.step.get() \n
		Defines the input power step size. \n
			:return: input_power_step: numeric value"""
		response = self._core.io.query_str(f'SENSe:PSERvoing:INPut:STEP?')
		return Conversions.str_to_float(response)
