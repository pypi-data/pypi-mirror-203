from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WbandCls:
	"""Wband commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wband", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:IQ:WBANd \n
		Snippet: driver.applications.iqAnalyzer.sense.iq.wband.set(state = False) \n
		Selects the signal path for signal processing. For details and restrictions, see 'Signal Path'. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 The narrowband signal path is used. ON | 1 The wideband signal path is used.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:IQ:WBANd {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:IQ:WBANd \n
		Snippet: value: bool = driver.applications.iqAnalyzer.sense.iq.wband.get() \n
		Selects the signal path for signal processing. For details and restrictions, see 'Signal Path'. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 The narrowband signal path is used. ON | 1 The wideband signal path is used."""
		response = self._core.io.query_str(f'SENSe:IQ:WBANd?')
		return Conversions.str_to_bool(response)
