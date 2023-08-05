from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NpratioCls:
	"""Npratio commands group definition. 26 total commands, 11 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("npratio", core, parent)

	@property
	def settings(self):
		"""settings commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_settings'):
			from .Settings import SettingsCls
			self._settings = SettingsCls(self._core, self._cmd_group)
		return self._settings

	@property
	def frequency(self):
		"""frequency commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def control(self):
		"""control commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_control'):
			from .Control import ControlCls
			self._control = ControlCls(self._core, self._cmd_group)
		return self._control

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def notch(self):
		"""notch commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_notch'):
			from .Notch import NotchCls
			self._notch = NotchCls(self._core, self._cmd_group)
		return self._notch

	@property
	def bb(self):
		"""bb commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bb'):
			from .Bb import BbCls
			self._bb = BbCls(self._core, self._cmd_group)
		return self._bb

	@property
	def awgn(self):
		"""awgn commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_awgn'):
			from .Awgn import AwgnCls
			self._awgn = AwgnCls(self._core, self._cmd_group)
		return self._awgn

	@property
	def connection(self):
		"""connection commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_connection'):
			from .Connection import ConnectionCls
			self._connection = ConnectionCls(self._core, self._cmd_group)
		return self._connection

	@property
	def rfOutput(self):
		"""rfOutput commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfOutput'):
			from .RfOutput import RfOutputCls
			self._rfOutput = RfOutputCls(self._core, self._cmd_group)
		return self._rfOutput

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def external(self):
		"""external commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_external'):
			from .External import ExternalCls
			self._external = ExternalCls(self._core, self._cmd_group)
		return self._external

	def clone(self) -> 'NpratioCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NpratioCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
