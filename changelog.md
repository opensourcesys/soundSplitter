# Changelog:

### 24.0.0

* Compatibility with NVDA 2024.1.
* Fixes a bug with WASAPI state detection in NVDA 2024.1 and later.
* Emits a dynamic notice on installation, that WASAPI sound split feature is available in NVDA 2024.2. The notice is appropriately different depending on NVDA version.

### 23.5.8

Hotfix for WASAPI detection, contributed by @CyrilleB79:
Previous WASAPI check accidentally used config spec where config was meant. This is fixed.
It now also handles the case of using a newer NVDA config with an older NVDA.

### 23.5.7

* Handle the changed capitalization for the WASAPI config key in 2023.3 series NVDA alphas.

### 23.5.2

Bug fixes:
* Fixed a logic error that could sometimes occur when detecting WASAPI status the first time.
* Attempt to fix a missing string in Turkish translation

Fixes submitted by Cyrille Bougot:
* If nvda.ini was used by both NVDA versions supporting and not supporting WASAPI, the support state was incorrectly detected.
 * The message spoken when the shortcut key was pressed but WASAPI was enabled, did not direct a restart of NVDA.

### 23.5.0

* Disable the add-on's configuration and splitting function, with appropriate message to the user, if WASAPI is active in NVDA. (NVDA 2023.2 and up)

### 23.04.1

* New maintainer: Luke Davis.
* Minor under the hood changes such as code movement, typo corrections, etc.

### 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

### 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer supported by Microsoft as of January 2023.
* Updated psutil dependency to 5.9.4.

### 22.03

* NVDA 2021.3 or later is required.
* Improved security by not loading the add-on when NVDA is running in secure mode.
* Updated psutil dependency to 5.9.0.
* Changed sound splitter toggle command (Alt+NVDA+S) to toggle between NVDA on the right channel, on the left channel, or sound splitter disabled.

### 22.02.1

* Fixed NVDA and app audio not being restored to both audio channels after the add-on is disabled or uninstalled.

### 22.02

* Initial version based on Tony Malykh's Tony's Enhancements add-on.
