from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FetchCls:
	"""Fetch commands group definition. 96 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fetch", core, parent)

	@property
	def burst(self):
		"""burst commands group. 29 Sub-classes, 0 commands."""
		if not hasattr(self, '_burst'):
			from .Burst import BurstCls
			self._burst = BurstCls(self._core, self._cmd_group)
		return self._burst

	@property
	def sfield(self):
		"""sfield commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sfield'):
			from .Sfield import SfieldCls
			self._sfield = SfieldCls(self._core, self._cmd_group)
		return self._sfield

	@property
	def symbol(self):
		"""symbol commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_symbol'):
			from .Symbol import SymbolCls
			self._symbol = SymbolCls(self._core, self._cmd_group)
		return self._symbol

	@property
	def scDetailed(self):
		"""scDetailed commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_scDetailed'):
			from .ScDetailed import ScDetailedCls
			self._scDetailed = ScDetailedCls(self._core, self._cmd_group)
		return self._scDetailed

	@property
	def uteSummary(self):
		"""uteSummary commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_uteSummary'):
			from .UteSummary import UteSummaryCls
			self._uteSummary = UteSummaryCls(self._core, self._cmd_group)
		return self._uteSummary

	@property
	def sfSummary(self):
		"""sfSummary commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sfSummary'):
			from .SfSummary import SfSummaryCls
			self._sfSummary = SfSummaryCls(self._core, self._cmd_group)
		return self._sfSummary

	def clone(self) -> 'FetchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FetchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
