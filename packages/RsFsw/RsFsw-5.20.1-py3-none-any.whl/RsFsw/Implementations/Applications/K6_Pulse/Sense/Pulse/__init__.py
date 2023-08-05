from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PulseCls:
	"""Pulse commands group definition. 486 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pulse", core, parent)

	@property
	def id(self):
		"""id commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_id'):
			from .Id import IdCls
			self._id = IdCls(self._core, self._cmd_group)
		return self._id

	@property
	def number(self):
		"""number commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_number'):
			from .Number import NumberCls
			self._number = NumberCls(self._core, self._cmd_group)
		return self._number

	@property
	def count(self):
		"""count commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import CountCls
			self._count = CountCls(self._core, self._cmd_group)
		return self._count

	@property
	def frequency(self):
		"""frequency commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def phase(self):
		"""phase commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import PhaseCls
			self._phase = PhaseCls(self._core, self._cmd_group)
		return self._phase

	@property
	def power(self):
		"""power commands group. 16 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def timing(self):
		"""timing commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_timing'):
			from .Timing import TimingCls
			self._timing = TimingCls(self._core, self._cmd_group)
		return self._timing

	@property
	def emodel(self):
		"""emodel commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_emodel'):
			from .Emodel import EmodelCls
			self._emodel = EmodelCls(self._core, self._cmd_group)
		return self._emodel

	@property
	def tsidelobe(self):
		"""tsidelobe commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_tsidelobe'):
			from .Tsidelobe import TsidelobeCls
			self._tsidelobe = TsidelobeCls(self._core, self._cmd_group)
		return self._tsidelobe

	def clone(self) -> 'PulseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PulseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
