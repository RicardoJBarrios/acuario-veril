# 15 de octubre de 2026 — Medición diaria del ciclado

## Mediciones comunicadas

El propietario comunica estas lecturas como tomadas «ahora mismo» el **15 de
octubre de 2026**. No se asigna una hora exacta de toma: la hora de consulta o
edición no sustituye una hora comunicada por el propietario. La fuente es su
lectura manual de los tests, sin fotografía de las escalas en esta ronda.

| Parámetro | Lectura | Método y alcance |
| --- | --- | --- |
| Amonio total (NH₃ + NH₄⁺) | 0 mg/L, categoría del test | Salifert Ammonia NH3 Profi Test; lectura visual, no demostración de cero absoluto |
| NO₂, test principal | >4 mg/L, escala del kit | Seguimiento con Salifert NO2 Profi Test; fuera de escala, sin extrapolar un valor exacto |
| NO₃, tira | 100 mg/L como NO₃⁻ | Tetra Test 7 en 1 |
| NO₂, tira | 10 mg/L como NO₂⁻ | Tetra Test 7 en 1 |
| GH, tira | 8 °dH | Tetra Test 7 en 1 |
| KH, tira | 6 °dH | Tetra Test 7 en 1; no titulación Salifert |
| pH, tira | 7,2 | Tetra Test 7 en 1; pendiente de confirmación con método apto para agua marina |
| Cl₂, tira | 0 mg/L | Tetra Test 7 en 1, categoría de su escala |
| Temperatura | 26,9 °C | Lectura comunicada por el propietario como complemento de esta ronda; instrumento no especificado en este mensaje |

Se conservan las unidades documentadas en las fichas de
[amonio](../../../01_verilpedia/05_productos/12_salifert-ammonia-nh3/salifert-ammonia-nh3.md),
[nitrito](../../../01_verilpedia/05_productos/13_salifert-no2/salifert-no2.md) y
[Tetra Test 7 en 1](../../../01_verilpedia/05_productos/14_tetra-test-7-en-1/tetra-test-7-en-1.md).
Los dos métodos de nitrito se mantienen separados y no se promedian. No se han
comunicado hoy salinidad, CO₂ ni una titulación de KH con Salifert.

## Telemetría asociada de Home Assistant

No se ha consultado Home Assistant. No se dispone en esta sesión de una entidad
química identificada y validada que corrobore estos tests manuales; tampoco hay
un MCP de Home Assistant disponible entre las herramientas. No se infieren los
resultados químicos a partir de conductividad, TDS o temperatura. No se ha
accionado equipo alguno.
La temperatura de 26,9 °C permanece como lectura comunicada, sin contrastar aquí
la entidad del sensor, su actualización ni su marca temporal.

## Interpretación limitada y seguimiento

La temperatura comunicada de **26,9 °C** está **0,4 °C por encima** del límite
superior del objetivo operativo normal local de **24,5–26,5 °C**. Ayer se
comunicaron 27,1 °C; la diferencia entre estas muestras es de −0,2 °C, sin
establecer una tendencia sostenida ni la duración de la temperatura elevada.
El objetivo local no se interpreta como un umbral biológico universal y esta
lectura no acredita cambios en la refrigeración.

Frente a [la ronda del 14 de octubre](2026-10-14-medicion-diaria-ciclado.md), el
amonio pasa de una descripción visual más cercana a cero a la categoría **0**.
El nitrito principal sigue en **>4**: el test no permite establecer si ha subido,
bajado o permanecido igual dentro de ese intervalo. Es compatible con amonio
bajo y nitrito acumulado durante el ciclado, sin acreditar su finalización.

Según el [runbook](../../../03_pendientes/ciclado/runbook.md), no se cumple todavía
la condición de amonio y nitrito en el límite de aceptación durante 24 horas para
la segunda carga de **2 ml de Fishless Fuel**. Esta ronda no habilita esa carga
ni la introducción de fauna o equipo de limpieza.

La tira repite **NO₃ 100**, **NO₂ 10**, **GH 8**, **pH 7,2** y **Cl₂ 0** respecto
a ayer; su KH cambia de **10 a 6 °dH**. Son categorías visuales repetidas o
distintas, sin demostrar estabilidad exacta ni una caída real de alcalinidad de
4 dKH. El KH Salifert de **8,9 dKH del 13 de octubre** procede de otro método y
otra fecha; no se resta directamente del resultado actual de la tira.

La prioridad es confirmar **pH y KH** con métodos aptos para agua marina,
incluido el Salifert KH/Alk disponible para alcalinidad. No se da por confirmado
un pH real de 7,2 ni se prescribe una corrección con aditivos a partir de la tira.
El [manual oficial de Tetra](https://www.tetra.net/fileadmin/pictures/TH54269_9074.pdf),
consultado el 15 de octubre, explica sus referencias de pH para peces de agua
dulce; ni ese manual ni la
[página del producto consultada](https://www.tetra.net/en-eu/products/tetra-test-7in1)
aportan una validación expresa localizada para cuantificar estos parámetros en
agua marina. Esto limita la interpretación, sin demostrar por sí solo que cada
campo de la tira sea erróneo.

El NO₃ de tira no permite cuantificar por sí solo la conversión de nitrito ni
cerrar el ciclo. No se calcula CO₂ a partir de pH y KH de la tira ni se utiliza
GH para deducir salinidad, calcio o magnesio marinos. Mantener el seguimiento de
amonio y nitrito y confirmar el pH sin esperar a que una repetición de la tira
equivalga a validación. Esta entrada no acredita dosificaciones ni cambios de
agua, que no se han comunicado.

**Estado:** operación documentada sin telemetría pertinente o disponible;
ciclado sin criterio de cierre, con pH y alcalinidad pendientes de confirmación.
