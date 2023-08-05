from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CaptureCls:
	"""Capture commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("capture", core, parent)

	@property
	def default(self):
		"""default commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_default'):
			from .Default import DefaultCls
			self._default = DefaultCls(self._core, self._cmd_group)
		return self._default

	@property
	def fset(self):
		"""fset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fset'):
			from .Fset import FsetCls
			self._fset = FsetCls(self._core, self._cmd_group)
		return self._fset

	@property
	def length(self):
		"""length commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_length'):
			from .Length import LengthCls
			self._length = LengthCls(self._core, self._cmd_group)
		return self._length

	@property
	def oversampling(self):
		"""oversampling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_oversampling'):
			from .Oversampling import OversamplingCls
			self._oversampling = OversamplingCls(self._core, self._cmd_group)
		return self._oversampling

	@property
	def preset(self):
		"""preset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_preset'):
			from .Preset import PresetCls
			self._preset = PresetCls(self._core, self._cmd_group)
		return self._preset

	def clone(self) -> 'CaptureCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CaptureCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
