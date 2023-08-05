from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WfilterCls:
	"""Wfilter commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wfilter", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: TRACe:IQ:WFILter \n
		Snippet: driver.applications.iqAnalyzer.trace.iq.wfilter.set(state = False) \n
		Activates a 200 MHz filter before the A/D converter, thus restricting the processed bandwidth to 200 MHz while using the
		wideband processing path in the R&S FSWP. For prerequisites see manual operation. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'TRACe:IQ:WFILter {param}')

	def get(self) -> bool:
		"""SCPI: TRACe:IQ:WFILter \n
		Snippet: value: bool = driver.applications.iqAnalyzer.trace.iq.wfilter.get() \n
		Activates a 200 MHz filter before the A/D converter, thus restricting the processed bandwidth to 200 MHz while using the
		wideband processing path in the R&S FSWP. For prerequisites see manual operation. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'TRACe:IQ:WFILter?')
		return Conversions.str_to_bool(response)
