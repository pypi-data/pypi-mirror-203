from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SummaryCls:
	"""Summary commands group definition. 93 total commands, 15 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("summary", core, parent)

	@property
	def crest(self):
		"""crest commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_crest'):
			from .Crest import CrestCls
			self._crest = CrestCls(self._core, self._cmd_group)
		return self._crest

	@property
	def evm(self):
		"""evm commands group. 27 Sub-classes, 0 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import EvmCls
			self._evm = EvmCls(self._core, self._cmd_group)
		return self._evm

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
	def iqOffset(self):
		"""iqOffset commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffsetCls
			self._iqOffset = IqOffsetCls(self._core, self._cmd_group)
		return self._iqOffset

	@property
	def ostp(self):
		"""ostp commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ostp'):
			from .Ostp import OstpCls
			self._ostp = OstpCls(self._core, self._cmd_group)
		return self._ostp

	@property
	def power(self):
		"""power commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def quadError(self):
		"""quadError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_quadError'):
			from .QuadError import QuadErrorCls
			self._quadError = QuadErrorCls(self._core, self._cmd_group)
		return self._quadError

	@property
	def rbp(self):
		"""rbp commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rbp'):
			from .Rbp import RbpCls
			self._rbp = RbpCls(self._core, self._cmd_group)
		return self._rbp

	@property
	def nbPower(self):
		"""nbPower commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_nbPower'):
			from .NbPower import NbPowerCls
			self._nbPower = NbPowerCls(self._core, self._cmd_group)
		return self._nbPower

	@property
	def rfError(self):
		"""rfError commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfError'):
			from .RfError import RfErrorCls
			self._rfError = RfErrorCls(self._core, self._cmd_group)
		return self._rfError

	@property
	def rssi(self):
		"""rssi commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rssi'):
			from .Rssi import RssiCls
			self._rssi = RssiCls(self._core, self._cmd_group)
		return self._rssi

	@property
	def rstp(self):
		"""rstp commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rstp'):
			from .Rstp import RstpCls
			self._rstp = RstpCls(self._core, self._cmd_group)
		return self._rstp

	@property
	def serror(self):
		"""serror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_serror'):
			from .Serror import SerrorCls
			self._serror = SerrorCls(self._core, self._cmd_group)
		return self._serror

	@property
	def tframe(self):
		"""tframe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tframe'):
			from .Tframe import TframeCls
			self._tframe = TframeCls(self._core, self._cmd_group)
		return self._tframe

	def clone(self) -> 'SummaryCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SummaryCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
