from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NpdschCls:
	"""Npdsch commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("npdsch", core, parent)

	@property
	def dmodulation(self):
		"""dmodulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dmodulation'):
			from .Dmodulation import DmodulationCls
			self._dmodulation = DmodulationCls(self._core, self._cmd_group)
		return self._dmodulation

	@property
	def sflist(self):
		"""sflist commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sflist'):
			from .Sflist import SflistCls
			self._sflist = SflistCls(self._core, self._cmd_group)
		return self._sflist

	@property
	def ueId(self):
		"""ueId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueId'):
			from .UeId import UeIdCls
			self._ueId = UeIdCls(self._core, self._cmd_group)
		return self._ueId

	def clone(self) -> 'NpdschCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NpdschCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
