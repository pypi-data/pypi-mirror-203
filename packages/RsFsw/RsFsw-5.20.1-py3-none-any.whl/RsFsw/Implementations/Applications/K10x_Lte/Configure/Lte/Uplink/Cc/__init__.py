from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CcCls:
	"""Cc commands group definition. 70 total commands, 17 Subgroups, 0 group commands
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
	def bw(self):
		"""bw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bw'):
			from .Bw import BwCls
			self._bw = BwCls(self._core, self._cmd_group)
		return self._bw

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
	def drs(self):
		"""drs commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_drs'):
			from .Drs import DrsCls
			self._drs = DrsCls(self._core, self._cmd_group)
		return self._drs

	@property
	def mimo(self):
		"""mimo commands group. 1 Sub-classes, 0 commands."""
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
	def prach(self):
		"""prach commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_prach'):
			from .Prach import PrachCls
			self._prach = PrachCls(self._core, self._cmd_group)
		return self._prach

	@property
	def pucch(self):
		"""pucch commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_pucch'):
			from .Pucch import PucchCls
			self._pucch = PucchCls(self._core, self._cmd_group)
		return self._pucch

	@property
	def pusch(self):
		"""pusch commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_pusch'):
			from .Pusch import PuschCls
			self._pusch = PuschCls(self._core, self._cmd_group)
		return self._pusch

	@property
	def scin(self):
		"""scin commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scin'):
			from .Scin import ScinCls
			self._scin = ScinCls(self._core, self._cmd_group)
		return self._scin

	@property
	def sfno(self):
		"""sfno commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfno'):
			from .Sfno import SfnoCls
			self._sfno = SfnoCls(self._core, self._cmd_group)
		return self._sfno

	@property
	def srs(self):
		"""srs commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_srs'):
			from .Srs import SrsCls
			self._srs = SrsCls(self._core, self._cmd_group)
		return self._srs

	@property
	def subframe(self):
		"""subframe commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_subframe'):
			from .Subframe import SubframeCls
			self._subframe = SubframeCls(self._core, self._cmd_group)
		return self._subframe

	@property
	def tdd(self):
		"""tdd commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdd'):
			from .Tdd import TddCls
			self._tdd = TddCls(self._core, self._cmd_group)
		return self._tdd

	@property
	def ueId(self):
		"""ueId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueId'):
			from .UeId import UeIdCls
			self._ueId = UeIdCls(self._core, self._cmd_group)
		return self._ueId

	def clone(self) -> 'CcCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CcCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
