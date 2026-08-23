# Veril: configuración integrada

> Esta ficha integra las decisiones concretas de Veril que se documentan por separado en las fichas del directorio. No sustituye las dimensiones, las fichas de hardware, las fichas de organismos ni los planes operativos.

## Alcance

Veril se configura como un acuario marino de arrecife de aproximadamente **60 × 32 × 40 cm** de display, con una arquitectura AIO lateral de pequeño volumen, una configuración biológica mixta y una arquitectura de procesamiento basada en el método Berlín.

La configuración integrada combina:

- Una envolvente física AIO con display y compartimento técnico lateral
- Un aquascape organizado mediante masas rocosas, islas, playa, canal y espacio negativo
- Una circulación con retorno integrado y bomba de movimiento independiente
- Una luminaria LED de amplio espectro con zonificación posterior mediante PPFD
- Una comunidad prevista de peces, corales, coraliformes e invertebrados compatibles
- Una química que se comprobará mediante parámetros, relaciones y tendencias
- Un procesamiento basado en superficies colonizadas, exportación orgánica mediante skimmer y retirada física de materia, bajo las condiciones proporcionadas por la circulación

La explicación general de cada línea pertenece al [modelo de dimensiones](../01_fichas/01_dimensiones/00_modelo.md) y a sus fichas correspondientes. Este documento solo reúne cómo se conectan en la implementación de Veril.

## Matriz de implementación

| Dimensión | Decisión concreta en Veril | Documento propietario | Comprobación principal |
| --- | --- | --- | --- |
| Infraestructura | AIO lateral de pequeño volumen, con display, compartimento técnico, retorno y margen de seguridad | [Infraestructura](01_infraestructura.md), [dimensión de infraestructura](../01_fichas/01_dimensiones/01_infraestructura.md) y documentación de la urna | Integridad, niveles, parada, reinicio, acceso y mantenimiento |
| Espacial | Masa principal posterior derecha, masa secundaria, islas, playa, canal y espacio negativo funcional | [Espacial](02_espacial.md) y [dimensión espacial](../01_fichas/01_dimensiones/02_espacial.md) | Estabilidad, accesibilidad, rutas libres y reserva de crecimiento |
| Hidráulica | [Mantis Tourbon 60](../01_fichas/04_hardware/mantis-tourbon-60/mantis-tourbon-60.md) para movimiento y [Sicce Micra Plus 600](../01_fichas/04_hardware/sicce-micra-plus-600/sicce-micra-plus-600.md) para retorno, integradas sobre las rutas de renovación del aquascape | [Hidráulica](03_hidraulica.md) y [técnica de la urna](../01_fichas/04_hardware/urna/tecnica.md) | Renovación, distribución, transporte, reinicio y acumulaciones |
| Iluminación | [AI Prime 16HD Reef](../01_fichas/04_hardware/ai-prime-16hd-reef/ai-prime-16hd-reef.md), suspendida y con *shade*, cuyo mapa se medirá con [DanoPlus DP-414](../01_fichas/04_hardware/danoplus-dp-414/danoplus-dp-414.md) | [Iluminación](04_iluminacion.md) | Cobertura, gradientes, sombras, mapa de PPFD y compatibilidad con las zonas |
| Biológica | Configuración mixta con incorporación progresiva y evaluación de compatibilidad y crecimiento | [Biología](06_biologia.md) y fichas específicas de organismos | Respuesta observable, capacidad compartida, contención y mantenimiento |
| Química | Seguimiento de composición y estabilidad mediante parámetros, relaciones y tendencias; temperatura objetivo del agua de 25,0 °C | [Química](05_quimica.md) y [fichas de parámetros](../01_fichas/03_parametros/README.md) | Método de medición, tendencias, relaciones, estabilidad y respuesta térmica |
| Procesamiento | Método Berlín como referencia: superficies colonizadas, skimmer y retirada física, bajo las condiciones hidráulicas del sistema | [Procesamiento](07_procesamiento.md), [dimensión de procesamiento](../01_fichas/01_dimensiones/07_procesamiento.md) y [ficha del skimmer Sicce Shark 300](../01_fichas/04_hardware/sicce-shark-skimmer-300/sicce-shark-skimmer-300.md) | Capacidad demostrada, exportación, acumulaciones y continuidad del mantenimiento |

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

- La estabilidad física de la urna, la roca, el sustrato y los elementos técnicos
- La recepción del volumen de retrosifonado y el reinicio seguro del retorno
- La renovación del agua alrededor, debajo y detrás de la estructura
- La ausencia de acumulaciones persistentes que no puedan localizarse o retirarse
- La cobertura lumínica y el mapa de PPFD de las zonas funcionales
- La compatibilidad entre las primeras incorporaciones y las condiciones reales del sistema
- La estabilidad química durante el ciclado, la maduración y las incorporaciones
- La capacidad de procesamiento y exportación frente a las entradas reales
- El acceso suficiente para observar, medir, limpiar, ajustar y retirar elementos
- La conservación de margen operativo frente a evaporación, crecimiento, suciedad y perturbaciones previsibles

Estos criterios se demostrarán mediante observaciones, mediciones y pruebas en los documentos propietarios. El ciclado y la maduración mantienen sus protocolos separados y utilizarán estos criterios cuando corresponda. Mientras no se hayan realizado, se consideran pendientes.

## Estado de implementación

La configuración reúne decisiones de diseño y pendientes de validación. En particular, deben quedar registrados antes de dar por cerrada la implementación:

- El montaje final y la estabilidad de las masas de roca
- La profundidad y distribución real del sustrato
- La respuesta hidráulica con la composición instalada
- La prueba de parada, retrosifonado y reinicio
- El mapa reproducible de PPFD
- La selección y posición de los primeros organismos
- Las tendencias químicas de referencia
- La respuesta del procesamiento durante las fases operativas documentadas en `03_ciclado/`

Una decisión prevista no debe redactarse como una propiedad demostrada. El estado de cada comprobación se actualizará en su documento propietario o en el plan operativo que corresponda.

## Régimen térmico adoptado

Veril adopta una **temperatura objetivo del agua de 25,0 °C**.

Esta decisión se toma como un punto de consigna para una configuración mixta de arrecife, no como un valor universal ni como una garantía biológica. Se sitúa en una posición intermedia dentro del intervalo operativo general de aproximadamente 24–26 °C descrito en la [ficha de temperatura](../01_fichas/03_parametros/temperatura.md).

La elección de 25,0 °C busca equilibrar:

- Compatibilidad general con peces, corales, coraliformes e invertebrados tropicales previstos
- Demanda metabólica y de oxígeno inferior a la que implicaría mantener habitualmente el sistema en el extremo alto del intervalo
- Margen frente a episodios cálidos en Santa Cruz de Tenerife
- Carga térmica de la iluminación, las bombas y los equipos sumergidos
- Capacidad de mantener el despacho y el acuario en condiciones razonablemente estables mediante aire acondicionado portátil, ventilación y control térmico

El clima local no determina por sí solo la temperatura del agua, pero sí forma parte de la carga térmica que debe gestionar el sistema. Las normales de AEMET para Santa Cruz de Tenerife muestran máximas medias cercanas a 28–29 °C en julio y agosto, por lo que la refrigeración ambiental aporta margen durante los periodos cálidos. [AEMET](https://www.aemet.es/es/serviciosclimaticos/datosclimatologicos/valoresclimatologicos?k=coo&l=C449C)

La temperatura objetivo no implica perseguir décimas mediante conmutaciones constantes. La banda normal de funcionamiento, los avisos, los límites de intervención, la respuesta ante sobretemperatura y la respuesta ante pérdida de calefacción quedan pendientes de fijarse con el sensor, el calentador, la carga térmica y las pruebas de la instalación.

La dimensión química conserva la interpretación de la temperatura como variable de estado y contexto de medición. La infraestructura documenta la capacidad física de calentamiento y disipación, la hidráulica su distribución y homogeneización, y la dimensión biológica su compatibilidad con la comunidad prevista.

## Documentos relacionados

- [Modelo de dimensiones](../01_fichas/01_dimensiones/00_modelo.md)
- [Índice de dimensiones](../01_fichas/01_dimensiones/00_README.md)
- [Plan de ciclado](../03_ciclado/plan.md)
- [Plan de maduración](../04_maduracion/plan.md)
- [Parámetros del agua](../01_fichas/03_parametros/README.md)
