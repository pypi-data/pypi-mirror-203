from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MupGeneratorCls:
	"""MupGenerator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mupGenerator", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:HAMMerstein:MUPGenerator \n
		Snippet: driver.applications.k18AmplifierEt.configure.hammerstein.mupGenerator.set() \n
		Starts the DSP and updates the generator. \n
		"""
		self._core.io.write(f'CONFigure:HAMMerstein:MUPGenerator')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:HAMMerstein:MUPGenerator \n
		Snippet: driver.applications.k18AmplifierEt.configure.hammerstein.mupGenerator.set_with_opc() \n
		Starts the DSP and updates the generator. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:HAMMerstein:MUPGenerator', opc_timeout_ms)
