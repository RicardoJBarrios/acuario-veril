# 24 de septiembre de 2026 — Revisión y preparación del control térmico

## Actuación

El propietario confirmó que el aire acondicionado Rowenta estaba físicamente
apagado. La automatización térmica permaneció deshabilitada durante la
intervención. Se añadió telemetría de observación y se actualizó la norma
pública de Veril.

## Evidencia y cambios en Zigbee2MQTT

La inspección identificó `off-sns-05` como el SONOFF SNZB-02LD de IEEE
`0xa4c13810b72fffff`, dispositivo final a batería. Zigbee2MQTT informó versión
2.13.0, entrevista correcta, batería al 100 %, `linkquality` 236 en la última
lectura y OTA instalada al día. El informe de `bridge/health` no mostró salidas
de la red ni cambios de dirección para este dispositivo; MQTT estaba conectado.

Se activó `advanced.last_seen: ISO_8601` en Zigbee2MQTT, sin reinicio requerido,
para registrar la hora del último mensaje en los informes MQTT. Tras el
reinicio de Home Assistant, el dato `last_seen` observado fue
`2026-09-24T06:51:54Z`; el valor de temperatura asociado fue **26,6 °C**. La
antigüedad calculada en Home Assistant fue **6,1 min** a las 06:58 UTC.

Se solicitó configurar el reporte Zigbee de temperatura con mínimo 60 s,
máximo 600 s y cambio reportable 10 (equivalente, en general, a 0,1 °C). El
primer intento agotó el tiempo de espera y no modificó la configuración. Tras
el propietario pulsar el botón del dispositivo, Zigbee2MQTT recibió un mensaje
a las 07:22:03 UTC (26,6 °C; batería 100 %; `linkquality` 255). Un segundo
intento, realizado inmediatamente después de una nueva comunicación del
sensor, sí quedó aplicado: la lectura de `bridge/devices` mostró para
`msTemperatureMeasurement/measuredValue` mínimo 60 s, máximo 600 s y cambio
reportable 10. La configuración de batería permaneció sin cambios (mínimo
3600 s, máximo 65000 s, cambio 10). Zigbee2MQTT volvió a recibir el sensor a
las 07:24:42 UTC con 26,7 °C.

A las 07:34:45 UTC, Zigbee2MQTT recibió otro mensaje con temperatura todavía
en 26,7 °C, batería 100 % y `linkquality` 236. El mensaje anterior había sido
a las 07:24:42 UTC: intervalo observado de 10 min 03 s con temperatura sin
cambio. En HA `sensor.veril_off_sns_05_last_seen` avanzó a las
07:34:45 UTC, mientras que la entidad de temperatura y las derivadas seguían
con su última actualización a las 07:24:42 UTC.

## Cambios en Home Assistant

Antes de editar se creó una copia de seguridad de los ficheros YAML de HA. Se
añadieron, guardaron y validaron las siguientes entidades:

- `sensor.veril_off_sns_05_last_seen`: último mensaje recibido de
  `zigbee2mqtt/off-sns-05`, como fecha y hora.
- `sensor.veril_water_sensor_age`: antigüedad calculada del mensaje en minutos.
- Sensores descriptivos de temperatura mínima, mediana y máxima de
  `off-sns-01`, `off-sns-06` y `off-sns-08`.
- Diferencia agua–ambiente independiente para cada una de esas tres ubicaciones.
- Derivadas de temperatura del agua en ventanas de 30 y 60 minutos, en °C/h.
  La configuración pasó la validación y las entidades se cargaron tras el
  reinicio de HA. Al inicio ambas mostraban 0,000 °C/h, como valores iniciales. Tras recibir la lectura de 26,7 °C a las 07:24:42 UTC, HA mostró
  0,200 °C/h (ventana de 30 min) y 0,100 °C/h (60 min). HA conservaba un
  estado de 26,6 °C desde las 06:56:13, pero Zigbee2MQTT atribuía su último
  mensaje entonces a las 06:51:54; el valor de las 06:56 corresponde al estado de HA. La nueva lectura de 26,7 °C llegó a las
  07:24:42, unos 32 min 48 s después del mensaje Zigbee anterior.

Se conservó la meteorología de `weather.forecast_home`; Home Assistant atribuye
esta entidad a met.no.

El panel `acuario-veril`, vista «Control», incorpora el histórico de agua,
temperaturas del despacho y derivadas, además de humedad, meteorología,
antigüedad de telemetría y comparación de diferencias por ubicación. Se marcó
explícitamente como observación, no control.

La comprobación de configuración devolvió `valid: true`. Home Assistant se
reinició a petición expresa del propietario y volvió a responder. No se ejecutó
ninguna orden IR durante el reinicio.

## Estado del AC, automatización y shadows

La automatización `automation.veril_iniciar_refrigeracion_preventiva_del_despacho`
permaneció **deshabilitada**.

Después del reinicio, `input_boolean.off_clm_01_power_shadow` apareció en `on`.
Se corrigió a `off` conforme al apagado físico comunicado por el propietario,
sin enviar una orden IR.

Home Assistant mostró **26,6 °C** en el agua y estos estados ambientales:
**27,9 °C** (`off-sns-01`), **27,8 °C** (`off-sns-06`) y **28,0 °C**
(`off-sns-08`). `weather.forecast_home`, atribuida a met.no, mostró parcialmente
nuboso y **24,9 °C**, con actualización a las **06:55:33Z**.

## Trazabilidad

- [Régimen térmico adoptado](../../../02_configuracion/README.md#régimen-térmico-adoptado).
- [Química de Veril](../../../02_configuracion/01_dimensiones/05_quimica.md).
