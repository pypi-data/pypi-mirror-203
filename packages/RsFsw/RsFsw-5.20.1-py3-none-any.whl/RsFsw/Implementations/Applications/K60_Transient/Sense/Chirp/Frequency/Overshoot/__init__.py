from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OvershootCls:
	"""Overshoot commands group definition. 5 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("overshoot", core, parent)

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_average'):
			from .Average import AverageCls
			self._average = AverageCls(self._core, self._cmd_group)
		return self._average

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maximum'):
			from .Maximum import MaximumCls
			self._maximum = MaximumCls(self._core, self._cmd_group)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_minimum'):
			from .Minimum import MinimumCls
			self._minimum = MinimumCls(self._core, self._cmd_group)
		return self._minimum

	@property
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_standardDev'):
			from .StandardDev import StandardDevCls
			self._standardDev = StandardDevCls(self._core, self._cmd_group)
		return self._standardDev

	def get(self, query_range: enums.SelectionRange) -> float:
		"""SCPI: [SENSe]:CHIRp:FREQuency:OVERshoot \n
		Snippet: value: float = driver.applications.k60Transient.sense.chirp.frequency.overshoot.get(query_range = enums.SelectionRange.ALL) \n
		Queries chirp frequency overshoot from the result table. \n
			:param query_range: SELected | CURRent | ALL
			:return: result: numeric value"""
		param = Conversions.enum_scalar_to_str(query_range, enums.SelectionRange)
		response = self._core.io.query_str(f'SENSe:CHIRp:FREQuency:OVERshoot? {param}')
		return Conversions.str_to_float(response)

	def clone(self) -> 'OvershootCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OvershootCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
