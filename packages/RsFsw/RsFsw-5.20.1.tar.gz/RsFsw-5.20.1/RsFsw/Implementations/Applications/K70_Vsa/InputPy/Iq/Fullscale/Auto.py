from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AutoCls:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:IQ:FULLscale:AUTO \n
		Snippet: driver.applications.k70Vsa.inputPy.iq.fullscale.auto.set(state = False, inputIx = repcap.InputIx.Default) \n
		This command defines whether the full scale level (i.e. the maximum input power on the Baseband Input connector) is
		defined automatically according to the reference level, or manually. \n
			:param state: ON | 1 Automatic definition OFF | 0 Manual definition according to method RsFsw.Applications.K6_Pulse.InputPy.Iq.Fullscale.Level.set
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.bool_to_str(state)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:IQ:FULLscale:AUTO {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> bool:
		"""SCPI: INPut<ip>:IQ:FULLscale:AUTO \n
		Snippet: value: bool = driver.applications.k70Vsa.inputPy.iq.fullscale.auto.get(inputIx = repcap.InputIx.Default) \n
		This command defines whether the full scale level (i.e. the maximum input power on the Baseband Input connector) is
		defined automatically according to the reference level, or manually. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: state: ON | 1 Automatic definition OFF | 0 Manual definition according to method RsFsw.Applications.K6_Pulse.InputPy.Iq.Fullscale.Level.set"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IQ:FULLscale:AUTO?')
		return Conversions.str_to_bool(response)
