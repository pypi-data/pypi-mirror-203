from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LanguageCls:
	"""Language commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("language", core, parent)

	def set(self, language: enums.PictureFormat) -> None:
		"""SCPI: HCOPy:DEVice:LANGuage \n
		Snippet: driver.hardCopy.device.language.set(language = enums.PictureFormat.BMP) \n
		This command selects the file format for a print job or to store a screenshot to a file. \n
			:param language: BMP | JPG | PNG | PDF | SVG Data format for output to files DOC | PDF File type for test reports Available for HCOP:MODE REPort
		"""
		param = Conversions.enum_scalar_to_str(language, enums.PictureFormat)
		self._core.io.write(f'HCOPy:DEVice:LANGuage {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PictureFormat:
		"""SCPI: HCOPy:DEVice:LANGuage \n
		Snippet: value: enums.PictureFormat = driver.hardCopy.device.language.get() \n
		This command selects the file format for a print job or to store a screenshot to a file. \n
			:return: language: BMP | JPG | PNG | PDF | SVG Data format for output to files DOC | PDF File type for test reports Available for HCOP:MODE REPort"""
		response = self._core.io.query_str(f'HCOPy:DEVice:LANGuage?')
		return Conversions.str_to_scalar_enum(response, enums.PictureFormat)
