# Normas de edición de las fichas

## Responsabilidad

- Mantener aquí el conocimiento general, las fichas de referencia y la documentación técnica reutilizable del repositorio
- Separar la definición general, la evidencia y los límites de una aplicación concreta en Veril
- Enlazar `02_veril/`, `03_ciclado/`, `04_maduracion/` o `05_operacion/` cuando una decisión pertenezca a esos documentos
- Mantener las categorías y los índices alineados con el orden numérico de lectura

## Límites

- No documentar aquí cantidades, posiciones, fechas, proveedores, dosis ni criterios de aceptación exclusivos de Veril, salvo en una ficha de hardware o producto cuyo estado local deba registrarse explícitamente
- No repetir una explicación completa de otra ficha: conservar solo la consecuencia necesaria y enlazar la fuente propietaria
- No convertir una ficha general en un protocolo operativo
- No presentar una opinión del hobby, una especificación comercial o una experiencia aislada como evidencia suficiente

## Evidencia y redacción

- Separar hechos documentados, especificaciones del fabricante, observaciones independientes, inferencias y decisiones del proyecto
- Priorizar fuentes primarias, revisiones, documentación del método de medición y manuales vigentes según el tipo de afirmación
- Mantener los rangos y recomendaciones como orientativos cuando dependan del sistema, el organismo, el método o la escala
- Usar enlaces relativos y conservar visibles las incertidumbres y los pendientes reales

## Comprobación

- Comprobar que el documento respeta la responsabilidad de su categoría
- Revisar que los enlaces a la aplicación concreta apunten al documento propietario
- Ejecutar la validación de enlaces y `git diff --check` antes de terminar
