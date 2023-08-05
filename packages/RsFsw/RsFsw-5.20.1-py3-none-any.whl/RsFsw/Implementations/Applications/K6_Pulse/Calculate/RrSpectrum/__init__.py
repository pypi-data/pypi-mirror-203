from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RrSpectrumCls:
	"""RrSpectrum commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rrSpectrum", core, parent)

	@property
	def window(self):
		"""window commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_window'):
			from .Window import WindowCls
			self._window = WindowCls(self._core, self._cmd_group)
		return self._window

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import AutoCls
			self._auto = AutoCls(self._core, self._cmd_group)
		return self._auto

	@property
	def rbw(self):
		"""rbw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbw'):
			from .Rbw import RbwCls
			self._rbw = RbwCls(self._core, self._cmd_group)
		return self._rbw

	def clone(self) -> 'RrSpectrumCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RrSpectrumCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
