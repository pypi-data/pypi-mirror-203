from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PspectrumCls:
	"""Pspectrum commands group definition. 13 total commands, 13 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pspectrum", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import AutoCls
			self._auto = AutoCls(self._core, self._cmd_group)
		return self._auto

	@property
	def maxFrequency(self):
		"""maxFrequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maxFrequency'):
			from .MaxFrequency import MaxFrequencyCls
			self._maxFrequency = MaxFrequencyCls(self._core, self._cmd_group)
		return self._maxFrequency

	@property
	def window(self):
		"""window commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_window'):
			from .Window import WindowCls
			self._window = WindowCls(self._core, self._cmd_group)
		return self._window

	@property
	def blockSize(self):
		"""blockSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_blockSize'):
			from .BlockSize import BlockSizeCls
			self._blockSize = BlockSizeCls(self._core, self._cmd_group)
		return self._blockSize

	@property
	def gthreshold(self):
		"""gthreshold commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gthreshold'):
			from .Gthreshold import GthresholdCls
			self._gthreshold = GthresholdCls(self._core, self._cmd_group)
		return self._gthreshold

	@property
	def sthreshold(self):
		"""sthreshold commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sthreshold'):
			from .Sthreshold import SthresholdCls
			self._sthreshold = SthresholdCls(self._core, self._cmd_group)
		return self._sthreshold

	@property
	def rbw(self):
		"""rbw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbw'):
			from .Rbw import RbwCls
			self._rbw = RbwCls(self._core, self._cmd_group)
		return self._rbw

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def phase(self):
		"""phase commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import PhaseCls
			self._phase = PhaseCls(self._core, self._cmd_group)
		return self._phase

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def timing(self):
		"""timing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_timing'):
			from .Timing import TimingCls
			self._timing = TimingCls(self._core, self._cmd_group)
		return self._timing

	@property
	def emodel(self):
		"""emodel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_emodel'):
			from .Emodel import EmodelCls
			self._emodel = EmodelCls(self._core, self._cmd_group)
		return self._emodel

	@property
	def tsidelobe(self):
		"""tsidelobe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tsidelobe'):
			from .Tsidelobe import TsidelobeCls
			self._tsidelobe = TsidelobeCls(self._core, self._cmd_group)
		return self._tsidelobe

	def clone(self) -> 'PspectrumCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PspectrumCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
