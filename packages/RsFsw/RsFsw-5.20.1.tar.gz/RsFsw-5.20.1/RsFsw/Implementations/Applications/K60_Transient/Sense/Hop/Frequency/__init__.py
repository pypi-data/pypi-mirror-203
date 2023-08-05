from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 30 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def fmError(self):
		"""fmError commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_fmError'):
			from .FmError import FmErrorCls
			self._fmError = FmErrorCls(self._core, self._cmd_group)
		return self._fmError

	@property
	def maxFm(self):
		"""maxFm commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_maxFm'):
			from .MaxFm import MaxFmCls
			self._maxFm = MaxFmCls(self._core, self._cmd_group)
		return self._maxFm

	@property
	def rmsFm(self):
		"""rmsFm commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmsFm'):
			from .RmsFm import RmsFmCls
			self._rmsFm = RmsFmCls(self._core, self._cmd_group)
		return self._rmsFm

	@property
	def avgFm(self):
		"""avgFm commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_avgFm'):
			from .AvgFm import AvgFmCls
			self._avgFm = AvgFmCls(self._core, self._cmd_group)
		return self._avgFm

	@property
	def relFrequency(self):
		"""relFrequency commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_relFrequency'):
			from .RelFrequency import RelFrequencyCls
			self._relFrequency = RelFrequencyCls(self._core, self._cmd_group)
		return self._relFrequency

	def clone(self) -> 'FrequencyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FrequencyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
