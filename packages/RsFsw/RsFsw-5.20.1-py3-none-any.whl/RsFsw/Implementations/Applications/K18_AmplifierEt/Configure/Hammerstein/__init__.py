from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HammersteinCls:
	"""Hammerstein commands group definition. 8 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hammerstein", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def iteration(self):
		"""iteration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iteration'):
			from .Iteration import IterationCls
			self._iteration = IterationCls(self._core, self._cmd_group)
		return self._iteration

	@property
	def order(self):
		"""order commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_order'):
			from .Order import OrderCls
			self._order = OrderCls(self._core, self._cmd_group)
		return self._order

	@property
	def mupGenerator(self):
		"""mupGenerator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mupGenerator'):
			from .MupGenerator import MupGeneratorCls
			self._mupGenerator = MupGeneratorCls(self._core, self._cmd_group)
		return self._mupGenerator

	@property
	def genWaveform(self):
		"""genWaveform commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_genWaveform'):
			from .GenWaveform import GenWaveformCls
			self._genWaveform = GenWaveformCls(self._core, self._cmd_group)
		return self._genWaveform

	@property
	def nonlinearity(self):
		"""nonlinearity commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_nonlinearity'):
			from .Nonlinearity import NonlinearityCls
			self._nonlinearity = NonlinearityCls(self._core, self._cmd_group)
		return self._nonlinearity

	@property
	def filterPy(self):
		"""filterPy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPyCls
			self._filterPy = FilterPyCls(self._core, self._cmd_group)
		return self._filterPy

	def clone(self) -> 'HammersteinCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HammersteinCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
