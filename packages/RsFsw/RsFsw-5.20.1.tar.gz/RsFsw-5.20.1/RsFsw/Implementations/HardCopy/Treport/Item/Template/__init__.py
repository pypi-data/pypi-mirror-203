from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TemplateCls:
	"""Template commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("template", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	def delete(self, template: str) -> None:
		"""SCPI: HCOPy:TREPort:ITEM:TEMPlate:DELete \n
		Snippet: driver.hardCopy.treport.item.template.delete(template = '1') \n
		This command deletes a test report template. \n
			:param template: String containing the name of the template.
		"""
		param = Conversions.value_to_quoted_str(template)
		self._core.io.write(f'HCOPy:TREPort:ITEM:TEMPlate:DELete {param}')

	def load(self, template: str) -> None:
		"""SCPI: HCOPy:TREPort:ITEM:TEMPlate:LOAD \n
		Snippet: driver.hardCopy.treport.item.template.load(template = '1') \n
		This command loads a test report template. \n
			:param template: String containing the name of the template.
		"""
		param = Conversions.value_to_quoted_str(template)
		self._core.io.write(f'HCOPy:TREPort:ITEM:TEMPlate:LOAD {param}')

	def save(self, template: str) -> None:
		"""SCPI: HCOPy:TREPort:ITEM:TEMPlate:SAVE \n
		Snippet: driver.hardCopy.treport.item.template.save(template = '1') \n
		This command saves a test report template in XML format. \n
			:param template: String containing the name of the template. The .xml file extension is added automatically.
		"""
		param = Conversions.value_to_quoted_str(template)
		self._core.io.write(f'HCOPy:TREPort:ITEM:TEMPlate:SAVE {param}')

	def clone(self) -> 'TemplateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TemplateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
