# SONOFF S60ZBTPF: Home Assistant y Zigbee2MQTT

## Integración

Cada enchufe S60ZBTPF se emparejará como dispositivo independiente en Zigbee2MQTT y se descubrirá en Home Assistant mediante MQTT Discovery. La ficha sirve para todas las unidades del mismo modelo; cada una tendrá un `friendly_name`, una carga y unos límites propios.

## Entidades y controles disponibles

| Entidad o función | Tipo | Uso |
| --- | --- | --- |
| `state` | Interruptor | Encender, apagar o alternar la salida |
| `energy` | Sensor | Energía acumulada en kWh |
| `energy_yesterday` | Sensor | Energía consumida ayer en kWh |
| `energy_today` | Sensor | Energía consumida hoy en kWh |
| `energy_month` | Sensor | Energía consumida durante el mes en kWh |
| `power` | Sensor | Potencia activa en W |
| `current` | Sensor | Corriente en A |
| `voltage` | Sensor | Tensión en V |
| `power_on_behavior` | Selector | Estado tras recuperar la alimentación: `off`, `on`, `toggle` o `previous` |
| `network_indicator` | Interruptor | Activar o desactivar el indicador azul de red |
| `inching_control_set` | Configuración | Habilitar el temporizador, fijar duración y elegir modo |
| `outlet_control_protect` | Interruptor | Activar la protección de la toma |
| `overload_protection` | Configuración | Límites de potencia, corriente y tensión |
| OTA | Actualización | Consultar y aplicar actualizaciones de firmware compatibles |

El apagado temporizado puede utilizar `on_time` y, cuando el firmware lo admita, `off_wait_time`. La compatibilidad concreta debe probarse en cada unidad.

## Calibración y precisión

Zigbee2MQTT permite configurar, según la entidad y la versión instalada:

- Corrección porcentual de energía
- Precisión de energía
- Corrección porcentual de corriente
- Precisión de corriente
- Corrección porcentual de tensión
- Precisión de tensión
- Corrección porcentual de potencia
- Precisión de potencia
- Publicación opcional de acciones del interruptor como `action`

Las calibraciones no se aplicarán sin comparar primero la lectura con un instrumento de referencia y conservar el valor original.

## Uso en Veril

Cada carga crítica tendrá un enchufe independiente. Home Assistant podrá registrar estado, disponibilidad y consumo, y generar avisos por:

- Pérdida de disponibilidad Zigbee
- Salida inesperadamente apagada o encendida
- Potencia nula o anómala durante el funcionamiento esperado
- Corriente o tensión fuera del comportamiento habitual
- Activación de la protección de sobrecarga
- Recuperación eléctrica con un estado no previsto

El consumo eléctrico no demuestra que una bomba mueva agua, que el skimmer produzca espuma ni que la luminaria esté emitiendo el espectro esperado.

## Prueba de aceptación

- Emparejar cada unidad con un nombre estable
- Confirmar el descubrimiento de todas las entidades esperadas
- Encender, apagar y alternar la salida
- Probar el comportamiento tras un corte eléctrico
- Comparar potencia, corriente y tensión con una carga conocida
- Comprobar energía diaria, mensual y acumulada
- Probar `inching` antes de usarlo con una carga crítica
- Activar y probar límites de protección sin superar condiciones seguras
- Confirmar que Home Assistant y Zigbee2MQTT siguen disponibles durante la recuperación eléctrica

## Límites

- Las entidades pueden variar con el firmware y la versión de Zigbee2MQTT
- Un valor de consumo no confirma el funcionamiento hidráulico o mecánico de la carga
- Las protecciones del enchufe no sustituyen el diferencial, la puesta a tierra ni la instalación eléctrica adecuada
- Home Assistant y Zigbee2MQTT no se alimentarán mediante estos mismos enchufes

## Fuentes

- [SONOFF S60ZBTPF en Zigbee2MQTT](https://www.zigbee2mqtt.io/devices/S60ZBTPF.html)
- [Guía de MQTT de Zigbee2MQTT](https://www.zigbee2mqtt.io/guide/usage/mqtt_topics_and_messages.html)
- [Ficha del SONOFF S60ZBTPF](sonoff-s60zbtpf.md)
