from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Utilities import trim_str_response
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApacketsCls:
	"""Apackets commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apackets", core, parent)

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: FETCh<n>:PACKet:SYNC:SYNC:LENGth:PHR:APACkets \n
		Snippet: value: str = driver.applications.k149Uwb.fetch.packet.sync.sync.length.phr.apackets.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fetch')
			:return: result: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'FETCh{window_cmd_val}:PACKet:SYNC:SYNC:LENGth:PHR:APACkets?')
		return trim_str_response(response)
