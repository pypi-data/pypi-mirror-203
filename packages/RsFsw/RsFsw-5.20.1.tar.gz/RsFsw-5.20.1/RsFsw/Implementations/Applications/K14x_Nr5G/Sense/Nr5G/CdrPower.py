from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CdrPowerCls:
	"""CdrPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cdrPower", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:NR5G:CDRPower \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.cdrPower.set(state = False) \n
		Turns the consideration of a boosting factor to calculate the constellation points in the constellation diagram on and
		off. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:NR5G:CDRPower {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:NR5G:CDRPower \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.nr5G.cdrPower.get() \n
		Turns the consideration of a boosting factor to calculate the constellation points in the constellation diagram on and
		off. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:NR5G:CDRPower?')
		return Conversions.str_to_bool(response)
