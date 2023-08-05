from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IterationCls:
	"""Iteration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iteration", core, parent)

	def set(self, max_iterations: float) -> None:
		"""SCPI: [SENSe]:PSERvoing:MAX:ITERation \n
		Snippet: driver.applications.k18AmplifierEt.sense.pservoing.max.iteration.set(max_iterations = 1.0) \n
		Sets and queries the maximum number of iteratons during the power servoing sequence. \n
			:param max_iterations: numeric value
		"""
		param = Conversions.decimal_value_to_str(max_iterations)
		self._core.io.write(f'SENSe:PSERvoing:MAX:ITERation {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:PSERvoing:MAX:ITERation \n
		Snippet: value: float = driver.applications.k18AmplifierEt.sense.pservoing.max.iteration.get() \n
		Sets and queries the maximum number of iteratons during the power servoing sequence. \n
			:return: max_iterations: numeric value"""
		response = self._core.io.query_str(f'SENSe:PSERvoing:MAX:ITERation?')
		return Conversions.str_to_float(response)
