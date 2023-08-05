from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllocCls:
	"""Alloc commands group definition. 12 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alloc", core, parent)

	@property
	def cluster(self):
		"""cluster commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cluster'):
			from .Cluster import ClusterCls
			self._cluster = ClusterCls(self._core, self._cmd_group)
		return self._cluster

	@property
	def cont(self):
		"""cont commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cont'):
			from .Cont import ContCls
			self._cont = ContCls(self._core, self._cmd_group)
		return self._cont

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import ModulationCls
			self._modulation = ModulationCls(self._core, self._cmd_group)
		return self._modulation

	@property
	def precoding(self):
		"""precoding commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_precoding'):
			from .Precoding import PrecodingCls
			self._precoding = PrecodingCls(self._core, self._cmd_group)
		return self._precoding

	@property
	def puach(self):
		"""puach commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_puach'):
			from .Puach import PuachCls
			self._puach = PuachCls(self._core, self._cmd_group)
		return self._puach

	@property
	def pucch(self):
		"""pucch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pucch'):
			from .Pucch import PucchCls
			self._pucch = PucchCls(self._core, self._cmd_group)
		return self._pucch

	@property
	def pusch(self):
		"""pusch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pusch'):
			from .Pusch import PuschCls
			self._pusch = PuschCls(self._core, self._cmd_group)
		return self._pusch

	@property
	def rato(self):
		"""rato commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rato'):
			from .Rato import RatoCls
			self._rato = RatoCls(self._core, self._cmd_group)
		return self._rato

	def clone(self) -> 'AllocCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AllocCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
