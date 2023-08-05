from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChrDetectionCls:
	"""ChrDetection commands group definition. 76 total commands, 14 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("chrDetection", core, parent)

	@property
	def compensation(self):
		"""compensation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_compensation'):
			from .Compensation import CompensationCls
			self._compensation = CompensationCls(self._core, self._cmd_group)
		return self._compensation

	@property
	def fmTolerance(self):
		"""fmTolerance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fmTolerance'):
			from .FmTolerance import FmToleranceCls
			self._fmTolerance = FmToleranceCls(self._core, self._cmd_group)
		return self._fmTolerance

	@property
	def pmTolerance(self):
		"""pmTolerance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmTolerance'):
			from .PmTolerance import PmToleranceCls
			self._pmTolerance = PmToleranceCls(self._core, self._cmd_group)
		return self._pmTolerance

	@property
	def frequency(self):
		"""frequency commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def fdeviation(self):
		"""fdeviation commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_fdeviation'):
			from .Fdeviation import FdeviationCls
			self._fdeviation = FdeviationCls(self._core, self._cmd_group)
		return self._fdeviation

	@property
	def pdeviation(self):
		"""pdeviation commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdeviation'):
			from .Pdeviation import PdeviationCls
			self._pdeviation = PdeviationCls(self._core, self._cmd_group)
		return self._pdeviation

	@property
	def pnoise(self):
		"""pnoise commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_pnoise'):
			from .Pnoise import PnoiseCls
			self._pnoise = PnoiseCls(self._core, self._cmd_group)
		return self._pnoise

	@property
	def power(self):
		"""power commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def length(self):
		"""length commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_length'):
			from .Length import LengthCls
			self._length = LengthCls(self._core, self._cmd_group)
		return self._length

	@property
	def states(self):
		"""states commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_states'):
			from .States import StatesCls
			self._states = StatesCls(self._core, self._cmd_group)
		return self._states

	@property
	def detection(self):
		"""detection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_detection'):
			from .Detection import DetectionCls
			self._detection = DetectionCls(self._core, self._cmd_group)
		return self._detection

	@property
	def selected(self):
		"""selected commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_selected'):
			from .Selected import SelectedCls
			self._selected = SelectedCls(self._core, self._cmd_group)
		return self._selected

	@property
	def total(self):
		"""total commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_total'):
			from .Total import TotalCls
			self._total = TotalCls(self._core, self._cmd_group)
		return self._total

	@property
	def table(self):
		"""table commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_table'):
			from .Table import TableCls
			self._table = TableCls(self._core, self._cmd_group)
		return self._table

	def clone(self) -> 'ChrDetectionCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ChrDetectionCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
