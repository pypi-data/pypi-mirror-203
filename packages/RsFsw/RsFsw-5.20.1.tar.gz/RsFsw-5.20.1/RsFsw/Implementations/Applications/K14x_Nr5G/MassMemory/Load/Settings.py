from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SettingsCls:
	"""Settings commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("settings", core, parent)

	def set(self) -> None:
		"""SCPI: MMEMory:LOAD:SETTings \n
		Snippet: driver.applications.k14Xnr5G.massMemory.load.settings.set() \n
		Restores the settings of the last measurement sequence in combined mode. \n
		"""
		self._core.io.write(f'MMEMory:LOAD:SETTings')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: MMEMory:LOAD:SETTings \n
		Snippet: driver.applications.k14Xnr5G.massMemory.load.settings.set_with_opc() \n
		Restores the settings of the last measurement sequence in combined mode. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'MMEMory:LOAD:SETTings', opc_timeout_ms)
