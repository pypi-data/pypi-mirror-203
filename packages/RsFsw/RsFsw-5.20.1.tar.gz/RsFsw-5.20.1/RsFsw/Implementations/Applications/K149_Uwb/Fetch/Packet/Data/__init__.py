from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DataCls:
	"""Data commands group definition. 24 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	@property
	def a(self):
		"""a commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_a'):
			from .A import ACls
			self._a = ACls(self._core, self._cmd_group)
		return self._a

	@property
	def cburst(self):
		"""cburst commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_cburst'):
			from .Cburst import CburstCls
			self._cburst = CburstCls(self._core, self._cmd_group)
		return self._cburst

	@property
	def constraint(self):
		"""constraint commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_constraint'):
			from .Constraint import ConstraintCls
			self._constraint = ConstraintCls(self._core, self._cmd_group)
		return self._constraint

	@property
	def data(self):
		"""data commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_data'):
			from .Data import DataCls
			self._data = DataCls(self._core, self._cmd_group)
		return self._data

	@property
	def hbursts(self):
		"""hbursts commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_hbursts'):
			from .Hbursts import HburstsCls
			self._hbursts = HburstsCls(self._core, self._cmd_group)
		return self._hbursts

	@property
	def mac(self):
		"""mac commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mac'):
			from .Mac import MacCls
			self._mac = MacCls(self._core, self._cmd_group)
		return self._mac

	@property
	def payload(self):
		"""payload commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_payload'):
			from .Payload import PayloadCls
			self._payload = PayloadCls(self._core, self._cmd_group)
		return self._payload

	@property
	def ranging(self):
		"""ranging commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ranging'):
			from .Ranging import RangingCls
			self._ranging = RangingCls(self._core, self._cmd_group)
		return self._ranging

	@property
	def reserved(self):
		"""reserved commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_reserved'):
			from .Reserved import ReservedCls
			self._reserved = ReservedCls(self._core, self._cmd_group)
		return self._reserved

	@property
	def secded(self):
		"""secded commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_secded'):
			from .Secded import SecdedCls
			self._secded = SecdedCls(self._core, self._cmd_group)
		return self._secded

	def clone(self) -> 'DataCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DataCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
