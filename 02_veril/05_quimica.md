# Veril: química

> La [dimensión química](../01_fichas/01_dimensiones/05_quimica.md) define cómo interpretar composición, relaciones, tendencias y estabilidad. Esta ficha registra la aplicación prevista en Veril sin repetir las fichas generales de parámetros.

## Aplicación adoptada

La química de Veril se seguirá mediante las [fichas de parámetros](../01_fichas/03_parametros/README.md), con atención a la relación entre salinidad, temperatura, pH, alcalinidad, compuestos nitrogenados, nitrato, fosfato y oxígeno cuando corresponda a la fase del sistema.

La configuración integrada adopta una temperatura objetivo del agua de **25,0 °C**. La justificación y las consecuencias distribuidas entre las dimensiones se documentan en [Régimen térmico adoptado](00_configuracion.md#régimen-térmico-adoptado); esta ficha conserva la interpretación de la temperatura como variable química y contexto de medición.

El agua de reposición por evaporación será agua RO/DI mediante el [ATO seleccionado](../01_fichas/04_hardware/dd-h2ocean-compact-ato/dd-h2ocean-compact-ato.md), sin añadir sal: la evaporación retira agua, no sal. El agua nueva para la preparación inicial y los cambios de agua se preparará con RO/DI y [Aquaforest Reef Salt](../01_fichas/05_productos/aquaforest-reef-salt.md), según el [procedimiento operativo de cambios de agua](../05_operacion/cambios-agua.md), hasta alcanzar una salinidad objetivo de `S_P = 35`.

No se fija en esta ficha una tabla independiente de valores objetivo. Los rangos, métodos, unidades, frecuencia y límites de interpretación pertenecen a las fichas de parámetros y a los planes operativos que los utilicen.

## Justificación de la salinidad objetivo

Veril adopta una salinidad práctica objetivo de **`S_P = 35`**. Esta decisión no presenta 35 como una salinidad universalmente obligatoria, sino como el punto de consigna elegido para esta configuración.

La decisión se fundamenta en varios criterios convergentes, documentados en la [ficha general de salinidad](../01_fichas/03_parametros/salinidad.md) y en la [ficha de Aquaforest Reef Salt](../01_fichas/05_productos/aquaforest-reef-salt.md):

- `S_P = 35` se aproxima a la referencia habitual de salinidad del océano abierto y ofrece un punto de comparación claro con la química marina
- La configuración prevista es un arrecife mixto, no un sistema fish-only ni un sistema deliberadamente hiposalino
- Aquaforest considera aproximadamente 33–35 ppt un intervalo adecuado para acuarios marinos y recomienda alrededor de 35 ppt para acuarios de arrecife
- Aquaforest publica expresamente la composición esperable de Reef Salt a 35 ppt, por lo que el objetivo está contemplado por el fabricante y no requiere extrapolar la formulación fuera de sus referencias publicadas
- Trabajar con una consigna única facilita interpretar conjuntamente salinidad, calcio, magnesio, alcalinidad y otras mediciones relacionadas

Los valores de 33 o 34 ppt también serían biológicamente plausibles y operativamente utilizables. No se adopta 35 porque sea un valor mágico, sino porque no existe en Veril una razón específica para trabajar deliberadamente por debajo de esa referencia y sí existe una ventaja documental y metrológica en utilizarla.

La estabilidad tiene prioridad sobre la persecución de una cifra aislada. Una desviación moderada y estable no se corregirá de forma brusca, y cualquier cambio de consigna deberá tratarse como una decisión operativa explícita.

La masa de sal no define por sí sola el resultado. Aquaforest publica aproximadamente 390 g por 10 L como referencia de preparación a 33 ppt, pero también caracteriza Reef Salt a 35 ppt. En Veril, la cantidad inicial se utilizará únicamente como punto de partida y la aceptación se realizará mediante medición de la salinidad preparada, no mediante una equivalencia fija entre gramos y `S_P`.

## Estado de la decisión

**Adoptado:** La reposición por evaporación utilizará agua RO/DI mediante el ATO. El agua nueva para preparación inicial y cambios utilizará RO/DI con Aquaforest Reef Salt y se ajustará y comprobará hasta `S_P = 35`.

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

La preparación, ejecución y trazabilidad de los cambios de agua pertenecen al [procedimiento operativo correspondiente](../05_operacion/cambios-agua.md).

## Aplicación durante las fases operativas

El [ciclado](../03_ciclado/plan.md) y la [maduración](../04_maduracion/plan.md) mantienen sus propios protocolos. Esta ficha solo define qué relación debe conservarse entre la química medida y la configuración de Veril.

Antes de nuevas incorporaciones se comprobará que las tendencias químicas sean interpretables para la carga prevista. Una corrección química no se aplicará únicamente para perseguir una cifra aislada ni sustituirá la identificación de entradas, consumos, procesamiento o mantenimiento.

## Criterios de aceptación

- Las muestras se toman con un método y unas unidades registradas
- Salinidad y temperatura se interpretan conjuntamente con el momento de la medición
- Las tendencias de los parámetros relevantes son conocidas para la fase del sistema
- Las variaciones se relacionan con alimentación, evaporación, cambios de agua, consumo y mantenimiento
- No se utilizan proxies aislados como demostración de estabilidad o madurez
- Los cambios químicos que afecten a la población o al procesamiento quedan registrados

Las fichas de parámetros y los planes de ciclado y maduración conservan el detalle ejecutable y el estado de cada medición.
