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

	def set(self, state: enums.DspreadK91) -> None:
		"""SCPI: [SENSe]:DEMod:INTerpolate:WIENer:DSPRead:STATe \n
		Snippet: driver.applications.k91Wlan.sense.demod.interpolate.wiener.dspread.state.set(state = enums.DspreadK91.MANual) \n
		Defines whether the Wiener relative delay spread is disabled or defined manually. This command is only available for
		standards IEEE 802.11ax, be and only for [SENSe:]DEMod:INTerpolateWiener. \n
			:param state: OFF | MANual OFF No delay spread is used. MAN The value is determined manually, using [SENSe:]DEMod:INTerpolate:WIENer:DSPRead.
		"""
		param = Conversions.enum_scalar_to_str(state, enums.DspreadK91)
		self._core.io.write(f'SENSe:DEMod:INTerpolate:WIENer:DSPRead:STATe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DspreadK91:
		"""SCPI: [SENSe]:DEMod:INTerpolate:WIENer:DSPRead:STATe \n
		Snippet: value: enums.DspreadK91 = driver.applications.k91Wlan.sense.demod.interpolate.wiener.dspread.state.get() \n
		Defines whether the Wiener relative delay spread is disabled or defined manually. This command is only available for
		standards IEEE 802.11ax, be and only for [SENSe:]DEMod:INTerpolateWiener. \n
			:return: state: OFF | MANual OFF No delay spread is used. MAN The value is determined manually, using [SENSe:]DEMod:INTerpolate:WIENer:DSPRead."""
		response = self._core.io.query_str(f'SENSe:DEMod:INTerpolate:WIENer:DSPRead:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.DspreadK91)
