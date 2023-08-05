from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrsCls:
	"""Prs commands group definition. 10 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prs", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def slot(self):
		"""slot commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_slot'):
			from .Slot import SlotCls
			self._slot = SlotCls(self._core, self._cmd_group)
		return self._slot

	@property
	def noRbs(self):
		"""noRbs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noRbs'):
			from .NoRbs import NoRbsCls
			self._noRbs = NoRbsCls(self._core, self._cmd_group)
		return self._noRbs

	@property
	def srb(self):
		"""srb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srb'):
			from .Srb import SrbCls
			self._srb = SrbCls(self._core, self._cmd_group)
		return self._srb

	@property
	def lpStart(self):
		"""lpStart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lpStart'):
			from .LpStart import LpStartCls
			self._lpStart = LpStartCls(self._core, self._cmd_group)
		return self._lpStart

	@property
	def lprs(self):
		"""lprs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lprs'):
			from .Lprs import LprsCls
			self._lprs = LprsCls(self._core, self._cmd_group)
		return self._lprs

	@property
	def npId(self):
		"""npId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_npId'):
			from .NpId import NpIdCls
			self._npId = NpIdCls(self._core, self._cmd_group)
		return self._npId

	@property
	def kpComb(self):
		"""kpComb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_kpComb'):
			from .KpComb import KpCombCls
			self._kpComb = KpCombCls(self._core, self._cmd_group)
		return self._kpComb

	@property
	def kpOffset(self):
		"""kpOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_kpOffset'):
			from .KpOffset import KpOffsetCls
			self._kpOffset = KpOffsetCls(self._core, self._cmd_group)
		return self._kpOffset

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	def clone(self) -> 'PrsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PrsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
