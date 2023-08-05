from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReferenceCls:
	"""Reference commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reference", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import AutoCls
			self._auto = AutoCls(self._core, self._cmd_group)
		return self._auto

	def set(self, curve_width_reference: float) -> None:
		"""SCPI: CONFigure:AMPM:CWIDth:REFerence \n
		Snippet: driver.applications.k18AmplifierEt.configure.amPm.cwidth.reference.set(curve_width_reference = 1.0) \n
		Sets and queries the curve width computation reference point \n
			:param curve_width_reference: numeric value Unit: dB
		"""
		param = Conversions.decimal_value_to_str(curve_width_reference)
		self._core.io.write(f'CONFigure:AMPM:CWIDth:REFerence {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:AMPM:CWIDth:REFerence \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.amPm.cwidth.reference.get() \n
		Sets and queries the curve width computation reference point \n
			:return: curve_width_reference: numeric value Unit: dB"""
		response = self._core.io.query_str(f'CONFigure:AMPM:CWIDth:REFerence?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'ReferenceCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ReferenceCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
