# 12 de octubre de 2026 — Revisión fotográfica del soporte de biobolas v1

## Alcance y procedencia

El 12 de octubre se revisaron las doce imágenes más recientes de Descargas y
los comentarios del propietario. Esta es la fecha de revisión y comunicación,
no una fecha atribuida a la impresión: la fecha exacta de fabricación de los
módulos y del hotel de pods no se ha indicado. La rotura previa de la tapa está
registrada el [11 de octubre](2026-10-11-rotura-tapa-soporte-biobolas.md).

El propietario confirma que son las piezas de **v1**, generadas previamente,
y que **v2 no se ha tocado ni impreso**. No se ha confirmado por nombre el
G-code usado, la bobina concreta ni los parámetros efectivos de la impresión.
Las recetas conservadas no se atribuyen automáticamente a estas piezas.

## Resultados comunicados por el propietario

- Los laterales que contienen las presillas comienzan a deformarse
  aproximadamente a media altura. Quedan con arrugas y muy endebles, y la
  presilla superior queda muy deformada. El propietario cree que «bailan»
  durante la impresión.
- Los soportes centrales y de las esquinas se imprimieron bien.
- La base se percibe bastante endeble y se pide reforzarla.
- La tapa se percibe muy frágil y se cuestionan sus grosores y planteamiento.
  Los soportes de impresión deben reducirse al mínimo porque su retirada
  destruye las piezas frágiles.
- El hotel para pods situado en el centro se imprimió bien.
- El propietario considera necesario buscar otro sistema de soportes y
  confirma que rediseñar la base también afectará a la tapa.

## Observaciones de las fotografías

| Archivos originales revisados | Hallazgo visual y límite |
| --- | --- |
| `IMG20261012112533.jpg`, `IMG20261012112538.jpg`, `IMG20261012112544.jpg`, `IMG20261012112549.jpg`, `IMG20261012112556.jpg` | Vista del módulo y detalles de laterales con bandas irregulares, abultamientos y filamentos sueltos, junto a mástiles con acabado más uniforme. Las fotos no miden rigidez ni muestran el movimiento durante la impresión |
| `IMG20261012112600.jpg` | Vista superior de la base abierta y las columnas. No permite medir deformación bajo carga ni espesor real |
| `IMG20261012112611.jpg`, `IMG20261012112616.jpg`, `IMG20261012112625.jpg` | Tapa con un tramo del bastidor separado y material auxiliar adherido o entrelazado. El propietario atribuye la rotura a la retirada de soportes; las fotos muestran el resultado, no la maniobra |
| `IMG20261012112636.jpg`, `IMG20261012112640.jpg`, `IMG20261012112648.jpg` | Inserto central aparentemente íntegro, con ventanas y apoyos visibles. Coincide con la impresión satisfactoria comunicada; no acredita ajuste completo ni función biológica |

Los doce originales permanecen en Descargas, sin moverlos ni modificarlos.
No se han incorporado copias al repositorio. Esta tabla conserva la identidad
y cobertura de la inspección, pero no sustituye los originales para una revisión
visual posterior. Los nombres y las fechas de archivo no demuestran la fecha
de impresión.

## Interpretación y límites

El movimiento de los laterales durante la impresión es una hipótesis del
propietario compatible con la distribución de defectos observada. No se dispone
de vídeo, medidas de desplazamiento ni registro térmico para confirmarla o
descartar otras causas. La fragilidad de base y tapa es una valoración física
comunicada, sin ensayo cuantificado de flexión o carga.

La impresión satisfactoria de mástiles, esquinas e inserto es un resultado
parcial. El conjunto v1 no está aceptado. V2 no ha sido ensayada y no se le
atribuye el fallo de v1. La función biológica del inserto, la suspensión y el
comportamiento húmedo prolongado siguen sin validación.

## Telemetría y pendientes derivados

No hay telemetría de Home Assistant pertinente para contrastar el acabado, la
rigidez o la retirada de soportes de estas piezas. No se consultó ni accionó
ningún equipo. Estado: **operación de revisión documentada sin telemetría
pertinente**, con evidencia física comunicada e inspección de fotografías.

El [plan de rediseño](../../../privado/disenos-3d/soporte-biobolas.md#replanteamiento-tras-la-impresión-de-v1--12-de-octubre-de-2026)
replantea base, elementos portantes, cierres y tapa, conservando inicialmente
el inserto central. No se ha ejecutado el rediseño ni se han generado nuevos
archivos de impresión en esta revisión.
