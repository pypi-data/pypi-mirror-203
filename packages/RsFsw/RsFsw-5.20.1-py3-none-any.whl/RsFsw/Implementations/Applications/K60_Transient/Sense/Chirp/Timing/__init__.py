from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TimingCls:
	"""Timing commands group definition. 20 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("timing", core, parent)

	@property
	def begin(self):
		"""begin commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_begin'):
			from .Begin import BeginCls
			self._begin = BeginCls(self._core, self._cmd_group)
		return self._begin

	@property
	def length(self):
		"""length commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_length'):
			from .Length import LengthCls
			self._length = LengthCls(self._core, self._cmd_group)
		return self._length

	@property
	def switching(self):
		"""switching commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_switching'):
			from .Switching import SwitchingCls
			self._switching = SwitchingCls(self._core, self._cmd_group)
		return self._switching

	@property
	def rate(self):
		"""rate commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_rate'):
			from .Rate import RateCls
			self._rate = RateCls(self._core, self._cmd_group)
		return self._rate

	def clone(self) -> 'TimingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TimingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
