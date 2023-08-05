from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RateCls:
	"""Rate commands group definition. 4 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rate", core, parent)

	@property
	def apackets(self):
		"""apackets commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apackets'):
			from .Apackets import ApacketsCls
			self._apackets = ApacketsCls(self._core, self._cmd_group)
		return self._apackets

	@property
	def phr(self):
		"""phr commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_phr'):
			from .Phr import PhrCls
			self._phr = PhrCls(self._core, self._cmd_group)
		return self._phr

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: FETCh<n>:PACKet:DATA:DATA:RATE \n
		Snippet: value: float = driver.applications.k149Uwb.fetch.packet.data.data.rate.get(window = repcap.Window.Default) \n
		Returns the payload of the packet in hexadecimal format. In accordance with IEEE 802.15.4, the LSB of each octet of the
		payload is output first. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fetch')
			:return: result: Use n to select a 'Packet Insights' result display. Window"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'FETCh{window_cmd_val}:PACKet:DATA:DATA:RATE?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'RateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
