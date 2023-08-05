from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GosCls:
	"""Gos commands group definition. 13 total commands, 13 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gos", core, parent)

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import BandwidthCls
			self._bandwidth = BandwidthCls(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def crest(self):
		"""crest commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crest'):
			from .Crest import CrestCls
			self._crest = CrestCls(self._core, self._cmd_group)
		return self._crest

	@property
	def dcycle(self):
		"""dcycle commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dcycle'):
			from .Dcycle import DcycleCls
			self._dcycle = DcycleCls(self._core, self._cmd_group)
		return self._dcycle

	@property
	def fpath(self):
		"""fpath commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fpath'):
			from .Fpath import FpathCls
			self._fpath = FpathCls(self._core, self._cmd_group)
		return self._fpath

	@property
	def ledState(self):
		"""ledState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ledState'):
			from .LedState import LedStateCls
			self._ledState = LedStateCls(self._core, self._cmd_group)
		return self._ledState

	@property
	def nposition(self):
		"""nposition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nposition'):
			from .Nposition import NpositionCls
			self._nposition = NpositionCls(self._core, self._cmd_group)
		return self._nposition

	@property
	def nwidth(self):
		"""nwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nwidth'):
			from .Nwidth import NwidthCls
			self._nwidth = NwidthCls(self._core, self._cmd_group)
		return self._nwidth

	@property
	def path(self):
		"""path commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_path'):
			from .Path import PathCls
			self._path = PathCls(self._core, self._cmd_group)
		return self._path

	@property
	def rlength(self):
		"""rlength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rlength'):
			from .Rlength import RlengthCls
			self._rlength = RlengthCls(self._core, self._cmd_group)
		return self._rlength

	@property
	def slength(self):
		"""slength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slength'):
			from .Slength import SlengthCls
			self._slength = SlengthCls(self._core, self._cmd_group)
		return self._slength

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRateCls
			self._symbolRate = SymbolRateCls(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def wname(self):
		"""wname commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wname'):
			from .Wname import WnameCls
			self._wname = WnameCls(self._core, self._cmd_group)
		return self._wname

	@property
	def write(self):
		"""write commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_write'):
			from .Write import WriteCls
			self._write = WriteCls(self._core, self._cmd_group)
		return self._write

	def clone(self) -> 'GosCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = GosCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
