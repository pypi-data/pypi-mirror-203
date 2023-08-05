from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LinkCls:
	"""Link commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("link", core, parent)

	def set(self, coupling: enums.PmeterFreqLink, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: [SENSe]:PMETer<p>:FREQuency:LINK \n
		Snippet: driver.applications.k14Xnr5G.sense.pmeter.frequency.link.set(coupling = enums.PmeterFreqLink.CENTer, powerMeter = repcap.PowerMeter.Default) \n
		No command help available \n
			:param coupling: No help available
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.enum_scalar_to_str(coupling, enums.PmeterFreqLink)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'SENSe:PMETer{powerMeter_cmd_val}:FREQuency:LINK {param}')

	# noinspection PyTypeChecker
	def get(self, powerMeter=repcap.PowerMeter.Default) -> enums.PmeterFreqLink:
		"""SCPI: [SENSe]:PMETer<p>:FREQuency:LINK \n
		Snippet: value: enums.PmeterFreqLink = driver.applications.k14Xnr5G.sense.pmeter.frequency.link.get(powerMeter = repcap.PowerMeter.Default) \n
		No command help available \n
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: coupling: No help available"""
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_str(f'SENSe:PMETer{powerMeter_cmd_val}:FREQuency:LINK?')
		return Conversions.str_to_scalar_enum(response, enums.PmeterFreqLink)
