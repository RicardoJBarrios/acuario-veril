# Normas de edición del repositorio

Estas reglas adaptan al repositorio `veril-docs` las normas editoriales compartidas de [normativa](../normativa/README.md) y las convenciones del repositorio `acuario`.

## Organización y fuentes

- Mantener separadas las fuentes, las decisiones de proyecto, los planes operativos y las fichas reutilizables
- Mantener las decisiones y el plan específico de ciclado de Veril en `03_ciclado/`, la maduración en `04_maduracion/`, la operación recurrente en `05_operacion/`, las del hardware en su documentación propia y los criterios transversales de configuración en `01_fichas/01_dimensiones/`
- Mantener la información general y reutilizable en `01_fichas/`
- Mantener los conceptos, beneficios, límites y modelos generales de un proceso en `01_fichas/06_procesos/`; reservar `05_operacion/` para los procedimientos concretos de Veril que los aplican
- Mantener la información general de los organismos en `01_fichas/02_biologia/`; documentar las aplicaciones y decisiones específicas en `02_veril/` o en los planes operativos correspondientes
- Usar enlaces internos relativos; no enlazar rutas absolutas de otro repositorio
- Conservar la incertidumbre y los pendientes como tales; no convertir hipótesis, publicidad o experiencia aislada en hechos
- Documentar las opiniones generalizadas, los debates y las críticas extendidas cuando sean relevantes, etiquetándolos como opiniones, percepción del hobby o práctica común y separándolos de los hechos verificados
- No duplicar una explicación completa cuando exista una fuente local equivalente; enlazarla
- Aplicar la regla editorial de que el producto adquirido y su documentación vigente prevalecen sobre una ficha antigua o una fuente secundaria

## Fuentes y referencias externas de interés

- [ReefCalcs](https://reefcalcs.com/): Calculadoras y referencias sobre volumen, sustrato, dosificación, salinidad, iluminación, parámetros y otros aspectos del mantenimiento de acuarios. Puede servir como herramienta de contraste y apoyo práctico; comprobar sus constantes, supuestos y resultados frente a la documentación del fabricante, fuentes primarias y mediciones del sistema antes de convertirlos en decisiones de Veril

## Redacción

- Escribir en español correcto, con tildes, concordancia y puntuación revisadas
- Usar mayúsculas naturales en los títulos, salvo marcas y nombres oficiales
- Escribir los nombres científicos en cursiva cuando corresponda
- Separar especificaciones del fabricante, observaciones independientes, inferencias y decisiones de Veril
- Mantener un tono técnico, claro, prudente y no promocional
- No presentar una narrativa que dependa de que el lector conozca conversaciones o decisiones anteriores
- Tratar todos los documentos como documentación final y autosuficiente: no mencionar decisiones anteriores, alternativas descartadas, versiones previas ni el proceso histórico que llevó a la configuración actual
- Describir únicamente la configuración vigente, sus condiciones, sus límites y los pendientes reales de ejecución
- Definir los términos operativos antes de utilizarlos como criterios de decisión
- Preferir condiciones observables y registrables a calendarios, impresiones visuales o cifras sin contexto

## Listas

- Cada elemento comenzará con mayúscula, incluida la primera palabra significativa después de negrita, código, casillas o etiquetas Markdown
- Los elementos no terminarán en punto, coma ni punto y coma
- La regla se aplica a listas con viñetas y listas numeradas
- Las listas conservarán la puntuación propia de los bloques de código, citas literales, enlaces y denominaciones oficiales cuando sea significativa

## Markdown de GitHub

Se pueden utilizar las extensiones de GitHub Flavored Markdown cuando mejoren la comprensión o la trazabilidad del documento:

- Usar Tablas para comparar métodos, componentes, variantes, parámetros o evidencias
- Usar Notas al pie para definir términos, añadir precisiones breves o conservar límites de una fuente sin interrumpir la explicación principal
- Usar Listas de tareas con `- [ ]` y `- [x]` para pendientes y comprobaciones operativas reales
- Usar Alertas de GitHub (`> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]` y `> [!CAUTION]`) solo cuando la información sea especialmente relevante al leer en diagonal
- Usar Emojis con moderación y únicamente cuando aporten una señal semántica clara, como el estado de una tarea o el tipo de advertencia
- Usar Bloques de código con lenguaje declarado, fórmulas, diagramas o expresiones matemáticas cuando faciliten la reproducción o la verificación
- Usar Mermaid, en la variante adecuada, para representar flujos, secuencias, dependencias, cronologías, estados, arquitecturas o relaciones que resulten más claras de forma gráfica
- Usar `<details>` para ocultar material secundario extenso sin ocultar decisiones, riesgos, fuentes o pendientes importantes
- Mantener el documento legible también como texto Markdown sin renderizar y no sustituir una explicación necesaria por un recurso visual
- No encadenar alertas ni convertir cada pendiente, definición o párrafo en un elemento decorativo

## Fichas

Antes de modificar una ficha, conservar su separación entre información general, aplicación a Veril, pendientes y fuentes. Las fichas de productos no sustituyen a las fichas generales de conceptos, organismos o parámetros, y una recomendación de compra debe quedar diferenciada de la identificación del producto.

## Comprobación antes de terminar

- Revisar ortografía, tildes, nombres científicos, marcas y unidades
- Comprobar que las listas comiencen con mayúscula y no terminen con puntuación prohibida
- Validar los enlaces internos y mantenerlos relativos
- Ejecutar `git diff --check` cuando el repositorio esté bajo control de versiones
- No declarar una revisión terminada sin indicar qué se ha comprobado
