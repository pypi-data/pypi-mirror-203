from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FmSettlingCls:
	"""FmSettling commands group definition. 15 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fmSettling", core, parent)

	@property
	def fmSpoint(self):
		"""fmSpoint commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_fmSpoint'):
			from .FmSpoint import FmSpointCls
			self._fmSpoint = FmSpointCls(self._core, self._cmd_group)
		return self._fmSpoint

	@property
	def fmStime(self):
		"""fmStime commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_fmStime'):
			from .FmStime import FmStimeCls
			self._fmStime = FmStimeCls(self._core, self._cmd_group)
		return self._fmStime

	@property
	def fmsLength(self):
		"""fmsLength commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_fmsLength'):
			from .FmsLength import FmsLengthCls
			self._fmsLength = FmsLengthCls(self._core, self._cmd_group)
		return self._fmsLength

	def clone(self) -> 'FmSettlingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FmSettlingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
