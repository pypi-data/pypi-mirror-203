from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, signal_path_mode: enums.SignalPathMode, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:ATTenuation:AUTO:MODE \n
		Snippet: driver.applications.k18AmplifierEt.inputPy.attenuation.auto.mode.set(signal_path_mode = enums.SignalPathMode.LDIS, inputIx = repcap.InputIx.Default) \n
		Selects the priority for signal processing after the RF attenuation has been applied. \n
			:param signal_path_mode: No help available
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(signal_path_mode, enums.SignalPathMode)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:ATTenuation:AUTO:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.SignalPathMode:
		"""SCPI: INPut<ip>:ATTenuation:AUTO:MODE \n
		Snippet: value: enums.SignalPathMode = driver.applications.k18AmplifierEt.inputPy.attenuation.auto.mode.get(inputIx = repcap.InputIx.Default) \n
		Selects the priority for signal processing after the RF attenuation has been applied. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: signal_path_mode: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:ATTenuation:AUTO:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SignalPathMode)
