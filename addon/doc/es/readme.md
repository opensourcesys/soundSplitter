# Sound Splitter #

* Autores: Joseph Lee, Luke Davis y colaboradores
* Descargar [versión estable][1]
* Compatibilidad con NVDA: de 2022.4 en adelante

Este complemento, basado en parte en Mejoras de Tony de Tony Malykh, añade
la posibilidad de dividir el audio de NVDA y otros sonidos en canales de
audio separados.

Nota: este complemento no está diseñado para ejecutarse en pantallas
seguras.

## Órdenes:

* Alt+NVDA+S: conmuta el divisor de sonido entre activado con NVDA en el
  canal derecho, NVDA en el canal izquierdo, o desactivado.

## Opciones de Sound Splitter

Puedes configurar las opciones del complemento desde menú NVDA /
Preferencias / Opciones / categoría Sound Splitter.

* Separar el sonido de NVDA y de otras aplicaciones en los canales izquierdo
  y derecho: al marcar esta casilla, se activará la función de división de
  sonido.
* Alternar izquierda y derecha durante la división de sonido: por defecto,
  NVDA se escuchará por el canal derecho si la división de sonido está
  activada. En su lugar, puedes escuchar NVDA por la izquierda marcando esta
  casilla.

## Versión 23.02

* Se requiere NVDA 2022.4 o posterior.
* Se requiere Windows 10 21H2 (actualización de noviembre de 2021 /
  compilación 19044) o posterior.

## Versión 23.01

* Se requiere NVDA 2022.3 o posterior.
* Se requiere Windows 10 o posterior, ya que Microsoft no soporta Windows 7,
  8 y 8.1 desde enero de 2023.
* Actualizada la dependencia psutil a la versión 5.9.4.

## Versión 22.03

* Se requiere NVDA 2021.3 o posterior.
* Se ha mejorado la seguridad no cargando el complemento cuando NVDA se
  ejecuta en modo seguro.
* Actualizada la dependencia psutil a la versión 5.9.0.
* Cambiada la orden de conmutación del divisor de sonido (alt+NVDA+s) para
  conmutar entre NVDA en el canal derecho, en el canal izquierdo, o división
  de sonido desactivada.

## Versión 22.02.1

* Corregido un problema por el que el audio de NVDA y las aplicaciones no se
  restauraba por ambos canales después de deshabilitar o desinstalar el
  complemento.

## Versión 22.02

* Versión inicial, basada en el complemento Mejoras de Tony, creado por Tony
  Malykh.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=soundSplitter
