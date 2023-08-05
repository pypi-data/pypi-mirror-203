from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApplicationsCls:
	"""Applications commands group definition. 7387 total commands, 15 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("applications", core, parent)

	@property
	def k70_Vsa(self):
		"""k70_Vsa commands group. 14 Sub-classes, 0 commands."""
		if not hasattr(self, '_k70_Vsa'):
			from .K70_Vsa import K70_VsaCls
			self._k70_Vsa = K70_VsaCls(self._core, self._cmd_group)
		return self._k70_Vsa

	@property
	def k10x_Lte(self):
		"""k10x_Lte commands group. 18 Sub-classes, 0 commands."""
		if not hasattr(self, '_k10x_Lte'):
			from .K10x_Lte import K10x_LteCls
			self._k10x_Lte = K10x_LteCls(self._core, self._cmd_group)
		return self._k10x_Lte

	@property
	def k17_Mcgd(self):
		"""k17_Mcgd commands group. 14 Sub-classes, 0 commands."""
		if not hasattr(self, '_k17_Mcgd'):
			from .K17_Mcgd import K17_McgdCls
			self._k17_Mcgd = K17_McgdCls(self._core, self._cmd_group)
		return self._k17_Mcgd

	@property
	def k50_Spurious(self):
		"""k50_Spurious commands group. 16 Sub-classes, 0 commands."""
		if not hasattr(self, '_k50_Spurious'):
			from .K50_Spurious import K50_SpuriousCls
			self._k50_Spurious = K50_SpuriousCls(self._core, self._cmd_group)
		return self._k50_Spurious

	@property
	def k91_Wlan(self):
		"""k91_Wlan commands group. 16 Sub-classes, 1 commands."""
		if not hasattr(self, '_k91_Wlan'):
			from .K91_Wlan import K91_WlanCls
			self._k91_Wlan = K91_WlanCls(self._core, self._cmd_group)
		return self._k91_Wlan

	@property
	def k6_Pulse(self):
		"""k6_Pulse commands group. 15 Sub-classes, 0 commands."""
		if not hasattr(self, '_k6_Pulse'):
			from .K6_Pulse import K6_PulseCls
			self._k6_Pulse = K6_PulseCls(self._core, self._cmd_group)
		return self._k6_Pulse

	@property
	def k9x_11ad(self):
		"""k9x_11ad commands group. 17 Sub-classes, 0 commands."""
		if not hasattr(self, '_k9x_11ad'):
			from .K9x_11ad import K9x_11adCls
			self._k9x_11ad = K9x_11adCls(self._core, self._cmd_group)
		return self._k9x_11ad

	@property
	def k18_AmplifierEt(self):
		"""k18_AmplifierEt commands group. 18 Sub-classes, 0 commands."""
		if not hasattr(self, '_k18_AmplifierEt'):
			from .K18_AmplifierEt import K18_AmplifierEtCls
			self._k18_AmplifierEt = K18_AmplifierEtCls(self._core, self._cmd_group)
		return self._k18_AmplifierEt

	@property
	def k60_Transient(self):
		"""k60_Transient commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_k60_Transient'):
			from .K60_Transient import K60_TransientCls
			self._k60_Transient = K60_TransientCls(self._core, self._cmd_group)
		return self._k60_Transient

	@property
	def k30_NoiseFigure(self):
		"""k30_NoiseFigure commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_k30_NoiseFigure'):
			from .K30_NoiseFigure import K30_NoiseFigureCls
			self._k30_NoiseFigure = K30_NoiseFigureCls(self._core, self._cmd_group)
		return self._k30_NoiseFigure

	@property
	def k40_PhaseNoise(self):
		"""k40_PhaseNoise commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_k40_PhaseNoise'):
			from .K40_PhaseNoise import K40_PhaseNoiseCls
			self._k40_PhaseNoise = K40_PhaseNoiseCls(self._core, self._cmd_group)
		return self._k40_PhaseNoise

	@property
	def iqAnalyzer(self):
		"""iqAnalyzer commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqAnalyzer'):
			from .IqAnalyzer import IqAnalyzerCls
			self._iqAnalyzer = IqAnalyzerCls(self._core, self._cmd_group)
		return self._iqAnalyzer

	@property
	def k7_AnalogDemod(self):
		"""k7_AnalogDemod commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_k7_AnalogDemod'):
			from .K7_AnalogDemod import K7_AnalogDemodCls
			self._k7_AnalogDemod = K7_AnalogDemodCls(self._core, self._cmd_group)
		return self._k7_AnalogDemod

	@property
	def k149_Uwb(self):
		"""k149_Uwb commands group. 14 Sub-classes, 0 commands."""
		if not hasattr(self, '_k149_Uwb'):
			from .K149_Uwb import K149_UwbCls
			self._k149_Uwb = K149_UwbCls(self._core, self._cmd_group)
		return self._k149_Uwb

	@property
	def k14x_Nr5G(self):
		"""k14x_Nr5G commands group. 18 Sub-classes, 0 commands."""
		if not hasattr(self, '_k14x_Nr5G'):
			from .K14x_Nr5G import K14x_Nr5GCls
			self._k14x_Nr5G = K14x_Nr5GCls(self._core, self._cmd_group)
		return self._k14x_Nr5G

	def clone(self) -> 'ApplicationsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ApplicationsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
