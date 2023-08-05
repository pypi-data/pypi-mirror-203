from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:MACCuracy:SRERror:CURRent[:RESult] \n
		Snippet: value: float = driver.applications.k18AmplifierEt.fetch.maccuracy.srError.current.result.get() \n
		Queries the absolute phase value between reference signal and measured signal. Note that the absolute phase is not
		relevant for R&S FSW-K18 measurements. However, it can be used to track the absolute phase stability between generator
		and analyzer (including their local oscillators) . \n
			:return: sample_rate_error: Numeric value Unit: radian"""
		response = self._core.io.query_str(f'FETCh:MACCuracy:SRERror:CURRent:RESult?')
		return Conversions.str_to_float(response)
