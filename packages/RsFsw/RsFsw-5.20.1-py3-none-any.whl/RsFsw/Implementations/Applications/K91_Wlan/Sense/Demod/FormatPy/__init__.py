from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPyCls:
	"""FormatPy commands group definition. 21 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	@property
	def sigSymbol(self):
		"""sigSymbol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sigSymbol'):
			from .SigSymbol import SigSymbolCls
			self._sigSymbol = SigSymbolCls(self._core, self._cmd_group)
		return self._sigSymbol

	@property
	def bcontent(self):
		"""bcontent commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bcontent'):
			from .Bcontent import BcontentCls
			self._bcontent = BcontentCls(self._core, self._cmd_group)
		return self._bcontent

	@property
	def banalyze(self):
		"""banalyze commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_banalyze'):
			from .Banalyze import BanalyzeCls
			self._banalyze = BanalyzeCls(self._core, self._cmd_group)
		return self._banalyze

	@property
	def mcsIndex(self):
		"""mcsIndex commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcsIndex'):
			from .McsIndex import McsIndexCls
			self._mcsIndex = McsIndexCls(self._core, self._cmd_group)
		return self._mcsIndex

	@property
	def nstsIndex(self):
		"""nstsIndex commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_nstsIndex'):
			from .NstsIndex import NstsIndexCls
			self._nstsIndex = NstsIndexCls(self._core, self._cmd_group)
		return self._nstsIndex

	def clone(self) -> 'FormatPyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FormatPyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
