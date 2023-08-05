from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 12 total commands, 12 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def all(self):
		"""all commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	@property
	def avgFm(self):
		"""avgFm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_avgFm'):
			from .AvgFm import AvgFmCls
			self._avgFm = AvgFmCls(self._core, self._cmd_group)
		return self._avgFm

	@property
	def avgNonlinear(self):
		"""avgNonlinear commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_avgNonlinear'):
			from .AvgNonlinear import AvgNonlinearCls
			self._avgNonlinear = AvgNonlinearCls(self._core, self._cmd_group)
		return self._avgNonlinear

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import BandwidthCls
			self._bandwidth = BandwidthCls(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def chError(self):
		"""chError commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_chError'):
			from .ChError import ChErrorCls
			self._chError = ChErrorCls(self._core, self._cmd_group)
		return self._chError

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def maxFm(self):
		"""maxFm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maxFm'):
			from .MaxFm import MaxFmCls
			self._maxFm = MaxFmCls(self._core, self._cmd_group)
		return self._maxFm

	@property
	def maxNonlinear(self):
		"""maxNonlinear commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maxNonlinear'):
			from .MaxNonlinear import MaxNonlinearCls
			self._maxNonlinear = MaxNonlinearCls(self._core, self._cmd_group)
		return self._maxNonlinear

	@property
	def rmsFm(self):
		"""rmsFm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmsFm'):
			from .RmsFm import RmsFmCls
			self._rmsFm = RmsFmCls(self._core, self._cmd_group)
		return self._rmsFm

	@property
	def rmsNonlinear(self):
		"""rmsNonlinear commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmsNonlinear'):
			from .RmsNonlinear import RmsNonlinearCls
			self._rmsNonlinear = RmsNonlinearCls(self._core, self._cmd_group)
		return self._rmsNonlinear

	@property
	def overshoot(self):
		"""overshoot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_overshoot'):
			from .Overshoot import OvershootCls
			self._overshoot = OvershootCls(self._core, self._cmd_group)
		return self._overshoot

	@property
	def undershoot(self):
		"""undershoot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_undershoot'):
			from .Undershoot import UndershootCls
			self._undershoot = UndershootCls(self._core, self._cmd_group)
		return self._undershoot

	def clone(self) -> 'FrequencyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FrequencyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
