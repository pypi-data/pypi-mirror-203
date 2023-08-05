from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PortsCls:
	"""Ports commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ports", core, parent)

	def set(self, port: float) -> None:
		"""SCPI: [SENSe]:MIXer:PORTs \n
		Snippet: driver.applications.k6Pulse.sense.mixer.ports.set(port = 1.0) \n
		No command help available \n
			:param port: No help available
		"""
		param = Conversions.decimal_value_to_str(port)
		self._core.io.write(f'SENSe:MIXer:PORTs {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:PORTs \n
		Snippet: value: float = driver.applications.k6Pulse.sense.mixer.ports.get() \n
		No command help available \n
			:return: port: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:PORTs?')
		return Conversions.str_to_float(response)
