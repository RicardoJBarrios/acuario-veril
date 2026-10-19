# 26 de septiembre de 2026 — Reposición manual y lectura de salinidad

## Ejecución comunicada

Como quedaba poca agua en la cámara C3, se añadió agua al sistema desde el
barril. El barril contenía agua salada. Su volumen se estimó en **unos 3,6 L**
antes de la operación y **unos 1,75 L** después.

El volumen añadido comunicado por el propietario es de aproximadamente
**1,85 L**, calculado restando el volumen final al inicial del barril:
3,6 L − 1,75 L. La cifra es aproximada porque ambos volúmenes de partida se
estimaron.

El propietario precisó que hizo la reposición y la lectura del refractómetro
unos minutos antes de comunicarlo.

## Resultado observado

Después de la reposición, el refractómetro seguía indicando una lectura fuera
de escala, aproximadamente **1,032**, según la notación comunicada.

El propietario añadió que el nivel de C3 quedó a **117 mm del borde superior**.

## Telemetría asociada de Home Assistant

Consulta realizada poco después de la comunicación. Horas locales de Canarias
(WEST, UTC+1).

| Variable | Entidad | Valor observado | Momento | Alcance |
| --- | --- | ---: | --- | --- |
| Temperatura del agua | `sensor.0xa4c13810b72fffff_temperature` (`off-sns-05`) | 28,2 °C | Estado sin cambio desde 17:14:32; mensaje Zigbee más reciente a las 17:24:34 | Estado de temperatura y último mensaje Zigbee. |
| Antigüedad del mensaje de `off-sns-05` | `sensor.veril_water_sensor_age` | 0,4 min | 17:25 | Antigüedad del mensaje Zigbee. |
| Tendencia del agua, ventana 30 min | `sensor.veril_velocidad_termica_agua_30_min` | +0,025 °C/h | 17:14:32 | Salida calculada de Home Assistant. |
| Tendencia del agua, ventana 60 min | `sensor.veril_velocidad_termica_agua_60_min` | +0,026 °C/h | 17:14:32 | Salida calculada de Home Assistant. |
| Temperatura ambiente mediana del despacho | `sensor.veril_room_temperature_median` | 30,4 °C | 17:18:41 | Mediana ambiental del despacho. |
| Gravedad específica del monitor `off-sns-09` | `sensor.0xa4c138ed21676ef4_sg` | 1,067 | 16:29:23 | Estado de las 16:29:23. |

El monitor `off-sns-09` conservaba estados del **24 de septiembre**:
salinidad **50 ‰**, TDS **13.000 ppm** y EC **20.000 μS/cm**.

## Fuentes internas

- [Medición manual de salinidad y química inicial del 20 de septiembre](2026-09-20-medicion-manual-salinidad-y-quimica.md)
- [Parámetro de salinidad](../../../01_verilpedia/03_parametros/salinidad.md)
