from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TitleCls:
	"""Title commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("title", core, parent)

	def set(self, title: str, line=repcap.Line.Default) -> None:
		"""SCPI: HCOPy:TREPort:ITEM:HEADer:LINE<li>:TITLe \n
		Snippet: driver.hardCopy.treport.item.header.line.title.set(title = '1', line = repcap.Line.Default) \n
		This command defines a custom name for one of the items part of the report header. You can define up to 6 items in the
		header. Use method RsFsw.HardCopy.Treport.Item.Header.Line.Text.set to add a value to each item. Use method RsFsw.
		HardCopy.Treport.Item.Header.Line.Control.set to select the condition under which each item is shown. \n
			:param title: String containing the title of the item. The default titles are as follows: • Line 1: 'Heading' • Line 2: 'Meas Type' • Line 3: 'Equipment under Test' • Line 4: 'Manufacturer' • Line 5: 'OP Condition' • Line 6: 'Test Spec' Make sure that the title string is not too long, because strings that are too long could mess up the layout of the report.
			:param line: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Line')
		"""
		param = Conversions.value_to_quoted_str(title)
		line_cmd_val = self._cmd_group.get_repcap_cmd_value(line, repcap.Line)
		self._core.io.write(f'HCOPy:TREPort:ITEM:HEADer:LINE{line_cmd_val}:TITLe {param}')

	def get(self, line=repcap.Line.Default) -> str:
		"""SCPI: HCOPy:TREPort:ITEM:HEADer:LINE<li>:TITLe \n
		Snippet: value: str = driver.hardCopy.treport.item.header.line.title.get(line = repcap.Line.Default) \n
		This command defines a custom name for one of the items part of the report header. You can define up to 6 items in the
		header. Use method RsFsw.HardCopy.Treport.Item.Header.Line.Text.set to add a value to each item. Use method RsFsw.
		HardCopy.Treport.Item.Header.Line.Control.set to select the condition under which each item is shown. \n
			:param line: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Line')
			:return: title: String containing the title of the item. The default titles are as follows: • Line 1: 'Heading' • Line 2: 'Meas Type' • Line 3: 'Equipment under Test' • Line 4: 'Manufacturer' • Line 5: 'OP Condition' • Line 6: 'Test Spec' Make sure that the title string is not too long, because strings that are too long could mess up the layout of the report."""
		line_cmd_val = self._cmd_group.get_repcap_cmd_value(line, repcap.Line)
		response = self._core.io.query_str(f'HCOPy:TREPort:ITEM:HEADer:LINE{line_cmd_val}:TITLe?')
		return trim_str_response(response)
