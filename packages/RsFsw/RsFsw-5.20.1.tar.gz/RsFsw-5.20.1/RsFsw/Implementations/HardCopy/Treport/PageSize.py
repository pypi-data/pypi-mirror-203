from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PageSizeCls:
	"""PageSize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pageSize", core, parent)

	def set(self, size: enums.HardcopyPageSize) -> None:
		"""SCPI: HCOPy:TREPort:PAGesize \n
		Snippet: driver.hardCopy.treport.pageSize.set(size = enums.HardcopyPageSize.A4) \n
		This command selects the size of the test report document. \n
			:param size: A4 | US A4 Document pages have an A4 size. US Document pages have a US letter size.
		"""
		param = Conversions.enum_scalar_to_str(size, enums.HardcopyPageSize)
		self._core.io.write(f'HCOPy:TREPort:PAGesize {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.HardcopyPageSize:
		"""SCPI: HCOPy:TREPort:PAGesize \n
		Snippet: value: enums.HardcopyPageSize = driver.hardCopy.treport.pageSize.get() \n
		This command selects the size of the test report document. \n
			:return: size: A4 | US A4 Document pages have an A4 size. US Document pages have a US letter size."""
		response = self._core.io.query_str(f'HCOPy:TREPort:PAGesize?')
		return Conversions.str_to_scalar_enum(response, enums.HardcopyPageSize)
