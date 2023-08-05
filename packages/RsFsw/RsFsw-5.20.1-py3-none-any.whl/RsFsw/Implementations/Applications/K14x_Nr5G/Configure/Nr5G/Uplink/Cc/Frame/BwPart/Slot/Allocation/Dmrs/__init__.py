from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DmrsCls:
	"""Dmrs commands group definition. 14 total commands, 13 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dmrs", core, parent)

	@property
	def ap(self):
		"""ap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ap'):
			from .Ap import ApCls
			self._ap = ApCls(self._core, self._cmd_group)
		return self._ap

	@property
	def cgwd(self):
		"""cgwd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cgwd'):
			from .Cgwd import CgwdCls
			self._cgwd = CgwdCls(self._core, self._cmd_group)
		return self._cgwd

	@property
	def ctype(self):
		"""ctype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ctype'):
			from .Ctype import CtypeCls
			self._ctype = CtypeCls(self._core, self._cmd_group)
		return self._ctype

	@property
	def msymbol(self):
		"""msymbol commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_msymbol'):
			from .Msymbol import MsymbolCls
			self._msymbol = MsymbolCls(self._core, self._cmd_group)
		return self._msymbol

	@property
	def mtype(self):
		"""mtype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mtype'):
			from .Mtype import MtypeCls
			self._mtype = MtypeCls(self._core, self._cmd_group)
		return self._mtype

	@property
	def nid(self):
		"""nid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nid'):
			from .Nid import NidCls
			self._nid = NidCls(self._core, self._cmd_group)
		return self._nid

	@property
	def nirId(self):
		"""nirId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nirId'):
			from .NirId import NirIdCls
			self._nirId = NirIdCls(self._core, self._cmd_group)
		return self._nirId

	@property
	def nirs(self):
		"""nirs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nirs'):
			from .Nirs import NirsCls
			self._nirs = NirsCls(self._core, self._cmd_group)
		return self._nirs

	@property
	def nscid(self):
		"""nscid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nscid'):
			from .Nscid import NscidCls
			self._nscid = NscidCls(self._core, self._cmd_group)
		return self._nscid

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def rst(self):
		"""rst commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rst'):
			from .Rst import RstCls
			self._rst = RstCls(self._core, self._cmd_group)
		return self._rst

	@property
	def sgeneration(self):
		"""sgeneration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sgeneration'):
			from .Sgeneration import SgenerationCls
			self._sgeneration = SgenerationCls(self._core, self._cmd_group)
		return self._sgeneration

	@property
	def tapos(self):
		"""tapos commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tapos'):
			from .Tapos import TaposCls
			self._tapos = TaposCls(self._core, self._cmd_group)
		return self._tapos

	def clone(self) -> 'DmrsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DmrsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
