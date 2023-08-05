from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AcquireCls:
	"""Acquire commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("acquire", core, parent)

	def set(self, meas_type: enums.CorrectionMeasType) -> None:
		"""SCPI: [SENSe]:CORRection:COLLect[:ACQuire] \n
		Snippet: driver.sense.correction.collect.acquire.set(meas_type = enums.CorrectionMeasType.OPEN) \n
		No command help available \n
			:param meas_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(meas_type, enums.CorrectionMeasType)
		self._core.io.write(f'SENSe:CORRection:COLLect:ACQuire {param}')
