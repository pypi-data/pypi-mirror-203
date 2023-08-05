from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TrendCls:
	"""Trend commands group definition. 21 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trend", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def llines(self):
		"""llines commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_llines'):
			from .Llines import LlinesCls
			self._llines = LlinesCls(self._core, self._cmd_group)
		return self._llines

	@property
	def phase(self):
		"""phase commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import PhaseCls
			self._phase = PhaseCls(self._core, self._cmd_group)
		return self._phase

	@property
	def power(self):
		"""power commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def timing(self):
		"""timing commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_timing'):
			from .Timing import TimingCls
			self._timing = TimingCls(self._core, self._cmd_group)
		return self._timing

	@property
	def emodel(self):
		"""emodel commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_emodel'):
			from .Emodel import EmodelCls
			self._emodel = EmodelCls(self._core, self._cmd_group)
		return self._emodel

	@property
	def stability(self):
		"""stability commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stability'):
			from .Stability import StabilityCls
			self._stability = StabilityCls(self._core, self._cmd_group)
		return self._stability

	@property
	def tsidelobe(self):
		"""tsidelobe commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_tsidelobe'):
			from .Tsidelobe import TsidelobeCls
			self._tsidelobe = TsidelobeCls(self._core, self._cmd_group)
		return self._tsidelobe

	@property
	def dstyle(self):
		"""dstyle commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dstyle'):
			from .Dstyle import DstyleCls
			self._dstyle = DstyleCls(self._core, self._cmd_group)
		return self._dstyle

	def clone(self) -> 'TrendCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TrendCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
