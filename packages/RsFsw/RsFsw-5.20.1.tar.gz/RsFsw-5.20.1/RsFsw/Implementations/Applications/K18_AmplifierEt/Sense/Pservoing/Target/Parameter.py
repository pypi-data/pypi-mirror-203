from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ParameterCls:
	"""Parameter commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("parameter", core, parent)

	def set(self, target: enums.TargetParameter) -> None:
		"""SCPI: [SENSe]:PSERvoing:TARGet:PARameter \n
		Snippet: driver.applications.k18AmplifierEt.sense.pservoing.target.parameter.set(target = enums.TargetParameter.EVM) \n
		Sets the power servoing target parameter. \n
			:param target: POUT | EVM | LADJ | UADJ | LALT | UALT POUT Power Out EVM EVM LADJ ACLR Adjacent Lower UADJ ACLR Adjacent Upper LALT ACLR Alternate Lower UALT ACLR Alternate Upper
		"""
		param = Conversions.enum_scalar_to_str(target, enums.TargetParameter)
		self._core.io.write(f'SENSe:PSERvoing:TARGet:PARameter {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.TargetParameter:
		"""SCPI: [SENSe]:PSERvoing:TARGet:PARameter \n
		Snippet: value: enums.TargetParameter = driver.applications.k18AmplifierEt.sense.pservoing.target.parameter.get() \n
		Sets the power servoing target parameter. \n
			:return: target: POUT | EVM | LADJ | UADJ | LALT | UALT POUT Power Out EVM EVM LADJ ACLR Adjacent Lower UADJ ACLR Adjacent Upper LALT ACLR Alternate Lower UALT ACLR Alternate Upper"""
		response = self._core.io.query_str(f'SENSe:PSERvoing:TARGet:PARameter?')
		return Conversions.str_to_scalar_enum(response, enums.TargetParameter)
