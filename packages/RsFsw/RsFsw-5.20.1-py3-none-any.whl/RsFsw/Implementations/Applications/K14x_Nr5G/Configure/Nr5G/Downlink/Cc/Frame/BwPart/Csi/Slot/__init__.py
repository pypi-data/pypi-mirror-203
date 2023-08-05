from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SlotCls:
	"""Slot commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slot", core, parent)

	@property
	def aperiodic(self):
		"""aperiodic commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aperiodic'):
			from .Aperiodic import AperiodicCls
			self._aperiodic = AperiodicCls(self._core, self._cmd_group)
		return self._aperiodic

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import ModeCls
			self._mode = ModeCls(self._core, self._cmd_group)
		return self._mode

	@property
	def periodicity(self):
		"""periodicity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_periodicity'):
			from .Periodicity import PeriodicityCls
			self._periodicity = PeriodicityCls(self._core, self._cmd_group)
		return self._periodicity

	@property
	def poffset(self):
		"""poffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_poffset'):
			from .Poffset import PoffsetCls
			self._poffset = PoffsetCls(self._core, self._cmd_group)
		return self._poffset

	def clone(self) -> 'SlotCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SlotCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
