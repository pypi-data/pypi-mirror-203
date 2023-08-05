from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ds1KCls:
	"""Ds1K commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ds1K", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:ALL:SUMMary:EVM:DS1K \n
		Snippet: value: float = driver.applications.k14Xnr5G.fetch.all.summary.evm.ds1K.get() \n
		This command queries the EVM of all PDSCH resource elements with a 1024QAM modulation.
			INTRO_CMD_HELP: method RsFsw.Applications.K14x_Nr5G.Fetch.All.Summary.Evm.Ds1K.get_ queries the average result over all carriers. Prerequisites: \n
			- Select to evaluate all carriers ([SENSe:]NR5G:RSUMmary:CCResult) . \n
			:return: result: ALL Available for combined measurements. Queries the EVM of all events (meas IDs) . Omitting this parameter queries the EVM of the selected event."""
		response = self._core.io.query_str(f'FETCh:ALL:SUMMary:EVM:DS1K?')
		return Conversions.str_to_float(response)
