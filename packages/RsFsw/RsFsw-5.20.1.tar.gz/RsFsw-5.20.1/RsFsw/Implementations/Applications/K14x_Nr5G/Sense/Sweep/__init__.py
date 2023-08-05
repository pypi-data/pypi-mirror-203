from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SweepCls:
	"""Sweep commands group definition. 27 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sweep", core, parent)

	@property
	def count(self):
		"""count commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import CountCls
			self._count = CountCls(self._core, self._cmd_group)
		return self._count

	@property
	def duration(self):
		"""duration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_duration'):
			from .Duration import DurationCls
			self._duration = DurationCls(self._core, self._cmd_group)
		return self._duration

	@property
	def egate(self):
		"""egate commands group. 9 Sub-classes, 1 commands."""
		if not hasattr(self, '_egate'):
			from .Egate import EgateCls
			self._egate = EgateCls(self._core, self._cmd_group)
		return self._egate

	@property
	def event(self):
		"""event commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_event'):
			from .Event import EventCls
			self._event = EventCls(self._core, self._cmd_group)
		return self._event

	@property
	def lcapture(self):
		"""lcapture commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lcapture'):
			from .Lcapture import LcaptureCls
			self._lcapture = LcaptureCls(self._core, self._cmd_group)
		return self._lcapture

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import ModeCls
			self._mode = ModeCls(self._core, self._cmd_group)
		return self._mode

	@property
	def optimize(self):
		"""optimize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_optimize'):
			from .Optimize import OptimizeCls
			self._optimize = OptimizeCls(self._core, self._cmd_group)
		return self._optimize

	@property
	def scapture(self):
		"""scapture commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_scapture'):
			from .Scapture import ScaptureCls
			self._scapture = ScaptureCls(self._core, self._cmd_group)
		return self._scapture

	@property
	def time(self):
		"""time commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_time'):
			from .Time import TimeCls
			self._time = TimeCls(self._core, self._cmd_group)
		return self._time

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePyCls
			self._typePy = TypePyCls(self._core, self._cmd_group)
		return self._typePy

	def clone(self) -> 'SweepCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SweepCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
