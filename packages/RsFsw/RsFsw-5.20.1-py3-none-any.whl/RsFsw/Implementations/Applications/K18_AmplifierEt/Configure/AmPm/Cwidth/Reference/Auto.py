from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AutoCls:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:AMPM:CWIDth:REFerence:AUTO \n
		Snippet: driver.applications.k18AmplifierEt.configure.amPm.cwidth.reference.auto.set(state = False) \n
		Sets and queries the curve width computation refrence point mode. \n
			:param state: ON | 1 Automatic mode OFF | 0 Manual mode
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:AMPM:CWIDth:REFerence:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:AMPM:CWIDth:REFerence:AUTO \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.amPm.cwidth.reference.auto.get() \n
		Sets and queries the curve width computation refrence point mode. \n
			:return: state: ON | 1 Automatic mode OFF | 0 Manual mode"""
		response = self._core.io.query_str(f'CONFigure:AMPM:CWIDth:REFerence:AUTO?')
		return Conversions.str_to_bool(response)
