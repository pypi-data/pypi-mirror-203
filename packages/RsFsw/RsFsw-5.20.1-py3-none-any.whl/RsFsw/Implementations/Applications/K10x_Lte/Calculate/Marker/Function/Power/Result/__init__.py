from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	@property
	def details(self):
		"""details commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_details'):
			from .Details import DetailsCls
			self._details = DetailsCls(self._core, self._cmd_group)
		return self._details

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_current'):
			from .Current import CurrentCls
			self._current = CurrentCls(self._core, self._cmd_group)
		return self._current

	@property
	def phz(self):
		"""phz commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phz'):
			from .Phz import PhzCls
			self._phz = PhzCls(self._core, self._cmd_group)
		return self._phz

	@property
	def unit(self):
		"""unit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_unit'):
			from .Unit import UnitCls
			self._unit = UnitCls(self._core, self._cmd_group)
		return self._unit

	def clone(self) -> 'ResultCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ResultCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
