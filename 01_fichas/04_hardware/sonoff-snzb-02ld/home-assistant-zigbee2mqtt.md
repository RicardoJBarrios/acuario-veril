# SONOFF SNZB-02LD: Home Assistant y Zigbee2MQTT

## Integración

El SNZB-02LD se emparejará con un coordinador Zigbee compatible con Zigbee2MQTT y se descubrirá en Home Assistant mediante MQTT Discovery. El gateway SONOFF ZBBridge-P documentado para eWeLink es una ruta distinta y no se considerará el coordinador de esta integración.

## Entidades y controles disponibles

| Entidad o función | Tipo | Uso |
| --- | --- | --- |
| `battery` | Sensor | Batería restante en % |
| `temperature` | Sensor | Temperatura de la sonda en °C |
| `temperature_units` | Selector | Unidad de pantalla: `celsius` o `fahrenheit` |
| `temperature_calibration` | Número | Corrección absoluta entre −50 y +50 °C |
| OTA | Actualización | Actualizar el firmware si Zigbee2MQTT ofrece una imagen compatible |

La opción `temperature_precision` permite reducir el número de decimales publicados, entre 0 y 3; no aumenta la precisión real del sensor.

## Uso en Veril

Home Assistant podrá registrar la temperatura y generar avisos por:

- Temperatura fuera de los límites definidos
- Falta de actualización del sensor
- Batería baja
- Pérdida de disponibilidad Zigbee
- Diferencia sostenida frente al termómetro independiente

La automatización no modificará la temperatura ni actuará sobre un calentador sin una decisión separada y una prueba de seguridad.

## Prueba de aceptación

- Emparejar el sensor y confirmar el descubrimiento MQTT
- Confirmar temperatura, batería y unidad de pantalla
- Comparar la sonda con un termómetro independiente
- Comprobar la calibración con una corrección conocida y devolverla después al valor documentado
- Probar el cambio entre grados Celsius y Fahrenheit
- Comprobar la actualización después de despertar el sensor
- Verificar la recuperación tras una pérdida de cobertura y un reinicio de Zigbee2MQTT
- Confirmar que el cuerpo permanece seco y que solo la sonda queda en el agua

## Límites

- La disponibilidad de OTA, las entidades y las opciones dependen de la versión de Zigbee2MQTT y del firmware
- La batería publicada es una estimación y no una medida directa de autonomía restante
- La corrección no sustituye una calibración física ni un instrumento independiente
- El sensor no mide salinidad, pH, alcalinidad, nutrientes, nivel ni estado del calentador

## Fuentes

- [SONOFF SNZB-02LD en Zigbee2MQTT](https://www.zigbee2mqtt.io/devices/SNZB-02LD.html)
- [Guía de MQTT de Zigbee2MQTT](https://www.zigbee2mqtt.io/guide/usage/mqtt_topics_and_messages.html)
- [Ficha del SONOFF SNZB-02LD](sonoff-snzb-02ld.md)
