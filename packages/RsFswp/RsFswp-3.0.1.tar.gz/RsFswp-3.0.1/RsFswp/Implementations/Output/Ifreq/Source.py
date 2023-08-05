from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SourceCls:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, source: enums.Source, outputConnector=repcap.OutputConnector.Default) -> None:
		"""SCPI: OUTPut<up>:IF[:SOURce] \n
		Snippet: driver.output.ifreq.source.set(source = enums.Source.AM, outputConnector = repcap.OutputConnector.Default) \n
		Defines the type of signal available at one of the output connectors of the R&S FSWP. Note that you can use the audio
		frequency output only if the IF output source is 'Video'. \n
			:param source: IF The measured IF value is available at the IF/VIDEO/DEMOD output connector. VIDeo The displayed video signal (i.e. the filtered and detected IF signal, 200mV) is available at the IF/VIDEO/DEMOD output connector. This setting is required to provide demodulated audio frequencies at the output.
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(source, enums.Source)
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		self._core.io.write(f'OUTPut{outputConnector_cmd_val}:IF:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self, outputConnector=repcap.OutputConnector.Default) -> enums.Source:
		"""SCPI: OUTPut<up>:IF[:SOURce] \n
		Snippet: value: enums.Source = driver.output.ifreq.source.get(outputConnector = repcap.OutputConnector.Default) \n
		Defines the type of signal available at one of the output connectors of the R&S FSWP. Note that you can use the audio
		frequency output only if the IF output source is 'Video'. \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: source: IF The measured IF value is available at the IF/VIDEO/DEMOD output connector. VIDeo The displayed video signal (i.e. the filtered and detected IF signal, 200mV) is available at the IF/VIDEO/DEMOD output connector. This setting is required to provide demodulated audio frequencies at the output."""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		response = self._core.io.query_str(f'OUTPut{outputConnector_cmd_val}:IF:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.Source)
