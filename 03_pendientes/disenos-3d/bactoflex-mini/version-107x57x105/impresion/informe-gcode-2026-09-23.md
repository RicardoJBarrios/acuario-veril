# Cesta y tapa BactoFlex Mini: informe de G-code

Regeneración y comprobación del **23 de septiembre de 2026, 15:00 hora local** para probar el encaje y el uso sumergido de la jaula y su tapa deslizante. La [fuente editable](../veril-bactoflex.FCStd) es FreeCAD; los [STL de la jaula](veril-bactoflex-jaula.stl) y [de la tapa](veril-bactoflex-tapa.stl) son derivados geométricos. Los 3MF conservan la preparación para OrcaSlicer y los G-code son salidas regenerables para esta combinación concreta. El paquete se ofrece bajo [MIT](../../LICENSE).

## Procedencia y resultado

| Pieza | Proyecto 3MF usado y SHA-256 | G-code, tamaño y SHA-256 | Generado / resultado |
| --- | --- | --- | --- |
| Cesta o jaula | [`veril-bactoflex-jaula--kp3-winkle-petg.3mf`](veril-bactoflex-jaula--kp3-winkle-petg.3mf), `d6cf3fb24da548f772bbc1f6e6c648a230eb76bda17e5454abaff1fc4ad4d328` | [`VBFXCAG2.GCO`](VBFXCAG2.GCO), 10.559.225 bytes, `930d90ef81d2a3ce00a553f6461e75c156eaa0632d2a4835624db6f5919ac3c9` | 15:00; regenerado con cama de 180 × 180 mm. |
| Tapa | [`veril-bactoflex-tapa--kp3-winkle-petg.3mf`](veril-bactoflex-tapa--kp3-winkle-petg.3mf), `2ed945cd05162da3cfcf14b8c632371dec87a6e507b03b5ce1b717ba7f726566` | [`VBFXLID.GCO`](VBFXLID.GCO), 469.978 bytes, `10e54e1b3d00c6e36be95c7d9816837b854c0388325519f54e6eac04282b1dd6` | 15:00; regenerado con cama de 180 × 180 mm. |

OrcaSlicer **2.4.2** generó los archivos mediante su CLI en directorios aislados y explícitos para datos y salida, utilizando la configuración y los perfiles embebidos en los proyectos 3MF. La importación de los perfiles JSON externos fue rechazada por la CLI antes de laminar; no se atribuye esta salida a esos archivos externos. No se usó `--no-check`, ni se reparó o escaló la malla. Ambos 3MF superaron la comprobación de integridad ZIP y se abrieron realmente en OrcaSlicer sin diálogo de error observado. La vista previa de capas no se ha revisado visualmente.

El proyecto inicial de la tapa, con SHA-256 `10b450aac20cc84ba20ebf59ca20cb285f0fbeeba87b94875d6136d21744dced`, terminaba con una caída de la CLI y declaraba cinco perímetros y `Cool Plate`. Para el 3MF distribuido se conservaron geometría y posición; se sustituyó su bloque `project_settings.config` por el bloque completo del proyecto de la cesta y se fijaron **cuatro perímetros**, **soportes desactivados**, tipo de soporte `normal(manual)` inactivo, cama `High Temp Plate` e identificador propio del proceso de tapa. Su filamento hereda un identificador interno que menciona el proyecto de la cesta; el material y los parámetros efectivos son los que figuran abajo. El G-code histórico de la cesta se excluye del paquete actual.

## Máquina, material y receta candidata

Kingroon KP3 original (`KP3-3DP180`), boquilla de **0,4 mm**, extrusión directa, G-code **Marlin**. La ficha de la unidad y los perfiles locales confirman un volumen de **180 × 180 × 180 mm**. Se corrigieron ambos proyectos de Orca: `printable_area` y `bed_shape` ahora declaran 180 × 180 mm, y el G-code aparca en X=0, Y=179 mm para mantenerse 1 mm dentro del límite. Se recorrieron todas las líneas de movimiento `G0/G1`: cesta X=0–170 mm, Y=5–179 mm y Z de comando=0,3–109,44 mm; tapa X=0–170 mm, Y=5–179 mm y Z de comando=0,3–5 mm. La altura de modelo declarada es 109,04 mm para la cesta y 1,64 mm para la tapa. Todas las coordenadas emitidas están dentro de los límites 0–180 mm en X/Y/Z.

Filamento declarado: **Winkle PETG Jet Black, 1,75 mm**. El lote, la bobina concreta, su secado real y la boquilla actualmente montada no se han comprobado en esta generación. Perfil de impresora embebido: `Kingroon KP3 (KP3-3DP180) 0.4 nozzle`. Perfil de filamento embebido: `Winkle PETG Jet Black 1.75 mm` con sufijo de proyecto. Perfiles de proceso embebidos: identificador procedente del 3MF de jaula y `0.20mm BactoFlex tapa KP3 Winkle PETG`, respectivamente. Estado de ambas recetas: **candidatas**, sin impresión física aceptada.

| Parámetro efectivo leído del G-code | Cesta | Tapa |
| --- | ---: | ---: |
| Capa normal / inicial | 0,20 / 0,24 mm | igual |
| Boquilla / cama, también en primera capa | 230 / 70 °C | igual |
| Flujo / caudal volumétrico máximo | 1,00 / 8 mm³/s | igual |
| Retracción | 0,8 mm a 30 mm/s | igual |
| Velocidad primera capa / pared externa / interna | 20 / 40 / 50 mm/s | igual |
| Velocidad sólido interior / superficie superior / relleno / puente / viaje | 45 / 35 / 50 / 20 / 120 mm/s | igual |
| Aceleración normal / pared interna / externa / primera capa | 1000 / 1000 / 800 / 500 mm/s² | igual |
| Pressure advance | 0,02 declarado, **desactivado** | igual |
| Ventilación | 0 % primera capa; 100 % desde la segunda | igual |
| Perímetros; capas superiores / inferiores | 5; 5 / 6 | 4; 5 / 6 |
| Relleno | 35 % gyroid | 35 % gyroid configurado; la geometría fina puede quedar cubierta por perímetros |
| Compensaciones XY / escala | 0 / sin cambio declarado | igual |
| Secuencia | Por capas; un objeto en una placa | igual |

La cesta se orienta con la base en cama y la tapa plana. La cesta usa **soporte árbol manual solo desde la cama**, con umbral de 30°, separación superior de 0,20 mm, interfaz superior de tres capas y separación de interfaz de 0,5 mm. El G-code contiene trayectorias de soporte; la revisión visual de su presencia solo bajo los dos soportes superiores de ventosa y las dos patas traseras sigue pendiente. La tapa tiene `enable_support=0` y el G-code no contiene trayectorias etiquetadas como soporte; su geometría fue concebida sin voladizos que lo requieran, pero también necesita revisión de vista previa. Ambos usan **brim exterior de 5 mm** y una vuelta de faldilla. No se declaró raft. Se mantienen las orientaciones y posiciones de los 3MF, sin rotación ni cambio de escala durante el laminado.

## Estimaciones y comprobaciones

| Dato de OrcaSlicer | Cesta | Tapa |
| --- | ---: | ---: |
| Tiempo estimado | 5 h 43 min 38 s | 28 min 42 s |
| Filamento | 19.890,61 mm; 47,84 cm³ | 2.099,67 mm; 5,05 cm³ |
| Capas / altura máxima del modelo | 545 / 109,04 mm | 8 / 1,64 mm |

Los perfiles embebidos guardan `filament_density=0`, por lo que OrcaSlicer imprime **0,00 g y coste 0,00**: esos dos valores no son estimaciones utilizables. La ficha del material contiene dos densidades publicadas distintas; no se elige una por analogía para este informe. No aparecieron advertencias de laminado en la salida CLI, que tampoco ofrece aquí una revisión visual de puentes, paredes finas o soportes. Se comprobó el bloque de configuración de ambos G-code, la presencia de soportes solo en el de cesta y la ausencia de movimientos XY por encima de 180 mm. No existe tiempo real de impresión para comparar con estas estimaciones.

## Preparación y límites

Estos G-code corresponden solo a la **KP3 original, boquilla 0,4 mm, Winkle PETG Jet Black de 1,75 mm y los perfiles embebidos indicados**. Se prepararon para copia manual a **microSD**; no se han enviado a la impresora ni se ha iniciado una impresión. Antes de usarlos, comprobar boquilla y bobina reales, primera capa, adherencia, espacio de la cama, orientación y vista previa de soportes. El encaje de la tapa, retirada de soportes, resistencia e inmersión siguen sin prueba física.

El estado de secado de la bobina no se registró al generar estos archivos. Antes de imprimir, sigue las instrucciones del fabricante del filamento y del secador que utilices; imprimir desde un secador requiere comprobar que la bobina gira libremente y que la ruta de alimentación no roza. El G-code no demuestra que el material esté seco. Registra el ciclo aplicado y el resultado físico antes de promover esta receta a vigente.
