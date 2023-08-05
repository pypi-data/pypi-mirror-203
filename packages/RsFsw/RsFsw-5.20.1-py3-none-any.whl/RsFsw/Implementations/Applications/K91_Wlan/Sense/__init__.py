from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SenseCls:
	"""Sense commands group definition. 113 total commands, 13 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sense", core, parent)

	@property
	def adjust(self):
		"""adjust commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_adjust'):
			from .Adjust import AdjustCls
			self._adjust = AdjustCls(self._core, self._cmd_group)
		return self._adjust

	@property
	def power(self):
		"""power commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def average(self):
		"""average commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_average'):
			from .Average import AverageCls
			self._average = AverageCls(self._core, self._cmd_group)
		return self._average

	@property
	def frequency(self):
		"""frequency commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def iq(self):
		"""iq commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iq'):
			from .Iq import IqCls
			self._iq = IqCls(self._core, self._cmd_group)
		return self._iq

	@property
	def probe(self):
		"""probe commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_probe'):
			from .Probe import ProbeCls
			self._probe = ProbeCls(self._core, self._cmd_group)
		return self._probe

	@property
	def sweep(self):
		"""sweep commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_sweep'):
			from .Sweep import SweepCls
			self._sweep = SweepCls(self._core, self._cmd_group)
		return self._sweep

	@property
	def demod(self):
		"""demod commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_demod'):
			from .Demod import DemodCls
			self._demod = DemodCls(self._core, self._cmd_group)
		return self._demod

	@property
	def burst(self):
		"""burst commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_burst'):
			from .Burst import BurstCls
			self._burst = BurstCls(self._core, self._cmd_group)
		return self._burst

	@property
	def swapIq(self):
		"""swapIq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_swapIq'):
			from .SwapIq import SwapIqCls
			self._swapIq = SwapIqCls(self._core, self._cmd_group)
		return self._swapIq

	@property
	def tracking(self):
		"""tracking commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_tracking'):
			from .Tracking import TrackingCls
			self._tracking = TrackingCls(self._core, self._cmd_group)
		return self._tracking

	@property
	def mixer(self):
		"""mixer commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_mixer'):
			from .Mixer import MixerCls
			self._mixer = MixerCls(self._core, self._cmd_group)
		return self._mixer

	@property
	def window(self):
		"""window commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_window'):
			from .Window import WindowCls
			self._window = WindowCls(self._core, self._cmd_group)
		return self._window

	def clone(self) -> 'SenseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SenseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
