from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqCls:
	"""Iq commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iq", core, parent)

	@property
	def tbw(self):
		"""tbw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbw'):
			from .Tbw import TbwCls
			self._tbw = TbwCls(self._core, self._cmd_group)
		return self._tbw

	@property
	def dpll(self):
		"""dpll commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpll'):
			from .Dpll import DpllCls
			self._dpll = DpllCls(self._core, self._cmd_group)
		return self._dpll

	@property
	def decimation(self):
		"""decimation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_decimation'):
			from .Decimation import DecimationCls
			self._decimation = DecimationCls(self._core, self._cmd_group)
		return self._decimation

	@property
	def online(self):
		"""online commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_online'):
			from .Online import OnlineCls
			self._online = OnlineCls(self._core, self._cmd_group)
		return self._online

	def clone(self) -> 'IqCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IqCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
