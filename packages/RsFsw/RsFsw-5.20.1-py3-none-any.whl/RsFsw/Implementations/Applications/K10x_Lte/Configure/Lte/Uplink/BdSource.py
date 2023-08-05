from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BdSourceCls:
	"""BdSource commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bdSource", core, parent)

	def set(self, reference: enums.ReferenceBdSourceK10x) -> None:
		"""SCPI: CONFigure[:LTE]:UL:BDSource \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.bdSource.set(reference = enums.ReferenceBdSourceK10x.NONE) \n
		No command help available \n
			:param reference: No help available
		"""
		param = Conversions.enum_scalar_to_str(reference, enums.ReferenceBdSourceK10x)
		self._core.io.write(f'CONFigure:LTE:UL:BDSource {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ReferenceBdSourceK10x:
		"""SCPI: CONFigure[:LTE]:UL:BDSource \n
		Snippet: value: enums.ReferenceBdSourceK10x = driver.applications.k10Xlte.configure.lte.uplink.bdSource.get() \n
		No command help available \n
			:return: reference: No help available"""
		response = self._core.io.query_str(f'CONFigure:LTE:UL:BDSource?')
		return Conversions.str_to_scalar_enum(response, enums.ReferenceBdSourceK10x)
