from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DexportCls:
	"""Dexport commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dexport", core, parent)

	@property
	def dseparator(self):
		"""dseparator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dseparator'):
			from .Dseparator import DseparatorCls
			self._dseparator = DseparatorCls(self._core, self._cmd_group)
		return self._dseparator

	@property
	def xdistrib(self):
		"""xdistrib commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_xdistrib'):
			from .Xdistrib import XdistribCls
			self._xdistrib = XdistribCls(self._core, self._cmd_group)
		return self._xdistrib

	def clone(self) -> 'DexportCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DexportCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
