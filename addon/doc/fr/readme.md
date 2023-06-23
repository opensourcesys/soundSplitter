# Séparateur de son #

* Auteurs : Joseph Lee, Luke Davis et contributeurs
* Télécharger [version stable][1]
* Compatibilité NVDA : 2022.4 et versions ultérieures

Cette extension, en partie basé sur Tony's Enhancements de Tony Malykh,
ajoute la possibilité de séparer l'audio de NVDA et d'autres sons sur des
canaux audio séparés.

Remarque : cette extension n'est pas destinée à être utilisée sur des écrans
sécurisés.

## Commandes :

* Alt+NvDA+S : basculer le séparateur de son entre activé avec NVDA sur le
  canal droit, NVDA sur le canal gauche ou désactivé.

## Paramètres du séparateur de son

Vous pouvez configurer les paramètres de l'extension à partir du menu
NVDA/Préférences/Paramètres/catégorie Séparateur de son.

* Séparer le son de NVDA et les sons des applications entre canaux gauche et
  droit : cocher cette case pour activer la fonction de séparation du son.
* Intervertir la gauche et la droite pendant que le son est séparé : par
  défaut, NVDA sera entendu via le canal droit si la séparation du son est
  activée. Vous pouvez cependant entendre NVDA via le canal gauche en
  cochant cette case.

## Version 23.02

* Nécessite NVDA 2022.4 ou version ultérieure.
* Windows 10 21H2 (November 2021 Update/build 19044) ou ultérieure est
  requise.

## Version 23.01

* Nécessite NVDA 2022.3 ou version ultérieure.
* Windows 10 ou ultérieure est requis car Windows 7, 8 et 8.1 ne sont plus
  pris en charge par Microsoft en janvier 2023.
* Mise à jour de la dépendance psutil à la version 5.9.4.

## Version 22.03

* Nécessite NVDA 2021.3 ou version ultérieure.
* Amélioration de la sécurité en ne chargeant pas l'extension lorsque NVDA
  s'exécute en mode sécurisé.
* Mise à jour de la dépendance psutil à la version 5.9.0.
* Modification de la commande de bascule du séparateur de son (Alt + NVDA +
  S) pour basculer entre NVDA sur le canal droit, sur le canal gauche ou le
  séparateur de son désactivé.

## Version 22.02.1

* Correctif d'un problème où l'audio de NVDA et des applications n'étaient
  pas restaurés sur les deux canaux audio après la désactivation ou la
  désinstallation de l'extension.

## Version 22.02

* Version initiale basée sur l'extension Tony's Enhancements de Tony Malykh.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=soundSplitter
