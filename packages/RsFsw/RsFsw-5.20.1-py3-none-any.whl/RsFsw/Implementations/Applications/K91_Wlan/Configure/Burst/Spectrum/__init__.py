from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpectrumCls:
	"""Spectrum commands group definition. 8 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spectrum", core, parent)

	@property
	def acpr(self):
		"""acpr commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_acpr'):
			from .Acpr import AcprCls
			self._acpr = AcprCls(self._core, self._cmd_group)
		return self._acpr

	@property
	def fft(self):
		"""fft commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fft'):
			from .Fft import FftCls
			self._fft = FftCls(self._core, self._cmd_group)
		return self._fft

	@property
	def flatness(self):
		"""flatness commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_flatness'):
			from .Flatness import FlatnessCls
			self._flatness = FlatnessCls(self._core, self._cmd_group)
		return self._flatness

	@property
	def mask(self):
		"""mask commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_mask'):
			from .Mask import MaskCls
			self._mask = MaskCls(self._core, self._cmd_group)
		return self._mask

	@property
	def obwidth(self):
		"""obwidth commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_obwidth'):
			from .Obwidth import ObwidthCls
			self._obwidth = ObwidthCls(self._core, self._cmd_group)
		return self._obwidth

	def clone(self) -> 'SpectrumCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SpectrumCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
