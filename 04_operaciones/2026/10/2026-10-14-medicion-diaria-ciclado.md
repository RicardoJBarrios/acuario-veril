# 14 de octubre de 2026 — Medición diaria del ciclado

## Mediciones comunicadas

El propietario comunica que acaba de realizar los tests el **14 de octubre de
2026**. Hora exacta de la toma no comunicada. Fecha atribuida a «acabo de hacer»
en la sesión de ese día, sin asignar la hora de edición como hora de medición.
La salinidad se conserva en ppt y la temperatura como lectura comunicada, sin
atribuir un instrumento que no se ha vuelto a identificar en esta ronda.

| Parámetro | Lectura | Método y alcance |
| --- | --- | --- |
| Salinidad | 35 ppt | Lectura comunicada; método disponible documentado: refractómetro D-D AQPR001, no vuelto a especificar hoy |
| Temperatura | 27,1 °C | Lectura comunicada por el propietario; instrumento no especificado hoy |
| Amonio total (NH₃ + NH₄⁺) | Color más próximo a 0 que a <0,15 | Salifert Ammonia NH3 Profi Test; descripción visual, sin interpolación numérica ni confirmación de cero absoluto |
| NO₂, test principal | >4, escala comunicada | Seguimiento con Salifert NO2 Profi Test documentado en la ronda anterior; el propietario no vuelve a nombrar el kit para esta lectura. Se conserva >4, sin extrapolar fuera de escala |
| NO₃, tira | 100 mg/L como NO₃⁻ | Tetra Test 7 en 1, misma tira que el día anterior, confirmada por el propietario |
| NO₂, tira | 10 mg/L como NO₂⁻ | Tetra Test 7 en 1 |
| GH, tira | 8 °dH | Tetra Test 7 en 1 |
| KH, tira | 10 °dH | Tetra Test 7 en 1; no es una titulación Salifert |
| pH, tira | 7,2 | Lectura visual pendiente de confirmación |
| Cl₂, tira | 0 mg/L | Tetra Test 7 en 1, escala de la tira |

El orden comunicado fue NO₃, NO₂, GH, KH, pH y Cl₂. El propietario confirma
que la tira llamada inicialmente «10 en 1» es la misma **Tetra Test 7 en 1**
utilizada ayer. Se aplican las unidades documentadas de su escala: NO₃, NO₂ y
Cl₂ en mg/L, GH y KH en °dH, y pH adimensional. Las lecturas de ambos métodos
se conservan separadas y no se promedian.
No se ha comunicado hoy una titulación de KH con Salifert.

## Telemetría asociada de Home Assistant

Se consideró pertinente contrastar temperatura y actualización del sensor
sumergido. El MCP de Home Assistant no está disponible entre las herramientas
de esta sesión y el preflight de la alternativa REST no encontró la combinación
de URL y credencial necesaria en el entorno/configuración local consultados.
No se realizó consulta de estados ni se accionó equipo alguno. La temperatura
de 27,1 °C permanece como lectura comunicada por el propietario, sin marca
temporal de entidad contrastada. Esta falta de acceso no indica un fallo del
sensor ni del acuario.

## Interpretación limitada y seguimiento

Respecto a [la ronda del 13 de octubre](2026-10-13-medicion-diaria-ciclado.md),
el amonio se describe visualmente más cerca de cero y el nitrito principal
pasa de 4 a >4. Es compatible con una fase de ciclado con amonio bajo y nitrito
acumulado, sin demostrar la velocidad de transformación ni el cierre del ciclo.
Con nitrito detectable fuera de escala no se cumple el criterio local de
amonio y nitrito en cero durante 24 horas para autorizar la segunda carga de
2 ml de Fishless Fuel. No corresponde redosificar ahora según el
[runbook](../../../03_pendientes/ciclado/runbook.md).

El pH de tira cambia de 8,0 a 7,2 frente a la ronda anterior. La diferencia
requiere comprobar método, tiempo de lectura e idoneidad para agua marina, y
confirmar con un test de pH apto para agua salada o un medidor calibrado.
Repetir también KH con el Salifert disponible para valorar alcalinidad.
No se atribuye la diferencia al ciclado ni se recomienda corregir pH con
aditivos a partir de esta tira sola. Un deterioro confirmado y sostenido de
pH o alcalinidad obligaría a revisar la progresión conforme al runbook.

El NO₃ de tira comunicado cambia de 50 a 100 respecto a ayer, con la misma Tetra Test 7 en 1 confirmada por el propietario. La lectura visual
de la tira no confirma por sí sola una duplicación real del nitrato
ni permite estimar el avance del ciclado. La ficha general de
[nitrato](../../../01_verilpedia/03_parametros/nitrato.md) recuerda que el nitrito
puede interferir en determinados métodos; no se cuantifica ni se afirma esa
interferencia para esta tira concreta.

La temperatura comunicada, 27,1 °C, supera el objetivo operativo normal local
de 24,5–26,5 °C. La lectura de ayer fue 27 °C; dos muestras puntuales no
establecen cuánto tiempo permaneció elevada. No se modifica la automatización
ni se interpreta este objetivo operativo como umbral biológico universal.
La salinidad se mantiene en los 35 ppt comunicados ayer.

Mantener el seguimiento diario de amonio y nitrito en esta fase inicial y
comprobar circulación y agitación superficial. La confirmación del pH tiene
prioridad sobre esperar a la siguiente ronda habitual. Esta entrada no acredita
cambios de agua, dosificaciones ni correcciones, que no se han comunicado.

**Estado:** operación documentada sin telemetría disponible; ciclado aún sin
criterio de cierre y pH bajo de tira pendiente de confirmar.
