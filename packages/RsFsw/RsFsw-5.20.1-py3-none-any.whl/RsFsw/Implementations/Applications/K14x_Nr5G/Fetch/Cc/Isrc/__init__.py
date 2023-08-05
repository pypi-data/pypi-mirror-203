from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IsrcCls:
	"""Isrc commands group definition. 130 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("isrc", core, parent)

	@property
	def frame(self):
		"""frame commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frame'):
			from .Frame import FrameCls
			self._frame = FrameCls(self._core, self._cmd_group)
		return self._frame

	@property
	def summary(self):
		"""summary commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_summary'):
			from .Summary import SummaryCls
			self._summary = SummaryCls(self._core, self._cmd_group)
		return self._summary

	def clone(self) -> 'IsrcCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IsrcCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
