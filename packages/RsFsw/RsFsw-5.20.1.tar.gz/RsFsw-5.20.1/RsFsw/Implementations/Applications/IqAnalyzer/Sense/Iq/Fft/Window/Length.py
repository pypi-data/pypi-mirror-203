from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LengthCls:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, length: int) -> None:
		"""SCPI: [SENSe]:IQ:FFT:WINDow:LENGth \n
		Snippet: driver.applications.iqAnalyzer.sense.iq.fft.window.length.set(length = 1) \n
		Defines the number of samples to be included in a single FFT window when multiple FFT windows are used. \n
			:param length: integer value Range: 3 to 1001
		"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'SENSe:IQ:FFT:WINDow:LENGth {param}')

	def get(self) -> int:
		"""SCPI: [SENSe]:IQ:FFT:WINDow:LENGth \n
		Snippet: value: int = driver.applications.iqAnalyzer.sense.iq.fft.window.length.get() \n
		Defines the number of samples to be included in a single FFT window when multiple FFT windows are used. \n
			:return: length: No help available"""
		response = self._core.io.query_str(f'SENSe:IQ:FFT:WINDow:LENGth?')
		return Conversions.str_to_int(response)
