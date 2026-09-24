# 24 de septiembre de 2026: revisión y preparación del control térmico

## Motivo y alcance

Se inició la aplicación del plan de control térmico basado en evidencias. Antes
de cambiar configuración, el propietario confirmó que el aire acondicionado
Rowenta estaba físicamente apagado. La automatización térmica se mantuvo
deshabilitada durante la intervención. El objetivo de diseño es procurar
25–26 °C, con rango óptimo de 24,5–26,5 °C y aceptable de 24–27,5 °C; los
umbrales térmicos no se deben confundir con los estados del controlador.

Esta actuación instala telemetría de observación y actualiza la norma pública.
No implanta todavía el control predictivo: las decisiones sobre entradas,
salidas, pendientes, protección por fallos y consignas del Rowenta necesitan
datos nuevos de temperatura y una validación posterior.

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
antigüedad calculada en Home Assistant fue **6,1 min** a las 06:58 UTC. La
temperatura es telemetría del sensor sumergido, no una medida contrastada en
esta operación con un termómetro independiente.

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
las 07:24:42 UTC con 26,7 °C; esto confirma nueva telemetría, pero todavía no
caracteriza la cadencia sostenida ni el efecto sobre la autonomía. No se
interpretó el primer timeout como avería ni se cambió canal, red, firmware o
topología.

A las 07:34:45 UTC, Zigbee2MQTT recibió otro mensaje con temperatura todavía
en 26,7 °C, batería 100 % y `linkquality` 236. El mensaje anterior había sido
a las 07:24:42 UTC: intervalo observado de 10 min 03 s con temperatura sin
cambio. Es una primera observación compatible con el máximo configurado de
600 s, no una caracterización sostenida ni garantía de que el firmware respete
ese intervalo. En HA `sensor.veril_off_sns_05_last_seen` avanzó a las
07:34:45 UTC, mientras que la entidad de temperatura y las derivadas seguían
con su última actualización a las 07:24:42 UTC; distinguir frescura del
mensaje de frescura de una nueva muestra de temperatura es necesario.

## Cambios en Home Assistant

Antes de editar se creó una copia de seguridad de los ficheros YAML de HA. Se
añadieron, guardaron y validaron las siguientes entidades:

- `sensor.veril_off_sns_05_last_seen`: último mensaje recibido de
  `zigbee2mqtt/off-sns-05`, como fecha y hora.
- `sensor.veril_water_sensor_age`: antigüedad calculada del mensaje en minutos.
- Sensores descriptivos de temperatura mínima, mediana y máxima de
  `off-sns-01`, `off-sns-06` y `off-sns-08`. La mediana es solo un resumen; no se
  ha elegido aún una temperatura ambiente representativa para el control.
- Diferencia agua–ambiente independiente para cada una de esas tres ubicaciones.
- Derivadas de temperatura del agua en ventanas de 30 y 60 minutos, en °C/h.
  La configuración pasó la validación y las entidades se cargaron tras el
  reinicio de HA. Al inicio ambas mostraban 0,000 °C/h, sin demostrar
  estabilidad. Tras recibir la lectura de 26,7 °C a las 07:24:42 UTC, HA mostró
  0,200 °C/h (ventana de 30 min) y 0,100 °C/h (60 min). HA conservaba un
  estado de 26,6 °C desde las 06:56:13, pero Zigbee2MQTT atribuía su último
  mensaje entonces a las 06:51:54; por ello ese estado de HA no se considera
  una muestra nueva a las 06:56. La nueva lectura de 26,7 °C llegó a las
  07:24:42, unos 32 min 48 s después del mensaje Zigbee anterior. La secuencia
  aún es demasiado escasa para validar las ventanas o una tendencia de
  control; las derivadas se conservan solo como salidas observadas.

Se conservó la meteorología de `weather.forecast_home`; Home Assistant atribuye
esta entidad a met.no. La comparación temporal con la temperatura de la
habitación y el agua debe respetar las marcas de actualización de cada fuente.

El panel `acuario-veril`, vista «Control», incorpora el histórico de agua,
temperaturas del despacho y derivadas, además de humedad, meteorología,
antigüedad de telemetría y comparación de diferencias por ubicación. Se marcó
explícitamente como observación, no control.

La comprobación de configuración devolvió `valid: true`. Home Assistant se
reinició a petición expresa del propietario y volvió a responder. No se ejecutó
ninguna orden IR durante el reinicio.

## Estado del AC, automatización y shadows

La automatización `automation.veril_iniciar_refrigeracion_preventiva_del_despacho`
permanece **deshabilitada**. La regla antigua iniciaba refrigeración por una
lectura del agua superior a 26 °C sin requerir confirmación por tendencia ni
condición ambiental; reactivarla habría contradicho la decisión de no
refrigerar solo por encontrarse dentro del intervalo óptimo. No se ha sustituido
por umbrales predictivos aún no validados.

Después del reinicio, el helper `input_boolean.off_clm_01_power_shadow` apareció
en `on`, en contradicción con la confirmación física de apagado comunicada por
el propietario. Se corrigió el helper a `off` sin enviar una orden IR. Este
shadow es una representación lógica y no confirma por sí mismo el estado físico
del climatizador. No se volvió a comprobar físicamente tras el reinicio.

La lectura de agua **26,6 °C** cae en la banda cálida aceptable (26,5–27,0 °C),
no en alerta ni protección. Los estados ambientales mostrados al arrancar HA
fueron 27,9 °C (`off-sns-01`), 27,8 °C (`off-sns-06`) y 28,0 °C (`off-sns-08`);
se conservan como contexto mostrado por HA, sin inferir simultaneidad física ni
causalidad. `weather.forecast_home` mostró parcialmente nuboso y 24,9 °C, con
marca de actualización 06:55:33Z. HA atribuye esa entidad a met.no; no representa
la temperatura del agua ni una medición dentro del despacho.

## Pendientes antes de volver a automatizar

1. Continuar observando durante una o dos semanas la cadencia real de
   `off-sns-05` con el reporting 60/600/10 y vigilar la batería. Ya se observó
   un informe sin cambio de temperatura tras 10 min 03 s; es solo un intervalo,
   por lo que el comportamiento sostenido y su efecto en autonomía siguen sin
   caracterizarse.
2. Recoger informes suficientemente frecuentes y recientes para evaluar si las
   ventanas de 30 y 60 minutos producen pendientes interpretables. El informe
   sin cambio de las 07:34:45 actualizó `last_seen`, pero no la entidad de
   temperatura: las derivadas tampoco se actualizaron después de las 07:24:42.
   No usar una derivada inicial o un cero aislado como tendencia real.
3. Reconstruir y contrastar sesiones nuevas con los tres sensores ambientales,
   meteorología y las marcas/consignas del AC, manteniendo separados comandos,
   shadows y respuesta física.
4. Definir y validar condiciones de entrada/salida, antigüedad máxima,
   histéresis, estados degradados y alarmas. Hasta entonces la automatización
   queda deshabilitada.

## Trazabilidad

- Norma térmica vigente: [Régimen térmico adoptado](../../../02_configuracion/README.md#régimen-térmico-adoptado).
- Aplicación química: [Química de Veril](../../../02_configuracion/01_dimensiones/05_quimica.md).
- Análisis privado del plan y evidencias: permanece en `privado/`; no se replica
  ni publica aquí.
- Referencia Home Assistant sobre derivadas: [integración Derivative](https://www.home-assistant.io/integrations/derivative).
- Referencia Zigbee2MQTT sobre peticiones e informes MQTT:
  [MQTT topics and messages](https://www.zigbee2mqtt.io/guide/usage/mqtt_topics_and_messages.html).
