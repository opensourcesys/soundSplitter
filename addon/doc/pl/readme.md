# Sound Splitter #

* Authors: Joseph Lee, Luke Davis and contributors
* Pobierz [Wersja stabilna][1]
* NVDA compatibility: 2022.4 and later

Ten dodatek, częściowo oparty na ulepszeniach Tony'ego Autorstwa Tony'ego
Malykha, dodaje możliwość dzielenia dźwięku z NVDA i innych dźwięków na
oddzielne kanały audio.

Uwaga: ten dodatek nie jest przeznaczony do użytku na bezpiecznych ekranach.

## Polecenia

* Alt+NvDA+S: przełączaj rozdzielacz dźwięku między włączonym z NVDA na
  prawym kanale, NVDA na lewym kanale lub wyłączonym.

## Ustawienia rozdzielacza dźwięku

Ustawienia dodatku można skonfigurować z poziomu menu
NVDA/Preferencje/Ustawienia/Rozdzielacz dźwięku.

* Podziel dźwięk NVDA i dźwięki aplikacji na lewy i prawy kanał: zaznacz to
  pole wyboru włączy funkcję dzielenia dźwięku.
* Przełączaj się w lewo i w prawo podczas podziału dźwięku: domyślnie NVDA
  będzie słyszalny przez prawy kanał, jeśli podział dźwięku jest
  włączony. Zamiast tego możesz usłyszeć NVDA przez lewy kanał, zaznaczając
  to pole wyboru.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer
  supported by Microsoft as of January 2023.
* Updated psutil dependency to 5.9.4.

## Wersja 22.03

* Wymagana jest nvda 2021.3 lub nowsza.
* Poprawiono bezpieczeństwo, nie ładując dodatku, gdy NVDA działa w trybie
  bezpiecznym.
* Zaktualizowano zależność psutil do wersji 5.9.0.
* Zmieniono polecenie przełączania rozdzielacza dźwięku (Alt + NVDA + S),
  aby przełączać się między NVDA na prawym kanale, na lewym kanale lub
  wyłączonym rozdzielaczem dźwięku.

## Wersja 22.02.1

* Naprawiono NVDA i dźwięk aplikacji, który nie był przywracany do obu
  kanałów audio po wyłączeniu lub odinstalowaniu dodatku.

## Wersja 22.02

* Początkowa wersja oparta na dodatku Tony Malykh's Tony's Enhancements.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=soundSplitter
