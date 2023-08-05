from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DataCls:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, mode: enums.DataDemodModeK91) -> None:
		"""SCPI: [SENSe]:DEMod:DATA \n
		Snippet: driver.applications.k91Wlan.sense.demod.data.set(mode = enums.DataDemodModeK91.ACDScarrier) \n
		Defines when in the demodulation process the bitstream is determined and thus which results are available. See also 'BER
		and CWER'. \n
			:param mode: ACDScarrier | ALBDecoder ACDScarrier (Default:) No channel decoding is performed. Processing time is reduced, but BER and CWER results are not available. ALBDecoder Decoding is performed, providing BER and CWER results. Measurement time is increased compared to non-decoding process.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.DataDemodModeK91)
		self._core.io.write(f'SENSe:DEMod:DATA {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DataDemodModeK91:
		"""SCPI: [SENSe]:DEMod:DATA \n
		Snippet: value: enums.DataDemodModeK91 = driver.applications.k91Wlan.sense.demod.data.get() \n
		Defines when in the demodulation process the bitstream is determined and thus which results are available. See also 'BER
		and CWER'. \n
			:return: mode: ACDScarrier | ALBDecoder ACDScarrier (Default:) No channel decoding is performed. Processing time is reduced, but BER and CWER results are not available. ALBDecoder Decoding is performed, providing BER and CWER results. Measurement time is increased compared to non-decoding process."""
		response = self._core.io.query_str(f'SENSe:DEMod:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.DataDemodModeK91)
