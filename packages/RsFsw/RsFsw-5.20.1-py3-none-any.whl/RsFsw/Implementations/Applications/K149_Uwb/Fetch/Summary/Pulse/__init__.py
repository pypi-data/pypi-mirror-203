from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PulseCls:
	"""Pulse commands group definition. 28 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pulse", core, parent)

	@property
	def location(self):
		"""location commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_location'):
			from .Location import LocationCls
			self._location = LocationCls(self._core, self._cmd_group)
		return self._location

	@property
	def mask(self):
		"""mask commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mask'):
			from .Mask import MaskCls
			self._mask = MaskCls(self._core, self._cmd_group)
		return self._mask

	@property
	def rise(self):
		"""rise commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rise'):
			from .Rise import RiseCls
			self._rise = RiseCls(self._core, self._cmd_group)
		return self._rise

	def clone(self) -> 'PulseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PulseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
