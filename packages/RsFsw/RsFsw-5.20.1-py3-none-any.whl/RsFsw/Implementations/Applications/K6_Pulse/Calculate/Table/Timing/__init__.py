from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TimingCls:
	"""Timing commands group definition. 32 total commands, 11 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("timing", core, parent)

	@property
	def all(self):
		"""all commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	@property
	def dcycle(self):
		"""dcycle commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dcycle'):
			from .Dcycle import DcycleCls
			self._dcycle = DcycleCls(self._core, self._cmd_group)
		return self._dcycle

	@property
	def dratio(self):
		"""dratio commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dratio'):
			from .Dratio import DratioCls
			self._dratio = DratioCls(self._core, self._cmd_group)
		return self._dratio

	@property
	def fall(self):
		"""fall commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_fall'):
			from .Fall import FallCls
			self._fall = FallCls(self._core, self._cmd_group)
		return self._fall

	@property
	def off(self):
		"""off commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_off'):
			from .Off import OffCls
			self._off = OffCls(self._core, self._cmd_group)
		return self._off

	@property
	def prf(self):
		"""prf commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_prf'):
			from .Prf import PrfCls
			self._prf = PrfCls(self._core, self._cmd_group)
		return self._prf

	@property
	def pri(self):
		"""pri commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_pri'):
			from .Pri import PriCls
			self._pri = PriCls(self._core, self._cmd_group)
		return self._pri

	@property
	def pwidth(self):
		"""pwidth commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_pwidth'):
			from .Pwidth import PwidthCls
			self._pwidth = PwidthCls(self._core, self._cmd_group)
		return self._pwidth

	@property
	def rise(self):
		"""rise commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_rise'):
			from .Rise import RiseCls
			self._rise = RiseCls(self._core, self._cmd_group)
		return self._rise

	@property
	def settling(self):
		"""settling commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_settling'):
			from .Settling import SettlingCls
			self._settling = SettlingCls(self._core, self._cmd_group)
		return self._settling

	@property
	def tstamp(self):
		"""tstamp commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_tstamp'):
			from .Tstamp import TstampCls
			self._tstamp = TstampCls(self._core, self._cmd_group)
		return self._tstamp

	def clone(self) -> 'TimingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TimingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
