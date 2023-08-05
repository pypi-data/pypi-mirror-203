from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FetchCls:
	"""Fetch commands group definition. 52 total commands, 16 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fetch", core, parent)

	@property
	def evm(self):
		"""evm commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import EvmCls
			self._evm = EvmCls(self._core, self._cmd_group)
		return self._evm

	@property
	def cfactor(self):
		"""cfactor commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cfactor'):
			from .Cfactor import CfactorCls
			self._cfactor = CfactorCls(self._core, self._cmd_group)
		return self._cfactor

	@property
	def cfError(self):
		"""cfError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cfError'):
			from .CfError import CfErrorCls
			self._cfError = CfErrorCls(self._core, self._cmd_group)
		return self._cfError

	@property
	def ftime(self):
		"""ftime commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ftime'):
			from .Ftime import FtimeCls
			self._ftime = FtimeCls(self._core, self._cmd_group)
		return self._ftime

	@property
	def gimbalance(self):
		"""gimbalance commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_gimbalance'):
			from .Gimbalance import GimbalanceCls
			self._gimbalance = GimbalanceCls(self._core, self._cmd_group)
		return self._gimbalance

	@property
	def hbeRate(self):
		"""hbeRate commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_hbeRate'):
			from .HbeRate import HbeRateCls
			self._hbeRate = HbeRateCls(self._core, self._cmd_group)
		return self._hbeRate

	@property
	def iqOffset(self):
		"""iqOffset commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffsetCls
			self._iqOffset = IqOffsetCls(self._core, self._cmd_group)
		return self._iqOffset

	@property
	def pbeRate(self):
		"""pbeRate commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pbeRate'):
			from .PbeRate import PbeRateCls
			self._pbeRate = PbeRateCls(self._core, self._cmd_group)
		return self._pbeRate

	@property
	def quadError(self):
		"""quadError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_quadError'):
			from .QuadError import QuadErrorCls
			self._quadError = QuadErrorCls(self._core, self._cmd_group)
		return self._quadError

	@property
	def rtime(self):
		"""rtime commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rtime'):
			from .Rtime import RtimeCls
			self._rtime = RtimeCls(self._core, self._cmd_group)
		return self._rtime

	@property
	def snr(self):
		"""snr commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_snr'):
			from .Snr import SnrCls
			self._snr = SnrCls(self._core, self._cmd_group)
		return self._snr

	@property
	def symbolError(self):
		"""symbolError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_symbolError'):
			from .SymbolError import SymbolErrorCls
			self._symbolError = SymbolErrorCls(self._core, self._cmd_group)
		return self._symbolError

	@property
	def tdPower(self):
		"""tdPower commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdPower'):
			from .TdPower import TdPowerCls
			self._tdPower = TdPowerCls(self._core, self._cmd_group)
		return self._tdPower

	@property
	def tskew(self):
		"""tskew commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tskew'):
			from .Tskew import TskewCls
			self._tskew = TskewCls(self._core, self._cmd_group)
		return self._tskew

	@property
	def pmeter(self):
		"""pmeter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmeter'):
			from .Pmeter import PmeterCls
			self._pmeter = PmeterCls(self._core, self._cmd_group)
		return self._pmeter

	@property
	def burst(self):
		"""burst commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_burst'):
			from .Burst import BurstCls
			self._burst = BurstCls(self._core, self._cmd_group)
		return self._burst

	def clone(self) -> 'FetchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FetchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
