from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SemCls:
	"""Sem commands group definition. 8 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sem", core, parent)

	@property
	def category(self):
		"""category commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_category'):
			from .Category import CategoryCls
			self._category = CategoryCls(self._core, self._cmd_group)
		return self._category

	@property
	def chbs(self):
		"""chbs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_chbs'):
			from .Chbs import ChbsCls
			self._chbs = ChbsCls(self._core, self._cmd_group)
		return self._chbs

	@property
	def oband(self):
		"""oband commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_oband'):
			from .Oband import ObandCls
			self._oband = ObandCls(self._core, self._cmd_group)
		return self._oband

	@property
	def piom(self):
		"""piom commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_piom'):
			from .Piom import PiomCls
			self._piom = PiomCls(self._core, self._cmd_group)
		return self._piom

	@property
	def piov(self):
		"""piov commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_piov'):
			from .Piov import PiovCls
			self._piov = PiovCls(self._core, self._cmd_group)
		return self._piov

	@property
	def uplink(self):
		"""uplink commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import UplinkCls
			self._uplink = UplinkCls(self._core, self._cmd_group)
		return self._uplink

	def clone(self) -> 'SemCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SemCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
