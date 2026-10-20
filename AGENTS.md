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

## Registro de actuaciones comunicadas por el propietario

Por instrucción del propietario del 19 de octubre de 2026, cuando pida apuntar
algo que ha hecho, registra únicamente lo que haya comunicado expresamente.
No completes el relato con acciones, condiciones, motivos, resultados ni
comprobaciones supuestos. No añadas frases como «no ha indicado X», «no consta
Y» o «pendiente de confirmar» sobre aspectos que no haya mencionado.

Si una duda afecta a la fidelidad del registro, pregunta antes de documentar
el punto dudoso. Si un dato no es necesario para registrar lo comunicado,
omítelo sin convertir su ausencia en contenido del documento. Una consulta
de telemetría o de documentación previa no autoriza a ampliar el relato del
propietario; cualquier ampliación del encargo debe consultarse antes.

Antes de guardar, contrasta cada afirmación del registro con lo comunicado por
el propietario y elimina cualquier añadido sin respaldo en su relato.

### Home Assistant y límites de la asistencia

Al registrar actuaciones, incorpora las lecturas pertinentes de Home Assistant
cuando corresponda, identificadas como telemetría y con su momento de lectura.
Esto no autoriza a deducir acciones físicas, motivos ni resultados.

El acceso local a Home Assistant está previsto en `home-assistant-operaciones`:
usa el MCP disponible o la API autenticada mediante su script documentado.
La falta de una herramienta cargada, una variable en la sesión o conocimiento
del procedimiento no justifica afirmar que no se puede acceder: consulta las
instrucciones y utiliza la vía documentada antes de concluir nada.

Por instrucción del propietario del 19 de octubre de 2026, no le comuniques
que no puedes acceder salvo que hayas comprobado un problema real de red.
Si la consulta falla realmente, omite del registro las lecturas no obtenidas
y los comentarios sobre su ausencia o sobre el fallo de acceso. No inventes
valores ni presentes lecturas antiguas como actuales.

En estos registros, limita la asistencia a documentar hechos comunicados y
lecturas obtenidas. No añadas juicios de valor, interpretaciones, valoraciones
de corrección o seguridad, recomendaciones, decisiones ni pendientes propios,
salvo petición expresa del propietario. Las decisiones corresponden al
propietario. Esta instrucción prevalece sobre las indicaciones de las skills
que pidan añadir interpretaciones o dejar constancia de telemetría ausente.

## Investigaciones y trabajo local

Las investigaciones de fuentes y sus procesos intermedios pertenecen al espacio
privado externo `../acuario-veril-local/`, por decisión del propietario del
19 de octubre de 2026. Aplica la regla «Investigación privada y procesos
intermedios» de `veril-documentacion` antes de recuperar o generar ese material.

## Proyectos 3D locales

Por instrucción expresa del propietario del **19 de octubre de 2026**, el desarrollo de
los diseños 3D de Veril se crea y mantiene en el espacio hermano local
`../acuario-veril-local/`: diseños y fabricación en `disenos-3d/`, y
reconstrucción espacial en `reconstruccion-espacial/`.

Esta decisión sustituye los destinos anteriores de desarrollo en `privado/`.
Incluye CAD, mallas, escenas, capturas, scripts,
perfiles, laminados, G-code e informes. No se crean copias ni enlaces simbólicos
desde el árbol público al espacio local. No se publican ni se indexan por
inferencia. El traslado local no elimina versiones del historial Git ni
autoriza commit o push.

Por aclaración expresa del propietario del **20 de octubre de 2026**, la carpeta
pública `03_pendientes/disenos-3d/` se conserva tal cual, con sus ediciones
seleccionadas. Esta excepción no traslada el desarrollo local al árbol público
ni autoriza añadir nuevos proyectos, hacer commit o push.
