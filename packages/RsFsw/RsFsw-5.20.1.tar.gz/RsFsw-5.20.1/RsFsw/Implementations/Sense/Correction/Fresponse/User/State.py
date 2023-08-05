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
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:STATe \n
		Snippet: driver.sense.correction.fresponse.user.state.set(state = False) \n
		Activates or deactivates the general usage of user-defined frequency response correction settings. Only if activated, the
		filter is calculated and applied to the results. For details, see 'Frequency response correction (R&S FSW-K544) '. TPIS
		correction is not supported if user frequency response correction is active. If you activate frequency response
		correction, TPIS correction is automatically deactivated in all channels. For details see 'Correct TPIS'. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:CORRection:FRESponse:USER:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:STATe \n
		Snippet: value: bool = driver.sense.correction.fresponse.user.state.get() \n
		Activates or deactivates the general usage of user-defined frequency response correction settings. Only if activated, the
		filter is calculated and applied to the results. For details, see 'Frequency response correction (R&S FSW-K544) '. TPIS
		correction is not supported if user frequency response correction is active. If you activate frequency response
		correction, TPIS correction is automatically deactivated in all channels. For details see 'Correct TPIS'. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:CORRection:FRESponse:USER:STATe?')
		return Conversions.str_to_bool(response)
