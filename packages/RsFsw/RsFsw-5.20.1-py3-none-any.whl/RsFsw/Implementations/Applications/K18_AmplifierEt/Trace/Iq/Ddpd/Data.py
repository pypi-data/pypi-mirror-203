from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DataCls:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def get(self) -> List[float]:
		"""SCPI: TRACe:IQ:DDPD[:DATA] \n
		Snippet: value: List[float] = driver.applications.k18AmplifierEt.trace.iq.ddpd.data.get() \n
		Queries the I/Q values of the current direct DPD iteration (only for unencrypted files) . \n
			:return: iq_data: No help available"""
		response = self._core.io.query_bin_or_ascii_float_list(f'FORMAT REAL,32;TRACe:IQ:DDPD:DATA?')
		return response
