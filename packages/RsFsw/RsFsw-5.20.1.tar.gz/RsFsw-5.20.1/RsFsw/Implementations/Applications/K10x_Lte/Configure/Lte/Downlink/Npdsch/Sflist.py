from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SflistCls:
	"""Sflist commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sflist", core, parent)

	def set(self, sub_frame_list: str) -> None:
		"""SCPI: CONFigure[:LTE]:DL:NPDSch:SFList \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.npdsch.sflist.set(sub_frame_list = '1') \n
		No command help available \n
			:param sub_frame_list: No help available
		"""
		param = Conversions.value_to_quoted_str(sub_frame_list)
		self._core.io.write(f'CONFigure:LTE:DL:NPDSch:SFList {param}')

	def get(self) -> str:
		"""SCPI: CONFigure[:LTE]:DL:NPDSch:SFList \n
		Snippet: value: str = driver.applications.k10Xlte.configure.lte.downlink.npdsch.sflist.get() \n
		No command help available \n
			:return: sub_frame_list: No help available"""
		response = self._core.io.query_str(f'CONFigure:LTE:DL:NPDSch:SFList?')
		return trim_str_response(response)
