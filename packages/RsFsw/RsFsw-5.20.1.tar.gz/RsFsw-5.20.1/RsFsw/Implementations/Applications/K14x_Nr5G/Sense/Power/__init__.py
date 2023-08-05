from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerCls:
	"""Power commands group definition. 84 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def achannel(self):
		"""achannel commands group. 16 Sub-classes, 1 commands."""
		if not hasattr(self, '_achannel'):
			from .Achannel import AchannelCls
			self._achannel = AchannelCls(self._core, self._cmd_group)
		return self._achannel

	@property
	def aclr(self):
		"""aclr commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_aclr'):
			from .Aclr import AclrCls
			self._aclr = AclrCls(self._core, self._cmd_group)
		return self._aclr

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import BandwidthCls
			self._bandwidth = BandwidthCls(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def category(self):
		"""category commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_category'):
			from .Category import CategoryCls
			self._category = CategoryCls(self._core, self._cmd_group)
		return self._category

	@property
	def hspeed(self):
		"""hspeed commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hspeed'):
			from .Hspeed import HspeedCls
			self._hspeed = HspeedCls(self._core, self._cmd_group)
		return self._hspeed

	@property
	def ncorrection(self):
		"""ncorrection commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ncorrection'):
			from .Ncorrection import NcorrectionCls
			self._ncorrection = NcorrectionCls(self._core, self._cmd_group)
		return self._ncorrection

	@property
	def pclass(self):
		"""pclass commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pclass'):
			from .Pclass import PclassCls
			self._pclass = PclassCls(self._core, self._cmd_group)
		return self._pclass

	@property
	def sem(self):
		"""sem commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_sem'):
			from .Sem import SemCls
			self._sem = SemCls(self._core, self._cmd_group)
		return self._sem

	@property
	def tid(self):
		"""tid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tid'):
			from .Tid import TidCls
			self._tid = TidCls(self._core, self._cmd_group)
		return self._tid

	@property
	def trace(self):
		"""trace commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import TraceCls
			self._trace = TraceCls(self._core, self._cmd_group)
		return self._trace

	def clone(self) -> 'PowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
