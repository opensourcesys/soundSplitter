# Разделяне на звука (Sound Splitter) #

* Автори: Joseph Lee, Luke Davis и други сътрудници
* Изтегляне на [стабилна версия][1]
* Съвместимост с NVDA: от 2022.4 и по-нови версии

Тази добавка, частично базирана на добавката "Подобрения от Тони (Tony's
enhancements)" от Tony Malykh, добавя възможността за разделяне на звука от
NVDA и другите звуци в отделни аудио канали.

Забележка: Тази добавка не е предназначена за използване в защитени екрани.

## Команди:

* Alt+NVDA+S: Превключване на разделянето на звука между извеждане на NVDA в
  десния канал, в левия канал или изключено разделяне на звука.

## Настройки за разделянето на звука

Можете да конфигурирате настройките на добавката от менюто на NVDA ->
Настройки -> Опции -> категория "Разделяне на звука".

* Разделяй звука от NVDA и звуците от другите приложения на ляв и десен
  канал: Поставянето на отметка в квадратчето ще задейства функцията за
  разделяне на звука.
* Разменяй левия и десния канал при разделяне на звука: По подразбиране, ако
  разделянето на звука е включено, NVDA ще се чува през десния канал. Вместо
  това можете да чувате NVDA през левия канал, като поставите отметка в това
  квадратче.

## Версия 23.02

* Изисква се NVDA 2022.4 или по-нова версия.
* Изисква се Windows 10 21H2 (актуализация от месец ноември 2021
  г./компилация 19044) или по-нова версия.

## Версия 23.01

* Изисква се NVDA 2022.3 или по-нова версия.
* Изисква се Windows 10 или по-нова версия, тъй като Windows 7, 8 и 8.1 вече
  не се поддържат от Microsoft от януари 2023 г.
* Външната библиотека psutil е обновена до версия 5.9.4.

## Версия 22.03

* Изисква се NVDA 2021.3 или по-нова версия.
* Подобрена е сигурността, като не се зарежда добавката, когато NVDA работи
  в защитен режим.
* Външната библиотека psutil е обновена до версия 5.9.0.
* Променено е поведението на командата за превключване на разделянето на
  звука (Alt+NVDA+S) да превключва подаването на NVDA в десния канал, в
  левия канал или да няма разделяне на звука.

## Версия 22.02.1

* Поправено е, че звукът на NVDA и приложението не се възстановява и в двата
  аудио канала, след като добавката е изключена или деинсталирана.

## Версия 22.02

* Първо издание, базирана на добавката "Подобрения от Тони (Tony's
  enhancements)" от Tony Malykh.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=soundSplitter
