# 17 de octubre de 2026 — Medición diaria del ciclado

## Mediciones comunicadas

El propietario comunica estas lecturas como tomadas «justo ahora» el **17 de
octubre de 2026**. No se asigna una hora exacta. Son resultados manuales
comunicados por el propietario; no se aporta fotografía de las escalas en esta
ronda.

| Parámetro | Lectura | Método y alcance |
| --- | --- | --- |
| Temperatura | 27,2 °C | Lectura comunicada por el propietario; instrumento no especificado en este mensaje |
| Amonio total (NH₃ + NH₄⁺) | 0 mg/L, categoría del test | Salifert Ammonia NH3 Profi Test; lectura visual, no demostración de cero absoluto |
| NO₂, test principal | >4 mg/L, escala del kit | Salifert NO2 Profi Test; fuera de escala, sin extrapolar un valor exacto |
| NO₃, tira | 250 mg/L como NO₃⁻ | Tetra Test 7 en 1, lectura visual de su escala |
| NO₂, tira | 10 mg/L como NO₂⁻ | Tetra Test 7 en 1 |
| GH, tira | 8 °dH | Tetra Test 7 en 1 |
| KH, tira | 6 °dH | Tetra Test 7 en 1; no es una titulación Salifert |
| pH, tira | 6,8 | Tetra Test 7 en 1; lectura visual pendiente de confirmación con método apto para agua marina |
| Cl₂, tira | 0 mg/L | Tetra Test 7 en 1, categoría de su escala |

No se comunica una lectura de salinidad en esta ronda. Los dos métodos de
nitrito se conservan separados y no se promedian. No se comunica una titulación
de KH con Salifert.

Se conservan las unidades documentadas en las fichas de
[amonio](../../../01_verilpedia/05_productos/12_salifert-ammonia-nh3/salifert-ammonia-nh3.md),
[nitrito](../../../01_verilpedia/05_productos/13_salifert-no2/salifert-no2.md) y
[Tetra Test 7 en 1](../../../01_verilpedia/05_productos/14_tetra-test-7-en-1/tetra-test-7-en-1.md).

## Telemetría asociada de Home Assistant

No se consultó Home Assistant. La temperatura y la química quedan como
lecturas manuales comunicadas por el propietario, sin contraste de entidad,
marca temporal ni actualización. No se infieren parámetros químicos a partir
de otras variables ni se accionó equipo alguno.

## Interpretación limitada y seguimiento

El amonio permanece en la categoría visual **0**, mientras el nitrito Salifert
sigue en **>4** y la tira en **10 mg/L**. El nitrito continúa detectable; por
tanto, no se cumple el criterio del runbook para añadir la segunda carga de
**2 ml de Fishless Fuel**. Estas lecturas no demuestran el cierre del ciclado.

La tira repite **NO₃ 250**, **NO₂ 10**, **GH 8**, **KH 6**, **pH 6,8** y **Cl₂
0** respecto a la ronda del 16 de octubre. La repetición de categorías visuales
no demuestra estabilidad cuantitativa. El pH y la alcalinidad siguen pendientes
de confirmación con métodos aptos para agua marina; no se prescribe una
corrección a partir de la tira.

La temperatura comunicada de **27,2 °C** está **0,7 °C por encima** del límite
superior del objetivo operativo normal local (**24,5–26,5 °C**) y dentro de la
banda cálida local (**26,5–27,5 °C**). La lectura anterior comunicada fue
26,5 °C el 16 de octubre. Dos puntos no determinan cuánto tiempo lleva el agua
en esta banda ni acreditan una tendencia sostenida o el estado del control
térmico; conviene comprobar la lectura y su evolución con el seguimiento
habitual.

**Estado:** operación documentada sin telemetría pertinente disponible;
ciclado sin criterio de cierre, con temperatura por encima del objetivo normal
y pH/alcalinidad pendientes de confirmación.
