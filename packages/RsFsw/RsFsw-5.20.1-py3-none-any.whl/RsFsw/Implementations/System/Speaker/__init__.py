from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpeakerCls:
	"""Speaker commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("speaker", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def volume(self):
		"""volume commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_volume'):
			from .Volume import VolumeCls
			self._volume = VolumeCls(self._core, self._cmd_group)
		return self._volume

	@property
	def maxVolume(self):
		"""maxVolume commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maxVolume'):
			from .MaxVolume import MaxVolumeCls
			self._maxVolume = MaxVolumeCls(self._core, self._cmd_group)
		return self._maxVolume

	def clone(self) -> 'SpeakerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SpeakerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
