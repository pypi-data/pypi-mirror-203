from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ErrorCls:
	"""Error commands group definition. 10 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("error", core, parent)

	@property
	def compensation(self):
		"""compensation commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_compensation'):
			from .Compensation import CompensationCls
			self._compensation = CompensationCls(self._core, self._cmd_group)
		return self._compensation

	@property
	def estimation(self):
		"""estimation commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_estimation'):
			from .Estimation import EstimationCls
			self._estimation = EstimationCls(self._core, self._cmd_group)
		return self._estimation

	def clone(self) -> 'ErrorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ErrorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
