from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IfPowerCls:
	"""IfPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ifPower", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:LEVel:IFPower \n
		Snippet: driver.applications.k14Xnr5G.trigger.sequence.level.ifPower.set(level = 1.0) \n
		This command defines the power level at the third intermediate frequency that must be exceeded to cause a trigger event.
		Note that any RF attenuation or preamplification is considered when the trigger level is analyzed.
		If defined, a reference level offset is also considered. \n
			:param level: numeric value For details on available trigger levels and trigger bandwidths see the data sheet. Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'TRIGger:SEQuence:LEVel:IFPower {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:LEVel:IFPower \n
		Snippet: value: float = driver.applications.k14Xnr5G.trigger.sequence.level.ifPower.get() \n
		This command defines the power level at the third intermediate frequency that must be exceeded to cause a trigger event.
		Note that any RF attenuation or preamplification is considered when the trigger level is analyzed.
		If defined, a reference level offset is also considered. \n
			:return: level: numeric value For details on available trigger levels and trigger bandwidths see the data sheet. Unit: dBm"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:LEVel:IFPower?')
		return Conversions.str_to_float(response)
