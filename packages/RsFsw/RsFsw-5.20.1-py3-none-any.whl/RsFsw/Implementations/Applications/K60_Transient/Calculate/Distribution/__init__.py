from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DistributionCls:
	"""Distribution commands group definition. 17 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("distribution", core, parent)

	@property
	def nbins(self):
		"""nbins commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nbins'):
			from .Nbins import NbinsCls
			self._nbins = NbinsCls(self._core, self._cmd_group)
		return self._nbins

	@property
	def hop(self):
		"""hop commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_hop'):
			from .Hop import HopCls
			self._hop = HopCls(self._core, self._cmd_group)
		return self._hop

	@property
	def chirp(self):
		"""chirp commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_chirp'):
			from .Chirp import ChirpCls
			self._chirp = ChirpCls(self._core, self._cmd_group)
		return self._chirp

	@property
	def x(self):
		"""x commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_x'):
			from .X import XCls
			self._x = XCls(self._core, self._cmd_group)
		return self._x

	@property
	def y(self):
		"""y commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_y'):
			from .Y import YCls
			self._y = YCls(self._core, self._cmd_group)
		return self._y

	def clone(self) -> 'DistributionCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DistributionCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
