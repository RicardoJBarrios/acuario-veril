# Soporte modular de biobolas: revisión de la unión

Revisión CAD del 10 de octubre de 2026. Estado: **prototipo con comprobación
geométrica; pendiente de laminado, impresión y prueba de carga**. Este diseño
permanece en pendientes y no representa una instalación validada en Veril.

## Objetivo y referencias

Cada módulo es una pieza monolítica para 20 biobolas Mantis, distribuidas en
cuatro mástiles X con cinco bolas por mástil. Dos módulos idénticos e
intercambiables reúnen las 40 bolas adquiridas. La tapa de suspensión se
diseñará posteriormente a partir de esta interfaz.

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

La revisión utiliza dos ganchos exteriores integrados que atraviesan ventanas
del módulo superior. Sus caras inferiores quedan **por encima de los hombros
portantes de la base superior**. Tras consumir 0,3 mm de juego axial, esas
caras apoyan sobre los hombros e impiden la extracción hacia abajo.

El recorrido de carga es: bolas → apoyos y bastidor inferior → montantes
laterales → lengüetas y ganchos → hombros del módulo superior → bastidor
superior. Los cuatro tetones y alojamientos conservan la función de alineación.
La retención no se atribuye a su fricción.

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
| Radio en la raíz del diente | 0,6 mm |
| Rampa respecto a la dirección vertical de inserción | 35° |
| Espesor del hombro portante | 3 mm |
| Ventana radial × tangencial | 4,2 × 8,6 mm |
| Holgura axial en reposo | 0,3 mm |
| Desplazamiento de cabeza para liberar | 1,2 mm hacia dentro |
| Superficie horizontal de contacto por gancho | 0,9 × 8 = 7,2 mm² |
| Holgura entre la bola superior y el módulo siguiente | 2 mm |
| Paso entre módulos | 150 mm |
| Envolvente de una pieza | 81 × 75 × 155,871 mm |
| Altura de dos módulos ensamblados | 305,871 mm |

El conjunto se centra en X/Y dentro del contexto C1 para permitir acceso a
ambos cierres. La base comienza a 25 mm del fondo: se ocupa parte del hueco
inferior inicialmente previsto de 50 mm, conforme a la autorización del
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

- El módulo es un único sólido válido, con volumen de 50,351 cm³ y altura
  inferior a los 180 mm de la Kingroon KP3
- Las representaciones auxiliares contienen 20 bolas por módulo y no
  presentan intersección volumétrica con sus soportes
- Las cuatro bolas superiores del módulo inferior tienen 2 mm de distancia CAD
  al módulo superior, sin intersección volumétrica
- Los módulos ensamblados no se intersecan en la posición de reposo
- Un intento de separación axial de 0,4 mm produce dos zonas de solapamiento
  en los ganchos, con volumen total de 1,384 mm³: esa posición sería impedida
  por los topes. Una separación de 1 mm también queda bloqueada
- Con las cabezas desplazadas 1,2 mm hacia dentro, las posiciones de retirada
  comprobadas a 0, 0,4, 1, 3 y 6 mm no muestran colisión con el receptor
- La probeta de un solo cierre también está libre en reposo, bloquea el
  intento de separación de 0,4 mm y permite la retirada comprobada a 3 mm
  con la cabeza desplazada hacia dentro

La prueba de liberación traslada rígidamente la cabeza recortada para comprobar
espacio disponible. No simula la deformación elástica de la lengüeta, la fuerza
de accionamiento, las tensiones ni la resistencia del PETG impreso.

## Fabricación y prueba física pendiente

Material previsto: PETG, boquilla de 0,4 mm. El módulo se imprime verticalmente
con la base sobre la cama, como una sola pieza. La probeta reúne cuatro
artículos independientes: mástil X, calibre Ø10,5 mm, gancho macho y receptor.
Las dos últimas piezas reproducen el hombro, la ventana, la rampa y el radio
del modelo revisado, con agujeros Ø3 mm para sujeción durante las pruebas.

Antes de imprimir los módulos completos:

1. Laminar e imprimir las probetas en la misma orientación, con la misma bobina,
   secado y proceso previstos para el soporte. Revisar el pequeño voladizo de
   la cara portante y el puente de 8,6 mm del receptor antes de decidir soportes
2. Dejar enfriar y medir al menos dos veces el espesor de lengüeta, la ventana
   y las holguras. Probar el mástil con varias bolas reales
3. Confirmar inserción vertical, enclavamiento y liberación manual. La carga
   debe apoyar en las caras horizontales y no mantener la lengüeta presionada
   hacia dentro. Comprobar que no aparece apertura espontánea al tirar
4. Como prueba inicial propuesta, someter el cierre de la probeta a 1 kg
   durante 10 minutos y repetir montaje/desmontaje. Registrar el resultado y
   cualquier marca, blanqueamiento, grieta o deformación residual
5. Tras aceptar el encaje, probar la unión completa a dos cierres fuera del
   acuario. Se propone una carga de comprobación de 2 kg durante 10 minutos,
   seguida de comprobación con las 20 bolas y de evaluación bajo carga en
   ambiente húmedo. Estas pruebas aún no se han ejecutado

La carga axial de los montantes y lengüetas solicita la unión entre capas FDM.
El CAD no aporta una resistencia admisible ni certifica comportamiento a largo
plazo, fluencia del PETG o fatiga tras ciclos de accionamiento. La tapa y su
unión necesitarán su propia comprobación con la carga total suspendida.

## Archivos

- [Fuente FreeCAD editable](soporte-biobolas.FCStd): contiene el contexto C1,
  las bolas auxiliares, el módulo, su enlace de montaje superior y las probetas
- [STL del módulo](soporte-biobolas-modulo.stl): centrado en X/Y y con base Z=0,
  derivado de un único sólido
- [STL de las probetas](soporte-biobolas-probeta-ajuste.stl): cuatro sólidos
  independientes colocados para imprimir en una misma placa
- [Sección de la unión](soporte-biobolas-union-seccion.png): vista de inspección,
  sin incorporar sus recortes temporales al FCStd ni a los STL

Los STL se regeneran desde esta revisión del FCStd. No contienen perfiles de
laminado ni constituyen evidencia de una impresión o una prueba de carga.
