# Reglas locales de Veril

El checkout editable es este repositorio. `proyectos/acuario-veril` es un
enlace simbólico de conveniencia y no una segunda copia. Antes de editar,
compón los `AGENTS.md` de la ruta real, revisa el estado Git y preserva cambios
ajenos. El submódulo `privado/` es otro repositorio y no se publica ni se
indexa por inferencia.

La autoridad de cada dato se separa así:

- `01_verilpedia/`: conocimiento reutilizable y fichas generales de Veril
- `02_configuracion/`: decisiones y configuración vigente de Veril
- `03_pendientes/`: planes aún no ejecutados
- `04_operaciones/`: hechos fechados, resultados, evidencias e incidencias

No promociones una hipótesis, una recomendación, una lectura aislada o un plan
a configuración vigente u operación. Las instrucciones más profundas concretan
esta clasificación. La organización editorial, las fuentes, la autosuficiencia,
las excepciones de hardware y la validación pertenecen a
`veril-documentacion`; no se duplican aquí.

## Privacidad de proyectos 3D

Por instrucción del propietario del 16 de octubre de 2026, y hasta nuevo aviso,
todos los proyectos 3D de Veril se crean y mantienen en el repositorio privado,
salvo excepción explícita suya. El destino de los diseños y su fabricación es
`privado/disenos-3d/`; la reconstrucción espacial del acuario reside en
`privado/reconstruccion-espacial/`.

Esta regla incluye CAD, mallas, escenas, capturas de trabajo, scripts,
simulaciones, perfiles, proyectos de laminado, G-code e informes propios del
proyecto. No se crean copias ni nuevas autoridades de esos proyectos en el
árbol público. Los índices y registros generales pueden enlazar su autoridad
privada sin duplicar el diseño. No se presume autorización para publicarlos.

El propietario autoriza expresamente el 16 de octubre de 2026 preparar
ediciones públicas de los proyectos que vaya indicando, empezando por el
soporte de biobolas. Estas ediciones residen en `03_pendientes/disenos-3d/`
y contienen únicamente el FreeCAD editable consolidado, su README y modelos
3MF neutros para laminar. El desarrollo, los antecedentes, las pruebas y los
perfiles o laminados específicos de impresora permanecen en privado. Las
capturas del modelo destinadas al README pueden incluirse cuando el propietario
las solicite expresamente, como la vista del soporte de biobolas. Esta
excepción no autoriza incorporar otros proyectos ni hacer commit o push.
