from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CatalogCls:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:CORRection:CVL:CATalog \n
		Snippet: value: float = driver.applications.k6Pulse.sense.correction.cvl.catalog.get() \n
		No command help available \n
			:return: catalog: No help available"""
		response = self._core.io.query_str(f'SENSe:CORRection:CVL:CATalog?')
		return Conversions.str_to_float(response)
