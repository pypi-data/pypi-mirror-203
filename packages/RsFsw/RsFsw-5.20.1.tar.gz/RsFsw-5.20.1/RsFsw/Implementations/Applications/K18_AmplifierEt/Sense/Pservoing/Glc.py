from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GlcCls:
	"""Glc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("glc", core, parent)

	def set(self, gen_level_control: enums.GenLevelControl) -> None:
		"""SCPI: [SENSe]:PSERvoing[:GLC] \n
		Snippet: driver.applications.k18AmplifierEt.sense.pservoing.glc.set(gen_level_control = enums.GenLevelControl.DATT) \n
		Selects if the generator level is modified using input power or digital attenuation. \n
			:param gen_level_control: RFL | DATT RFL Input power DATT Digital attenuation
		"""
		param = Conversions.enum_scalar_to_str(gen_level_control, enums.GenLevelControl)
		self._core.io.write(f'SENSe:PSERvoing:GLC {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.GenLevelControl:
		"""SCPI: [SENSe]:PSERvoing[:GLC] \n
		Snippet: value: enums.GenLevelControl = driver.applications.k18AmplifierEt.sense.pservoing.glc.get() \n
		Selects if the generator level is modified using input power or digital attenuation. \n
			:return: gen_level_control: RFL | DATT RFL Input power DATT Digital attenuation"""
		response = self._core.io.query_str(f'SENSe:PSERvoing:GLC?')
		return Conversions.str_to_scalar_enum(response, enums.GenLevelControl)
