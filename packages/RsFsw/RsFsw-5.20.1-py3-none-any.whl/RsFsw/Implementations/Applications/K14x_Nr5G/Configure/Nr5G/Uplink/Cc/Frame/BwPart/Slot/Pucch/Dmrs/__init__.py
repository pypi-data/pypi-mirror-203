from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DmrsCls:
	"""Dmrs commands group definition. 12 total commands, 12 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dmrs", core, parent)

	@property
	def additional(self):
		"""additional commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_additional'):
			from .Additional import AdditionalCls
			self._additional = AdditionalCls(self._core, self._cmd_group)
		return self._additional

	@property
	def ghopping(self):
		"""ghopping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ghopping'):
			from .Ghopping import GhoppingCls
			self._ghopping = GhoppingCls(self._core, self._cmd_group)
		return self._ghopping

	@property
	def hid(self):
		"""hid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hid'):
			from .Hid import HidCls
			self._hid = HidCls(self._core, self._cmd_group)
		return self._hid

	@property
	def icShift(self):
		"""icShift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_icShift'):
			from .IcShift import IcShiftCls
			self._icShift = IcShiftCls(self._core, self._cmd_group)
		return self._icShift

	@property
	def isfHopping(self):
		"""isfHopping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_isfHopping'):
			from .IsfHopping import IsfHoppingCls
			self._isfHopping = IsfHoppingCls(self._core, self._cmd_group)
		return self._isfHopping

	@property
	def nid(self):
		"""nid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nid'):
			from .Nid import NidCls
			self._nid = NidCls(self._core, self._cmd_group)
		return self._nid

	@property
	def occLength(self):
		"""occLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_occLength'):
			from .OccLength import OccLengthCls
			self._occLength = OccLengthCls(self._core, self._cmd_group)
		return self._occLength

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def sgeneration(self):
		"""sgeneration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sgeneration'):
			from .Sgeneration import SgenerationCls
			self._sgeneration = SgenerationCls(self._core, self._cmd_group)
		return self._sgeneration

	@property
	def shPrb(self):
		"""shPrb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_shPrb'):
			from .ShPrb import ShPrbCls
			self._shPrb = ShPrbCls(self._core, self._cmd_group)
		return self._shPrb

	@property
	def sid(self):
		"""sid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sid'):
			from .Sid import SidCls
			self._sid = SidCls(self._core, self._cmd_group)
		return self._sid

	@property
	def tdoIndex(self):
		"""tdoIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdoIndex'):
			from .TdoIndex import TdoIndexCls
			self._tdoIndex = TdoIndexCls(self._core, self._cmd_group)
		return self._tdoIndex

	def clone(self) -> 'DmrsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DmrsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
