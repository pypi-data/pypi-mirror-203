from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PathCls:
	"""Path commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("path", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:DPD:WAVeform:PATH \n
		Snippet: value: str = driver.applications.k18AmplifierEt.fetch.dpd.waveform.path.get() \n
		Queries the path of the Polynomial DPD waveform. \n
			:return: filename: No help available"""
		response = self._core.io.query_str(f'FETCh:DPD:WAVeform:PATH?')
		return trim_str_response(response)
