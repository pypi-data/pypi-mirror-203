from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ActiveCls:
	"""Active commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("active", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	def set(self, active_count: List[float]) -> None:
		"""SCPI: CONFigure:WLAN:RUConfig:COUNt:ACTive \n
		Snippet: driver.applications.k91Wlan.configure.wlan.ruConfig.count.active.set(active_count = [1.1, 2.2, 3.3]) \n
		Determines the RUs for which the results are evaluated. \n
			:param active_count: integer Comma-separated list of resource unit numbers from the PPDU configuration table.
		"""
		param = Conversions.list_to_csv_str(active_count)
		self._core.io.write(f'CONFigure:WLAN:RUConfig:COUNt:ACTive {param}')

	def get(self) -> List[float]:
		"""SCPI: CONFigure:WLAN:RUConfig:COUNt:ACTive \n
		Snippet: value: List[float] = driver.applications.k91Wlan.configure.wlan.ruConfig.count.active.get() \n
		Determines the RUs for which the results are evaluated. \n
			:return: active_count: integer Comma-separated list of resource unit numbers from the PPDU configuration table."""
		response = self._core.io.query_bin_or_ascii_float_list(f'CONFigure:WLAN:RUConfig:COUNt:ACTive?')
		return response

	def clone(self) -> 'ActiveCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ActiveCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
