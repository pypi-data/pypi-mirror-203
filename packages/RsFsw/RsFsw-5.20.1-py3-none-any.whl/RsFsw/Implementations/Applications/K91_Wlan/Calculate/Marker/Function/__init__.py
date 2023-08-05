from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FunctionCls:
	"""Function commands group definition. 6 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("function", core, parent)

	@property
	def power(self):
		"""power commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def center(self):
		"""center commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_center'):
			from .Center import CenterCls
			self._center = CenterCls(self._core, self._cmd_group)
		return self._center

	@property
	def zoom(self):
		"""zoom commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_zoom'):
			from .Zoom import ZoomCls
			self._zoom = ZoomCls(self._core, self._cmd_group)
		return self._zoom

	def clone(self) -> 'FunctionCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FunctionCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
