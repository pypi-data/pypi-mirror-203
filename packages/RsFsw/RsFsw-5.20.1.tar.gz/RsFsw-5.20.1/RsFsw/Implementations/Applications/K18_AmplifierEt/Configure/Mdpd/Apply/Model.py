from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModelCls:
	"""Model commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("model", core, parent)

	def set(self, channel: str) -> None:
		"""SCPI: CONFigure:MDPD:APPLy:MODel \n
		Snippet: driver.applications.k18AmplifierEt.configure.mdpd.apply.model.set(channel = '1') \n
		Selects the waveform to which the model should be applied. \n
			:param channel: No help available
		"""
		param = Conversions.value_to_quoted_str(channel)
		self._core.io.write(f'CONFigure:MDPD:APPLy:MODel {param}')

	def get(self) -> str:
		"""SCPI: CONFigure:MDPD:APPLy:MODel \n
		Snippet: value: str = driver.applications.k18AmplifierEt.configure.mdpd.apply.model.get() \n
		Selects the waveform to which the model should be applied. \n
			:return: channel: No help available"""
		response = self._core.io.query_str(f'CONFigure:MDPD:APPLy:MODel?')
		return trim_str_response(response)
