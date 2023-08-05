from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPyCls:
	"""FilterPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)

	def set(self, filter_py: enums.FilterDemodNr5G) -> None:
		"""SCPI: [SENSe]:NR5G:DEMod:FILTer \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.demod.filterPy.set(filter_py = enums.FilterDemodNr5G.MFILter) \n
		This command selects the filter for suppression of neighboring channels. \n
			:param filter_py: MFILter Multicarrier filter. NONE No filter. PBWP Bandwidthpart filter.
		"""
		param = Conversions.enum_scalar_to_str(filter_py, enums.FilterDemodNr5G)
		self._core.io.write(f'SENSe:NR5G:DEMod:FILTer {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FilterDemodNr5G:
		"""SCPI: [SENSe]:NR5G:DEMod:FILTer \n
		Snippet: value: enums.FilterDemodNr5G = driver.applications.k14Xnr5G.sense.nr5G.demod.filterPy.get() \n
		This command selects the filter for suppression of neighboring channels. \n
			:return: filter_py: MFILter Multicarrier filter. NONE No filter. PBWP Bandwidthpart filter."""
		response = self._core.io.query_str(f'SENSe:NR5G:DEMod:FILTer?')
		return Conversions.str_to_scalar_enum(response, enums.FilterDemodNr5G)
