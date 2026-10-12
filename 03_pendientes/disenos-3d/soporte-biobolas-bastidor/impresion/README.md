# Fabricación del bastidor de biobolas

**Revisión de simplificación abierta:** estos archivos pertenecen al bastidor
anterior de pasadores y chavetas. La recomendación de imprimirlos queda
suspendida mientras se desarrolla la alternativa con tornillería de plástico.
Consultar la [revisión del diseño](../README.md#revisión-de-simplificación-solicitada).

Estado del antecedente: **laminado candidato; impresión, encaje y carga pendientes**.
El orden previsto comenzaba por [BASTTEST.GCO](gcode/BASTTEST.GCO), medir y seguir el
[procedimiento de validación](../validacion-fisica.md). Los archivos completos
son prototipos del diseño, no piezas físicamente aceptadas.

Fuente editable: [FCStd](../soporte-biobolas-bastidor.FCStd).
SHA-256: `0d0f8379cbb6bc3c4f82101783c6768a08a9fc6232e5b9b60d392e7c17c8ba1f`.
Las mallas se exportaron desde sus cuerpos nativos, con deflexión de 0,05 mm,
soldando vértices coincidentes; no se repararon ni simplificaron las formas.
El marco superior se gira 180° en X; las demás maestras conservan su orientación
de fabricación XY. Las copias se normalizan a Z=0 y se colocan explícitamente
en la cama sin modificar el CAD montado. Los STEP individuales están en
[modelos](modelos/). La receta hereda la identidad y los ajustes KP3/PETG del
proyecto anterior; toda la geometría y los metadatos de objetos se sustituyen.

OrcaSlicer 2.4.2, CLI con `--datadir` temporal independiente por placa, perfiles
embebidos y sin `--no-check`. Cada placa tiene un proyecto 3MF editable, un
3MF laminado y un G-code ligado a esa receta. La
[comprobación completa](comprobacion-laminado.json) conserva parámetros,
huellas, avisos y límites de movimiento. Las fechas UTC de generación están en
[generacion.json](generacion.json).

## Máquina, material y preparación

Kingroon KP3, unidad KP3-3DP180, volumen 180 × 180 × 180 mm, boquilla de
0,4 mm, extrusor directo y lenguaje Marlin. Perfil de impresora:
`Kingroon KP3 (KP3-3DP180) 0.4 nozzle`. Material Winkle PETG Jet Black,
negro, 1,75 mm; perfil `Winkle PETG Jet Black 1.75 mm`. Lote y estado de
secado no disponibles: no se han observado ni ejecutado en este trabajo.

Receta de proceso `Veril bastidor <placa> KP3 PETG 0.20 candidato`. Propuesta
de secado: SUNLU S2 a 55 °C durante 6 h, PETG y LED opcional; retirar bolsas
y comprobar giro y salida. Alimentación desde el S2 a 55 °C con temporizador
que cubra la impresión. La lectura RH no acredita humedad del filamento.

## Placas y estimaciones nativas

Cada G-code imprime los objetos de una sola placa. Repetir la placa el número
indicado para obtener el conjunto; no duplicar de nuevo los 32 cierres o las
10 llaves estructurales, que ya están agrupados.

| Placa | Objetos por placa | Repeticiones | Capas | Tiempo por placa | PETG por placa | G-code |
| --- | --- | --- | --- | --- | --- | --- |
| base | 1 | 2 | 740 | 5h 42m 56s | 44.46 g | [BASTBASE.GCO](gcode/BASTBASE.GCO) |
| panel-a | 1 | 4 | 26 | 2h 38m 58s | 30.75 g | [BASTPA.GCO](gcode/BASTPA.GCO) |
| panel-b | 1 | 4 | 26 | 2h 39m 21s | 30.73 g | [BASTPB.GCO](gcode/BASTPB.GCO) |
| marco-superior | 1 | 2 | 155 | 56m 1s | 7.64 g | [BASTSUP.GCO](gcode/BASTSUP.GCO) |
| tapa | 1 | 1 | 40 | 3h 12m 11s | 38.15 g | [BASTTAPA.GCO](gcode/BASTTAPA.GCO) |
| escuadra | 1 | 2 | 40 | 2h 44m 6s | 33.03 g | [BASTCOLG.GCO](gcode/BASTCOLG.GCO) |
| asa | 1 | 1 | 40 | 1h 14m 2s | 14.47 g | [BASTASA.GCO](gcode/BASTASA.GCO) |
| cierres-panel | 64 | 1 | 20 | 55m 21s | 7.89 g | [BASTPIN.GCO](gcode/BASTPIN.GCO) |
| cierres-estructurales | 20 | 1 | 26 | 43m 41s | 7.02 g | [BASTSEG.GCO](gcode/BASTSEG.GCO) |
| probetas | 15 | 1 | 155 | 2h 31m 29s | 26.98 g | [BASTTEST.GCO](gcode/BASTTEST.GCO) |

El conjunto completo, sin probetas, suma **46 h 4 min 37 s y 483.71 g**
según OrcaSlicer. No se aplica ningún factor de tiempo de otras impresiones.
El consumo incluye elementos de adhesión; no es la masa neta instalada.

## Receta efectiva

Valores extraídos del bloque de configuración del G-code. Las configuraciones
completas relevantes de todas las placas están en el JSON; el brim es la
excepción por placa.

| Área | Valores efectivos |
| --- | --- |
| Capas | layer_height = 0.2; initial_layer_print_height = 0.24 |
| Temperaturas | nozzle_temperature = 230; nozzle_temperature_initial_layer = 230; hot_plate_temp = 70; hot_plate_temp_initial_layer = 70 |
| Flujo y caudal | filament_flow_ratio = 1; filament_max_volumetric_speed = 8; filament_density = 1.23 |
| Velocidades, mm/s | initial_layer_speed = 20; initial_layer_infill_speed = 20; outer_wall_speed = 35; inner_wall_speed = 45; sparse_infill_speed = 45; internal_solid_infill_speed = 40; top_surface_speed = 30; bridge_speed = 20; travel_speed = 120 |
| Aceleraciones, mm/s² | default_acceleration = 1000; outer_wall_acceleration = 800; inner_wall_acceleration = 1000; initial_layer_acceleration = 500 |
| Retracción | retraction_length = 0.8; retraction_speed = 30; deretraction_speed = 0 |
| Pressure advance | enable_pressure_advance = 0; pressure_advance = 0.02 |
| Ventilación | fan_min_speed = 100; fan_max_speed = 100; close_fan_the_first_x_layers = 1; full_fan_speed_layer = 2 |
| Sección resistente | wall_loops = 6; sparse_infill_density = 100%; sparse_infill_pattern = rectilinear; top_shell_layers = 5; bottom_shell_layers = 6 |
| Compensaciones | xy_hole_compensation = 0; xy_contour_compensation = 0; elefant_foot_compensation = 0 |

Soportes desactivados en todas las placas; los G-code y las estadísticas del
3MF laminado no contienen soporte generado. Brim exterior de 5 mm para las
piezas grandes y de 3 mm para cierres y probetas, separación de 0,1 mm y sin
raft. Las ventanas horizontales pequeñas generan puentes: su calidad física
debe comprobarse con las muestras. No hay soportes atrapados que retirar.

## Verificación y límites

Las diez estructuras ZIP/3MF y sus mallas cerradas pasan la auditoría. Los
G-code embebidos coinciden byte a byte con los entregados. Orca declara
`support_used=false` y `outside=false`. Se interpretaron G90, G91, G92 y G28
y todos los movimientos XYZ: no se detectan movimientos fuera de 0–180 mm.
No hay movimientos de arco que queden fuera de esa comprobación.

La revisión digital no sustituye la impresión ni el ensayo de puentes,
retención, carga, mantenimiento e inmersión. La apertura real y la revisión
visual se registran por separado; consultar [apertura y vistas](apertura-orca.json).

No se encontraron líneas de aviso/error en los logs de CLI.

## Identidad de archivos

| Placa | Proyecto | SHA-256 del 3MF fuente | SHA-256 del G-code | Bytes G-code |
| --- | --- | --- | --- | --- |
| base | [base--kp3-winkle-petg.3mf](base--kp3-winkle-petg.3mf) | `a3357ea85c6f2babc2a7fe99629d0aea9ef6a00475819f460629755aee21bb6e` | `0084f9d3611b7bd202a087e6a9614886e737e02f460c36a7f484b45f206b287b` | 11384376 |
| panel-a | [panel-a--kp3-winkle-petg.3mf](panel-a--kp3-winkle-petg.3mf) | `6cba8d624e9a25974431391144fd4fd7618027caf060aa99dfebed1e0a1d01f3` | `4d0c94575f30fe64cebbd4759c82cccf71a5fc034881633ba9d5d01052c70001` | 1922249 |
| panel-b | [panel-b--kp3-winkle-petg.3mf](panel-b--kp3-winkle-petg.3mf) | `82d23ff90d4bc2e16c0f1b995c40ada93cf17cf1c678356dba53967c42b14043` | `f5215b28ef2e47225444db813c851abdea808b8c2a66099d2f1953351de96235` | 1942135 |
| marco-superior | [marco-superior--kp3-winkle-petg.3mf](marco-superior--kp3-winkle-petg.3mf) | `696f5c090e100171873c14d091bbd92507b130e58b6df75b825e80e61bd8d174` | `fad646a5756cf3467c6050b035a18112c0e3abe02ffa61a60cc934bdf5c7d935` | 1017303 |
| tapa | [tapa--kp3-winkle-petg.3mf](tapa--kp3-winkle-petg.3mf) | `6844871e87f74171c47fe1ba7203c8cf8c6d0a6fcad0e5eae7abec4590cf9e0d` | `2982dc82e8d6f060455344bd6f137863b04e5204a20af35f0b45cf0fd0f998e6` | 1974079 |
| escuadra | [escuadra--kp3-winkle-petg.3mf](escuadra--kp3-winkle-petg.3mf) | `65048a3859d7d207644d0d59f6a98d7a76839ad3f7648d244677f8b35f60f936` | `1e5b397f638b9aa5e6cd5a8af213606355b69ef0e46fe014b341b22efc9ee4c9` | 1469947 |
| asa | [asa--kp3-winkle-petg.3mf](asa--kp3-winkle-petg.3mf) | `d91b1e5d4d713fba05c055c8c7c98e5f011ae2d80053e2ebdf10a16384a9a00a` | `83982423cc59d17d39b27abc5c72205229432cc9bbc54a16a0ff781e4be0aa11` | 857358 |
| cierres-panel | [cierres-panel--kp3-winkle-petg.3mf](cierres-panel--kp3-winkle-petg.3mf) | `0aacbcd40170d1ffa2612b674dac0ecb7dfb04b8263fb15034e7a99f87c8a033` | `0173725890044e01163eb05ab8351968804e61d3b1f8d6ea3f07f4272c9b0b13` | 1673648 |
| cierres-estructurales | [cierres-estructurales--kp3-winkle-petg.3mf](cierres-estructurales--kp3-winkle-petg.3mf) | `a0e9e351c4a8906a04c6d380c2c4788479e5da1055adf85df2a7e6bb2025debf` | `b10c14ec52c9177a7433bab8487c2ddc999a8d25c6ddeb82fae3b52be471daed` | 926419 |
| probetas | [probetas--kp3-winkle-petg.3mf](probetas--kp3-winkle-petg.3mf) | `9f4bc14f157919a4e5884138fd1df5eabf051094d6e66c52acf77b8bfa61d3dd` | `d423ff4bef912872b09082236b5b914329dc1d3a765707a5fa151bfa05ee2d3b` | 1971066 |

Compatibilidad limitada a KP3-3DP180, boquilla de 0,4 mm, Winkle PETG Jet Black
y esta receta candidata. Copiar el archivo ASCII correspondiente a microSD;
no se ha copiado, enviado ni iniciado una impresión. Antes de fabricar, revisar
primera capa, adhesión, espacio, ventanas y puentes. Confirmar los encajes con
la placa de probetas antes de fabricar las piezas completas.
