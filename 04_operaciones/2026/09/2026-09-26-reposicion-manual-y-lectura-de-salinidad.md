# 2026-09-26 — Reposición manual y lectura de salinidad

## Estado

Operación documentada con evidencia física comunicada por el propietario y
telemetría contextual de Home Assistant.

## Ejecución comunicada

Como quedaba poca agua en la cámara C3, se añadió agua al sistema desde el
barril. El barril contenía agua salada. Su volumen se estimó en **unos 3,6 L**
antes de la operación y **unos 1,75 L** después.

El volumen añadido comunicado por el propietario es de aproximadamente
**1,85 L**, calculado restando el volumen final al inicial del barril:
3,6 L − 1,75 L. La cifra es aproximada porque ambos volúmenes de partida se
estimaron.

El propietario precisó que hizo la reposición y la lectura del refractómetro
unos minutos antes de comunicarlo. No se conoce el minuto exacto.

## Resultado observado

Después de la reposición, el refractómetro seguía indicando una lectura fuera
de escala, aproximadamente **1,032** según la notación comunicada. La lectura
se conserva como observación del instrumento, no como una medida validada de
salinidad: no se aportaron la escala concreta, la temperatura de la muestra ni
la verificación de calibración o contraste.

El propietario añadió que, después de rellenar, el nivel de agua en C3 quedó a
**117 mm del borde superior**. Se registra como medición comunicada; no se
indicó el instrumento ni el punto exacto de referencia en el borde.

## Telemetría asociada de Home Assistant

La consulta de Home Assistant se realizó poco después del aviso. Las marcas
horarias se muestran en hora local de Canarias (WEST, UTC+1).

| Variable | Entidad | Valor observado | Momento | Alcance |
| --- | --- | ---: | --- | --- |
| Temperatura del agua | `sensor.0xa4c13810b72fffff_temperature` (`off-sns-05`) | 28,2 °C | Estado sin cambio desde 17:14:32; mensaje Zigbee más reciente a las 17:24:34 | Contexto térmico próximo a la reposición; el mensaje reciente no implica que la cifra de temperatura haya cambiado. |
| Antigüedad del mensaje de `off-sns-05` | `sensor.veril_water_sensor_age` | 0,4 min | 17:25 | Confirma recepción reciente de telemetría, no una nueva lectura numérica de temperatura. |
| Tendencia del agua, ventana 30 min | `sensor.veril_velocidad_termica_agua_30_min` | +0,025 °C/h | 17:14:32 | Último valor calculado registrado; no acredita el efecto de la reposición. |
| Tendencia del agua, ventana 60 min | `sensor.veril_velocidad_termica_agua_60_min` | +0,026 °C/h | 17:14:32 | Último valor calculado registrado; no acredita el efecto de la reposición. |
| Temperatura ambiente mediana del despacho | `sensor.veril_room_temperature_median` | 30,4 °C | 17:18:41 | Contexto ambiental; no mide el nivel de C3 ni la salinidad. |
| Gravedad específica del monitor `off-sns-09` | `sensor.0xa4c138ed21676ef4_sg` | 1,067 | 16:29:23 | Valor de más de 50 min antes de la reposición aproximada; no es contemporáneo ni valida el refractómetro. |

Las entidades de salinidad (50 ‰), TDS (13.000 ppm) y EC (20.000 μS/cm) de
`off-sns-09` conservaban estados desde el 24 de septiembre, por lo que no se
consideran lecturas de esta operación. No se identificó una entidad de Home
Assistant que mida el nivel de C3; los **117 mm** son la medición comunicada
por el propietario.

## Interpretación y límites

Home Assistant registraba 28,2 °C en el agua cerca de la operación y telemetría
reciente de `off-sns-05`; no ofrece una medición del nivel de C3. El monitor
`off-sns-09` presentaba una gravedad específica de 1,067 con más de 50 min de
antigüedad y otras lecturas de salinidad/TDS/EC de dos días antes. Estos datos
no corroboran la lectura manual aproximada de 1,032, que seguía fuera de escala,
ni permiten establecer la salinidad final con precisión. La cota final de
117 mm tampoco determina por sí sola el volumen añadido, pues no se registró
la cota inicial ni la geometría de llenado de C3.

## Pendientes derivados

- [ ] Comprobar el refractómetro con el procedimiento y una referencia adecuados, y repetir la lectura dentro de su escala
- [ ] Registrar en futuras reposiciones el volumen transferido y el nivel de C3 antes y después

## Fuentes internas

- [Medición manual de salinidad y química inicial del 20 de septiembre](2026-09-20-medicion-manual-salinidad-y-quimica.md)
- [Parámetro de salinidad](../../../01_verilpedia/03_parametros/salinidad.md)
