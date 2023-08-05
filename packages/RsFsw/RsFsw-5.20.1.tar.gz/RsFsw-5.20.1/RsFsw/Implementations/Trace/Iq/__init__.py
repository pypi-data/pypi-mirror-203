from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqCls:
	"""Iq commands group definition. 20 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iq", core, parent)

	@property
	def data(self):
		"""data commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import DataCls
			self._data = DataCls(self._core, self._cmd_group)
		return self._data

	@property
	def egate(self):
		"""egate commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_egate'):
			from .Egate import EgateCls
			self._egate = EgateCls(self._core, self._cmd_group)
		return self._egate

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import BandwidthCls
			self._bandwidth = BandwidthCls(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def eval(self):
		"""eval commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eval'):
			from .Eval import EvalCls
			self._eval = EvalCls(self._core, self._cmd_group)
		return self._eval

	@property
	def diqFilter(self):
		"""diqFilter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_diqFilter'):
			from .DiqFilter import DiqFilterCls
			self._diqFilter = DiqFilterCls(self._core, self._cmd_group)
		return self._diqFilter

	@property
	def apcon(self):
		"""apcon commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_apcon'):
			from .Apcon import ApconCls
			self._apcon = ApconCls(self._core, self._cmd_group)
		return self._apcon

	@property
	def file(self):
		"""file commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_file'):
			from .File import FileCls
			self._file = FileCls(self._core, self._cmd_group)
		return self._file

	@property
	def lcapture(self):
		"""lcapture commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lcapture'):
			from .Lcapture import LcaptureCls
			self._lcapture = LcaptureCls(self._core, self._cmd_group)
		return self._lcapture

	@property
	def scapture(self):
		"""scapture commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_scapture'):
			from .Scapture import ScaptureCls
			self._scapture = ScaptureCls(self._core, self._cmd_group)
		return self._scapture

	def clone(self) -> 'IqCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IqCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
