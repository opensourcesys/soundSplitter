# Äänenjakaja #

* Tekijät: Joseph Lee, Luke Davis sekä muut
* Lataa [vakaa versio][1]
* Yhteensopivuus: NVDA 2022.4 ja uudemmat

Tämä lisäosa, joka perustuu osittain Tony Malykhin Tony's Enhancementsiin,
lisää mahdollisuuden jakaa NVDA:n puhe ja muut äänet erillisiin
äänikanaviin.

Huom: Tätä lisäosaa ei ole tarkoitettu suojatuissa ruuduissa käytettäväksi.

## Komennot:

* Alt+NVDA+S: Vaihtaa Äänenjakajan tilaa siten, että se on joko käytössä ja
  NVDA kuuluu oikeasta kanavasta, vasemmasta kanavasta tai pois käytöstä.

## Äänenjakajan asetukset

Voit muuttaa tämän lisäosan asetuksia kohdasta
NVDA-valikko/Asetukset/Asetukset/Äänenjakaja-kategoria.

* Jaa NVDA:n äänet oikeaan kanavaan ja muiden sovellusten vasempaan: tämän
  valintaruudun valitseminen ottaa käyttöön äänenjakotoiminnon.
* Vaihda vasen ja oikea keskenään äänenjakamisen ollessa käytössä: NVDA
  kuuluu oletusarvoisesti oikeasta kanavasta, kun äänenjakaminen on
  käytössä. Voit vaihtaa NVDA:n kuulumaan vasemmasta kanavasta valitsemalla
  tämän valintaruudun.

## Versio 23.02

* Edellyttää NVDA 2022.4:ää tai uudempaa.
* Windows 10 21H2 (marraskuun 2021 päivitys/koontiversio 19044) tai uudempi
  vaaditaan.

## Versio 23.01

* Edellyttää NVDA 2022.3:a tai uudempaa.
* Windows 10 tai uudempi vaaditaan, koska Microsoft ei enää tue Windows
  7:ää, 8:aa tai 8.1:tä tammikuusta 2023 alkaen.
* Päivitetty psutil-riippuvuus versioksi 5.9.4.

## Versio 22.03

* Edellyttää NVDA 2021.3:a tai uudempaa.
* Tietoturvaa parannettu jättämällä lisäosa lataamatta, kun NVDA on
  käynnissä suojatussa tilassa.
* Päivitetty psutil-riippuvuus versioksi 5.9.0.
* Muutettu Äänenjakajan tilanvaihtokomento (Alt+NVDA+S) vaihtamaan NVDA
  oikeaan kanavaan, vasempaan kanavaan tai poistamaan lisäosa käytöstä.

## Versio 22.02.1

* Korjattu ongelma, joka aiheutti sen, ettei NVDA:n ja sovelluksen ääniä
  palautettu molempiin äänikanaviin lisäosan käytöstä poistamisen tai
  asennuksen poiston jälkeen.

## Versio 22.02

* Ensimmäinen versio, joka perustuu Tony Malykhin Tony's Enhancements
  -lisäosaan.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=soundSplitter
