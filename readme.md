# Sound Splitter

* Authors: Luke Davis, Joseph Lee and contributors
* Download [stable version][1]
* NVDA compatibility: 2022.4 and beyond

This add-on, partly based on Tony's Enhancements by Tony Malykh, adds the ability to split audio from NVDA and other sounds onto separate audio channels.

Note: this add-on is not intended to be used in secure screens.
Nor is it able to support WASAPI at this time.
That means that it will disable itself in NVDA 2023.2 and above, if WASAPI is enabled in Advanced settings.

## Commands:

* Alt+NVDA+S: toggle sound splitter between enabled with NVDA on the right channel, NVDA on the left channel, or disabled.

## Sound Splitter settings

You can configure add-on settings from NVDA menu/Preferences/Settings/Sound Splitter category.

* Split NVDA sound and applications' sounds into left and right channels: checking this checkbox will enable the sound splitting feature.
* Switch left and right during sound split: by default, NVDA will be heard through the right channel if sound splitting is on. You can instead hear NVDA through the left channel by checking this checkbox.

### Changelog:

#### 23.5.0

* Disable the add-on's configuration and splitting function, with appropriate message to the user, if WASAPI is active in NVDA. (NVDA 2023.2 and up)

#### 23.04.1

* New maintainer: Luke Davis.
* Minor under the hood changes such as code movement, typo corrections, etc.

#### 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

#### 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer supported by Microsoft as of January 2023.
* Updated psutil dependency to 5.9.4.

#### 22.03

* NVDA 2021.3 or later is required.
* Improved security by not loading the add-on when NVDA is running in secure mode.
* Updated psutil dependency to 5.9.0.
* Changed sound splitter toggle command (Alt+NVDA+S) to toggle between NVDA on the right channel, on the left channel, or sound splitter disabled.

#### 22.02.1

* Fixed NVDA and app audio not being restored to both audio channels after the add-on is disabled or uninstalled.

#### 22.02

* Initial version based on Tony Malykh's Tony's Enhancements add-on.

[1]: https://nvaccess.org/addonStore/legacy?file=soundSplitter
