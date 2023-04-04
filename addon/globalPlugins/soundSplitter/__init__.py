# -*- coding: UTF-8 -*-
# Sound Splitter add-on
# Originally part of Tony's Enhancements add-on
# Copyright: 2022, Joseph Lee. 2023, Luke Davis.
# Tony's Enhancements copyright (C) 2019 Tony Malykh
# This file is covered by the GNU General Public License version 2.
# See the file LICENSE for more details.

# Joseph Lee: completely rewritten to make it compliant with NVDA Core expectations
# and to align with many other add-ons.
# This is evident in config access and the ability to handle config profile switches.

import ctypes
import types
import wx
import os

import addonHandler
import globalPluginHandler
import config
import core
import globalVars
import gui
from gui.settingsDialogs import SettingsPanel
import nvwave
from scriptHandler import script
import ui

winmm = ctypes.windll.winmm

# Sound Splitter config variables and settings UI.
config.conf.spec["soundSplitter"] = {
	"soundSplitLeft": "boolean( default=False)",
	"soundSplit": "boolean( default=False)",
}


# Security: disable alltogether in secure mode.
def disableInSecureMode(cls):
	return globalPluginHandler.GlobalPlugin if globalVars.appArgs.secure else cls


addonHandler.initTranslation()


class SettingsDialog(SettingsPanel):
	# Translators: Title for the settings dialog
	title = _("Sound Splitter")

	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# checkbox Enable sound split
		# Translators: Checkbox for sound split
		label = _("&Split NVDA sound and applications' sounds into left and right channels")
		self.soundSplitCheckbox = sHelper.addItem(wx.CheckBox(self, label=label))
		self.soundSplitCheckbox.Value = config.conf["soundSplitter"]["soundSplit"]
		# checkbox switch left and right during sound split
		# Translators: Checkbox for switching left and right sound split
		label = _("Switch &left and right during sound split")
		self.soundSplitLeftCheckbox = sHelper.addItem(wx.CheckBox(self, label=label))
		self.soundSplitLeftCheckbox.Value = config.conf["soundSplitter"]["soundSplitLeft"]

	def onSave(self):
		config.conf["soundSplitter"]["soundSplit"] = self.soundSplitCheckbox.Value
		config.conf["soundSplitter"]["soundSplitLeft"] = self.soundSplitLeftCheckbox.Value
		updateSoundSplitterMonitorThread()


# Sound Splitter mechanics and internal functions.
originalWaveOpen = None


def preWaveOpen(selfself, *args, **kwargs):
	global originalWaveOpen
	result = originalWaveOpen(selfself, *args, **kwargs)
	# All we care about is splitting sounds, so set volume to 100 percent always.
	volume = 100
	volume2 = int(0xFFFF * (volume / 100))
	if not config.conf["soundSplitter"]["soundSplit"]:
		volume2 = volume2 | (volume2 << 16)
	else:
		if config.conf["soundSplitter"]["soundSplitLeft"]:
			pass
		else:
			volume2 = (volume2 << 16)
	winmm.waveOutSetVolume(selfself._waveout, volume2)
	return result


def setAppsVolume(volumes=None, exit=False):
	from . pycaw.pycaw import AudioUtilities, IChannelAudioVolume
	if volumes is not None:
		leftVolume, rightVolume = volumes
	else:
		volume = 100
		if config.conf["soundSplitter"]["soundSplit"]:
			if config.conf["soundSplitter"]["soundSplitLeft"]:
				leftVolume = 0
				rightVolume = volume
			else:
				leftVolume = volume
				rightVolume = 0
		else:
			leftVolume = rightVolume = volume

	leftVolume /= 100.0
	rightVolume /= 100.0

	audioSessions = AudioUtilities.GetAllSessions()
	for s in audioSessions:
		if (
			not exit
			and s.Process is not None
			and s.ProcessId == os.getpid()  # FixMe should this be here? (Luke)
		):
			continue
		channelVolume = s._ctl.QueryInterface(IChannelAudioVolume)
		if channelVolume.GetChannelCount() == 2:
			channelVolume.SetChannelVolume(0, leftVolume, None)
			channelVolume.SetChannelVolume(1, rightVolume, None)


soundSplitterMonitorCounter = 0


def soundSplitterMonitorThread(localSoundSplitterMonitorCounter):
	global soundSplitterMonitorCounter
	while localSoundSplitterMonitorCounter == soundSplitterMonitorCounter:
		if not config.conf["soundSplitter"]["soundSplit"]:
			return
		setAppsVolume()
		yield 1000


def updateSoundSplitterMonitorThread(exit=False):
	# Ignore all this if secure flag is in effect.
	if globalVars.appArgs.secure:
		return
	global soundSplitterMonitorCounter
	soundSplitterMonitorCounter += 1
	if exit:
		setAppsVolume((100, 100), exit=True)
		return
	ss = config.conf["soundSplitter"]["soundSplit"]
	if ss:
		executeAsynchronously(soundSplitterMonitorThread(soundSplitterMonitorCounter))
	else:
		setAppsVolume()


def executeAsynchronously(gen):
	"""This function executes a generator in such a manner, that allows updates
	from the operating system to be processed during execution.
	Specifically, every time the generator yields a positive number,,
	the rest of the generator function will be executed from within wx.CallLater().
	If the generator yields a value of 0, then the rest of the generator
	will be executed from within wx.CallAfter().
	This allows clear and simple expression of the logic inside the generator body,
	while still allowing NVDA to process update events from the operating system.
	Essentially the generator will be paused every time it calls yield, then the updates will be
	processed by NVDA and then the remainder of generator function will continue executing.
	"""
	if not isinstance(gen, types.GeneratorType):
		raise Exception("A generator is required")
	try:
		value = gen.__next__()
	except StopIteration:
		return
	# FixMe: The below line may require a rewrite as multiple Flake8/lint errors are raised.
	l = lambda gen=gen: executeAsynchronously(gen)  # NOQA
	core.callLater(value, executeAsynchronously, gen)


updateSoundSplitterMonitorThread()


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = _("Sound Splitter")

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		global originalWaveOpen
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(SettingsDialog)
		config.post_configProfileSwitch.register(self.handleConfigProfileSwitch)
		config.post_configReset.register(self.reload)
		originalWaveOpen = nvwave.WavePlayer.open
		nvwave.WavePlayer.open = preWaveOpen

	def terminate(self):
		global originalWaveOpen
		config.post_configProfileSwitch.unregister(self.handleConfigProfileSwitch)
		config.post_configReset.unregister(self.reload)
		updateSoundSplitterMonitorThread(exit=True)
		nvwave.WavePlayer.open = originalWaveOpen
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(SettingsDialog)
		super().terminate()  # Probably unnecessary but maybe needed in the future

	def handleConfigProfileSwitch(self):
		updateSoundSplitterMonitorThread()

	def reload(self, factoryDefaults=False):
		updateSoundSplitterMonitorThread()

	@script(
		# Translators: input help message for toggle sound splitter command.
		description=_("Toggle sound split"),
		gesture="kb:NVDA+Alt+S"
	)
	def script_toggleSoundSplit(self, gesture):
		soundSplit = config.conf["soundSplitter"]["soundSplit"]
		soundSplitLeft = config.conf["soundSplitter"]["soundSplitLeft"]
		if not soundSplit:
			soundSplit = True
			soundSplitLeft = False
			# Translators: presented when toggling sound splitter.
			msg = _("Sound split enabled, NVDA on the right")
		elif soundSplit and not soundSplitLeft:
			soundSplitLeft = True
			# Translators: presented when toggling sound splitter.
			msg = _("Sound split enabled, NVDA on the left")
		elif soundSplit and soundSplitLeft:
			soundSplit = False
			soundSplitLeft = False
			# Translators: presented when toggling sound splitter.
			msg = _("Sound split disabled")
		config.conf["soundSplitter"]["soundSplit"] = soundSplit
		config.conf["soundSplitter"]["soundSplitLeft"] = soundSplitLeft
		updateSoundSplitterMonitorThread()
		ui.message(msg)
