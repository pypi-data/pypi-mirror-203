from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ImpedanceCls:
	"""Impedance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("impedance", core, parent)

	def set(self, impedance: int) -> None:
		"""SCPI: [SENSe]:IQ:IMPedance \n
		Snippet: driver.applications.iqAnalyzer.sense.iq.impedance.set(impedance = 1) \n
		No command help available \n
			:param impedance: No help available
		"""
		param = Conversions.decimal_value_to_str(impedance)
		self._core.io.write(f'SENSe:IQ:IMPedance {param}')

	def get(self) -> int:
		"""SCPI: [SENSe]:IQ:IMPedance \n
		Snippet: value: int = driver.applications.iqAnalyzer.sense.iq.impedance.get() \n
		No command help available \n
			:return: impedance: No help available"""
		response = self._core.io.query_str(f'SENSe:IQ:IMPedance?')
		return Conversions.str_to_int(response)
