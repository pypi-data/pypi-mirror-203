from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaccuracyCls:
	"""Maccuracy commands group definition. 35 total commands, 13 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maccuracy", core, parent)

	@property
	def adroop(self):
		"""adroop commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_adroop'):
			from .Adroop import AdroopCls
			self._adroop = AdroopCls(self._core, self._cmd_group)
		return self._adroop

	@property
	def freqError(self):
		"""freqError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_freqError'):
			from .FreqError import FreqErrorCls
			self._freqError = FreqErrorCls(self._core, self._cmd_group)
		return self._freqError

	@property
	def gimbalance(self):
		"""gimbalance commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_gimbalance'):
			from .Gimbalance import GimbalanceCls
			self._gimbalance = GimbalanceCls(self._core, self._cmd_group)
		return self._gimbalance

	@property
	def iqImbalance(self):
		"""iqImbalance commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqImbalance'):
			from .IqImbalance import IqImbalanceCls
			self._iqImbalance = IqImbalanceCls(self._core, self._cmd_group)
		return self._iqImbalance

	@property
	def iqOffset(self):
		"""iqOffset commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffsetCls
			self._iqOffset = IqOffsetCls(self._core, self._cmd_group)
		return self._iqOffset

	@property
	def merror(self):
		"""merror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_merror'):
			from .Merror import MerrorCls
			self._merror = MerrorCls(self._core, self._cmd_group)
		return self._merror

	@property
	def perror(self):
		"""perror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_perror'):
			from .Perror import PerrorCls
			self._perror = PerrorCls(self._core, self._cmd_group)
		return self._perror

	@property
	def qerror(self):
		"""qerror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_qerror'):
			from .Qerror import QerrorCls
			self._qerror = QerrorCls(self._core, self._cmd_group)
		return self._qerror

	@property
	def result(self):
		"""result commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_result'):
			from .Result import ResultCls
			self._result = ResultCls(self._core, self._cmd_group)
		return self._result

	@property
	def revm(self):
		"""revm commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_revm'):
			from .Revm import RevmCls
			self._revm = RevmCls(self._core, self._cmd_group)
		return self._revm

	@property
	def rmev(self):
		"""rmev commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rmev'):
			from .Rmev import RmevCls
			self._rmev = RmevCls(self._core, self._cmd_group)
		return self._rmev

	@property
	def srError(self):
		"""srError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_srError'):
			from .SrError import SrErrorCls
			self._srError = SrErrorCls(self._core, self._cmd_group)
		return self._srError

	@property
	def poffset(self):
		"""poffset commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_poffset'):
			from .Poffset import PoffsetCls
			self._poffset = PoffsetCls(self._core, self._cmd_group)
		return self._poffset

	def clone(self) -> 'MaccuracyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MaccuracyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
