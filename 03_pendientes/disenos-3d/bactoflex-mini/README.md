# Cesta y tapa para BactoFlex Mini

Diseño paramétrico de una cesta y una tapa deslizante destinadas a alojar un
BactoFlex Mini en Veril. La fuente editable es
[`veril-bactoflex.FCStd`](veril-bactoflex.FCStd); las exportaciones geométricas,
proyectos de OrcaSlicer y G-code están en [`impresion/`](impresion/README.md).

Este paquete describe un diseño y una receta candidata. Sus archivos no
registran por sí mismos el estado de compra, instalación o prueba física del
BactoFlex Mini o de estas piezas en Veril. La aceptación requiere imprimir
ambas piezas, comprobar la retirada de soportes, el deslizamiento de la tapa y
el montaje en el uso previsto, y registrar el resultado.

## Archivos principales

- [`veril-bactoflex.FCStd`](veril-bactoflex.FCStd): modelo paramétrico editable.
- [`impresion/veril-bactoflex-jaula.stl`](impresion/veril-bactoflex-jaula.stl)
  y [`impresion/veril-bactoflex-tapa.stl`](impresion/veril-bactoflex-tapa.stl):
  exportaciones geométricas.
- [`impresion/README.md`](impresion/README.md): receta y estado de los archivos.
- [`impresion/informe-gcode-2026-09-23.md`](impresion/informe-gcode-2026-09-23.md):
  procedencia, parámetros y comprobaciones del laminado.

## Por qué tiene estas partes

El diseño separa tres funciones: alojar el BactoFlex Mini, sujetar el conjunto
en la cámara y permitir abrir la parte superior sin desmontar la cesta. Las
medidas de interfaz están en la hoja de parámetros del archivo FreeCAD. Allí
se usan como entrada 100 × 50 × 100 mm para el BactoFlex, 1,5 mm de holgura
interior y paredes de 2 mm, de donde salen unas dimensiones exteriores de
cesta de 107 × 57 × 105 mm. Son cotas del modelo de diseño; la compatibilidad
con una unidad física concreta aún debe comprobarse.

| Parte | Motivo de diseño | Qué falta comprobar |
| --- | --- | --- |
| Cuerpo abierto de la cesta | Rodea el BactoFlex y deja acceso desde arriba. Las paredes de 2 mm y la base forman una pieza imprimible; las esquinas verticales y la unión interior con la base llevan radios de 0,8 y 0,6 mm. | Rigidez, dimensiones reales del BactoFlex y ausencia de interferencias al introducirlo. |
| Huecos de las cuatro paredes | El patrón de ranuras con extremos redondeados distribuye aberturas por las caras largas y cortas para permitir intercambio pasivo de agua alrededor del medio. El modelo usa seis huecos por cara larga y tres por cara corta, con margen de 7,5 mm y 5 mm de material entre huecos. El CAD declara expresamente que esto no demuestra un caudal ni un rendimiento de filtración. | Que no escape el medio, que no se obstruyan los huecos y que la circulación real sea suficiente. |
| Perforación de la base | Tres ranuras pasantes longitudinales evitan que el fondo sea una superficie cerrada y permiten intercambio por debajo de la cesta, además de por los laterales. El modelo reutiliza este patrón en la tapa. | Área abierta efectiva, resistencia de la base y efecto sobre la circulación una vez montada. |
| Dos anclajes superiores para ventosa | Los tetones superiores están pensados para encajar en ojales de ventosa nominales de 5 mm. El tetón deja 0,3 mm de holgura diametral; su base de 10 mm de diámetro y 2 mm de espesor reparte la unión con la pared. | El diámetro y la forma del ojal de las ventosas reales, el encaje y la sujeción bajo carga. Las ventosas dibujadas en FreeCAD son referencias visuales, no piezas validadas. |
| Dos patas inferiores de apoyo | Llegan hasta el cristal trasero usando la separación de instalación parametrizada de 8 mm. Son apoyos rígidos que sustituyen a dos ventosas inferiores; ayudan a posicionar la cesta sin depender de una cuarta ventosa. Sus puntas redondeadas evitan terminar en una arista plana estrecha. | La separación real del cristal y el contacto, estabilidad y reparto de carga del conjunto. |
| Guía en U de la tapa | Dos guías largas, frontal y trasera, retienen la lámina por sus bordes; una guía lateral cierra el extremo. El lado opuesto queda abierto para insertar y retirar la tapa deslizándola desde +X. Los redondeos alivian las esquinas de la guía y del extremo de entrada. | Que la guía no se deforme, que no atrape residuos y que funcione después de la impresión y la inmersión. |
| Tapa plana perforada | Cubre la abertura para retener el medio, pero conserva las tres ranuras longitudinales enlazadas al patrón de la base para el intercambio de agua. Entra desde +X y se desliza hacia −X para acceder al BactoFlex sin retirar la cesta; queda a ras en el lado +X. Su espesor nominal sale de pared menos holgura vertical (2 − 0,3 = 1,7 mm); el modelo reserva 0,3 mm por lado y bajo el labio superior para el deslizamiento. | Holgura real tras imprimir, facilidad de apertura, retención del medio y circulación. La holgura es un valor inicial de CAD, no una prueba de encaje. |

La orientación de instalación también forma parte de la intención del modelo:
la cara `+Y` se toma como trasera, `+X` como derecha y el divisor frontal como
`−Y`. La hoja paramétrica describe una cámara de referencia de 139 × 85 ×
390 mm y una separación inicial de 8 mm con el cristal trasero. Estas
referencias ayudan a situar la cesta en el conjunto previsto, pero no
acreditan por sí solas que la cámara o sus cotas sigan siendo las mismas en la
instalación actual.

Los radios, espesores y holguras son decisiones geométricas para esta versión,
no resultados de un cálculo estructural ni de una prueba hidráulica. La
validación final requiere revisar el encaje con el BactoFlex y las ventosas
reales, comprobar el movimiento de la tapa y observar la circulación y la
estabilidad una vez montada. El estado de esas pruebas se registra en la
[receta de impresión](impresion/README.md).

## Licencia

Todo el contenido de este directorio, incluidos el archivo FreeCAD, STL, 3MF,
G-code y documentación, se distribuye bajo la licencia MIT. Consulta
[`LICENSE`](LICENSE). La licencia no implica aprobación ni garantía del
fabricante del BactoFlex.
