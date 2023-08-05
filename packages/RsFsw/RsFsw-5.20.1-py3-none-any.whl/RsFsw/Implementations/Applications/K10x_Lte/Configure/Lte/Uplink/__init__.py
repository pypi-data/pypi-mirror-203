from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 72 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	@property
	def cabw(self):
		"""cabw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cabw'):
			from .Cabw import CabwCls
			self._cabw = CabwCls(self._core, self._cmd_group)
		return self._cabw

	@property
	def bdSource(self):
		"""bdSource commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bdSource'):
			from .BdSource import BdSourceCls
			self._bdSource = BdSourceCls(self._core, self._cmd_group)
		return self._bdSource

	@property
	def cc(self):
		"""cc commands group. 17 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .Cc import CcCls
			self._cc = CcCls(self._core, self._cmd_group)
		return self._cc

	def clone(self) -> 'UplinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UplinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
