from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ControlCls:
	"""Control commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("control", core, parent)

	def set(self, repetition: enums.HardcopyHeader, line=repcap.Line.Default) -> None:
		"""SCPI: HCOPy:TREPort:ITEM:HEADer:LINE<li>:CONTrol \n
		Snippet: driver.hardCopy.treport.item.header.line.control.set(repetition = enums.HardcopyHeader.ALWays, line = repcap.Line.Default) \n
		No command help available \n
			:param repetition: No help available
			:param line: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Line')
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.HardcopyHeader)
		line_cmd_val = self._cmd_group.get_repcap_cmd_value(line, repcap.Line)
		self._core.io.write(f'HCOPy:TREPort:ITEM:HEADer:LINE{line_cmd_val}:CONTrol {param}')

	# noinspection PyTypeChecker
	def get(self, line=repcap.Line.Default) -> enums.HardcopyHeader:
		"""SCPI: HCOPy:TREPort:ITEM:HEADer:LINE<li>:CONTrol \n
		Snippet: value: enums.HardcopyHeader = driver.hardCopy.treport.item.header.line.control.get(line = repcap.Line.Default) \n
		No command help available \n
			:param line: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Line')
			:return: repetition: No help available"""
		line_cmd_val = self._cmd_group.get_repcap_cmd_value(line, repcap.Line)
		response = self._core.io.query_str(f'HCOPy:TREPort:ITEM:HEADer:LINE{line_cmd_val}:CONTrol?')
		return Conversions.str_to_scalar_enum(response, enums.HardcopyHeader)
