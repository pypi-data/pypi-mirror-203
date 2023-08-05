from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WriteCls:
	"""Write commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("write", core, parent)

	def set(self, command: str) -> None:
		"""SCPI: CONFigure:GENerator:RELay:WRITe \n
		Snippet: driver.applications.k18AmplifierEt.configure.generator.relay.write.set(command = '1') \n
		Provides functionality to configure the signal generator directly through the R&S FSW-K18 application. It resends the
		string parameter as a SCPI command to the connected signal generator. If the command contains a '?', use method RsFsw.
		Configure.Generator.Relay.Read.get_ to read the answer. \n
			:param command: No help available
		"""
		param = Conversions.value_to_quoted_str(command)
		self._core.io.write_with_opc(f'CONFigure:GENerator:RELay:WRITe {param}')
