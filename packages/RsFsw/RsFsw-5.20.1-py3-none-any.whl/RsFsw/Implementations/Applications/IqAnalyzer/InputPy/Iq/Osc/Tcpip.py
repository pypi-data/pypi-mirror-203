from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TcpipCls:
	"""Tcpip commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tcpip", core, parent)

	def get(self, inputIx=repcap.InputIx.Default) -> str:
		"""SCPI: INPut<ip>:IQ:OSC:TCPip \n
		Snippet: value: str = driver.applications.iqAnalyzer.inputPy.iq.osc.tcpip.get(inputIx = repcap.InputIx.Default) \n
		Defines the TCPIP address or computer name of the oscilloscope connected to the R&S FSW via LAN. Note: The IP address is
		maintained after a [PRESET], and is transferred between applications. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: ip_address: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IQ:OSC:TCPip?')
		return trim_str_response(response)
