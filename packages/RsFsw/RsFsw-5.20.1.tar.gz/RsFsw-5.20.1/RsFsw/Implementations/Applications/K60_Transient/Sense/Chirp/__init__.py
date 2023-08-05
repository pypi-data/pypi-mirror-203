from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChirpCls:
	"""Chirp commands group definition. 157 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("chirp", core, parent)

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
	def state(self):
		"""state commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def timing(self):
		"""timing commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_timing'):
			from .Timing import TimingCls
			self._timing = TimingCls(self._core, self._cmd_group)
		return self._timing

	@property
	def fmSettling(self):
		"""fmSettling commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_fmSettling'):
			from .FmSettling import FmSettlingCls
			self._fmSettling = FmSettlingCls(self._core, self._cmd_group)
		return self._fmSettling

	@property
	def frequency(self):
		"""frequency commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def power(self):
		"""power commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def phase(self):
		"""phase commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import PhaseCls
			self._phase = PhaseCls(self._core, self._cmd_group)
		return self._phase

	@property
	def pmSettling(self):
		"""pmSettling commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmSettling'):
			from .PmSettling import PmSettlingCls
			self._pmSettling = PmSettlingCls(self._core, self._cmd_group)
		return self._pmSettling

	def clone(self) -> 'ChirpCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ChirpCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
