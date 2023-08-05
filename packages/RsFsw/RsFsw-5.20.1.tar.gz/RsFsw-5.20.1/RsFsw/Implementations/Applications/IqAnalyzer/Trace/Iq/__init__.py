from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqCls:
	"""Iq commands group definition. 22 total commands, 13 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iq", core, parent)

	@property
	def apcon(self):
		"""apcon commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_apcon'):
			from .Apcon import ApconCls
			self._apcon = ApconCls(self._core, self._cmd_group)
		return self._apcon

	@property
	def tpisample(self):
		"""tpisample commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpisample'):
			from .Tpisample import TpisampleCls
			self._tpisample = TpisampleCls(self._core, self._cmd_group)
		return self._tpisample

	@property
	def average(self):
		"""average commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_average'):
			from .Average import AverageCls
			self._average = AverageCls(self._core, self._cmd_group)
		return self._average

	@property
	def diqFilter(self):
		"""diqFilter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_diqFilter'):
			from .DiqFilter import DiqFilterCls
			self._diqFilter = DiqFilterCls(self._core, self._cmd_group)
		return self._diqFilter

	@property
	def egate(self):
		"""egate commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_egate'):
			from .Egate import EgateCls
			self._egate = EgateCls(self._core, self._cmd_group)
		return self._egate

	@property
	def eval(self):
		"""eval commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eval'):
			from .Eval import EvalCls
			self._eval = EvalCls(self._core, self._cmd_group)
		return self._eval

	@property
	def wband(self):
		"""wband commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_wband'):
			from .Wband import WbandCls
			self._wband = WbandCls(self._core, self._cmd_group)
		return self._wband

	@property
	def wfilter(self):
		"""wfilter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wfilter'):
			from .Wfilter import WfilterCls
			self._wfilter = WfilterCls(self._core, self._cmd_group)
		return self._wfilter

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def file(self):
		"""file commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_file'):
			from .File import FileCls
			self._file = FileCls(self._core, self._cmd_group)
		return self._file

	@property
	def rlength(self):
		"""rlength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rlength'):
			from .Rlength import RlengthCls
			self._rlength = RlengthCls(self._core, self._cmd_group)
		return self._rlength

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRateCls
			self._symbolRate = SymbolRateCls(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def data(self):
		"""data commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_data'):
			from .Data import DataCls
			self._data = DataCls(self._core, self._cmd_group)
		return self._data

	def clone(self) -> 'IqCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IqCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
