from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConstCls:
	"""Const commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("const", core, parent)

	@property
	def ccarrier(self):
		"""ccarrier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccarrier'):
			from .Ccarrier import CcarrierCls
			self._ccarrier = CcarrierCls(self._core, self._cmd_group)
		return self._ccarrier

	@property
	def csymbol(self):
		"""csymbol commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_csymbol'):
			from .Csymbol import CsymbolCls
			self._csymbol = CsymbolCls(self._core, self._cmd_group)
		return self._csymbol

	@property
	def carrier(self):
		"""carrier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import CarrierCls
			self._carrier = CarrierCls(self._core, self._cmd_group)
		return self._carrier

	def clone(self) -> 'ConstCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ConstCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
