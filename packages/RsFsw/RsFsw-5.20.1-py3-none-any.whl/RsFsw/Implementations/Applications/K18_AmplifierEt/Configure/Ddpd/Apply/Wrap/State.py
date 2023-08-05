from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:DDPD:APPLy:WRAP[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.configure.ddpd.apply.wrap.state.set(state = False) \n
		Smoothes start- and tail-samples down to '0' in order to avoid phase discontinuities when the file is cyclically played
		from a signal source. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:DDPD:APPLy:WRAP:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:DDPD:APPLy:WRAP[:STATe] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.ddpd.apply.wrap.state.get() \n
		Smoothes start- and tail-samples down to '0' in order to avoid phase discontinuities when the file is cyclically played
		from a signal source. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'CONFigure:DDPD:APPLy:WRAP:STATe?')
		return Conversions.str_to_bool(response)
