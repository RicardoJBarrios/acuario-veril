# Laminado del soporte de biobolas

Última actualización: 2026-10-11. Estado: **probetas impresas y encajes individuales comprobados cualitativamente; piezas funcionales y ensayo de carga pendientes**.

## Fuente y método

La fuente es [soporte-biobolas.FCStd](../soporte-biobolas.FCStd). Su revisión actual tiene SHA-256 `dcad9e51075f0557c13f14d363be6fb3ff2534c6526cc75a21f5a71011551390`; los ocho laminados originales se generaron desde la revisión `b07531eab561058886f51565b7968c1ed6666a9e274b432cc55eb78955a1c06e`. Se exportaron ocho piezas funcionales/probetas originales y una segunda variante de la probeta de cristal, sin los modelos de vidrio, agua, biobolas cerámicas ni acolchados. Los dos módulos usan la misma pieza; los dos insertos también.

Las siete mallas STL iniciales se exportaron desde FreeCAD, con deflexión lineal de 0,05 mm y angular de 0,15 rad. El peine de cristal original quedó en el FCStd como un bloque base y tres cortes editables de 7, 8 y 9 mm. Tras observar juego en la ranura impresa de 7 mm, se añadió al mismo documento otro grupo de operaciones con ranuras de 6,00, 6,25 y 6,50 mm; el usuario estimó la ranura anterior en 7 mm con un escalímetro, sin calibre de precisión. El grosor real del vidrio no se midió. La malla nueva se exportó desde FreeCAD. Las mallas se centraron en X/Y y se llevó el punto inferior a Z=0, sin cambiar escala. La tapa se giró +90° en X antes de exportarla; el resto conserva su orientación de CAD o de ensayo documentada. La tapa mide 94,5 × 74 × 81 mm en impresión, el módulo 81 × 81 × 155,871 mm y el inserto 38,5 × 38,5 × 142 mm. Las cuatro probetas originales caben individualmente en 15,5 × 14 × 25 mm; ambos peines de cristal miden 33 × 12 × 20 mm.

Se crearon proyectos con parámetros completos embebidos a partir del proyecto PETG de [BactoFlex](../bactoflex-mini/version-107x57x105/impresion/veril-bactoflex-jaula--kp3-winkle-petg.3mf). Se conservaron la identidad KP3 y sus secuencias Marlin. Se sustituyeron toda la geometría, los metadatos de objetos y las recetas de proceso. Se eliminaron campos de conexión y credenciales. La densidad se fijó a 1,23 g/cm³, según la ficha local Winkle; el proyecto de referencia la guardaba a cero. No se repararon ni simplificaron las mallas.

OrcaSlicer 2.4.2, CLI aislada con `--datadir /tmp/veril-biobolas-orca-datos`, `--slice 0`, salida explícita y exportación 3MF. No se usó `--no-check`. [laminar.py](laminar.py) permite repetir el laminado en un directorio temporal aislado. Los perfiles globales no se editaron. Las instrucciones efectivas son los AGENTS de Documents y del checkout acuario-veril, sin reglas más profundas en esta ruta.

## Impresora y material

- Kingroon KP3, unidad `KP3-3DP180`, 180 × 180 × 180 mm, extrusor directo, boquilla de 0,4 mm y lenguaje Marlin. El campo interno heredado `printer_model` es `Generic Marlin Printer`; el perfil aplicado se identifica como `Kingroon KP3 (KP3-3DP180) 0.4 nozzle`.
- Winkle PETG Jet Black, negro, 1,75 mm. El identificador embebido de filamento es `Winkle PETG Jet Black 1.75 mm`. Lote y estado físico de secado: no disponibles en este trabajo. El perfil es candidato, no una calibración física aceptada.
- Antes de imprimir se propone SUNLU S2 a **55 °C durante 6 h**, material PETG y LED opcional. Retirar bolsas, comprobar giro libre y recorrido al extrusor. Durante alimentación, mantener 55 °C y un temporizador que cubra el trabajo: 12 h para un módulo, 8 h para la tapa y 3 h para un inserto. La lectura RH no demuestra humedad del filamento. Es una receta inicial basada en la ficha local del S2, sin secado ejecutado por el agente.

## Parámetros efectivos comunes

| Grupo | Valores |
| --- | --- |
| Capas | 0,20 mm; primera capa 0,24 mm |
| Temperaturas | Boquilla 230 °C y cama 70 °C, incluida primera capa |
| Filamento | Flujo 1,00; máximo volumétrico 8 mm³/s; densidad 1,23 g/cm³ |
| Anchos | Exterior y sólidos 0,42 mm; pared interna y relleno 0,45 mm |
| Velocidades | Primera capa y su relleno 20; exterior 35; interior y relleno 45; sólido 40; superficie superior 30; puentes 20; viajes 120 mm/s |
| Aceleraciones | Normal/interior/viajes 1000; primera capa 500; exterior 800 mm/s²; puente 50 % de la normal |
| Retracción | 0,8 mm a 30 mm/s; recuperación configurada a 0, que usa la velocidad de retracción |
| Pressure advance | Desactivado; se conserva el valor 0,02 sin aplicarlo |
| Ventilación | 0 % en primera capa; mínimo/máximo 100 %, completo desde capa 2 |
| Cubiertas | 5 capas superiores y 6 inferiores |
| Compensaciones | Contorno, agujero y elefant foot a 0; escala 1:1 |
| Secuencia | Un objeto, una placa y un solo filamento por proyecto |

La temperatura, el flujo, el máximo volumétrico, las retracciones y la ventilación son valores de receta, pendientes de comprobar con la bobina real. Los límites máximos Marlin de máquina se conservan, pero las velocidades solicitadas de impresión son las indicadas arriba. Los parámetros completos relevantes de cada archivo están en [comprobacion-laminado.json](comprobacion-laminado.json), con configuración de proyecto y valores extraídos del bloque efectivo de G-code.

## Piezas y estimaciones por impresión

| Pieza | Unidades necesarias | Paredes / gyroid | Soportes generados | Brim exterior | Capas | Tiempo estimado de impresión (Orca) | PETG | G-code |
| --- | ---: | --- | --- | ---: | ---: | --- | ---: | --- |
| Módulo soporte | 2 | 5 / 30% | Árbol | 5 mm | 779 | 9h 34m 20s | 69.63 g | [VBMOD.GCO](VBMOD.GCO) |
| Tapa de suspensión | 1 | 6 / 40% | Normal snug | 5 mm | 594 | 6h 42m 48s | 77.92 g | [VBTAPA.GCO](VBTAPA.GCO) |
| Inserto de microfauna | 2 | 3 / 15% | No | 5 mm | 710 | 1h 16m 46s | 11.40 g | [VBINS.GCO](VBINS.GCO) |
| Probeta de mástil | 1 | 5 / 30% | No | 3 mm | 125 | 12m 20s | 0.96 g | [VBMAST.GCO](VBMAST.GCO) |
| Calibre de agujero | 1 | 3 / 20% | No | 3 mm | 15 | 2m 4s | 0.41 g | [VBHOLE.GCO](VBHOLE.GCO) |
| Probeta de gancho | 1 | 5 / 30% | No | 3 mm | 118 | 10m 1s | 1.02 g | [VBHOOK.GCO](VBHOOK.GCO) |
| Probeta de receptor | 1 | 5 / 30% | Sí | 3 mm | 44 | 7m 52s | 1.05 g | [VBRCVR.GCO](VBRCVR.GCO) |
| Probeta de cristal | 1 | 5 / 30% | No | 3 mm | 100 | 23m 23s | 3.85 g | [VBCGLS.GCO](VBCGLS.GCO) |
| Probeta de cristal — ajuste 6/6,25/6,5 mm | 1 | 5 / 30% | No | 3 mm | 100 | 28m 36s | 5.05 g | [VBCGL2.GCO](VBCGL2.GCO) |

Cada G-code imprime **una sola unidad**. Repetir dos veces el archivo del módulo y dos veces el del inserto para el conjunto completo. El conjunto funcional (dos módulos, tapa y dos insertos) suma **28 h 25 min 20 s y 239,98 g**. Las cinco probetas originales añaden 55 min 40 s y 7,29 g; la nueva variante de cristal añade 28 min 36 s y 5,05 g. Las seis probetas suman **1 h 24 min 16 s y 12,34 g**; el total de las once impresiones es **29 h 49 min 36 s y 252,32 g**. Son estimaciones nativas, sin aplicar factores medidos en otras geometrías o materiales.

## Orientación, soportes y adhesión

Módulo: vertical, base sobre cama. Una posición acostada reduciría altura y podría favorecer la dirección de algunas cargas, pero exigiría soporte bajo numerosos mástiles y receptores; se conserva la orientación acordada. Soporte de árbol automático desde cama, umbral 30°, con omisión de puentes. Debe retirarse sin dañar las caras de los ganchos y comprobarse el ajuste antes de suspender peso.

Tapa: lateral, +90° en X, para situar las escuadras XZ en el plano de las capas. La alternativa vertical tendría menor altura y algunos apoyos más directos, pero solicitaría de otra manera las uniones entre capas. Se prioriza el recorrido de carga de las escuadras; se añade soporte normal snug automático en todas partes porque los salientes y el bastidor quedan a distintas alturas. Revisar la retirada de los soportes de las cuatro ventanas receptoras. Esta orientación no demuestra resistencia del conjunto.

Inserto: vertical sobre su cruz y láminas inferiores, sin soportes habilitados ni trayectorias de soporte generadas. Conserva los pequeños voladizos de 2,3 mm, puentes de ventanas de 4 mm y techo en lágrima. Imprimir una unidad de prueba y comprobar adherencia, estabilidad de las láminas, retirada y espacio con las bolas reales.

Probetas de unión: orientación de CAD y una por placa. La del gancho lleva soporte de árbol habilitado, pero Orca no genera trayectorias de soporte en esta geometría. La del receptor genera soporte. Ambas probetas de cristal se imprimen con su cara continua apoyada en la cama y las ranuras abiertas hacia arriba; tienen soportes desactivados, brim de 3 mm y puentes internos breves. La primera serie tiene ranuras de 7, 8 y 9 mm: la de 9 mm representa 6 mm de vidrio + 1 mm de acolchado por cara + 0,5 mm de holgura por cara. La ranura de 7 mm presentó juego en la prueba. La segunda serie tiene ranuras de 6,00, 6,25 y 6,50 mm; la de 6,00 mm entra en el vidrio real con margen muy estrecho y ajuste satisfactorio. El resultado es cualitativo y se limita a esa muestra de vidrio, PETG y proceso; no establece una compensación universal ni valida la silla completa con acolchado.

Soportes de las piezas que los generan: separación Z superior/inferior 0,20 mm, XY 0,35 mm, dos capas de interfaz, espaciado de base 2,5 mm e interfaz 0,5 mm. Su desprendimiento en PETG no está validado. Adhesión mediante brim exterior de 5 mm para piezas completas y 3 mm para probetas, con separación objeto/brim de 0,1 mm. Sin raft.

Las capas auxiliares de soporte de la tapa tienen altura independiente: por eso el contador de capas supera el resultado de dividir 81 mm por 0,20 mm. El Z de la pieza laminada puede superar unas centésimas la cota CAD por la discretización de capas.

## Comprobaciones

- Los ocho procesos CLI originales y el proceso de la nueva variante terminaron con código 0 y produjeron G-code y 3MF laminado.
- Los nueve 3MF laminados tienen ZIP íntegro y contienen exactamente el mismo G-code que sus archivos cortos de entrega.
- El proyecto preparado y el 3MF laminado de la nueva variante se abrieron en OrcaSlicer; el registro completo es [apertura-orca.json](apertura-orca.json).
- Se analizaron todos los movimientos G0/G1, incluidos modo relativo, purga y aparcado. No hay G2/G3. X/Y permanecen entre 0 y 180 mm y el Z máximo, incluida retirada final de 5 mm, es 160,84 mm en el módulo.
- La configuración de conexión y los campos de credenciales comprobados quedan vacíos. No se envió ningún trabajo a una impresora.
- Revisión visual global de las vistas previas en Orca para [módulo](laminados/modulo/vista-previa.png), [tapa](laminados/tapa/vista-previa.png) e [inserto](laminados/inserto/vista-previa.png). La geometría de la nueva probeta se revisó en Orca; su estimación es de 28m 36s y 5,05 g. No se afirma una inspección manual exhaustiva de cada capa; las seis probetas tienen apertura y análisis de G-code comprobados, sin captura de preview de capas.
- **Validación física comunicada por el usuario (11-10-2026):** todas las probetas se imprimieron. La ranura de 6,00 mm entra en el vidrio con margen muy estrecho y ajuste satisfactorio; el mástil encaja en el círculo y en una biobola real; la presilla y el receptor funcionan. Es una aceptación cualitativa de encajes individuales en las piezas ensayadas. No se conocen calibre usado, ciclos, fuerza de montaje ni ensayo de carga.
- Estos resultados no validan la retirada de soportes en la tapa funcional, la silla con acolchado, la resistencia del conjunto, su comportamiento en húmedo ni la función biológica de los insertos. La carga suspendida aún debe ensayarse fuera del acuario.

## Proyectos y trazabilidad

| Pieza | Proyecto preparado | Proyecto laminado | G-code | SHA-256 G-code |
| --- | --- | --- | --- | --- |
| Módulo soporte | [modulo--kp3-winkle-petg.3mf](modulo--kp3-winkle-petg.3mf) | [3MF laminado](laminados/modulo/modulo-laminado.3mf) | [VBMOD.GCO](VBMOD.GCO) | `b12adb1dbec5958a5729631e47a93a847fe7f04b9c08e055ffca9608c2520251` |
| Tapa de suspensión | [tapa--kp3-winkle-petg.3mf](tapa--kp3-winkle-petg.3mf) | [3MF laminado](laminados/tapa/tapa-laminado.3mf) | [VBTAPA.GCO](VBTAPA.GCO) | `a6782799a908e0092c2b01fde8fd5e0f601f164fde59f589f7d0d513437414d2` |
| Inserto de microfauna | [inserto--kp3-winkle-petg.3mf](inserto--kp3-winkle-petg.3mf) | [3MF laminado](laminados/inserto/inserto-laminado.3mf) | [VBINS.GCO](VBINS.GCO) | `300d2aa722f0cb0acc41615b18db272a6c9452d4d3d9b2d0215f11a9494fb989` |
| Probeta de mástil | [probeta-mastil--kp3-winkle-petg.3mf](probeta-mastil--kp3-winkle-petg.3mf) | [3MF laminado](laminados/probeta-mastil/probeta-mastil-laminado.3mf) | [VBMAST.GCO](VBMAST.GCO) | `098b1699739e4d5fc460dc640c5f2012879fbe95484b8fa51fc5846da99d7918` |
| Calibre de agujero | [probeta-agujero--kp3-winkle-petg.3mf](probeta-agujero--kp3-winkle-petg.3mf) | [3MF laminado](laminados/probeta-agujero/probeta-agujero-laminado.3mf) | [VBHOLE.GCO](VBHOLE.GCO) | `d45c5628c3ab681eaee2ddbe50e102234ba1ed07a8a5424bb4aaa9552c92ef14` |
| Probeta de gancho | [probeta-gancho--kp3-winkle-petg.3mf](probeta-gancho--kp3-winkle-petg.3mf) | [3MF laminado](laminados/probeta-gancho/probeta-gancho-laminado.3mf) | [VBHOOK.GCO](VBHOOK.GCO) | `b3e94d3e4800beb231148480a0a0d5f4fd000a6946db8541b88e438404c79e0b` |
| Probeta de receptor | [probeta-receptor--kp3-winkle-petg.3mf](probeta-receptor--kp3-winkle-petg.3mf) | [3MF laminado](laminados/probeta-receptor/probeta-receptor-laminado.3mf) | [VBRCVR.GCO](VBRCVR.GCO) | `19e69b9a7fa0aeaae1a39b83083da74d3ca898e5285dac0ae5e0cb03896aa07e` |
| Probeta de cristal | [probeta-cristal--kp3-winkle-petg.3mf](probeta-cristal--kp3-winkle-petg.3mf) | [3MF laminado](laminados/probeta-cristal/probeta-cristal-laminado.3mf) | [VBCGLS.GCO](VBCGLS.GCO) | `4fab06f85aba9bd3f21228e2811af3c393c3056c2bd7647d0fab202e05ef1067` |
| Probeta cristal — ajuste | [probeta-cristal-ajuste--kp3-winkle-petg.3mf](probeta-cristal-ajuste--kp3-winkle-petg.3mf) | [3MF laminado](laminados/probeta-cristal-ajuste/probeta-cristal-ajuste-laminado.3mf) | [VBCGL2.GCO](VBCGL2.GCO) | `84da6e05e517dbe1ce6e53aaa8ec9c025a0e3bfcdc55e138fe94a5cea312f473` |

Las sumas SHA-256 de los STL, proyectos preparados, proyectos laminados, el tamaño de cada G-code y su marca de generación tomada de la cabecera están en [comprobacion-laminado.json](comprobacion-laminado.json). El STL de la segunda serie está en [modelos/probeta-cristal-6_00-6_25-6_50.stl](modelos/probeta-cristal-6_00-6_25-6_50.stl). Los logs CLI se conservan junto a cada proyecto laminado. Un cambio de CAD o de receta obliga a regenerar los derivados y sus sumas.

## Uso y pendientes

Compatibilidad de esta entrega: **Kingroon KP3 KP3-3DP180, boquilla 0,4 mm y Winkle PETG Jet Black 1,75 mm con las recetas aquí descritas**. Copiar el archivo ASCII corto correspondiente a microSD. No se ha copiado a una tarjeta, enviado ni iniciado una impresión.

Las probetas están impresas y los encajes indicados arriba han sido aceptados cualitativamente. Antes de fabricar el conjunto completo, revisar la retirada de soportes de la tapa y confirmar el contacto de la silla y el acolchado. Después, ensayar la suspensión completa fuera del acuario con la carga real, incluyendo reacciones de giro. La pieza no se considera aceptada para uso por disponer de G-code ni por superar estas probetas de encaje.

La comprobación documental `git diff --check` y los enlaces de esta entrega pasan. El validador general de Documents sigue detectando dos entradas previas ajenas al laminado: `00000.log` y `662F23 _documentos`.
