from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RefSignalCls:
	"""RefSignal commands group definition. 27 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refSignal", core, parent)

	@property
	def cgw(self):
		"""cgw commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cgw'):
			from .Cgw import CgwCls
			self._cgw = CgwCls(self._core, self._cmd_group)
		return self._cgw

	@property
	def cwf(self):
		"""cwf commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cwf'):
			from .Cwf import CwfCls
			self._cwf = CwfCls(self._core, self._cmd_group)
		return self._cwf

	@property
	def gos(self):
		"""gos commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_gos'):
			from .Gos import GosCls
			self._gos = GosCls(self._core, self._cmd_group)
		return self._gos

	@property
	def segment(self):
		"""segment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_segment'):
			from .Segment import SegmentCls
			self._segment = SegmentCls(self._core, self._cmd_group)
		return self._segment

	@property
	def sinfo(self):
		"""sinfo commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_sinfo'):
			from .Sinfo import SinfoCls
			self._sinfo = SinfoCls(self._core, self._cmd_group)
		return self._sinfo

	def clone(self) -> 'RefSignalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RefSignalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
