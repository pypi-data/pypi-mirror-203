from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AmplCls:
	"""Ampl commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ampl", core, parent)

	@property
	def icomponent(self):
		"""icomponent commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_icomponent'):
			from .Icomponent import IcomponentCls
			self._icomponent = IcomponentCls(self._core, self._cmd_group)
		return self._icomponent

	@property
	def qcomponent(self):
		"""qcomponent commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_qcomponent'):
			from .Qcomponent import QcomponentCls
			self._qcomponent = QcomponentCls(self._core, self._cmd_group)
		return self._qcomponent

	def clone(self) -> 'AmplCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AmplCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
