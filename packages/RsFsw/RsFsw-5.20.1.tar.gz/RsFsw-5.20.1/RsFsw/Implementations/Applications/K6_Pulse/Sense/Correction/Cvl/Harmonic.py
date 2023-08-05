from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HarmonicCls:
	"""Harmonic commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("harmonic", core, parent)

	def set(self, harmonic: float) -> None:
		"""SCPI: [SENSe]:CORRection:CVL:HARMonic \n
		Snippet: driver.applications.k6Pulse.sense.correction.cvl.harmonic.set(harmonic = 1.0) \n
		No command help available \n
			:param harmonic: No help available
		"""
		param = Conversions.decimal_value_to_str(harmonic)
		self._core.io.write(f'SENSe:CORRection:CVL:HARMonic {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CORRection:CVL:HARMonic \n
		Snippet: value: float = driver.applications.k6Pulse.sense.correction.cvl.harmonic.get() \n
		No command help available \n
			:return: harmonic: No help available"""
		response = self._core.io.query_str(f'SENSe:CORRection:CVL:HARMonic?')
		return Conversions.str_to_float(response)
