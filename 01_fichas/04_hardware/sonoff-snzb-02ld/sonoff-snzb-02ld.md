# SONOFF SNZB-02LD

## Identificación

- **Fabricante:** SONOFF
- **Modelo:** SNZB-02LD
- **Tipo:** Termómetro Zigbee con pantalla LCD y sonda externa
- **Protocolo:** Zigbee 3.0 / IEEE 802.15.4
- **Gateway previsto:** SONOFF ZBBridge-P

## Ficha normalizada

| Campo | Valor |
| --- | --- |
| `hardware_id` | `SONOFF_SNZB_02LD` |
| `category` | `aquarium_monitoring` |
| `vendor` | `SONOFF` |
| `model` | `SNZB-02LD` |
| `hardware_kind` | `physical` |
| `physical_type` | `zigbee_temperature_sensor_probe` |
| `protocol` | Zigbee 3.0 |
| `gateway` | SONOFF ZBBridge-P |
| `measurement` | Temperatura del agua |

## Función en Veril

El **SONOFF SNZB-02LD** se incorporará como termómetro inalámbrico principal de seguimiento de la temperatura del acuario. La sonda se colocará en el agua del display y el cuerpo electrónico permanecerá fuera de la zona húmeda. La comunicación se realizará mediante el gateway **SONOFF ZBBridge-P**.

El sensor servirá para registrar tendencias y generar avisos de temperatura. No sustituirá la comprobación independiente de la temperatura durante la puesta en marcha ni la verificación periódica del sensor.

## Especificaciones

| Campo | Dato |
| --- | --- |
| Fabricante | SONOFF |
| Modelo | SNZB-02LD |
| Tipo | Termómetro Zigbee con pantalla LCD y sonda externa |
| Comunicación | Zigbee 3.0 / IEEE 802.15.4 |
| Gateway previsto | SONOFF ZBBridge-P |
| Alimentación | 3 V, pila CR2477 |
| Pantalla | LCD de aproximadamente 5,6 cm |
| Dimensiones del cuerpo | 62,8 × 58,5 × 21,8 mm |
| Material del cuerpo | PC + ABS |
| Peso neto publicado | 86,2 g, con cables |
| Longitud de la sonda | 1,5 m |
| Tolerancia de temperatura declarada | ±0,5 °C |
| Protección del cuerpo | IP65 |
| Temperatura de funcionamiento del cuerpo | −10–60 °C según el PDF oficial V1.0 |
| Humedad de funcionamiento del cuerpo | 0–100 % HR según el PDF oficial V1.0 |
| Temperatura de funcionamiento de la sonda | −40–115 °C según el PDF oficial V1.0 |
| Altura máxima de instalación declarada | <2000 m |

## Instalación

- Fijar únicamente la sonda en una zona representativa del agua
- Mantener el cuerpo y la tapa de la pila fuera del acuario y protegidos de salpicaduras directas
- Evitar que la sonda quede contra un calentador, una bomba, la iluminación o una pared sometida a radiación directa
- Comprobar que la longitud de 1,5 m permite colocar el cuerpo en una zona seca sin tensar el cable
- Verificar la lectura frente a un termómetro independiente antes de usar avisos o automatizaciones

IP65 no significa que el cuerpo pueda sumergirse. La protección está pensada para salpicaduras y chorros de baja presión; no se expondrá el módulo a inmersión, condensación persistente ni chorros de agua salada.

## Datos disponibles en Zigbee2MQTT

Zigbee2MQTT expone para este modelo:

- Batería restante en porcentaje
- Temperatura de la sonda en °C
- Unidad mostrada en pantalla: `celsius` o `fahrenheit`
- Calibración de temperatura mediante una corrección entre −50 y +50 °C
- Actualización OTA

La calibración y la precisión configurable aparecen como opciones del dispositivo. La integración completa con Home Assistant está en [Home Assistant y Zigbee2MQTT](home-assistant-zigbee2mqtt.md).

El manual permite emparejar el sensor con un SONOFF ZBBridge-P. El alta se realiza desde eWeLink: se mantiene pulsado el botón durante cinco segundos, el indicador entra en modo de emparejamiento durante aproximadamente 180 segundos y se selecciona el gateway Zigbee.

El gateway, la cobertura real y la publicación de la temperatura se comprobarán en la ubicación definitiva. Una lectura disponible en la aplicación no demuestra por sí sola que la sonda esté bien colocada ni que su valor sea correcto.

## Limitaciones

- El dispositivo mide temperatura; no mide salinidad, pH, alcalinidad, nutrientes ni nivel de agua
- La tolerancia declarada no sustituye una comparación con un instrumento independiente
- El cuerpo IP65 no debe sumergirse
- La pila CR2477 y la disponibilidad Zigbee deben vigilarse como parte del mantenimiento


## Fuentes

- [Manual local del SNZB-02LD, versión 1.0 en inglés](sonoff-snzb-02ld-manual-en-v1-0.pdf)
- [Página oficial del SONOFF SNZB-02LD](https://sonoff.tech/en-eu/products/sonoff-snzb-02ld-ip65-zigbee-lcd-smart-thermometer-probe-version)
- [Manual oficial del SNZB-02LD](https://support.sonoff.tech/snzb-02ld-usermanual/)
- [Descarga directa del PDF oficial](https://cdn.shopify.com/s/files/1/0742/9963/8001/files/User_Manual_SNZB-02LD_EN_V1.0.pdf?v=1749029821)
