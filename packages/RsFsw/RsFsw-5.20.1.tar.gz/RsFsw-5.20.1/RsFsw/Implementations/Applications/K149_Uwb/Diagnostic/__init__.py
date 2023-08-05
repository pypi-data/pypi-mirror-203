from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DiagnosticCls:
	"""Diagnostic commands group definition. 3 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("diagnostic", core, parent)

	@property
	def dsp(self):
		"""dsp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dsp'):
			from .Dsp import DspCls
			self._dsp = DspCls(self._core, self._cmd_group)
		return self._dsp

	@property
	def simulation(self):
		"""simulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_simulation'):
			from .Simulation import SimulationCls
			self._simulation = SimulationCls(self._core, self._cmd_group)
		return self._simulation

	def clone(self) -> 'DiagnosticCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DiagnosticCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
