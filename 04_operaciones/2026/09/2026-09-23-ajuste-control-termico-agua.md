# 23 de septiembre de 2026 — Ajuste del control térmico del agua

## Objetivo comunicado

El propietario pidió inicialmente mantener el agua cerca de **25 °C**, con un
margen de **±1 °C**. La decisión posterior consta en la
[configuración de Veril](../../../02_configuracion/README.md#régimen-térmico-adoptado).

En esta fecha, `off-sns-05` tenía la sonda sumergida en la cámara Skimmer.
`off-sns-01`, `off-sns-06` y `off-sns-08` medían el ambiente del despacho.

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
las acciones.

## Actuación durante el ajuste

Antes de aplicar el criterio basado en el agua, una configuración intermedia
usó por error los sensores ambientales. La traza de Home Assistant muestra que
esa regla inició una sesión el **23 de septiembre a las 14:44:32 WEST** al
cambiar `sensor.0xa4c1386d58395a91_temperature` (`off-sns-06`). La automatización
envió el script de selección a 24 °C y después el de ventilador alto. El shadow
de alimentación pasó a encendido y el shadow de consigna quedó en 24 °C.

## Telemetría asociada de Home Assistant

| Variable | Entidad | Valor observado | Momento | Alcance |
| --- | --- | ---: | --- | --- |
| Temperatura del agua | `sensor.0xa4c13810b72fffff_temperature` (`off-sns-05`) | 26,4 °C | 2026-09-23 14:48:47 WEST | Sensor sumergido. |
| Shadow de alimentación del climatizador | `input_boolean.off_clm_01_power_shadow` | `on` | 2026-09-23 14:44:32 WEST | Shadow actualizado tras la orden. |
| Shadow de consigna | `input_number.off_clm_01_target_temperature_shadow` | 24,0 °C | 2026-09-23 14:44:42 WEST | Shadow de consigna tras ejecutar el script. |
| Automatización | `automation.veril_iniciar_refrigeracion_preventiva_del_despacho` | Habilitada | 2026-09-23 14:48:47 WEST | Configuración aceptada y cargada en Home Assistant. |

## Revisión posterior de trazas e histórico

Una consulta de solo lectura del **24 de septiembre** recuperó cinco ejecuciones
de `veril_gestion_termica_despacho` el día 23, entre las **18:49:37 y las
22:50:16 WEST**. Los cambios de temperatura del agua que las dispararon fueron:

- 26,3 → 26,1 °C.
- 26,1 → 26,0 °C.
- 26,0 → 25,9 °C.
- 25,9 → 25,7 °C.
- 25,7 → 25,6 °C.

En las cinco trazas, el shadow de alimentación ya estaba `on` y no se ejecutaron
las ramas de arranque o parada ni llamadas a los scripts IR.

Entre 26,1 °C a las 18:49:37 y 25,6 °C a las 22:50:16 transcurrieron
**4 h 00 min 39 s**. El cociente entre la variación y ese intervalo es
aproximadamente **−0,125 °C/h**.

## Referencias

- [Ajuste del 22 de septiembre](2026-09-22-ajuste-refrigeracion-preventiva-bajo-27.md).
- [Revisión del 24 de septiembre](2026-09-24-revision-observacion-control-termico.md).
