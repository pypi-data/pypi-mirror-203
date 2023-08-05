from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AutoCls:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:SANalyzer:ATTenuation:AUTO \n
		Snippet: driver.inputPy.sanalyzer.attenuation.auto.set(state = False, inputIx = repcap.InputIx.Default) \n
		Enables or disables automatic configuration of attenuation at the analyzer input for an active external frontend.
		By default, the attenuation settings are applied at the input of the external frontend, see method RsFsw.Applications.
		K10x_Lte.InputPy.Attenuation.Auto.set and method RsFsw.Applications.K10x_Lte.InputPy.Attenuation.set. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Auto mode for analyzer attenuation is disabled. Allows you to configure attenuation at the analyzer using method RsFsw.InputPy.Sanalyzer.Attenuation.set. ON | 1 Auto mode for analyzer attenuation is enabled. No attenuation is configured at the analyzer.
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.bool_to_str(state)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:SANalyzer:ATTenuation:AUTO {param}')
