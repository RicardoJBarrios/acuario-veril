# Cambios de agua de Veril

## Propósito

Este documento define el procedimiento específico de Veril para preparar, comprobar, registrar y utilizar el agua de cambio. La explicación general de qué es un cambio de agua, qué puede aportar y cuáles son sus límites pertenece a la [ficha general de cambios de agua](../../01_verilpedia/06_procesos/06_cambios-agua.md).

La composición declarada y los límites del producto pertenecen a la [ficha de Aquaforest Reef Salt](../../01_verilpedia/05_productos/02_aquaforest-reef-salt/aquaforest-reef-salt.md). La interpretación de cada parámetro pertenece a las [fichas de parámetros](../../01_verilpedia/03_parametros/README.md). Este documento concreta cómo se utilizará esa información en Veril, sin duplicar sus definiciones generales.

## Decisiones adoptadas

- Preparar el agua nueva con agua RO/DI y [Aquaforest Reef Salt](../../01_verilpedia/05_productos/02_aquaforest-reef-salt/aquaforest-reef-salt.md)
- Tomar como referencia un cambio nominal de **10 L** y preparar el agua nueva para `S_P = 35`; la base de cálculo y la masa inicial de sal se detallan en «Base nominal para cambios y sal»
- Utilizar exclusivamente agua RO/DI sin sal para reponer la evaporación mediante el [ATO seleccionado](../../01_verilpedia/04_hardware/dd-h2ocean-compact-ato/dd-h2ocean-compact-ato.md)
- Registrar el lote de sal, la preparación y las mediciones asociadas a cada cambio
- No utilizar un cambio de agua como sustituto de identificar una fuente, un consumo anómalo, una precipitación o un problema de procesamiento

## Decisiones pendientes

- Frecuencia o condición que desencadenará un cambio
- Momento y parámetros de la medición posterior en el acuario
- Límites que obligarán a aplazar, repetir o modificar una preparación
- Diferencia máxima admisible de temperatura y salinidad entre el agua nueva y Veril
- Criterio de preparación del agua nueva cuando la salinidad real de Veril difiera del objetivo `S_P = 35`
- Criterio operativo de aceptación del agua RO/DI

## Base nominal para cambios y sal

La convención simplificada vigente de Veril es **75 L para el sistema completo** y **60 L para el display**. El cambio nominal será de **10 L**, aproximadamente el 13,3 % del sistema completo. Si en una ocasión se decide expresar un cambio como porcentaje, el cálculo será:

```text
Volumen del cambio (L) = 75 L × porcentaje / 100
```

Si el cálculo se refiere solo al display, se utilizarán sus **60 L** nominales. La frecuencia o el motivo que desencadenará el cambio sigue pendiente y no se fija aquí.

Aquaforest publica **390 g por 10 L** como cantidad inicial aproximada para **33 ppt** y pide medir la salinidad resultante ([instrucciones oficiales](https://aquaforest.eu/en/products/seawater/marine-salts/reef-salt/)). Para **35 ppt** se han encontrado dos referencias de usuarios a **415 g por 10 L**: un usuario informa que su envase lo indica para 35 ppt ([Ultimate Reef, 7 de junio de 2025](https://www.ultimatereef.net/threads/aqua-forest-reef-salt-measurements.939220/)); otro declara que pesó 415 g en 10 L de RO/DI y obtuvo 35 ppt con un refractómetro calibrado ([Reef2Reef, 12 de febrero de 2025](https://www.reef2reef.com/threads/aquaforest-reef-salt-mixing-low-alkalinity.1096824/)). Son referencias de usuarios y no una especificación oficial verificada para todos los lotes. Como punto de partida nominal para los 10 L de Veril se adopta **aproximadamente 415 g**, sujeto a comprobación y ajuste por medición.

El cálculo de sal corresponde únicamente a los **10 L de agua nueva**, no a todo el sistema de 75 L. Los 415 g son un punto de partida: se medirán la salinidad y la temperatura después de disolver, y se ajustará gradualmente hasta `S_P = 35`. La lectura medida prevalece sobre las referencias publicadas. Tras preparar una primera mezcla, la masa realmente necesaria para ese lote y ese método podrá sustituir la estimación en las preparaciones posteriores.

## Preparación del agua nueva

La preparación seguirá la [ficha del producto](../../01_verilpedia/05_productos/02_aquaforest-reef-salt/aquaforest-reef-salt.md) y conservará la trazabilidad de la mezcla:

1. Identificar el lote de Aquaforest Reef Salt y comprobar el estado seco del producto
2. Medir el volumen real de agua RO/DI utilizado
3. Llevar el agua de partida aproximadamente a **24 °C**, como referencia de preparación del fabricante, y registrar su temperatura
4. Registrar la masa de sal añadida
5. Añadir la masa inicial definida en «Base nominal para cambios y sal» —o la referencia validada para ese lote— y mezclar con una bomba o movimiento suficiente
6. Mantener la mezcla durante al menos **15 minutos**, tiempo de disolución publicado por Aquaforest
7. Comprobar la claridad y medir la salinidad con un instrumento calibrado para agua marina; ajustar gradualmente con RO/DI o con salmuera preparada por separado hasta `S_P = 35`, homogeneizando y midiendo de nuevo tras cada ajuste
8. Igualar la temperatura con el acuario antes del uso y medir los parámetros adicionales definidos para esa fase o tipo de cambio
9. Registrar las mediciones y cualquier ajuste realizado

Los aproximadamente **24 °C** corresponden a la referencia de preparación del fabricante; antes del uso, el agua debe alcanzar la diferencia de temperatura que se establezca como admisible para Veril. Los 15 minutos son un mínimo de mezcla, no un criterio de aceptación: antes de incorporar el agua se deben verificar salinidad, temperatura y claridad. La salinidad medida prevalece sobre cualquier masa inicial; humedad, lote, volumen real, temperatura e instrumento pueden influir en el resultado.

Aquaforest indica que el agua preparada debe utilizarse dentro de los tres días posteriores a la disolución. Si no se utiliza inmediatamente, se almacenará en un recipiente limpio y cerrado para limitar la evaporación; antes del uso se repetirá la comprobación de salinidad, temperatura y estado visual.

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

Cuando el cambio pueda afectar a la interpretación química del sistema, se registrarán también los parámetros relevantes de la [química de Veril](../../02_configuracion/01_dimensiones/05_quimica.md), especialmente alcalinidad, calcio y magnesio. El pH, el oxígeno, los nutrientes u otros parámetros se incorporarán cuando el motivo del cambio o la fase del sistema lo requieran.

La medición del agua nueva permite conocer su composición observada, pero no demuestra por sí sola la composición completa de la sal ni sustituye un análisis de laboratorio o de lote.

La alcalinidad, el calcio, el magnesio y otros parámetros se medirán para caracterizar un lote nuevo o investigar resultados inesperados, no necesariamente en cada preparación. Los controles mínimos de aceptación se describen en «Preparación del agua nueva».

## Ejecución del cambio

Antes de retirar agua se registrarán:

- Fecha y hora
- Volumen previsto y volumen realmente retirado
- Salinidad y temperatura del acuario
- Parámetros que motiven o condicionen el cambio
- Alimentación, dosificación, mantenimiento o incidencias recientes

Antes de iniciar la retirada:

- Desactivar temporalmente el [ATO seleccionado](../../01_verilpedia/04_hardware/dd-h2ocean-compact-ato/dd-h2ocean-compact-ato.md) para que no interprete el descenso de nivel como evaporación
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

## Refuerzo del biofiltro con FritzZyme 9

Fritz menciona los cambios de agua, la incorporación de nuevos peces, la limpieza agresiva, la medicación y el cambio de material filtrante entre las situaciones en que puede reforzarse el biofiltro con FritzZyme 9. No prescribe una repetición automática después de cada cambio de agua: indica utilizarlo cuando se necesite reforzar el biofiltro y vigilar amoniaco y nitrito para valorar nuevas dosis.

En Veril, un cambio de agua rutinario por sí solo **no será motivo para dosificar FritzZyme 9**. Tras introducir peces u otra fauna que aumente la carga biológica, se vigilarán amoniaco y nitrito; se reservará el producto para una necesidad concreta de refuerzo del biofiltro. La misma condición se aplicará después de una intervención que pueda reducir significativamente la población bacteriana. Durante el ciclado sin peces prevalecen las dosis y el procedimiento del [plan de ciclado](../ciclado/plan.md).

Para un sistema establecido, Fritz publica **30 ml por cada 19 L**. El cálculo se hace sobre el volumen total del sistema, no solo sobre los 10 L cambiados ni sobre el volumen de animales incorporados. Con la base nominal de **75 L**, corresponde a **aproximadamente 118 ml por aplicación**. Si se actualiza el volumen operativo, se recalculará proporcionalmente.

Fritz indica mantener apagados el skimmer y los esterilizadores UV durante al menos **cinco días** después de la aplicación y mantener flujo o aireación adecuados. Como esta condición interrumpe el funcionamiento normal del skimmer de Veril, no se dosificará preventivamente: solo se valorará una aplicación si existe una necesidad concreta de refuerzo y se puede cumplir el periodo de apagado de forma segura. Si no es viable, se mantendrá la vigilancia de amoniaco y nitrito y no se usará el producto. La dosis, las condiciones y los límites del producto se detallan en la [ficha de FritzZyme 9](../../01_verilpedia/05_productos/09_fritzzyme-9/fritzzyme-9.md).

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

La interpretación general de la dilución, la sustitución y sus límites se conserva en la [ficha general de cambios de agua](../../01_verilpedia/06_procesos/06_cambios-agua.md).

## Fuentes y documentos relacionados

- [Cambios de agua en un acuario marino](../../01_verilpedia/06_procesos/06_cambios-agua.md): definición general, efectos, límites y balance simplificado de mezcla
- [Aquaforest Reef Salt](../../01_verilpedia/05_productos/02_aquaforest-reef-salt/aquaforest-reef-salt.md): composición declarada, preparación, conservación y análisis por lote
- [FritzZyme 9](../../01_verilpedia/05_productos/09_fritzzyme-9/fritzzyme-9.md): dosis, condiciones de uso y conservación del producto
- [Química de Veril](../../02_configuracion/01_dimensiones/05_quimica.md): decisión de utilizar RO/DI y Aquaforest Reef Salt
- [Fichas de parámetros](../../01_verilpedia/03_parametros/README.md): interpretación de salinidad, temperatura, alcalinidad, calcio, magnesio y demás variables
- [Plan de ciclado](../ciclado/plan.md): cambios de agua durante el establecimiento y sus efectos sobre la prueba
- [Plan de maduración](../maduracion/plan.md): cambios de agua durante la evolución inicial del sistema
