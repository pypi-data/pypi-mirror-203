from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TrackingCls:
	"""Tracking commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tracking", core, parent)

	@property
	def iqMcomp(self):
		"""iqMcomp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqMcomp'):
			from .IqMcomp import IqMcompCls
			self._iqMcomp = IqMcompCls(self._core, self._cmd_group)
		return self._iqMcomp

	@property
	def level(self):
		"""level commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_level'):
			from .Level import LevelCls
			self._level = LevelCls(self._core, self._cmd_group)
		return self._level

	@property
	def phase(self):
		"""phase commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import PhaseCls
			self._phase = PhaseCls(self._core, self._cmd_group)
		return self._phase

	def clone(self) -> 'TrackingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TrackingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
