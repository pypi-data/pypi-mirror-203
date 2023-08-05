from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TsidelobeCls:
	"""Tsidelobe commands group definition. 32 total commands, 11 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsidelobe", core, parent)

	@property
	def all(self):
		"""all commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	@property
	def psLevel(self):
		"""psLevel commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_psLevel'):
			from .PsLevel import PsLevelCls
			self._psLevel = PsLevelCls(self._core, self._cmd_group)
		return self._psLevel

	@property
	def isLevel(self):
		"""isLevel commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_isLevel'):
			from .IsLevel import IsLevelCls
			self._isLevel = IsLevelCls(self._core, self._cmd_group)
		return self._isLevel

	@property
	def mwidth(self):
		"""mwidth commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mwidth'):
			from .Mwidth import MwidthCls
			self._mwidth = MwidthCls(self._core, self._cmd_group)
		return self._mwidth

	@property
	def sdelay(self):
		"""sdelay commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_sdelay'):
			from .Sdelay import SdelayCls
			self._sdelay = SdelayCls(self._core, self._cmd_group)
		return self._sdelay

	@property
	def cratio(self):
		"""cratio commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_cratio'):
			from .Cratio import CratioCls
			self._cratio = CratioCls(self._core, self._cmd_group)
		return self._cratio

	@property
	def imPower(self):
		"""imPower commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_imPower'):
			from .ImPower import ImPowerCls
			self._imPower = ImPowerCls(self._core, self._cmd_group)
		return self._imPower

	@property
	def amPower(self):
		"""amPower commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_amPower'):
			from .AmPower import AmPowerCls
			self._amPower = AmPowerCls(self._core, self._cmd_group)
		return self._amPower

	@property
	def pcorrelation(self):
		"""pcorrelation commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcorrelation'):
			from .Pcorrelation import PcorrelationCls
			self._pcorrelation = PcorrelationCls(self._core, self._cmd_group)
		return self._pcorrelation

	@property
	def mphase(self):
		"""mphase commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mphase'):
			from .Mphase import MphaseCls
			self._mphase = MphaseCls(self._core, self._cmd_group)
		return self._mphase

	@property
	def mfrequency(self):
		"""mfrequency commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mfrequency'):
			from .Mfrequency import MfrequencyCls
			self._mfrequency = MfrequencyCls(self._core, self._cmd_group)
		return self._mfrequency

	def clone(self) -> 'TsidelobeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TsidelobeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
