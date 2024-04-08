# SoundSplitter/installTasks.py
# Copyright: 2022, Joseph Lee. 2023-2024, Luke Davis. Released under GPL V2.

# Provides needed routines during add-on installation and removal.
# Mostly checks compatibility.
# Routines are partly based on other add-ons,
# particularly Place Markers by Noelia Martinez (thanks add-on authors).

import addonHandler
addonHandler.initTranslation()


def onInstall():
	import gui
	import wx
	import winVersion
	import globalVars
	from buildVersion import version_year, version_major
	# Do not present dialog if minimal mode is set.
	# Sound Splitter requires Windows 10 21H2 or later.
	currentWinVer = winVersion.getWinVer()
	# Translators: title of the error dialog shown when trying to install the add-on in unsupported systems.
	# Unsupported systems include Windows versions earlier than 10 and unsupported feature updates.
	unsupportedWindowsReleaseTitle = _("Unsupported Windows release")
	minimumWinVer = winVersion.WIN10_21H2
	if currentWinVer < minimumWinVer:
		if not globalVars.appArgs.minimal:
			gui.messageBox(
				_(
					# Translators: Dialog text shown when trying to install the add-on on
					# releases earlier than minimum supported release.
					"You are using {releaseName} ({build}), a Windows release not supported by this add-on.\n"
					"This add-on requires {supportedReleaseName} ({supportedBuild}) or later."
				).format(
					releaseName=currentWinVer.releaseName,
					build=currentWinVer.build,
					supportedReleaseName=minimumWinVer.releaseName,
					supportedBuild=minimumWinVer.build
				), unsupportedWindowsReleaseTitle, wx.OK
			)
		raise RuntimeError("Attempting to install Sound Splitter on unsupported Windows release.")
	# Notify about sound split feature in 2024.2 versions of NVDA
	preRelease_featureIncludedMsg_top: str = _(
		# Translators: Part of a message shown before NVDA 2024.2 is released.
		"The sound split feature will be included in NVDA version 2024.2. "
		"It may already be available in your version, if you use alpha or beta releases of NVDA 2024.2."
	)
	featureIncludedMsg_top: str = _(
		# Translators: Part of a message shown after NVDA 2024.2 is released.
		"The sound split feature is now part of NVDA itself, as of NVDA 2024.2!"
	)
	featureIncludedMsg_body: str = _(
		# Translators: The remainder of the message shown on installation.
		"However, this is only helpful if you use WASAPI as your sound interface preference."
		" (NVDA menu, Preferences, Settings, Advanced.)\n"
		"While WASAPI is the default in modern versions of NVDA, this add-on is still necessary if you "
		"choose to, or must, use sound split without WASAPI. The add-on will be maintained for that purpose, "
		"and for use in older versions of NVDA.\n"
		"If you only plan to use WASAPI, you may remove the add-on from copies of NVDA 2024.2, "
		"and configure the built-in feature."
	)
	if (  # NVDA less than 2024.2
		version_year < 2024
		or (version_year == 2024 and version_major < 2)
	):
		preInstallMsg: str = f"{preRelease_featureIncludedMsg_top}\n{featureIncludedMsg_body}"
	else:  # NVDA 2024.2 and up
		preInstallMsg: str = f"{featureIncludedMsg_top}\n{featureIncludedMsg_body}"
	gui.messageBox(
		preInstallMsg,
		_(
			# Translators: title of a dialog notifying about upcoming WASAPI sound split support.
			"Sound Splitter Alert!"
		), wx.OK | wx.ICON_WARNING
	)
