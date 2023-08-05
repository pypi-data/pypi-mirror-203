from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CcCls:
	"""Cc commands group definition. 146 total commands, 14 Subgroups, 0 group commands
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
	def dfRange(self):
		"""dfRange commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dfRange'):
			from .DfRange import DfRangeCls
			self._dfRange = DfRangeCls(self._core, self._cmd_group)
		return self._dfRange

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
	def pamapping(self):
		"""pamapping commands group. 2 Sub-classes, 0 commands."""
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
	def prach(self):
		"""prach commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_prach'):
			from .Prach import PrachCls
			self._prach = PrachCls(self._core, self._cmd_group)
		return self._prach

	@property
	def pusch(self):
		"""pusch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pusch'):
			from .Pusch import PuschCls
			self._pusch = PuschCls(self._core, self._cmd_group)
		return self._pusch

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
	def sflatness(self):
		"""sflatness commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sflatness'):
			from .Sflatness import SflatnessCls
			self._sflatness = SflatnessCls(self._core, self._cmd_group)
		return self._sflatness

	@property
	def tpRecoding(self):
		"""tpRecoding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpRecoding'):
			from .TpRecoding import TpRecodingCls
			self._tpRecoding = TpRecodingCls(self._core, self._cmd_group)
		return self._tpRecoding

	def clone(self) -> 'CcCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CcCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
