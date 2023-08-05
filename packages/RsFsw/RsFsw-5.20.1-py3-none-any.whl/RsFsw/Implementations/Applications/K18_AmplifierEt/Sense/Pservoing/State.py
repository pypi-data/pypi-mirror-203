from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:PSERvoing:STATe \n
		Snippet: driver.applications.k18AmplifierEt.sense.pservoing.state.set(state = False) \n
		Sets and queries the power servoing state. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:PSERvoing:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:PSERvoing:STATe \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.sense.pservoing.state.get() \n
		Sets and queries the power servoing state. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:PSERvoing:STATe?')
		return Conversions.str_to_bool(response)
