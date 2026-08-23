# Cambios de agua de Veril

## Propósito

Este documento define el procedimiento específico de Veril para preparar, comprobar, registrar y utilizar el agua de cambio. La explicación general de qué es un cambio de agua, qué puede aportar y cuáles son sus límites pertenece a la [ficha general de cambios de agua](../fichas/procesos/cambios-agua.md).

La composición declarada y los límites del producto pertenecen a la [ficha de Aquaforest Reef Salt](../fichas/productos/aquaforest-reef-salt.md). La interpretación de cada parámetro pertenece a las [fichas de parámetros](../fichas/parametros/README.md). Este documento concreta cómo se utilizará esa información en Veril, sin duplicar sus definiciones generales.

## Decisiones adoptadas

- Preparar el agua nueva con agua RO/DI y [Aquaforest Reef Salt](../fichas/productos/aquaforest-reef-salt.md)
- Preparar el agua nueva para una salinidad objetivo de `S_P = 35`
- Utilizar exclusivamente agua RO/DI sin sal para reponer la evaporación mediante el [ATO seleccionado](../fichas/hardware/dd-h2ocean-compact-ato/dd-h2ocean-compact-ato.md)
- Medir y verificar la salinidad, la temperatura y el estado visual del agua nueva antes de incorporarla al sistema
- Registrar el lote de sal, la preparación y las mediciones asociadas a cada cambio
- No utilizar un cambio de agua como sustituto de identificar una fuente, un consumo anómalo, una precipitación o un problema de procesamiento

## Decisiones pendientes

- Volumen operativo de cada cambio
- Frecuencia o condición que desencadenará un cambio
- Parámetros que se medirán siempre en el agua preparada
- Momento y parámetros de la medición posterior en el acuario
- Límites que obligarán a aplazar, repetir o modificar una preparación
- Diferencia máxima admisible de temperatura y salinidad entre el agua nueva y Veril
- Criterio de preparación del agua nueva cuando la salinidad real de Veril difiera del objetivo `S_P = 35`
- Criterio operativo de aceptación del agua RO/DI
- Volumen operativo de referencia para calcular la fracción `f`

Hasta que esas decisiones se documenten, no se fija aquí un porcentaje, volumen o calendario universal. La salinidad objetivo sí queda fijada en `S_P = 35`.

## Preparación del agua nueva

La preparación seguirá la [ficha del producto](../fichas/productos/aquaforest-reef-salt.md) y conservará la trazabilidad de la mezcla:

1. Identificar el lote de Aquaforest Reef Salt y comprobar el estado seco del producto
2. Medir el volumen real de agua RO/DI utilizado
3. Llevar el agua de partida aproximadamente a **24 °C**, como referencia de preparación del fabricante, y registrar su temperatura
4. Registrar la masa de sal añadida
5. Utilizar la referencia publicada de 390 g por 10 L para 33 ppt como punto de partida orientativo, no como receta final
6. Una vez exista un historial suficiente de un mismo lote, utilizar como referencia inicial la masa específica obtenida en preparaciones anteriores, manteniendo siempre la medición final de salinidad como criterio de aceptación
7. Considerar la referencia de composición publicada por Aquaforest para Reef Salt a 35 ppt al evaluar el agua preparada
8. Añadir la sal al agua y mezclar con una bomba o movimiento suficiente
9. Mantener la mezcla durante al menos **15 minutos**, que es el tiempo de disolución publicado por Aquaforest
10. Comprobar que el agua esté clara y medir la salinidad con un instrumento calibrado para agua marina
11. Ajustar de forma controlada con agua RO/DI o con sal previamente disuelta hasta alcanzar `S_P = 35`
12. Igualar la temperatura con el acuario antes del uso. Si por razones operativas el agua debe mantenerse preparada durante más tiempo, conservarla según las instrucciones de almacenamiento del fabricante y aplicar únicamente la circulación o aireación que el procedimiento correspondiente justifique
13. Medir los parámetros adicionales definidos para esa fase o tipo de cambio
14. Registrar cualquier ajuste realizado antes de utilizar el agua

La referencia de masa publicada para 33 ppt no se convertirá automáticamente mediante una regla lineal en una cantidad objetivo para 35 ppt. La humedad, la composición del lote, el volumen real, la temperatura y el instrumento pueden modificar el resultado. La salinidad medida prevalece siempre sobre cualquier cálculo inicial.

Los 15 minutos representan el tiempo mínimo de mezcla y disolución indicado para el producto, no una garantía de que el agua esté lista sin medición. No se incorporará el agua hasta comprobar la salinidad, la temperatura y la claridad de la mezcla. La preparación química y el acondicionamiento térmico son operaciones distintas: los aproximadamente 24 °C corresponden a la referencia de preparación del producto, mientras que antes del uso se debe alcanzar la diferencia de temperatura que se establezca como admisible para Veril.

Aquaforest indica que el agua preparada debe utilizarse dentro de los tres días posteriores a la disolución. Si no se utiliza inmediatamente, se almacenará en un recipiente limpio y cerrado para limitar la evaporación. Antes del uso se comprobarán, como mínimo, la salinidad, la temperatura y el estado visual de la mezcla.

Si la salinidad es demasiado alta, se corregirá con RO/DI. Si es demasiado baja, se corregirá añadiendo progresivamente una preparación salina de concentración conocida preparada por separado, evitando incorporar sal seca directamente al agua ya destinada al cambio. Esto reduce el riesgo de disolución incompleta y de concentraciones locales elevadas. Después de cada ajuste se homogeneizará completamente y se volverá a medir.

No se corregirá una preparación basándose únicamente en gramos por litro, gravedad específica nominal o apariencia del agua.

## Parámetros del agua preparada

Como mínimo, cada preparación deberá conservar:

- Salinidad y unidad o escala utilizada
- Temperatura de la muestra
- Método, instrumento y calibración
- Lote de la sal
- Estado o criterio de aceptación del agua RO/DI
- Volumen inicial de agua RO/DI
- Volumen final de agua preparada disponible
- Masa de sal utilizada

Cuando forme parte del control del sistema RO/DI, se conservará también la conductividad o el TDS de salida correspondiente. La frecuencia, el método y los límites pertenecen a la documentación específica del sistema RO/DI.

Cuando el cambio pueda afectar a la interpretación química del sistema, se registrarán también los parámetros relevantes de la [química de Veril](../veril/quimica.md), especialmente alcalinidad, calcio y magnesio. El pH, el oxígeno, los nutrientes u otros parámetros se incorporarán cuando el motivo del cambio o la fase del sistema lo requieran.

La medición del agua nueva permite conocer su composición observada, pero no demuestra por sí sola la composición completa de la sal ni sustituye un análisis de laboratorio o de lote.

Los criterios de aceptación de cada preparación serán, como mínimo, la salinidad, la temperatura, la claridad de la mezcla y la trazabilidad del agua de partida. La alcalinidad, el calcio, el magnesio y otros parámetros se utilizarán para caracterización periódica, comprobación de un lote nuevo o investigación de un resultado inesperado, sin convertirlos automáticamente en controles obligatorios de cada preparación.

## Ejecución del cambio

Antes de retirar agua se registrarán:

- Fecha y hora
- Volumen previsto y volumen realmente retirado
- Salinidad y temperatura del acuario
- Parámetros que motiven o condicionen el cambio
- Alimentación, dosificación, mantenimiento o incidencias recientes

Antes de iniciar la retirada:

- Desactivar temporalmente el [ATO seleccionado](../fichas/hardware/dd-h2ocean-compact-ato/dd-h2ocean-compact-ato.md) para que no interprete el descenso de nivel como evaporación
- Detener los equipos que puedan aspirar aire, funcionar en seco o quedar fuera de su nivel operativo
- Mantener o detener la circulación interna según el procedimiento del cambio y las condiciones de seguridad de cada equipo

Durante la operación:

- Retirar el volumen previsto evitando mezclarlo de nuevo con el agua de reposición
- Incorporar el agua nueva de forma controlada y compatible con la circulación del sistema
- Evitar introducir agua con una diferencia no evaluada de temperatura o salinidad
- Registrar cualquier interrupción, derrame, salpicadura o cambio respecto al volumen previsto

Después de incorporar el volumen previsto:

- Restablecer el nivel operativo normal del sistema
- Reiniciar los equipos detenidos y comprobar que el retorno y las demás bombas funcionen correctamente, sin aspirar aire ni operar fuera de sus condiciones previstas
- Reactivar el ATO únicamente cuando el volumen salado ya haya sido restituido y el nivel de la cámara de retorno sea estable
- Confirmar finalmente que los niveles de las cámaras han recuperado su estado operativo

No se añadirá sal seca directamente al acuario con animales. La salinidad del sistema no se corregirá mediante una estimación visual del nivel o una compensación improvisada del volumen retirado.

## Comprobación posterior

Después de que el sistema haya recuperado una mezcla representativa, se comprobarán los parámetros definidos para el tipo de cambio. El momento exacto de esta comprobación deberá quedar fijado en el procedimiento operativo cuando se establezcan los criterios de seguimiento.

La comparación deberá distinguir entre:

- El efecto de dilución o sustitución producido por el volumen cambiado
- La composición del agua nueva
- El consumo, la precipitación o la producción ocurridos durante el intervalo
- Los cambios de temperatura, salinidad o circulación que alteren la medición

Una modificación observada después del cambio no se atribuirá automáticamente a la sal sin comparar el agua nueva, el agua del sistema y las intervenciones concurrentes.

Cuando existan mediciones anteriores, del agua nueva y posteriores, se comprobará que la magnitud y la dirección del cambio sean plausibles para la fracción sustituida. Una discrepancia significativa se considerará primero como posible error de medición, volumen, mezcla o proceso concurrente antes de atribuirla al producto.

## Registro de cada cambio

| Campo | Registro |
| --- | --- |
| Fecha y hora | Pendiente de completar |
| Motivo o condición desencadenante | Pendiente de completar |
| Lote de Aquaforest Reef Salt | Pendiente de completar |
| Estado y criterio del agua RO/DI | Pendiente de completar |
| Conductividad o TDS de salida del RO/DI, si se mide | Pendiente de completar |
| Volumen inicial de RO/DI | Pendiente de completar |
| Volumen final de agua preparada disponible | Pendiente de completar |
| Masa de sal | Pendiente de completar |
| Temperatura del agua preparada | Pendiente de completar |
| Salinidad del agua preparada | Pendiente de completar |
| Método e instrumento | Pendiente de completar |
| Alcalinidad, calcio y magnesio del agua preparada, si procede | Pendiente de completar |
| Volumen retirado | Pendiente de completar |
| Volumen realmente introducido en Veril | Pendiente de completar |
| Volumen operativo utilizado para el cálculo, si procede | Pendiente de completar |
| Salinidad y temperatura del acuario antes y después | Pendiente de completar |
| Parámetros adicionales | Pendiente de completar |
| Incidencias o ajustes | Pendiente de completar |

## Límites de interpretación

- La composición nominal del producto no equivale a la composición medida de cada preparación o lote
- El agua de reposición por evaporación no debe contener sal añadida
- Los cambios de agua realizados durante ciclado o maduración deben registrarse en el plan correspondiente porque pueden alterar la interpretación de una prueba o tendencia

La interpretación general de la dilución, la sustitución y sus límites se conserva en la [ficha general de cambios de agua](../fichas/procesos/cambios-agua.md).

## Fuentes y documentos relacionados

- [Cambios de agua en un acuario marino](../fichas/procesos/cambios-agua.md): definición general, efectos, límites y balance simplificado de mezcla
- [Aquaforest Reef Salt](../fichas/productos/aquaforest-reef-salt.md): composición declarada, preparación, conservación y análisis por lote
- [Química de Veril](../veril/quimica.md): decisión de utilizar RO/DI y Aquaforest Reef Salt
- [Fichas de parámetros](../fichas/parametros/README.md): interpretación de salinidad, temperatura, alcalinidad, calcio, magnesio y demás variables
- [Plan de ciclado](../ciclado/plan.md): cambios de agua durante el establecimiento y sus efectos sobre la prueba
- [Plan de maduración](../maduracion/plan.md): cambios de agua durante la evolución inicial del sistema
