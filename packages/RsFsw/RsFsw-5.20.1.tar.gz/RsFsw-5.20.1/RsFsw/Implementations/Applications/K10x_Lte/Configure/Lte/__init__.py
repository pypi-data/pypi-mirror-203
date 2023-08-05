from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LteCls:
	"""Lte commands group definition. 178 total commands, 14 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lte", core, parent)

	@property
	def antMatrix(self):
		"""antMatrix commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_antMatrix'):
			from .AntMatrix import AntMatrixCls
			self._antMatrix = AntMatrixCls(self._core, self._cmd_group)
		return self._antMatrix

	@property
	def caggregation(self):
		"""caggregation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_caggregation'):
			from .Caggregation import CaggregationCls
			self._caggregation = CaggregationCls(self._core, self._cmd_group)
		return self._caggregation

	@property
	def downlink(self):
		"""downlink commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import DownlinkCls
			self._downlink = DownlinkCls(self._core, self._cmd_group)
		return self._downlink

	@property
	def duplexing(self):
		"""duplexing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_duplexing'):
			from .Duplexing import DuplexingCls
			self._duplexing = DuplexingCls(self._core, self._cmd_group)
		return self._duplexing

	@property
	def eutra(self):
		"""eutra commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_eutra'):
			from .Eutra import EutraCls
			self._eutra = EutraCls(self._core, self._cmd_group)
		return self._eutra

	@property
	def ldirection(self):
		"""ldirection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ldirection'):
			from .Ldirection import LdirectionCls
			self._ldirection = LdirectionCls(self._core, self._cmd_group)
		return self._ldirection

	@property
	def measurement(self):
		"""measurement commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_measurement'):
			from .Measurement import MeasurementCls
			self._measurement = MeasurementCls(self._core, self._cmd_group)
		return self._measurement

	@property
	def mimo(self):
		"""mimo commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mimo'):
			from .Mimo import MimoCls
			self._mimo = MimoCls(self._core, self._cmd_group)
		return self._mimo

	@property
	def ndevices(self):
		"""ndevices commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ndevices'):
			from .Ndevices import NdevicesCls
			self._ndevices = NdevicesCls(self._core, self._cmd_group)
		return self._ndevices

	@property
	def noCc(self):
		"""noCc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noCc'):
			from .NoCc import NoCcCls
			self._noCc = NoCcCls(self._core, self._cmd_group)
		return self._noCc

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
	def uplink(self):
		"""uplink commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import UplinkCls
			self._uplink = UplinkCls(self._core, self._cmd_group)
		return self._uplink

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePyCls
			self._typePy = TypePyCls(self._core, self._cmd_group)
		return self._typePy

	def clone(self) -> 'LteCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LteCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
