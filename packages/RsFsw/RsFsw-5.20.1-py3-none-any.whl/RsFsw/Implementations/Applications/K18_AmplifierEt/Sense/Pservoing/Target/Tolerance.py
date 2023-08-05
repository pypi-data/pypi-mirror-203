from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ToleranceCls:
	"""Tolerance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tolerance", core, parent)

	def set(self, target_value: float) -> None:
		"""SCPI: [SENSe]:PSERvoing:TARGet:TOLerance \n
		Snippet: driver.applications.k18AmplifierEt.sense.pservoing.target.tolerance.set(target_value = 1.0) \n
		Sets and queries the power servoing target tolerance. The unit depends on the selected target parameter. \n
			:param target_value: numeric value
		"""
		param = Conversions.decimal_value_to_str(target_value)
		self._core.io.write(f'SENSe:PSERvoing:TARGet:TOLerance {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:PSERvoing:TARGet:TOLerance \n
		Snippet: value: float = driver.applications.k18AmplifierEt.sense.pservoing.target.tolerance.get() \n
		Sets and queries the power servoing target tolerance. The unit depends on the selected target parameter. \n
			:return: target_value: numeric value"""
		response = self._core.io.query_str(f'SENSe:PSERvoing:TARGet:TOLerance?')
		return Conversions.str_to_float(response)
