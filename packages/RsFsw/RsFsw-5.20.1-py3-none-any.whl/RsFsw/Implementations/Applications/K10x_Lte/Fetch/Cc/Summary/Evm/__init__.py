from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EvmCls:
	"""Evm commands group definition. 57 total commands, 27 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("evm", core, parent)

	@property
	def all(self):
		"""all commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	@property
	def dsqp(self):
		"""dsqp commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dsqp'):
			from .Dsqp import DsqpCls
			self._dsqp = DsqpCls(self._core, self._cmd_group)
		return self._dsqp

	@property
	def dssf(self):
		"""dssf commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dssf'):
			from .Dssf import DssfCls
			self._dssf = DssfCls(self._core, self._cmd_group)
		return self._dssf

	@property
	def dsst(self):
		"""dsst commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dsst'):
			from .Dsst import DsstCls
			self._dsst = DsstCls(self._core, self._cmd_group)
		return self._dsst

	@property
	def dsts(self):
		"""dsts commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dsts'):
			from .Dsts import DstsCls
			self._dsts = DstsCls(self._core, self._cmd_group)
		return self._dsts

	@property
	def ds1K(self):
		"""ds1K commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ds1K'):
			from .Ds1K import Ds1KCls
			self._ds1K = Ds1KCls(self._core, self._cmd_group)
		return self._ds1K

	@property
	def pchannel(self):
		"""pchannel commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pchannel'):
			from .Pchannel import PchannelCls
			self._pchannel = PchannelCls(self._core, self._cmd_group)
		return self._pchannel

	@property
	def psignal(self):
		"""psignal commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_psignal'):
			from .Psignal import PsignalCls
			self._psignal = PsignalCls(self._core, self._cmd_group)
		return self._psignal

	@property
	def sdop(self):
		"""sdop commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sdop'):
			from .Sdop import SdopCls
			self._sdop = SdopCls(self._core, self._cmd_group)
		return self._sdop

	@property
	def sdqp(self):
		"""sdqp commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_sdqp'):
			from .Sdqp import SdqpCls
			self._sdqp = SdqpCls(self._core, self._cmd_group)
		return self._sdqp

	@property
	def sdsf(self):
		"""sdsf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sdsf'):
			from .Sdsf import SdsfCls
			self._sdsf = SdsfCls(self._core, self._cmd_group)
		return self._sdsf

	@property
	def sdst(self):
		"""sdst commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_sdst'):
			from .Sdst import SdstCls
			self._sdst = SdstCls(self._core, self._cmd_group)
		return self._sdst

	@property
	def sdts(self):
		"""sdts commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sdts'):
			from .Sdts import SdtsCls
			self._sdts = SdtsCls(self._core, self._cmd_group)
		return self._sdts

	@property
	def spop(self):
		"""spop commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_spop'):
			from .Spop import SpopCls
			self._spop = SpopCls(self._core, self._cmd_group)
		return self._spop

	@property
	def spqp(self):
		"""spqp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_spqp'):
			from .Spqp import SpqpCls
			self._spqp = SpqpCls(self._core, self._cmd_group)
		return self._spqp

	@property
	def spst(self):
		"""spst commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_spst'):
			from .Spst import SpstCls
			self._spst = SpstCls(self._core, self._cmd_group)
		return self._spst

	@property
	def uccd(self):
		"""uccd commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_uccd'):
			from .Uccd import UccdCls
			self._uccd = UccdCls(self._core, self._cmd_group)
		return self._uccd

	@property
	def ucch(self):
		"""ucch commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ucch'):
			from .Ucch import UcchCls
			self._ucch = UcchCls(self._core, self._cmd_group)
		return self._ucch

	@property
	def upop(self):
		"""upop commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_upop'):
			from .Upop import UpopCls
			self._upop = UpopCls(self._core, self._cmd_group)
		return self._upop

	@property
	def upqp(self):
		"""upqp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_upqp'):
			from .Upqp import UpqpCls
			self._upqp = UpqpCls(self._core, self._cmd_group)
		return self._upqp

	@property
	def upra(self):
		"""upra commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_upra'):
			from .Upra import UpraCls
			self._upra = UpraCls(self._core, self._cmd_group)
		return self._upra

	@property
	def upst(self):
		"""upst commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_upst'):
			from .Upst import UpstCls
			self._upst = UpstCls(self._core, self._cmd_group)
		return self._upst

	@property
	def usop(self):
		"""usop commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_usop'):
			from .Usop import UsopCls
			self._usop = UsopCls(self._core, self._cmd_group)
		return self._usop

	@property
	def usqp(self):
		"""usqp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_usqp'):
			from .Usqp import UsqpCls
			self._usqp = UsqpCls(self._core, self._cmd_group)
		return self._usqp

	@property
	def ussf(self):
		"""ussf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ussf'):
			from .Ussf import UssfCls
			self._ussf = UssfCls(self._core, self._cmd_group)
		return self._ussf

	@property
	def usst(self):
		"""usst commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_usst'):
			from .Usst import UsstCls
			self._usst = UsstCls(self._core, self._cmd_group)
		return self._usst

	@property
	def usts(self):
		"""usts commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_usts'):
			from .Usts import UstsCls
			self._usts = UstsCls(self._core, self._cmd_group)
		return self._usts

	def clone(self) -> 'EvmCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EvmCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
