from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CtpisCls:
	"""Ctpis commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ctpis", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: TRIGger[:SEQuence]:CTPis \n
		Snippet: driver.trigger.sequence.ctpis.set(state = False) \n
		The trigger event is set to the actual trigger point within the sample (TPIS) . . \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'TRIGger:SEQuence:CTPis {param}')

	def get(self) -> bool:
		"""SCPI: TRIGger[:SEQuence]:CTPis \n
		Snippet: value: bool = driver.trigger.sequence.ctpis.get() \n
		The trigger event is set to the actual trigger point within the sample (TPIS) . . \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:CTPis?')
		return Conversions.str_to_bool(response)
