from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SettingsCls:
	"""Settings commands group definition. 2 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("settings", core, parent)

	@property
	def npratio(self):
		"""npratio commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_npratio'):
			from .Npratio import NpratioCls
			self._npratio = NpratioCls(self._core, self._cmd_group)
		return self._npratio

	def clone(self) -> 'SettingsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SettingsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
