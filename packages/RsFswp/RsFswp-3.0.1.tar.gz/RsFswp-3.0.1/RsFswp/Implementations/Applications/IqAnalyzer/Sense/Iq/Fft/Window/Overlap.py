from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OverlapCls:
	"""Overlap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("overlap", core, parent)

	def set(self, overlap: float) -> None:
		"""SCPI: [SENSe]:IQ:FFT:WINDow:OVERlap \n
		Snippet: driver.applications.iqAnalyzer.sense.iq.fft.window.overlap.set(overlap = 1.0) \n
		Defines the part of a single FFT window that is re-calculated by the next FFT calculation. \n
			:param overlap: double value Percentage rate Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(overlap)
		self._core.io.write(f'SENSe:IQ:FFT:WINDow:OVERlap {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:IQ:FFT:WINDow:OVERlap \n
		Snippet: value: float = driver.applications.iqAnalyzer.sense.iq.fft.window.overlap.get() \n
		Defines the part of a single FFT window that is re-calculated by the next FFT calculation. \n
			:return: overlap: No help available"""
		response = self._core.io.query_str(f'SENSe:IQ:FFT:WINDow:OVERlap?')
		return Conversions.str_to_float(response)
