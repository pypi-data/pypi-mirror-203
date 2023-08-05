from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PtrsCls:
	"""Ptrs commands group definition. 9 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptrs", core, parent)

	@property
	def k(self):
		"""k commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_k'):
			from .K import KCls
			self._k = KCls(self._core, self._cmd_group)
		return self._k

	@property
	def lpy(self):
		"""lpy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lpy'):
			from .Lpy import LpyCls
			self._lpy = LpyCls(self._core, self._cmd_group)
		return self._lpy

	@property
	def ngroups(self):
		"""ngroups commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ngroups'):
			from .Ngroups import NgroupsCls
			self._ngroups = NgroupsCls(self._core, self._cmd_group)
		return self._ngroups

	@property
	def nid(self):
		"""nid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nid'):
			from .Nid import NidCls
			self._nid = NidCls(self._core, self._cmd_group)
		return self._nid

	@property
	def niId(self):
		"""niId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_niId'):
			from .NiId import NiIdCls
			self._niId = NiIdCls(self._core, self._cmd_group)
		return self._niId

	@property
	def nsamples(self):
		"""nsamples commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsamples'):
			from .Nsamples import NsamplesCls
			self._nsamples = NsamplesCls(self._core, self._cmd_group)
		return self._nsamples

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def reOffset(self):
		"""reOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reOffset'):
			from .ReOffset import ReOffsetCls
			self._reOffset = ReOffsetCls(self._core, self._cmd_group)
		return self._reOffset

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'PtrsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PtrsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
