from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............Internal.Types import DataType
from ............Internal.ArgSingleList import ArgSingleList
from ............Internal.ArgSingle import ArgSingle
from ............ import enums
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RelativeCls:
	"""Relative commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("relative", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	def set(self, sb_gaps: enums.SubBlockGaps, limit: float, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, gapChannel=repcap.GapChannel.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:GAP<gap>:MANual:LOWer:ACLR[:RELative] \n
		Snippet: driver.applications.k14Xnr5G.calculate.limit.acPower.gap.manual.lower.aclr.relative.set(sb_gaps = enums.SubBlockGaps.AB, limit = 1.0, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, gapChannel = repcap.GapChannel.Default) \n
		No command help available \n
			:param sb_gaps: No help available
			:param limit: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('sb_gaps', sb_gaps, DataType.Enum, enums.SubBlockGaps), ArgSingle('limit', limit, DataType.Float))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:GAP{gapChannel_cmd_val}:MANual:LOWer:ACLR:RELative {param}'.rstrip())

	def get(self, sb_gaps: enums.SubBlockGaps, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, gapChannel=repcap.GapChannel.Default) -> float:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:GAP<gap>:MANual:LOWer:ACLR[:RELative] \n
		Snippet: value: float = driver.applications.k14Xnr5G.calculate.limit.acPower.gap.manual.lower.aclr.relative.get(sb_gaps = enums.SubBlockGaps.AB, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, gapChannel = repcap.GapChannel.Default) \n
		No command help available \n
			:param sb_gaps: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
			:return: limit: No help available"""
		param = Conversions.enum_scalar_to_str(sb_gaps, enums.SubBlockGaps)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:GAP{gapChannel_cmd_val}:MANual:LOWer:ACLR:RELative? {param}')
		return Conversions.str_to_float(response)

	def clone(self) -> 'RelativeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RelativeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
