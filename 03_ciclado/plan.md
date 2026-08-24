# Plan de ciclado de Veril

## Objetivo y alcance

Veril aplicará la [variante de ciclado sin peces](../01_fichas/06_procesos/01a_ciclado-sin-peces.md) para demostrar una capacidad nitrificante bajo condiciones definidas. La definición del proceso, lo que debe demostrar y sus límites de interpretación están en la [ficha de ciclado biológico](../01_fichas/06_procesos/01_ciclado.md).

La prueba se ejecutará dentro de la arquitectura de procesamiento Berlín adoptada por Veril. El ciclado validará la capacidad nitrificante de las superficies y condiciones del sistema, pero no sustituirá la evaluación posterior de la exportación orgánica, la retirada física ni el mantenimiento propios de esa arquitectura.

El resultado no autoriza por sí solo la introducción de toda la población. La receta elegida y sus exclusiones están documentadas en la [receta combinada Fritz–Aquaforest](decisiones/seleccion-inoculante-y-receta.md).

Las condiciones físicas, hidráulicas, químicas y de procesamiento que el plan necesita se definen en las fichas enlazadas al final. Este documento solo establece cómo deben comprobarse durante la prueba.

La [proyección microbiológica del ciclado](proyeccion-microbiologica.md) describe los grupos que podrían establecerse y sus límites de interpretación. No constituye un criterio adicional de cierre.

## Condiciones de partida

La prueba se realizará con:

- Roca inerte, AF Bio Sand y las superficies que vayan a permanecer instaladas
- Agua osmotizada de RO/DI preparada con **Aquaforest Reef Salt**
- Retorno, circulación y agitación superficial activos
- Sin animales, equipo de limpieza ni materia orgánica en descomposición
- Sin productos biológicos adicionales a los definidos en la receta

El volumen geométrico de la urna no se utilizará para dosificar. Todas las cargas se calcularán sobre el volumen operativo real.

Para preparar el runbook se utilizará provisionalmente un volumen de planificación de **75 L**, porque es la escala operativa adoptada para Veril. El volumen geométrico bruto estimado de la urna es aproximadamente 96 L. Este segundo valor se conserva como referencia geométrica de control, pero tampoco se utilizará como volumen final de dosificación. Antes de dosificar se medirá el volumen operativo real y se recalcularán todas las cantidades.

### Dosis de referencia y cálculo

Las siguientes cantidades son referencias para 75 L y 96 L. Ninguna sustituye la medición del volumen operativo ni la verificación analítica:

| Elemento | Cálculo | Referencia para 75 L | Referencia para 96 L |
| --- | --- | ---: | ---: |
| FritzZyme TurboStart 900 | `V_operativo × 29 mL / 95 L` | 22,9 mL | 29,3 mL |
| Primera carga de Fishless Fuel, objetivo 2,0 mg/L como N | `V_operativo × 2,0 mg/L ÷ 40 mg/mL` | 3,75 mL | 4,80 mL |
| Segunda carga de Fishless Fuel, objetivo 1,0 mg/L como N | `V_operativo × 1,0 mg/L ÷ 40 mg/mL` | 1,88 mL | 2,40 mL |
| Aquaforest Reef Salt | Referencia del fabricante: 39 g/L para aproximadamente 33 ppt | 2.925 g | 3.744 g |

La cantidad de Reef Salt no se convertirá linealmente en una dosis fija para `S_P = 35`. Los 2.925 g y 3.744 g son referencias iniciales a aproximadamente 39 g/L para 33 ppt, no cantidades finales garantizadas. Se preparará el agua y se ajustará mediante medición. La activación de AF Bio Sand utilizará los **3 L de agua salada durante 24 horas** indicados por su ficha, sin recalcular ese volumen salvo que la etiqueta de la presentación adquirida disponga otra cosa.

Cuando se conozca el volumen operativo real, se sustituirá `V_operativo` en las fórmulas y se redondeará la dosis a una cantidad que pueda medirse con el material disponible. El redondeo se registrará y no se corregirá añadiendo producto sin volver a calcular.

El TurboStart se dosificará según la concentración de la ficha vigente y el volumen operativo medido. Fishless Fuel se calculará con la concentración declarada de 40 mg/mL como TAN y se verificará con el test seleccionado. Si la etiqueta, el lote o el método analítico difieren, prevalecerán esos datos y se registrará el recálculo.

## Criterios de medición

Veril aplicará los criterios de medición de las fichas generales de ciclado, amonio, nitrito, pH, alcalinidad, salinidad y temperatura. Antes de iniciar se registrarán los tests seleccionados, sus escalas, procedimientos y límites de aceptación.

Para esta prueba, las cargas se expresarán como **mg/L como N** y se conservará también la lectura en la unidad nativa del test. Cualquier conversión entre NH₃, NH₄⁺, TAN o NH₃-N se documentará antes de iniciar.

El límite local de aceptación será el valor mínimo que el método seleccionado permita distinguir con fiabilidad del cero operativo. El plazo de cada carga será el definido en este plan y no se modificará durante la prueba.

El nitrato se registrará como apoyo interpretativo. El pH y la alcalinidad se utilizarán como controles de estabilidad.

## Preparación

1. Comprobar que la urna, el rebosadero, el retorno y las cámaras funcionan sin fugas ni niveles inseguros
2. Colocar la roca con apoyos estables y superficies accesibles al flujo
3. Preparar el agua osmotizada con Aquaforest Reef Salt según la ficha del producto y registrar salinidad, temperatura, pH y alcalinidad
4. Preparar e instalar el AF Bio Sand según la documentación del producto
5. Medir el volumen operativo real y registrar el método de cálculo y su incertidumbre
6. Activar retorno, circulación y agitación superficial
7. Mantener una línea base de observación de 24–48 horas
8. Registrar proveedor, presentación, lote, fecha, conservación y aspecto de los productos

La línea base incluirá temperatura, salinidad, pH, alcalinidad, nitrógeno amoniacal y nitrito, y, como apoyo, nitrato y fosfato. Se conservará también la lectura en la unidad nativa de cada test.

La prueba no comenzará si existen fugas, niveles inseguros, circulación insuficiente, mala oxigenación o materia orgánica en descomposición.

## Protocolo de mantenimiento durante el ciclado

Durante la prueba se mantendrá una rutina mínima y estable para no introducir variables que dificulten la interpretación:

- Revisar urna, rebosadero, retorno, nivel de la cámara de retorno, circulación y agitación superficial
- Reponer la evaporación normalmente mediante el ATO seleccionado y únicamente con agua osmotizada de RO/DI; la reposición manual quedará limitada a una contingencia registrada
- Comprobar salinidad y temperatura y registrar cualquier corrección
- Retirar detritos solo si obstruyen el flujo, el rebosadero o algún equipo, anotando la intervención
- Limpiar una entrada, rejilla o rotor únicamente si la acumulación reduce el funcionamiento
- Mantener las superficies biológicas y el sustrato sin limpiezas rutinarias que alteren la prueba
- No añadir alimentos, bacterias adicionales a la receta, medios filtrantes, carbono, resinas ni correctores por una lectura aislada
- No realizar cambios de agua durante la carga activa salvo que exista una condición roja o un riesgo para el sistema

Las muestras se tomarán siempre con el mismo método y se registrarán fecha, hora, parámetros, mantenimiento realizado y cualquier incidencia. El agua de reposición por evaporación no llevará sal.

Si una condición roja obliga a realizar un cambio de agua durante la prueba, se registrarán el volumen retirado, el volumen repuesto, la salinidad antes y después y la causa. La carga en curso se considerará potencialmente alterada y no se utilizará como confirmación sin recalcular la concentración o repetirla.

## Cargas y condiciones específicas de Veril

La ejecución detallada está en el [runbook de ciclado](runbook.md). El plan fija las siguientes condiciones propias de Veril:

- TurboStart 900 y Fishless Fuel se añadirán según las dosis recalculadas para el volumen operativo real
- Fishless Fuel se añadirá en la misma sesión que TurboStart o dentro de las 24 horas siguientes
- La primera carga será de 2,0 mg/L como N y la segunda de 1,0 mg/L como N, después de confirmar la primera
- El skimmer permanecerá apagado durante los cinco primeros días posteriores a TurboStart, salvo intervención registrada por seguridad
- No se redosificará mientras amonio o nitrito permanezcan por encima del límite de aceptación
- No se añadirán alimentos, otros cultivos, carbono, carbón activo, resinas ni correctores para compensar una lectura aislada

## Seguimiento

| Momento | Registro mínimo |
| --- | --- |
| Línea base | Nitrógeno amoniacal, nitrito, pH, alcalinidad, salinidad y temperatura |
| Primera carga | Producto, lote, concentración, cálculo, fecha y hora |
| Primeras 24 horas | Nitrógeno amoniacal, nitrito, pH y temperatura |
| Evolución | Nitrógeno amoniacal y nitrito con la frecuencia necesaria para seguir la tendencia; pH, alcalinidad, salinidad y temperatura como controles |
| Segunda carga | Nueva carga objetivo de 1,0 mg/L como N (±10 %) cuando la primera se haya procesado |
| Confirmación | Nitrógeno amoniacal y nitrito hasta alcanzar el límite de aceptación dentro del plazo fijado |

La primera carga tendrá un plazo operativo máximo de **5 días desde su adición** y la segunda carga tendrá el mismo plazo máximo desde su propia adición. Estos plazos son criterios de aceptación de Veril, no una garantía de resultado del fabricante. Si no se cumplen, no se declarará cerrado el ciclado: se mantendrá el sistema sin animales, se investigará la causa y se documentará cualquier repetición como una nueva prueba o una desviación.

La segunda carga se añadirá solo después de que la primera haya alcanzado el límite de aceptación de amonio y nitrito y haya mantenido ese estado durante 24 horas sin una intervención que altere la prueba. La confirmación de la segunda carga se seguirá hasta el mismo límite.

## Criterio de cierre

Además de los criterios generales de la ficha de ciclado, Veril cerrará esta prueba únicamente cuando:

- La primera carga de 2,0 mg/L como N se haya procesado dentro del plazo fijado
- Una segunda carga independiente de 1,0 mg/L como N (±10 %) también vuelva al límite de aceptación
- pH y alcalinidad no presenten un deterioro que invalide la interpretación
- Salinidad, temperatura, circulación y oxigenación permanezcan estables
- No haya animales ni materia orgánica en descomposición

La aparición de nitrato apoyará la interpretación, pero no sustituirá las mediciones de amonio y nitrito.

## Puertas de decisión

Se aplicarán las puertas de decisión generales de la [ficha de ciclado sin peces](../01_fichas/06_procesos/01a_ciclado-sin-peces.md), con estos criterios operativos para Veril:

### Roja — detener

Se detiene la progresión si falla la circulación, la oxigenación es insuficiente, aparece descomposición, se pierde un nivel seguro o pH y alcalinidad se deterioran de forma sostenida.

Se mantiene el sistema sin redosificar, se identifica la causa y se aplica solo la intervención necesaria.

### Amarilla — mantener

Se mantiene la pauta si una lectura no puede interpretarse con seguridad o una intervención menor altera la comparabilidad.

Se repiten las mediciones con el mismo método y no se añaden nuevas variables.

### Verde — cerrar

Se cierra la prueba cuando las dos cargas cumplen los criterios locales, las condiciones físicas son estables y no existen riesgos operativos.

Después se pasa al [plan de maduración](../04_maduracion/plan.md), no a la introducción inmediata de toda la población.

## Errores que invalidan la interpretación

Además de los límites generales de interpretación descritos en las fichas de proceso, esta prueba de Veril quedará invalidada o deberá repetirse si ocurre lo siguiente:

- Cambiar de inoculante a mitad de la prueba
- Añadir alimentos u otros productos nitrogenados
- Redosificar antes de procesar la carga anterior
- Utilizar el volumen geométrico en lugar del volumen operativo
- Apagar retorno, circulación o agitación superficial
- Reactivar o apagar el skimmer sin registrar la intervención y su motivo
- Interpretar agua clara, ausencia de olor o nitrato aislado como prueba completa
- Introducir animales durante el ensayo

## Fuentes

- [Variante general de ciclado sin peces](../01_fichas/06_procesos/01a_ciclado-sin-peces.md)
- [Receta combinada Fritz–Aquaforest](decisiones/seleccion-inoculante-y-receta.md)
- [Ficha de AF Bio Sand](../01_fichas/05_productos/af-bio-sand.md)
- [Ficha de TurboStart 900](../01_fichas/05_productos/fritzzyme-turbostart-900.md)
- [Ficha de Fishless Fuel](../01_fichas/05_productos/fritz-fishless-fuel.md)
- [Ficha de Aquaforest Reef Salt](../01_fichas/05_productos/aquaforest-reef-salt.md)
- [Procedimiento operativo de cambios de agua](../05_operacion/cambios-agua.md)
- [Runbook de ciclado sin peces](runbook.md)

## Condiciones definidas en otras fichas de Veril

- [Infraestructura](../02_veril/01_infraestructura.md)
- [Hidráulica](../02_veril/03_hidraulica.md)
- [Procesamiento](../02_veril/07_procesamiento.md)
- [Química](../02_veril/05_quimica.md)
- [Amonio](../01_fichas/03_parametros/amonio.md)
- [Nitrito](../01_fichas/03_parametros/nitrito.md)
- [Nitrato](../01_fichas/03_parametros/nitrato.md)
- [Oxígeno](../01_fichas/03_parametros/oxigeno.md)
- [pH](../01_fichas/03_parametros/ph.md)
- [Alcalinidad](../01_fichas/03_parametros/alcalinidad.md)
- [Salinidad](../01_fichas/03_parametros/salinidad.md)
- [Temperatura](../01_fichas/03_parametros/temperatura.md)
