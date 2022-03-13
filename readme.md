# Sound Splitter

* Authors: Joseph Lee and contributors
* Download [stable version][1]
* NVDA compatibility: 2021.3 and later

This add-on, partly based on Tony's Enhancements by Tony Malykh, adds the ability to split audio from NVDA and other sounds onto separate audio channels.

Note: this add-on is not intended to be used in secure screens.

## Commands:

* Alt+NvDA+S: toggle sound splitter between enabled with NVDA on the right channel, NVDA on the left channel, or disabled.

## Sound Splitter settings

You can configure add-on settings from NVDA menu/Preferences/Settings/Sound Splitter category.

* Split NVDA sound and applications' sounds into left and right channels: checkinb this checkbox will enable sound splitting feature.
* Switch left and right during sound split: by default, NVDA will be heard through the right channel if sound splitting is on. You can instead hear NVDA through the left channel by checking this checkbox.

## Version 22.03

* NVDA 2021.3 or later is required.
* Improved security by not loading the add-on when NVDA is running in secure mode.
* Updated psutil dependency to 5.9.0.
* Changed sound splitter toggle command (Alt+NVDA+S) to toggle between NVDA on the right channel, on the left channel, or sound splitter disabled.

## Version 22.02.1

* Fixed NVDA and app audio not being restored to both audio channels after the add-on is disabled or uninstalled.

## Version 22.02

* Initial version based on Tony Malykh's Tony's Enhancements add-on.

[1]: https://addons.nvda-project.org/files/get.php?file=soundsplitter
