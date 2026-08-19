# Normas de edición del repositorio

Estas reglas adaptan al repositorio `veril-docs` las normas editoriales compartidas de [normativa](../normativa/README.md) y las convenciones del repositorio `acuario`.

## Organización y fuentes

- Mantener separadas las fuentes, las decisiones de proyecto, los planes operativos y las fichas reutilizables
- Mantener las decisiones específicas de Veril en `ciclado/` o en la documentación específica del hardware
- Mantener la información general y reutilizable en `fichas/`
- Usar enlaces internos relativos; no enlazar rutas absolutas de otro repositorio
- Conservar la incertidumbre y los pendientes como tales; no convertir hipótesis, publicidad o experiencia aislada en hechos
- No duplicar una explicación completa cuando exista una fuente local equivalente; enlazarla
- Aplicar la regla editorial de que el producto adquirido y su documentación vigente prevalecen sobre una ficha antigua o una fuente secundaria

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

## Fichas

Antes de modificar una ficha, conservar su separación entre información general, aplicación a Veril, pendientes y fuentes. Las fichas de productos no sustituyen a las fichas generales de conceptos, organismos o parámetros, y una recomendación de compra debe quedar diferenciada de la identificación del producto.

## Comprobación antes de terminar

- Revisar ortografía, tildes, nombres científicos, marcas y unidades
- Comprobar que las listas comiencen con mayúscula y no terminen con puntuación prohibida
- Validar los enlaces internos y mantenerlos relativos
- Ejecutar `git diff --check` cuando el repositorio esté bajo control de versiones
- No declarar una revisión terminada sin indicar qué se ha comprobado
