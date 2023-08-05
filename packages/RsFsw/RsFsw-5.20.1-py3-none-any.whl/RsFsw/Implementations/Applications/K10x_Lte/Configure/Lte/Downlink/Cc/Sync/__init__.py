from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SyncCls:
	"""Sync commands group definition. 8 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sync", core, parent)

	@property
	def antenna(self):
		"""antenna commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_antenna'):
			from .Antenna import AntennaCls
			self._antenna = AntennaCls(self._core, self._cmd_group)
		return self._antenna

	@property
	def ppower(self):
		"""ppower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ppower'):
			from .Ppower import PpowerCls
			self._ppower = PpowerCls(self._core, self._cmd_group)
		return self._ppower

	@property
	def spower(self):
		"""spower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spower'):
			from .Spower import SpowerCls
			self._spower = SpowerCls(self._core, self._cmd_group)
		return self._spower

	@property
	def csWeight(self):
		"""csWeight commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_csWeight'):
			from .CsWeight import CsWeightCls
			self._csWeight = CsWeightCls(self._core, self._cmd_group)
		return self._csWeight

	def clone(self) -> 'SyncCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SyncCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
