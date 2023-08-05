from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PolynomialCls:
	"""Polynomial commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("polynomial", core, parent)

	def set(self, order: str) -> None:
		"""SCPI: CONFigure:HAMMerstein:ORDer:POLYnomial \n
		Snippet: driver.applications.k18AmplifierEt.configure.hammerstein.order.polynomial.set(order = '1') \n
		Sets the polynomial order for the Hammerstein model as a string. \n
			:param order: No help available
		"""
		param = Conversions.value_to_quoted_str(order)
		self._core.io.write(f'CONFigure:HAMMerstein:ORDer:POLYnomial {param}')

	def get(self) -> str:
		"""SCPI: CONFigure:HAMMerstein:ORDer:POLYnomial \n
		Snippet: value: str = driver.applications.k18AmplifierEt.configure.hammerstein.order.polynomial.get() \n
		Sets the polynomial order for the Hammerstein model as a string. \n
			:return: order: No help available"""
		response = self._core.io.query_str(f'CONFigure:HAMMerstein:ORDer:POLYnomial?')
		return trim_str_response(response)
