from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RpaCls:
	"""Rpa commands group definition. 9 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rpa", core, parent)

	@property
	def afrequency(self):
		"""afrequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_afrequency'):
			from .Afrequency import AfrequencyCls
			self._afrequency = AfrequencyCls(self._core, self._cmd_group)
		return self._afrequency

	@property
	def kzero(self):
		"""kzero commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_kzero'):
			from .Kzero import KzeroCls
			self._kzero = KzeroCls(self._core, self._cmd_group)
		return self._kzero

	@property
	def rtcf(self):
		"""rtcf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rtcf'):
			from .Rtcf import RtcfCls
			self._rtcf = RtcfCls(self._core, self._cmd_group)
		return self._rtcf

	@property
	def tbOffset(self):
		"""tbOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbOffset'):
			from .TbOffset import TbOffsetCls
			self._tbOffset = TbOffsetCls(self._core, self._cmd_group)
		return self._tbOffset

	def clone(self) -> 'RpaCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RpaCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
