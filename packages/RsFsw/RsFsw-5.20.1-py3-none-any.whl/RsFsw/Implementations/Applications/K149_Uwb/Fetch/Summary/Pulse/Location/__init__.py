from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LocationCls:
	"""Location commands group definition. 12 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("location", core, parent)

	@property
	def sfd(self):
		"""sfd commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfd'):
			from .Sfd import SfdCls
			self._sfd = SfdCls(self._core, self._cmd_group)
		return self._sfd

	@property
	def sts(self):
		"""sts commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_sts'):
			from .Sts import StsCls
			self._sts = StsCls(self._core, self._cmd_group)
		return self._sts

	@property
	def sync(self):
		"""sync commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import SyncCls
			self._sync = SyncCls(self._core, self._cmd_group)
		return self._sync

	def clone(self) -> 'LocationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LocationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
