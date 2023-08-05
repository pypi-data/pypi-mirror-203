from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CountCls:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, repetitions: int) -> None:
		"""SCPI: TRACe:IQ:FILE:REPetition:COUNt \n
		Snippet: driver.applications.iqAnalyzer.trace.iq.file.repetition.count.set(repetitions = 1) \n
		Determines how often the data stream is repeatedly copied in the I/Q data memory. If the available memory is not
		sufficient for the specified number of repetitions, the largest possible number of complete data streams is used. \n
			:param repetitions: integer
		"""
		param = Conversions.decimal_value_to_str(repetitions)
		self._core.io.write(f'TRACe:IQ:FILE:REPetition:COUNt {param}')

	def get(self) -> int:
		"""SCPI: TRACe:IQ:FILE:REPetition:COUNt \n
		Snippet: value: int = driver.applications.iqAnalyzer.trace.iq.file.repetition.count.get() \n
		Determines how often the data stream is repeatedly copied in the I/Q data memory. If the available memory is not
		sufficient for the specified number of repetitions, the largest possible number of complete data streams is used. \n
			:return: repetitions: No help available"""
		response = self._core.io.query_str(f'TRACe:IQ:FILE:REPetition:COUNt?')
		return Conversions.str_to_int(response)
