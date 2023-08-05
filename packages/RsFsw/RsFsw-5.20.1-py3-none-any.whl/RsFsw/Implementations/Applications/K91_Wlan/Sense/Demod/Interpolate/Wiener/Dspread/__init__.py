from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DspreadCls:
	"""Dspread commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dspread", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	def set(self, value: float) -> None:
		"""SCPI: [SENSe]:DEMod:INTerpolate:WIENer:DSPRead \n
		Snippet: driver.applications.k91Wlan.sense.demod.interpolate.wiener.dspread.set(value = 1.0) \n
		Defines the value relative to the DFT period that is used for the Wiener filter design. Decrease this setting to finetune
		the EVM result if there is negligible delay spread, for example for a wired connection. This setting is only available
		for [SENSe:]DEMod:INTerpolate:WIENer:DSPRead:STATe OFF. \n
			:param value: Range: 0.0001 to 0.5
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'SENSe:DEMod:INTerpolate:WIENer:DSPRead {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DEMod:INTerpolate:WIENer:DSPRead \n
		Snippet: value: float = driver.applications.k91Wlan.sense.demod.interpolate.wiener.dspread.get() \n
		Defines the value relative to the DFT period that is used for the Wiener filter design. Decrease this setting to finetune
		the EVM result if there is negligible delay spread, for example for a wired connection. This setting is only available
		for [SENSe:]DEMod:INTerpolate:WIENer:DSPRead:STATe OFF. \n
			:return: value: Range: 0.0001 to 0.5"""
		response = self._core.io.query_str(f'SENSe:DEMod:INTerpolate:WIENer:DSPRead?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'DspreadCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DspreadCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
