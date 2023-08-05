from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SccCls:
	"""Scc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scc", core, parent)

	def set(self, select: float) -> None:
		"""SCPI: [SENSe]:NR5G:SCC \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.scc.set(select = 1.0) \n
		No command help available \n
			:param select: No help available
		"""
		param = Conversions.decimal_value_to_str(select)
		self._core.io.write(f'SENSe:NR5G:SCC {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:NR5G:SCC \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.nr5G.scc.get() \n
		No command help available \n
			:return: select: No help available"""
		response = self._core.io.query_str(f'SENSe:NR5G:SCC?')
		return Conversions.str_to_float(response)
