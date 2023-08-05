from ..............Internal.Core import Core
from ..............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DciSettingsCls:
	"""DciSettings commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dciSettings", core, parent)

	@property
	def fdrAssign(self):
		"""fdrAssign commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fdrAssign'):
			from .FdrAssign import FdrAssignCls
			self._fdrAssign = FdrAssignCls(self._core, self._cmd_group)
		return self._fdrAssign

	@property
	def item(self):
		"""item commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_item'):
			from .Item import ItemCls
			self._item = ItemCls(self._core, self._cmd_group)
		return self._item

	@property
	def listPy(self):
		"""listPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPyCls
			self._listPy = ListPyCls(self._core, self._cmd_group)
		return self._listPy

	@property
	def noBlock(self):
		"""noBlock commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noBlock'):
			from .NoBlock import NoBlockCls
			self._noBlock = NoBlockCls(self._core, self._cmd_group)
		return self._noBlock

	@property
	def scope(self):
		"""scope commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scope'):
			from .Scope import ScopeCls
			self._scope = ScopeCls(self._core, self._cmd_group)
		return self._scope

	@property
	def tpcCommand(self):
		"""tpcCommand commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpcCommand'):
			from .TpcCommand import TpcCommandCls
			self._tpcCommand = TpcCommandCls(self._core, self._cmd_group)
		return self._tpcCommand

	def clone(self) -> 'DciSettingsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DciSettingsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
