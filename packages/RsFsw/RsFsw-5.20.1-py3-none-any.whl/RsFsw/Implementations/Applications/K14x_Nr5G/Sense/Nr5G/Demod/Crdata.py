from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CrdataCls:
	"""Crdata commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crdata", core, parent)

	def set(self, state: enums.CrDataState) -> None:
		"""SCPI: [SENSe]:NR5G:DEMod:CRData \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.demod.crdata.set(state = enums.CrDataState.ALL0) \n
		This command selects the CORESET reference data. \n
			:param state: AUTO Automatic detection of reference values. ALL0 CORESET consists of 0's only. PASLots CORESET based on NR-TM PN23 (pseudo random sequence 23) with all PDCCH having the same sequence. If an ORAN test case is selected (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Oran.Tcase.set, this parameter selects the ORAN PN23 sequence for all PDCCH. PN23 CORESET based on NR-TM PN23 (pseudo random sequence 23) .
		"""
		param = Conversions.enum_scalar_to_str(state, enums.CrDataState)
		self._core.io.write(f'SENSe:NR5G:DEMod:CRData {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.CrDataState:
		"""SCPI: [SENSe]:NR5G:DEMod:CRData \n
		Snippet: value: enums.CrDataState = driver.applications.k14Xnr5G.sense.nr5G.demod.crdata.get() \n
		This command selects the CORESET reference data. \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'SENSe:NR5G:DEMod:CRData?')
		return Conversions.str_to_scalar_enum(response, enums.CrDataState)
