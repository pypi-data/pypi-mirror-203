from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConnectorCls:
	"""Connector commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connector", core, parent)

	def set(self, conn_type: enums.InputConnector, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:CONNector \n
		Snippet: driver.applications.k10Xlte.inputPy.connector.set(conn_type = enums.InputConnector.AIQI, inputIx = repcap.InputIx.Default) \n
		Determines which connector the input for the measurement is taken from. For more information, see 'Receiving Data Input
		and Providing Data Output'. If an external frontend is active, the connector is automatically set to RF. \n
			:param conn_type: RF RF input connector RFPRobe Active RF probe
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(conn_type, enums.InputConnector)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:CONNector {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.InputConnector:
		"""SCPI: INPut<ip>:CONNector \n
		Snippet: value: enums.InputConnector = driver.applications.k10Xlte.inputPy.connector.get(inputIx = repcap.InputIx.Default) \n
		Determines which connector the input for the measurement is taken from. For more information, see 'Receiving Data Input
		and Providing Data Output'. If an external frontend is active, the connector is automatically set to RF. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: conn_type: RF RF input connector RFPRobe Active RF probe"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.InputConnector)
