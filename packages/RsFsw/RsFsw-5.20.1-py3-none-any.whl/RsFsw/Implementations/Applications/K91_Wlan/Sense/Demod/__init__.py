from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DemodCls:
	"""Demod commands group definition. 33 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demod", core, parent)

	@property
	def cestimation(self):
		"""cestimation commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_cestimation'):
			from .Cestimation import CestimationCls
			self._cestimation = CestimationCls(self._core, self._cmd_group)
		return self._cestimation

	@property
	def data(self):
		"""data commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import DataCls
			self._data = DataCls(self._core, self._cmd_group)
		return self._data

	@property
	def txArea(self):
		"""txArea commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txArea'):
			from .TxArea import TxAreaCls
			self._txArea = TxAreaCls(self._core, self._cmd_group)
		return self._txArea

	@property
	def fft(self):
		"""fft commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fft'):
			from .Fft import FftCls
			self._fft = FftCls(self._core, self._cmd_group)
		return self._fft

	@property
	def filterPy(self):
		"""filterPy commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPyCls
			self._filterPy = FilterPyCls(self._core, self._cmd_group)
		return self._filterPy

	@property
	def formatPy(self):
		"""formatPy commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPyCls
			self._formatPy = FormatPyCls(self._core, self._cmd_group)
		return self._formatPy

	@property
	def interpolate(self):
		"""interpolate commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_interpolate'):
			from .Interpolate import InterpolateCls
			self._interpolate = InterpolateCls(self._core, self._cmd_group)
		return self._interpolate

	def clone(self) -> 'DemodCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DemodCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
