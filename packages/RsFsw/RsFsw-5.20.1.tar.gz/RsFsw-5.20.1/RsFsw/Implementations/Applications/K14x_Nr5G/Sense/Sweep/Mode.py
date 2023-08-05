from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.SweepModeD) -> None:
		"""SCPI: [SENSe]:SWEep:MODE \n
		Snippet: driver.applications.k14Xnr5G.sense.sweep.mode.set(mode = enums.SweepModeD.AUTO) \n
		This command selects the capture mode for combined measurements.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Measure the EVM only:
			Table Header:  \n
			- method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Aclr.set = OFF
			- method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Sem.set = OFF
			- method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Evm.set = ON \n
			:param mode: AUTO Captures and analyzes the complete signal. TX Captures and analyzes the Tx channel only.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SweepModeD)
		self._core.io.write(f'SENSe:SWEep:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SweepModeD:
		"""SCPI: [SENSe]:SWEep:MODE \n
		Snippet: value: enums.SweepModeD = driver.applications.k14Xnr5G.sense.sweep.mode.get() \n
		This command selects the capture mode for combined measurements.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Measure the EVM only:
			Table Header:  \n
			- method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Aclr.set = OFF
			- method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Sem.set = OFF
			- method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Evm.set = ON \n
			:return: mode: AUTO Captures and analyzes the complete signal. TX Captures and analyzes the Tx channel only."""
		response = self._core.io.query_str(f'SENSe:SWEep:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SweepModeD)
