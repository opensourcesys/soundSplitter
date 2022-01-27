# -*- coding: UTF-8 -*-
# Sound Splitter add-on
# Originally part of Tony's Enhancements add-on
# Sound Splitter copyright 2022 Joseph Lee
# Tony's Enhancements copyright (C) 2019 Tony Malykh
#This file is covered by the GNU General Public License.
#See the file LICENSE for more details.

import addonHandler
import api
import bisect
import collections
import config
import controlTypes
import core
import copy
import ctypes
from ctypes import create_string_buffer, byref
import documentBase
import editableText
import globalPluginHandler
import gui
from gui import guiHelper, nvdaControls
from gui.settingsDialogs import SettingsPanel
import html
import inputCore
import itertools
import json
import keyboardHandler
import locationHelper
from logHandler import log
import math
import mouseHandler
import NVDAHelper
from NVDAObjects import behaviors, NVDAObject
from NVDAObjects.IAccessible import IAccessible
from NVDAObjects.UIA import UIA
from NVDAObjects.window import winword
import nvwave
import operator
import os
import re
from scriptHandler import script, willSayAllResume
import speech
from speech.priorities import SpeechPriority
import string
import struct
import textInfos
import threading
import time
import tones
import types
import ui
import watchdog
import wave
import winUser
import wx

winmm = ctypes.windll.winmm

module = "soundSplitter"
def initConfiguration():
    confspec = {
        "nvdaVolume" : "integer( default=100, min=0, max=100)",
        "appsVolume" : "integer( default=100, min=0, max=100)",
        "soundSplitLeft" : "boolean( default=False)",
        "soundSplit" : "boolean( default=False)",
    }
    config.conf.spec[module] = confspec

def getConfig(key):
    value = config.conf[module][key]
    return value
def setConfig(key, value):
    config.conf[module][key] = value



addonHandler.initTranslation()
initConfiguration()



class SettingsDialog(SettingsPanel):
    # Translators: Title for the settings dialog
    title = _("Sound Splitter")

    def makeSettings(self, settingsSizer):
        sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

      # NVDA volume slider
        sizer=wx.BoxSizer(wx.HORIZONTAL)
        # Translators: slider to select NVDA  volume
        label=wx.StaticText(self,wx.ID_ANY,label=_("NVDA volume"))
        slider=wx.Slider(self, wx.NewId(), minValue=0,maxValue=100)
        slider.SetValue(getConfig("nvdaVolume"))
        sizer.Add(label)
        sizer.Add(slider)
        settingsSizer.Add(sizer)
        self.nvdaVolumeSlider = slider
      # Apps  volume slider
        sizer=wx.BoxSizer(wx.HORIZONTAL)
        # Translators: slider to select Apps   volume
        label=wx.StaticText(self,wx.ID_ANY,label=_("Applications volume"))
        slider=wx.Slider(self, wx.NewId(), minValue=0,maxValue=100)
        slider.SetValue(getConfig("appsVolume"))
        sizer.Add(label)
        sizer.Add(slider)
        settingsSizer.Add(sizer)
        self.appsVolumeSlider = slider
      # checkbox Enable sound split
        # Translators: Checkbox for sound split
        label = _("Split NVDA sound and applications' sounds into left and right channels.")
        self.soundSplitCheckbox = sHelper.addItem(wx.CheckBox(self, label=label))
        self.soundSplitCheckbox.Value = getConfig("soundSplit")
      # checkbox switch left and rright during sound split
        # Translators: Checkbox for switching left and right sound split
        label = _("Switch left and right during sound split.")
        self.soundSplitLeftCheckbox = sHelper.addItem(wx.CheckBox(self, label=label))
        self.soundSplitLeftCheckbox.Value = getConfig("soundSplitLeft")

    def onSave(self):

        setConfig("nvdaVolume", self.nvdaVolumeSlider.Value)
        setConfig("appsVolume", self.appsVolumeSlider.Value)
        setConfig("soundSplit", self.soundSplitCheckbox.Value)
        setConfig("soundSplitLeft", self.soundSplitLeftCheckbox.Value)
        updateSoundSplitterMonitorThread()


originalWaveOpen = None

def preWaveOpen(selfself, *args, **kwargs):
    global originalWaveOpen
    result = originalWaveOpen(selfself, *args, **kwargs)
    volume = getConfig("nvdaVolume")
    volume2 = int(0xFFFF * (volume / 100))
    if not getConfig("soundSplit"):
        volume2 = volume2 | (volume2 << 16)
    else:
        if getConfig("soundSplitLeft"):
            pass
        else:
            volume2 = (volume2 << 16)
    winmm.waveOutSetVolume(selfself._waveout, volume2)
    return result

def setAppsVolume(volumes=None):
    from . pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, IChannelAudioVolume
    if volumes is not None:
        leftVolume, rightVolume = volumes
    else:
        volume = getConfig("appsVolume")
        if getConfig("soundSplit"):
            if getConfig("soundSplitLeft"):
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
        if s.Process is not None and 'nvda' in s.Process.name().lower():
            continue
        channelVolume = s._ctl.QueryInterface(IChannelAudioVolume)
        if channelVolume.GetChannelCount() == 2:
            channelVolume.SetChannelVolume(0, leftVolume, None)
            channelVolume.SetChannelVolume(1, rightVolume, None)

soundSplitterMonitorCounter = 0
def soundSplitterMonitorThread(localSoundSplitterMonitorCounter):
    global soundSplitterMonitorCounter
    while localSoundSplitterMonitorCounter == soundSplitterMonitorCounter:
        if not getConfig("soundSplit"):
            return
        setAppsVolume()
        #time.sleep(1)
        yield 1000

def updateSoundSplitterMonitorThread(exit=False):
    global soundSplitterMonitorCounter
    soundSplitterMonitorCounter += 1
    if exit:
        setAppsVolume((100,100))
        return
    ss = getConfig("soundSplit")
    if ss:
        executeAsynchronously(soundSplitterMonitorThread(soundSplitterMonitorCounter))
    else:
        setAppsVolume()

def executeAsynchronously(gen):
    """
    This function executes a generator-function in such a manner, that allows updates from the operating system to be processed during execution.
    For an example of such generator function, please see GlobalPlugin.script_editJupyter.
    Specifically, every time the generator function yilds a positive number,, the rest of the generator function will be executed
    from within wx.CallLater() call.
    If generator function yields a value of 0, then the rest of the generator function
    will be executed from within wx.CallAfter() call.
    This allows clear and simple expression of the logic inside the generator function, while still allowing NVDA to process update events from the operating system.
    Essentially the generator function will be paused every time it calls yield, then the updates will be processed by NVDA and then the remainder of generator function will continue executing.
    """
    if not isinstance(gen, types.GeneratorType):
        raise Exception("Generator function required")
    try:
        value = gen.__next__()
    except StopIteration:
        return
    l = lambda gen=gen: executeAsynchronously(gen)
    core.callLater(value, executeAsynchronously, gen)


updateSoundSplitterMonitorThread()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    scriptCategory = _("Sound Splitter")

    def __init__(self, *args, **kwargs):
        super(GlobalPlugin, self).__init__(*args, **kwargs)
        self.createMenu()
        self.injectHooks()

    def createMenu(self):
        gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(SettingsDialog)

    def terminate(self):
        updateSoundSplitterMonitorThread(exit=True)
        self.removeHooks()
        gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(SettingsDialog)

    def injectHooks(self):
        global originalWaveOpen
        originalWaveOpen = nvwave.WavePlayer.open
        nvwave.WavePlayer.open = preWaveOpen

    def  removeHooks(self):
        global originalWaveOpen
        nvwave.WavePlayer.open = originalWaveOpen

    @script(description='Toggle sound split.', gestures=['kb:NVDA+Alt+S'])
    def script_toggleSoundSplit(self, gesture):
        ss = getConfig("soundSplit")
        ss = not ss
        msg = _("Sound split enabled") if ss else _("Sound split disabled")
        setConfig("soundSplit", False)
        def updateSoundSplit():
            setConfig("soundSplit", ss)
            updateSoundSplitterMonitorThread()
        #core.callLater(100, updateSoundSplit)
        updateSoundSplit()
        ui.message(msg)
