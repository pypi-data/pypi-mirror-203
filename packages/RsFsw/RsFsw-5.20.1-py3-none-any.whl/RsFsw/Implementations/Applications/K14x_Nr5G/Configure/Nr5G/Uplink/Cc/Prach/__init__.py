from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrachCls:
	"""Prach commands group definition. 9 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prach", core, parent)

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPyCls
			self._formatPy = FormatPyCls(self._core, self._cmd_group)
		return self._formatPy

	@property
	def lra(self):
		"""lra commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lra'):
			from .Lra import LraCls
			self._lra = LraCls(self._core, self._cmd_group)
		return self._lra

	@property
	def scs(self):
		"""scs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scs'):
			from .Scs import ScsCls
			self._scs = ScsCls(self._core, self._cmd_group)
		return self._scs

	@property
	def rbOffset(self):
		"""rbOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbOffset'):
			from .RbOffset import RbOffsetCls
			self._rbOffset = RbOffsetCls(self._core, self._cmd_group)
		return self._rbOffset

	@property
	def rset(self):
		"""rset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rset'):
			from .Rset import RsetCls
			self._rset = RsetCls(self._core, self._cmd_group)
		return self._rset

	@property
	def rsequence(self):
		"""rsequence commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rsequence'):
			from .Rsequence import RsequenceCls
			self._rsequence = RsequenceCls(self._core, self._cmd_group)
		return self._rsequence

	@property
	def zcZone(self):
		"""zcZone commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_zcZone'):
			from .ZcZone import ZcZoneCls
			self._zcZone = ZcZoneCls(self._core, self._cmd_group)
		return self._zcZone

	@property
	def preamble(self):
		"""preamble commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_preamble'):
			from .Preamble import PreambleCls
			self._preamble = PreambleCls(self._core, self._cmd_group)
		return self._preamble

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	def clone(self) -> 'PrachCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PrachCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
