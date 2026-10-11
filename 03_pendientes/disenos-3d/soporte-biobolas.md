# Soporte modular de biobolas y tapa de suspensión

Revisión CAD y laminado del 11 de octubre de 2026. Estado: **probetas impresas;
el primer prototipo de tapa se rompió al retirar sus soportes; la variante
base-en-cama está laminada y pendiente de impresión y prueba de carga**. El
conjunto funcional no está aceptado ni representa una instalación validada en
Veril.

## Objetivo y referencias

Cada módulo es una pieza monolítica para 20 biobolas Mantis, distribuidas en
cuatro mástiles X con cinco bolas por mástil. Dos módulos idénticos e
intercambiables reúnen las 40 bolas adquiridas. El primer prototipo de tapa se
imprimió, pero se rompió durante la retirada de los soportes, según comunica el
propietario. Se conserva el laminado fallido y se ha preparado una variante
paramétrica separada para imprimir con la base sobre la cama y sin soportes.

Se conservan la altura de bola de 29 mm elegida por el propietario, el diámetro
exterior de 31 mm y el paso lateral de 36,5 mm. El peso declarado es de unos
25 g por bola: el módulo inferior añade aproximadamente 500 g de cerámica a
su propio peso, que deberá medirse tras imprimirlo. La tapa futura soportará
ambos módulos, aproximadamente 1 kg de cerámica más las piezas impresas.

El agujero de referencia es Ø10,5 mm. El sketch existente de la biobola usa
radio interior de 5,5 mm, equivalente a Ø11 mm. La probeta conserva Ø10,5 mm
como referencia y debe contrastarse con las bolas reales, que pueden variar.

## Fallo identificado y solución

El diseño anterior dejaba los labios debajo del techo del receptor. Al
suspender el conjunto, el módulo inferior se desplazaba hacia abajo y sus
labios se alejaban del techo. La prueba CAD permitía separar los módulos
0,4, 1 y 4 mm sin colisión. La ausencia de intersecciones en reposo no
demostraba retención axial.

La revisión utiliza cuatro ganchos exteriores integrados: dos orientados en X
y la pareja añadida en Y. Cada gancho atraviesa su ventana correspondiente del
módulo superior. Sus caras inferiores quedan **por encima de los hombros
portantes de la base superior**. Tras consumir 0,3 mm de juego axial, esas
caras apoyan sobre los hombros e impiden la extracción hacia abajo. Los cuatro
tetones y alojamientos conservan la función de alineación; no se atribuye la
retención a su fricción.

El recorrido de carga es: bolas → apoyos y bastidor inferior → montantes
laterales → lengüetas y ganchos X/Y → hombros del módulo superior → bastidor
superior. La superficie de contacto nominal suma 28,8 mm² si los cuatro
ganchos llegan a apoyar por igual; el CAD no demuestra ese reparto real de
carga.

![Sección de la unión: inferior naranja y superior azul](soporte-biobolas-union-seccion.png)

El corte muestra el gancho del módulo inferior en naranja y el receptor
superior en azul. Los fragmentos azules están conectados por paredes laterales
fuera del plano de corte. La cara inferior horizontal del gancho apoya sobre
el bloque azul exterior, a la derecha de la ventana.

## Parámetros e implantación

La hoja `SupportParameters` gobierna las dimensiones de la unión. Los dos
perfiles de gancho son sketches completamente restringidos, extruidos con
operaciones nativas de PartDesign. Los radios se aplican al final.

| Parámetro | Valor de esta revisión |
| --- | ---: |
| Longitud flexible nominal | 18 mm |
| Espesor y anchura de lengüeta | 1,8 × 8 mm |
| Proyección del diente | 1,8 mm |
| Radio en la raíz del diente | 1,0 mm |
| Rampa respecto a la dirección vertical de inserción | 35° |
| Espesor del hombro portante | 3 mm |
| Ventana radial × tangencial | 4,2 × 8,6 mm |
| Holgura axial en reposo | 0,3 mm |
| Desplazamiento de cabeza para liberar | 1,2 mm hacia dentro |
| Superficie horizontal de contacto por gancho | 0,9 × 8 = 7,2 mm² |
| Holgura entre la bola superior y el módulo siguiente | 2 mm |
| Paso entre módulos | 150 mm |
| Envolvente de una pieza | 81 × 81 × 155,871 mm |
| Altura de dos módulos ensamblados | 305,871 mm |

El conjunto se sitúa junto al vidrio derecho de C1: `assemblyCenterX = 29 mm`
alinea nominalmente el extremo del soporte con la cara interior del vidrio en
`X=69,5 mm`. En Y permanece centrado, dejando 2 mm hasta cada vidrio frontal y
trasero. Las bolas conservan unos 6,75 mm de separación respecto al vidrio
derecho. Esta tangencia CAD es para la visualización; no incorpora tolerancia
de montaje ni silicona. La base comienza a 25 mm del fondo: se ocupa parte del
hueco inferior inicialmente previsto de 50 mm, conforme a la autorización del
propietario. El punto más alto queda a 330,871 mm del fondo, con 22,129 mm
hasta el nivel de agua de 353 mm. Las bolas ocupan Z=28–173 mm y Z=178–323 mm.

El paso incluye 3 mm de base, 145 mm de apilamiento de bolas y 2 mm de holgura
superior. Los cuatro tetones se elevan con el paso y los postes de guiado se
prolongan para mantener su unión. Los ganchos también suben mediante sus
parámetros derivados, conservando el apoyo de 0,3 mm sobre el hombro receptor.

La separación lateral nominal entre bolas sigue siendo de 5,5 mm. Las bases
mantienen la estructura abierta. La tapa aún no está incluida en estas cotas.

Los brazos de los cuatro mástiles quedan orientados a 0° y 90° en planta,
alineados con los nervios de la base. El giro anterior de 45° hacía que el
arranque pareciera desplazado, aunque los ejes ya estaban centrados. Sus
posiciones ahora dependen mediante expresiones de los centros de esos nervios:
se conservan los ejes X/Y = ±18,25 mm y la sección de dos brazos de 8,5 × 2 mm.
La probeta del mástil reproduce esta misma orientación. Se mantiene un
solapamiento de 0,2 mm entre el arranque y la base para asegurar la unión sólida.

Se han retirado las doce barras elevadas `SphereSeat`: eran tres barras
centradas por columna, no tres apoyos radiales exteriores. Sus extremos
formaban los salientes alrededor del pie y quedaban dentro del agujero de la
bola del modelo. El apoyo inferior se conserva sobre los nervios abiertos de
la base, alineados con el mástil. Las cuatro bolas inferiores tienen distancia
CAD cero al soporte sin intersección volumétrica. El contacto con la cerámica
real y su estabilidad siguen pendientes de la prueba física.

## Comprobación geométrica

Las siguientes observaciones proceden del modelo recomputado en FreeCAD:

- El módulo es un único sólido válido, con volumen de 57,780 cm³ y altura
  inferior a los 180 mm de la Kingroon KP3
- Las representaciones auxiliares contienen 20 bolas por módulo y no
  presentan intersección volumétrica con sus soportes
- En la posición de visualización actual, el soporte ocupa X=−11,5–69,5 mm y
  Y=−40,5–40,5 mm: queda tangente a la cara interior del vidrio derecho y
  dentro de la envolvente interior de C1. Las bolas terminan en X=62,75 mm
- Las cuatro bolas superiores del módulo inferior tienen 2 mm de distancia CAD
  al módulo superior, sin intersección volumétrica
- Los módulos ensamblados no se intersecan en la posición de reposo
- Un intento de separación axial de 0,4 mm produce cuatro zonas de solapamiento
  en los ganchos X/Y, con volumen total de 1,488 mm³: esa posición sería
  impedida por los topes. Una separación de 1 mm también queda bloqueada
- La probeta de un solo cierre también está libre en reposo, bloquea el
  intento de separación de 0,4 mm y permite la retirada comprobada a 3 mm
  con la cabeza desplazada hacia dentro

El radio de raíz de los ganchos se aumentó de 0,6 a 1,0 mm para suavizar la
transición de los brazos flexibles. La pareja nueva en Y usa sketches
restringidos y operaciones nativas de PartDesign, con los mismos parámetros de
los perfiles X. Con los cuatro cierres, el módulo recalcula como un sólido
válido, los módulos no se intersecan en reposo y el desplazamiento axial de
0,4 mm queda bloqueado con 1,488 mm³ de solapamiento CAD en cuatro zonas. La
prueba de retirada con la cabeza desplazada 1,2 mm hacia dentro se documentó
con el radio anterior y debe repetirse con la probeta actualizada. El cambio no
demuestra resistencia a fatiga ni mejora mecánica física; ambas requieren
impresión y ensayo.

La prueba de liberación traslada rígidamente la cabeza recortada para comprobar
espacio disponible. No simula la deformación elástica de la lengüeta, la fuerza
de accionamiento, las tensiones ni la resistencia del PETG impreso.

## Fabricación y resultados de las probetas

Material de las recetas preparadas: PETG, boquilla de 0,4 mm. El módulo se
imprime verticalmente con la base sobre la cama, como una sola pieza. El paquete
reúne probetas de mástil, agujero Ø10,5 mm, gancho macho, receptor y dos peines
de ajuste para el vidrio. El usuario confirma que ha impreso todas las pruebas
y comunica los siguientes resultados físicos (11 de octubre de 2026):

- La ranura de 6,00 mm entra en el vidrio con un margen muy estrecho y ajuste
  satisfactorio. Se adopta como referencia de la interfaz desnuda para este
  ejemplar de vidrio, PETG y proceso de impresión; no se extrapola como
  tolerancia universal.
- El mástil entra correctamente tanto en el agujero circular como en una
  biobola real.
- La presilla y su encaje con el receptor funcionan correctamente.

No se han comunicado medidas con calibre, número de ciclos, fuerza de montaje
ni ensayo de carga. Por ello los resultados validan cualitativamente esos
encajes individuales, no la resistencia, repetibilidad ni vida útil de las
uniones.
Las probetas de cierre representan un cierre individual; no ensayan una carga
repartida entre cuatro cierres ni el montaje completo con los cierres X/Y.
Las probetas macho y receptor reproducen el hombro, la ventana, la rampa y el
radio del modelo revisado, con agujeros Ø3 mm para sujeción durante las pruebas.
El primer peine de cristal tiene ranuras de 7, 8 y 9 mm. La referencia de 9 mm
presupone vidrio nominal de 6 mm, almohadillas de 1 mm por cara y 0,5 mm de
juego por cara; la de 7 mm evalúa el vidrio desnudo. La ranura de 7 mm presentó
juego. La segunda serie tiene ranuras de 6,00, 6,25 y 6,50 mm; la ranura de
6,00 mm entra en el vidrio real con margen muy estrecho y ajuste satisfactorio.
El espesor exacto del vidrio no se midió con instrumento de precisión. Este
resultado conserva 6 mm como referencia nominal para la interfaz desnuda y la
combinación ensayada, pero no valida la silla completa: los peines no incorporan
su acolchado ni ensayan rigidez, reacciones al giro o carga suspendida.

Antes de imprimir y usar el conjunto completo:

1. Las probetas ya están impresas y los encajes comunicados arriba funcionan.
   Revisar en las piezas impresas el voladizo de la cara portante y el puente
   del receptor, además de la retirada de soportes.
2. Confirmar inserción vertical, enclavamiento y liberación manual. La carga
   debe apoyar en las caras horizontales y no mantener la lengüeta presionada
   hacia dentro. Comprobar que no aparece apertura espontánea al tirar
3. Como prueba inicial propuesta, someter el cierre de la probeta a 1 kg
   durante 10 minutos y repetir montaje/desmontaje. Registrar el resultado y
   cualquier marca, blanqueamiento, grieta o deformación residual
4. Tras aceptar el encaje individual, probar la unión completa a cuatro cierres
   fuera del acuario. Se propone una carga de comprobación de 2 kg durante 10 minutos,
   seguida de comprobación con las 20 bolas y de evaluación bajo carga en
   ambiente húmedo. Estas pruebas aún no se han ejecutado

La carga axial de los montantes y lengüetas solicita la unión entre capas FDM.
El CAD no aporta una resistencia admisible ni certifica comportamiento a largo
plazo, fluencia del PETG o fatiga tras ciclos de accionamiento. La tapa y su
unión necesitarán su propia comprobación con la carga total suspendida.

## Tapa superior: revisión del prototipo CAD

La primera tapa presentaba un fallo de retención: el recorte de la base a
75 × 75 mm eliminaba los hombros exteriores de los receptores. En el CAD,
bajar el módulo superior 0,4 mm respecto a esa tapa no encontraba un tope. Se
ha sustituido por una base con los **cuatro receptores completos**, reproducidos
mediante operaciones nativas de PartDesign y las expresiones de
`SupportParameters`. Con la base corregida, ese desplazamiento genera cuatro
zonas de solapamiento, con un volumen total de 1,488 mm³. Es una comprobación
de retención geométrica; no demuestra resistencia mecánica.

La tapa incorpora dos escuadras en el plano XZ, alineadas con los nervios del
bastidor en Y=±18,25 mm. Cada escuadra tiene una pestaña inferior continua,
un montante de 10 × 8 mm y una cartela amplia. Las transiciones de las cartelas
llevan radio de 3 mm. Ambas escuadras se unen a una silla sobre el canto del
vidrio derecho, con un puente de 8 mm de espesor y 60 mm de longitud de apoyo
en Y. El recorrido de carga es: ganchos del módulo superior → receptores de la
tapa → bastidor reforzado → escuadras con cartelas → puente acolchado → canto
del vidrio.

La posición del peso hacia el interior genera un momento de giro. Tomando
solo el kilogramo declarado de cerámica, su centro en X=29 mm y el centro
nominal del canto en X=72,5 mm, resulta aproximadamente
9,81 N × 0,0435 m = **0,43 N·m**. El peso de las piezas impresas incrementará
esa demanda. Los dos apoyos interiores bajos y el apoyo exterior alto deben
reaccionar a ese momento: **no son simples estabilizadores**. Se representan
con almohadillas separadas, sin un apriete deliberado sobre el vidrio.

El asa está centrada sobre la torre en X=29 mm, Y=0 mm. Su plano es XZ y permite
introducir los dedos desde delante o detrás. La abertura bajo el tramo de
agarre mide 40 mm de ancho; su cara inferior está a Z=378 mm, 25 mm por encima
del nivel nominal del agua. El punto superior del asa está a Z=386 mm, por
debajo del borde de la urna. Los cantos del agarre llevan radio de 2 mm. Al
levantar, el esfuerzo se aplica sobre el centro de las biobolas y se transmite
al bastidor mediante un travesaño central reforzado.

`LidAssembly` es un único sólido válido. Su envolvente es X=−11,5–83 mm,
Y=−40,5–40,5 mm y Z=325–399 mm. Los perfiles de las dos escuadras y del asa
están completamente restringidos. La hoja `LidParameters` gobierna las cotas
del vidrio, el apoyo, las secciones y el agarre. La base ya no contiene una
forma recortada estática. Los objetos de `LidContactPads` son volúmenes de
referencia del acolchado y quedan separados del cuerpo imprimible.

| Parámetro del prototipo revisado | Valor CAD |
| --- | ---: |
| Grosor nominal del vidrio | 6 mm |
| Juego lateral de referencia por cara | 0,5 mm |
| Espesor de almohadilla de referencia | 1 mm |
| Longitud de apoyo sobre el canto en Y | 60 mm |
| Sección de cada montante | 10 × 8 mm |
| Espesor del puente sobre el canto | 8 mm |
| Radio de las transiciones de cartela | 3 mm |
| Abertura libre bajo el agarre | 40 mm |
| Cara inferior y superior del agarre | Z=378 / 386 mm |
| Envolvente de la tapa | 94,5 × 81 × 74 mm |

El grosor nominal de 6 mm y el canto a Z=390 mm proceden del modelo de C1. La
probeta de 6 mm ha entrado en el vidrio real con margen muy estrecho, pero no se
midió el espesor con instrumento de precisión. La nueva abertura de 6,5 mm no
se ha probado todavía en la silla de la tapa. El primer prototipo se imprimió,
pero se rompió al retirar sus soportes; la variante actual aún debe imprimirse.
Después habrá que revisar el contacto con el vidrio y ensayar el conjunto
completo fuera del acuario con la carga real y las reacciones al giro. El CAD no
determina la resistencia del vidrio ni del PETG impreso, su fluencia o cómo se
reparte la carga entre los cuatro cierres.

### Variante paramétrica para imprimir la tapa sin soportes

El propietario comunicó una abertura interior de 9 mm en el gancho sobre el
cristal. Confirmó que no instalará almohadillas y pidió dejar 6,5 mm para el
vidrio nominal de 6 mm. El archivo original
[soporte-biobolas.FCStd](soporte-biobolas.FCStd) queda intacto. El derivado
[soporte-biobolas-tapa-fdm.FCStd](soporte-biobolas-tapa-fdm.FCStd) modifica la
hoja `LidParameters` y elimina del duplicado los volúmenes de referencia de
acolchado:

| Parámetro de la variante | Valor |
| --- | ---: |
| Grosor nominal de vidrio | 6 mm |
| Almohadilla | 0 mm; sin acolchado |
| Holgura por cara | 0,25 mm |
| Abertura interior resultante | 6,5 mm |
| Grosor de la pared exterior del gancho | 3,2 mm, antes 6 mm |
| Borde inferior de las cartelas | 325 mm, alineado con `seatZ` |
| Envolvente de la pieza | 90,45 × 81 × 73 mm |

La pared de 3,2 mm es una primera reducción candidata, todavía sin ensayo de
carga. Alinear el borde inferior de las cartelas con el plano de la base hace
que esa zona apoye en la cama y evita el puente inferior de unos 73 mm presente
en la primera prueba de orientación. El laminado final desactiva soportes, pero
mantiene un puente de hasta aproximadamente 55 mm en la silla del cristal. Su
acabado y la abertura de 6,5 mm requieren prueba física; el cálculo CAD no
valida el ajuste ni la resistencia.

## Insertos desmontables para microfauna

Prototipo CAD añadido y revisado para FDM el 11 de octubre de 2026.
`MicrofaunaInsert` es un Body
independiente con operaciones nativas de PartDesign. `UpperMicrofaunaInsert`
es un enlace a la misma pieza, situado 150 mm más arriba: se necesitan dos
impresiones iguales. La hoja `MicrofaunaParameters` gobierna las dimensiones,
las guías y la posición, vinculadas al paso y a los nervios del soporte.

Cada inserto ocupa el hueco central entre las cuatro columnas. Tiene tres
láminas verticales de 1,6 mm, separadas por dos canales de 4 mm, con una
profundidad de 12 mm. Una espina une las láminas y contiene diez ventanas de
4 × 12 mm, cinco por canal, para permitir comunicación transversal. Los
canales quedan abiertos por delante, por arriba y parcialmente por abajo:
los apoyos cruzados ocupan únicamente una parte del paso inferior. Las
dimensiones son una propuesta de fabricación y espacio de refugio, no un
óptimo biológico demostrado.

Dos apoyos cruzados descansan sobre los nervios de la base. Cuatro guías bajan
2 mm por su cara interior, con 0,3 mm de juego nominal por lado. Las guías
quedan conectadas por una cruz inferior dentro del hueco del bastidor. Las
láminas y la espina también se prolongan hasta ese plano inferior para que
su arranque esté apoyado desde la primera capa. Los canales conservan pasos
inferiores abiertos entre los brazos. No hay clips,
apriete ni retención frente a una inversión del conjunto. Para retirarlo hay
que separar los módulos, o quitar la tapa en el módulo superior, y levantar
el inserto mediante una pinza o herramienta en la oreja con orificio en
lágrima: mantiene el círculo de paso Ø3 mm y añade un techo a 45° mediante
un sketch completamente restringido y un Pocket. Se han aplicado radios de
0,6 mm en seis aristas del arranque de las láminas, que suavizan su unión con
los apoyos y reducen localmente la sección libre de los canales en la raíz.
El inserto no participa en la suspensión ni modifica los cierres portantes.

Comprobaciones del CAD:

- Un único sólido válido, sin errores en las operaciones, de 9,609 cm³
- Envolvente de 38,5 × 38,5 × 142 mm, incluyendo los apoyos y la oreja
- Inserto inferior en Z=26–168 mm y superior en Z=176–318 mm
- Contacto con el soporte sin intersección volumétrica, en ambos módulos
- Sin intersección con las bolas, con distancia mínima de aproximadamente
  1,54 mm, ni con la tapa superior
- Superficie de la primera capa, calculada mediante un corte de 0,01 mm
  próximo al fondo, de 245,12 mm². Antes de la revisión, los extremos de las
  cuatro guías sumaban solo 20,48 mm² y no estaban conectados en ese plano
- Un levantamiento de 40 mm del inserto inferior no produce intersección
  con sus bolas ni con su soporte. Es una posición comprobada, no una
  simulación continua del recorrido completo

Material previsto: PETG y boquilla de 0,4 mm. La orientación inicial propuesta
es vertical, con altura de 142 mm, inferior al volumen de la KP3. La cruz
inferior y el arranque de las láminas forman una base continua. Los extremos
portantes de los apoyos sobresalen 2,3 mm de esa cruz, a 2 mm sobre su plano
inferior: debe revisarse ese pequeño voladizo en el laminado. También deben
comprobarse los puentes de 4 mm de las ventanas y el techo del orificio en
lágrima. La revisión reduce la necesidad geométrica de soportes, pero no
demuestra una impresión sin ellos. Se ha laminado una receta candidata sin
soportes. La
estabilidad de las láminas durante la impresión, las holguras con el bastidor
y con varias bolas reales y la retirada completa siguen pendientes. Las
mallas y los proyectos laminados se conservan en la entrega enlazada al final.

La función secundaria buscada es ofrecer superficies colonizables y pequeños
espacios protegidos con renovación de agua. Su colonización, acumulación de
detrito y utilidad para copépodos o anfípodos no están comprobadas. Debe poder
retirarse si dificulta el mantenimiento o el paso de agua.

## Archivos

- [Fuente FreeCAD editable](soporte-biobolas.FCStd): contiene el contexto C1,
  las bolas auxiliares, el módulo, su enlace de montaje superior, la tapa, los
  insertos de microfauna, cuatro probetas de unión y las dos series de la
  probeta de cristal, ambas integradas como grupos de cortes editables
- [STL del módulo](soporte-biobolas-modulo.stl): centrado en X/Y y con base Z=0,
  derivado del sólido con cuatro cierres, huella 81 × 81 mm
- [STL de las probetas de unión](soporte-biobolas-probeta-ajuste.stl): cuatro sólidos
  independientes colocados para imprimir en una misma placa
- [STL de la probeta de cristal](soporte-biobolas-impresion/modelos/probeta-cristal.stl):
  peine independiente con ranuras de 7, 8 y 9 mm; la ranura de 9 mm corresponde
  a vidrio nominal de 6 mm más almohadillas de 1 mm por cara y holgura de 0,5 mm
  por cara. La de 7 mm comprueba directamente el vidrio sin acolchado
- [STL de ajuste de cristal](soporte-biobolas-impresion/modelos/probeta-cristal-6_00-6_25-6_50.stl):
  peine con ranuras de 6,00, 6,25 y 6,50 mm. La ranura de 6,00 mm ha entrado en
  el vidrio real con margen muy estrecho y ajuste satisfactorio; no se midió el
  espesor exacto ni se deriva una compensación universal del PETG
- [Sección de la unión](soporte-biobolas-union-seccion.png): vista de inspección,
  sin incorporar sus recortes temporales al FCStd ni a los STL

Los STL originales, incluido el calibre de cristal, se regeneran desde la revisión
original del FCStd. El derivado FDM de la tapa y su malla se conservan aparte.
Los STL no contienen perfiles de laminado ni constituyen evidencia de una impresión
o una prueba de carga.
La tapa, los insertos y ambas series de la probeta de cristal disponen de mallas y laminados en
[soporte-biobolas-impresion/](soporte-biobolas-impresion/README.md).

## Laminado candidato

El [informe y los archivos de impresión](soporte-biobolas-impresion/README.md)
contienen diez proyectos independientes: módulo, dos versiones de tapa, inserto, cuatro tipos
de probeta de unión y dos variantes de probeta de cristal. Cada archivo imprime
una unidad. Para el conjunto se necesitan
dos módulos, una tapa y dos insertos. La entrega usa Kingroon KP3
`KP3-3DP180`, boquilla de 0,4 mm y Winkle PETG Jet Black de 1,75 mm, con recetas
candidatas de OrcaSlicer 2.4.2. El informe conserva los perfiles efectivos,
orientaciones, soportes, estimaciones, sumas y límites. Las probetas se han
impreso y sus encajes individuales se han comprobado. La primera tapa falló al
retirar los soportes; la nueva variante aún debe imprimirse y probarse antes de
evaluar la carga y el uso en húmedo.
