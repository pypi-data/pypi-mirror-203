from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScaleCls:
	"""Scale commands group definition. 8 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scale", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import AutoCls
			self._auto = AutoCls(self._core, self._cmd_group)
		return self._auto

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maximum'):
			from .Maximum import MaximumCls
			self._maximum = MaximumCls(self._core, self._cmd_group)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_minimum'):
			from .Minimum import MinimumCls
			self._minimum = MinimumCls(self._core, self._cmd_group)
		return self._minimum

	@property
	def pdivision(self):
		"""pdivision commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdivision'):
			from .Pdivision import PdivisionCls
			self._pdivision = PdivisionCls(self._core, self._cmd_group)
		return self._pdivision

	@property
	def refLevel(self):
		"""refLevel commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_refLevel'):
			from .RefLevel import RefLevelCls
			self._refLevel = RefLevelCls(self._core, self._cmd_group)
		return self._refLevel

	@property
	def refPosition(self):
		"""refPosition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_refPosition'):
			from .RefPosition import RefPositionCls
			self._refPosition = RefPositionCls(self._core, self._cmd_group)
		return self._refPosition

	@property
	def rvalue(self):
		"""rvalue commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rvalue'):
			from .Rvalue import RvalueCls
			self._rvalue = RvalueCls(self._core, self._cmd_group)
		return self._rvalue

	def clone(self) -> 'ScaleCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ScaleCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
