from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DrsCls:
	"""Drs commands group definition. 9 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("drs", core, parent)

	@property
	def aocc(self):
		"""aocc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aocc'):
			from .Aocc import AoccCls
			self._aocc = AoccCls(self._core, self._cmd_group)
		return self._aocc

	@property
	def dsShift(self):
		"""dsShift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dsShift'):
			from .DsShift import DsShiftCls
			self._dsShift = DsShiftCls(self._core, self._cmd_group)
		return self._dsShift

	@property
	def enpr(self):
		"""enpr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enpr'):
			from .Enpr import EnprCls
			self._enpr = EnprCls(self._core, self._cmd_group)
		return self._enpr

	@property
	def grpHopping(self):
		"""grpHopping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_grpHopping'):
			from .GrpHopping import GrpHoppingCls
			self._grpHopping = GrpHoppingCls(self._core, self._cmd_group)
		return self._grpHopping

	@property
	def ndmrs(self):
		"""ndmrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ndmrs'):
			from .Ndmrs import NdmrsCls
			self._ndmrs = NdmrsCls(self._core, self._cmd_group)
		return self._ndmrs

	@property
	def plid(self):
		"""plid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plid'):
			from .Plid import PlidCls
			self._plid = PlidCls(self._core, self._cmd_group)
		return self._plid

	@property
	def pucch(self):
		"""pucch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pucch'):
			from .Pucch import PucchCls
			self._pucch = PucchCls(self._core, self._cmd_group)
		return self._pucch

	@property
	def pusch(self):
		"""pusch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pusch'):
			from .Pusch import PuschCls
			self._pusch = PuschCls(self._core, self._cmd_group)
		return self._pusch

	@property
	def seqHopping(self):
		"""seqHopping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_seqHopping'):
			from .SeqHopping import SeqHoppingCls
			self._seqHopping = SeqHoppingCls(self._core, self._cmd_group)
		return self._seqHopping

	def clone(self) -> 'DrsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DrsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
