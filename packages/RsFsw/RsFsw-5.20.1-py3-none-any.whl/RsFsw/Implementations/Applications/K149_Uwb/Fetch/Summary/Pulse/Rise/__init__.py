from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RiseCls:
	"""Rise commands group definition. 12 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rise", core, parent)

	@property
	def monotonic(self):
		"""monotonic commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_monotonic'):
			from .Monotonic import MonotonicCls
			self._monotonic = MonotonicCls(self._core, self._cmd_group)
		return self._monotonic

	@property
	def time(self):
		"""time commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import TimeCls
			self._time = TimeCls(self._core, self._cmd_group)
		return self._time

	def clone(self) -> 'RiseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RiseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
