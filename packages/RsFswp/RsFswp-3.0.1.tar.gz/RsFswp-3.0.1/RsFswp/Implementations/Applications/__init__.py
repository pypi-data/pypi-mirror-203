from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApplicationsCls:
	"""Applications commands group definition. 1237 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("applications", core, parent)

	@property
	def k70_Vsa(self):
		"""k70_Vsa commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_k70_Vsa'):
			from .K70_Vsa import K70_VsaCls
			self._k70_Vsa = K70_VsaCls(self._core, self._cmd_group)
		return self._k70_Vsa

	@property
	def iqAnalyzer(self):
		"""iqAnalyzer commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqAnalyzer'):
			from .IqAnalyzer import IqAnalyzerCls
			self._iqAnalyzer = IqAnalyzerCls(self._core, self._cmd_group)
		return self._iqAnalyzer

	@property
	def k7_AnalogDemod(self):
		"""k7_AnalogDemod commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_k7_AnalogDemod'):
			from .K7_AnalogDemod import K7_AnalogDemodCls
			self._k7_AnalogDemod = K7_AnalogDemodCls(self._core, self._cmd_group)
		return self._k7_AnalogDemod

	@property
	def k30_NoiseFigure(self):
		"""k30_NoiseFigure commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_k30_NoiseFigure'):
			from .K30_NoiseFigure import K30_NoiseFigureCls
			self._k30_NoiseFigure = K30_NoiseFigureCls(self._core, self._cmd_group)
		return self._k30_NoiseFigure

	@property
	def k40_PhaseNoise(self):
		"""k40_PhaseNoise commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_k40_PhaseNoise'):
			from .K40_PhaseNoise import K40_PhaseNoiseCls
			self._k40_PhaseNoise = K40_PhaseNoiseCls(self._core, self._cmd_group)
		return self._k40_PhaseNoise

	@property
	def k50_Spurious(self):
		"""k50_Spurious commands group. 16 Sub-classes, 0 commands."""
		if not hasattr(self, '_k50_Spurious'):
			from .K50_Spurious import K50_SpuriousCls
			self._k50_Spurious = K50_SpuriousCls(self._core, self._cmd_group)
		return self._k50_Spurious

	@property
	def k60_Transient(self):
		"""k60_Transient commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_k60_Transient'):
			from .K60_Transient import K60_TransientCls
			self._k60_Transient = K60_TransientCls(self._core, self._cmd_group)
		return self._k60_Transient

	def clone(self) -> 'ApplicationsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ApplicationsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
