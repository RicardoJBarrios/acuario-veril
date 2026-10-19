# 22 de septiembre de 2026 — Ajuste de la refrigeración preventiva para mantener el agua bajo 27 °C

## Cambio aplicado

Se modificó en Home Assistant la automatización
`automation.veril_iniciar_refrigeracion_preventiva_del_despacho` para anticipar
la refrigeración ambiental. Home Assistant aceptó y devolvió la configuración
actualizada. Se mantuvo la consigna de **24 °C** y ventilador alto.

## Configuración aplicada

La rama de encendido automático requiere simultáneamente:

- Agua de `off-sns-05` de al menos **26,5 °C**, actualizada en los últimos 90 minutos
- Al menos dos de los tres sensores ambientales del despacho (`off-sns-01`, `off-sns-06` y `off-sns-08`) a **27,0 °C** o más, también actualizados en los últimos 90 minutos
- *Shadow* del climatizador sincronizado manualmente y *shadow* de alimentación apagado

La rama de apagado continúa requiriendo que al menos dos sensores ambientales estén a 27,0 °C o menos. Su criterio de agua queda adelantado: el agua debe permanecer por debajo de **26,0 °C durante 45 minutos** antes de enviar el apagado.

Se conservan las protecciones anteriores frente a entidades `unknown` o `unavailable`, lecturas antiguas y posibles reinicios durante el temporizador de apagado.

## Telemetría asociada de Home Assistant

| Variable | Entidad | Valor observado al comprobar el cambio | Alcance |
| --- | --- | --- | --- |
| Automatización | `automation.veril_iniciar_refrigeracion_preventiva_del_despacho` | Habilitada | Home Assistant aceptó la nueva configuración. |
| Temperatura del agua | `sensor.0xa4c13810b72fffff_temperature` | 27,8 °C, última actualización a las 05:42 WEST | La muestra superaba el umbral nuevo, pero tenía más de 90 minutos y la automatización no podía usarla para arrancar. |
| Sincronización declarada | `input_boolean.off_clm_01_shadow_synchronized` | Activada | Confirmación manual previa. |
| Alimentación declarada | `input_boolean.off_clm_01_power_shadow` | Apagada | Shadow de alimentación. |

## Resultado

La configuración quedó guardada. No se envió una orden de encendido como
consecuencia de la modificación: el dato de agua disponible tenía más de
90 minutos, límite configurado para su uso.

## Referencia

- [Automatización preventiva del 17 de septiembre](2026-09-17.md#automatización-de-la-refrigeración-preventiva-del-despacho).
