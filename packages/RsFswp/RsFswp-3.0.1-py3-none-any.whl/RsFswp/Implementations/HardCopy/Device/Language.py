from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LanguageCls:
	"""Language commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("language", core, parent)

	def set(self, language: enums.PictureFormat) -> None:
		"""SCPI: HCOPy:DEVice:LANGuage \n
		Snippet: driver.hardCopy.device.language.set(language = enums.PictureFormat.BMP) \n
		This command selects the file format for a print job or to store a screenshot to a file. \n
			:param language: GDI Graphics Device Interface Default format for output to a printer configured under Windows. Must be selected for output to the printer interface. Can be used for output to a file. The printer driver configured under Windows is used to generate a printer-specific file format. BMP | JPG | PNG | PDF | SVG Data format for output to files
		"""
		param = Conversions.enum_scalar_to_str(language, enums.PictureFormat)
		self._core.io.write(f'HCOPy:DEVice:LANGuage {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PictureFormat:
		"""SCPI: HCOPy:DEVice:LANGuage \n
		Snippet: value: enums.PictureFormat = driver.hardCopy.device.language.get() \n
		This command selects the file format for a print job or to store a screenshot to a file. \n
			:return: language: GDI Graphics Device Interface Default format for output to a printer configured under Windows. Must be selected for output to the printer interface. Can be used for output to a file. The printer driver configured under Windows is used to generate a printer-specific file format. BMP | JPG | PNG | PDF | SVG Data format for output to files"""
		response = self._core.io.query_str(f'HCOPy:DEVice:LANGuage?')
		return Conversions.str_to_scalar_enum(response, enums.PictureFormat)
