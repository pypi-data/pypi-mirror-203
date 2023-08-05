from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EvmCls:
	"""Evm commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("evm", core, parent)

	@property
	def ecarrier(self):
		"""ecarrier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ecarrier'):
			from .Ecarrier import EcarrierCls
			self._ecarrier = EcarrierCls(self._core, self._cmd_group)
		return self._ecarrier

	@property
	def esymbol(self):
		"""esymbol commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_esymbol'):
			from .Esymbol import EsymbolCls
			self._esymbol = EsymbolCls(self._core, self._cmd_group)
		return self._esymbol

	@property
	def evChip(self):
		"""evChip commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_evChip'):
			from .EvChip import EvChipCls
			self._evChip = EvChipCls(self._core, self._cmd_group)
		return self._evChip

	@property
	def standard(self):
		"""standard commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_standard'):
			from .Standard import StandardCls
			self._standard = StandardCls(self._core, self._cmd_group)
		return self._standard

	def clone(self) -> 'EvmCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EvmCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
