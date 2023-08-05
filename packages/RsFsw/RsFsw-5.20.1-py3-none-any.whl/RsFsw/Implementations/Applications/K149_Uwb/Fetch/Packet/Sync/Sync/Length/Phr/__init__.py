from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhrCls:
	"""Phr commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phr", core, parent)

	@property
	def apackets(self):
		"""apackets commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apackets'):
			from .Apackets import ApacketsCls
			self._apackets = ApacketsCls(self._core, self._cmd_group)
		return self._apackets

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: FETCh<n>:PACKet:SYNC:SYNC:LENGth:PHR \n
		Snippet: value: float = driver.applications.k149Uwb.fetch.packet.sync.sync.length.phr.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fetch')
			:return: result: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'FETCh{window_cmd_val}:PACKet:SYNC:SYNC:LENGth:PHR?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'PhrCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PhrCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
