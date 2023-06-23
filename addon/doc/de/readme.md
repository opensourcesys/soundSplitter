# Sound-Teilung #

* Autoren: Joseph Lee, Luke Davis und weitere Entwickler
* [Stabile Version herunterladen][1]
* NVDA-Kompatibilität: 2022.4 und neuer

Diese Erweiterung, die teilweise auf die Erweiterung von Tony Malykh
basiert, fügt die Möglichkeit hinzu, Audio von NVDA und anderen Sounds auf
separate Audiokanäle aufzuteilen.

Hinweis: Diese Erweiterung ist nicht für die Verwendung im geschützten
Bereich vorgesehen.

## Befehle:

* Alt+NVDA+S: Schaltet die Sound-Teilung zwischen aktiviert mit NVDA auf dem
  rechten Kanal, NVDA auf dem linken Kanal oder deaktiviert um.

## Einstellungen für Sound Splitter

Sie können die Einstellungen der Erweiterung im NVDA-Menü -> Optionen ->
Einstellungen -> Sound Splitter konfigurieren.

* NVDA-Sound und Anwendungssound in linke und rechte Kanäle aufteilen: Wenn
  Sie dieses Kontrollkästchen aktivieren, wird die Funktion zum Aufteilen
  des Sounds aktiviert.
* Bei Tonaufteilung zwischen linken und rechten Audiokanal wechseln:
  Standardmäßig wird NVDA über den rechten Kanal gehört, wenn die
  Tonaufteilung aktiviert ist. Sie können NVDA stattdessen über den linken
  Kanal hören, indem Sie dieses Kontrollkästchen aktivieren.

## Version 23.02

* NVDA 2022.4 oder neuer wird benötigt.
* Windows 10 Version 21H2 (November 2021 Update bzw. Build 19044) oder neuer
  wird benötigt.

## Version 23.01

* NVDA 2022.3 oder neuer wird benötigt.
* Windows 10 oder neuer ist erforderlich, da Windows 7, 8 und 8.1 ab Januar
  2023 nicht mehr von Microsoft unterstützt werden.
* Die Python-Abhängigkeit "psutil" wurde auf 5.9.4 aktualisiert.

## Version 22.03

* NVDA 2021.3 oder neuer wird benötigt.
* Die Sicherheit wurde verbessert, indem die Erweiterung nicht geladen
  werden kann, sobald NVDA im geschützten Bereich ausgeführt wird.
* Psutil-Abhängigkeit auf 5.9.0 aktualisiert.
* Der Befehl zum Umschalten der Sound-Teilung (Alt+NVDA+S) wurde geändert,
  um zwischen NVDA auf dem rechten Kanal, auf dem linken Kanal oder
  deaktivierter Sound-Teilung umzuschalten.

## Version 22.02.1

* Problem behoben, dass NVDA und App-Audio nicht auf beiden Audiokanälen
  wiederhergestellt wurden, nachdem die erweiterung deaktiviert oder
  deinstalliert wurde.

## Version 22.02

* Die erste Version basiert auf die Erweiterung von Tony Malykh.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=soundSplitter
