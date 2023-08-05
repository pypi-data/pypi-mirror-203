from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhaseCls:
	"""Phase commands group definition. 15 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	@property
	def avgPm(self):
		"""avgPm commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_avgPm'):
			from .AvgPm import AvgPmCls
			self._avgPm = AvgPmCls(self._core, self._cmd_group)
		return self._avgPm

	@property
	def maxPm(self):
		"""maxPm commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_maxPm'):
			from .MaxPm import MaxPmCls
			self._maxPm = MaxPmCls(self._core, self._cmd_group)
		return self._maxPm

	@property
	def rmsPm(self):
		"""rmsPm commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmsPm'):
			from .RmsPm import RmsPmCls
			self._rmsPm = RmsPmCls(self._core, self._cmd_group)
		return self._rmsPm

	def clone(self) -> 'PhaseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PhaseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
