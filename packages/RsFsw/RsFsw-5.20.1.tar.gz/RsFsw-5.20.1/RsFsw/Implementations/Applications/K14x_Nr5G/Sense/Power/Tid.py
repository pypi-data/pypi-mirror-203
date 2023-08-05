from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TidCls:
	"""Tid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tid", core, parent)

	def set(self, idn: enums.PowerIdn) -> None:
		"""SCPI: [SENSe]:POWer:TID \n
		Snippet: driver.applications.k14Xnr5G.sense.power.tid.set(idn = enums.PowerIdn.ID1) \n
		This command selects the test ID for ACLR measurements.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select FR2 frequency deployment (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.DfRange.set) . \n
			:param idn: NONE No test ID. ID1 | ID2 | ID3 | ID4 | ID5 | ID6 | ID7 | ID8 | ID9 | ID10 | ID11 | ID12 | ID13 | ID14 | ID15 Test ID 1 to 15.
		"""
		param = Conversions.enum_scalar_to_str(idn, enums.PowerIdn)
		self._core.io.write(f'SENSe:POWer:TID {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PowerIdn:
		"""SCPI: [SENSe]:POWer:TID \n
		Snippet: value: enums.PowerIdn = driver.applications.k14Xnr5G.sense.power.tid.get() \n
		This command selects the test ID for ACLR measurements.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select FR2 frequency deployment (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.DfRange.set) . \n
			:return: idn: NONE No test ID. ID1 | ID2 | ID3 | ID4 | ID5 | ID6 | ID7 | ID8 | ID9 | ID10 | ID11 | ID12 | ID13 | ID14 | ID15 Test ID 1 to 15."""
		response = self._core.io.query_str(f'SENSe:POWer:TID?')
		return Conversions.str_to_scalar_enum(response, enums.PowerIdn)
