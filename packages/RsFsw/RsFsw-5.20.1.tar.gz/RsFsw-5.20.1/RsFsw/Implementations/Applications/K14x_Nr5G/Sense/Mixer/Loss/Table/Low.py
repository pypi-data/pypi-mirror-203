from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowCls:
	"""Low commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("low", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: [SENSe]:MIXer:LOSS:TABLe[:LOW] \n
		Snippet: driver.applications.k14Xnr5G.sense.mixer.loss.table.low.set(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:MIXer:LOSS:TABLe:LOW {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:MIXer:LOSS:TABLe[:LOW] \n
		Snippet: value: str = driver.applications.k14Xnr5G.sense.mixer.loss.table.low.get() \n
		No command help available \n
			:return: filename: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:LOSS:TABLe:LOW?')
		return trim_str_response(response)
