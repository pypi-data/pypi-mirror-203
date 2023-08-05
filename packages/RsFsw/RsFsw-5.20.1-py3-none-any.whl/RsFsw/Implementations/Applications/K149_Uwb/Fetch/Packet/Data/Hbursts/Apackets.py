from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApacketsCls:
	"""Apackets commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apackets", core, parent)

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: FETCh<n>:PACKet:DATA:HBURsts:APACkets \n
		Snippet: value: str = driver.applications.k149Uwb.fetch.packet.data.hbursts.apackets.get(window = repcap.Window.Default) \n
		Returns the payload of the packet in hexadecimal format. In accordance with IEEE 802.15.4, the LSB of each octet of the
		payload is output first. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fetch')
			:return: result: Use n to select a 'Packet Insights' result display. Window"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'FETCh{window_cmd_val}:PACKet:DATA:HBURsts:APACkets?')
		return trim_str_response(response)
