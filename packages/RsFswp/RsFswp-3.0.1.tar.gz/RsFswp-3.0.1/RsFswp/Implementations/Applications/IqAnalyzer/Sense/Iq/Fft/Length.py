from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LengthCls:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, length: int) -> None:
		"""SCPI: [SENSe]:IQ:FFT:LENGth \n
		Snippet: driver.applications.iqAnalyzer.sense.iq.fft.length.set(length = 1) \n
		Defines the number of frequency points determined by each FFT calculation. The more points are used, the higher the
		resolution in the spectrum becomes, but the longer the calculation takes. \n
			:param length: integer value Range: 3 to 524288
		"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'SENSe:IQ:FFT:LENGth {param}')

	def get(self) -> int:
		"""SCPI: [SENSe]:IQ:FFT:LENGth \n
		Snippet: value: int = driver.applications.iqAnalyzer.sense.iq.fft.length.get() \n
		Defines the number of frequency points determined by each FFT calculation. The more points are used, the higher the
		resolution in the spectrum becomes, but the longer the calculation takes. \n
			:return: length: No help available"""
		response = self._core.io.query_str(f'SENSe:IQ:FFT:LENGth?')
		return Conversions.str_to_int(response)
