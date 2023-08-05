from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 20 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def all(self):
		"""all commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	@property
	def crate(self):
		"""crate commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_crate'):
			from .Crate import CrateCls
			self._crate = CrateCls(self._core, self._cmd_group)
		return self._crate

	@property
	def deviation(self):
		"""deviation commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_deviation'):
			from .Deviation import DeviationCls
			self._deviation = DeviationCls(self._core, self._cmd_group)
		return self._deviation

	@property
	def perror(self):
		"""perror commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_perror'):
			from .Perror import PerrorCls
			self._perror = PerrorCls(self._core, self._cmd_group)
		return self._perror

	@property
	def point(self):
		"""point commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_point'):
			from .Point import PointCls
			self._point = PointCls(self._core, self._cmd_group)
		return self._point

	@property
	def ppFrequency(self):
		"""ppFrequency commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ppFrequency'):
			from .PpFrequency import PpFrequencyCls
			self._ppFrequency = PpFrequencyCls(self._core, self._cmd_group)
		return self._ppFrequency

	@property
	def rerror(self):
		"""rerror commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_rerror'):
			from .Rerror import RerrorCls
			self._rerror = RerrorCls(self._core, self._cmd_group)
		return self._rerror

	def clone(self) -> 'FrequencyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FrequencyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
