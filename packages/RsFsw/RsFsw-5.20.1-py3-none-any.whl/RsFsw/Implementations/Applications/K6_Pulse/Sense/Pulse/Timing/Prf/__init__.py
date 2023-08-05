from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrfCls:
	"""Prf commands group definition. 7 total commands, 6 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prf", core, parent)

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_average'):
			from .Average import AverageCls
			self._average = AverageCls(self._core, self._cmd_group)
		return self._average

	@property
	def count(self):
		"""count commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import CountCls
			self._count = CountCls(self._core, self._cmd_group)
		return self._count

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
	def limit(self):
		"""limit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import LimitCls
			self._limit = LimitCls(self._core, self._cmd_group)
		return self._limit

	@property
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_standardDev'):
			from .StandardDev import StandardDevCls
			self._standardDev = StandardDevCls(self._core, self._cmd_group)
		return self._standardDev

	def get(self, query_range: enums.SelectionRange) -> str:
		"""SCPI: [SENSe]:PULSe:TIMing:PRF \n
		Snippet: value: str = driver.applications.k6Pulse.sense.pulse.timing.prf.get(query_range = enums.SelectionRange.ALL) \n
		Returns the Pulse Repetition Frequency (Hz) for the specified pulse(s) . \n
			:param query_range: SELected | CURRent | ALL SELected Currently selected pulse CURRent Detected pulses in the current capture buffer ALL All detected pulses in the entire measurement.
			:return: result: char_data"""
		param = Conversions.enum_scalar_to_str(query_range, enums.SelectionRange)
		response = self._core.io.query_str(f'SENSe:PULSe:TIMing:PRF? {param}')
		return trim_str_response(response)

	def clone(self) -> 'PrfCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PrfCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
