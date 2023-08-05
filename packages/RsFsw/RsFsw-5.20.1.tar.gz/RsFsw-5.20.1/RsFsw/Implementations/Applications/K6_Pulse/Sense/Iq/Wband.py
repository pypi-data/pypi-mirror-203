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
		Snippet: driver.applications.k6Pulse.sense.iq.wband.set(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:IQ:WBANd {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:IQ:WBANd \n
		Snippet: value: bool = driver.applications.k6Pulse.sense.iq.wband.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'SENSe:IQ:WBANd?')
		return Conversions.str_to_bool(response)
