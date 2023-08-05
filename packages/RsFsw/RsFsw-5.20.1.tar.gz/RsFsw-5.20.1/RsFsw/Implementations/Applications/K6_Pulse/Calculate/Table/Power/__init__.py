from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerCls:
	"""Power commands group definition. 62 total commands, 16 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def all(self):
		"""all commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	@property
	def adroop(self):
		"""adroop commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_adroop'):
			from .Adroop import AdroopCls
			self._adroop = AdroopCls(self._core, self._cmd_group)
		return self._adroop

	@property
	def amplitude(self):
		"""amplitude commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_amplitude'):
			from .Amplitude import AmplitudeCls
			self._amplitude = AmplitudeCls(self._core, self._cmd_group)
		return self._amplitude

	@property
	def avg(self):
		"""avg commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_avg'):
			from .Avg import AvgCls
			self._avg = AvgCls(self._core, self._cmd_group)
		return self._avg

	@property
	def base(self):
		"""base commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_base'):
			from .Base import BaseCls
			self._base = BaseCls(self._core, self._cmd_group)
		return self._base

	@property
	def max(self):
		"""max commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_max'):
			from .Max import MaxCls
			self._max = MaxCls(self._core, self._cmd_group)
		return self._max

	@property
	def min(self):
		"""min commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_min'):
			from .Min import MinCls
			self._min = MinCls(self._core, self._cmd_group)
		return self._min

	@property
	def on(self):
		"""on commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_on'):
			from .On import OnCls
			self._on = OnCls(self._core, self._cmd_group)
		return self._on

	@property
	def overshoot(self):
		"""overshoot commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_overshoot'):
			from .Overshoot import OvershootCls
			self._overshoot = OvershootCls(self._core, self._cmd_group)
		return self._overshoot

	@property
	def pavg(self):
		"""pavg commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_pavg'):
			from .Pavg import PavgCls
			self._pavg = PavgCls(self._core, self._cmd_group)
		return self._pavg

	@property
	def pmin(self):
		"""pmin commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmin'):
			from .Pmin import PminCls
			self._pmin = PminCls(self._core, self._cmd_group)
		return self._pmin

	@property
	def point(self):
		"""point commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_point'):
			from .Point import PointCls
			self._point = PointCls(self._core, self._cmd_group)
		return self._point

	@property
	def pon(self):
		"""pon commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_pon'):
			from .Pon import PonCls
			self._pon = PonCls(self._core, self._cmd_group)
		return self._pon

	@property
	def ppRatio(self):
		"""ppRatio commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ppRatio'):
			from .PpRatio import PpRatioCls
			self._ppRatio = PpRatioCls(self._core, self._cmd_group)
		return self._ppRatio

	@property
	def ripple(self):
		"""ripple commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ripple'):
			from .Ripple import RippleCls
			self._ripple = RippleCls(self._core, self._cmd_group)
		return self._ripple

	@property
	def top(self):
		"""top commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_top'):
			from .Top import TopCls
			self._top = TopCls(self._core, self._cmd_group)
		return self._top

	def clone(self) -> 'PowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
