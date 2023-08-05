from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConfigureCls:
	"""Configure commands group definition. 189 total commands, 19 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("configure", core, parent)

	@property
	def cfReduction(self):
		"""cfReduction commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_cfReduction'):
			from .CfReduction import CfReductionCls
			self._cfReduction = CfReductionCls(self._core, self._cmd_group)
		return self._cfReduction

	@property
	def ddpd(self):
		"""ddpd commands group. 10 Sub-classes, 3 commands."""
		if not hasattr(self, '_ddpd'):
			from .Ddpd import DdpdCls
			self._ddpd = DdpdCls(self._core, self._cmd_group)
		return self._ddpd

	@property
	def dpd(self):
		"""dpd commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpd'):
			from .Dpd import DpdCls
			self._dpd = DpdCls(self._core, self._cmd_group)
		return self._dpd

	@property
	def dut(self):
		"""dut commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dut'):
			from .Dut import DutCls
			self._dut = DutCls(self._core, self._cmd_group)
		return self._dut

	@property
	def equalizer(self):
		"""equalizer commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_equalizer'):
			from .Equalizer import EqualizerCls
			self._equalizer = EqualizerCls(self._core, self._cmd_group)
		return self._equalizer

	@property
	def generator(self):
		"""generator commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_generator'):
			from .Generator import GeneratorCls
			self._generator = GeneratorCls(self._core, self._cmd_group)
		return self._generator

	@property
	def frSpan(self):
		"""frSpan commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_frSpan'):
			from .FrSpan import FrSpanCls
			self._frSpan = FrSpanCls(self._core, self._cmd_group)
		return self._frSpan

	@property
	def amPm(self):
		"""amPm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_amPm'):
			from .AmPm import AmPmCls
			self._amPm = AmPmCls(self._core, self._cmd_group)
		return self._amPm

	@property
	def hammerstein(self):
		"""hammerstein commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_hammerstein'):
			from .Hammerstein import HammersteinCls
			self._hammerstein = HammersteinCls(self._core, self._cmd_group)
		return self._hammerstein

	@property
	def modeling(self):
		"""modeling commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_modeling'):
			from .Modeling import ModelingCls
			self._modeling = ModelingCls(self._core, self._cmd_group)
		return self._modeling

	@property
	def mdpd(self):
		"""mdpd commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_mdpd'):
			from .Mdpd import MdpdCls
			self._mdpd = MdpdCls(self._core, self._cmd_group)
		return self._mdpd

	@property
	def pae(self):
		"""pae commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pae'):
			from .Pae import PaeCls
			self._pae = PaeCls(self._core, self._cmd_group)
		return self._pae

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def psweep(self):
		"""psweep commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_psweep'):
			from .Psweep import PsweepCls
			self._psweep = PsweepCls(self._core, self._cmd_group)
		return self._psweep

	@property
	def refSignal(self):
		"""refSignal commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_refSignal'):
			from .RefSignal import RefSignalCls
			self._refSignal = RefSignalCls(self._core, self._cmd_group)
		return self._refSignal

	@property
	def result(self):
		"""result commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_result'):
			from .Result import ResultCls
			self._result = ResultCls(self._core, self._cmd_group)
		return self._result

	@property
	def settings(self):
		"""settings commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_settings'):
			from .Settings import SettingsCls
			self._settings = SettingsCls(self._core, self._cmd_group)
		return self._settings

	@property
	def signal(self):
		"""signal commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_signal'):
			from .Signal import SignalCls
			self._signal = SignalCls(self._core, self._cmd_group)
		return self._signal

	@property
	def sync(self):
		"""sync commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import SyncCls
			self._sync = SyncCls(self._core, self._cmd_group)
		return self._sync

	def clone(self) -> 'ConfigureCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ConfigureCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
