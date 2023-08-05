from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GeneratorCls:
	"""Generator commands group definition. 27 total commands, 12 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generator", core, parent)

	@property
	def control(self):
		"""control commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_control'):
			from .Control import ControlCls
			self._control = ControlCls(self._core, self._cmd_group)
		return self._control

	@property
	def external(self):
		"""external commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_external'):
			from .External import ExternalCls
			self._external = ExternalCls(self._core, self._cmd_group)
		return self._external

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def ipConnection(self):
		"""ipConnection commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipConnection'):
			from .IpConnection import IpConnectionCls
			self._ipConnection = IpConnectionCls(self._core, self._cmd_group)
		return self._ipConnection

	@property
	def power(self):
		"""power commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def level(self):
		"""level commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_level'):
			from .Level import LevelCls
			self._level = LevelCls(self._core, self._cmd_group)
		return self._level

	@property
	def dut(self):
		"""dut commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dut'):
			from .Dut import DutCls
			self._dut = DutCls(self._core, self._cmd_group)
		return self._dut

	@property
	def rfOutput(self):
		"""rfOutput commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfOutput'):
			from .RfOutput import RfOutputCls
			self._rfOutput = RfOutputCls(self._core, self._cmd_group)
		return self._rfOutput

	@property
	def segment(self):
		"""segment commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_segment'):
			from .Segment import SegmentCls
			self._segment = SegmentCls(self._core, self._cmd_group)
		return self._segment

	@property
	def settings(self):
		"""settings commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_settings'):
			from .Settings import SettingsCls
			self._settings = SettingsCls(self._core, self._cmd_group)
		return self._settings

	@property
	def target(self):
		"""target commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_target'):
			from .Target import TargetCls
			self._target = TargetCls(self._core, self._cmd_group)
		return self._target

	@property
	def relay(self):
		"""relay commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_relay'):
			from .Relay import RelayCls
			self._relay = RelayCls(self._core, self._cmd_group)
		return self._relay

	def clone(self) -> 'GeneratorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = GeneratorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
