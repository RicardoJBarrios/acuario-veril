# Runbook de ciclado sin peces de Veril

## Propósito

Este runbook ejecuta el [plan de ciclado](plan.md) con la receta adoptada para Veril. Convierte el plan en una secuencia reproducible de preparación, dosificación, medición, decisión y registro.

> [!CAUTION]
> No introducir peces, corales, invertebrados ni equipo de limpieza durante esta prueba. Fritz Fishless Fuel no debe utilizarse con animales.

## Valores fijados

| Variable | Valor o criterio |
| --- | --- |
| Volumen de planificación | 75 L, provisional |
| Volumen geométrico estimado | Aproximadamente 96 L; referencia de control, no volumen final de dosificación |
| Temperatura del sistema | 25,0 °C como objetivo operativo |
| Salinidad | `S_P = 35`, verificada por medición |
| Primera carga | 2,0 mg/L como N |
| Segunda carga | 1,0 mg/L como N, después de confirmar la primera |
| TurboStart | 29 mL por 95 L de volumen operativo |
| Fishless Fuel | 40 mg/mL como TAN, verificado por el test |
| Skimmer | Apagado durante los cinco primeros días tras TurboStart |
| Plazo de cada carga | Máximo 5 días desde su adición |

### Cantidades provisionales para 75 L y 96 L

- TurboStart 900: **22,9 mL**
- Fishless Fuel para la primera carga: **3,75 mL**
- Fishless Fuel para la segunda carga: **1,88 mL**
- Reef Salt: **2.925 g como referencia inicial**, no como dosis final garantizada para `S_P = 35`
- Activación de AF Bio Sand: **3 L de agua salada durante 24 horas**, según su ficha

Como referencia alternativa sobre los 96 L geométricos: **29,3 mL de TurboStart**, **4,80 mL de Fishless Fuel** para la primera carga, **2,40 mL** para la segunda y **3.744 g de Reef Salt** como punto de partida aproximado para 33 ppt. Estas cantidades no se utilizarán como dosis finales mientras no se mida el volumen operativo real.

Si el volumen medido no coincide con 75 L o 96 L, recalcular antes de dosificar:

```text
TurboStart (mL) = V_operativo (L) × 29 / 95
Fishless Fuel (mL) = V_operativo (L) × objetivo (mg/L como N) / 40
```

## Material y comprobaciones previas

Para Reef Salt, usar provisionalmente 39 g/L como referencia de preparación a 33 ppt y ajustar después con el instrumento hasta el objetivo S_P = 35. No convertir esa referencia linealmente en una dosis final de 35 ppt.

- RO/DI y medidor de TDS o conductividad operativo
- Aquaforest Reef Salt y recipiente limpio de preparación
- AF Bio Sand y sus dos preparaciones de activación
- FritzZyme TurboStart 900 Saltwater refrigerado, vigente y trazable
- Fritz Fishless Fuel vigente y trazable
- Tests de nitrógeno amoniacal y nitrito, con unidades, escala y límites registrados
- Métodos para pH, alcalinidad, salinidad y temperatura
- Recipientes graduados o balanza adecuados para las dosis
- Retorno, circulación y agitación superficial instalados
- Skimmer apagado o preparado para permanecer apagado
- Registro de fecha, hora, lote, dosis, mediciones e incidencias

No iniciar si hay fugas, niveles inseguros, materia orgánica en descomposición, circulación insuficiente o una lectura de salinidad que no pueda interpretarse.

## Secuencia de ejecución

### T−24 horas: activar AF Bio Sand

1. Preparar 3 L de agua salada con RO/DI y Aquaforest Reef Salt
2. Ajustar y verificar la preparación a `S_P = 35`
3. Llevar el recipiente aproximadamente al intervalo de 25–28 °C indicado para la activación del producto
4. Mezclar el AF Bio Sand con sus dos preparaciones según su ficha
5. Mantener el recipiente abierto durante 24 horas
6. Registrar lote, hora de inicio, temperatura y observaciones

No interpretar la activación como demostración de ciclado ni añadir productos no incluidos en la receta.

### T0: preparar el sistema

1. Instalar la roca, el sustrato activado y las superficies que permanecerán durante la prueba
2. Llenar el sistema con agua preparada y medir el volumen operativo real mediante volúmenes conocidos o un método equivalente registrable
3. Registrar el volumen, el método y cualquier incertidumbre
4. Comprobar que la temperatura se aproxima a 25,0 °C y que la salinidad es `S_P = 35`
5. Activar retorno, circulación y agitación superficial
6. Registrar línea base de nitrógeno amoniacal, nitrito, pH, alcalinidad, salinidad y temperatura; nitrato y fosfato serán opcionales de apoyo
7. Verificar lote, caducidad y conservación del TurboStart

### T0: inocular y añadir la primera carga

1. Agitar el TurboStart según su ficha y medir la dosis recalculada
2. Añadir el TurboStart al sistema con retorno y circulación activos
3. Mantener el skimmer apagado durante cinco días completos, salvo intervención necesaria por seguridad
4. Añadir Fishless Fuel en la misma sesión o dentro de las 24 horas siguientes
5. Utilizar la dosis recalculada para un objetivo de 2,0 mg/L como N
6. Medir la carga con el test elegido después de la mezcla suficiente del sistema y registrar el resultado
7. No redosificar aunque la lectura sea inferior a la prevista; primero comprobar cálculo, volumen, método y tendencia

La dosis calculada es un punto de partida. El resultado medido y la concentración declarada del lote prevalecen sobre una equivalencia teórica.

### Días 1–5: seguimiento inicial

Realizar cada día, aproximadamente a la misma hora:

- Medir nitrógeno amoniacal y nitrito
- Medir pH y temperatura
- Comprobar visualmente retorno, circulación, agitación superficial y nivel de la cámara de retorno
- Registrar salinidad y alcalinidad con la frecuencia fijada en el plan
- Anotar mantenimiento, evaporación, correcciones e incidencias

Mantener el ATO únicamente con RO/DI. No cambiar agua, limpiar superficies biológicas ni añadir otros productos salvo que una condición roja obligue a intervenir.

### Después de la primera carga

1. Confirmar que nitrógeno amoniacal y nitrito han alcanzado el límite de aceptación del método
2. Confirmar que permanecen en ese estado durante 24 horas
3. Verificar que no hubo una intervención que invalide la interpretación
4. Añadir la segunda carga de 1,0 mg/L como N con la dosis recalculada
5. Registrar fecha, hora, cálculo y medición inicial

Si la primera carga no cumple en un máximo de cinco días, no añadir la segunda: mantener el sistema, investigar y documentar la desviación.

### Después de la segunda carga

Seguir las mediciones hasta que amonio y nitrito alcancen de nuevo el límite de aceptación en un máximo de cinco días. La prueba solo se cierra si también permanecen estables durante el periodo de confirmación y el resto de condiciones siguen siendo interpretables.

## Puertas de decisión

### Verde: continuar

- Las mediciones siguen una tendencia interpretable
- La circulación, temperatura, salinidad y oxigenación son estables
- No hay animales ni descomposición

### Amarilla: pausar la progresión

- Una lectura contradice la tendencia
- El método, la unidad o la muestra son dudosos
- Se ha producido una intervención menor que debe evaluarse

Repetir la medición con el mismo método y no añadir nuevas variables.

### Roja: detener y corregir

- Oxigenación insuficiente o fallo de circulación
- Fuga, nivel inseguro o fallo del ATO
- Descomposición o contaminación
- Deterioro sostenido de pH o alcalinidad
- Necesidad de un cambio de agua urgente

Registrar la causa, la intervención y el volumen afectado. La carga en curso no se utilizará como confirmación sin repetirla o justificar formalmente su validez.

## Registro mínimo

```text
Fecha y hora:
Fase y carga:
Volumen operativo y método de medida:
Producto, presentación y lote:
Dosis calculada y dosis añadida:
Unidad del objetivo:
Nitrógeno amoniacal:
Nitrito:
Nitrato, si se mide:
pH / alcalinidad:
Salinidad / temperatura:
Estado de retorno, circulación y agitación:
Estado del skimmer y ATO:
Mantenimiento o intervención:
Incidencias:
Decisión:
```

## Cierre y transición

Al cumplir las dos cargas, guardar el registro completo y enlazarlo con el [plan de maduración](../04_maduracion/plan.md). El cierre demuestra capacidad nitrificante bajo esta prueba; no autoriza por sí solo la incorporación de toda la comunidad ni sustituye la observación de maduración.

## Referencias operativas

- [Plan de ciclado](plan.md)
- [Receta combinada Fritz–Aquaforest](decisiones/seleccion-inoculante-y-receta.md)
- [Ficha de TurboStart 900](../01_fichas/05_productos/fritzzyme-turbostart-900.md)
- [Ficha de Fishless Fuel](../01_fichas/05_productos/fritz-fishless-fuel.md)
- [Ficha de AF Bio Sand](../01_fichas/05_productos/af-bio-sand.md)
- [Ficha de Aquaforest Reef Salt](../01_fichas/05_productos/aquaforest-reef-salt.md)
