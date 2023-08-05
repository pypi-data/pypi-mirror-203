from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TpiSampleCls:
	"""TpiSample commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tpiSample", core, parent)

	def get(self) -> float:
		"""SCPI: TRACe:IQ:TPISample \n
		Snippet: value: float = driver.applications.iqAnalyzer.trace.iq.tpiSample.get() \n
		This command queries the time offset between the sample start and the trigger event (trigger point in sample = TPIS) .
		Since the R&S FSWP usually samples with a much higher sample rate than the specific application actually requires, the
		trigger point determined internally is much more precise than the one determined from the (downsampled) data in the
		application. Thus, the TPIS indicates the offset between the sample start and the actual trigger event. This value can
		only be determined in triggered measurements using external or IFPower triggers, otherwise the value is 0. \n
			:return: tpis: numeric value Unit: s"""
		response = self._core.io.query_str(f'TRACe:IQ:TPISample?')
		return Conversions.str_to_float(response)
