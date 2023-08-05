from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OptimizeCls:
	"""Optimize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("optimize", core, parent)

	def set(self, mode: enums.SweepOptimizeB) -> None:
		"""SCPI: [SENSe]:SWEep:OPTimize \n
		Snippet: driver.sense.sweep.optimize.set(mode = enums.SweepOptimizeB.AUTO) \n
		In FFT mode, several FFT analysis steps are required to cover the entire measurement span. The span which is covered by
		one FFT analysis step is called subspan. The subspan cannot be defined directly, but it can be optimized according to
		measurement requirements. Optimization parameters in FFT mode
			Table Header: Optimization mode / Description \n
			- DYNamic / Optimizes the dynamic range by using the narrowest possible subspan (depending on the RBW) . The autorange function for the internal IF gain calculation is activated to obtain the best control range for the A/D converter.
			- SPEed / Optimizes the sweep rate by using the widest possible subspan (depending on the RBW) . The autorange function for the internal IF gain calculation is deactivated. (Note: set the reference level accordingly to optimize the control range for the A/D converter) . It is recommended that you set the 'Sweep Time' to 'Auto' to optimize the sweep rate.
			- TRANsient / Recommended mode for measurements on highly transient signals in spectrum analysis. It increases the measurement speed with a trade off in dynamic range. Only available for R&S FSW67/85 models.
			- AUTO / Uses a medium-sized subspan to obtain a compromise between a large dynamic range and a fast sweep rate. The autorange function for the internal IF gain calculation is activated to obtain the best control range for the A/D converter.
		Note: FFT mode and external mixers (R&S FSW-B21) The subspan optimization modes 'Dynamic' and 'Auto' include automatic
		suppression of unwanted mixing products. Thus, when using external mixers (R&S FSW-B21) , use the 'Speed' mode to obtain
		similar results in FFT mode as in frequency sweep mode. Zero span mode For zero span measurements, the optimization mode
		defines the selection of the A/D converter prefilter. Optimization parameters in zero span mode
			Table Header: Optimization mode / Description \n
			- DYNamic / The narrowest filter possible (depending on the RBW) is used.
			- SPEed / The widest filter possible (depending on the RBW) is used.
			- AUTO / A medium-sized prefilter is used.
		Note: EMI measurements For EMI measurements (using R&S FSW-K54) , 'Dynamic' mode is not supported. 'Auto' mode always
		uses 'Speed' optimization. \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SweepOptimizeB)
		self._core.io.write(f'SENSe:SWEep:OPTimize {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SweepOptimizeB:
		"""SCPI: [SENSe]:SWEep:OPTimize \n
		Snippet: value: enums.SweepOptimizeB = driver.sense.sweep.optimize.get() \n
		In FFT mode, several FFT analysis steps are required to cover the entire measurement span. The span which is covered by
		one FFT analysis step is called subspan. The subspan cannot be defined directly, but it can be optimized according to
		measurement requirements. Optimization parameters in FFT mode
			Table Header: Optimization mode / Description \n
			- DYNamic / Optimizes the dynamic range by using the narrowest possible subspan (depending on the RBW) . The autorange function for the internal IF gain calculation is activated to obtain the best control range for the A/D converter.
			- SPEed / Optimizes the sweep rate by using the widest possible subspan (depending on the RBW) . The autorange function for the internal IF gain calculation is deactivated. (Note: set the reference level accordingly to optimize the control range for the A/D converter) . It is recommended that you set the 'Sweep Time' to 'Auto' to optimize the sweep rate.
			- TRANsient / Recommended mode for measurements on highly transient signals in spectrum analysis. It increases the measurement speed with a trade off in dynamic range. Only available for R&S FSW67/85 models.
			- AUTO / Uses a medium-sized subspan to obtain a compromise between a large dynamic range and a fast sweep rate. The autorange function for the internal IF gain calculation is activated to obtain the best control range for the A/D converter.
		Note: FFT mode and external mixers (R&S FSW-B21) The subspan optimization modes 'Dynamic' and 'Auto' include automatic
		suppression of unwanted mixing products. Thus, when using external mixers (R&S FSW-B21) , use the 'Speed' mode to obtain
		similar results in FFT mode as in frequency sweep mode. Zero span mode For zero span measurements, the optimization mode
		defines the selection of the A/D converter prefilter. Optimization parameters in zero span mode
			Table Header: Optimization mode / Description \n
			- DYNamic / The narrowest filter possible (depending on the RBW) is used.
			- SPEed / The widest filter possible (depending on the RBW) is used.
			- AUTO / A medium-sized prefilter is used.
		Note: EMI measurements For EMI measurements (using R&S FSW-K54) , 'Dynamic' mode is not supported. 'Auto' mode always
		uses 'Speed' optimization. \n
			:return: mode: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:OPTimize?')
		return Conversions.str_to_scalar_enum(response, enums.SweepOptimizeB)
