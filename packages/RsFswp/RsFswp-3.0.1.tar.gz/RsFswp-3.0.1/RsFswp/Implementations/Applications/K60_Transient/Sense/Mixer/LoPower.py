from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LoPowerCls:
	"""LoPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("loPower", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: [SENSe]:MIXer:LOPower \n
		Snippet: driver.applications.k60Transient.sense.mixer.loPower.set(level = 1.0) \n
		No command help available \n
			:param level: No help available
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SENSe:MIXer:LOPower {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:LOPower \n
		Snippet: value: float = driver.applications.k60Transient.sense.mixer.loPower.get() \n
		No command help available \n
			:return: level: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:LOPower?')
		return Conversions.str_to_float(response)
