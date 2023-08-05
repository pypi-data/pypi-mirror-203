from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DemodCls:
	"""Demod commands group definition. 13 total commands, 13 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demod", core, parent)

	@property
	def acon(self):
		"""acon commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acon'):
			from .Acon import AconCls
			self._acon = AconCls(self._core, self._cmd_group)
		return self._acon

	@property
	def attSlots(self):
		"""attSlots commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_attSlots'):
			from .AttSlots import AttSlotsCls
			self._attSlots = AttSlotsCls(self._core, self._cmd_group)
		return self._attSlots

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import AutoCls
			self._auto = AutoCls(self._core, self._cmd_group)
		return self._auto

	@property
	def cbScrambling(self):
		"""cbScrambling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbScrambling'):
			from .CbScrambling import CbScramblingCls
			self._cbScrambling = CbScramblingCls(self._core, self._cmd_group)
		return self._cbScrambling

	@property
	def cdcOffset(self):
		"""cdcOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cdcOffset'):
			from .CdcOffset import CdcOffsetCls
			self._cdcOffset = CdcOffsetCls(self._core, self._cmd_group)
		return self._cdcOffset

	@property
	def cestimation(self):
		"""cestimation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cestimation'):
			from .Cestimation import CestimationCls
			self._cestimation = CestimationCls(self._core, self._cmd_group)
		return self._cestimation

	@property
	def dummy(self):
		"""dummy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dummy'):
			from .Dummy import DummyCls
			self._dummy = DummyCls(self._core, self._cmd_group)
		return self._dummy

	@property
	def eePeriod(self):
		"""eePeriod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eePeriod'):
			from .EePeriod import EePeriodCls
			self._eePeriod = EePeriodCls(self._core, self._cmd_group)
		return self._eePeriod

	@property
	def loFrequency(self):
		"""loFrequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_loFrequency'):
			from .LoFrequency import LoFrequencyCls
			self._loFrequency = LoFrequencyCls(self._core, self._cmd_group)
		return self._loFrequency

	@property
	def loLocation(self):
		"""loLocation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_loLocation'):
			from .LoLocation import LoLocationCls
			self._loLocation = LoLocationCls(self._core, self._cmd_group)
		return self._loLocation

	@property
	def mcFilter(self):
		"""mcFilter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcFilter'):
			from .McFilter import McFilterCls
			self._mcFilter = McFilterCls(self._core, self._cmd_group)
		return self._mcFilter

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import ModeCls
			self._mode = ModeCls(self._core, self._cmd_group)
		return self._mode

	@property
	def siSync(self):
		"""siSync commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_siSync'):
			from .SiSync import SiSyncCls
			self._siSync = SiSyncCls(self._core, self._cmd_group)
		return self._siSync

	def clone(self) -> 'DemodCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DemodCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
