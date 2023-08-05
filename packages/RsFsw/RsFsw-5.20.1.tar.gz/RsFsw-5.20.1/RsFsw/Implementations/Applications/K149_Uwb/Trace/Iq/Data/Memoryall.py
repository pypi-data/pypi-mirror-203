from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MemoryallCls:
	"""Memoryall commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("memoryall", core, parent)

	def get(self) -> List[float]:
		"""SCPI: TRACe:IQ:DATA:MEMory \n
		Snippet: value: List[float] = driver.applications.k149Uwb.trace.iq.data.memoryall.get() \n
		No command help available \n
			:return: iq_data: No help available"""
		response = self._core.io.query_bin_or_ascii_float_list(f'FORMAT REAL,32;TRACe:IQ:DATA:MEMory?')
		return response
