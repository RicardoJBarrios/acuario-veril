# 2026-09-20 — Medición manual de salinidad y química inicial

## Estado

Operación documentada con observación manual y telemetría contextual.

## Contexto

El ciclado de Veril todavía no ha comenzado. Hasta disponer del sistema RO/DI,
se han realizado varias reposiciones con agua salada; el usuario identifica
este hecho como explicación coherente de la concentración progresiva de la
salinidad. No se registraron los volúmenes ni las fechas de cada reposición.

## Mediciones manuales observadas

### Salinidad

Se realizaron varias lecturas con el refractómetro D-D The Aquarium Solution
AQPR001. La densidad específica observada fue aproximadamente **1,031**. El
resultado se comunicó como coherente entre repeticiones y con las reposiciones
realizadas con agua salada.

No se registraron la temperatura de la muestra, la verificación del cero, una
solución patrón ni la escala de lectura. Por ello, esta cifra describe una
observación repetida, pero no constituye todavía una aceptación metrológica de
la salinidad ni una equivalencia automática en ppt o salinidad práctica.

### Tetra Test 7 en 1

La tira Tetra 7 en 1 dio las siguientes lecturas comunicadas:

| Parámetro | Resultado | Unidad o escala |
| --- | ---: | --- |
| Nitrato, NO₃ | 0 | mg/L |
| Nitrito, NO₂ | 0 | mg/L |
| Dureza general, GH | 8 | °dH |
| Alcalinidad carbonatada, KH | 6 | °dH |
| pH | 7,6 | escala de pH |
| Cloro, Cl₂ | 0 | mg/L |

Las tiras se conservan como caracterización orientativa. En agua marina, el GH
no se utilizará como control operativo y las lecturas de pH y KH requerirán
confirmación mediante métodos adecuados antes de modificar la química del
sistema. Esta medición no incluye nitrógeno amoniacal.

## Telemetría asociada de Home Assistant

| Variable | Entidad | Valor observado | Momento de la lectura | Alcance |
| --- | --- | ---: | --- | --- |
| Temperatura del agua | `sensor.0xa4c13810b72fffff_temperature` | 27,8 °C | 2026-09-20 18:35 WEST | Lectura del termómetro con sonda `off-sns-05` situado en la cámara Skimmer; contexto térmico, no validación de los tests manuales. |

## Interpretación limitada

La densidad específica observada es alta respecto de la consigna prevista
`S_P = 35`, pero no se corregirá con una intervención brusca ni se iniciará el
ciclado a partir de esta medición. Antes del inicio siguen pendientes el
montaje y la aceptación del RO/DI, la reposición exclusiva con agua RO/DI y una
línea base con métodos adecuados para salinidad, pH, alcalinidad, nitrógeno
amoniacal y nitrito.

## Pendientes derivados

- [ ] Montar y aceptar el sistema RO/DI antes de una corrección controlada de salinidad.
- [ ] Registrar las futuras reposiciones con fecha, volumen y tipo de agua.
- [ ] Limpiar el prisma, comprobar el cero y contrastar el refractómetro con una solución patrón marina antes de aceptar la salinidad.
- [ ] Repetir la línea base de pH y alcalinidad con métodos adecuados antes del ciclado.
- [ ] Medir nitrógeno amoniacal al iniciar la línea base de ciclado.

## Fuentes internas

- [Comprobación de salinidad del 13 de septiembre](2026-09-13-comprobacion-salinidad-refractometro.md)
- [Tetra Test 7 en 1](../../../01_verilpedia/05_productos/14_tetra-test-7-en-1/tetra-test-7-en-1.md)
- [Refractómetro D-D AQPR001](../../../01_verilpedia/05_productos/06_dd-aquarium-solution-aqpr001/dd-aquarium-solution-aqpr001.md)
- [Plan de ciclado](../../../03_pendientes/ciclado/plan.md)
