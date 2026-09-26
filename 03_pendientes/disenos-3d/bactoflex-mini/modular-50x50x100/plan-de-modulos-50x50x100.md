# Plan de dos módulos BactoFlex Mini para C1 y uso de cuarentena

**Estado:** diseño CAD candidato cerrado por ahora. Fabricación y validación
pendientes. Este documento describe el diseño previsto, no una instalación ni
un resultado probado.

## Objetivo

Alojar dos bloques de BactoFlex Mini, cada uno de **50 × 50 × 100 mm**, en dos
cestas idénticas e independientes. La disposición vertical busca reducir la
huella ocupada en C1 y dejar más espacio libre para la circulación y la
retirada de detrito. Esos efectos son objetivos de diseño que deben
comprobarse en uso; no se dan por demostrados.

## Diseño adoptado para esta iteración

- Una cesta independiente por bloque, con tapa propia. Se fabricarán dos
  juegos iguales a partir del mismo modelo paramétrico.
- El bloque nominal se introduce con su eje de 100 mm en vertical. Las
  dimensiones interiores del CAD están parametrizadas para 50 × 100 × 50 mm.
- La cara posterior de 50 × 100 mm queda continua y cerrada para aportar
  rigidez y recibir los elementos de apoyo. Las otras tres caras laterales
  quedan abiertas mediante los huecos definidos en el CAD; la base también
  incorpora una abertura redondeada. La tapa es una pieza separada y
  redondeada.
- Cada cesta lleva un único tetón de ventosa centrado en la cara posterior y
  una pata inferior centrada. La pata forma parte del cuerpo de la cesta y su
  extremo de contacto está redondeado. La ventosa sirve para estabilizar y
  posicionar; el diseño no acredita por sí mismo capacidad de carga ni
  sujeción.
- Los dos módulos no comparten bastidor y pueden situarse a distintas alturas
  o posiciones, sujetas a comprobar holguras y circulación en C1.

## Interfaz provisional de ventosa

Hasta medir la ventosa real, el CAD usa una referencia temporal de tetón
nominal **Ø6 × 8 mm**, con **0,3 mm de holgura diametral** respecto a la
abertura nominal parametrizada. La ranura de retención tiene 1 mm de anchura;
su profundidad radial de 1 mm y su posición a 1 mm del extremo son hipótesis
de modelado, no medidas confirmadas de la EHEIM 7271100. Las dimensiones son
editables en la hoja de parámetros del archivo FreeCAD.

Por tanto, no se debe interpretar esta geometría como interfaz EHEIM validada
ni forzar la ventosa real sobre el tetón sin probar antes el encaje de forma
controlada. Cuando se disponga de la ventosa, se medirán el diámetro y la
forma del alojamiento, el resalte, la garganta y la profundidad útil, y se
ajustará el modelo si procede.

## Uso previsto como reserva biológica

La independencia de los módulos permite retirar una cesta completa y
trasladarla a un acuario hospital o de cuarentena, acompañada de agua del
sistema, como medio filtrante colonizado. Se plantea como ayuda para aportar
material biológico existente; **no garantiza un ciclado instantáneo ni
sustituye la comprobación de amoniaco y nitrito**.

Si un módulo queda expuesto a medicación incompatible con el material
biológico, se retirará del sistema principal. Su reutilización, reinicio o
descarte requerirá decidirse según el medicamento y el protocolo aplicable;
este plan no define un procedimiento de descontaminación.

## Comprobaciones antes de considerar el diseño validado

1. Contrastar las medidas reales del bloque y confirmar que entra, queda
   retenido por la tapa y puede extraerse sin dañar el material.
2. Medir la ventosa real y revisar el encaje; corregir el tetón y la ranura si
   hace falta.
3. Imprimir dos juegos idénticos y registrar material, orientación, soportes,
   dimensiones impresas y cualquier ajuste necesario.
4. Comprobar integridad de la cesta, continuidad de uniones, pata, estabilidad
   y apertura/cierre de la tapa tras retirar soportes.
5. Probar la colocación en C1, las holguras y la circulación; observar si se
   acumula detrito alrededor o dentro de las cestas.
6. Registrar por separado los resultados de la prueba de uso en C1 y, si se
   realiza, del traslado a hospital/cuarentena.

Hasta completar estas pruebas, las mejoras de espacio, flujo, menor
acumulación de detrito y utilidad como reserva biológica siguen siendo
intenciones o hipótesis de diseño. La ficha de [cesta y tapa](README.md)
identifica el modelo candidato y separa sus archivos de los derivados de la
variante anterior.
