"""Informe humano generado de los valores auditados, sin estimaciones inventadas."""
from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'impresion'
report=json.loads((OUT/'comprobacion-laminado.json').read_text())
generation=json.loads((OUT/'generacion.json').read_text())


def seconds(text):
    return sum(int(v)*{'h':3600,'m':60,'s':1}[unit] for v,unit in re.findall(r'(\d+)([hms])',text))


def duration(sec):
    return str(sec//3600)+' h '+str(sec%3600//60)+' min '+str(sec%60)+' s'


rows=[];total_time=0;total_mass=0
for job in report['jobs']:
    g=job['gcode_check'];repeat=job['repeat_count']
    rows.append('| '+job['slug']+' | '+str(job['objects'])+' | '+str(repeat)+' | '+
        str(g['layers'])+' | '+str(g['estimated_time'])+' | '+str(g['estimated_mass_g'])+
        ' g | ['+job['gcode']+'](gcode/'+job['gcode']+') |')
    if job['slug']!='probetas':
        total_time+=seconds(g['estimated_time'])*repeat
        total_mass+=g['estimated_mass_g']*repeat
first=report['jobs'][0]['gcode_check']['settings']
param_rows=[]
for label,keys in [
 ('Capas',['layer_height','initial_layer_print_height']),
 ('Temperaturas',['nozzle_temperature','nozzle_temperature_initial_layer','hot_plate_temp','hot_plate_temp_initial_layer']),
 ('Flujo y caudal',['filament_flow_ratio','filament_max_volumetric_speed','filament_density']),
 ('Velocidades, mm/s',['initial_layer_speed','initial_layer_infill_speed','outer_wall_speed','inner_wall_speed','sparse_infill_speed','internal_solid_infill_speed','top_surface_speed','bridge_speed','travel_speed']),
 ('Aceleraciones, mm/s²',['default_acceleration','outer_wall_acceleration','inner_wall_acceleration','initial_layer_acceleration']),
 ('Retracción',['retraction_length','retraction_speed','deretraction_speed']),
 ('Pressure advance',['enable_pressure_advance','pressure_advance']),
 ('Ventilación',['fan_min_speed','fan_max_speed','close_fan_the_first_x_layers','full_fan_speed_layer']),
 ('Sección resistente',['wall_loops','sparse_infill_density','sparse_infill_pattern','top_shell_layers','bottom_shell_layers']),
 ('Compensaciones',['xy_hole_compensation','xy_contour_compensation','elefant_foot_compensation']),
]:
    values='; '.join(k+' = '+first[k] for k in keys if k in first)
    param_rows.append('| '+label+' | '+(values or 'no disponible; consultar perfil y verificar en Orca')+' |')
identity=[]
for job in report['jobs']:
    g=job['gcode_check']
    identity.append('| '+job['slug']+' | ['+job['project']+']('+job['project']+') | `'+job['project_sha256']+'` | `'+g['sha256']+'` | '+str(g['bytes'])+' |')
warnings=[]
for job in report['jobs']:
    if job['cli_warning_lines']:warnings.append('- '+job['slug']+': '+str(len(job['cli_warning_lines']))+' líneas de aviso en su log; ver el JSON de comprobación.')
text='''# Fabricación del bastidor de biobolas

Estado: **laminado candidato; impresión, encaje y carga pendientes**. Imprimir
primero [BASTTEST.GCO](gcode/BASTTEST.GCO), medir y seguir el
[procedimiento de validación](../validacion-fisica.md). Los archivos completos
son prototipos del diseño, no piezas físicamente aceptadas.

Fuente editable: [FCStd](../soporte-biobolas-bastidor.FCStd).
SHA-256: `'''+report['source_fcstd_sha256']+'''`.
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
'''+ '\n'.join(rows)+'''

El conjunto completo, sin probetas, suma **'''+duration(total_time)+' y '+format(total_mass,'.2f')+''' g**
según OrcaSlicer. No se aplica ningún factor de tiempo de otras impresiones.
El consumo incluye elementos de adhesión; no es la masa neta instalada.

## Receta efectiva

Valores extraídos del bloque de configuración del G-code. Las configuraciones
completas relevantes de todas las placas están en el JSON; el brim es la
excepción por placa.

| Área | Valores efectivos |
| --- | --- |
'''+ '\n'.join(param_rows)+'''

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

'''+ ('\n'.join(warnings) if warnings else 'No se encontraron líneas de aviso/error en los logs de CLI.')+'''

## Identidad de archivos

| Placa | Proyecto | SHA-256 del 3MF fuente | SHA-256 del G-code | Bytes G-code |
| --- | --- | --- | --- | --- |
'''+ '\n'.join(identity)+'''

Compatibilidad limitada a KP3-3DP180, boquilla de 0,4 mm, Winkle PETG Jet Black
y esta receta candidata. Copiar el archivo ASCII correspondiente a microSD;
no se ha copiado, enviado ni iniciado una impresión. Antes de fabricar, revisar
primera capa, adhesión, espacio, ventanas y puentes. Confirmar los encajes con
la placa de probetas antes de fabricar las piezas completas.
'''
(OUT/'README.md').write_text(text)
print('INFORME',duration(total_time),format(total_mass,'.2f')+' g')
