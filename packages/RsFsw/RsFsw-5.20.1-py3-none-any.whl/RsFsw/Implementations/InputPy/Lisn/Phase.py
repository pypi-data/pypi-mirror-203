from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhaseCls:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def set(self, phase: enums.LisnPhase, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:LISN:PHASe \n
		Snippet: driver.inputPy.lisn.phase.set(phase = enums.LisnPhase.L1, inputIx = repcap.InputIx.Default) \n
		This command selects one LISN phase to be measured. \n
			:param phase: L1 L2 Available for networks with four phases (R&S ESH2Z5, R&S ENV4200 and R&S ENV432) L3 Available for networks with four phases (R&S ESH2Z5, R&S ENV4200 and R&S ENV432) N
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(phase, enums.LisnPhase)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:LISN:PHASe {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.LisnPhase:
		"""SCPI: INPut<ip>:LISN:PHASe \n
		Snippet: value: enums.LisnPhase = driver.inputPy.lisn.phase.get(inputIx = repcap.InputIx.Default) \n
		This command selects one LISN phase to be measured. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: phase: L1 L2 Available for networks with four phases (R&S ESH2Z5, R&S ENV4200 and R&S ENV432) L3 Available for networks with four phases (R&S ESH2Z5, R&S ENV4200 and R&S ENV432) N"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:LISN:PHASe?')
		return Conversions.str_to_scalar_enum(response, enums.LisnPhase)
