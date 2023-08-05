from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqCls:
	"""Iq commands group definition. 15 total commands, 11 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iq", core, parent)

	@property
	def data(self):
		"""data commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import DataCls
			self._data = DataCls(self._core, self._cmd_group)
		return self._data

	@property
	def ddpd(self):
		"""ddpd commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ddpd'):
			from .Ddpd import DdpdCls
			self._ddpd = DdpdCls(self._core, self._cmd_group)
		return self._ddpd

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import BandwidthCls
			self._bandwidth = BandwidthCls(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def file(self):
		"""file commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_file'):
			from .File import FileCls
			self._file = FileCls(self._core, self._cmd_group)
		return self._file

	@property
	def rlength(self):
		"""rlength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rlength'):
			from .Rlength import RlengthCls
			self._rlength = RlengthCls(self._core, self._cmd_group)
		return self._rlength

	@property
	def synchronized(self):
		"""synchronized commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_synchronized'):
			from .Synchronized import SynchronizedCls
			self._synchronized = SynchronizedCls(self._core, self._cmd_group)
		return self._synchronized

	@property
	def sync(self):
		"""sync commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import SyncCls
			self._sync = SyncCls(self._core, self._cmd_group)
		return self._sync

	@property
	def equalized(self):
		"""equalized commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_equalized'):
			from .Equalized import EqualizedCls
			self._equalized = EqualizedCls(self._core, self._cmd_group)
		return self._equalized

	@property
	def tpis(self):
		"""tpis commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpis'):
			from .Tpis import TpisCls
			self._tpis = TpisCls(self._core, self._cmd_group)
		return self._tpis

	@property
	def symbolRate(self):
		"""symbolRate commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRateCls
			self._symbolRate = SymbolRateCls(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def wband(self):
		"""wband commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_wband'):
			from .Wband import WbandCls
			self._wband = WbandCls(self._core, self._cmd_group)
		return self._wband

	def clone(self) -> 'IqCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IqCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
