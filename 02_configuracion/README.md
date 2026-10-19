# Veril: configuración integrada

> Esta ficha integra las decisiones concretas de Veril que se documentan por separado en las fichas del directorio. No sustituye las dimensiones, las fichas de hardware, las fichas de organismos ni los planes operativos.

## Alcance

Veril se configura como un acuario marino de arrecife con un display interior de **594 × 308 mm** y una altura exterior de **400 mm**, con una arquitectura AIO lateral de pequeño volumen, una configuración biológica mixta y una arquitectura de procesamiento basada en el método Berlín.

El detalle de material, envases y recepción está en [Infraestructura](01_dimensiones/01_infraestructura.md#material-y-estado-documentados); los tests disponibles, en [Química](01_dimensiones/05_quimica.md#métodos-disponibles).

La explicación general de cada línea pertenece al [modelo de dimensiones](../01_verilpedia/01_dimensiones/README.md) y a sus fichas correspondientes. Este documento solo reúne cómo se conectan en la configuración de Veril.

## Matriz de implementación

| Dimensión | Decisión concreta en Veril | Documento propietario | Comprobación principal |
| --- | --- | --- | --- |
| Infraestructura | AIO lateral de pequeño volumen, con display, compartimento técnico, retorno y margen de seguridad | [Infraestructura](01_dimensiones/01_infraestructura.md), [dimensión de infraestructura](../01_verilpedia/01_dimensiones/01_infraestructura.md) y documentación de la urna | Integridad, niveles, parada, reinicio, acceso y mantenimiento |
| Espacial | Masa principal posterior derecha, masa secundaria, islas, playa, canal y espacio negativo funcional | [Espacial](01_dimensiones/02_espacial.md) y [dimensión espacial](../01_verilpedia/01_dimensiones/02_espacial.md) | Estabilidad, accesibilidad, rutas libres y reserva de crecimiento |
| Hidráulica | [Mantis Tourbon 60](../01_verilpedia/04_hardware/mantis-tourbon-60/mantis-tourbon-60.md) instalada como bomba de movimiento, con ajuste actual documentado, y Sicce Micra instalada para retorno (identificación corregida el 19/10/2026; compra de la Jebao DC-650 comunicada, instalación pendiente), integradas sobre las rutas de renovación del aquascape | [Hidráulica](01_dimensiones/03_hidraulica.md) y [técnica de la urna](../01_verilpedia/04_hardware/urna/tecnica.md) | Renovación, distribución, transporte, reinicio y acumulaciones |
| Iluminación | [AI Prime 16HD Reef](../01_verilpedia/04_hardware/ai-prime-16hd-reef/ai-prime-16hd-reef.md) instalada, centrada geométricamente y apagada; posición de diseño, configuración final y mapa pendientes de comprobación | [Iluminación](01_dimensiones/04_iluminacion.md) | Cobertura, gradientes, sombras, mapa de PPFD y compatibilidad con las zonas |
| Biológica | Configuración mixta con incorporación progresiva y evaluación de compatibilidad y crecimiento | [Biología](01_dimensiones/06_biologia.md) y fichas específicas de organismos | Respuesta observable, capacidad compartida, contención y mantenimiento |
| Química | Seguimiento de composición y estabilidad mediante parámetros, relaciones y tendencias; 25–26 °C preferida y 24,5–26,5 °C como objetivo operativo normal | [Química](01_dimensiones/05_quimica.md) y [fichas de parámetros](../01_verilpedia/03_parametros/README.md) | Método de medición, tendencias, relaciones, estabilidad y respuesta térmica |
| Procesamiento | Método Berlín como referencia: superficies colonizadas, skimmer encendido el 19/10/2026 para intentar favorecer la oxigenación (efecto pendiente de medir) y retirada física, bajo las condiciones hidráulicas del sistema | [Procesamiento](01_dimensiones/07_procesamiento.md), [dimensión de procesamiento](../01_verilpedia/01_dimensiones/07_procesamiento.md) y [ficha del skimmer Sicce Shark 300](../01_verilpedia/04_hardware/sicce-shark-skimmer-300/sicce-shark-skimmer-300.md) | Capacidad demostrada, exportación, acumulaciones y continuidad del mantenimiento |

## Dependencias de diseño

Las decisiones no se ejecutan como una secuencia independiente. Cada una establece condiciones para las demás:

1. La infraestructura limita el volumen, el acceso, los niveles y la seguridad
2. La roca y el sustrato distribuyen estructura, espacio negativo, playas, canales y superficies
3. La hidráulica debe comprobar que esas formas permiten renovación y transporte suficientes
4. La iluminación debe medirse sobre la geometría real y no solo sobre la posición de la luminaria
5. La biología se incorporará según las zonas, el espacio, el crecimiento, el flujo, la luz y la capacidad demostrada
6. La química se interpretará junto con las entradas, los consumos, el procesamiento y el mantenimiento
7. El procesamiento debe demostrar que puede transformar y retirar la materia introducida bajo las condiciones resultantes

Este orden sirve para identificar dependencias, no para imponer un procedimiento único. Una modificación en una dimensión puede exigir revisar las demás.

## Criterios de aceptación integrados

La configuración no se considerará cerrada por la mera instalación de los componentes. Deberá comprobarse conjuntamente:

- La estabilidad física de la urna, las masas de roca y los elementos técnicos, y la profundidad y distribución del sustrato
- La recepción del volumen de retrosifonado y el reinicio seguro del retorno
- La renovación del agua alrededor, debajo y detrás de la estructura
- La ausencia de acumulaciones persistentes que no puedan localizarse o retirarse
- La cobertura lumínica y el mapa reproducible de PPFD de las zonas funcionales
- La selección, posición y compatibilidad de las primeras incorporaciones con las condiciones reales del sistema
- Las tendencias de referencia y la estabilidad química durante el ciclado, la maduración y las incorporaciones
- La capacidad de procesamiento y exportación frente a las entradas reales, incluido el ciclado documentado en `03_pendientes/ciclado/`
- El acceso suficiente para observar, medir, limpiar, ajustar y retirar elementos
- La conservación de margen operativo frente a evaporación, crecimiento, suciedad y perturbaciones previsibles

Estos criterios se demostrarán mediante observaciones, mediciones y pruebas en los documentos propietarios. El ciclado y la maduración mantienen sus protocolos separados y utilizarán estos criterios cuando corresponda. Mientras no se hayan realizado, se consideran pendientes.

## Estado de implementación

Las comprobaciones anteriores se mantienen abiertas hasta su registro en la ficha propietaria o el plan correspondiente, enlazando la operación que las documenta. Una decisión prevista no equivale a una propiedad demostrada.

## Régimen térmico adoptado

La lógica vigente del controlador del Rowenta y sus guardarraíles se documentan
en [Control térmico de Veril](04_control-termico.md). Las mediciones y actuaciones
fechadas se conservan en el [registro de puesta en servicio y mediciones del
27 de septiembre](../04_operaciones/2026/09/2026-09-27.md#puesta-en-servicio-del-control-térmico-inicial).

La zona preferida del agua es **25–26 °C**, con **24,5–26,5 °C** como objetivo operativo normal. 25 °C es una referencia central, no una consigna puntual. Las bandas siguientes son criterios locales de gestión, no umbrales fisiológicos universales.

| Estado | Temperatura del agua | Interpretación operativa |
| --- | --- | --- |
| Prioridad fría | **<22,0 °C** | Escalón local de revisión prioritaria; no es un umbral científico de lesión. Verificar enseguida la lectura y el termómetro independiente, y valorar duración, tendencia y fauna. No hay calefacción automática instalada. |
| Por debajo del objetivo | **22,0–23,0 °C** | Fuera del objetivo operativo. Confirmar telemetría y medición; si persiste, investigar y corregir gradualmente cuando exista una solución de calefacción validada. No equivale por sí solo a daño demostrado. |
| Excursión fría | **23,0–24,0 °C** | Excursión tolerable según la evidencia disponible, pero no se adopta como régimen normal; investigar si persiste. La caída de rendimiento fisiológico de peces observada en experimentos no equivale a lesión aguda en el acuario. |
| Fresca | **24,0–24,5 °C** | Banda baja razonablemente normal, aunque inferior al óptimo; observar estabilidad y tendencia, sin exigir corrección inmediata por una lectura aislada. |
| Óptima baja | **24,5–25,0 °C** | Zona óptima; no requiere refrigeración. |
| Preferida | **25,0–26,0 °C** | Zona que se procura mantener la mayor parte del tiempo. 25 °C es referencia central, no una consigna exacta. |
| Óptima alta | **26,0–26,5 °C** | Dentro del rango óptimo; no refrigerar solo por cruzar 26 °C. |
| Cálida | **26,5–27,0 °C** | Aceptable; interpretar duración y tendencia. |
| Cálida estival | **27,0–27,5 °C** | Aceptable temporalmente; no equivale por sí sola a alarma. |
| Alta / transición | **27,5–28,0 °C** | Fin del rango aceptable; procurar que deje de subir, interpretando duración y tendencia. |
| Protección | **28,0–28,5 °C** | Buscar que la temperatura deje de subir y disminuya. |
| Alerta | **28,5–29,0 °C** | Aviso al propietario y comprobación de lectura, duración, tendencia y refrigeración. |
| Crítica | **29,0–30,0 °C** | Situación no aceptable como operación normal; priorizar recuperar margen térmico. |
| Emergencia | **≥30,0 °C** | Episodio excepcional que requiere respuesta prioritaria. |

La envolvente y sus bandas se adoptan como decisión específica para Veril. No afirman que el límite de una banda sea un umbral universal de lesión o blanqueamiento. La temperatura, duración y tendencia se interpretan por separado. El clima de Santa Cruz de Tenerife contribuye a la carga ambiental, pero no determina por sí solo la temperatura del agua: las normales de AEMET de la estación C449C reflejan máximas medias diarias de 28,7 °C en julio, 29,0 °C en agosto y 28,1 °C en septiembre. [AEMET: valores climatológicos normales de Santa Cruz de Tenerife](https://www.aemet.es/es/serviciosclimaticos/datosclimatologicos/valoresclimatologicos?k=coo&l=C449C)

La refrigeración está automatizada como piloto; no hay alarma ni calefacción automática para el extremo frío. Las comprobaciones y los requisitos de una futura calefacción están en [Control térmico](04_control-termico.md#extremo-frío-y-preparación-de-calefacción).

Las normales ambientales no demuestran por sí mismas la temperatura del acuario. La relación concreta entre ambos sistemas requiere contrastar los históricos de Home Assistant, las órdenes del climatizador y las lecturas del agua.

La telemetría de temperatura del agua procede de `off-sns-05`, con la sonda sumergida en la cámara Skimmer. Es una lectura del agua del sistema, no una comprobación metrológica independiente; la ubicación y las observaciones fechadas constan en los [registros del 20 y 23 de septiembre](../04_operaciones/2026/09/2026-09-20-medicion-manual-salinidad-y-quimica.md) y en la [revisión del 24 de septiembre](../04_operaciones/2026/09/2026-09-24.md#revisión-y-preparación-del-control-térmico).

El piloto se puso en servicio el **27 de septiembre de 2026**. Su lógica, consignas, protección de telemetría y estado de validación están en [Control térmico](04_control-termico.md); las actuaciones y lecturas fechadas, en la [operación de puesta en servicio](../04_operaciones/2026/09/2026-09-27.md#puesta-en-servicio-del-control-térmico-inicial).

Este régimen es vinculante como criterio de compatibilidad para las decisiones posteriores de Veril:

- La población futura se seleccionará para que su mantenimiento habitual sea compatible con la zona preferida 25–26 °C y el objetivo operativo normal 24,5–26,5 °C; una especie con mínimo publicado superior podrá estrechar el extremo frío. Las excursiones 23–24 °C no se consideran régimen normal y por debajo de 23 °C se está fuera del objetivo. No se añadirá fauna mientras el agua esté en alerta.
- Las recetas, la preparación de agua y los cambios de agua deberán evitar saltos térmicos innecesarios y ser compatibles con esta envolvente. No se modifica con ello ninguna receta ni dosis ya adoptada; su validación térmica se hará en su documento operativo antes de ejecutarla.
- La iluminación, bombas, ventilación y refrigeración ambiental se evaluarán por su contribución al balance térmico, no por una lectura aislada.
- Cualquier ficha o plan posterior que proponga un requisito incompatible deberá revisarse expresamente; este régimen no presupone que una especie, una receta o un equipo ya cumplan el criterio sin evidencia propia.

La dimensión química conserva la interpretación de la temperatura como variable de estado y contexto de medición. La infraestructura documenta la capacidad física de calentamiento y disipación, la hidráulica su distribución y homogeneización, y la dimensión biológica su compatibilidad con la comunidad prevista.

## Organización y documentos específicos

- [Hardscape](02_hardscape/README.md): composición, plantilla, inventario fotográfico y registro visual de la roca
- [Biología específica](03_biologia/README.md): criterios de selección, candidatos y escenarios del proyecto
- [Identidad gráfica](../06_Logo/README.md): nombre, logotipo y criterios visuales de Veril

Los documentos de `01_dimensiones/` mantienen la correspondencia con las siete dimensiones generales de [Verilpedia](../01_verilpedia/01_dimensiones/README.md). `README.md` integra sus decisiones sin sustituir las fichas propietarias. Los directorios `02` y `03` reúnen bloques específicos del proyecto que necesitan más de un documento o recursos visuales.

Cada ficha es propietaria de su materia. Las relaciones con otros aspectos deben expresarse mediante enlaces y consecuencias concretas, sin repetir las definiciones generales ni la configuración integrada.

La función general de la microfauna pertenece a las fichas de [Verilpedia](../01_verilpedia/02_biologia/01_microorganismos/02_microfauna/README.md). Su papel esperado en Veril se resume en [Biología](01_dimensiones/06_biologia.md), y su incorporación, si procede, se decide en el [plan de microfauna de maduración](../03_pendientes/maduracion/03_plan-microfauna.md).

Las actuaciones que materializan o comprueban esta configuración se registran en [Operaciones](../04_operaciones/README.md). Estas fichas pueden resumir el estado vigente y enlazar la operación que lo acredita, pero no sustituyen su registro fechado.

## Documentos relacionados

- [Índice de dimensiones](../01_verilpedia/01_dimensiones/README.md)
- [Plan de ciclado](../03_pendientes/ciclado/01_plan.md)
- [Plan de maduración](../03_pendientes/maduracion/01_plan.md)
- [Parámetros del agua](../01_verilpedia/03_parametros/README.md)
