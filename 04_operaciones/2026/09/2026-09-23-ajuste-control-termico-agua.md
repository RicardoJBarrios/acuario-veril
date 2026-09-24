# 23 de septiembre de 2026: ajuste del control térmico del agua

## Objetivo y contexto

En esta actuación se trabajó sobre la petición inicial del propietario de
mantener el agua cerca de **25 °C**, con un margen de **±1 °C**. Esa petición
quedó posteriormente sustituida por la envolvente térmica final adoptada para
Veril: zona preferida **25–26 °C**, óptima **24,5–26,5 °C** y aceptable
**24–27,5 °C**. La configuración vigente y el registro del 24 de septiembre
recogen la decisión final y el estado actual de revisión del control.

En la fecha de esta actuación, `off-sns-05` tenía la sonda sumergida en el agua
de la cámara Skimmer. Los sensores `off-sns-01`, `off-sns-06` y `off-sns-08`
miden el ambiente del despacho y no la temperatura del agua.

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

La regla configurada en esta actuación usaba la lectura del agua de
`off-sns-05`, no la temperatura ambiental del despacho. En la última lectura
consultada, el agua estaba a 26,4 °C y el shadow indicaba el climatizador
encendido. No había una sesión posterior suficiente para evaluar la respuesta
térmica ni confirmar el efecto físico del aire acondicionado. El Rowenta solo
refrigera y no controla el límite inferior. Esta configuración es un antecedente
histórico: la automatización se deshabilitó durante la actuación del 24 de
septiembre y sigue en revisión, según el [registro posterior](2026-09-24-revision-observacion-control-termico.md).

La configuración de esta fecha no define la política térmica actual. La
envolvente final de Veril distingue la temperatura de su duración y tendencia;
no implica que Home Assistant deba perseguir un valor puntual ni establece por
sí sola los umbrales o acciones del control. La comparación de las órdenes con
la respuesta del agua queda sujeta a la revisión y validación descritas en el
registro del 24 de septiembre.

### Revisión posterior de trazas e histórico (consulta del 24 de septiembre)

La consulta de solo lectura a las trazas conservadas por Home Assistant
recuperó cinco ejecuciones de `veril_gestion_termica_despacho` el 23 de
septiembre, entre las 18:49:37 y las 22:50:16 WEST. Todas se dispararon por
cambios de `sensor.0xa4c13810b72fffff_temperature` (agua): 26,3→26,1 °C;
26,1→26,0 °C; 26,0→25,9 °C; 25,9→25,7 °C; y 25,7→25,6 °C. En cada traza, la
rama de arranque no pasó su condición porque
`input_boolean.off_clm_01_power_shadow` ya estaba `on`; la rama de parada
tampoco se ejecutó. No aparecen llamadas a los scripts IR en esas cinco
ejecuciones. Esto confirma qué ramas evaluó HA y por qué no emitió nuevas
órdenes en esos eventos; no confirma que el Rowenta siguiera funcionando
físicamente.

Entre el estado de agua de 26,1 °C a las 18:49:37 y el de 25,6 °C a las
22:50:16 WEST transcurrieron 4 h 00 min 39 s; la variación media entre esos
extremos es aproximadamente −0,125 °C/h. Es un cálculo de extremos a partir
de estados registrados, no una derivada continua ni una medición de la tasa
instantánea; no demuestra que el AC causara el descenso.

El último cambio de agua de la secuencia fue 25,6 °C a las 22:50:16 WEST, en
concordancia temporal con el mínimo del histórico de temperatura descrito en
la tabla de datos; los sensores ambientales también registraron descensos en
la ventana. La coincidencia temporal no permite atribuir causalidad al AC,
porque el estado `on` es un *shadow* y no existe confirmación física
independiente del equipo. La telemetría y las trazas se conservan como
observaciones de Home Assistant.

La definición operativa previa está en el [ajuste del 22 de septiembre](2026-09-22-ajuste-refrigeracion-preventiva-bajo-27.md). La identidad y las limitaciones del sensor constan en la [ficha de integración del SONOFF SNZB-02LD](../../../01_verilpedia/04_hardware/sonoff-snzb-02ld/home-assistant-zigbee2mqtt.md). La configuración técnica del Rowenta permanece en la documentación local de Home Assistant y no se enlaza aquí porque no forma parte del repositorio público.
