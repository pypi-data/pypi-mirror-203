from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RiqCls:
	"""Riq commands group definition. 14 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("riq", core, parent)

	@property
	def select(self):
		"""select commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_select'):
			from .Select import SelectCls
			self._select = SelectCls(self._core, self._cmd_group)
		return self._select

	@property
	def fiq(self):
		"""fiq commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_fiq'):
			from .Fiq import FiqCls
			self._fiq = FiqCls(self._core, self._cmd_group)
		return self._fiq

	@property
	def pfm(self):
		"""pfm commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pfm'):
			from .Pfm import PfmCls
			self._pfm = PfmCls(self._core, self._cmd_group)
		return self._pfm

	@property
	def barker(self):
		"""barker commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_barker'):
			from .Barker import BarkerCls
			self._barker = BarkerCls(self._core, self._cmd_group)
		return self._barker

	@property
	def ebarker(self):
		"""ebarker commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ebarker'):
			from .Ebarker import EbarkerCls
			self._ebarker = EbarkerCls(self._core, self._cmd_group)
		return self._ebarker

	def clone(self) -> 'RiqCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RiqCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
