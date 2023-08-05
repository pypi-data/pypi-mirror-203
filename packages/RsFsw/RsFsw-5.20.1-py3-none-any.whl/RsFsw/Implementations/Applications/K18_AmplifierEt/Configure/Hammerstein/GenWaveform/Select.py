from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SelectCls:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, generator_waveform: enums.GenWaveform) -> None:
		"""SCPI: CONFigure:HAMMerstein:GENWaveform[:SELect] \n
		Snippet: driver.applications.k18AmplifierEt.configure.hammerstein.genWaveform.select.set(generator_waveform = enums.GenWaveform.DDPD) \n
		Switches the generator waveform between reference and direct DPD. \n
			:param generator_waveform: REFerence | DDPD REFerence Reference waveform DDPD DDPD waveform
		"""
		param = Conversions.enum_scalar_to_str(generator_waveform, enums.GenWaveform)
		self._core.io.write(f'CONFigure:HAMMerstein:GENWaveform:SELect {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.GenWaveform:
		"""SCPI: CONFigure:HAMMerstein:GENWaveform[:SELect] \n
		Snippet: value: enums.GenWaveform = driver.applications.k18AmplifierEt.configure.hammerstein.genWaveform.select.get() \n
		Switches the generator waveform between reference and direct DPD. \n
			:return: generator_waveform: REFerence | DDPD REFerence Reference waveform DDPD DDPD waveform"""
		response = self._core.io.query_str(f'CONFigure:HAMMerstein:GENWaveform:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.GenWaveform)
