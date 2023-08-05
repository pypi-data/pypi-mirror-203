from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DemodCls:
	"""Demod commands group definition. 11 total commands, 11 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demod", core, parent)

	@property
	def caMode(self):
		"""caMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_caMode'):
			from .CaMode import CaModeCls
			self._caMode = CaModeCls(self._core, self._cmd_group)
		return self._caMode

	@property
	def cestimation(self):
		"""cestimation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cestimation'):
			from .Cestimation import CestimationCls
			self._cestimation = CestimationCls(self._core, self._cmd_group)
		return self._cestimation

	@property
	def cetAverage(self):
		"""cetAverage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cetAverage'):
			from .CetAverage import CetAverageCls
			self._cetAverage = CetAverageCls(self._core, self._cmd_group)
		return self._cetAverage

	@property
	def cmethod(self):
		"""cmethod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cmethod'):
			from .Cmethod import CmethodCls
			self._cmethod = CmethodCls(self._core, self._cmd_group)
		return self._cmethod

	@property
	def crdata(self):
		"""crdata commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crdata'):
			from .Crdata import CrdataCls
			self._crdata = CrdataCls(self._core, self._cmd_group)
		return self._crdata

	@property
	def ddata(self):
		"""ddata commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ddata'):
			from .Ddata import DdataCls
			self._ddata = DdataCls(self._core, self._cmd_group)
		return self._ddata

	@property
	def eflRange(self):
		"""eflRange commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eflRange'):
			from .EflRange import EflRangeCls
			self._eflRange = EflRangeCls(self._core, self._cmd_group)
		return self._eflRange

	@property
	def filterPy(self):
		"""filterPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPyCls
			self._filterPy = FilterPyCls(self._core, self._cmd_group)
		return self._filterPy

	@property
	def mcFilter(self):
		"""mcFilter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcFilter'):
			from .McFilter import McFilterCls
			self._mcFilter = McFilterCls(self._core, self._cmd_group)
		return self._mcFilter

	@property
	def prData(self):
		"""prData commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prData'):
			from .PrData import PrDataCls
			self._prData = PrDataCls(self._core, self._cmd_group)
		return self._prData

	@property
	def stAdjust(self):
		"""stAdjust commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stAdjust'):
			from .StAdjust import StAdjustCls
			self._stAdjust = StAdjustCls(self._core, self._cmd_group)
		return self._stAdjust

	def clone(self) -> 'DemodCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DemodCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
