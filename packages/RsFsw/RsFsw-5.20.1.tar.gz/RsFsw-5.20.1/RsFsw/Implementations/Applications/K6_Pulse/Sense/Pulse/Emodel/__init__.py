from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EmodelCls:
	"""Emodel commands group definition. 126 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("emodel", core, parent)

	@property
	def riseBasePoint(self):
		"""riseBasePoint commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_riseBasePoint'):
			from .RiseBasePoint import RiseBasePointCls
			self._riseBasePoint = RiseBasePointCls(self._core, self._cmd_group)
		return self._riseBasePoint

	@property
	def riseLowPoint(self):
		"""riseLowPoint commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_riseLowPoint'):
			from .RiseLowPoint import RiseLowPointCls
			self._riseLowPoint = RiseLowPointCls(self._core, self._cmd_group)
		return self._riseLowPoint

	@property
	def riseMidPoint(self):
		"""riseMidPoint commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_riseMidPoint'):
			from .RiseMidPoint import RiseMidPointCls
			self._riseMidPoint = RiseMidPointCls(self._core, self._cmd_group)
		return self._riseMidPoint

	@property
	def riseHighPoint(self):
		"""riseHighPoint commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_riseHighPoint'):
			from .RiseHighPoint import RiseHighPointCls
			self._riseHighPoint = RiseHighPointCls(self._core, self._cmd_group)
		return self._riseHighPoint

	@property
	def riseTopPoint(self):
		"""riseTopPoint commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_riseTopPoint'):
			from .RiseTopPoint import RiseTopPointCls
			self._riseTopPoint = RiseTopPointCls(self._core, self._cmd_group)
		return self._riseTopPoint

	@property
	def fallBasePoint(self):
		"""fallBasePoint commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fallBasePoint'):
			from .FallBasePoint import FallBasePointCls
			self._fallBasePoint = FallBasePointCls(self._core, self._cmd_group)
		return self._fallBasePoint

	@property
	def fallLowPoint(self):
		"""fallLowPoint commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fallLowPoint'):
			from .FallLowPoint import FallLowPointCls
			self._fallLowPoint = FallLowPointCls(self._core, self._cmd_group)
		return self._fallLowPoint

	@property
	def fallMidPoint(self):
		"""fallMidPoint commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fallMidPoint'):
			from .FallMidPoint import FallMidPointCls
			self._fallMidPoint = FallMidPointCls(self._core, self._cmd_group)
		return self._fallMidPoint

	@property
	def fallHighPoint(self):
		"""fallHighPoint commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fallHighPoint'):
			from .FallHighPoint import FallHighPointCls
			self._fallHighPoint = FallHighPointCls(self._core, self._cmd_group)
		return self._fallHighPoint

	@property
	def fallTopPoint(self):
		"""fallTopPoint commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fallTopPoint'):
			from .FallTopPoint import FallTopPointCls
			self._fallTopPoint = FallTopPointCls(self._core, self._cmd_group)
		return self._fallTopPoint

	def clone(self) -> 'EmodelCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EmodelCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
