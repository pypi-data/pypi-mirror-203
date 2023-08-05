from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExecuteCls:
	"""Execute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("execute", core, parent)

	def set(self, application_group: str, display_name: str) -> None:
		"""SCPI: SYSTem:PLUGin:APPStarter:EXECute \n
		Snippet: driver.system.plugin.appStarter.execute.set(application_group = '1', display_name = '1') \n
		Starts the specified application directly on the R&S FSW. Note that for data security reasons, executable applications
		cannot be added to the Application Starter remotely. Only applications added to the firmware manually in advance can be
		executed remotely. \n
			:param application_group: 'External' | 'User' The group (tab) of applications in the Application Starter that the application belongs to. 'External' External Applications 'User' User Applications
			:param display_name: Name of the application in the Application Starter
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('application_group', application_group, DataType.String), ArgSingle('display_name', display_name, DataType.String))
		self._core.io.write(f'SYSTem:PLUGin:APPStarter:EXECute {param}'.rstrip())
