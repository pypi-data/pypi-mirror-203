from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SrsCls:
	"""Srs commands group definition. 12 total commands, 12 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("srs", core, parent)

	@property
	def anst(self):
		"""anst commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_anst'):
			from .Anst import AnstCls
			self._anst = AnstCls(self._core, self._cmd_group)
		return self._anst

	@property
	def bhop(self):
		"""bhop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bhop'):
			from .Bhop import BhopCls
			self._bhop = BhopCls(self._core, self._cmd_group)
		return self._bhop

	@property
	def bsrs(self):
		"""bsrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bsrs'):
			from .Bsrs import BsrsCls
			self._bsrs = BsrsCls(self._core, self._cmd_group)
		return self._bsrs

	@property
	def csrs(self):
		"""csrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csrs'):
			from .Csrs import CsrsCls
			self._csrs = CsrsCls(self._core, self._cmd_group)
		return self._csrs

	@property
	def cycs(self):
		"""cycs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cycs'):
			from .Cycs import CycsCls
			self._cycs = CycsCls(self._core, self._cmd_group)
		return self._cycs

	@property
	def isrs(self):
		"""isrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_isrs'):
			from .Isrs import IsrsCls
			self._isrs = IsrsCls(self._core, self._cmd_group)
		return self._isrs

	@property
	def mupt(self):
		"""mupt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mupt'):
			from .Mupt import MuptCls
			self._mupt = MuptCls(self._core, self._cmd_group)
		return self._mupt

	@property
	def nrrc(self):
		"""nrrc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nrrc'):
			from .Nrrc import NrrcCls
			self._nrrc = NrrcCls(self._core, self._cmd_group)
		return self._nrrc

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def stat(self):
		"""stat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stat'):
			from .Stat import StatCls
			self._stat = StatCls(self._core, self._cmd_group)
		return self._stat

	@property
	def suConfig(self):
		"""suConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_suConfig'):
			from .SuConfig import SuConfigCls
			self._suConfig = SuConfigCls(self._core, self._cmd_group)
		return self._suConfig

	@property
	def trComb(self):
		"""trComb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trComb'):
			from .TrComb import TrCombCls
			self._trComb = TrCombCls(self._core, self._cmd_group)
		return self._trComb

	def clone(self) -> 'SrsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SrsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
