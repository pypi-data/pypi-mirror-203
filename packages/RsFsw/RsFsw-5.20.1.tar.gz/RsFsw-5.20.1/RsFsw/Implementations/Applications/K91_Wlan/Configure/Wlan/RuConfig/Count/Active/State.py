from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: enums.AllOrOne) -> None:
		"""SCPI: CONFigure:WLAN:RUConfig:COUNt:ACTive:STATe \n
		Snippet: driver.applications.k91Wlan.configure.wlan.ruConfig.count.active.state.set(state = enums.AllOrOne.ALL) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.enum_scalar_to_str(state, enums.AllOrOne)
		self._core.io.write(f'CONFigure:WLAN:RUConfig:COUNt:ACTive:STATe {param}')
