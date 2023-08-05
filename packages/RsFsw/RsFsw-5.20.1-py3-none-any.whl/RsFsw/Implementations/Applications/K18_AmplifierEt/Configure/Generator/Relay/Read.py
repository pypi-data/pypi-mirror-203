from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReadCls:
	"""Read commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("read", core, parent)

	def get(self) -> str:
		"""SCPI: CONFigure:GENerator:RELay:READ \n
		Snippet: value: str = driver.applications.k18AmplifierEt.configure.generator.relay.read.get() \n
		Provides functionality to read the answer if the command that was sent to the signal generator using method RsFsw.
		Configure.Generator.Relay.Write.set contained a '?'. \n
			:return: response: No help available"""
		response = self._core.io.query_str_with_opc(f'CONFigure:GENerator:RELay:READ?')
		return trim_str_response(response)
