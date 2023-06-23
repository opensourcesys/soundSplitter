# Razdjeljivač zvuka (Sound Splitter) #

* Autori: Joseph Lee, Luke Davis i doprinositelji
* Preuzmi [stabilnu verziju][1]
* NVDA kompatibilnost: 2022.4 i novije verzije

Ovaj dodatak, djelomično temeljen na dodatku „Tony’s Enhancements” od Tonyja
Malykha, dodaje mogućnost podjele NVDA zvuka i drugih zvukova u zasebne
audio kanale.

Napomena: ovaj dodatak nije namijenjen za korištenje u sigurnim ekranima.

## Naredbe:

* Alt+NvDA+S: mijenjaj stanje razdjeljivača zvuka između aktiviranog desnog
  kanala NVDA čitača, aktiviranog lijevog kanala NVDA čitača ili
  deaktivirano.

## Postavke razdjeljivača zvuka

Postavke dodatka možeš konfigurirati u kategoriji NVDA
izbornik/Postavke/Postavke/Razdjeljivač zvuka.

* Podijeli zvuk NVDA čitača i zvukove aplikacija na lijevi i desni kanal:
  označavanjem ovog polja aktivira se funkcija dijeljenja zvuka.
* Mijenjaj na lijevi i desni kanal tijekom razdjeljivanja zvuka: NVDA čitač
  se standardno čuje na desnom kanalu ako je razdjeljivanje zvuka
  uključeno. Označavanjem ovog polja možeš slušati NVDA čitača na lijevom
  kanalu.

## Verzija 23.02

* Potrebna je NVDA verzija 2022.4 ili novija.
* Potreban je sustav Windows 10 21H2 (aktualizirana verzija iz studenog
  2021./izgradnja 19044) ili novija verzija.

## Verzija 23.01

* Potrebna je NVDA verzija 2022.3 ili novija.
* Zahtijeva Windows 10 ili noviju verziju, jer od siječnja 2023. Microsoft
  više ne pordržava Windows 7, 8 i 8.1.
* Aktualizirana je psutil ovisnost na 5.9.4.

## Verzija 22.03

* Potrebna je NVDA verzija 2021.3 ili novija.
* Poboljšana je sigurnost ne učitavanjem dodatka kad NVDA radi u sigurnom
  modusu.
* Ažurirana je psutil zavisnost na 5.9.0.
* Promijenjena je naredba za uključivanje/isključivanje razdjelivača zvuka
  (Alt+NVDA+S) za mijenjanje između desnog i lijevog kanala NVDA čitača ili
  deaktiviranje razdjelivača zvuka.

## Verzija 22.02.1

* Ispravljen je problem sa zvukom NVDA čitača i aplikacije, koji se nije
  obnavljao na oba audio kanala nakon deaktiviranja ili deinstaliranja
  dodatka.

## Verzija 22.02

* Prva verzija temeljena na dodatku „Tony’s Enhancements” od Tonyja Malykha.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=soundSplitter
