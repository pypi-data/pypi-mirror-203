from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CcCls:
	"""Cc commands group definition. 179 total commands, 17 Subgroups, 0 group commands
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
	def demod(self):
		"""demod commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_demod'):
			from .Demod import DemodCls
			self._demod = DemodCls(self._core, self._cmd_group)
		return self._demod

	@property
	def dfRange(self):
		"""dfRange commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dfRange'):
			from .DfRange import DfRangeCls
			self._dfRange = DfRangeCls(self._core, self._cmd_group)
		return self._dfRange

	@property
	def euids(self):
		"""euids commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_euids'):
			from .Euids import EuidsCls
			self._euids = EuidsCls(self._core, self._cmd_group)
		return self._euids

	@property
	def fnnf(self):
		"""fnnf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fnnf'):
			from .Fnnf import FnnfCls
			self._fnnf = FnnfCls(self._core, self._cmd_group)
		return self._fnnf

	@property
	def frame(self):
		"""frame commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_frame'):
			from .Frame import FrameCls
			self._frame = FrameCls(self._core, self._cmd_group)
		return self._frame

	@property
	def ftConfig(self):
		"""ftConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ftConfig'):
			from .FtConfig import FtConfigCls
			self._ftConfig = FtConfigCls(self._core, self._cmd_group)
		return self._ftConfig

	@property
	def idc(self):
		"""idc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_idc'):
			from .Idc import IdcCls
			self._idc = IdcCls(self._core, self._cmd_group)
		return self._idc

	@property
	def lte(self):
		"""lte commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Lte import LteCls
			self._lte = LteCls(self._core, self._cmd_group)
		return self._lte

	@property
	def pamapping(self):
		"""pamapping commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pamapping'):
			from .Pamapping import PamappingCls
			self._pamapping = PamappingCls(self._core, self._cmd_group)
		return self._pamapping

	@property
	def plc(self):
		"""plc commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_plc'):
			from .Plc import PlcCls
			self._plc = PlcCls(self._core, self._cmd_group)
		return self._plc

	@property
	def rfuc(self):
		"""rfuc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfuc'):
			from .Rfuc import RfucCls
			self._rfuc = RfucCls(self._core, self._cmd_group)
		return self._rfuc

	@property
	def rpa(self):
		"""rpa commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_rpa'):
			from .Rpa import RpaCls
			self._rpa = RpaCls(self._core, self._cmd_group)
		return self._rpa

	@property
	def ssCa(self):
		"""ssCa commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssCa'):
			from .SsCa import SsCaCls
			self._ssCa = SsCaCls(self._core, self._cmd_group)
		return self._ssCa

	@property
	def ssBlock(self):
		"""ssBlock commands group. 14 Sub-classes, 0 commands."""
		if not hasattr(self, '_ssBlock'):
			from .SsBlock import SsBlockCls
			self._ssBlock = SsBlockCls(self._core, self._cmd_group)
		return self._ssBlock

	@property
	def ssCount(self):
		"""ssCount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssCount'):
			from .SsCount import SsCountCls
			self._ssCount = SsCountCls(self._core, self._cmd_group)
		return self._ssCount

	def clone(self) -> 'CcCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CcCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
