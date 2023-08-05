from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerCls:
	"""Power commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def all(self):
		"""all commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	@property
	def avePower(self):
		"""avePower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_avePower'):
			from .AvePower import AvePowerCls
			self._avePower = AvePowerCls(self._core, self._cmd_group)
		return self._avePower

	@property
	def maxPower(self):
		"""maxPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maxPower'):
			from .MaxPower import MaxPowerCls
			self._maxPower = MaxPowerCls(self._core, self._cmd_group)
		return self._maxPower

	@property
	def minPower(self):
		"""minPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_minPower'):
			from .MinPower import MinPowerCls
			self._minPower = MinPowerCls(self._core, self._cmd_group)
		return self._minPower

	@property
	def pwrRipple(self):
		"""pwrRipple commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pwrRipple'):
			from .PwrRipple import PwrRippleCls
			self._pwrRipple = PwrRippleCls(self._core, self._cmd_group)
		return self._pwrRipple

	def clone(self) -> 'PowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
