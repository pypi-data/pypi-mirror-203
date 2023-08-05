from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LraCls:
	"""Lra commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lra", core, parent)

	def set(self, value: enums.LraValue, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PRACh:LRA \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.prach.lra.set(value = enums.LraValue.L1151, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the PRACH paramater LRA. \n
			:param value: L139 | L571 | L839 | L1151 The availability of the parameters depends on the PRACH format and subcarrier spacing. •method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Prach.FormatPy.set •method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Prach.Scs.set
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(value, enums.LraValue)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PRACh:LRA {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.LraValue:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PRACh:LRA \n
		Snippet: value: enums.LraValue = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.prach.lra.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the PRACH paramater LRA. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: value: L139 | L571 | L839 | L1151 The availability of the parameters depends on the PRACH format and subcarrier spacing. •method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Prach.FormatPy.set •method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Prach.Scs.set"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PRACh:LRA?')
		return Conversions.str_to_scalar_enum(response, enums.LraValue)
