from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AlgorithmCls:
	"""Algorithm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("algorithm", core, parent)

	def set(self, algorithm: enums.SummaryMode) -> None:
		"""SCPI: [SENSe]:IQ:FFT:ALGorithm \n
		Snippet: driver.applications.iqAnalyzer.sense.iq.fft.algorithm.set(algorithm = enums.SummaryMode.AVERage) \n
		Defines the FFT calculation method. For more information see 'Basics on FFT'. \n
			:param algorithm: SINGle One FFT is calculated for the entire record length; if the FFT length is larger than the record length (see [SENSe:]IQ:FFT:LENGth and method RsFswp.Applications.IqAnalyzer.Trace.Iq.Rlength.set) , zeros are appended to the captured data. AVERage Several overlapping FFTs are calculated for each record; the results are averaged to determine the final FFT result for the record. The user-defined window length and window overlap are used (see [SENSe:]IQ:FFT:WINDow:LENGth and [SENSe:]IQ:FFT:WINDow:OVERlap) .
		"""
		param = Conversions.enum_scalar_to_str(algorithm, enums.SummaryMode)
		self._core.io.write(f'SENSe:IQ:FFT:ALGorithm {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SummaryMode:
		"""SCPI: [SENSe]:IQ:FFT:ALGorithm \n
		Snippet: value: enums.SummaryMode = driver.applications.iqAnalyzer.sense.iq.fft.algorithm.get() \n
		Defines the FFT calculation method. For more information see 'Basics on FFT'. \n
			:return: algorithm: No help available"""
		response = self._core.io.query_str(f'SENSe:IQ:FFT:ALGorithm?')
		return Conversions.str_to_scalar_enum(response, enums.SummaryMode)
