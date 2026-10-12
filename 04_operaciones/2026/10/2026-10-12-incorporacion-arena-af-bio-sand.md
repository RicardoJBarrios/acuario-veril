# 12 de octubre de 2026 — Incorporación de AF Bio Sand

## Ejecución comunicada

El propietario comunica que hoy incorporó al display aproximadamente **8 kg**
de AF Bio Sand, procedentes de la remesa activada durante 24 horas y registrada
el [11 de octubre](2026-10-11-activacion-af-bio-sand.md). Comunica que la cama
resultante tiene aproximadamente **3 cm** de altura.

El 12 de octubre, el propietario adopta **3 cm** como profundidad objetivo de
la cama regular. La decisión sustituye la referencia anterior de 20 mm en la
configuración de Veril. La basa en la recomendación de Aquaforest, otras
referencias de acuariofilia marina, su preferencia estética y el uso previsto
por fauna que se entierra. La valoración biológica y los límites de esta
profundidad constan en la [configuración espacial](../../../02_configuracion/01_dimensiones/02_espacial.md#sustrato-integrado-en-la-composición).

Al entrar en contacto con el agua que ya había en el acuario, la arena dejó el
agua muy blanca. El propietario está esperando a que se asiente para repartir
la arena de forma uniforme. No se ha comunicado que el agua haya aclarado ni
que la cama se haya nivelado todavía.

Las dos bombas están encendidas. El skimmer permanece apagado y el propietario
confirma que no hay esterilizador UV instalado. El propietario comunica una
lectura de **26,3 °C** del sensor sumergido del acuario **off-sns-05**. Más tarde,
a las **18:54 (hora local, Canarias)**, comunica una nueva lectura del mismo
sensor: **26,4 °C**.

Después de incorporar la arena, el propietario añadió **466 ml de FritzZyme 9**
inmediatamente antes de tomar las mediciones, por error respecto al orden
previsto. Posteriormente, añadió **4 ml de Fishless Fuel a las 18:52 (hora local,
Canarias)**.

## Mediciones comunicadas después de añadir FritzZyme 9

Las lecturas se tomaron después de la inoculación y, por tanto, no constituyen
una línea base previa a ella:

| Parámetro | Lectura | Método comunicado |
| --- | ---: | --- |
| Salinidad | 35,5 ppt | Refractómetro D-D The Aquarium Solution AQPR001 |
| NO₃ | 50 mg/L como NO₃⁻ | Tetra 7 in 1 |
| NO₂ | 5 mg/L como NO₂⁻ | Tetra 7 in 1 |
| GH | 8 °dH | Tetra 7 in 1 |
| KH | 10 °dH | Tetra 7 in 1 |
| pH | 7,6 | Tetra 7 in 1 |
| Cloro (Cl₂) | 0 mg/L | Tetra 7 in 1 |
| KH | 7,7 dKH | Salifert |
| Amonio total (NH₃ + NH₄⁺) | `<0,15 mg/L` | Salifert Ammonia; escala del kit |
| NO₂ | `4 mg/L como NO₂⁻` | Salifert NO₂; escala del kit |

La discrepancia entre KH de la tira (°dH) y Salifert (dKH) se conserva como dos
resultados de métodos distintos; no se promedian. Tetra expresa NO₂ y NO₃ en
mg/L como sus respectivos iones, GH/KH en °dH y Cl₂ en mg/L; pH es adimensional.
Salifert expresa amonio total en mg/L, NO₂ en mg/L según la escala del kit y KH
en dKH. Se conservan las lecturas en la unidad nativa de cada prueba, sin
convertirlas ni atribuirles precisión superior a la escala visual.

## Telemetría asociada de Home Assistant

No se consultó Home Assistant durante esta operación ni se accionó ningún
equipo. Las dos temperaturas son lecturas del sensor sumergido **off-sns-05**,
comunicadas por el propietario; no se recuperó aquí el historial de telemetría
para contrastar sus marcas temporales.

## Estado y pendientes

La arena está incorporada; siguen pendientes su distribución uniforme y el
asentamiento final. La medición previa a la inoculación ya no puede
recuperarse. Los **4 ml de Fishless Fuel** se añadieron después de las
mediciones de la tabla, a las **18:52 (hora local, Canarias)**; todavía no se ha
comunicado una lectura posterior a su mezcla. Las lecturas iniciales no
demuestran por sí solas capacidad nitrificante establecida: NO₂ es medible y
el amonio total está por debajo del límite reportado por el test, no confirmado
como cero absoluto. Medir NH₃/NH₄ tras mezclar Fishless Fuel y continuar con las
mediciones diarias del runbook; no redosificar por una lectura inferior a la
prevista. La siguiente carga de desafío sigue sujeta a las puertas de decisión
del
[runbook de ciclado](../../../03_pendientes/ciclado/runbook.md).

**Estado:** arena incorporada; 466 ml de FritzZyme 9 añadidos inmediatamente
antes de las mediciones, y 4 ml de Fishless Fuel añadidos a las 18:52, hora
local. Pendiente resultado posterior a Fishless Fuel.
