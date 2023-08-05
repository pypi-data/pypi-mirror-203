from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrachCls:
	"""Prach commands group definition. 9 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prach", core, parent)

	@property
	def apm(self):
		"""apm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apm'):
			from .Apm import ApmCls
			self._apm = ApmCls(self._core, self._cmd_group)
		return self._apm

	@property
	def conf(self):
		"""conf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_conf'):
			from .Conf import ConfCls
			self._conf = ConfCls(self._core, self._cmd_group)
		return self._conf

	@property
	def foffset(self):
		"""foffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_foffset'):
			from .Foffset import FoffsetCls
			self._foffset = FoffsetCls(self._core, self._cmd_group)
		return self._foffset

	@property
	def frIndex(self):
		"""frIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frIndex'):
			from .FrIndex import FrIndexCls
			self._frIndex = FrIndexCls(self._core, self._cmd_group)
		return self._frIndex

	@property
	def hfIndicator(self):
		"""hfIndicator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hfIndicator'):
			from .HfIndicator import HfIndicatorCls
			self._hfIndicator = HfIndicatorCls(self._core, self._cmd_group)
		return self._hfIndicator

	@property
	def ncsc(self):
		"""ncsc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ncsc'):
			from .Ncsc import NcscCls
			self._ncsc = NcscCls(self._core, self._cmd_group)
		return self._ncsc

	@property
	def rseq(self):
		"""rseq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rseq'):
			from .Rseq import RseqCls
			self._rseq = RseqCls(self._core, self._cmd_group)
		return self._rseq

	@property
	def rset(self):
		"""rset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rset'):
			from .Rset import RsetCls
			self._rset = RsetCls(self._core, self._cmd_group)
		return self._rset

	@property
	def sindex(self):
		"""sindex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sindex'):
			from .Sindex import SindexCls
			self._sindex = SindexCls(self._core, self._cmd_group)
		return self._sindex

	def clone(self) -> 'PrachCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PrachCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
