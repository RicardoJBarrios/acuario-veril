# Criterios de edición de dimensiones arquitectónicas y configuración

Este directorio documenta las dimensiones arquitectónicas de referencia adoptadas para Veril. El marco común está definido en [modelo.md](modelo.md), que explica qué es una dimensión, cómo se relacionan y cómo se evalúan. No se limita al procesamiento: también recoge la comunidad, la organización física y la organización espacial que el sistema debe integrar.

## Alcance

- Documentar dimensiones generales, sus funciones, límites y requisitos
- Documentar decisiones estructurales de Veril que afectan a varias áreas del sistema
- Explicar solo las consecuencias prácticas que la dimensión tratada tenga sobre animales, luz, flujo, alimentación, nutrientes, química o mantenimiento
- Mantener separadas las decisiones de Veril de las descripciones generales reutilizables
- Enlazar las fichas de hardware, parámetros, biología, implementación de Veril y los planes de ciclado cuando sean la fuente propietaria del detalle

## Marco del modelo

- Tratar las siete dimensiones como perspectivas funcionales de una única configuración, no como métodos alternativos ni como sistemas independientes
- Mantener explícita la variante de referencia adoptada para Veril en cada dimensión; estas fichas no son completamente genéricas
- Documentar en cada dimensión qué debe tenerse en cuenta, por qué importa, cómo se aplicará y cómo se comprobará
- Considerar la operación como una capa transversal de medición, mantenimiento, pruebas y respuesta, no como una octava dimensión
- Resolver las relaciones entre dimensiones mediante enlaces y consecuencias limitadas al objeto de la ficha responsable

## Alcance por documento

Cada documento de una dimensión debe ceñirse a la dimensión que trata, a su origen, funciones, componentes, efectos, límites, variantes, críticas, opiniones generalizadas y criterios de evaluación relacionados con ella.

- Incluir teoría general solo cuando sea necesaria para explicar una función o un límite específico de la arquitectura
- Documentar una consecuencia de animales, luz, flujo, nutrientes, química o mantenimiento solo si deriva de la arquitectura tratada
- No convertir una ficha de dimensión en una guía general de acuariofilia marina
- No añadir recomendaciones generales de población, bienestar, hardware o mantenimiento si no modifican o explican la arquitectura
- Enlazar el documento propietario cuando un tema general sea necesario para completar la lectura
- Tratar las opiniones generalizadas únicamente como recepción, debate o percepción de esa dimensión

### Bloques de contenido recomendados

La estructura no es un índice rígido. Cada ficha debe incluir únicamente los bloques pertinentes y puede agruparlos o renombrarlos cuando el objeto lo requiera, manteniendo la responsabilidad de la dimensión y la evaluación como hilo conductor:

1. **Qué es**: Definición breve de la dimensión, núcleo funcional, variante adoptada y tesis que la distingue de una lista de componentes
2. **Principio de funcionamiento**: Flujos de materia, energía o información que la arquitectura organiza, con un diagrama Mermaid cuando mejore la comprensión
3. **Componentes fundamentales**: Elementos que forman el núcleo, descritos por la función que cumplen y por sus condiciones de funcionamiento
4. **Exportación y mantenimiento**: Procesos mediante los que la arquitectura retira, transforma o controla aquello que procesa, incluyendo los puntos de acumulación y las tareas necesarias
5. **Elementos compatibles, pero no obligatorios**: Complementos que pueden coexistir con la arquitectura sin definirla, indicando qué función añaden y qué límites tienen
6. **Variantes habituales**: Formas reconocibles de aplicar la misma arquitectura y cambios funcionales que introduce cada variante
7. **Fortalezas, debilidades y críticas**: Ventajas, limitaciones y objeciones conocidas, separando fallos propios de la arquitectura de errores de aplicación
8. **Opiniones extendidas**: Percepciones generalizadas sobre esa arquitectura, documentadas como recepción o debate y no como hechos experimentales
9. **Perspectivas propias**: Síntesis funcional razonada de la documentación, marcada explícitamente como análisis editorial cuando no proceda de una fuente concreta
10. **Ventajas y compromisos frente a otras dimensiones**: Comparación funcional, simétrica y limitada a dimensiones realmente comparables
11. **Aplicación en condiciones particulares**: Consecuencias de la arquitectura en sistemas pequeños, grandes, de baja tecnología u otras condiciones relevantes para ella
12. **Qué no es la dimensión**: Delimitación frente a métodos, componentes, objetivos o resultados que suelen confundirse con ella
13. **Errores comunes al aplicarla**: Fallos de interpretación o de operación que impiden que la dimensión cumpla sus funciones
14. **Función durante el ciclado, la maduración o las transiciones**: Solo cuando la arquitectura tenga consecuencias específicas en esas fases; no sustituye a los documentos operativos correspondientes
15. **Cómo evaluar la dimensión en funcionamiento**: Criterios observables para comprobar procesamiento, circulación, exportación, estabilidad y capacidad
16. **Indicadores que pueden inducir a error**: Señales insuficientes o ambiguas que no deben utilizarse como demostración aislada
17. **Resumen funcional**: Tabla breve con principio, soporte, procesos, exportación, complementos, límites y unidad de evaluación
18. **Contexto histórico, cuando sea necesario**: Referencia breve al origen o evolución de la dimensión, enlazando la ficha correspondiente de `fichas/historia/` en lugar de incorporar un apéndice histórico completo
19. **Fuentes y límites de la evidencia**: Fuentes clasificadas por peso y función, incertidumbres historiográficas y afirmaciones que no pueden darse por demostradas

### Reglas de aplicación de la estructura

- Mantener la definición y el principio antes de entrar en componentes o debates
- Describir primero las funciones del núcleo y después los complementos
- Separar procesamiento, transporte, consumo, almacenamiento y exportación cuando la arquitectura los trate de forma diferente
- Incluir fortalezas y debilidades aunque el balance general de la arquitectura sea favorable
- Reducir las opiniones extendidas a las formulaciones más representativas y no duplicar críticas ya desarrolladas
- Marcar las síntesis propias y distinguirlas de hechos documentados, testimonios históricos y opiniones generalizadas
- Comparar únicamente funciones equivalentes; no mezclar una dimensión con un objetivo de población o con una categoría de uso
- Trasladar el detalle de la aplicación concreta de Veril a sus documentos propietarios, salvo que una consecuencia de la dimensión deba quedar definida aquí
- Omitir una sección cuando no sea pertinente, pero no omitir límites, evaluación o fuentes por razones de brevedad
- Evitar que la plantilla produzca repeticiones: si una explicación pertenece a otra dimensión, enlazarla y conservar solo la consecuencia necesaria

## Configuración vigente

La configuración de Veril debe describirse como un acuario marino mixto cuando la decisión esté vigente. «Mixto» significa que el sistema se diseña para alojar conjuntamente peces y corales, con sus invertebrados compatibles, y no como un sistema fish-only ni como un sistema dedicado exclusivamente a corales.

Al documentar esta configuración, explicar sus consecuencias observables y operativas:

- Compatibilidad entre los animales previstos y el espacio disponible
- Iluminación suficiente y distribuida para los corales compatibles con el sistema
- Circulación que mantenga oxigenación y movimiento sin desplazar el sustrato ni dañar tejidos
- Alimentación y carga orgánica compatibles con peces, corales y capacidad de exportación
- Control conjunto de nutrientes, alcalinidad, calcio, magnesio, salinidad y temperatura
- Introducción gradual de animales y observación de la respuesta del sistema
- Cuarentena o aclimatación según el tipo de animal y el riesgo que se quiera controlar
- Mantenimiento que no optimice una sola función a costa del resto de la comunidad

No convertir «mixto» en una lista de especies, una promesa de compatibilidad universal ni una autorización para introducir animales sin pruebas de capacidad. Las especies, cantidades, parámetros objetivo y fechas deben documentarse en sus documentos propietarios.

## Redacción y evidencia

- Describir primero la configuración vigente y después sus implicaciones
- Separar método general, decisión de Veril, observación, inferencia y pendiente
- No presentar una recomendación de fabricante o una experiencia aislada como requisito universal
- Mantener visibles los límites de volumen, espacio, medición, maduración y capacidad de exportación
- Usar criterios comprobables, como comportamiento de los animales, mediciones, distribución de la luz, zonas de flujo y acumulación de detritos
- Enlazar en lugar de repetir explicaciones completas que pertenezcan a otra ficha

## Documentos propietarios

- Los métodos generales pertenecen a sus fichas correspondientes
- La dimensión biológica, la configuración mixta y sus implicaciones generales pertenecen a `dimension-biologica.md`
- La elección concreta de animales pertenece a las fichas de biología y a la documentación específica de Veril
- La roca, el sustrato, el flujo y la iluminación concretos pertenecen a `veril/`
- El ciclado, la maduración y sus procedimientos pertenecen a `ciclado/`
- Las especificaciones y comprobaciones de equipos pertenecen a `fichas/hardware/`
- El origen y la evolución histórica de métodos y conceptos pertenecen a `fichas/historia/`

## Comprobación antes de terminar

- Confirmar que el documento distingue dimensión de referencia y aplicación a Veril
- Confirmar que la ficha respeta la responsabilidad definida en [modelo.md](modelo.md) y no se comporta como una octava dimensión
- Revisar que las consecuencias del diseño mixto no contradigan las fichas propietarias
- Comprobar que la aplicación concreta queda enlazada en `veril/` y que el compendio temporal no se trata como fuente estructural
- Comprobar los enlaces internos y mantenerlos relativos
- Ejecutar `git diff --check`
