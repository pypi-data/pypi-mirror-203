from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 5 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def analyzer(self):
		"""analyzer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_analyzer'):
			from .Analyzer import AnalyzerCls
			self._analyzer = AnalyzerCls(self._core, self._cmd_group)
		return self._analyzer

	@property
	def generator(self):
		"""generator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_generator'):
			from .Generator import GeneratorCls
			self._generator = GeneratorCls(self._core, self._cmd_group)
		return self._generator

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import OffsetCls
			self._offset = OffsetCls(self._core, self._cmd_group)
		return self._offset

	@property
	def factor(self):
		"""factor commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_factor'):
			from .Factor import FactorCls
			self._factor = FactorCls(self._core, self._cmd_group)
		return self._factor

	def clone(self) -> 'FrequencyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FrequencyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
