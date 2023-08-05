from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CreferenceCls:
	"""Creference commands group definition. 7 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("creference", core, parent)

	@property
	def value(self):
		"""value commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_value'):
			from .Value import ValueCls
			self._value = ValueCls(self._core, self._cmd_group)
		return self._value

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def preference(self):
		"""preference commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_preference'):
			from .Preference import PreferenceCls
			self._preference = PreferenceCls(self._core, self._cmd_group)
		return self._preference

	@property
	def freference(self):
		"""freference commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_freference'):
			from .Freference import FreferenceCls
			self._freference = FreferenceCls(self._core, self._cmd_group)
		return self._freference

	@property
	def harmonics(self):
		"""harmonics commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_harmonics'):
			from .Harmonics import HarmonicsCls
			self._harmonics = HarmonicsCls(self._core, self._cmd_group)
		return self._harmonics

	def clone(self) -> 'CreferenceCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CreferenceCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
