from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SyncCls:
	"""Sync commands group definition. 14 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sync", core, parent)

	@property
	def code(self):
		"""code commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_code'):
			from .Code import CodeCls
			self._code = CodeCls(self._core, self._cmd_group)
		return self._code

	@property
	def delta(self):
		"""delta commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_delta'):
			from .Delta import DeltaCls
			self._delta = DeltaCls(self._core, self._cmd_group)
		return self._delta

	@property
	def sfd(self):
		"""sfd commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfd'):
			from .Sfd import SfdCls
			self._sfd = SfdCls(self._core, self._cmd_group)
		return self._sfd

	@property
	def sync(self):
		"""sync commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import SyncCls
			self._sync = SyncCls(self._core, self._cmd_group)
		return self._sync

	def clone(self) -> 'SyncCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SyncCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
