# 20 de septiembre de 2026 — Medición manual de salinidad y química inicial

## Contexto comunicado

El ciclado todavía no había comenzado. El propietario comunicó que había
realizado varias reposiciones con agua salada hasta disponer del sistema RO/DI
e identificó este hecho como explicación de la concentración progresiva de la
salinidad.

## Mediciones manuales

Se realizaron varias lecturas con el refractómetro **D-D The Aquarium Solution
AQPR001**. La densidad específica observada fue aproximadamente **1,031**. El
propietario comunicó que las repeticiones eran coherentes entre sí.

La tira Tetra Test 7 en 1 dio las siguientes lecturas comunicadas:

| Parámetro | Resultado | Unidad o escala |
| --- | ---: | --- |
| Nitrato, NO₃ | 0 | mg/L |
| Nitrito, NO₂ | 0 | mg/L |
| Dureza general, GH | 8 | °dH |
| Alcalinidad carbonatada, KH | 6 | °dH |
| pH | 7,6 | escala de pH |
| Cloro, Cl₂ | 0 | mg/L |

## Telemetría asociada de Home Assistant

| Variable | Entidad | Valor observado | Momento de la lectura | Alcance |
| --- | --- | ---: | --- | --- |
| Temperatura del agua | `sensor.0xa4c13810b72fffff_temperature` | 27,8 °C | 2026-09-20 18:35 WEST | Lectura del termómetro con sonda `off-sns-05` situado en la cámara Skimmer; lectura de Home Assistant. |

## Referencias

- [Comprobación de salinidad del 13 de septiembre](2026-09-13-comprobacion-salinidad-refractometro.md)
- [Tetra Test 7 en 1](../../../01_verilpedia/05_productos/14_tetra-test-7-en-1/tetra-test-7-en-1.md)
- [Refractómetro D-D AQPR001](../../../01_verilpedia/05_productos/06_dd-aquarium-solution-aqpr001/dd-aquarium-solution-aqpr001.md)
- [Plan de ciclado](../../../03_pendientes/ciclado/plan.md)
