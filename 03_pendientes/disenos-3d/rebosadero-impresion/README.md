# Laminado del rebosadero regulable C2–C3

Generado el 11 de octubre de 2026 con **OrcaSlicer 2.4.2**. Tres piezas, cada
una en un proyecto y una impresión independientes. Estado: G-code generado,
movimientos comprobados y trayectorias revisadas; **impresión y uso hidráulico
pendientes**. Primero imprimir y probar la probeta de silicona.

## Fuentes y método

Fuente paramétrica: [rebosadero.FCStd](../rebosadero.FCStd).
Función, interfaces y validaciones pendientes: [rebosadero.md](../rebosadero.md).
El CAD original se conserva en su ruta; la exportación aplica las rotaciones a
formas temporales sin alterar la geometría del documento. No se ha reparado,
simplificado ni escalado ninguna malla. Todas las piezas exportadas son sólidos
válidos y sus mallas son cerradas.

La receta procede de
[la probeta de cristal de biobolas](../soporte-biobolas-impresion/probeta-cristal-ajuste--kp3-winkle-petg.3mf).
Se conservaron las identidades de impresora y filamento y los parámetros de
máquina, PETG y velocidades. Se reemplazaron geometría y metadatos de objeto;
se ajustaron por pieza el relleno, el brim y la secuencia final de la estructura.
Los campos de conexión se eliminaron. La referencia no se ha modificado.
Su huella se registra en [receta-origen.json](receta-origen.json).

Laminado por CLI con `--datadir` temporal, perfiles completos embebidos,
`--slice 0`, salida explícita y `--export-3mf`. No se usó `--no-check` ni se
editaron perfiles globales. La comprobación de ZIP/XML, las sumas de todas las
fuentes y derivados, tamaños, cabeceras de generación y parámetros efectivos
están en [comprobacion-laminado.json](comprobacion-laminado.json).

## Impresora, material y secado

- Kingroon **KP3, unidad KP3-3DP180**, volumen nominal 180 × 180 × 180 mm,
  extrusor directo, boquilla de 0,4 mm, filamento de 1,75 mm y G-code Marlin.
  Firmware exacto: no disponible; comprobar en la pantalla de información de
  la máquina si se necesita identificar su versión.
- Perfil de máquina: `Kingroon KP3 (KP3-3DP180) 0.4 nozzle`.
  Se conserva el campo interno heredado `printer_model = Generic Marlin Printer`.
- **Winkle PETG Jet Black**, negro, 1,75 mm;
  perfil `Winkle PETG Jet Black 1.75 mm`, densidad 1,23 g/cm³.
  El color de visualización naranja heredado del proyecto no cambia el material.
  Lote y secado físico de la bobina: no disponibles en este trabajo.
- Procesos `Veril rebosadero estructura KP3 PETG`,
  `Veril rebosadero placa-20mm KP3 PETG` y
  `Veril rebosadero probeta-silicona KP3 PETG`: recetas candidatas para estas
  geometrías. La prueba anterior del encaje de 6 mm no valida la pieza completa.

Se conserva la pauta inicial de la entrega anterior: SUNLU S2 a **55 °C durante
6 h**, `Material=PETG`, `LED` opcional. Antes de alimentar, retirar embalaje y
comprobar giro libre y recorrido al extrusor. Durante impresión desde el S2,
conservar 55 °C y poner `Time` suficiente para cubrir el trabajo: **10 h para
la estructura, 2 h para la placa y 1 h para la probeta**, después del secado.
`PV` es la temperatura medida; `RH` no certifica humedad del filamento.
No se ha ejecutado ningún ciclo de secado ni accionado la impresora.

## Parámetros efectivos comunes

| Grupo | Valores |
| --- | --- |
| Capas | 0,20 mm; primera capa 0,24 mm |
| Temperaturas, incluida primera capa | Boquilla 230 °C; cama 70 °C |
| Filamento | Flujo 1,00; máximo volumétrico 8 mm³/s; densidad 1,23 g/cm³ |
| Anchos | Exterior y sólidos 0,42 mm; interior y relleno 0,45 mm |
| Velocidades | Primera capa/relleno 20; exterior 35; interior/relleno 45; sólidos 40; superior 30; puentes 20; viajes 120 mm/s |
| Aceleraciones | Normal/interior/viajes 1000; primera capa 500; exterior 800 mm/s²; puente 50 % de la normal |
| Retracción | 0,8 mm a 30 mm/s; recuperación 0, que usa la velocidad de retracción; Z-hop 0,4 mm |
| Pressure advance | Desactivado; valor conservado 0,02 sin aplicarlo |
| Ventilación | Primera capa 0 %; mínimo/máximo 100 %; completo desde capa 2 |
| Cubiertas | 5 capas superiores y 6 inferiores |
| Compensaciones | Contorno, agujero y pie de elefante 0; escala 1:1 |
| Secuencia | Un objeto, una cama y un filamento por proyecto |
| Adhesión adicional | Faldilla de una vuelta a 2 mm; sin raft; separación brim/pieza 0,1 mm |

Los valores completos relevantes de cada proyecto y los extraídos del bloque
efectivo del G-code se conservan en el informe JSON. Son parámetros de receta,
no una nueva calibración aceptada de la bobina o de la impresora.

## Piezas y estimaciones por impresión

| Pieza | Unidades | Paredes / relleno | Soportes generados | Brim exterior | Capas | Tiempo estimado (Orca) | PETG | G-code |
| --- | ---: | --- | --- | ---: | ---: | --- | ---: | --- |
| Estructura del rebosadero | 1 | 5 / 30% | No | 5 mm | 892 | 7h 41m 20s | 94.01 g | [VRREBO.GCO](VRREBO.GCO) |
| Placa de 20 mm | 1 | 5 / 100% | No | 3 mm | 12 | 42m 43s | 8.33 g | [VRPL20.GCO](VRPL20.GCO) |
| Probeta de silicona derecha | 1 | 5 / 30% | No | 3 mm | 155 | 15m 1s | 1.29 g | [VRPSIL.GCO](VRPSIL.GCO) |

Son estimaciones nativas de Orca, con brim y faldilla incluidos. No se aplica
corrección de tiempos de otros modelos; no hay tiempos reales de estas piezas.

## Orientación y decisiones por pieza

**Estructura:** invertida 180° alrededor de X, con la parte superior original
contra la cama. Envolvente 139 × 25,2 × 178,4 mm. Las columnas y cartelas se
imprimen en la orientación para la que se diseñaron sus pendientes a 45°.
Cinco paredes y 30 % gyroid; brim de 5 mm. Frente a tumbada sobre la pantalla
posterior, se conserva la orientación invertida acordada para reducir soportes
en el canal y mantener las caras de acoplamiento libres de sus marcas.

**Placa:** giro de 90° alrededor de X, con su cara de 133,6 × 20 mm sobre la
cama y 2,4 mm de altura CAD. Cinco paredes, relleno al 100 % y brim de 3 mm.
Se imprime plana para reducir altura, dar apoyo completo y evitar soportes.
El acabado de cama y el brim deben permitir su deslizamiento en las guías.

**Probeta:** invertida, 9,5 × 10,8 × 31 mm, conservando pinza, cartela y rebaje
lateral de 3,5 mm del extremo derecho. Cinco paredes, 30 % gyroid y brim de
3 mm. Conserva la orientación del conjunto para representar sus pendientes y
superficies funcionales; no contiene la placa ni la pantalla larga.

Los tres proyectos tienen soportes desactivados y el resultado de Orca indica
`support_used=false`. Las reconstrucciones de extrusión revisadas no contienen
soportes. El resultado conserva paredes y guías, pero la calidad real de los
cierres a 45° y los puentes internos sigue pendiente de impresión.

## Límite de altura y comprobación de movimientos

Orca redondea la última capa a **178,44 mm** en la estructura, **2,44 mm** en la
placa y **31,04 mm** en la probeta. Son cotas de laminado, no cambios de CAD.

La secuencia heredada subía 5 mm relativos al terminar. En la estructura se
sustituye por un movimiento absoluto a **Z=179,2 mm**, seguido del aparcado
habitual X=0/Y=179. Así se evita rebasar los 180 mm nominales. Los otros dos
proyectos conservan la elevación de 5 mm porque tienen altura disponible.
Se mantiene Z-hop de 0,4 mm en los tres.

El analizador recorre los movimientos de inicio, impresión, viajes, retracción
y final, interpretando G90/G91. No hay coordenadas fuera de 0–180 mm:

| Pieza | X máximo | Y máximo | Z máximo, incluido final |
| --- | ---: | ---: | ---: |
| Estructura | 170 mm | 179 mm | 179,2 mm |
| Placa | 170 mm | 179 mm | 7,44 mm |
| Probeta | 170 mm | 179 mm | 36,04 mm |

Orca declara `outside=false` para las tres camas. No hubo error CLI ni
advertencias de laminado en sus logs. La comprobación numérica presupone la
KP3 de 180 mm declarada; no mide su recorrido físico ni comprueba su nivelación.

## Artefactos y evidencia

| Pieza | Proyecto preparado | Proyecto laminado | Malla de impresión | Vista de G-code |
| --- | --- | --- | --- | --- |
| Estructura del rebosadero | [Proyecto](estructura--kp3-winkle-petg.3mf) | [3MF laminado](laminados/estructura/estructura-laminado.3mf) | [STL](modelos/estructura.stl) | [Trayectorias](laminados/estructura/vista-previa.png) |
| Placa de 20 mm | [Proyecto](placa-20mm--kp3-winkle-petg.3mf) | [3MF laminado](laminados/placa-20mm/placa-20mm-laminado.3mf) | [STL](modelos/placa-20mm.stl) | [Trayectorias](laminados/placa-20mm/vista-previa.png) |
| Probeta de silicona derecha | [Proyecto](probeta-silicona--kp3-winkle-petg.3mf) | [3MF laminado](laminados/probeta-silicona/probeta-silicona-laminado.3mf) | [STL](modelos/probeta-silicona.stl) | [Trayectorias](laminados/probeta-silicona/vista-previa.png) |

Las vistas enlazadas reconstruyen los segmentos reales de extrusión del G-code:
vista global muestreada y capas seleccionadas con todos sus segmentos.
Se revisaron la primera capa, los cierres de ventana y cartelas en la estructura,
las transiciones de la probeta y las capas de la placa. No se afirma una
inspección manual exhaustiva de todas las capas.

Las capturas de apertura en Orca se conservan para
[estructura](laminados/estructura/orca-vista.png) y
[placa](laminados/placa-20mm/orca-vista.png), y se conserva la
[previsualización de la probeta](laminados/probeta-silicona/orca-vista.png).
La revisión de trayectorias de las tres piezas usa las vistas reconstruidas
del G-code indicadas en la tabla.
La apertura real de los 3MF laminados, con sus perfiles, se registra en
[apertura-orca.json](apertura-orca.json). El aviso `Perfil Personalizado`
se reconoce al cargar las secuencias propias de máquina. La primera instancia
aislada mostró el asistente de configuración; la verificación posterior
inicializó únicamente el directorio temporal con el modelo KP3 y abrió los
proyectos sin completar ese asistente ni tocar la configuración global.

| G-code | Tamaño (bytes) | SHA-256 |
| --- | ---: | --- |
| [VRREBO.GCO](VRREBO.GCO) | 2,881,723 | `7b90319454dff180d619fde28d1cc2f9b533f4d88ad65c6b83df19b6217614e4` |
| [VRPL20.GCO](VRPL20.GCO) | 231,767 | `2704e0ebc48ee75dfcb8e330a6c16375351c2d2698a3599fae1e10847ac17c57` |
| [VRPSIL.GCO](VRPSIL.GCO) | 272,222 | `dddb079eddd310ae3a115ed5189740972bc2737f4fb5c8a96d17a1a651dfc10b` |

Las cabeceras sitúan la generación a las 17:09 del 11 de octubre de 2026.
Las marcas completas y la hora de verificación con zona Atlantic/Canary están
en el informe JSON. El SHA-256 del CAD y las mallas, proyectos preparados y
laminados también quedan allí; el G-code externo coincide byte a byte con el
incluido en su 3MF laminado.

## Repetición y prueba física

[preparar.py](preparar.py) construye los proyectos desde las mallas registradas
y la receta identificada; [laminar.py](laminar.py) repite el laminado aislado;
[verificar.py](verificar.py) comprueba salidas y movimientos. Para regenerar las
vistas, usar `uv run --with matplotlib --with numpy python vistas.py`.
Un cambio de CAD requiere volver a exportar los sólidos y actualizar
`modelos/geometria.json` antes de preparar y laminar; también requiere regenerar
sumas, vistas e informe. La apertura GUI se verifica con
[abrir_verificar.py](abrir_verificar.py).

**Orden de prueba:** imprimir primero `VRPSIL.GCO`. Retirar el brim sin alterar
la pinza ni el borde que sirve de referencia. Debe apoyar en el canto y llegar
al lateral sin forzar ni rozar la silicona. Después comprobar la placa impresa
y el conjunto, el margen mínimo de 20 mm entre agua y borde y el funcionamiento
real del rebose y de la pantalla de burbujas.

Compatibilidad de esta entrega: **KP3-3DP180, boquilla de 0,4 mm, Marlin y
Winkle PETG Jet Black 1,75 mm**, con los procesos descritos. Los archivos ASCII
cortos se transfieren manualmente por microSD. **No se han copiado a una tarjeta,
enviado ni iniciado impresiones.** Revisar primera capa, adhesión, retirada del
brim y superficies de encaje. La fabricación y el comportamiento hidráulico
siguen pendientes de prueba física.
