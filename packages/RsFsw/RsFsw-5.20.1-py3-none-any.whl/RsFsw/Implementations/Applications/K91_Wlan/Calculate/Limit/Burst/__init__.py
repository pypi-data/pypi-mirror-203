from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BurstCls:
	"""Burst commands group definition. 38 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("burst", core, parent)

	@property
	def all(self):
		"""all commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	@property
	def trise(self):
		"""trise commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_trise'):
			from .Trise import TriseCls
			self._trise = TriseCls(self._core, self._cmd_group)
		return self._trise

	@property
	def tfall(self):
		"""tfall commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tfall'):
			from .Tfall import TfallCls
			self._tfall = TfallCls(self._core, self._cmd_group)
		return self._tfall

	@property
	def freqError(self):
		"""freqError commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_freqError'):
			from .FreqError import FreqErrorCls
			self._freqError = FreqErrorCls(self._core, self._cmd_group)
		return self._freqError

	@property
	def symbolError(self):
		"""symbolError commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_symbolError'):
			from .SymbolError import SymbolErrorCls
			self._symbolError = SymbolErrorCls(self._core, self._cmd_group)
		return self._symbolError

	@property
	def iqOffset(self):
		"""iqOffset commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffsetCls
			self._iqOffset = IqOffsetCls(self._core, self._cmd_group)
		return self._iqOffset

	@property
	def evm(self):
		"""evm commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import EvmCls
			self._evm = EvmCls(self._core, self._cmd_group)
		return self._evm

	def clone(self) -> 'BurstCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BurstCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
