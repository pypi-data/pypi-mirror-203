from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nr5GCls:
	"""Nr5G commands group definition. 53 total commands, 17 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nr5G", core, parent)

	@property
	def acPower(self):
		"""acPower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_acPower'):
			from .AcPower import AcPowerCls
			self._acPower = AcPowerCls(self._core, self._cmd_group)
		return self._acPower

	@property
	def cc(self):
		"""cc commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .Cc import CcCls
			self._cc = CcCls(self._core, self._cmd_group)
		return self._cc

	@property
	def ccolor(self):
		"""ccolor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ccolor'):
			from .Ccolor import CcolorCls
			self._ccolor = CcolorCls(self._core, self._cmd_group)
		return self._ccolor

	@property
	def cdrPower(self):
		"""cdrPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cdrPower'):
			from .CdrPower import CdrPowerCls
			self._cdrPower = CdrPowerCls(self._core, self._cmd_group)
		return self._cdrPower

	@property
	def demod(self):
		"""demod commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_demod'):
			from .Demod import DemodCls
			self._demod = DemodCls(self._core, self._cmd_group)
		return self._demod

	@property
	def emHold(self):
		"""emHold commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_emHold'):
			from .EmHold import EmHoldCls
			self._emHold = EmHoldCls(self._core, self._cmd_group)
		return self._emHold

	@property
	def tdView(self):
		"""tdView commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdView'):
			from .TdView import TdViewCls
			self._tdView = TdViewCls(self._core, self._cmd_group)
		return self._tdView

	@property
	def efilter(self):
		"""efilter commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_efilter'):
			from .Efilter import EfilterCls
			self._efilter = EfilterCls(self._core, self._cmd_group)
		return self._efilter

	@property
	def fevents(self):
		"""fevents commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fevents'):
			from .Fevents import FeventsCls
			self._fevents = FeventsCls(self._core, self._cmd_group)
		return self._fevents

	@property
	def frame(self):
		"""frame commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_frame'):
			from .Frame import FrameCls
			self._frame = FrameCls(self._core, self._cmd_group)
		return self._frame

	@property
	def iq(self):
		"""iq commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iq'):
			from .Iq import IqCls
			self._iq = IqCls(self._core, self._cmd_group)
		return self._iq

	@property
	def ooPower(self):
		"""ooPower commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ooPower'):
			from .OoPower import OoPowerCls
			self._ooPower = OoPowerCls(self._core, self._cmd_group)
		return self._ooPower

	@property
	def rantenna(self):
		"""rantenna commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rantenna'):
			from .Rantenna import RantennaCls
			self._rantenna = RantennaCls(self._core, self._cmd_group)
		return self._rantenna

	@property
	def rsummary(self):
		"""rsummary commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rsummary'):
			from .Rsummary import RsummaryCls
			self._rsummary = RsummaryCls(self._core, self._cmd_group)
		return self._rsummary

	@property
	def scc(self):
		"""scc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scc'):
			from .Scc import SccCls
			self._scc = SccCls(self._core, self._cmd_group)
		return self._scc

	@property
	def segment(self):
		"""segment commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_segment'):
			from .Segment import SegmentCls
			self._segment = SegmentCls(self._core, self._cmd_group)
		return self._segment

	@property
	def tracking(self):
		"""tracking commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_tracking'):
			from .Tracking import TrackingCls
			self._tracking = TrackingCls(self._core, self._cmd_group)
		return self._tracking

	def clone(self) -> 'Nr5GCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Nr5GCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
