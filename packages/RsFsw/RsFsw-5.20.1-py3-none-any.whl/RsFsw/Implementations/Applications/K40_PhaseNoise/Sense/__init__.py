from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SenseCls:
	"""Sense commands group definition. 68 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sense", core, parent)

	@property
	def probe(self):
		"""probe commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_probe'):
			from .Probe import ProbeCls
			self._probe = ProbeCls(self._core, self._cmd_group)
		return self._probe

	@property
	def frequency(self):
		"""frequency commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def listPy(self):
		"""listPy commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPyCls
			self._listPy = ListPyCls(self._core, self._cmd_group)
		return self._listPy

	@property
	def power(self):
		"""power commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def sweep(self):
		"""sweep commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_sweep'):
			from .Sweep import SweepCls
			self._sweep = SweepCls(self._core, self._cmd_group)
		return self._sweep

	@property
	def adjust(self):
		"""adjust commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_adjust'):
			from .Adjust import AdjustCls
			self._adjust = AdjustCls(self._core, self._cmd_group)
		return self._adjust

	@property
	def spurs(self):
		"""spurs commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_spurs'):
			from .Spurs import SpursCls
			self._spurs = SpursCls(self._core, self._cmd_group)
		return self._spurs

	@property
	def reject(self):
		"""reject commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_reject'):
			from .Reject import RejectCls
			self._reject = RejectCls(self._core, self._cmd_group)
		return self._reject

	@property
	def iq(self):
		"""iq commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_iq'):
			from .Iq import IqCls
			self._iq = IqCls(self._core, self._cmd_group)
		return self._iq

	@property
	def mixer(self):
		"""mixer commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_mixer'):
			from .Mixer import MixerCls
			self._mixer = MixerCls(self._core, self._cmd_group)
		return self._mixer

	def clone(self) -> 'SenseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SenseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
