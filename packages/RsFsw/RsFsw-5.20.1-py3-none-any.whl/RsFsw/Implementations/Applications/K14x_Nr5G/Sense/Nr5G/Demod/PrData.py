from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrDataCls:
	"""PrData commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prData", core, parent)

	def set(self, reference: enums.ReferenceDataNr5G) -> None:
		"""SCPI: [SENSe]:NR5G:DEMod:PRData \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.demod.prData.set(reference = enums.ReferenceDataNr5G.ALL0) \n
		This command selects the PUSCH reference data. Note that when you select an ORAN test case, this setting is automatically
		adjusted to the ORAN test case. \n
			:param reference: AUTO Automatic detection of reference values. PASLots Available when the ORAN application is installed. PDSCH based on NR-TM PN23 (pseudo random sequence 23) with all PUSCH having the same sequence. If an ORAN test case is selected (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Oran.Tcase.set, this parameter selects the ORAN PN23 sequence for all PUSCH. PN23 Available when the ORAN application is installed. PDSCH based on NR-TM PN23 (pseudo random sequence 23) with each PUSCH getting its own sequence. If an ORAN test case is selected (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Oran.Tcase.set, this parameter selects the ORAN PN23 sequence.
		"""
		param = Conversions.enum_scalar_to_str(reference, enums.ReferenceDataNr5G)
		self._core.io.write(f'SENSe:NR5G:DEMod:PRData {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ReferenceDataNr5G:
		"""SCPI: [SENSe]:NR5G:DEMod:PRData \n
		Snippet: value: enums.ReferenceDataNr5G = driver.applications.k14Xnr5G.sense.nr5G.demod.prData.get() \n
		This command selects the PUSCH reference data. Note that when you select an ORAN test case, this setting is automatically
		adjusted to the ORAN test case. \n
			:return: reference: AUTO Automatic detection of reference values. PASLots Available when the ORAN application is installed. PDSCH based on NR-TM PN23 (pseudo random sequence 23) with all PUSCH having the same sequence. If an ORAN test case is selected (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Oran.Tcase.set, this parameter selects the ORAN PN23 sequence for all PUSCH. PN23 Available when the ORAN application is installed. PDSCH based on NR-TM PN23 (pseudo random sequence 23) with each PUSCH getting its own sequence. If an ORAN test case is selected (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Oran.Tcase.set, this parameter selects the ORAN PN23 sequence."""
		response = self._core.io.query_str(f'SENSe:NR5G:DEMod:PRData?')
		return Conversions.str_to_scalar_enum(response, enums.ReferenceDataNr5G)
