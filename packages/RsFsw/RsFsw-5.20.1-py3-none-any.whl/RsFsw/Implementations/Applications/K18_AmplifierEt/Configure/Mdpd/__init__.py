from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MdpdCls:
	"""Mdpd commands group definition. 8 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mdpd", core, parent)

	@property
	def apply(self):
		"""apply commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_apply'):
			from .Apply import ApplyCls
			self._apply = ApplyCls(self._core, self._cmd_group)
		return self._apply

	@property
	def rms(self):
		"""rms commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rms'):
			from .Rms import RmsCls
			self._rms = RmsCls(self._core, self._cmd_group)
		return self._rms

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def waveform(self):
		"""waveform commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_waveform'):
			from .Waveform import WaveformCls
			self._waveform = WaveformCls(self._core, self._cmd_group)
		return self._waveform

	@property
	def iteration(self):
		"""iteration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iteration'):
			from .Iteration import IterationCls
			self._iteration = IterationCls(self._core, self._cmd_group)
		return self._iteration

	@property
	def order(self):
		"""order commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_order'):
			from .Order import OrderCls
			self._order = OrderCls(self._core, self._cmd_group)
		return self._order

	def clone(self) -> 'MdpdCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MdpdCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
