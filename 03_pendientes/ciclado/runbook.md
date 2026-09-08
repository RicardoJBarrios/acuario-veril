# Runbook de ciclado sin peces de Veril

## Propósito

Este runbook ejecuta el [plan de ciclado](plan.md) con la receta adoptada para Veril. Convierte el plan en una secuencia reproducible de preparación, dosificación, medición, decisión y registro.

El runbook ejecuta la ruta B adoptada: una fase previa con roca y fondo desnudo para liberar finos y observar el sistema, seguida de la incorporación del AF Bio Sand antes de iniciar el ciclado biológico.

> [!CAUTION]
> No introducir peces, corales, invertebrados ni equipo de limpieza durante esta prueba. Fritz Fishless Fuel no debe utilizarse con animales.

## Valores fijados

| Variable | Valor o criterio |
| --- | --- |
| Volumen estimado del display | 59–60 L con 2 cm de arena, 2 cm de margen superior y la roca disponible |
| Volumen de planificación del sistema completo | 75 L, provisional, incluido el sump |
| Volumen geométrico estimado | Aproximadamente 96 L; referencia de control, no volumen final de dosificación |
| Temperatura del sistema | 25,0 °C como objetivo operativo |
| Salinidad | `S_P = 35`, verificada por medición del agua de mar filtrada con UV |
| Agua introducida antes del ciclado | Aproximadamente 87 L de agua de mar filtrada con UV suministrada por Elite Reef Kanarias: 80 L el 5 de septiembre y unos 7 L el 6 de septiembre |
| Agua posterior para cambios | Agua de ósmosis RO/DI con la sal seleccionada para Veril; sistema RO/DI pendiente |
| Primera carga | 2,0 mg/L como N |
| Segunda carga | 1,0 mg/L como N, después de confirmar la primera |
| FritzZyme 9 | Sistema nuevo: 119 ml por 19 L; recalcular sobre `V_operativo` |
| Fishless Fuel | 40 mg/mL como TAN, verificado por el test |
| Skimmer | Apagado durante los cinco primeros días tras FritzZyme 9 |
| Plazo de cada carga | Máximo 5 días desde su adición |

### Cantidades provisionales para 75 L y 96 L

- FritzZyme 9: **469,7 ml para 75 L como referencia de sistema nuevo; el envase disponible contiene 946 ml**
- Fishless Fuel para la primera carga: **3,75 mL**
- Fishless Fuel para la segunda carga: **1,88 mL**
- Aquaforest Reef Salt: No se utilizará para el llenado inicial
- Activación de AF Bio Sand: **3 L de agua salada durante 24 horas**, preferentemente del agua filtrada con UV suministrada

Como referencia alternativa sobre los 96 L geométricos: **4,80 mL de Fishless Fuel** para la primera carga y **2,40 mL** para la segunda. La dosis de FritzZyme 9 y cualquier preparación con Reef Salt no se fijarán para este ciclado con agua de mar. Estas cantidades no se utilizarán como dosis finales mientras no se mida el volumen operativo real.

El valor de 59–60 L describe solo el display. Si el volumen operativo total medido no coincide con 75 L o 96 L, recalcular antes de dosificar:

```text
FritzZyme 9 (mL) = V_operativo (L) × 119 / 19
Fishless Fuel (mL) = V_operativo (L) × objetivo (mg/L como N) / 40
```

## Material y comprobaciones previas

El agua de mar suministrada no se preparará con Reef Salt. Se comprobará con el instrumento hasta confirmar el objetivo `S_P = 35`; no se corregirá mediante una equivalencia teórica de gramos por litro.

- Agua de mar filtrada con UV suministrada por Elite Reef Kanarias
- Medidor de salinidad y métodos para temperatura, pH y alcalinidad
- AF Bio Sand y sus dos preparaciones de activación
- FritzZyme 9 vigente y trazable; el envase disponible es de **946 ml** y cubre por sí solo la dosis de sistema nuevo para 75 L
- Fritz Fishless Fuel vigente y trazable
- [Refractómetro DD The Aquarium Solution **AQPR001**](../../01_verilpedia/05_productos/06_dd-aquarium-solution-aqpr001/dd-aquarium-solution-aqpr001.md), adquirido para medir la salinidad
- [Salifert Ammonia NH3 Profi Test](../../01_verilpedia/05_productos/12_salifert-ammonia-nh3/salifert-ammonia-nh3.md), 50 tests, caducidad **10/2027**
- [Salifert NO2 Profi Test](../../01_verilpedia/05_productos/13_salifert-no2/salifert-no2.md), 50 tests, caducidad **06/2029**
- [Tetra Test 7 en 1](../../01_verilpedia/05_productos/14_tetra-test-7-en-1/tetra-test-7-en-1.md), 50 tiras, para caracterización orientativa de pH, KH, GH, NO2, NO3, Cl2 y CO2
- Tests de nitrógeno amoniacal y nitrito, con unidades, escala y límites registrados; los Salifert serán los métodos principales
- Métodos para pH, alcalinidad, salinidad y temperatura
- Recipientes graduados o balanza adecuados para las dosis
- Retorno, circulación y agitación superficial instalados
- Skimmer apagado o preparado para permanecer apagado
- Registro de fecha, hora, lote, dosis, mediciones e incidencias

No iniciar si hay fugas, niveles inseguros, materia orgánica en descomposición, circulación insuficiente o una lectura de salinidad que no pueda interpretarse.

## Secuencia de ejecución

### Fase previa: acondicionar la roca sin arena

1. Mantener la roca instalada sin arena, FritzZyme 9 ni Fishless Fuel durante unos días
2. Mantener retorno, circulación y agitación superficial activos con niveles seguros
3. Observar y registrar polvo, partículas, suciedad, depósitos y cualquier anomalía
4. Recolocar, si es necesario, las piezas del hardscape y comprobar la estabilidad mecánica, los márgenes, los espacios negativos y el acceso de mantenimiento
5. Decidir si se conservan las islas y confirmar que siguen separadas de la estructura principal
6. Realizar los tests disponibles al finalizar esta fase
7. Si no aparece ninguna anomalía y el montaje queda validado, sifonar o retirar los residuos sueltos y continuar con la activación del sustrato

Esta fase no cuenta como inicio del ciclado y no se dosificará amonio ni bacterias durante ella.

### T−24 horas: activar AF Bio Sand

1. Separar 3 L del agua de mar filtrada con UV suministrada por Elite Reef Kanarias
2. Verificar que el agua está dentro del objetivo `S_P = 35` y registrar sus parámetros
3. Llevar el recipiente aproximadamente al intervalo de 25–28 °C indicado para la activación del producto
4. Mezclar el AF Bio Sand con sus dos preparaciones según su ficha
5. Mantener el recipiente abierto durante 24 horas
6. Registrar lote, hora de inicio, temperatura y observaciones

No interpretar la activación como demostración de ciclado ni añadir productos no incluidos en la receta.

La arena activada se incorporará al display después de la inspección y limpieza de la fase previa, antes de añadir FritzZyme 9 y Fishless Fuel. No se utilizará la arena para sostener las rocas.

### T0: preparar el sistema

1. Confirmar que la roca y las superficies que permanecerán durante la prueba siguen estables; añadir el sustrato activado como cama definitiva
2. Completar el sistema hasta sus niveles de trabajo previstos con agua de mar filtrada con UV y medir el volumen operativo real mediante volúmenes conocidos o un método equivalente registrable
3. Registrar el volumen, el método y cualquier incertidumbre
4. Comprobar que la temperatura se aproxima a 25,0 °C y que la salinidad es `S_P = 35`
5. Activar retorno, circulación y agitación superficial
6. Registrar línea base de nitrógeno amoniacal, nitrito, pH, alcalinidad, salinidad y temperatura; nitrato y fosfato serán opcionales de apoyo
7. Verificar lote, caducidad y conservación de FritzZyme 9, registrar su pauta de dosificación y confirmar que hay cantidad suficiente

### T0: inocular y añadir la primera carga

1. Agitar FritzZyme 9 según su etiqueta y medir la dosis recalculada
2. Añadir FritzZyme 9 al sistema con retorno y circulación activos
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

Al cumplir las dos cargas, guardar el registro completo y enlazarlo con el [plan de maduración](../maduracion/plan.md). El cierre demuestra capacidad nitrificante bajo esta prueba; no autoriza por sí solo la incorporación de toda la comunidad ni sustituye la observación de maduración.

## Referencias operativas

- [Plan de ciclado](plan.md)
- [Receta combinada Fritz–Aquaforest](decisiones/seleccion-inoculante-y-receta.md)
- [Ficha de FritzZyme 9](../../01_verilpedia/05_productos/09_fritzzyme-9/fritzzyme-9.md)
- [Ficha de Fishless Fuel](../../01_verilpedia/05_productos/08_fritz-fishless-fuel/fritz-fishless-fuel.md)
- [Ficha de AF Bio Sand](../../01_verilpedia/05_productos/01_af-bio-sand/af-bio-sand.md)
- [Ficha de Aquaforest Reef Salt](../../01_verilpedia/05_productos/02_aquaforest-reef-salt/aquaforest-reef-salt.md)
