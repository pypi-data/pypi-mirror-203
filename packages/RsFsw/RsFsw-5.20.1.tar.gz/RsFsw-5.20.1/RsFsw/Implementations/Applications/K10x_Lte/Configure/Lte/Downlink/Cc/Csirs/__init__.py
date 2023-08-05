from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CsirsCls:
	"""Csirs commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csirs", core, parent)

	@property
	def ci(self):
		"""ci commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ci'):
			from .Ci import CiCls
			self._ci = CiCls(self._core, self._cmd_group)
		return self._ci

	@property
	def nap(self):
		"""nap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nap'):
			from .Nap import NapCls
			self._nap = NapCls(self._core, self._cmd_group)
		return self._nap

	@property
	def opdsch(self):
		"""opdsch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_opdsch'):
			from .Opdsch import OpdschCls
			self._opdsch = OpdschCls(self._core, self._cmd_group)
		return self._opdsch

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def sci(self):
		"""sci commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sci'):
			from .Sci import SciCls
			self._sci = SciCls(self._core, self._cmd_group)
		return self._sci

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'CsirsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CsirsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
