from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	def set(self, test_model: str, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: MMEMory:LOAD[:CC<cc>]:TMOD:DL \n
		Snippet: driver.applications.k10Xlte.massMemory.load.cc.tmod.downlink.set(test_model = '1', carrierComponent = repcap.CarrierComponent.Default) \n
		This command loads an EUTRA test model (E-TM) . The EUTRA test models are in accordance with 3GPP 36.141. You can also
		select an O-RAN test case with the command. \n
			:param test_model: string String that contains the name of the test model, e.g. 'E-TM1_1__20MHz' (E-TM1.1) . To select a test model for a different bandwidth, replace '20MHz' with either '1_4MHz', '3MHz', '5MHz', '10MHz' or '15MHz'. Alternatively, a string that contains the name of the O-RAN test case, e.g. 'TC 3.2.3.7.1'.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.value_to_quoted_str(test_model)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'MMEMory:LOAD:CC{carrierComponent_cmd_val}:TMOD:DL {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> str:
		"""SCPI: MMEMory:LOAD[:CC<cc>]:TMOD:DL \n
		Snippet: value: str = driver.applications.k10Xlte.massMemory.load.cc.tmod.downlink.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command loads an EUTRA test model (E-TM) . The EUTRA test models are in accordance with 3GPP 36.141. You can also
		select an O-RAN test case with the command. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: test_model: string String that contains the name of the test model, e.g. 'E-TM1_1__20MHz' (E-TM1.1) . To select a test model for a different bandwidth, replace '20MHz' with either '1_4MHz', '3MHz', '5MHz', '10MHz' or '15MHz'. Alternatively, a string that contains the name of the O-RAN test case, e.g. 'TC 3.2.3.7.1'."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'MMEMory:LOAD:CC{carrierComponent_cmd_val}:TMOD:DL?')
		return trim_str_response(response)
