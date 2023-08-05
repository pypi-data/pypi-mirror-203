from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApconCls:
	"""Apcon commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apcon", core, parent)

	@property
	def a(self):
		"""a commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_a'):
			from .A import ACls
			self._a = ACls(self._core, self._cmd_group)
		return self._a

	@property
	def b(self):
		"""b commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_b'):
			from .B import BCls
			self._b = BCls(self._core, self._cmd_group)
		return self._b

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_result'):
			from .Result import ResultCls
			self._result = ResultCls(self._core, self._cmd_group)
		return self._result

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'ApconCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ApconCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
