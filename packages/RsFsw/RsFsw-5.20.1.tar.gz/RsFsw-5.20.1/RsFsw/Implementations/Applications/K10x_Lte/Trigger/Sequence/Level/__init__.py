from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LevelCls:
	"""Level commands group definition. 6 total commands, 6 Subgroups, 0 group commands
	Repeated Capability: Instrument, default value after init: Instrument.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_instrument_get', 'repcap_instrument_set', repcap.Instrument.Nr1)

	def repcap_instrument_set(self, instrument: repcap.Instrument) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Instrument.Default
		Default value after init: Instrument.Nr1"""
		self._cmd_group.set_repcap_enum_value(instrument)

	def repcap_instrument_get(self) -> repcap.Instrument:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def bbPower(self):
		"""bbPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bbPower'):
			from .BbPower import BbPowerCls
			self._bbPower = BbPowerCls(self._core, self._cmd_group)
		return self._bbPower

	@property
	def external(self):
		"""external commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_external'):
			from .External import ExternalCls
			self._external = ExternalCls(self._core, self._cmd_group)
		return self._external

	@property
	def ifPower(self):
		"""ifPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ifPower'):
			from .IfPower import IfPowerCls
			self._ifPower = IfPowerCls(self._core, self._cmd_group)
		return self._ifPower

	@property
	def iqPower(self):
		"""iqPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqPower'):
			from .IqPower import IqPowerCls
			self._iqPower = IqPowerCls(self._core, self._cmd_group)
		return self._iqPower

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def rfPower(self):
		"""rfPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfPower'):
			from .RfPower import RfPowerCls
			self._rfPower = RfPowerCls(self._core, self._cmd_group)
		return self._rfPower

	def clone(self) -> 'LevelCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LevelCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
