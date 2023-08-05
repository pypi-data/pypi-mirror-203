from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OevmCls:
	"""Oevm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("oevm", core, parent)

	def set(self, optimisation: enums.OptimisationOevm) -> None:
		"""SCPI: CONFigure:POWer:AUTO:OEVM \n
		Snippet: driver.applications.k91Wlan.configure.power.auto.oevm.set(optimisation = enums.OptimisationOevm.FULL) \n
		Defines whether an optional iterative search is performed to determine the required settings for minimum residual EVM. If
		enabled, the required reference level, preamplifier and, optionally, attenuation are configured. method RsFsw.
		Applications.K91_Wlan.Configure.Power.Auto.set is set to 'OFF'. \n
			:param optimisation: OFF | PAONly | FULL OFF (Default) : No optimization performed FULL An optional iterative search for minimum residual EVM is performed for the available preamplifier and attenuation settings. The optimal settings are configured. PAONly An optional iterative search for minimum residual EVM is performed, but only the available preamplifier settings are considered during the search. The optimal settings are configured.
		"""
		param = Conversions.enum_scalar_to_str(optimisation, enums.OptimisationOevm)
		self._core.io.write(f'CONFigure:POWer:AUTO:OEVM {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.OptimisationOevm:
		"""SCPI: CONFigure:POWer:AUTO:OEVM \n
		Snippet: value: enums.OptimisationOevm = driver.applications.k91Wlan.configure.power.auto.oevm.get() \n
		Defines whether an optional iterative search is performed to determine the required settings for minimum residual EVM. If
		enabled, the required reference level, preamplifier and, optionally, attenuation are configured. method RsFsw.
		Applications.K91_Wlan.Configure.Power.Auto.set is set to 'OFF'. \n
			:return: optimisation: OFF | PAONly | FULL OFF (Default) : No optimization performed FULL An optional iterative search for minimum residual EVM is performed for the available preamplifier and attenuation settings. The optimal settings are configured. PAONly An optional iterative search for minimum residual EVM is performed, but only the available preamplifier settings are considered during the search. The optimal settings are configured."""
		response = self._core.io.query_str(f'CONFigure:POWer:AUTO:OEVM?')
		return Conversions.str_to_scalar_enum(response, enums.OptimisationOevm)
