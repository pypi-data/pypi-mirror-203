from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DdpdCls:
	"""Ddpd commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ddpd", core, parent)

	@property
	def waveform(self):
		"""waveform commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_waveform'):
			from .Waveform import WaveformCls
			self._waveform = WaveformCls(self._core, self._cmd_group)
		return self._waveform

	@property
	def operation(self):
		"""operation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_operation'):
			from .Operation import OperationCls
			self._operation = OperationCls(self._core, self._cmd_group)
		return self._operation

	def clone(self) -> 'DdpdCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DdpdCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
