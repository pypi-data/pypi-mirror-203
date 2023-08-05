from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TrendCls:
	"""Trend commands group definition. 45 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trend", core, parent)

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

	@property
	def swap(self):
		"""swap commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_swap'):
			from .Swap import SwapCls
			self._swap = SwapCls(self._core, self._cmd_group)
		return self._swap

	def clone(self) -> 'TrendCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TrendCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
