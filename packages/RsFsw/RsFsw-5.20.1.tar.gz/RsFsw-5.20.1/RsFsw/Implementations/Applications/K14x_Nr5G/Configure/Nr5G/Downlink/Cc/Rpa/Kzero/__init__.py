from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class KzeroCls:
	"""Kzero commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("kzero", core, parent)

	@property
	def scfe(self):
		"""scfe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scfe'):
			from .Scfe import ScfeCls
			self._scfe = ScfeCls(self._core, self._cmd_group)
		return self._scfe

	@property
	def scft(self):
		"""scft commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scft'):
			from .Scft import ScftCls
			self._scft = ScftCls(self._core, self._cmd_group)
		return self._scft

	@property
	def scns(self):
		"""scns commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scns'):
			from .Scns import ScnsCls
			self._scns = ScnsCls(self._core, self._cmd_group)
		return self._scns

	@property
	def scot(self):
		"""scot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scot'):
			from .Scot import ScotCls
			self._scot = ScotCls(self._core, self._cmd_group)
		return self._scot

	@property
	def scst(self):
		"""scst commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scst'):
			from .Scst import ScstCls
			self._scst = ScstCls(self._core, self._cmd_group)
		return self._scst

	@property
	def sctt(self):
		"""sctt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sctt'):
			from .Sctt import ScttCls
			self._sctt = ScttCls(self._core, self._cmd_group)
		return self._sctt

	def clone(self) -> 'KzeroCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = KzeroCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
