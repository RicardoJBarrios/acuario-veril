# SONOFF SNZB-05P: Home Assistant y Zigbee2MQTT

## Integración

El SNZB-05P se emparejará con un coordinador Zigbee compatible con Zigbee2MQTT y se descubrirá en Home Assistant mediante MQTT Discovery. También es compatible con gateways SONOFF en eWeLink, pero la integración documentada aquí utiliza Zigbee2MQTT.

## Entidades y funciones disponibles

| Entidad o función | Tipo | Uso |
| --- | --- | --- |
| `water_leak` | Binario | Indica si se ha detectado agua |
| `battery` | Sensor | Batería restante en % |
| `battery_low` | Binario | Indica batería próxima a agotarse |
| OTA | Actualización | Actualizar el firmware si Zigbee2MQTT ofrece una imagen compatible |

El sensor no ofrece en Zigbee2MQTT una medida continua de nivel, caudal, humedad ambiental ni longitud de cable mojada. El accesorio WLDC200 forma parte del circuito de detección y se refleja en el estado binario `water_leak`.

Con firmware igual o posterior a la versión 1.0.2, el manual oficial indica que el dispositivo puede reenviar el aviso de fuga cada 10 minutos mientras el agua siga detectada. Este comportamiento no sustituye a la automatización de persistencia de Home Assistant.

## Automatizaciones en Home Assistant

Se podrán crear avisos por:

- Cambio de `water_leak` a activo
- Persistencia de una fuga durante el tiempo definido
- `battery_low` activo
- Batería por debajo del umbral operativo
- Pérdida de disponibilidad del dispositivo
- Recuperación del sensor tras una alerta

La automatización puede notificar, activar una sirena o apagar una carga eléctrica mediante una decisión separada. El sensor no debe apagar automáticamente equipos cuya interrupción pueda crear un riesgo mayor sin haber probado antes esa secuencia.

## Prueba de aceptación

- Emparejar el sensor y confirmar el descubrimiento de las tres entidades
- Mojar el sensor puntual y el cable por separado
- Confirmar el aviso en Home Assistant y la publicación MQTT
- Secar completamente el cable y comprobar el retorno al estado normal
- Simular batería baja o comprobar el aviso publicado por el dispositivo
- Verificar la recuperación tras reiniciar Zigbee2MQTT
- Probar la cobertura en la ubicación definitiva
- Confirmar que una humedad ambiental elevada no genera avisos persistentes sin agua

## Límites

- `water_leak` solo indica el estado detectado, no la cantidad ni el origen del agua
- La notificación depende de la alimentación del sensor, la red Zigbee, Zigbee2MQTT, Home Assistant y el canal de aviso
- La disponibilidad puede mantenerse durante un tiempo aunque se retire la pila, debido a la comunicación periódica del dispositivo
- OTA y entidades concretas dependen del firmware y de la versión de Zigbee2MQTT

## Fuentes

- [SONOFF SNZB-05P en Zigbee2MQTT](https://www.zigbee2mqtt.io/devices/SNZB-05P.html)
- [Guía de MQTT de Zigbee2MQTT](https://www.zigbee2mqtt.io/guide/usage/mqtt_topics_and_messages.html)
- [Ficha del SONOFF SNZB-05P](sonoff-snzb-05p.md)
