from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SelectCls:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, source: enums.BbInputSource) -> None:
		"""SCPI: INPut:SELect \n
		Snippet: driver.applications.k14Xnr5G.inputPy.select.set(source = enums.BbInputSource.AIQ) \n
		This command selects the signal source for measurements, i.e. it defines which connector is used to input data to the R&S
		FSW. If no additional input options are installed, only RF input or file input is supported. For R&S FSW85 models with
		two RF input connectors, you must select the input connector to configure first using method RsFsw.Applications.K10x_Lte.
		InputPy.TypePy.set. \n
			:param source: RF Radio Frequency ('RF INPUT' connector) FIQ I/Q data file (selected by method RsFsw.InputPy.File.Path.set) For details, see 'Basics on Input from I/Q Data Files'. Not available for Input2.
		"""
		param = Conversions.enum_scalar_to_str(source, enums.BbInputSource)
		self._core.io.write(f'INPut:SELect {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.BbInputSource:
		"""SCPI: INPut:SELect \n
		Snippet: value: enums.BbInputSource = driver.applications.k14Xnr5G.inputPy.select.get() \n
		This command selects the signal source for measurements, i.e. it defines which connector is used to input data to the R&S
		FSW. If no additional input options are installed, only RF input or file input is supported. For R&S FSW85 models with
		two RF input connectors, you must select the input connector to configure first using method RsFsw.Applications.K10x_Lte.
		InputPy.TypePy.set. \n
			:return: source: RF Radio Frequency ('RF INPUT' connector) FIQ I/Q data file (selected by method RsFsw.InputPy.File.Path.set) For details, see 'Basics on Input from I/Q Data Files'. Not available for Input2."""
		response = self._core.io.query_str(f'INPut:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.BbInputSource)
