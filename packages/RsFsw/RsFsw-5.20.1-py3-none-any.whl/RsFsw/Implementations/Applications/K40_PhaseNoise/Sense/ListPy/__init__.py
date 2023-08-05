from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPyCls:
	"""ListPy commands group definition. 10 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	@property
	def bandwidth(self):
		"""bandwidth commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import BandwidthCls
			self._bandwidth = BandwidthCls(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def iqWindow(self):
		"""iqWindow commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqWindow'):
			from .IqWindow import IqWindowCls
			self._iqWindow = IqWindowCls(self._core, self._cmd_group)
		return self._iqWindow

	@property
	def sweep(self):
		"""sweep commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sweep'):
			from .Sweep import SweepCls
			self._sweep = SweepCls(self._core, self._cmd_group)
		return self._sweep

	@property
	def range(self):
		"""range commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_range'):
			from .Range import RangeCls
			self._range = RangeCls(self._core, self._cmd_group)
		return self._range

	def clone(self) -> 'ListPyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
