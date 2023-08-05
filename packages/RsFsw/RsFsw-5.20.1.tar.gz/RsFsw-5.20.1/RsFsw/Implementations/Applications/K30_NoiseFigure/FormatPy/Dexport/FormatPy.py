from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPyCls:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, file_format: enums.FileFormat) -> None:
		"""SCPI: FORMat:DEXPort:FORMat \n
		Snippet: driver.applications.k30NoiseFigure.formatPy.dexport.formatPy.set(file_format = enums.FileFormat.CSV) \n
		No command help available \n
			:param file_format: No help available
		"""
		param = Conversions.enum_scalar_to_str(file_format, enums.FileFormat)
		self._core.io.write(f'FORMat:DEXPort:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FileFormat:
		"""SCPI: FORMat:DEXPort:FORMat \n
		Snippet: value: enums.FileFormat = driver.applications.k30NoiseFigure.formatPy.dexport.formatPy.get() \n
		No command help available \n
			:return: file_format: No help available"""
		response = self._core.io.query_str(f'FORMat:DEXPort:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.FileFormat)
