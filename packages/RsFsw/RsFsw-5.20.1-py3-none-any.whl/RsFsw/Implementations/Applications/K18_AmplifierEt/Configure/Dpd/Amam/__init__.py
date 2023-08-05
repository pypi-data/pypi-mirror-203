from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AmamCls:
	"""Amam commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("amam", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def ledState(self):
		"""ledState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ledState'):
			from .LedState import LedStateCls
			self._ledState = LedStateCls(self._core, self._cmd_group)
		return self._ledState

	@property
	def morder(self):
		"""morder commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_morder'):
			from .Morder import MorderCls
			self._morder = MorderCls(self._core, self._cmd_group)
		return self._morder

	def clone(self) -> 'AmamCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AmamCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
