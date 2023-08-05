from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PclassCls:
	"""Pclass commands group definition. 7 total commands, 5 Subgroups, 1 group commands
	Repeated Capability: PowerClass, default value after init: PowerClass.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pclass", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_powerClass_get', 'repcap_powerClass_set', repcap.PowerClass.Nr1)

	def repcap_powerClass_set(self, powerClass: repcap.PowerClass) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to PowerClass.Default
		Default value after init: PowerClass.Nr1"""
		self._cmd_group.set_repcap_enum_value(powerClass)

	def repcap_powerClass_get(self) -> repcap.PowerClass:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def count(self):
		"""count commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import CountCls
			self._count = CountCls(self._core, self._cmd_group)
		return self._count

	@property
	def exclusive(self):
		"""exclusive commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_exclusive'):
			from .Exclusive import ExclusiveCls
			self._exclusive = ExclusiveCls(self._core, self._cmd_group)
		return self._exclusive

	@property
	def limit(self):
		"""limit commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import LimitCls
			self._limit = LimitCls(self._core, self._cmd_group)
		return self._limit

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maximum'):
			from .Maximum import MaximumCls
			self._maximum = MaximumCls(self._core, self._cmd_group)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_minimum'):
			from .Minimum import MinimumCls
			self._minimum = MinimumCls(self._core, self._cmd_group)
		return self._minimum

	def set(self, exclusive: bool, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, powerClass=repcap.PowerClass.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum:PCLass<pc> \n
		Snippet: driver.applications.k149Uwb.calculate.limit.espectrum.pclass.set(exclusive = False, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, powerClass = repcap.PowerClass.Default) \n
		No command help available \n
			:param exclusive: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param powerClass: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pclass')
		"""
		param = Conversions.bool_to_str(exclusive)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		powerClass_cmd_val = self._cmd_group.get_repcap_cmd_value(powerClass, repcap.PowerClass)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum:PCLass{powerClass_cmd_val} {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, powerClass=repcap.PowerClass.Default) -> bool:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum:PCLass<pc> \n
		Snippet: value: bool = driver.applications.k149Uwb.calculate.limit.espectrum.pclass.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, powerClass = repcap.PowerClass.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param powerClass: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pclass')
			:return: exclusive: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		powerClass_cmd_val = self._cmd_group.get_repcap_cmd_value(powerClass, repcap.PowerClass)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum:PCLass{powerClass_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'PclassCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PclassCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
