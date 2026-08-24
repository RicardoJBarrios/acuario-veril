# Normas de edición de las dimensiones

## Responsabilidad

- Documentar las siete dimensiones adoptadas para Veril como perspectivas funcionales de una única configuración
- Mantener una ficha general por dimensión y su aplicación concreta, con numeración compartida entre `01_dimensiones/` y `02_veril/`
- Explicar en cada dimensión qué debe tenerse en cuenta, por qué importa, qué variante se adopta y cómo se comprobará
- Tratar la operación como capa transversal, no como una octava dimensión

## Límites

- Ceñir cada documento a la dimensión que le da nombre y documentar solo sus consecuencias sobre las demás
- Incluir teoría general únicamente cuando sea necesaria para explicar una función, un límite o un criterio de evaluación de esa dimensión
- No convertir una dimensión en una guía general de acuariofilia, una ficha de hardware, una ficha de organismo o un plan operativo
- No repetir la configuración concreta de Veril: enlazar su ficha equivalente en `02_veril/`
- No repetir detalles de parámetros, biología, hardware, ciclado, maduración u operación cuando exista una ficha propietaria

## Estructura y evidencia

- Mantener una progresión comprensible desde definición y principio hasta aplicación, límites y evaluación
- Incluir solo las secciones pertinentes; la estructura no es un índice rígido
- Separar fortalezas, debilidades, críticas, opiniones generalizadas y síntesis propia
- Comparar únicamente funciones equivalentes y evitar presentar una variante como regla universal
- Describir criterios observables, medibles y registrables en lugar de proxies aislados
- Enlazar la historia en `01_fichas/07_historia/` cuando sea relevante, sin convertir la ficha en un apéndice histórico

## Comprobación

- Confirmar que la variante adoptada y su aplicación están explícitas
- Confirmar que la ficha no invade otra dimensión
- Comprobar que la numeración coincide con la ficha de `02_veril/`
- Validar enlaces internos y ejecutar `git diff --check`
