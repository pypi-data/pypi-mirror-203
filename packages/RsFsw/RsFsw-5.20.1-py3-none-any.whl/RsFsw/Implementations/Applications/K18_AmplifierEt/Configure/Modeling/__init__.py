from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModelingCls:
	"""Modeling commands group definition. 9 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modeling", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def amam(self):
		"""amam commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_amam'):
			from .Amam import AmamCls
			self._amam = AmamCls(self._core, self._cmd_group)
		return self._amam

	@property
	def amPm(self):
		"""amPm commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_amPm'):
			from .AmPm import AmPmCls
			self._amPm = AmPmCls(self._core, self._cmd_group)
		return self._amPm

	@property
	def lrange(self):
		"""lrange commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lrange'):
			from .Lrange import LrangeCls
			self._lrange = LrangeCls(self._core, self._cmd_group)
		return self._lrange

	@property
	def npoints(self):
		"""npoints commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_npoints'):
			from .Npoints import NpointsCls
			self._npoints = NpointsCls(self._core, self._cmd_group)
		return self._npoints

	@property
	def scale(self):
		"""scale commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scale'):
			from .Scale import ScaleCls
			self._scale = ScaleCls(self._core, self._cmd_group)
		return self._scale

	@property
	def sequence(self):
		"""sequence commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sequence'):
			from .Sequence import SequenceCls
			self._sequence = SequenceCls(self._core, self._cmd_group)
		return self._sequence

	def clone(self) -> 'ModelingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ModelingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
