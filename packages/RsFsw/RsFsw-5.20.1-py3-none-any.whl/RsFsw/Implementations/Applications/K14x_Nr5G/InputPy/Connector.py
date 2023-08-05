from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConnectorCls:
	"""Connector commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connector", core, parent)

	def set(self, conn_type: enums.InputConnector) -> None:
		"""SCPI: INPut:CONNector \n
		Snippet: driver.applications.k14Xnr5G.inputPy.connector.set(conn_type = enums.InputConnector.AIQI) \n
		Determines which connector the input for the measurement is taken from. For more information, see 'Receiving Data Input
		and Providing Data Output'. If an external frontend is active, the connector is automatically set to RF. \n
			:param conn_type: RF RF input connector RFPRobe Active RF probe
		"""
		param = Conversions.enum_scalar_to_str(conn_type, enums.InputConnector)
		self._core.io.write(f'INPut:CONNector {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.InputConnector:
		"""SCPI: INPut:CONNector \n
		Snippet: value: enums.InputConnector = driver.applications.k14Xnr5G.inputPy.connector.get() \n
		Determines which connector the input for the measurement is taken from. For more information, see 'Receiving Data Input
		and Providing Data Output'. If an external frontend is active, the connector is automatically set to RF. \n
			:return: conn_type: RF RF input connector RFPRobe Active RF probe"""
		response = self._core.io.query_str(f'INPut:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.InputConnector)
