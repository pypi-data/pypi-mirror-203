from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WienerCls:
	"""Wiener commands group definition. 3 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wiener", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def dspread(self):
		"""dspread commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dspread'):
			from .Dspread import DspreadCls
			self._dspread = DspreadCls(self._core, self._cmd_group)
		return self._dspread

	def clone(self) -> 'WienerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = WienerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
