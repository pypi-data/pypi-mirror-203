from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BurstCls:
	"""Burst commands group definition. 85 total commands, 29 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("burst", core, parent)

	@property
	def iqSkew(self):
		"""iqSkew commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqSkew'):
			from .IqSkew import IqSkewCls
			self._iqSkew = IqSkewCls(self._core, self._cmd_group)
		return self._iqSkew

	@property
	def all(self):
		"""all commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	@property
	def count(self):
		"""count commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import CountCls
			self._count = CountCls(self._core, self._cmd_group)
		return self._count

	@property
	def am(self):
		"""am commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_am'):
			from .Am import AmCls
			self._am = AmCls(self._core, self._cmd_group)
		return self._am

	@property
	def preamble(self):
		"""preamble commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_preamble'):
			from .Preamble import PreambleCls
			self._preamble = PreambleCls(self._core, self._cmd_group)
		return self._preamble

	@property
	def payload(self):
		"""payload commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_payload'):
			from .Payload import PayloadCls
			self._payload = PayloadCls(self._core, self._cmd_group)
		return self._payload

	@property
	def rms(self):
		"""rms commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rms'):
			from .Rms import RmsCls
			self._rms = RmsCls(self._core, self._cmd_group)
		return self._rms

	@property
	def peak(self):
		"""peak commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_peak'):
			from .Peak import PeakCls
			self._peak = PeakCls(self._core, self._cmd_group)
		return self._peak

	@property
	def crest(self):
		"""crest commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_crest'):
			from .Crest import CrestCls
			self._crest = CrestCls(self._core, self._cmd_group)
		return self._crest

	@property
	def trise(self):
		"""trise commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_trise'):
			from .Trise import TriseCls
			self._trise = TriseCls(self._core, self._cmd_group)
		return self._trise

	@property
	def tfall(self):
		"""tfall commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tfall'):
			from .Tfall import TfallCls
			self._tfall = TfallCls(self._core, self._cmd_group)
		return self._tfall

	@property
	def freqError(self):
		"""freqError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_freqError'):
			from .FreqError import FreqErrorCls
			self._freqError = FreqErrorCls(self._core, self._cmd_group)
		return self._freqError

	@property
	def symbolError(self):
		"""symbolError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_symbolError'):
			from .SymbolError import SymbolErrorCls
			self._symbolError = SymbolErrorCls(self._core, self._cmd_group)
		return self._symbolError

	@property
	def iqOffset(self):
		"""iqOffset commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffsetCls
			self._iqOffset = IqOffsetCls(self._core, self._cmd_group)
		return self._iqOffset

	@property
	def gimbalance(self):
		"""gimbalance commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_gimbalance'):
			from .Gimbalance import GimbalanceCls
			self._gimbalance = GimbalanceCls(self._core, self._cmd_group)
		return self._gimbalance

	@property
	def quadOffset(self):
		"""quadOffset commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_quadOffset'):
			from .QuadOffset import QuadOffsetCls
			self._quadOffset = QuadOffsetCls(self._core, self._cmd_group)
		return self._quadOffset

	@property
	def berPilot(self):
		"""berPilot commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_berPilot'):
			from .BerPilot import BerPilotCls
			self._berPilot = BerPilotCls(self._core, self._cmd_group)
		return self._berPilot

	@property
	def mcPower(self):
		"""mcPower commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mcPower'):
			from .McPower import McPowerCls
			self._mcPower = McPowerCls(self._core, self._cmd_group)
		return self._mcPower

	@property
	def mchPower(self):
		"""mchPower commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mchPower'):
			from .MchPower import MchPowerCls
			self._mchPower = MchPowerCls(self._core, self._cmd_group)
		return self._mchPower

	@property
	def cfError(self):
		"""cfError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cfError'):
			from .CfError import CfErrorCls
			self._cfError = CfErrorCls(self._core, self._cmd_group)
		return self._cfError

	@property
	def cpError(self):
		"""cpError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cpError'):
			from .CpError import CpErrorCls
			self._cpError = CpErrorCls(self._core, self._cmd_group)
		return self._cpError

	@property
	def evm(self):
		"""evm commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import EvmCls
			self._evm = EvmCls(self._core, self._cmd_group)
		return self._evm

	@property
	def ppdu(self):
		"""ppdu commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ppdu'):
			from .Ppdu import PpduCls
			self._ppdu = PpduCls(self._core, self._cmd_group)
		return self._ppdu

	@property
	def ecmGain(self):
		"""ecmGain commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ecmGain'):
			from .EcmGain import EcmGainCls
			self._ecmGain = EcmGainCls(self._core, self._cmd_group)
		return self._ecmGain

	@property
	def pcmGain(self):
		"""pcmGain commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcmGain'):
			from .PcmGain import PcmGainCls
			self._pcmGain = PcmGainCls(self._core, self._cmd_group)
		return self._pcmGain

	@property
	def lengths(self):
		"""lengths commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lengths'):
			from .Lengths import LengthsCls
			self._lengths = LengthsCls(self._core, self._cmd_group)
		return self._lengths

	@property
	def starts(self):
		"""starts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_starts'):
			from .Starts import StartsCls
			self._starts = StartsCls(self._core, self._cmd_group)
		return self._starts

	@property
	def mcsIndex(self):
		"""mcsIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcsIndex'):
			from .McsIndex import McsIndexCls
			self._mcsIndex = McsIndexCls(self._core, self._cmd_group)
		return self._mcsIndex

	@property
	def ginterval(self):
		"""ginterval commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ginterval'):
			from .Ginterval import GintervalCls
			self._ginterval = GintervalCls(self._core, self._cmd_group)
		return self._ginterval

	def clone(self) -> 'BurstCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BurstCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
