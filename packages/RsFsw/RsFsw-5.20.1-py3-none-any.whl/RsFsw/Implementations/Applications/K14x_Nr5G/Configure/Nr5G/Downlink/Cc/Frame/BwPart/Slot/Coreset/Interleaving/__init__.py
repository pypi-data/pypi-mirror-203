from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InterleavingCls:
	"""Interleaving commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("interleaving", core, parent)

	@property
	def bsize(self):
		"""bsize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bsize'):
			from .Bsize import BsizeCls
			self._bsize = BsizeCls(self._core, self._cmd_group)
		return self._bsize

	@property
	def isize(self):
		"""isize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_isize'):
			from .Isize import IsizeCls
			self._isize = IsizeCls(self._core, self._cmd_group)
		return self._isize

	@property
	def nshift(self):
		"""nshift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nshift'):
			from .Nshift import NshiftCls
			self._nshift = NshiftCls(self._core, self._cmd_group)
		return self._nshift

	@property
	def sindex(self):
		"""sindex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sindex'):
			from .Sindex import SindexCls
			self._sindex = SindexCls(self._core, self._cmd_group)
		return self._sindex

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'InterleavingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InterleavingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
