from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CcCls:
	"""Cc commands group definition. 85 total commands, 26 Subgroups, 0 group commands
	Repeated Capability: CarrierComponent, default value after init: CarrierComponent.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cc", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_carrierComponent_get', 'repcap_carrierComponent_set', repcap.CarrierComponent.Nr1)

	def repcap_carrierComponent_set(self, carrierComponent: repcap.CarrierComponent) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CarrierComponent.Default
		Default value after init: CarrierComponent.Nr1"""
		self._cmd_group.set_repcap_enum_value(carrierComponent)

	def repcap_carrierComponent_get(self) -> repcap.CarrierComponent:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def bf(self):
		"""bf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bf'):
			from .Bf import BfCls
			self._bf = BfCls(self._core, self._cmd_group)
		return self._bf

	@property
	def bw(self):
		"""bw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bw'):
			from .Bw import BwCls
			self._bw = BwCls(self._core, self._cmd_group)
		return self._bw

	@property
	def csirs(self):
		"""csirs commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_csirs'):
			from .Csirs import CsirsCls
			self._csirs = CsirsCls(self._core, self._cmd_group)
		return self._csirs

	@property
	def csubframes(self):
		"""csubframes commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csubframes'):
			from .Csubframes import CsubframesCls
			self._csubframes = CsubframesCls(self._core, self._cmd_group)
		return self._csubframes

	@property
	def cycPrefix(self):
		"""cycPrefix commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cycPrefix'):
			from .CycPrefix import CycPrefixCls
			self._cycPrefix = CycPrefixCls(self._core, self._cmd_group)
		return self._cycPrefix

	@property
	def eiNbIot(self):
		"""eiNbIot commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_eiNbIot'):
			from .EiNbIot import EiNbIotCls
			self._eiNbIot = EiNbIotCls(self._core, self._cmd_group)
		return self._eiNbIot

	@property
	def epdcch(self):
		"""epdcch commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_epdcch'):
			from .Epdcch import EpdcchCls
			self._epdcch = EpdcchCls(self._core, self._cmd_group)
		return self._epdcch

	@property
	def mbsfn(self):
		"""mbsfn commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_mbsfn'):
			from .Mbsfn import MbsfnCls
			self._mbsfn = MbsfnCls(self._core, self._cmd_group)
		return self._mbsfn

	@property
	def mimo(self):
		"""mimo commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mimo'):
			from .Mimo import MimoCls
			self._mimo = MimoCls(self._core, self._cmd_group)
		return self._mimo

	@property
	def noRb(self):
		"""noRb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noRb'):
			from .NoRb import NoRbCls
			self._noRb = NoRbCls(self._core, self._cmd_group)
		return self._noRb

	@property
	def nrbOffset(self):
		"""nrbOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nrbOffset'):
			from .NrbOffset import NrbOffsetCls
			self._nrbOffset = NrbOffsetCls(self._core, self._cmd_group)
		return self._nrbOffset

	@property
	def pbch(self):
		"""pbch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pbch'):
			from .Pbch import PbchCls
			self._pbch = PbchCls(self._core, self._cmd_group)
		return self._pbch

	@property
	def pcfich(self):
		"""pcfich commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcfich'):
			from .Pcfich import PcfichCls
			self._pcfich = PcfichCls(self._core, self._cmd_group)
		return self._pcfich

	@property
	def pdcch(self):
		"""pdcch commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdcch'):
			from .Pdcch import PdcchCls
			self._pdcch = PdcchCls(self._core, self._cmd_group)
		return self._pdcch

	@property
	def pdsch(self):
		"""pdsch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdsch'):
			from .Pdsch import PdschCls
			self._pdsch = PdschCls(self._core, self._cmd_group)
		return self._pdsch

	@property
	def phich(self):
		"""phich commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_phich'):
			from .Phich import PhichCls
			self._phich = PhichCls(self._core, self._cmd_group)
		return self._phich

	@property
	def plc(self):
		"""plc commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_plc'):
			from .Plc import PlcCls
			self._plc = PlcCls(self._core, self._cmd_group)
		return self._plc

	@property
	def plci(self):
		"""plci commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_plci'):
			from .Plci import PlciCls
			self._plci = PlciCls(self._core, self._cmd_group)
		return self._plci

	@property
	def prss(self):
		"""prss commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_prss'):
			from .Prss import PrssCls
			self._prss = PrssCls(self._core, self._cmd_group)
		return self._prss

	@property
	def psOffset(self):
		"""psOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_psOffset'):
			from .PsOffset import PsOffsetCls
			self._psOffset = PsOffsetCls(self._core, self._cmd_group)
		return self._psOffset

	@property
	def refsig(self):
		"""refsig commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_refsig'):
			from .Refsig import RefsigCls
			self._refsig = RefsigCls(self._core, self._cmd_group)
		return self._refsig

	@property
	def sfno(self):
		"""sfno commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfno'):
			from .Sfno import SfnoCls
			self._sfno = SfnoCls(self._core, self._cmd_group)
		return self._sfno

	@property
	def subframe(self):
		"""subframe commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_subframe'):
			from .Subframe import SubframeCls
			self._subframe = SubframeCls(self._core, self._cmd_group)
		return self._subframe

	@property
	def sync(self):
		"""sync commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import SyncCls
			self._sync = SyncCls(self._core, self._cmd_group)
		return self._sync

	@property
	def tdd(self):
		"""tdd commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdd'):
			from .Tdd import TddCls
			self._tdd = TddCls(self._core, self._cmd_group)
		return self._tdd

	@property
	def compressed(self):
		"""compressed commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_compressed'):
			from .Compressed import CompressedCls
			self._compressed = CompressedCls(self._core, self._cmd_group)
		return self._compressed

	def clone(self) -> 'CcCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CcCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
