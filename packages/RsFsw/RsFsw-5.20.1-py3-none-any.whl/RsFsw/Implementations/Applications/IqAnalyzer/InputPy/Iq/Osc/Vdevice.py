from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VdeviceCls:
	"""Vdevice commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vdevice", core, parent)

	def get(self, inputIx=repcap.InputIx.Default) -> bool:
		"""SCPI: INPut<ip>:IQ:OSC:VDEVice \n
		Snippet: value: bool = driver.applications.iqAnalyzer.inputPy.iq.osc.vdevice.get(inputIx = repcap.InputIx.Default) \n
		Queries whether the connected instrument is supported for Oscilloscope Baseband Input. For details see the data sheet. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: state: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IQ:OSC:VDEVice?')
		return Conversions.str_to_bool(response)
