# Veril: química

> La [dimensión química](../../01_verilpedia/01_dimensiones/05_quimica.md) define cómo interpretar composición, relaciones, tendencias y estabilidad. Esta ficha registra la aplicación prevista en Veril sin repetir las fichas generales de parámetros.

## Aplicación adoptada

La química de Veril se seguirá mediante las [fichas de parámetros](../../01_verilpedia/03_parametros/README.md), con atención a la relación entre salinidad, temperatura, pH, alcalinidad, compuestos nitrogenados, nitrato, fosfato y oxígeno cuando corresponda a la fase del sistema.

El agua tiene como zona preferida **25–26 °C** y como objetivo normal **24,5–26,5 °C**. Las bandas y respuestas operativas están en [Régimen térmico adoptado](../README.md#régimen-térmico-adoptado). Aquí la temperatura se interpreta como variable química y contexto de medición.

El agua de reposición por evaporación será agua RO/DI mediante el [ATO seleccionado](../../01_verilpedia/04_hardware/dd-h2ocean-compact-ato/dd-h2ocean-compact-ato.md), sin añadir sal: la evaporación retira agua, no sal. El llenado inicial del ciclado utilizó agua de mar filtrada con UV de Elite Reef Kanarias. El agua nueva para los cambios posteriores se preparará con RO/DI y [Aquaforest Reef Salt](../../01_verilpedia/05_productos/02_aquaforest-reef-salt/aquaforest-reef-salt.md), según el [procedimiento operativo de cambios de agua](../../03_pendientes/operacion-recurrente/01_cambios-agua.md), para mantener el objetivo de **1,025 de densidad relativa** en Veril.

Para los cálculos de cambios de agua de Veril se toma como base nominal **75 L para el sistema completo** y **60 L para el display**. Se adopta un cambio nominal de **10 L**, aproximadamente el 13,3 % del sistema. La cantidad inicial de sal y la verificación del agua preparada se recogen en el [procedimiento de cambios de agua](../../03_pendientes/operacion-recurrente/01_cambios-agua.md).

Para la salinidad se dispone de un [refractómetro D-D The Aquarium Solution AQPR001](../../01_verilpedia/05_productos/06_dd-aquarium-solution-aqpr001/dd-aquarium-solution-aqpr001.md). Su calibración y el método de medición se registrarán antes de aceptar el agua de mar.

## Referencias químicas para la maduración

Estas referencias sirven para comparar las mediciones de Veril durante la
maduración y preparar las primeras incorporaciones. La ficha distingue
los objetivos adoptados, el criterio práctico del escenario y las bandas
orientativas acordadas como herramienta de comparación. La decisión de
actuar se apoya en la calidad de la medida, su tendencia y la carga presente.

| Parámetro | Valor o rango | Estado | Por qué se usa en Veril |
| --- | --- | --- | --- |
| [Salinidad](../../01_verilpedia/03_parametros/salinidad.md) | **1,025 de densidad relativa** | Objetivo adoptado | Coincide con la referencia de los proveedores del propietario y da un punto común para comparar agua preparada y agua del acuario. Mantener la misma escala y un método calibrado. |
| [Temperatura](../../01_verilpedia/03_parametros/temperatura.md) | Preferida **25–26 °C**. Banda normal **24,5–26,5 °C** | Régimen adoptado | Conserva margen para las oscilaciones habituales y separa la zona preferida de los umbrales de actuación del control térmico. |
| [Alcalinidad (KH)](../../01_verilpedia/03_parametros/alcalinidad.md) | Nominal **≈7 dKH**. Comparación **7–8 dKH** | Nominal del escenario y banda orientativa | El escenario ya toma 7 dKH como referencia. La banda se sitúa en el extremo bajo de los rangos habituales de arrecife y permite seguir el tampón y el consumo sin perseguir una alcalinidad alta. |
| [pH](../../01_verilpedia/03_parametros/ph.md) | **7,8–8,4** | Banda orientativa | Da contexto al equilibrio entre alcalinidad y CO₂. Es suficientemente amplia para interpretar la oscilación diaria. Para comparar tendencias, medir a una hora similar y contrastar con KH. |
| [Amoníaco / TAN](../../01_verilpedia/03_parametros/amonio.md) y [nitrito](../../01_verilpedia/03_parametros/nitrito.md) | **No detectables** con los tests habituales | Referencia de seguimiento tras el ciclado | Tras incorporar roca o aumentar la carga, su aparición puede indicar que la producción de compuestos nitrogenados supera temporalmente su procesamiento. Interpretar según el método y su sensibilidad. El TAN del Salifert de amonio y el NH₃ libre son magnitudes distintas. |
| [Nitrato (NO₃)](../../01_verilpedia/03_parametros/nitrato.md) | **5–25 mg/L** | Banda orientativa local | El extremo bajo deja margen para seguir un nutriente detectable. El alto permite contextualizar lecturas de maduración como los 25 mg/L del 20 de noviembre. Leer la tendencia junto al fosfato y la carga antes de plantear cambios. |
| [Fosfato (PO₄)](../../01_verilpedia/03_parametros/fosfato.md) | **0,03–0,10 mg/L** | Banda orientativa local | Ofrece una ventana de comparación para fosfato bajo y detectable, coherente con el criterio de evitar que ambos nutrientes se mantengan en cero. El [HI736](../../01_verilpedia/05_productos/32_hanna-hi736/hanna-hi736.md) informa ppb de P. Convertir a ppm de PO₄ antes de comparar y confirmar los valores cercanos al extremo bajo con atención a la exactitud del test. |
| [Calcio (Ca)](../../01_verilpedia/03_parametros/calcio.md) | **380–450 mg/L**. Nominal **≈420 mg/L** | Banda y nominal orientativos | Es un intervalo habitual de arrecife. El nominal queda cerca del centro y sirve para comparar el agua y seguir la demanda de los calcificadores junto con KH. |
| [Magnesio (Mg)](../../01_verilpedia/03_parametros/magnesio.md) | **1.250–1.400 mg/L**. Nominal **≈1.300 mg/L** | Banda y nominal orientativos | La referencia próxima a 1.300 permite seguir el equilibrio con Ca y KH, porque el magnesio influye en la precipitación de carbonato cálcico. Comparar también la salinidad antes de interpretar una desviación. |

Los nominales de Ca y Mg sirven como referencias de lectura. El criterio
del [escenario unificado](../03_biologia/03_escenarios/01_escenario-unificado-veril.md#parámetros-y-criterios-de-diseño)
es plantear dosificación de Ca, Mg y K cuando haya consumo medido. Las
bandas de nutrientes son propuestas locales de comparación, sin umbrales
automáticos de corrección. Como referencia general se emplean las
[recomendaciones de química de arrecife de Randy Holmes-Farley](https://www.reef2reef.com/ams/optimal-parameters-for-a-coral-reef-aquarium-by-randy-holmes-farley.79/).
Los métodos, la frecuencia y la interpretación de los tests se detallan
en el [plan de mediciones](../../03_pendientes/operacion-recurrente/02_medicion-y-tests.md).

## Métodos disponibles

También están disponibles para la caracterización y el ciclado el [Salifert Ammonia NH3 Profi Test](../../01_verilpedia/05_productos/12_salifert-ammonia-nh3/salifert-ammonia-nh3.md), presentación de 50 tests y caducidad **10/2027**, el [Salifert NO2 Profi Test](../../01_verilpedia/05_productos/13_salifert-no2/salifert-no2.md), presentación de 50 tests y caducidad **06/2029**, y un [Tetra Test 7 en 1](../../01_verilpedia/05_productos/14_tetra-test-7-en-1/tetra-test-7-en-1.md), presentación de 50 tiras, para pH, KH, GH, NO2, NO3, Cl2 y CO2. Los Salifert de amonio y nitrito serán los métodos principales para seguir el ciclado; las tiras Tetra se utilizarán únicamente como referencia inicial y caracterización orientativa.

## Agua del arranque biológico

El llenado se hizo con agua de mar filtrada con UV de Elite Reef Kanarias. Los recipientes, la corrección sobre el volumen y la recepción del RO6CB se conservan en [Material y estado documentados](01_infraestructura.md#material-y-estado-documentados). La base nominal de cálculo sigue siendo **75 L**; durante el ciclado se contrastó el agua con la referencia `S_P = 35` mediante salinidad, temperatura, pH y alcalinidad.

El ciclado empezó el [12 de octubre](../../04_operaciones/2026/10/2026-10-12.md#incorporación-de-af-bio-sand). La preparación previa tomaba como referencia **24,5–26,5 °C**, preferentemente **25–26 °C**; ahora las cargas, dosis y seguimiento se consultan en el [plan](../../03_pendientes/ciclado/01_plan.md) y su [procedimiento](../../03_pendientes/ciclado/02_runbook.md).

El agua de mar suministrada prepara la matriz salina, pero no inocula bacterias ni sustituye a FritzZyme 9. El agua RO/DI de reposición del ATO tampoco contiene sal y no se utilizará para preparar las cargas de Fishless Fuel.

## Justificación de la salinidad objetivo

El propietario adopta **1,025 de densidad relativa** como objetivo operativo
de Veril porque es el valor de referencia de sus proveedores. La medición de
**1,025** tras el [cambio de agua del 20 de noviembre de 2026](../../04_operaciones/2026/11/2026-11-20.md#cambio-de-agua)
queda registrada como contexto de la decisión.

La referencia `S_P = 35` corresponde al ciclado y se conserva en su historial.
Las tablas del fabricante a 33 y 35 ppt siguen siendo referencias de
composición en sus propias escalas. Véase la [ficha de salinidad](../../01_verilpedia/03_parametros/salinidad.md).

## Estado de la decisión

**Adoptado:** La reposición por evaporación utilizará agua RO/DI mediante el ATO. El llenado inicial del ciclado utilizó agua de mar filtrada con UV suministrada por Elite Reef Kanarias con `S_P = 35` como referencia de esa fase. Una vez finalizado el ciclado, el agua nueva para cambios posteriores se preparará con agua de ósmosis RO/DI y Aquaforest Reef Salt, salvo decisión documentada distinta.

**Previsto:** La química se interpretará mediante parámetros individuales, relaciones entre variables y tendencias temporales, teniendo en cuenta la fase del sistema y la carga existente.

**Pendiente:** Todavía deben quedar fijados en los documentos propietarios los métodos concretos, la frecuencia de medición, los límites de aceptación por fase y cualquier estrategia de dosificación que llegue a adoptarse. Esta ficha no anticipa esas decisiones.

## Relaciones específicas de Veril

La interpretación química deberá relacionarse con:

- La evaporación y el funcionamiento del ATO
- La carga biológica y la alimentación previstas
- La colonización y la maduración de las superficies
- La actividad del skimmer y la retirada de materia
- El consumo de organismos calcificadores si se incorporan
- Los cambios de agua y cualquier dosificación que se autorice
- La temperatura y la salinidad durante la toma de muestras

Una lectura puntual no cerrará por sí sola una decisión. Se registrarán el método, la fecha, la hora, la intervención previa y la tendencia necesaria para interpretar la respuesta del sistema.

La preparación, ejecución y trazabilidad de los cambios de agua pertenecen al [procedimiento operativo correspondiente](../../03_pendientes/operacion-recurrente/01_cambios-agua.md).

## Aplicación durante las fases operativas

El [ciclado](../../03_pendientes/ciclado/01_plan.md) y la [maduración](../../03_pendientes/maduracion/01_plan.md) mantienen sus propios protocolos. Esta ficha solo define qué relación debe conservarse entre la química medida y la configuración de Veril.

Antes de nuevas incorporaciones se comprobará que las tendencias químicas sean interpretables para la carga prevista. Una corrección química no se aplicará únicamente para perseguir una cifra aislada ni sustituirá la identificación de entradas, consumos, procesamiento o mantenimiento.

## Criterios de aceptación

- Las muestras se toman con un método y unas unidades registradas
- Salinidad y temperatura se interpretan conjuntamente con el momento de la medición
- Las tendencias de los parámetros relevantes son conocidas para la fase del sistema
- Las variaciones se relacionan con alimentación, evaporación, cambios de agua, consumo y mantenimiento
- No se utilizan proxies aislados como demostración de estabilidad o madurez
- Los cambios químicos que afecten a la población o al procesamiento quedan registrados

Las fichas de parámetros y los planes de ciclado y maduración conservan el detalle ejecutable y el estado de cada medición.
