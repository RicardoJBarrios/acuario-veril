# Cambios de agua en un acuario marino

## Qué es

Un cambio de agua sustituye una fracción del agua del sistema por agua nueva de composición conocida o caracterizada. No es únicamente una técnica para reducir nitrato o materia disuelta: modifica simultáneamente las concentraciones, las relaciones iónicas, la carga de contaminantes y la disponibilidad de algunos componentes del agua.

La calidad de un cambio depende tanto del agua nueva como de la fracción sustituida, la homogeneización, la compatibilidad con el sistema y la capacidad de comprobar el resultado.

## Qué puede aportar

Un cambio de agua puede:

- Reducir por dilución la concentración de sustancias disueltas
- Reponer parte de componentes consumidos o retirados
- Modificar las relaciones entre parámetros cuando el agua nueva tiene una composición diferente
- Retirar una fracción de materia disuelta y partículas que se encuentren en el agua extraída
- Permitir comparar la composición del agua del sistema con la composición del agua preparada

El efecto real depende del volumen cambiado y de la composición del agua nueva. Un cambio pequeño produce una modificación limitada, mientras que uno grande puede alterar de forma apreciable la salinidad, la temperatura y la química del sistema.

## Qué no resuelve por sí solo

Un cambio de agua no elimina necesariamente la fuente de un compuesto, no demuestra que el procesamiento del sistema sea suficiente y no sustituye la identificación de consumos, producción, precipitación, adsorción o dosificación anómalos.

Tampoco garantiza que todos los parámetros estén en condiciones adecuadas. El agua nueva puede tener una salinidad correcta y, aun así, presentar diferencias relevantes de alcalinidad, calcio, magnesio, nutrientes u otras magnitudes.

La reducción observada después de un cambio no debe interpretarse automáticamente como solución permanente. Debe distinguirse entre dilución temporal, retirada efectiva y desaparición de la fuente.

## Balance simple de mezcla

Para una sustancia cuya concentración pueda tratarse aproximadamente como conservativa durante la operación, si se sustituye una fracción `f` del volumen operativo por el mismo volumen de agua nueva y no existen otros procesos relevantes durante la mezcla, puede estimarse:

```text
f = V_cambio / V_operativo
C_final ≈ (1 − f) × C_acuario + f × C_agua_nueva
```

Donde `V_cambio` es el volumen realmente sustituido y `V_operativo` es el volumen funcional del sistema. El volumen operativo no debe confundirse automáticamente con el volumen geométrico nominal de la urna.

Esta relación sirve como comprobación de plausibilidad, no como predicción exacta. No incorpora errores de volumen, muestreo o mezcla incompleta.

No debe aplicarse directamente a magnitudes no lineales o gobernadas por equilibrios que se reajustan durante la mezcla, como el pH. Tampoco debe aplicarse sin reservas a sustancias sometidas a intercambio gaseoso, precipitación, adsorción, consumo o producción significativa, como puede ocurrir con oxígeno, dióxido de carbono, nutrientes reactivos o especies químicas concretas.

## Preparación y aceptación del agua nueva

El agua nueva debe prepararse con una fuente compatible y una composición conocida o verificable. La masa de sal, el volumen de agua de partida y las instrucciones del producto pueden servir como punto de partida, pero la salinidad final debe medirse antes del uso.

Los criterios de aceptación deben distinguir entre:

- Salinidad, temperatura y otras magnitudes medidas
- Claridad o estado visual de la mezcla
- Trazabilidad del agua de partida y del producto
- Compatibilidad con el sistema que recibirá el agua

La sal seca no debe añadirse directamente a un acuario con animales. Si es necesario corregir la salinidad del agua preparada, se debe utilizar agua sin sal o una preparación salina de concentración conocida, homogeneizar y volver a medir.

El agua preparada que no se utilice inmediatamente debe conservarse de forma que se limite la evaporación y debe volver a comprobarse antes de incorporarla al sistema.

## Ejecución y seguridad

Antes de retirar agua deben considerarse el nivel operativo, la circulación, los equipos que puedan aspirar aire o funcionar en seco y cualquier sistema automático que pueda interpretar la bajada de nivel como evaporación.

La reposición debe devolver el sistema a un estado operativo estable antes de reactivar automatismos o equipos que dependan del nivel. La temperatura y la salinidad del agua nueva deben ser compatibles con el sistema, y las diferencias admisibles deben definirse según la configuración concreta.

## Interpretación posterior

Cuando existan mediciones anteriores, del agua nueva y posteriores, debe comprobarse que la magnitud y la dirección del cambio sean plausibles para la fracción sustituida. Una discrepancia significativa puede deberse a un error de medición, volumen, mezcla, muestreo o proceso concurrente antes que al producto.

La interpretación debe separar:

- El efecto de dilución o sustitución
- La composición real del agua nueva
- El consumo, la producción o la precipitación durante el intervalo
- La retirada de partículas o materia asociada al agua extraída
- Los cambios de temperatura, salinidad y circulación que afecten a la medición

La medición posterior debe realizarse cuando el sistema haya recuperado una mezcla suficientemente representativa para el objetivo de la comprobación. El momento y los parámetros concretos pertenecen al procedimiento del sistema que realiza el cambio.

## Relación con otros procesos

Los cambios de agua interactúan con:

- La química, porque modifican concentraciones y relaciones entre parámetros
- El procesamiento y la exportación, porque pueden retirar materia sin eliminar su fuente
- La hidráulica, porque la mezcla y la renovación condicionan la homogeneidad de la muestra
- La biología, porque los organismos responden a cambios de salinidad, temperatura y composición
- El mantenimiento, porque la ejecución puede retirar sedimentos y materia particulada

Estas relaciones no convierten el cambio de agua en un sustituto de las dimensiones o procesos correspondientes. Cada uno debe evaluarse mediante su documentación propia.

## Indicadores que pueden inducir a error

- Asumir que una masa fija de sal produce siempre la misma salinidad
- Utilizar el volumen nominal de la urna en lugar del volumen operativo
- Considerar que una reducción temporal de nitrato elimina su fuente
- Aplicar un balance lineal a pH o a especies químicas en equilibrio
- Medir el agua nueva sin registrar temperatura, instrumento o calibración
- Reactivar un ATO durante la retirada y alterar el volumen realmente sustituido
- Atribuir cualquier cambio posterior al producto sin comparar el agua nueva y las intervenciones concurrentes

## Fuentes y límites

Esta ficha define el proceso de forma general. No establece una frecuencia universal, un porcentaje de cambio, una sal concreta ni límites válidos para cualquier sistema. Esos valores deben documentarse en el procedimiento operativo correspondiente y justificarse mediante las características del sistema, la composición del agua nueva y las mediciones disponibles.

La ecuación de mezcla es un modelo simplificado. La respuesta real puede incluir procesos biológicos, químicos, físicos y de medición que no estén representados en ella.

## Documentos relacionados

- El procedimiento operativo correspondiente: aplicación específica del sistema que realiza el cambio
- [Fichas de parámetros](../03_parametros/README.md): interpretación de las magnitudes medidas
- [Dimensión química](../01_dimensiones/05_quimica.md): relaciones y estabilidad de la composición del agua
- [Dimensión hidráulica](../01_dimensiones/03_hidraulica.md): mezcla, renovación y distribución del agua
