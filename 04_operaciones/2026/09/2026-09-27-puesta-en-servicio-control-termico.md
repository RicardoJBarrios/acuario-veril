# 27 de septiembre de 2026: puesta en servicio del control térmico inicial

## Motivo y alcance

Se instaló y habilitó en Home Assistant el piloto inicial previsto en el plan
de control térmico de Veril. Su finalidad es mantener margen antes de la banda
de protección y permitir que el agua regrese gradualmente hacia 25–26 °C. La
envolvente térmica biológica no cambia: estos umbrales son decisiones de
control y no nuevos límites de tolerancia.

## Sincronización y comprobación física

Antes de la puesta en servicio, el propietario confirmó que el Rowenta estaba
apagado. Home Assistant ejecutó el script discreto `power_on` a las
15:55:55 UTC (16:55:55 WEST). El propietario confirmó después que el equipo
encendió y que estaba en frío, a **24 °C**, con el ventilador en **alto**.
Esta confirmación física permitió alinear los *shadows* y transferir al
controlador la sesión iniciada para la prueba. La integración infrarroja es
unidireccional: sus helpers representan órdenes y valores estimados, no
telemetría de retorno.

## Lógica instalada en Home Assistant

La automatización anterior, que arrancaba a 26 °C, fue sustituida por un
evaluador central con modo `single`. No se corta la alimentación eléctrica del
Rowenta. La lógica vigente es:

| Estado o condición | Acción configurada |
| --- | --- |
| Agua ≥27,0 °C durante 10 min y 2 de 3 sensores ambientales frescos ≥29 °C, o previsión horaria ≥30 °C en las próximas 6 h | Refrigeración preventiva: frío, 25 °C y ventilador alto |
| Agua ≥27,5 °C durante 5 min | Refrigeración: frío, 25 °C y ventilador alto |
| Agua ≥28,0 °C | Protección: frío, 24 °C y ventilador alto |
| Agua <27,5 °C durante 15 min desde protección | Retorno a refrigeración con consigna de 25 °C |
| Agua ≤26,5 °C durante 15 min en una sesión propiedad del controlador | Enviar apagado y devolver el estado a normal |

Las lecturas de agua se consideran utilizables mientras `off-sns-05` comunique
en los últimos 20 min. Si falta esa comunicación o se pierde la sincronización
IR, el control bloquea nuevas órdenes y notifica la incidencia; no deduce la
temperatura ausente ni apaga a ciegas una sesión activa. Las derivadas de 30 y
60 min permanecen fuera de los disparadores. Las alarmas son 28,5 °C (`warning`),
29 °C (`critical`) y 30 °C (`emergency`).

Se añadió `input_datetime.veril_thermal_last_ac_power_off` para guardar la
hora del último comando de apagado. La lógica impone un mínimo de 3 min antes
de permitir un nuevo encendido. La persistencia de esta marca todavía no se ha
comprobado mediante un reinicio de HA. La automatización queda configurada
para iniciar habilitada tras reiniciar HA; su rama de inicio restablece el
periodo de persistencia sin emitir IR.

## Estado observado y límites de la evidencia

En Home Assistant, el estado de agua pasó de **28,9 °C** (último cambio
numérico guardado a las 16:23:17 WEST) a **28,8 °C** a las 17:11:17 WEST. En
esta última traza, la comunicación de `off-sns-05` tenía una antigüedad
calculada de **0 min**. El controlador figuraba en `protection`, el *shadow* de
alimentación en `on`, la sincronización en `on` y la alarma en `warning`. La
traza no contenía llamadas a scripts IR: el equipo ya estaba físicamente en
la configuración requerida, así que no se envió una orden redundante.

La diferencia de 0,1 °C entre estados guardados no demuestra que el Rowenta la
haya causado. El intervalo es corto, los sensores no tienen actualizaciones
perfectamente simultáneas y no hay una serie suficiente para medir retardo o
eficacia. El inicio físico del Rowenta se confirmó directamente por el
propietario; el apagado automático y la respuesta térmica prolongada siguen
pendientes de observación.

En la consulta de las 17:28 WEST, HA conservaba 28,8 °C como último estado
numérico de agua, actualizado a las 17:11 WEST; la edad del último mensaje
Zigbee era 6,7 min. La traza de las 17:28 evaluó la telemetría como válida,
mantuvo `protection` y `warning`, y no recorrió acciones IR. En esa ejecución,
una de tres temperaturas ambientales frescas alcanzaba 29 °C y la previsión
horaria no superaba 30 °C; esos datos no alteraban la protección ya activa.

## Mediciones históricas disponibles

Las cifras siguientes proceden de las series de Home Assistant recopiladas
antes de la instalación del nuevo piloto. Los estados ON/OFF son *shadows* de
una integración IR unidireccional, salvo donde se indica confirmación física.
Las lecturas de agua y ambiente no siempre son simultáneas. Los cambios medios
son cocientes entre muestras seleccionadas y no derivadas continuas.

### Ventanas anteriores con *shadow* ON

En las cinco ventanas documentadas, la consigna registrada fue 24 °C. No se
conserva confirmación física del Rowenta para estas sesiones, por lo que los
descensos coincidentes no prueban que el equipo estuviera funcionando ni que
causara la variación.

| Ventana de *shadow* ON (WEST) | Agua: muestra inicial → final seleccionada | Cambio medio aproximado | Ambiente del despacho observado durante la ventana |
| --- | --- | ---: | --- |
| 17 sep 20:48–18 sep 03:06 | 28,9 °C a las 21:20 → 27,1 °C a las 02:21 | −0,36 °C/h en unas 5 h | `off-sns-01`: aprox. 29,7 → 26,7 °C; `off-sns-06`: 29,5 °C al inicio, mínimo 25,5 °C; `off-sns-08`: 29,6 °C al inicio, mínimo 27,1 °C |
| 20 sep 16:34–21 sep 01:21 | 28,1 °C al inicio → 27,0 °C a las 00:36 | −0,13 °C/h en unas 7 h | Mínimos registrados: `off-sns-01` 26,9 °C; `off-sns-06` 25,7 °C; `off-sns-08` 27,1 °C |
| 22 sep 08:43–15:29 | No se recuperó pareja de muestras comparable en el resumen de la ventana; mínimo semanal 25,6 °C a las 15:44, posterior al *shadow* OFF | No calculable con seguridad | Hay lecturas de los tres sensores en el histórico semanal, pero no se conservó un rango completo emparejado para esta ventana |
| 22 sep 21:45–23 sep 06:32 | 26,6 °C a las 21:45 → 25,8 °C a las 06:47, después del *shadow* OFF | −0,10 °C/h en unas 6 h | `off-sns-01`: 28,7 °C antes, 27,7 °C a las 23:27; `off-sns-06`: 29,2 °C antes, cerca de 25,2 °C al final; `off-sns-08`: 28,9–29,1 °C al inicio, cerca de 26,3 °C al final |
| 23 sep 14:44–24 sep 00:06 | 26,3 °C antes del ON, 26,4 °C a las 14:48 → 25,6 °C a las 22:50 | −0,10 °C/h en unas 8 h | Mínimos: `off-sns-01` 26,1 °C; `off-sns-06` 25,4 °C; `off-sns-08` 26,0 °C |

En las ventanas con datos recuperados bajaron las lecturas de agua y de los
sensores ambientales. La asociación temporal justifica continuar observando,
pero no separa el efecto del Rowenta de la temperatura exterior, el ciclo
diario, las fuentes internas u otros cambios. En la ventana 23–24 de septiembre
se recuperaron además cinco trazas de automatización: ante cambios de agua de
26,3 a 25,6 °C, el *shadow* ya figuraba `on` y no se ejecutaron scripts IR.
Por tanto, esas trazas tampoco acreditan encendido físico.

### Tramo con AC físicamente apagado y ambiente exterior

El propietario confirmó que el aire acondicionado permaneció físicamente
apagado del 24 al 26 de septiembre. En Home Assistant, `off-sns-05` pasó de
26,6 a 28,4 °C entre los extremos de la ventana, un aumento de 1,8 °C en unas
63 h 47 min (cociente entre extremos: aprox. +0,028 °C/h; no es una tasa
continua). Los rangos diarios fueron:

| Día local | Estados numéricos de agua guardados | Rango de agua | Extremos diarios de la estación Santa Cruz C449C |
| --- | ---: | ---: | ---: |
| 24 sep desde 07:55 | 154 | 26,6–27,4 °C | 26,2–33,3 °C |
| 25 sep | 186 | 27,4–28,3 °C | 26,7–31,9 °C |
| 26 sep | 324 | 27,5–28,4 °C | 26,3–30,6 °C |

Los conteos corresponden a estados numéricos guardados, no a una frecuencia de
muestreo uniforme. En el mismo tramo, los rangos de temperatura ambiental
registrados fueron 27,6–30,5 °C (`off-sns-01`), 27,6–31,8 °C (`off-sns-06`) y
27,8–30,9 °C (`off-sns-08`). La HR combinada observada fue 32–63 %. Los extremos
exteriores proceden de la estación C449C y no son medidas dentro del despacho.
Las tablas horarias consultadas corresponden al [24 de septiembre](https://www.tutiempo.net/estaciones/stacruz-de-tenerife/24-septiembre-2026/),
[25 de septiembre](https://www.tutiempo.net/estaciones/stacruz-de-tenerife/25-septiembre-2026/)
y [26 de septiembre](https://www.tutiempo.net/estaciones/stacruz-de-tenerife/26-septiembre-2026/);
la [identificación de C449C en AEMET](https://www.aemet.es/es/eltiempo/observacion/ultimosdatos_espana_resumen-viernes-04.xls?l=C449C&w=1)
se conserva como referencia de estación. La previsión `weather.forecast_home`
era de met.no, distinta de la observación exterior; los estados recuperados
abarcaron 24,8–31,3 °C, pero no cubrieron de forma completa el final de la
ventana.

En esos tres días, el agua aumentó mientras el equipo estuvo apagado y hubo
temperaturas elevadas tanto en el despacho como en Santa Cruz. Esto confirma
la exposición a un entorno cálido y la acumulación de calor durante ese tramo;
no cuantifica qué fracción corresponde al exterior, a fuentes internas o al
retardo térmico.

### Estado después de la sincronización del piloto

En la consulta de Home Assistant de las 17:28 WEST del 27 de septiembre, el
último valor numérico del agua era 28,8 °C (actualizado a las 17:11 WEST), con
último mensaje Zigbee 6,7 min antes de la consulta. La traza mantenía
`protection` y `warning`; no emitió una orden redundante porque el Rowenta ya
estaba en la configuración requerida. En un mensaje posterior, el propietario
volvió a confirmar directamente que el equipo estaba en frío, a 24 °C y con
ventilador alto. No se proporcionó hora exacta para esta última observación y
el Rowenta no devuelve telemetría física a Home Assistant.

No hay una muestra numérica del agua posterior a la lectura de 28,8 °C en los
datos consultados para este registro. La diferencia anterior de 28,9 a 28,8 °C
no demuestra efecto del aire acondicionado; tampoco se ha observado todavía la
transición automática de protección a 25 °C ni el apagado automático a
≤26,5 °C durante 15 min.

## Fuente y seguimiento

La envolvente biológica adoptada permanece en
[Configuración integrada, régimen térmico](../../../02_configuracion/README.md#régimen-térmico-adoptado).
La lógica actualmente instalada está resumida en [Control térmico de Veril](../../../02_configuracion/control-termico.md).
El estado operativo no sustituye la revisión posterior del piloto con las
series de agua, sensores del despacho y meteorología.
