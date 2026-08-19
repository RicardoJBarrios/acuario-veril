# SONOFF S60ZBTPF

## Identificación

- **Fabricante:** SONOFF
- **Modelo:** S60ZBTPF
- **Tipo:** enchufe inteligente Zigbee con medición eléctrica
- **Protocolo:** Zigbee 3.0
- **Formato:** enchufe europeo tipo F
- **Canales de salida:** 1

## Ficha normalizada

| Campo | Valor |
| --- | --- |
| `hardware_id` | `SONOFF_S60ZBTPF` |
| `category` | `aquarium_hardware_control` |
| `vendor` | `SONOFF` |
| `model` | `S60ZBTPF` |
| `hardware_kind` | `physical` |
| `physical_type` | `zigbee_smart_plug` |
| `protocol` | Zigbee 3.0 |
| `channels` | 1 |
| `energy_monitoring` | Sí |
| `overload_protection` | Sí |
| `router` | Sí, según la documentación del fabricante |

## Especificaciones

| Parámetro | Valor declarado |
| --- | --- |
| Entrada | 250 V CA, 50/60 Hz |
| Corriente máxima | 16 A |
| Carga máxima | 4000 W |
| Consumo en espera | Menos de 1 W |
| Dimensiones | 50 × 50 × 61,5 mm |
| Material de la carcasa | PC V0 |
| Temperatura de funcionamiento | −10–40 °C |
| Humedad de funcionamiento | 5–95 %, sin condensación |
| Protección declarada | Sobrecarga |

Los límites de 16 A y 4000 W describen la capacidad eléctrica máxima del enchufe. No son una recomendación para conectar cualquier carga en un entorno húmedo ni sustituyen el diferencial, la puesta a tierra, la protección contra salpicaduras o una instalación eléctrica adecuada.

## Datos disponibles en Zigbee2MQTT

Zigbee2MQTT expone, según la versión de firmware y la integración:

- Estado de la salida: `ON`, `OFF` o `TOGGLE`
- Energía acumulada en kWh
- Potencia activa en W
- Corriente en A
- Tensión en V
- Energía de ayer, del día y del mes
- Comportamiento tras recuperar la alimentación: `off`, `on`, `toggle` o `previous`
- Indicador de red Zigbee
- Control temporizado `inching`, con habilitación, tiempo y modo
- Protección de la toma
- Protección contra sobrecarga, con límites de potencia, corriente y tensión
- Actualizaciones OTA

Zigbee2MQTT también permite configurar la precisión y la calibración porcentual de energía, corriente, tensión y potencia, además de publicar opcionalmente las acciones del estado como `action`.

La disponibilidad concreta de cada entidad debe comprobarse en el dispositivo emparejado. La medición eléctrica indica que existe consumo, pero no demuestra que el equipo conectado esté funcionando correctamente.

La integración completa con Home Assistant está en [Home Assistant y Zigbee2MQTT](home-assistant-zigbee2mqtt.md).

## Distribución eléctrica en Veril

Cada elemento electrónico se conectará a una unidad independiente del S60ZBTPF. Cada unidad tendrá un nombre, una automatización, unos límites y un registro propios. No se conectarán varias cargas críticas al mismo enchufe, porque la medición combinada impediría interpretar el consumo de cada equipo.

La distribución prevista es:

| Equipo electrónico | Carga conectada al S60ZBTPF | Identificador sugerido |
| --- | --- | --- |
| D-D H2Ocean Compact ATO | Adaptador del controlador ATO | `switch.veril_ato_alimentacion` |
| Sicce Shark SKIMMER 300 | Alimentación del skimmer | `switch.veril_skimmer_alimentacion` |
| Mantis Tourbon 60 | Adaptador del controlador de la bomba | `switch.veril_mantis_tourbon_60_alimentacion` |
| Sicce Micra Plus 600 | Alimentación de la bomba de retorno | `switch.veril_micra_plus_600_alimentacion` |
| AI Prime 16HD Reef | Adaptador de la luminaria | `switch.veril_ai_prime_16hd_reef_alimentacion` |

Home Assistant y la infraestructura de Zigbee2MQTT no se alimentarán a través de estos enchufes, porque deben permanecer disponibles para supervisarlos y controlarlos.

## Instalación segura

- Mantener el enchufe alejado de salpicaduras y condensación
- Evitar que los cables conduzcan agua hacia el enchufe
- Dejar accesible el botón y el indicador
- No colocarlo debajo de conexiones que puedan gotear
- Proteger el circuito con diferencial y protección eléctrica adecuados
- No superar los límites declarados
- Comprobar que la carga conectada tolera la interrupción y el rearranque
- Configurar y probar el comportamiento tras un corte eléctrico

El S60ZBTPF no es un dispositivo estanco ni un sensor de inundación. Su instalación debe quedar fuera de la zona húmeda y protegida frente a agua salada.

## Estado tras un corte eléctrico

El comportamiento de la salida se configurará mediante `power_on_behavior` y se comprobará después de un corte real o de una prueba controlada. Para cargas que no deban arrancar sin supervisión, se utilizará el estado apagado si el dispositivo y la instalación lo permiten.

La recuperación de Zigbee2MQTT y Home Assistant puede producirse después de la recuperación eléctrica. Por eso no se considerará suficiente confiar en una automatización que todavía no haya sido probada durante ese intervalo.

## Limitaciones

- No mide temperatura, nivel, caudal, aire ni estado mecánico del equipo conectado
- No detecta por sí solo una fuga o un desbordamiento
- No confirma que una bomba esté moviendo agua
- No sustituye las protecciones propias del ATO, del skimmer o de cualquier otra carga
- La automatización depende de la disponibilidad del coordinador Zigbee, Zigbee2MQTT y Home Assistant, salvo las funciones locales que el propio enchufe conserve

## Fuentes

- [Manual local del SONOFF S60ZBTPF, versión 1.1 en inglés](sonoff-s60zbtpf-manual-en-v1-1.pdf)
- [Fuente del PDF descargado, manual S60ZBTPF V1.1](https://homebrainz.s30.cdn-upgates.com/4/468b304349e4b5-user-manual-s60zbtpf-en-v1-1.pdf)
- [Centro de soporte oficial del S60ZBTPF](https://support.sonoff.tech/s60zbtpf-usermanual/)
- [Página oficial de la serie SONOFF S60](https://sonoff.tech/en-us/products/sonoff-iplug-zigbee-smart-plug-s60-series)
- [SONOFF S60ZBTPF/S60ZBTPG](https://sonoff.tech/products/sonoff-iplug-zigbee-smart-plug-s60-series)
- [SONOFF S60ZBTPF en Zigbee2MQTT](https://www.zigbee2mqtt.io/devices/S60ZBTPF.html)
