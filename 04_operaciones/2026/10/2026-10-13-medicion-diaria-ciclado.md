# 13 de octubre de 2026 — Medición diaria del ciclado

## Mediciones comunicadas

El propietario comunica que realizó las mediciones de seguimiento del ciclado el **13 de octubre de 2026 a las 19:42 (hora local de Canarias)**. La temperatura corresponde al sensor sumergido del acuario **off-sns-05**; la salinidad se conserva en la escala comunicada.

| Parámetro | Lectura | Método / procedencia |
| --- | ---: | --- |
| Salinidad | 35 ppt | Refractómetro D-D The Aquarium Solution AQPR001, único método de salinidad disponible documentado para Veril |
| Temperatura del agua | 27 °C | Sensor sumergido del acuario off-sns-05; valor comunicado por el propietario |
| KH | 8,9 dKH | Salifert KH/Alk Profi Test |
| NO₂ | 4 mg/L, escala del kit | Salifert NO2 Profi Test |
| Amonio total (NH₃ + NH₄⁺) | `<0,15 mg/L`, escala del kit | Salifert Ammonia NH3 Profi Test; no equivale a una confirmación de cero absoluto |
| NO₃ | 50 mg/L como NO₃⁻, escala de la tira | Tetra Test 7 en 1 |
| NO₂ | 10 mg/L como NO₂⁻, escala de la tira | Tetra Test 7 en 1 |
| GH | 8 °dH | Tetra Test 7 en 1 |
| KH | 10 °dH | Tetra Test 7 en 1 |
| pH | 8,0 | Tetra Test 7 en 1; se usa como método disponible para pH |
| Cl₂ | 0 mg/L, escala de la tira | Tetra Test 7 en 1 |

Las lecturas de NO₂ de Salifert y Tetra y las lecturas de KH de Salifert y Tetra se conservan por separado: proceden de métodos y escalas distintas y no se promedian. Las cifras de Tetra son lecturas visuales de tira y no se les atribuye precisión mayor que la escala del fabricante.

## Telemetría asociada de Home Assistant

No se consultó Home Assistant en esta sesión. La temperatura de **27 °C** se registra como valor comunicado por el propietario del sensor sumergido `off-sns-05`, sin contrastar aquí el estado, la actualización ni la marca temporal de la entidad `sensor.0xa4c13810b72fffff_temperature`.

## Alcance y seguimiento

Esta entrada conserva una ronda de mediciones manuales durante el ciclado iniciado el 12 de octubre. El amonio total permanece por debajo del límite indicado por el test, pero no queda confirmado como cero absoluto; el nitrito continúa siendo detectable en ambos métodos. Por tanto, estas lecturas no satisfacen la condición documentada para añadir la segunda dosis de **2 ml de Fishless Fuel**, que requiere que amonio y nitrito alcancen el límite de aceptación y permanezcan así durante 24 horas.

La temperatura comunicada de **27 °C** supera el límite superior de **26,5 °C** del objetivo operativo normal del runbook. Es una lectura puntual; sin una serie temporal contrastada no permite establecer cuánto duró ni si hubo una excursión sostenida. Se mantienen los resultados originales de cada método para comparar la evolución sin convertir ni promediar escalas distintas.

**Estado:** mediciones diarias registradas; la segunda carga de desafío no queda habilitada por esta lectura.
