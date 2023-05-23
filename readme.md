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

For version history, see [Changelog](https://github.com/opensourcesys/soundSplitter/blob/main/changelog.md#readme)

[1]: https://nvaccess.org/addonStore/legacy?file=soundSplitter
