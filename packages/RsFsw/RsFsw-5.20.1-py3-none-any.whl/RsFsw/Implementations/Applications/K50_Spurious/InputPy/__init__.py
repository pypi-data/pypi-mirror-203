from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPyCls:
	"""InputPy commands group definition. 6 total commands, 5 Subgroups, 0 group commands
	Repeated Capability: InputIx, default value after init: InputIx.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_inputIx_get', 'repcap_inputIx_set', repcap.InputIx.Nr1)

	def repcap_inputIx_set(self, inputIx: repcap.InputIx) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to InputIx.Default
		Default value after init: InputIx.Nr1"""
		self._cmd_group.set_repcap_enum_value(inputIx)

	def repcap_inputIx_get(self) -> repcap.InputIx:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def connector(self):
		"""connector commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_connector'):
			from .Connector import ConnectorCls
			self._connector = ConnectorCls(self._core, self._cmd_group)
		return self._connector

	@property
	def coupling(self):
		"""coupling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coupling'):
			from .Coupling import CouplingCls
			self._coupling = CouplingCls(self._core, self._cmd_group)
		return self._coupling

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePyCls
			self._typePy = TypePyCls(self._core, self._cmd_group)
		return self._typePy

	@property
	def filterPy(self):
		"""filterPy commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPyCls
			self._filterPy = FilterPyCls(self._core, self._cmd_group)
		return self._filterPy

	@property
	def impedance(self):
		"""impedance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_impedance'):
			from .Impedance import ImpedanceCls
			self._impedance = ImpedanceCls(self._core, self._cmd_group)
		return self._impedance

	def clone(self) -> 'InputPyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InputPyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
