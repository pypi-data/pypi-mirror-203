from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhaseCls:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:TRACking:PHASe \n
		Snippet: driver.applications.k9X11Ad.sense.tracking.phase.set(state = False) \n
		Activates or deactivates the compensation for phase drifts. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on. The measurement results are compensated for phase drifts on a per-symbol basis.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:TRACking:PHASe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:TRACking:PHASe \n
		Snippet: value: bool = driver.applications.k9X11Ad.sense.tracking.phase.get() \n
		Activates or deactivates the compensation for phase drifts. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on. The measurement results are compensated for phase drifts on a per-symbol basis."""
		response = self._core.io.query_str(f'SENSe:TRACking:PHASe?')
		return Conversions.str_to_bool(response)
