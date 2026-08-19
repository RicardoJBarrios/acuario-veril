# ZG-109TDS: Home Assistant y Zigbee2MQTT

## Integración

El ZG-109TDS se integrará mediante un coordinador compatible con Zigbee2MQTT y Home Assistant. Zigbee2MQTT identifica el dispositivo como **Excellux ZG-109TDS**. No se utilizará el SONOFF ZBBridge-P ni se asumirá compatibilidad con eWeLink, Tuya, Smart Life o ZHA.

## Entidades publicadas

| Entidad | Tipo | Lectura o control |
| --- | --- | --- |
| `probe_temperature_warning` | Estado | Aviso de sonda: `none`, `low` o `high` |
| `temperature_warning` | Estado | Aviso de temperatura ambiente: `none`, `low` o `high` |
| `humidity_warning` | Estado | Aviso de humedad: `none`, `low` o `high` |
| `tds_warning` | Estado | Aviso de TDS alto |
| `ec_warning` | Estado | Aviso de EC: `none`, `low` o `high` |
| `mode` | Selector | `freshwater` o `seawater` |
| `battery` | Sensor | Batería en % |
| `probe_temperature` | Sensor | Temperatura de la sonda en °C |
| `temperature` | Sensor | Temperatura del aire en °C |
| `humidity` | Sensor | Humedad relativa en % |
| `tds` | Sensor | TDS en ppm |
| `salinity` | Sensor | Salinidad en ‰ |
| `ec` | Sensor | Conductividad a 25 °C en µS/cm |
| `sg` | Sensor | Gravedad específica |
| `sampling_interval` | Número | Intervalo de muestreo entre 5 y 1200 s |

## Calibraciones y umbrales configurables

Zigbee2MQTT permite publicar o modificar, según la versión instalada:

- `probe_temperature_calibration`: corrección entre −2 y +2 °C
- `probe_temperature_v0_set` y `probe_temperature_v1_set`: límites de sonda entre −40 y 125 °C
- `tds_warning_set`: umbral de TDS entre 0 y 13.000 ppm
- `ec_v0_set` y `ec_v1_set`: límites de EC entre 0 y 20.000 µS/cm
- `temperature_calibration`: corrección entre −2 y +2 °C
- `temperature_v0_set` y `temperature_v1_set`: límites de temperatura entre −40 y 85 °C
- `humidity_calibration`: corrección entre −10 y +10 %
- `humidity_v0_set` y `humidity_v1_set`: límites de humedad entre 0 y 100 %

Las opciones de precisión de temperatura y humedad también pueden reducir los decimales publicados. No aumentan la exactitud física del instrumento.

## Uso en Veril

Home Assistant podrá registrar las magnitudes, avisar de límites y detectar cambios de modo o de disponibilidad. Antes de automatizar avisos se comprobarán:

- El modo `seawater`
- La unidad de salinidad publicada en ‰
- La correspondencia entre `probe_temperature` y el termómetro independiente
- La correspondencia entre `sg`, salinidad y refractómetro
- La respuesta de `sampling_interval`
- Los umbrales y las calibraciones

El equipo no se utilizará para dosificar sal, realizar cambios de agua ni corregir química automáticamente.

## Prueba de aceptación

- Emparejar el ZG-109TDS con el coordinador Zigbee2MQTT
- Confirmar todas las entidades publicadas
- Seleccionar `seawater` y comprobar que el cambio queda retenido
- Comparar temperatura, salinidad y gravedad específica con instrumentos independientes
- Probar la frecuencia de muestreo y el histórico en Home Assistant
- Probar umbrales de temperatura, humedad, TDS y EC
- Confirmar el comportamiento tras reiniciar Zigbee2MQTT y Home Assistant
- Verificar la batería y la disponibilidad Zigbee

## Límites

- La lista de entidades depende de la versión de Zigbee2MQTT y del firmware
- El `sg` publicado por Zigbee2MQTT muestra un rango de 1,000–1,100, distinto del rango del manual adjunto; debe comprobarse en el dispositivo real
- La conductividad publicada no se considerará válida para agua marina sin comparación independiente
- Las alarmas de Zigbee2MQTT no sustituyen la observación del acuario ni los tests de referencia

## Fuentes

- [Excellux ZG-109TDS en Zigbee2MQTT](https://www.zigbee2mqtt.io/devices/ZG-109TDS.html)
- [Guía de MQTT de Zigbee2MQTT](https://www.zigbee2mqtt.io/guide/usage/mqtt_topics_and_messages.html)
- [Ficha del Excellux ZG-109TDS](excellux-zg-109tds.md)
