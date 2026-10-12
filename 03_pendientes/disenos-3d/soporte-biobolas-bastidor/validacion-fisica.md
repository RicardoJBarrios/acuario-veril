# Validación física del bastidor de biobolas

Procedimiento propuesto; **ningún ensayo de este documento se ha ejecutado**.
La aceptación requiere registrar resultados con las piezas y la receta reales.
Los modelos y G-code preparados son candidatos para prototipos.

## Antes de imprimir

Usar Kingroon KP3 de 180 × 180 × 180 mm, boquilla de 0,4 mm y la receta
documentada de Winkle PETG Jet Black de 1,75 mm. Si cambia esa combinación,
repetir las muestras de encaje. Anotar lote, estado de la bobina, placa,
temperatura ambiente y ciclo de secado. Propuesta conservada: SUNLU S2 a
55 °C durante 6 h; alimentación desde el S2 a 55 °C con temporizador que cubra
el trabajo. Este ciclo no ha sido ejecutado por el agente.

Comenzar por la placa de probetas, no por la torre completa. Dejar enfriar y
estabilizar las piezas antes de medir. Retirar el brim y rebabas sin redondear
las superficies portantes ni aplicar una escala global para corregir un encaje.

## Encajes y retención

Registrar con calibre al menos dos medidas de cada dimensión crítica y su
resultado funcional. Las holguras iniciales no son compensaciones calibradas.

| Muestra | Qué representa | Criterio de aceptación propuesto |
| --- | --- | --- |
| Horquilla y lengüeta | Panel de 3,2 mm, canal de 3,8 mm y pasador rectangular de 4 mm en ventana de 4,4 mm | Montaje manual sin abrir las orejetas; el pasador atraviesa ambas orejetas y la lengüeta; juego controlado |
| Dos bloques de esquina | Apilamiento, llave de 3,6 × 5,2 mm y ventana de 4 × 5,6 mm | Apoyo plano; no depender de una interferencia para sostener el peso; no giro libre ni extracción con chaveta colocada |
| Muestra de escuadra | Ventana de llave en la misma orientación FDM que la escuadra | Puente limpio, sin caída del techo que impida el paso ni grietas de montaje |
| Muestra de asa | Ventana de llave en la misma orientación FDM que el asa | Paso y asiento de cabeza completos, sin deformar la pieza |
| Silla de vidrio | Apertura de 6,5 mm, sin almohadillas | Entrada y retirada libres sobre el vidrio real; asiento estable, sin tener que abrir la silla por fuerza |
| Chavetas | Bloqueo transversal del pasador; las estructurales también transmiten carga | Asiento completo y retirada deliberada; no migración al invertir, agitar y manipular con manos mojadas |

Repetir diez veces inserción y retirada de cada cierre. Después sumergir las
muestras en agua salada representativa del acuario durante 48 h y repetir.
Registrar temperatura y salinidad. Invertir las muestras diez veces y comprobar
que ninguna chaveta sale o se desplaza más de 0,2 mm respecto a su marca inicial.
**Si una chaveta migra, el cierre se rechaza:** revisar su retención y volver a
imprimir la muestra. Un ajuste seco aparentemente firme no demuestra retención
en agua salada.

## Ensayo de uniones y asiento

Usar un útil externo y sujetar por las superficies equivalentes a las del
montaje. La forma de sujeción no debe reforzar artificialmente la orejeta o
acortar el vano del pasador. Utilizar masas comprobadas y una bandeja de captura.

La masa aproximada comunicada de bolas y hoteles es 1,2 kg. El cálculo adopta
2 kg para el conjunto mojado, incluidas piezas impresas y reserva de agua, y
49,05 N de carga vertical de dimensionado. Comprobar el peso final: si supera
2 kg, rehacer el cálculo antes de aceptar el conjunto.

1. Cargar cada unión de panel y cada unión estructural con **2,5 kg durante
   10 minutos**, equivalentes a la fuerza de cálculo de una de las dos uniones
   efectivas supuestas. Registrar deformación, apertura y movimiento del seguro.
2. Descargar y esperar 20 minutos. Rechazar si hay grietas, blanqueamiento,
   cierre desplazado o deformación residual mayor de 0,2 mm en el encuentro.
3. Ensayar el nervio de asiento con apoyos separados 69 mm y dos masas de
   **300 g** en Y = −18,25 y +18,25 mm. Mantener 10 minutos. Objetivo: flexión
   máxima de 1 mm y recuperación a menos de 0,2 mm tras descargar.
4. Para fluencia del nervio, usar 120 g en cada punto durante la fase húmeda de
   30 días. Medir respecto al inicio, no solo fotografiar.

Estos ensayos separan el asiento de las bolas de las uniones del bastidor.
No aplicar la sobrecarga de toda la torre a los asientos individuales:
su caso de cálculo es 0,8 kg de servicio por módulo.

## Montaje y ensayo del conjunto

Montar fuera de C1, con los módulos apoyados. Instalar los paneles en sus
alojamientos, insertar pasadores y chavetas, y comprobar las cuatro caras.
Apilar los módulos, colocar las cuatro llaves estructurales y sus chavetas.
Cambiar el orden de los módulos para comprobar que son intercambiables.
Montar la tapa y sus escuadras; instalar el asa en los travesaños interiores.
Los pasadores se introducen por los pasos previstos, sin forzar diagonales.

Comprobar en ambos órdenes que entran las 40 bolas y los dos hoteles. Verificar
su extracción con la tapa desmontada y los módulos apoyados. Revisar el paso
de agua, limpieza de huecos y acceso a todos los seguros. La separación
geométrica no demuestra por sí sola que la mano o una herramienta tenga acceso.

Sobre un útil rígido que reproduzca el espesor y canto del vidrio nominal:

- Sostener **2 kg totales** durante 24 h y medir asentamiento, inclinación y
  apertura de la suspensión al inicio, a la hora y a las 24 h.
- Aplicar **5 kg totales durante 10 minutos al perímetro portante del bastidor**,
  distribuidos en sus esquinas, para comprobar el caso vertical de 49,05 N.
  Realizar esta sobrecarga fuera del acuario; el ensayo de asientos es el anterior.
- Con 2 kg, aplicar 10 N horizontales en ambos sentidos de X e Y y comprobar
  que no hay apertura de uniones, giro permanente ni diagonales que pandeen.
  Objetivo propuesto: desplazamiento reversible menor de 2 mm y residual menor
  de 0,5 mm.
- Repetir 100 elevaciones controladas por el asa con 2 kg y diez ciclos de
  montaje/desmontaje. Comprobar de nuevo seguros, apoyos y apertura de 6,5 mm.

Un útil de espesor equivalente permite ensayar la pieza, pero no acredita la
resistencia del vidrio real del acuario. El montaje real se comprueba con la
carga de servicio tras superar los ensayos anteriores, registrando el contacto
y sin trasladar al vidrio la sobrecarga del útil.

## Inmersión y aceptación

Mantener el conjunto en agua salada representativa durante 30 días con la
carga de servicio. Registrar temperatura, salinidad y medidas los días
0, 1, 7, 14 y 30. Comparar juegos, verticalidad, apertura de escuadras y
deformación de asientos con el día 0. Propuesta de rechazo: grietas,
blanqueamiento, seguros migrados, deformación creciente que impida desmontar
o cambio dimensional permanente mayor de 0,5 mm en un encuentro portante.

Treinta días detectan defectos tempranos; no certifican vida útil prolongada.
Mantener inspecciones posteriores. La aceptación queda limitada a la receta,
masa y ambiente registrados.

## Registro de resultados

| Campo | Resultado pendiente |
| --- | --- |
| Fuente CAD y SHA-256 | |
| Proyecto 3MF, G-code y SHA-256 | |
| Máquina, boquilla, bobina/lote y secado | |
| Fecha, instrumento y enfriamiento | |
| Nominal, dos medidas y ajuste funcional | |
| Masa mojada total y masa por módulo | |
| Carga, duración, temperatura y salinidad | |
| Flexión máxima y recuperación | |
| Migración de seguros y ciclos | |
| Fotografías/vídeo asociados al ensayo | |
| Decisión: aceptado, rechazado o repetir | |
