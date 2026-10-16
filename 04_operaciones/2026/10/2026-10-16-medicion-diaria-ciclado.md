# 16 de octubre de 2026 — Medición diaria del ciclado

## Mediciones comunicadas

El propietario comunica estas lecturas como tomadas «ahora» el **16 de octubre de 2026**. No se asigna una hora exacta. Son resultados manuales comunicados por el propietario; no se aporta fotografía de las escalas en esta ronda.

| Parámetro | Lectura | Método y alcance |
| --- | --- | --- |
| Salinidad | 35 ppt | Lectura comunicada; el método de esta ronda no se especifica |
| Temperatura | 26,5 °C | Lectura comunicada por el propietario; instrumento no especificado en este mensaje |
| Amonio total (NH₃ + NH₄⁺) | 0 mg/L, categoría del test | Salifert Ammonia NH3 Profi Test; lectura visual, no demostración de cero absoluto |
| NO₂, test principal | >4 mg/L, escala del kit | Salifert NO2 Profi Test; fuera de escala, sin extrapolar un valor exacto |
| NO₃, tira | 250 mg/L como NO₃⁻ | Tetra Test 7 en 1, lectura visual de su escala |
| NO₂, tira | 10 mg/L como NO₂⁻ | Tetra Test 7 en 1 |
| GH, tira | 8 °dH | Tetra Test 7 en 1 |
| KH, tira | 6 °dH | Tetra Test 7 en 1; no es una titulación Salifert |
| pH, tira | 6,8 | Tetra Test 7 en 1; lectura visual pendiente de confirmación con método apto para agua marina |
| Cl₂, tira | 0 mg/L | Tetra Test 7 en 1, categoría de su escala |

El propietario indica que no se ha intervenido en el agua desde la ronda anterior. No comunica cambio de agua ni corrección. Los métodos de nitrito se conservan separados y no se promedian. No se ha comunicado una titulación de KH con Salifert.

Se conservan las unidades documentadas en las fichas de
[amonio](../../../01_verilpedia/05_productos/12_salifert-ammonia-nh3/salifert-ammonia-nh3.md),
[nitrito](../../../01_verilpedia/05_productos/13_salifert-no2/salifert-no2.md) y
[Tetra Test 7 en 1](../../../01_verilpedia/05_productos/14_tetra-test-7-en-1/tetra-test-7-en-1.md).

## Telemetría asociada de Home Assistant

No se consultó Home Assistant. Las herramientas de Home Assistant no están disponibles en esta sesión y no se identificó una entidad pertinente que pudiera contrastarse. La temperatura y la química permanecen como lecturas comunicadas por el propietario, sin entidad, marca temporal ni actualización contrastadas. No se infieren resultados químicos a partir de conductividad o TDS y no se accionó equipo alguno.

## Interpretación limitada y seguimiento

El amonio continúa en la categoría visual **0**, mientras el nitrito Salifert sigue **>4** y la tira sigue marcando **10 mg/L**. El nitrito permanece detectable; por tanto, la condición del runbook para añadir la segunda carga de **2 ml de Fishless Fuel** no se cumple. Estas lecturas no demuestran el cierre del ciclado.

La tira marca NO₃ **250 mg/L**, frente a **100 mg/L** en la ronda del 15 de octubre. Este cambio de categoría visual no confirma por sí solo un aumento cuantitativo real ni mide el avance del ciclado. El NO₃ de la tira tampoco permite calcular cuánto nitrito se ha convertido.

El pH de tira pasa de **7,2 a 6,8** respecto a ayer y el KH de tira permanece en **6 °dH**. Ambos datos requieren confirmación; el cambio de lectura no demuestra por sí solo una caída real del pH. Conviene comprobar pH con un método apto para agua marina y repetir la alcalinidad mediante titulación Salifert antes de considerar cualquier corrección. El runbook establece revisar la progresión ante un deterioro sostenido confirmado de pH o alcalinidad; esta lectura puntual no determina su duración ni confirma ese deterioro.

La temperatura comunicada de **26,5 °C** está en el límite superior del objetivo operativo normal local (**24,5–26,5 °C**), sin excederlo. La ronda anterior fue de 26,9 °C; estas dos lecturas puntuales no determinan duración ni tendencia sostenida. La salinidad comunicada permanece en **35 ppt** y el propietario indica que no se ha intervenido en el agua.

**Estado:** operación documentada sin telemetría pertinente disponible; ciclado sin criterio de cierre y pH/alcalinidad pendientes de confirmación.
