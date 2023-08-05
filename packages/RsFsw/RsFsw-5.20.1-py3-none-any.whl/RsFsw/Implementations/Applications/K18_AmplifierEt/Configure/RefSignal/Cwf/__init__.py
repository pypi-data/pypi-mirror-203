from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CwfCls:
	"""Cwf commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cwf", core, parent)

	@property
	def dpiPower(self):
		"""dpiPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpiPower'):
			from .DpiPower import DpiPowerCls
			self._dpiPower = DpiPowerCls(self._core, self._cmd_group)
		return self._dpiPower

	@property
	def etGenerator(self):
		"""etGenerator commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_etGenerator'):
			from .EtGenerator import EtGeneratorCls
			self._etGenerator = EtGeneratorCls(self._core, self._cmd_group)
		return self._etGenerator

	@property
	def fpath(self):
		"""fpath commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fpath'):
			from .Fpath import FpathCls
			self._fpath = FpathCls(self._core, self._cmd_group)
		return self._fpath

	@property
	def ledState(self):
		"""ledState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ledState'):
			from .LedState import LedStateCls
			self._ledState = LedStateCls(self._core, self._cmd_group)
		return self._ledState

	@property
	def write(self):
		"""write commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_write'):
			from .Write import WriteCls
			self._write = WriteCls(self._core, self._cmd_group)
		return self._write

	def clone(self) -> 'CwfCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CwfCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
