# Rebose regulable y pantalla entre C2 y C3

Revisión CAD del 11 de octubre de 2026. Estado: **prototipo paramétrico revisado
para reducir soportes en impresión invertida**. Laminado de estructura, placa
y probeta generado y comprobado; encaje físico y comportamiento hidráulico
pendientes.

## Función e interfaces

Según las medidas indicadas por el propietario, el separador entre C2 y C3
tiene 6 mm de grosor y su canto está 50 mm por debajo del borde del acuario.
El agua pasa por encima del canto hacia C3. El propietario observa un nivel de
agua aproximado de 45 mm bajo el borde. La causa de ese nivel no está determinada.

La estructura se apoya sobre el separador y contiene dos guías para una placa
intercambiable. La placa tendrá 2,4 mm de grosor, igual al espesor de pared de
este modelo. Cambiar su altura pretende modificar la cota del rebose. La
pantalla posterior conserva un canal de bajada de 12 mm como propuesta de
separación de burbujas. Estas funciones aún no se han comprobado con agua.

## Geometría revisada

La fuente editable es [rebosadero.FCStd](rebosadero.FCStd). Se ha modificado el
documento existente, conservando `Pad001` y su simetría `Mirrored`, que forman
las guías originales.

| Parámetro | Valor CAD |
| --- | ---: |
| Ancho total | 139 mm |
| Espesor de paredes y placa intercambiable | 2,4 mm |
| Alojamiento nominal del vidrio | 6 mm |
| Columnas interiores de la ventana | 10 |
| Espesor y profundidad de cada columna | 2,4 × 2,4 mm |
| Aberturas entre columnas | 11 |
| Ancho de cada abertura | 9,582 mm |
| Pendiente de cierre de las aberturas | 45° |
| Pinzas extremas | 2, de 4,8 mm de ancho |
| Retranqueo lateral bajo el canto para silicona | 3,5 mm por extremo |
| Pendiente de cartelas de pinza | 45° |
| Longitud de la pantalla posterior | 176 mm |
| Envolvente completa | 139 × 25,2 × 178,4 mm |

Las columnas y los cierres inclinados están detrás de la placa. Su cara
frontal permanece en Y=8,4 mm y no invade el alojamiento entre las guías.
Los cierres inclinados eliminan el puente horizontal largo de esa ventana
en la orientación invertida. Sin placa, la ventana conserva aproximadamente
3.458 mm² de área abierta, el 75,9 % de sus 4.555 mm² originales. Esta cifra
geométrica no demuestra capacidad hidráulica ni ausencia de obstrucciones.

La longitud de pantalla se ha reducido de 180 a 176 mm, acortando únicamente
su extremo inferior. La altura completa baja de 182,4 a 178,4 mm para quedar
dentro de los 180 mm nominales de la Kingroon KP3.

Las nuevas operaciones son diez cajas aditivas `WindowColumn01`–`WindowColumn10`
y `WindowClosingSketch` con su extrusión `WindowClosingPad`. El sketch nuevo
está completamente restringido. Las dimensiones y posiciones dependen de
`data` mediante expresiones. La celda B11 describe las diez operaciones de
columna existentes: cambiar su número requiere editar también las operaciones
y el perfil de cierre. B12 calcula la luz y B13 referencia el grosor de placa.

La pinza continua se ha sustituido por dos pinzas extremas de 4,8 mm de ancho.
Los vaciados `CentralClipClearance` y `GateToGlassClearance` retiran su parte
central y dejan que la placa apoye directamente sobre el canto del vidrio.
No hay suelo añadido bajo las guías. La placa intercambiable conserva su forma
rectangular. `ClipRampSketch`, su extrusión
`ClipRampPad` y la simetría `ClipRampMirror` añaden cartelas a 45° fuera del
recorrido de la placa. La abertura nominal de 6 mm para el vidrio se conserva.
Se elimina así el voladizo horizontal largo de la pinza para la orientación
invertida.

La cota libre original de la pestaña retenedora, de 1,666031 mm, se ha fijado
sin cambiar su geometría. `Sketch002` y el sketch de las cartelas quedan
completamente restringidos. B14 gobierna ese espesor y B15 calcula el inicio
del canal de placa.

Para salvar la silicona de las esquinas, estimada por el propietario en 2–3 mm,
se ha adoptado una holgura inicial de 3,5 mm por extremo. Es una decisión de
prototipo con margen nominal de 0,5 mm sobre la estimación máxima, no un encaje
físico confirmado. La celda B16, alias `siliconeClearance`, gobierna la holgura.

`SiliconeReliefRight` y `SiliconeReliefLeft` retiran los extremos delanteros y
posteriores de la pinza únicamente por debajo del canto, entre Z=0 y Z=24 mm.
`OldFrontFingersRemoval` retira los dedos delanteros de su posición anterior.
Las pinzas delanteras nuevas, `InwardFrontFingerRight` y `InwardFrontFingerLeft`,
conservan 4,8 mm de ancho y se sitúan 3,5 mm hacia el interior. En el lado derecho
ocupan X=61,2–66 mm y en el izquierdo X=−66–−61,2 mm.

Los apoyos `InwardClipCapRight/Left` y las pestañas `InwardFrontGuideRight/Left`
prolongan la parte frontal de las guías para unirla a las pinzas desplazadas.
La prolongación queda por delante del canal de la placa y no ocupa su recorrido.
`InwardClipRampSketch`, su extrusión y su simetría conservan la transición a
45° para la impresión invertida. El sketch está completamente restringido.
El arranque de la cartela prolongada coincide con el de la pestaña frontal:
X=61,2 mm en el lado derecho, con simetría en el izquierdo. La cartela cubre
el borde completo, sin el desfase lateral de 0,25 mm corregido en esta revisión.
La zona superior conserva toda la geometría previa y los 139 mm de ancho,
sin prolongar los rebajes de silicona por encima del canto.

## Comprobaciones de CAD

- La estructura es un único sólido válido, sin errores de recomputación,
  de 78.678 mm³ aproximadamente.
- Una placa geométrica de comprobación de 133,6 mm de ancho y 2,4 mm de grosor,
  situada entre Y=5,6 y Y=8,0 mm, no interseca el soporte para alturas de 5,
  10, 20, 35,2 y 45 mm, en posiciones elevadas 0, 10 y 50 mm desde el canto
  del vidrio (Z=24 mm).
  Son posiciones de comprobación, no alturas de uso recomendadas ni una
  simulación continua de la extracción. La revisión actual añade la placa de 20 mm
  descrita a continuación como cuerpo independiente.
- Las dos zonas de holgura lateral, de 3,5 mm de ancho bajo el canto, no
  contienen material del soporte. No se ha retirado volumen de la geometría
  previa en Z≥24 mm.
- Una variante temporal de holgura de 3 mm y otra de ancho total de 137 mm
  recalcularon como un único sólido válido. Se restauraron los 139 mm de ancho
  y 3,5 mm de holgura antes de guardar.

La placa apoya directamente sobre el canto del vidrio en Z=24 mm. Para una
placa de altura h, su borde queda geométricamente h por encima del canto
original. El nivel real también depende del caudal, las
fugas por las holguras y la geometría de paso alrededor del marco.

## Placa intercambiable de 20 mm

En el mismo FCStd se ha creado `GatePlateBody`, un Body independiente de la
estructura, con la caja aditiva nativa `GatePlate`. Sus dimensiones son
**133,6 mm de ancho × 20 mm de alto × 2,4 mm de grosor**. Se muestra montada,
con el borde inferior en Z=24 mm, sobre el canto del vidrio. Es un sólido
válido de 6.412,8 mm³, separado de la estructura y sin intersecciones con ella.

La ranura tiene 134,2 mm de ancho y 3,134 mm de profundidad. La placa deja
0,3 mm de holgura por extremo en X y aproximadamente 0,367 mm por cara en Y.
La posición está centrada en el canal, en Y=5,633–8,033 mm. Las cotas y la
posición dependen de `data`: B17 (`gateHeight`) define la altura de 20 mm;
B18 (`gateSideClearance`) define la holgura lateral de 0,3 mm; B13 mantiene
el grosor. La placa apoya directamente en el vidrio, sin suelo añadido.

Se han comprobado posiciones de extracción a 0, 10, 40 y 60 mm por encima de
la posición montada, sin intersección con la estructura. El soporte conserva
su volumen y geometría anteriores. Estas comprobaciones no sustituyen la
prueba de deslizamiento de las piezas impresas.

El requisito indicado por el propietario es dejar al menos 20 mm entre el
agua y el borde del acuario. Esta placa deja su cresta 30 mm bajo el borde;
el nivel real será más alto que la cresta según el caudal. Debe verificarse
que esa elevación no supere 10 mm. Quedan 17,6 mm de abertura hasta la parte
inferior del travesaño superior. Una placa de 25 mm requeriría verificar que
la elevación del agua sobre su cresta no supera 5 mm.

Para laminar esta placa, la orientación prevista es con su cara ancha
133,6 × 20 mm contra la cama y 2,4 mm de altura impresa. El encaje y el nivel
resultante siguen pendientes de prueba física.

## Probeta de silicona del extremo derecho

Se ha creado `SiliconeCoupon`, una intersección nativa de Part entre el sólido
final de la estructura y `SiliconeCouponCrop`. La probeta conserva exactamente
la geometría del extremo derecho: pinza delantera completa, apoyo posterior,
cartela y borde lateral superior. Su envolvente es **9,5 × 10,8 × 31 mm** y
su volumen aproximadamente 1.032 mm³. Es un único sólido válido. El recorte
ocupa X=60–69,5, Y=0–10,8 y Z=0–31 mm en el modelo original.

El rebaje exterior de **3,5 mm** se conserva únicamente bajo el canto del
vidrio, entre Z=0 y Z=24 mm. Por encima conserva el borde original, que sirve
como referencia para aproximar la probeta al lateral real del acuario. La
abertura para el vidrio mantiene los 6 mm del modelo; el propietario indica
que ese encaje ya se ha comprobado en otra impresión. Esta probeta se destina
a comprobar el espacio para la silicona, no a recalibrar ese encaje.

`SiliconeCouponDisplay` es un enlace de visualización, desplazado 30 mm en X
y mostrado en naranja para distinguir la probeta del conjunto. El recorte
original y su caja auxiliar permanecen ocultos; no se modifica la estructura.

El derivado [rebosadero-probeta-silicona-derecha.stl](rebosadero-probeta-silicona-derecha.stl)
contiene únicamente la probeta, invertida con su parte superior contra la
cama y trasladada al origen. La malla es cerrada. El laminado está generado en [rebosadero-impresion](rebosadero-impresion/README.md);
la impresión está pendiente. Probar en la esquina derecha real: debe apoyar sobre el
canto y aproximarse al lateral sin apretar, arrastrar ni rozar la silicona.
Si no asienta libremente, detener el montaje y revisar el rebaje.

## Fabricación y validación

La orientación prevista es invertida, con la parte superior original contra
la cama. Las aberturas y las cartelas de las pinzas crecen progresivamente a
45°. Se han eliminado los voladizos largos de la ventana y de la pinza.
El laminado actual usa soportes desactivados y sus trayectorias se han revisado.
La impresión real sin soportes todavía requiere comprobar las pendientes y
puentes con la bobina y máquina concretas.

Antes del uso, comprobar el montaje sobre el vidrio, la inserción y extracción
de las placas impresas, la retirada de soportes y el paso de agua con el caudal
real. Verificar que los rebajes salvan la silicona real sin rozarla, incluyendo
su posible abultamiento junto al canto. Verificar también el nivel resultante,
el margen al borde, las fugas
alrededor de la placa y la eficacia de la pantalla frente a las burbujas.
Los STL, proyectos de Orca, G-code separados y el informe de parámetros,
estimaciones y comprobaciones están en
[rebosadero-impresion/README.md](rebosadero-impresion/README.md). Se ha conservado
el CAD original. No se ha iniciado ninguna impresión.
