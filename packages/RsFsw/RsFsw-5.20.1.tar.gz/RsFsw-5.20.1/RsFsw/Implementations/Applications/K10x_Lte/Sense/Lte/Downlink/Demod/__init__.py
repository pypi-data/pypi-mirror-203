from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DemodCls:
	"""Demod commands group definition. 9 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demod", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import AutoCls
			self._auto = AutoCls(self._core, self._cmd_group)
		return self._auto

	@property
	def bestimation(self):
		"""bestimation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bestimation'):
			from .Bestimation import BestimationCls
			self._bestimation = BestimationCls(self._core, self._cmd_group)
		return self._bestimation

	@property
	def cbScrambling(self):
		"""cbScrambling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbScrambling'):
			from .CbScrambling import CbScramblingCls
			self._cbScrambling = CbScramblingCls(self._core, self._cmd_group)
		return self._cbScrambling

	@property
	def cestimation(self):
		"""cestimation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cestimation'):
			from .Cestimation import CestimationCls
			self._cestimation = CestimationCls(self._core, self._cmd_group)
		return self._cestimation

	@property
	def daChannels(self):
		"""daChannels commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_daChannels'):
			from .DaChannels import DaChannelsCls
			self._daChannels = DaChannelsCls(self._core, self._cmd_group)
		return self._daChannels

	@property
	def evmCalc(self):
		"""evmCalc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_evmCalc'):
			from .EvmCalc import EvmCalcCls
			self._evmCalc = EvmCalcCls(self._core, self._cmd_group)
		return self._evmCalc

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
	def siSync(self):
		"""siSync commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_siSync'):
			from .SiSync import SiSyncCls
			self._siSync = SiSyncCls(self._core, self._cmd_group)
		return self._siSync

	def clone(self) -> 'DemodCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DemodCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
