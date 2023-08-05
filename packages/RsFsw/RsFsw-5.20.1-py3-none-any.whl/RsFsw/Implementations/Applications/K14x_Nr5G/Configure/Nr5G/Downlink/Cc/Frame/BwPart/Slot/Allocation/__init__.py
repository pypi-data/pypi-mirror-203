from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal.RepeatedCapability import RepeatedCapability
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllocationCls:
	"""Allocation commands group definition. 39 total commands, 15 Subgroups, 1 group commands
	Repeated Capability: Allocation, default value after init: Allocation.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("allocation", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_allocation_get', 'repcap_allocation_set', repcap.Allocation.Nr0)

	def repcap_allocation_set(self, allocation: repcap.Allocation) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Allocation.Default
		Default value after init: Allocation.Nr0"""
		self._cmd_group.set_repcap_enum_value(allocation)

	def repcap_allocation_get(self) -> repcap.Allocation:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def ccoding(self):
		"""ccoding commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccoding'):
			from .Ccoding import CcodingCls
			self._ccoding = CcodingCls(self._core, self._cmd_group)
		return self._ccoding

	@property
	def clMapping(self):
		"""clMapping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_clMapping'):
			from .ClMapping import ClMappingCls
			self._clMapping = ClMappingCls(self._core, self._cmd_group)
		return self._clMapping

	@property
	def copy(self):
		"""copy commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_copy'):
			from .Copy import CopyCls
			self._copy = CopyCls(self._core, self._cmd_group)
		return self._copy

	@property
	def cw(self):
		"""cw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cw'):
			from .Cw import CwCls
			self._cw = CwCls(self._core, self._cmd_group)
		return self._cw

	@property
	def dmrs(self):
		"""dmrs commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_dmrs'):
			from .Dmrs import DmrsCls
			self._dmrs = DmrsCls(self._core, self._cmd_group)
		return self._dmrs

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def ptrs(self):
		"""ptrs commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ptrs'):
			from .Ptrs import PtrsCls
			self._ptrs = PtrsCls(self._core, self._cmd_group)
		return self._ptrs

	@property
	def rbCount(self):
		"""rbCount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbCount'):
			from .RbCount import RbCountCls
			self._rbCount = RbCountCls(self._core, self._cmd_group)
		return self._rbCount

	@property
	def rbOffset(self):
		"""rbOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbOffset'):
			from .RbOffset import RbOffsetCls
			self._rbOffset = RbOffsetCls(self._core, self._cmd_group)
		return self._rbOffset

	@property
	def rpoint(self):
		"""rpoint commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rpoint'):
			from .Rpoint import RpointCls
			self._rpoint = RpointCls(self._core, self._cmd_group)
		return self._rpoint

	@property
	def scount(self):
		"""scount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scount'):
			from .Scount import ScountCls
			self._scount = ScountCls(self._core, self._cmd_group)
		return self._scount

	@property
	def scrambling(self):
		"""scrambling commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_scrambling'):
			from .Scrambling import ScramblingCls
			self._scrambling = ScramblingCls(self._core, self._cmd_group)
		return self._scrambling

	@property
	def soffset(self):
		"""soffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_soffset'):
			from .Soffset import SoffsetCls
			self._soffset = SoffsetCls(self._core, self._cmd_group)
		return self._soffset

	@property
	def ueId(self):
		"""ueId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueId'):
			from .UeId import UeIdCls
			self._ueId = UeIdCls(self._core, self._cmd_group)
		return self._ueId

	@property
	def vtpInter(self):
		"""vtpInter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vtpInter'):
			from .VtpInter import VtpInterCls
			self._vtpInter = VtpInterCls(self._core, self._cmd_group)
		return self._vtpInter

	def copy_to(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, slot=repcap.Slot.Default, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SLOT<sl>:ALLocation<al>:COPY \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.slot.allocation.copy_to(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, slot = repcap.Slot.Default, allocation = repcap.Allocation.Default) \n
		This command copies a PDSCH configuration to other slots.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Number of configurable slots > 1 (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Cslot.set) .
			- Select paste mode (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Slot.Allocation.Copy.Mode.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param slot: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Allocation')
		"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SLOT{slot_cmd_val}:ALLocation{allocation_cmd_val}:COPY')

	def copy_to_with_opc(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, slot=repcap.Slot.Default, allocation=repcap.Allocation.Default, opc_timeout_ms: int = -1) -> None:
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SLOT<sl>:ALLocation<al>:COPY \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.slot.allocation.copy_to_with_opc(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, slot = repcap.Slot.Default, allocation = repcap.Allocation.Default) \n
		This command copies a PDSCH configuration to other slots.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Number of configurable slots > 1 (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Cslot.set) .
			- Select paste mode (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Slot.Allocation.Copy.Mode.set) . \n
		Same as copy_to, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param slot: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Allocation')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SLOT{slot_cmd_val}:ALLocation{allocation_cmd_val}:COPY', opc_timeout_ms)

	def clone(self) -> 'AllocationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AllocationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
