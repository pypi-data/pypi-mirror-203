from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nr5GCls:
	"""Nr5G commands group definition. 356 total commands, 30 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nr5G", core, parent)

	@property
	def aclr(self):
		"""aclr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aclr'):
			from .Aclr import AclrCls
			self._aclr = AclrCls(self._core, self._cmd_group)
		return self._aclr

	@property
	def bstation(self):
		"""bstation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bstation'):
			from .Bstation import BstationCls
			self._bstation = BstationCls(self._core, self._cmd_group)
		return self._bstation

	@property
	def caclr(self):
		"""caclr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_caclr'):
			from .Caclr import CaclrCls
			self._caclr = CaclrCls(self._core, self._cmd_group)
		return self._caclr

	@property
	def center(self):
		"""center commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_center'):
			from .Center import CenterCls
			self._center = CenterCls(self._core, self._cmd_group)
		return self._center

	@property
	def craster(self):
		"""craster commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_craster'):
			from .Craster import CrasterCls
			self._craster = CrasterCls(self._core, self._cmd_group)
		return self._craster

	@property
	def cspacing(self):
		"""cspacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cspacing'):
			from .Cspacing import CspacingCls
			self._cspacing = CspacingCls(self._core, self._cmd_group)
		return self._cspacing

	@property
	def csCapture(self):
		"""csCapture commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csCapture'):
			from .CsCapture import CsCaptureCls
			self._csCapture = CsCaptureCls(self._core, self._cmd_group)
		return self._csCapture

	@property
	def evm(self):
		"""evm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import EvmCls
			self._evm = EvmCls(self._core, self._cmd_group)
		return self._evm

	@property
	def fcOffset(self):
		"""fcOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fcOffset'):
			from .FcOffset import FcOffsetCls
			self._fcOffset = FcOffsetCls(self._core, self._cmd_group)
		return self._fcOffset

	@property
	def felc(self):
		"""felc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_felc'):
			from .Felc import FelcCls
			self._felc = FelcCls(self._core, self._cmd_group)
		return self._felc

	@property
	def gmcFreq(self):
		"""gmcFreq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gmcFreq'):
			from .GmcFreq import GmcFreqCls
			self._gmcFreq = GmcFreqCls(self._core, self._cmd_group)
		return self._gmcFreq

	@property
	def sem(self):
		"""sem commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sem'):
			from .Sem import SemCls
			self._sem = SemCls(self._core, self._cmd_group)
		return self._sem

	@property
	def downlink(self):
		"""downlink commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import DownlinkCls
			self._downlink = DownlinkCls(self._core, self._cmd_group)
		return self._downlink

	@property
	def ldirection(self):
		"""ldirection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ldirection'):
			from .Ldirection import LdirectionCls
			self._ldirection = LdirectionCls(self._core, self._cmd_group)
		return self._ldirection

	@property
	def mcaClr(self):
		"""mcaClr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcaClr'):
			from .McaClr import McaClrCls
			self._mcaClr = McaClrCls(self._core, self._cmd_group)
		return self._mcaClr

	@property
	def measurement(self):
		"""measurement commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_measurement'):
			from .Measurement import MeasurementCls
			self._measurement = MeasurementCls(self._core, self._cmd_group)
		return self._measurement

	@property
	def msem(self):
		"""msem commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_msem'):
			from .Msem import MsemCls
			self._msem = MsemCls(self._core, self._cmd_group)
		return self._msem

	@property
	def msHelper(self):
		"""msHelper commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_msHelper'):
			from .MsHelper import MsHelperCls
			self._msHelper = MsHelperCls(self._core, self._cmd_group)
		return self._msHelper

	@property
	def ncSpacing(self):
		"""ncSpacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ncSpacing'):
			from .NcSpacing import NcSpacingCls
			self._ncSpacing = NcSpacingCls(self._core, self._cmd_group)
		return self._ncSpacing

	@property
	def noCc(self):
		"""noCc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noCc'):
			from .NoCc import NoCcCls
			self._noCc = NoCcCls(self._core, self._cmd_group)
		return self._noCc

	@property
	def nrqMaster(self):
		"""nrqMaster commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nrqMaster'):
			from .NrqMaster import NrqMasterCls
			self._nrqMaster = NrqMasterCls(self._core, self._cmd_group)
		return self._nrqMaster

	@property
	def nrqPrimary(self):
		"""nrqPrimary commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nrqPrimary'):
			from .NrqPrimary import NrqPrimaryCls
			self._nrqPrimary = NrqPrimaryCls(self._core, self._cmd_group)
		return self._nrqPrimary

	@property
	def nsources(self):
		"""nsources commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsources'):
			from .Nsources import NsourcesCls
			self._nsources = NsourcesCls(self._core, self._cmd_group)
		return self._nsources

	@property
	def oband(self):
		"""oband commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_oband'):
			from .Oband import ObandCls
			self._oband = ObandCls(self._core, self._cmd_group)
		return self._oband

	@property
	def omode(self):
		"""omode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_omode'):
			from .Omode import OmodeCls
			self._omode = OmodeCls(self._core, self._cmd_group)
		return self._omode

	@property
	def orel(self):
		"""orel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_orel'):
			from .Orel import OrelCls
			self._orel = OrelCls(self._core, self._cmd_group)
		return self._orel

	@property
	def ooPower(self):
		"""ooPower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ooPower'):
			from .OoPower import OoPowerCls
			self._ooPower = OoPowerCls(self._core, self._cmd_group)
		return self._ooPower

	@property
	def oran(self):
		"""oran commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_oran'):
			from .Oran import OranCls
			self._oran = OranCls(self._core, self._cmd_group)
		return self._oran

	@property
	def simulation(self):
		"""simulation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_simulation'):
			from .Simulation import SimulationCls
			self._simulation = SimulationCls(self._core, self._cmd_group)
		return self._simulation

	@property
	def uplink(self):
		"""uplink commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import UplinkCls
			self._uplink = UplinkCls(self._core, self._cmd_group)
		return self._uplink

	def clone(self) -> 'Nr5GCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Nr5GCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
