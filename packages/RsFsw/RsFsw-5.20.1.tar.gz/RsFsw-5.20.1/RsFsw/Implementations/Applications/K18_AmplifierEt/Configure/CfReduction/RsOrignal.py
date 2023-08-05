from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsOrignalCls:
	"""RsOrignal commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rsOrignal", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:CFReduction:RSORignal \n
		Snippet: driver.applications.k18AmplifierEt.configure.cfReduction.rsOrignal.set(state = False) \n
		Switches the EVM reference signal. \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:CFReduction:RSORignal {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:CFReduction:RSORignal \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.cfReduction.rsOrignal.get() \n
		Switches the EVM reference signal. \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'CONFigure:CFReduction:RSORignal?')
		return Conversions.str_to_bool(response)
