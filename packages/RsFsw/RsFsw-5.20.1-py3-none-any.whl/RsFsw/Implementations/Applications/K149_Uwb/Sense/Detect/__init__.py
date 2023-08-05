from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DetectCls:
	"""Detect commands group definition. 7 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("detect", core, parent)

	@property
	def burst(self):
		"""burst commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_burst'):
			from .Burst import BurstCls
			self._burst = BurstCls(self._core, self._cmd_group)
		return self._burst

	@property
	def default(self):
		"""default commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_default'):
			from .Default import DefaultCls
			self._default = DefaultCls(self._core, self._cmd_group)
		return self._default

	@property
	def evaluation(self):
		"""evaluation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_evaluation'):
			from .Evaluation import EvaluationCls
			self._evaluation = EvaluationCls(self._core, self._cmd_group)
		return self._evaluation

	@property
	def off(self):
		"""off commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_off'):
			from .Off import OffCls
			self._off = OffCls(self._core, self._cmd_group)
		return self._off

	@property
	def reference(self):
		"""reference commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reference'):
			from .Reference import ReferenceCls
			self._reference = ReferenceCls(self._core, self._cmd_group)
		return self._reference

	@property
	def threshold(self):
		"""threshold commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_threshold'):
			from .Threshold import ThresholdCls
			self._threshold = ThresholdCls(self._core, self._cmd_group)
		return self._threshold

	def clone(self) -> 'DetectCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DetectCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
