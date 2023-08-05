from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SenseCls:
	"""Sense commands group definition. 68 total commands, 16 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sense", core, parent)

	@property
	def ademod(self):
		"""ademod commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_ademod'):
			from .Ademod import AdemodCls
			self._ademod = AdemodCls(self._core, self._cmd_group)
		return self._ademod

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
	def rawPhase(self):
		"""rawPhase commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rawPhase'):
			from .RawPhase import RawPhaseCls
			self._rawPhase = RawPhaseCls(self._core, self._cmd_group)
		return self._rawPhase

	@property
	def adjust(self):
		"""adjust commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_adjust'):
			from .Adjust import AdjustCls
			self._adjust = AdjustCls(self._core, self._cmd_group)
		return self._adjust

	@property
	def bandwidth(self):
		"""bandwidth commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import BandwidthCls
			self._bandwidth = BandwidthCls(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def frequency(self):
		"""frequency commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def carrier(self):
		"""carrier commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import CarrierCls
			self._carrier = CarrierCls(self._core, self._cmd_group)
		return self._carrier

	@property
	def clock(self):
		"""clock commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_clock'):
			from .Clock import ClockCls
			self._clock = ClockCls(self._core, self._cmd_group)
		return self._clock

	@property
	def sweep(self):
		"""sweep commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sweep'):
			from .Sweep import SweepCls
			self._sweep = SweepCls(self._core, self._cmd_group)
		return self._sweep

	@property
	def average(self):
		"""average commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_average'):
			from .Average import AverageCls
			self._average = AverageCls(self._core, self._cmd_group)
		return self._average

	@property
	def subspan(self):
		"""subspan commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_subspan'):
			from .Subspan import SubspanCls
			self._subspan = SubspanCls(self._core, self._cmd_group)
		return self._subspan

	@property
	def mtime(self):
		"""mtime commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mtime'):
			from .Mtime import MtimeCls
			self._mtime = MtimeCls(self._core, self._cmd_group)
		return self._mtime

	@property
	def rlength(self):
		"""rlength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rlength'):
			from .Rlength import RlengthCls
			self._rlength = RlengthCls(self._core, self._cmd_group)
		return self._rlength

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRateCls
			self._symbolRate = SymbolRateCls(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def cestimation(self):
		"""cestimation commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_cestimation'):
			from .Cestimation import CestimationCls
			self._cestimation = CestimationCls(self._core, self._cmd_group)
		return self._cestimation

	def clone(self) -> 'SenseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SenseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
