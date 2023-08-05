from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EgateCls:
	"""Egate commands group definition. 14 total commands, 9 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("egate", core, parent)

	@property
	def agating(self):
		"""agating commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_agating'):
			from .Agating import AgatingCls
			self._agating = AgatingCls(self._core, self._cmd_group)
		return self._agating

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import AutoCls
			self._auto = AutoCls(self._core, self._cmd_group)
		return self._auto

	@property
	def continuous(self):
		"""continuous commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_continuous'):
			from .Continuous import ContinuousCls
			self._continuous = ContinuousCls(self._core, self._cmd_group)
		return self._continuous

	@property
	def holdoff(self):
		"""holdoff commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_holdoff'):
			from .Holdoff import HoldoffCls
			self._holdoff = HoldoffCls(self._core, self._cmd_group)
		return self._holdoff

	@property
	def length(self):
		"""length commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_length'):
			from .Length import LengthCls
			self._length = LengthCls(self._core, self._cmd_group)
		return self._length

	@property
	def level(self):
		"""level commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_level'):
			from .Level import LevelCls
			self._level = LevelCls(self._core, self._cmd_group)
		return self._level

	@property
	def polarity(self):
		"""polarity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_polarity'):
			from .Polarity import PolarityCls
			self._polarity = PolarityCls(self._core, self._cmd_group)
		return self._polarity

	@property
	def source(self):
		"""source commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_source'):
			from .Source import SourceCls
			self._source = SourceCls(self._core, self._cmd_group)
		return self._source

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePyCls
			self._typePy = TypePyCls(self._core, self._cmd_group)
		return self._typePy

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe \n
		Snippet: driver.applications.k14Xnr5G.sense.sweep.egate.set(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:SWEep:EGATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:SWEep:EGATe \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.sweep.egate.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'EgateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EgateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
