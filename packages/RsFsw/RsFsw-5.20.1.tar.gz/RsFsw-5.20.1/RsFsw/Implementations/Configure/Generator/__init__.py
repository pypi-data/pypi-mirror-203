from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GeneratorCls:
	"""Generator commands group definition. 39 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generator", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

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

	@property
	def target(self):
		"""target commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_target'):
			from .Target import TargetCls
			self._target = TargetCls(self._core, self._cmd_group)
		return self._target

	@property
	def npratio(self):
		"""npratio commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_npratio'):
			from .Npratio import NpratioCls
			self._npratio = NpratioCls(self._core, self._cmd_group)
		return self._npratio

	@property
	def relay(self):
		"""relay commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_relay'):
			from .Relay import RelayCls
			self._relay = RelayCls(self._core, self._cmd_group)
		return self._relay

	@property
	def connection(self):
		"""connection commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_connection'):
			from .Connection import ConnectionCls
			self._connection = ConnectionCls(self._core, self._cmd_group)
		return self._connection

	@property
	def ipConnection(self):
		"""ipConnection commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipConnection'):
			from .IpConnection import IpConnectionCls
			self._ipConnection = IpConnectionCls(self._core, self._cmd_group)
		return self._ipConnection

	@property
	def recording(self):
		"""recording commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_recording'):
			from .Recording import RecordingCls
			self._recording = RecordingCls(self._core, self._cmd_group)
		return self._recording

	def clone(self) -> 'GeneratorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = GeneratorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
