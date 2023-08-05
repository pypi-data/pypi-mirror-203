from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PservoingCls:
	"""Pservoing commands group definition. 8 total commands, 5 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pservoing", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def target(self):
		"""target commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_target'):
			from .Target import TargetCls
			self._target = TargetCls(self._core, self._cmd_group)
		return self._target

	@property
	def max(self):
		"""max commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_max'):
			from .Max import MaxCls
			self._max = MaxCls(self._core, self._cmd_group)
		return self._max

	@property
	def glc(self):
		"""glc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_glc'):
			from .Glc import GlcCls
			self._glc = GlcCls(self._core, self._cmd_group)
		return self._glc

	@property
	def inputPy(self):
		"""inputPy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPyCls
			self._inputPy = InputPyCls(self._core, self._cmd_group)
		return self._inputPy

	def start(self) -> None:
		"""SCPI: [SENSe]:PSERvoing:STARt \n
		Snippet: driver.applications.k18AmplifierEt.sense.pservoing.start() \n
		Starts the power servoing sequence. \n
		"""
		self._core.io.write(f'SENSe:PSERvoing:STARt')

	def start_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:PSERvoing:STARt \n
		Snippet: driver.applications.k18AmplifierEt.sense.pservoing.start_with_opc() \n
		Starts the power servoing sequence. \n
		Same as start, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:PSERvoing:STARt', opc_timeout_ms)

	def clone(self) -> 'PservoingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PservoingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
