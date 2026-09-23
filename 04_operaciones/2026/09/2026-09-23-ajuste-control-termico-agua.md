# 23 de septiembre de 2026: ajuste del control térmico del agua

## Objetivo y contexto

El propietario pidió mantener el agua de Veril cerca de **25 °C**, con un margen
de **±1 °C**. La automatización del aire acondicionado debe seguir la lectura
del termómetro `off-sns-05`, cuya sonda está sumergida en el agua de la cámara
Skimmer. Los sensores `off-sns-01`, `off-sns-06` y `off-sns-08` miden el
ambiente del despacho y no determinan este objetivo térmico.

## Cambio aplicado en Home Assistant

El 23 de septiembre se actualizó y validó la automatización
`automation.veril_iniciar_refrigeracion_preventiva_del_despacho` con estos
criterios:

- Iniciar la refrigeración si `off-sns-05` supera **26 °C**, la lectura tiene
  menos de 90 minutos, el *shadow* de sincronización está activado y el
  *shadow* de alimentación indica apagado.
- Fijar el climatizador en modo frío a **24 °C** y ventilador alto.
- Apagarlo cuando `off-sns-05` indique **25 °C o menos durante 15 minutos**,
  con lectura reciente, sincronización activa y el *shadow* de alimentación
  encendido.

Home Assistant aceptó la configuración y su validador confirmó los triggers y
las acciones. No se forzó una ejecución para probarla.

## Actuación durante el ajuste

Antes de aplicar el criterio basado en el agua, una configuración intermedia
usó por error los sensores ambientales. La traza de Home Assistant muestra que
esa regla inició una sesión el **23 de septiembre a las 14:44:32 WEST** al
cambiar `sensor.0xa4c1386d58395a91_temperature` (`off-sns-06`). La automatización
envió el script de selección a 24 °C y después el de ventilador alto. El shadow
de alimentación pasó a encendido y el shadow de consigna quedó en 24 °C. Como
el control infrarrojo es unidireccional, estos estados y la traza confirman las
órdenes de Home Assistant, no el estado físico del climatizador.

## Telemetría asociada de Home Assistant

| Variable | Entidad | Valor observado | Momento | Alcance |
| --- | --- | ---: | --- | --- |
| Temperatura del agua | `sensor.0xa4c13810b72fffff_temperature` (`off-sns-05`) | 26,4 °C | 2026-09-23 14:48:47 WEST | Lectura del sensor sumergido; sin contraste simultáneo con un termómetro independiente en esta operación. |
| Shadow de alimentación del climatizador | `input_boolean.off_clm_01_power_shadow` | `on` | 2026-09-23 14:44:32 WEST | Estado estimado actualizado tras la orden; no es realimentación del aparato. |
| Shadow de consigna | `input_number.off_clm_01_target_temperature_shadow` | 24,0 °C | 2026-09-23 14:44:42 WEST | Consigna estimada tras ejecutar el script; no confirma el valor mostrado en el panel. |
| Automatización | `automation.veril_iniciar_refrigeracion_preventiva_del_despacho` | Habilitada | 2026-09-23 14:48:47 WEST | Home Assistant aceptó y cargó la configuración; esto no demuestra el efecto térmico. |

## Resultado y seguimiento

La regla vigente actúa sobre el agua medida por `off-sns-05`, no sobre la
temperatura ambiental del despacho. En la última lectura consultada, el agua
estaba a 26,4 °C y el shadow indicaba el climatizador encendido. La temperatura
del agua sigue por encima del límite superior de 26 °C; todavía no hay una
sesión posterior suficiente para evaluar la respuesta térmica ni confirmar el
efecto físico del aire acondicionado. El Rowenta solo refrigera: no puede
recuperar la temperatura si el agua desciende por debajo de 24 °C, de modo que
el margen inferior requiere seguimiento y no queda garantizado por esta regla.

Contrastar el histórico de `off-sns-05` con las marcas de encendido y apagado y
observar el panel del climatizador. La política de **24–26 °C** solicitada como
objetivo de control es más estrecha que el rango habitual de diseño de Veril,
**25,0–27,5 °C**, que permanece documentado en la configuración integrada.

La definición operativa previa está en el [ajuste del 22 de septiembre](2026-09-22-ajuste-refrigeracion-preventiva-bajo-27.md)
y la identidad y limitaciones del sensor, en la [ficha de integración del
climatizador](../../../../../sistemas/homelab/domotica/home-assistant/documentacion/integraciones/off-clm-01-rowenta.md#automatización-térmica-de-veril).
