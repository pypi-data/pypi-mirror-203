from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RelayCls:
	"""Relay commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("relay", core, parent)

	@property
	def write(self):
		"""write commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_write'):
			from .Write import WriteCls
			self._write = WriteCls(self._core, self._cmd_group)
		return self._write

	@property
	def read(self):
		"""read commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_read'):
			from .Read import ReadCls
			self._read = ReadCls(self._core, self._cmd_group)
		return self._read

	def clone(self) -> 'RelayCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RelayCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
