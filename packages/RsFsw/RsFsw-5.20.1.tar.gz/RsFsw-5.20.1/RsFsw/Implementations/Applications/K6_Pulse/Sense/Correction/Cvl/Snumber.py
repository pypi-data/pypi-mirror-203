from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SnumberCls:
	"""Snumber commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("snumber", core, parent)

	def set(self, serial_number: str) -> None:
		"""SCPI: [SENSe]:CORRection:CVL:SNUMber \n
		Snippet: driver.applications.k6Pulse.sense.correction.cvl.snumber.set(serial_number = '1') \n
		No command help available \n
			:param serial_number: No help available
		"""
		param = Conversions.value_to_quoted_str(serial_number)
		self._core.io.write(f'SENSe:CORRection:CVL:SNUMber {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:CORRection:CVL:SNUMber \n
		Snippet: value: str = driver.applications.k6Pulse.sense.correction.cvl.snumber.get() \n
		No command help available \n
			:return: serial_number: No help available"""
		response = self._core.io.query_str(f'SENSe:CORRection:CVL:SNUMber?')
		return trim_str_response(response)
