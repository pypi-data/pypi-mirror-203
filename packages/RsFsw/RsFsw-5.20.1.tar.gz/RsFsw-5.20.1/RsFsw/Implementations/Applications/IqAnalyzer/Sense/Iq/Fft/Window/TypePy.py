from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePyCls:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.FftWindowType) -> None:
		"""SCPI: [SENSe]:IQ:FFT:WINDow:TYPE \n
		Snippet: driver.applications.iqAnalyzer.sense.iq.fft.window.typePy.set(type_py = enums.FftWindowType.BLACkharris) \n
		In the I/Q Analyzer you can select one of several FFT window types. \n
			:param type_py: (enum or string) BLACkharris Blackman-Harris FLATtop Flattop GAUSsian Gauss RECTangular Rectangular P5 5-Term
		"""
		param = Conversions.enum_ext_scalar_to_str(type_py, enums.FftWindowType)
		self._core.io.write(f'SENSe:IQ:FFT:WINDow:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FftWindowType:
		"""SCPI: [SENSe]:IQ:FFT:WINDow:TYPE \n
		Snippet: value: enums.FftWindowType = driver.applications.iqAnalyzer.sense.iq.fft.window.typePy.get() \n
		In the I/Q Analyzer you can select one of several FFT window types. \n
			:return: type_py: (enum or string) No help available"""
		response = self._core.io.query_str(f'SENSe:IQ:FFT:WINDow:TYPE?')
		return Conversions.str_to_scalar_enum_ext(response, enums.FftWindowType)
