from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LevelCls:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, threshold: float) -> None:
		"""SCPI: [SENSe]:DEMod:SQUelch:LEVel \n
		Snippet: driver.applications.k70Vsa.sense.demod.squelch.level.set(threshold = 1.0) \n
		No command help available \n
			:param threshold: No help available
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'SENSe:DEMod:SQUelch:LEVel {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DEMod:SQUelch:LEVel \n
		Snippet: value: float = driver.applications.k70Vsa.sense.demod.squelch.level.get() \n
		No command help available \n
			:return: threshold: No help available"""
		response = self._core.io.query_str(f'SENSe:DEMod:SQUelch:LEVel?')
		return Conversions.str_to_float(response)
