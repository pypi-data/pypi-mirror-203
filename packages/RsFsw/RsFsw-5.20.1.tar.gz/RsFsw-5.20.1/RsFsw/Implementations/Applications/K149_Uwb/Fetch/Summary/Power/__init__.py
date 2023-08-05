from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerCls:
	"""Power commands group definition. 36 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def iqOffset(self):
		"""iqOffset commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffsetCls
			self._iqOffset = IqOffsetCls(self._core, self._cmd_group)
		return self._iqOffset

	@property
	def packet(self):
		"""packet commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_packet'):
			from .Packet import PacketCls
			self._packet = PacketCls(self._core, self._cmd_group)
		return self._packet

	@property
	def psdu(self):
		"""psdu commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_psdu'):
			from .Psdu import PsduCls
			self._psdu = PsduCls(self._core, self._cmd_group)
		return self._psdu

	@property
	def shr(self):
		"""shr commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_shr'):
			from .Shr import ShrCls
			self._shr = ShrCls(self._core, self._cmd_group)
		return self._shr

	@property
	def sts(self):
		"""sts commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_sts'):
			from .Sts import StsCls
			self._sts = StsCls(self._core, self._cmd_group)
		return self._sts

	def clone(self) -> 'PowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
