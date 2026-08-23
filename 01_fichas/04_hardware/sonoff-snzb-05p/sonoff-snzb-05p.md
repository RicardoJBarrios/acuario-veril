# SONOFF SNZB-05P

## Identificación

- **Fabricante:** SONOFF
- **Modelo:** SNZB-05P
- **Tipo:** Sensor Zigbee de fugas de agua
- **Protocolo:** Zigbee 3.0
- **Accesorio incluido:** Cable de detección extendido SONOFF WLDC200

## Ficha normalizada

| Campo | Valor |
| --- | --- |
| `hardware_id` | `SONOFF_SNZB_05P` |
| `category` | `aquarium_leak_detection` |
| `vendor` | `SONOFF` |
| `model` | `SNZB-05P` |
| `hardware_kind` | `physical` |
| `physical_type` | `zigbee_water_leak_sensor` |
| `protocol` | Zigbee 3.0 |
| `accessory` | SONOFF WLDC200 |
| `measurement` | Presencia de agua |

## Función en Veril

El sensor se colocará para detectar agua en zonas donde una fuga o un desbordamiento pueda causar daños. El sensor puntual y el cable extendido permitirán cubrir tanto una zona concreta como un recorrido de detección. Home Assistant recibirá el estado de fuga y generará un aviso.

La detección de agua no mide el nivel del display, el nivel del sump ni el funcionamiento del ATO. No sustituye la inspección física ni las protecciones propias de la instalación.

## Especificaciones

| Parámetro | Valor declarado |
| --- | --- |
| Alimentación | Pila CR2477 |
| Comunicación | Zigbee 3.0 |
| Protección del cuerpo | IP67 |
| Temperatura de funcionamiento | −10–60 °C |
| Humedad de funcionamiento del sensor | 0–100 % HR |
| Distancia de comunicación publicada | Hasta 130 m en espacio abierto |
| Dimensiones del sensor | 48 × 48 × 21,6 mm |
| Peso neto publicado | 34,3 g, sin pila |
| Altura mínima de detección anunciada | 0,5 mm |
| Altitud máxima declarada | <5000 m |
| Cable incluido | SONOFF WLDC200 |
| Longitud del cable incluido | 2 m |
| Humedad de funcionamiento del cable | 0–80 % HR, sin condensación |

El cable WLDC200 puede conectarse en serie con otros cables sin límite total de longitud declarado por SONOFF. Después de mojarse debe secarse completamente antes de reutilizarlo. Una humedad ambiental excesiva puede provocar detecciones falsas.

El manual oficial indica una autonomía declarada de hasta cinco años con una frecuencia de 50 detecciones diarias. Es una cifra de referencia del fabricante, no una duración garantizada en la instalación de Veril.

## Instalación en Veril

- Colocar el sensor en el punto donde deba detectarse la acumulación de agua
- Tender el WLDC200 por la zona de riesgo sin dejarlo en contacto permanente con agua
- Mantener el cuerpo y la pila accesibles para inspección y sustitución
- Evitar que el cable forme bolsas donde se acumule condensación de manera permanente
- Probar el sensor con agua y confirmar la recuperación después del secado
- No utilizarlo como sensor sumergible ni como medidor continuo de nivel

## Datos disponibles en Zigbee2MQTT

Zigbee2MQTT expone el estado de fuga, el nivel de batería, el aviso de batería baja y las actualizaciones OTA. La integración completa con Home Assistant está en [Home Assistant y Zigbee2MQTT](home-assistant-zigbee2mqtt.md).

## Limitaciones

- Una detección de fuga no identifica el origen ni el volumen de agua
- La batería baja puede impedir la transmisión de un aviso si no se atiende
- La humedad excesiva puede generar falsos positivos en el cable
- El cable debe secarse completamente antes de volver a usarlo tras una detección
- El cuerpo está especificado para uso interior y no debe darse por apto para inmersión continua
- La disponibilidad Zigbee depende del coordinador, la red mallada y la ubicación

## Fuentes

- [Manual local del cable WLDC200, versión 2.0](wldc200-manual-v2-0.pdf)
- [Página oficial del SONOFF SNZB-05P](https://sonoff.tech/en-us/products/sonoff-zigbee-water-leak-sensor-snzb-05p/58)
- [Manual oficial del SNZB-05P](https://support.sonoff.tech/snzb-05p-usermanual/)
- [Cable de detección SONOFF WLDC200](https://sonoff.tech/es-es/products/sonoff-water-leak-detection-cable)
- [SONOFF SNZB-05P en Zigbee2MQTT](https://www.zigbee2mqtt.io/devices/SNZB-05P.html)
