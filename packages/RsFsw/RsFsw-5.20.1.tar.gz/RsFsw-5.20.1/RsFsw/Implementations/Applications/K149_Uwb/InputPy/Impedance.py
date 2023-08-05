from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ImpedanceCls:
	"""Impedance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("impedance", core, parent)

	def set(self, impedance: int) -> None:
		"""SCPI: INPut:IMPedance \n
		Snippet: driver.applications.k149Uwb.inputPy.impedance.set(impedance = 1) \n
		This command selects the nominal input impedance of the RF input. In some applications, only 50 Ω are supported. \n
			:param impedance: 50 | 75 Unit: OHM
		"""
		param = Conversions.decimal_value_to_str(impedance)
		self._core.io.write_with_opc(f'INPut:IMPedance {param}')

	def get(self) -> int:
		"""SCPI: INPut:IMPedance \n
		Snippet: value: int = driver.applications.k149Uwb.inputPy.impedance.get() \n
		This command selects the nominal input impedance of the RF input. In some applications, only 50 Ω are supported. \n
			:return: impedance: 50 | 75 Unit: OHM"""
		response = self._core.io.query_str_with_opc(f'INPut:IMPedance?')
		return Conversions.str_to_int(response)
