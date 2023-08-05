from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrameCls:
	"""Frame commands group definition. 8 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frame", core, parent)

	@property
	def count(self):
		"""count commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import CountCls
			self._count = CountCls(self._core, self._cmd_group)
		return self._count

	@property
	def optimization(self):
		"""optimization commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_optimization'):
			from .Optimization import OptimizationCls
			self._optimization = OptimizationCls(self._core, self._cmd_group)
		return self._optimization

	@property
	def saLevel(self):
		"""saLevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_saLevel'):
			from .SaLevel import SaLevelCls
			self._saLevel = SaLevelCls(self._core, self._cmd_group)
		return self._saLevel

	@property
	def scount(self):
		"""scount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scount'):
			from .Scount import ScountCls
			self._scount = ScountCls(self._core, self._cmd_group)
		return self._scount

	@property
	def slot(self):
		"""slot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slot'):
			from .Slot import SlotCls
			self._slot = SlotCls(self._core, self._cmd_group)
		return self._slot

	@property
	def srSlot(self):
		"""srSlot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srSlot'):
			from .SrSlot import SrSlotCls
			self._srSlot = SrSlotCls(self._core, self._cmd_group)
		return self._srSlot

	def clone(self) -> 'FrameCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FrameCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
