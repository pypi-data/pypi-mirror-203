from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: TRACe:IQ:AVERage[:STATe] \n
		Snippet: driver.applications.iqAnalyzer.trace.iq.average.state.set(state = False) \n
		This command turns averaging of the I/Q data on and off. Before you can use the command you have to turn the I/Q data
		acquisition on with method RsFsw.Applications.IqAnalyzer.Trace.Iq.State.set. If averaging is on, the maximum amount of
		I/Q data that can be recorded is 512kS (524288 samples) . \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'TRACe:IQ:AVERage:STATe {param}')

	def get(self) -> bool:
		"""SCPI: TRACe:IQ:AVERage[:STATe] \n
		Snippet: value: bool = driver.applications.iqAnalyzer.trace.iq.average.state.get() \n
		This command turns averaging of the I/Q data on and off. Before you can use the command you have to turn the I/Q data
		acquisition on with method RsFsw.Applications.IqAnalyzer.Trace.Iq.State.set. If averaging is on, the maximum amount of
		I/Q data that can be recorded is 512kS (524288 samples) . \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'TRACe:IQ:AVERage:STATe?')
		return Conversions.str_to_bool(response)
