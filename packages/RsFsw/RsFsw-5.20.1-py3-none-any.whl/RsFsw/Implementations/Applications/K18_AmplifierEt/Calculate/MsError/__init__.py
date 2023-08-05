from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MsErrorCls:
	"""MsError commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("msError", core, parent)

	@property
	def configure(self):
		"""configure commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_configure'):
			from .Configure import ConfigureCls
			self._configure = ConfigureCls(self._core, self._cmd_group)
		return self._configure

	@property
	def iqAvg(self):
		"""iqAvg commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqAvg'):
			from .IqAvg import IqAvgCls
			self._iqAvg = IqAvgCls(self._core, self._cmd_group)
		return self._iqAvg

	def get(self) -> float:
		"""SCPI: CALCulate:MSERror \n
		Snippet: value: float = driver.applications.k18AmplifierEt.calculate.msError.get() \n
		Calculates the detailed MSE and returns the result. \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'CALCulate:MSERror?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'MsErrorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MsErrorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
