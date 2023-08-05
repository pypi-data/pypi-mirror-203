from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeIdCls:
	"""UeId commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ueId", core, parent)

	def set(self, idn: float) -> None:
		"""SCPI: CONFigure[:LTE]:DL:NPDSch:UEID \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.npdsch.ueId.set(idn = 1.0) \n
		No command help available \n
			:param idn: No help available
		"""
		param = Conversions.decimal_value_to_str(idn)
		self._core.io.write(f'CONFigure:LTE:DL:NPDSch:UEID {param}')

	def get(self) -> float:
		"""SCPI: CONFigure[:LTE]:DL:NPDSch:UEID \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.npdsch.ueId.get() \n
		No command help available \n
			:return: idn: No help available"""
		response = self._core.io.query_str(f'CONFigure:LTE:DL:NPDSch:UEID?')
		return Conversions.str_to_float(response)
