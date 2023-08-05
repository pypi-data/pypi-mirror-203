from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RangingCls:
	"""Ranging commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ranging", core, parent)

	@property
	def rmarker(self):
		"""rmarker commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rmarker'):
			from .Rmarker import RmarkerCls
			self._rmarker = RmarkerCls(self._core, self._cmd_group)
		return self._rmarker

	@property
	def srMarker(self):
		"""srMarker commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_srMarker'):
			from .SrMarker import SrMarkerCls
			self._srMarker = SrMarkerCls(self._core, self._cmd_group)
		return self._srMarker

	def clone(self) -> 'RangingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RangingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
