# Jaula para BactoFlex Mini: receta de impresión

Este directorio contiene los derivados imprimibles de la jaula y de su tapa deslizante. La fuente editable y paramétrica es [`../veril-bactoflex.FCStd`](../veril-bactoflex.FCStd); ni los STL, ni los proyectos de OrcaSlicer, ni el G-code la sustituyen. Todo el paquete, incluidos estos archivos, se distribuye bajo la licencia [MIT](../LICENSE).

## Componentes

| Componente | Fuente de impresión | Orientación | Soportes | Estado |
| --- | --- | --- | --- | --- |
| Jaula | [`veril-bactoflex-jaula--kp3-winkle-petg.3mf`](veril-bactoflex-jaula--kp3-winkle-petg.3mf) | Base sobre la cama | Árbol manual desde la cama | Laminada el 23-09-2026; validación física pendiente. |
| Tapa | [`veril-bactoflex-tapa--kp3-winkle-petg.3mf`](veril-bactoflex-tapa--kp3-winkle-petg.3mf) | Plana sobre la cama | No | Proyecto corregido y laminado el 23-09-2026; validación física pendiente. |

Los STL se conservan como exportaciones geométricas. Para modificar la pieza se debe abrir el FCStd; para laminarla, el 3MF del componente correspondiente.

## Receta candidata

La receta está destinada a la Kingroon KP3 (`KP3-3DP180`) con boquilla de 0,4 mm y PETG Winkle Jet Black de 1,75 mm. El material y la receta son **candidatos**: aún no existe una impresión física aceptada de esta pieza.

| Parámetro | Jaula | Tapa | Motivo |
| --- | ---: | ---: | --- |
| OrcaSlicer | 2.4.2 | 2.4.2 | Versión usada para los proyectos y el G-code. |
| Altura de capa / primera capa | 0,20 / 0,24 mm | 0,20 / 0,24 mm | Compromiso entre resistencia, precisión y tiempo. |
| Boquilla / cama | 230 / 70 °C | 230 / 70 °C | Punto de partida del perfil portátil de PETG Winkle. |
| Perímetros | 5 | 4 | La jaula necesita rigidez. La tapa tiene 1,7 mm de espesor: cuatro líneas de 0,4 mm la dejan esencialmente maciza sin pedir cinco perímetros en un espesor insuficiente. |
| Capas superior / inferior | 5 / 6 | 5 / 6 | Cierre resistente para una pieza sumergida. |
| Relleno | 35 % gyroid | No relevante si queda maciza por perímetros | Resistencia de la jaula sin sobredimensionar el consumo. |
| Brim | Exterior, 5 mm | Exterior, 5 mm | Adhesión controlada para PETG. |
| Soportes | Árbol manual, solo desde cama | Ninguno | La jaula solo los requiere bajo los apoyos traseros; la tapa no tiene voladizos funcionales. |
| Aceleración normal / pared interna / externa / primera capa | 1000 / 1000 / 800 / 500 mm/s² | Igual | Dentro de los límites configurados para evitar el aviso de aceleración. |

Antes de imprimir, el PETG debe estar seco y se debe comprobar en la vista previa de OrcaSlicer que los soportes manuales de la jaula siguen visibles únicamente en los cuatro apoyos indicados. No se debe aplicar soporte a toda la guía de la tapa.

## Laminado revisado el 23 de septiembre de 2026

El [informe de generación y comprobación](informe-gcode-2026-09-23.md) contiene los parámetros efectivos, huellas, tiempos, consumo y límites de ambos trabajos. Los dos proyectos y G-code se regeneraron con la cama KP3 corregida a 180 × 180 mm; el G-code termina aparcando en Y=179 mm.

| Pieza | G-code para microSD | Estimación OrcaSlicer | Estado |
| --- | --- | --- | --- |
| Jaula | [`VBFXCAG2.GCO`](VBFXCAG2.GCO) | 5 h 43 min 38 s | Regenerado desde el proyecto corregido; sin prueba física. |
| Tapa | [`VBFXLID.GCO`](VBFXLID.GCO) | 28 min 42 s | Regenerado desde el proyecto corregido, con cuatro perímetros y sin soportes; sin prueba física. |

El G-code anterior de la cesta, los autosaves de FreeCAD y el primer proyecto de Orca de la tapa se conservan en el archivo local de trabajo y no forman parte de este paquete de distribución. No se ha enviado ningún archivo a la impresora.

## Procedencia comprobada

La fuente FreeCAD se modificó manualmente después de la generación de los
proyectos de Orca y G-code descrita en el informe del 23 de septiembre. La
fuente actual tiene SHA-256
`4b150f8a2fe6f462e7d288edae638592d6e5d58545fe49d8e9268827e5dfc0ce`; la
tabla de procedencia anterior registraba
`bb4dec50ba6769acaff8bad391ba463b4404e77bd01756305d6a0e0495e7dbc8`.
No se ha verificado que las exportaciones y el G-code correspondan a la fuente
modificada, por lo que se conserva pendiente esa comprobación.

| Artefacto | SHA-256 |
| --- | --- |
| `veril-bactoflex.FCStd` | `4b150f8a2fe6f462e7d288edae638592d6e5d58545fe49d8e9268827e5dfc0ce` |
| `veril-bactoflex-jaula--kp3-winkle-petg.3mf` | `d6cf3fb24da548f772bbc1f6e6c648a230eb76bda17e5454abaff1fc4ad4d328` |
| `veril-bactoflex-tapa--kp3-winkle-petg.3mf` | `2ed945cd05162da3cfcf14b8c632371dec87a6e507b03b5ce1b717ba7f726566` |

La validación pendiente es física: encaje de la tapa en su guía, retirada de los soportes de la jaula, continuidad de las patas y soportes de ventosa, estanqueidad geométrica de la pieza y comportamiento tras inmersión. Una impresión satisfactoria deberá registrar material real, estado de secado, tiempo real y evidencia del montaje antes de declarar esta receta reproducible.
