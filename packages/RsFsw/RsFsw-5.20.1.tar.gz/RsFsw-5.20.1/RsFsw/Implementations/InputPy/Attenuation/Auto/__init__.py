from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AutoCls:
	"""Auto commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import ModeCls
			self._mode = ModeCls(self._core, self._cmd_group)
		return self._mode

	def set(self, state: bool) -> None:
		"""SCPI: INPut:ATTenuation:AUTO \n
		Snippet: driver.inputPy.attenuation.auto.set(state = False) \n
		This command couples or decouples the attenuation to the reference level. Thus, when the reference level is changed, the
		R&S FSW determines the signal level for optimal internal data processing and sets the required attenuation accordingly.
		If an external frontend is active (see [SENSe:]EFRontend<fe>[:STATe]) , you can configure the attenuation of the external
		frontend and the analyzer separately. See also method RsFsw.InputPy.Sanalyzer.Attenuation.Auto.set and method RsFsw.
		InputPy.Sanalyzer.Attenuation.set. This function is not available if the optional 'Digital Baseband' interface is active. \n
			:param state: ON | OFF | 0 | 1
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INPut:ATTenuation:AUTO {param}')

	def clone(self) -> 'AutoCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AutoCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
