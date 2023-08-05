from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CalculateCls:
	"""Calculate commands group definition. 249 total commands, 12 Subgroups, 0 group commands
	Repeated Capability: Window, default value after init: Window.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("calculate", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_window_get', 'repcap_window_set', repcap.Window.Nr1)

	def repcap_window_set(self, window: repcap.Window) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Window.Default
		Default value after init: Window.Nr1"""
		self._cmd_group.set_repcap_enum_value(window)

	def repcap_window_get(self) -> repcap.Window:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def deltaMarker(self):
		"""deltaMarker commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_deltaMarker'):
			from .DeltaMarker import DeltaMarkerCls
			self._deltaMarker = DeltaMarkerCls(self._core, self._cmd_group)
		return self._deltaMarker

	@property
	def dline(self):
		"""dline commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dline'):
			from .Dline import DlineCls
			self._dline = DlineCls(self._core, self._cmd_group)
		return self._dline

	@property
	def espectrum(self):
		"""espectrum commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_espectrum'):
			from .Espectrum import EspectrumCls
			self._espectrum = EspectrumCls(self._core, self._cmd_group)
		return self._espectrum

	@property
	def fline(self):
		"""fline commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_fline'):
			from .Fline import FlineCls
			self._fline = FlineCls(self._core, self._cmd_group)
		return self._fline

	@property
	def limit(self):
		"""limit commands group. 15 Sub-classes, 2 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import LimitCls
			self._limit = LimitCls(self._core, self._cmd_group)
		return self._limit

	@property
	def marker(self):
		"""marker commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_marker'):
			from .Marker import MarkerCls
			self._marker = MarkerCls(self._core, self._cmd_group)
		return self._marker

	@property
	def math(self):
		"""math commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_math'):
			from .Math import MathCls
			self._math = MathCls(self._core, self._cmd_group)
		return self._math

	@property
	def msra(self):
		"""msra commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_msra'):
			from .Msra import MsraCls
			self._msra = MsraCls(self._core, self._cmd_group)
		return self._msra

	@property
	def pmeter(self):
		"""pmeter commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmeter'):
			from .Pmeter import PmeterCls
			self._pmeter = PmeterCls(self._core, self._cmd_group)
		return self._pmeter

	@property
	def statistics(self):
		"""statistics commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_statistics'):
			from .Statistics import StatisticsCls
			self._statistics = StatisticsCls(self._core, self._cmd_group)
		return self._statistics

	@property
	def threshold(self):
		"""threshold commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_threshold'):
			from .Threshold import ThresholdCls
			self._threshold = ThresholdCls(self._core, self._cmd_group)
		return self._threshold

	@property
	def unit(self):
		"""unit commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_unit'):
			from .Unit import UnitCls
			self._unit = UnitCls(self._core, self._cmd_group)
		return self._unit

	def clone(self) -> 'CalculateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CalculateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
