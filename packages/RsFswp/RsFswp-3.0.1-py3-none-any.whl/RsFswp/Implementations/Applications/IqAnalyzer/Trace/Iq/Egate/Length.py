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
		"""SCPI: TRACe:IQ:EGATe:LENGth \n
		Snippet: driver.applications.iqAnalyzer.trace.iq.egate.length.set(length = 1) \n
		This command defines the gate length for gated measurements with the I/Q analyzer. \n
			:param length: numeric value Max = (440 MS * sample rate/200MHz) -1 pretrigger samples defined by TRACe:IQ:SET; sample rate defined by method RsFswp.Applications.IqAnalyzer.Trace.Iq.SymbolRate.set) Range: 1…Max (samples)
		"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'TRACe:IQ:EGATe:LENGth {param}')

	def get(self) -> int:
		"""SCPI: TRACe:IQ:EGATe:LENGth \n
		Snippet: value: int = driver.applications.iqAnalyzer.trace.iq.egate.length.get() \n
		This command defines the gate length for gated measurements with the I/Q analyzer. \n
			:return: length: No help available"""
		response = self._core.io.query_str(f'TRACe:IQ:EGATe:LENGth?')
		return Conversions.str_to_int(response)
