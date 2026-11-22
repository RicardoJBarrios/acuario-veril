# Iluminación de Veril: mediciones, revisión y propuesta

Propuesta de iluminación para la maduración y las primeras incorporaciones,
basada en las mediciones del 21 de noviembre de 2026 y las pruebas posteriores.
Los perfiles de prueba y las etapas siguientes se recogen como referencias
para decidir futuros ajustes.
La propuesta parte de un Veril joven, con la AI Prime 16HD Reef y sin corales
en el momento descrito por el informe. El perfil alto es la referencia de
distribución. El objetivo es ajustar la luz a los primeros ejemplares y ampliar
el horario solo cuando haya un motivo concreto.

## Origen y finalidad de los perfiles

El diseño local **Veril Natural Reef Biológico** combinó dos referencias con
funciones distintas. Del enfoque **BRS AB+** tomó el predominio de violeta,
azul real y azul, con blanco como complemento para ampliar el espectro y
equilibrar la apariencia. Del perfil de **David Saxby** tomó la idea de una
intensidad que cambia a lo largo del día. Veril la tradujo en una subida
progresiva, una meseta y una bajada, con Moonlight al 0 % para conservar
un periodo nocturno oscuro. Los porcentajes y horarios de Veril fueron
elaborados para su propio montaje.
[Ensayo de BRStv con la Prime 16HD](https://www.bulkreefsupply.com/content/post/brstv-investigates-aqua-illumination-prime-hd) ·
[Perfil de David Saxby en AquaIllumination](https://www.aquaillumination.com/signature_series/david-saxby)

- **Diseño preliminar de septiembre (v0.1).** En el orden de la tabla
  siguiente, proponía máximos de **35 / 45 / 70 / 65 / 10 / 5 / 30 / 0 %**,
  con más blanco, verde y rojo que los perfiles bajo y alto. La propuesta
  del 18 de octubre preveía una ventana de **08:30 a 18:30**, con meseta de
  **11:30 a 16:30**. Eran hipótesis de diseño anteriores al mapa local.
  La meta de 150–200 en la cima reservaba margen para corales más exigentes.
- **Perfil bajo.** Se programó para iniciar la iluminación durante la
  maduración sin corales. Redujo los canales activos y utilizó una ventana
  de **12:00 a 17:00**, con rampas de **30 min**, para introducir luz con
  una exposición diaria contenida.
  [Perfil inicial documentado](../../02_configuracion/01_dimensiones/04_iluminacion.md#perfil-inicial-de-maduración)
- **Perfil alto.** Se obtuvo triplicando las consignas de los cinco canales
  activos del perfil bajo. El punto de partida fue la roca baja izquierda
  frontal: dio **25** con el perfil bajo y se buscaba acercarse a **75**
  para los zoas manteniendo la proporción entre canales. La roca dio **70**
  en lectura directa. El mapa resultante permite orientar el uso de las
  rocas, la terraza y la arena sin perseguir el máximo preliminar de la
  cima. Es la referencia empírica para planificar la aclimatación.
  [Mediciones del 21 de noviembre](../../04_operaciones/2026/11/2026-11-21.md#medición-de-par-con-el-danoplus)
- **Pruebas A y B.** Partieron del perfil alto para responder dos preguntas
  diferentes: qué cambia al retirar el blanco y qué cambia al añadir
  verde y rojo. Sus resultados ayudan a comparar perfiles, y la repetición
  en tres puntos respalda conservar el alto como referencia práctica.

Las lecturas anteriores están en µmol fotones·m⁻²·s⁻¹. La propuesta de
aplicación más abajo separa el pico del fotoperiodo, de forma que el horario
largo se pueda valorar por su dosis diaria y por la respuesta observada.

## Perfiles probados en myAI

| Canal | Bajo | Alto | A | B |
| --- | ---: | ---: | ---: | ---: |
| UV | 15 % | 45 % | 45 % | 45 % |
| Violet | 15 % | 45 % | 45 % | 45 % |
| Royal Blue | 25 % | 75 % | 75 % | 75 % |
| Blue | 25 % | 75 % | 75 % | 75 % |
| Green | 0 % | 0 % | 0 % | 5 % |
| Deep Red | 0 % | 0 % | 0 % | 3 % |
| Cool White | 8 % | 24 % | 0 % | 24 % |
| Moonlight | 0 % | 0 % | 0 % | 0 % |

A explora la retirada del blanco y B la adición de verde y rojo. Los
porcentajes de myAI son consignas. Su relación con el PPFD y la distribución
se comprueba con el instrumento, entre otras razones porque la Prime
redistribuye potencia entre canales.

## Mapa de PPFD

Cada celda muestra **lectura directa / estimación ×1,25**, en µmol
fotones·m⁻²·s⁻¹. El ×1,25 es el punto medio del intervalo ×1,2–×1,3
comunicado por usuarios que compararon otras unidades con Apogee. Sirve como
referencia orientativa. Una comparación directa de la unidad de Veril
permitiría estimar su sesgo bajo el espectro probado. Las cifras decimales
reflejan la aritmética del multiplicador.

| Zona | Bajo | Alto | A | B |
| --- | ---: | ---: | ---: | ---: |
| Arena derecha frontal | 19 / 23,75 | 45 / 56,25 | 31 / 38,75 | 50 / 62,5 |
| Arena central frontal | 32 / 40 | 100 / 125 | 95 / 118,75 | 100 / 125 |
| Roca baja izquierda frontal | 25 / 31,25 | 70 / 87,5 | 65 / 81,25 | 70 / 87,5 |
| Arena derecha trasera | 15 / 18,75 | 40 / 50 | 35 / 43,75 | 40 / 50 |
| Arena central trasera | 29 / 36,25 | 75 / 93,75 | 70 / 87,5 | 75 / 93,75 |
| Roca izquierda trasera | 25 / 31,25 | 70 / 87,5 | 65 / 81,25 | 85 / 106,25 |
| Masa izquierda | 33 / 41,25 | 90 / 112,5 | 85 / 106,25 | 90 / 112,5 |
| Masa centro | 38 / 47,5 | 90 / 112,5 | 90 / 112,5 | 100 / 125 |
| Masa top | 48 / 60 | 100 / 125 | 105 / 131,25 | 130 / 162,5 |
| Masa terraza | 22 / 27,5 | 70 / 87,5 | 60 / 75 | 70 / 87,5 |

Las medias de los diez puntos, con lecturas directas, fueron **28,6 / 75,0 /
70,1 / 81,0** para bajo, alto, A y B respectivamente. Son medias de los
puntos muestreados. A dio un 6,5 % menos que el alto y B un 8 % más. En A,
siete puntos quedaron entre −5 y 0 respecto al alto. En B, seis quedaron
iguales y la cima pasó de 100 a 130, el máximo observado.

### PPFD de referencia para Veril

Para interpretar el mapa y planificar ubicaciones se usa el **PPFD de
referencia**, calculado como **lectura del DanoPlus × 1,25**, redondeado
al múltiplo de **5 µmol fotones·m⁻²·s⁻¹** más cercano (en caso de empate,
al superior). El redondeo evita presentar decimales como precisión de
medida. Por ejemplo, **70 → 87,5 → ≈90**. Es una estimación operativa
provisional. La oscilación observada y el sesgo de la unidad siguen
siendo fuentes de incertidumbre.

Para cálculos intermedios se conserva el valor ×1,25 sin redondear y
se redondea solo el resultado que se presenta. Para repetir pruebas
y comparar perfiles se conservan las lecturas directas del instrumento.

### Qué representa cada zona del mapa

El [montaje documentado](../../04_operaciones/2026/09/2026-09-05.md#registro-detallado-del-hardscape-instalado)
confirma una base baja a la izquierda, una masa principal conectada que
sube hacia la torre posterior derecha, una terraza sobre el paso y
piezas separadas delante y detrás. La [ficha espacial](../../02_configuracion/01_dimensiones/02_espacial.md#medidas-de-referencia-de-la-composición-instalada)
recoge alturas aproximadas desde el fondo. La
[configuración de la luminaria](../../02_configuracion/01_dimensiones/04_iluminacion.md#luminaria-y-soporte)
sitúa la Prime centrada sobre el display.

La posición de cada punto respecto al haz y la sombra de la terraza se
recogen según la descripción del propietario. La última columna explica
cómo usar cada lectura. El mapa muestra el efecto combinado de la
geometría y la lámpara, sin cuantificar por separado la sombra, la
incidencia oblicua y la distancia a la fuente.

| Zona | PPFD referencia | Geometría y utilidad |
| --- | ---: | --- |
| Arena derecha frontal | 65 | En el extremo de la cobertura y parcialmente sombreada por la masa principal. El propietario identifica el saliente de la terraza como origen de la sombra. Sirve de referencia para la transición entre arena abierta y sombra. |
| Arena central frontal | 130 | Casi en la vertical de la lámpara según el propietario. Es el punto de arena más iluminado del mapa y la referencia para comparar el centro con los extremos. |
| Roca baja izquierda frontal | 90 | Punto bajo y despejado según el propietario, con luz oblicua. Es la lectura de partida para situar los zoas y comprobar el PPFD a la altura de sus pólipos. |
| Arena derecha trasera | 50 | Punto trasero del lado derecho. Queda en el mismo tramo de luz baja que la arena derecha frontal. Es útil para comprobar el alcance lateral del haz en la parte trasera. |
| Arena central trasera | 95 | Punto central de la franja trasera. Recibe más luz que la arena derecha trasera y menos que el centro frontal. Ofrece una referencia intermedia para reservar una ubicación en arena. |
| Roca izquierda trasera | 100 | El propietario describe una llegada oblicua y sin obstáculos, similar a la roca izquierda frontal. Es el punto de partida para valorar GSP o xenia en un soporte aislado. |
| Masa izquierda | 115 | Tramo bajo del cuerpo rocoso principal. Sirve para contrastar una superficie baja de la masa con las rocas separadas y la arena. |
| Masa centro | 125 | Tramo de altura media del mismo cuerpo. Con B queda un escalón por encima de la masa izquierda. |
| Masa top | 145 | Cima de la torre posterior derecha, el punto alto documentado del hardscape. Es una referencia para comprobar los máximos sobre roca al ajustar la Prime. |
| Masa terraza | 90 | Repisa que sobresale hacia delante. El propietario la sitúa a la altura lateral de la torre y a una elevación entre la masa izquierda y la media. Es a la vez una superficie candidata para corales y el saliente que sombrea parte de la arena derecha frontal. |

La documentación del montaje respalda el relieve general. Sus alturas de
referencia corresponden a elementos de la composición y no fijan las
coordenadas de la punta del sensor. La alineación lateral de terraza y
torre, la altura relativa exacta de los puntos y la proyección de la
sombra proceden de la observación del propietario.

Según el propietario, el interior del arco quedó fuera de la medición
porque está completamente a la sombra de la masa central.

### Cómo se eligió la lectura de cada punto

El propietario observó oscilaciones de aproximadamente **±10 µmol
fotones·m⁻²·s⁻¹** en cada punto y comunicó la media o el valor más
estable, según el caso. Ese margen describe la oscilación observada
durante la toma. Ayuda a interpretar diferencias pequeñas entre
perfiles y a valorar las predicciones del modelo. La exactitud del
DanoPlus y su repetibilidad instrumental requieren una comprobación
específica. Véase el [registro de la medición](../../04_operaciones/2026/11/2026-11-21.md#medición-de-par-con-el-danoplus).

### Cómo comparar futuras series

Fijar el perfil temporalmente, esperar unos cinco minutos y medir durante
la meseta, con el mismo nivel de agua, montaje y estado de las bombas.
Mantener el sensor horizontal y orientado hacia arriba, sin sombras del
operador. Si la superficie hace oscilar la lectura, observar varios valores
y anotar uno representativo. Registrar el perfil, la altura de la pantalla
y los puntos medidos. Para contrastar dos perfiles en un punto, repetir el
primero al final de la serie con el sensor en la misma posición.

## Repetición y elección del espectro

La tabla muestra el **PPFD aproximado de referencia** en cada sesión.

| Zona | Alto inicial | Alto repetido | B inicial | B repetida |
| --- | ---: | ---: | ---: | ---: |
| Masa top | 125 | 120 | 165 | 130 |
| Roca izquierda trasera | 90 | 95 | 105 | 95 |
| Arena central frontal | 125 | 130 | 125 | 140 |

Con lecturas directas, el alto varió 5 PAR en valor absoluto en los tres
puntos y B varió entre 10 y 25. La diferencia B menos alto en la cima pasó
de **+30 a +10**, en la roca trasera de **+15 a 0** y en la arena frontal
de **0 a +5**. Esto describe la concordancia entre sesiones. Para medir la
repetibilidad inmediata harían falta lecturas consecutivas con el sensor
inmóvil. Se comunicó una lectura por perfil y punto, así que la alternancia
propuesta alto → B → alto quedó sin una segunda lectura alta documentada.

El **perfil alto, con blanco al 24 %**, sigue siendo la referencia de las pruebas porque
su distribución está medida y fue más consistente en la repetición. A
muestra que sin blanco se conserva buena parte del PPFD indicado. B ofrece
una opción estética si interesa ensanchar el espectro. Las comparaciones con el DanoPlus permiten comparar lecturas, pero la contribución de
cada canal a la fotosíntesis y el sesgo espectral requieren otras medidas.

## Perfil B como objetivo final propuesto

El propietario propuso **B como objetivo final de iluminación**. Sus
consignas son **45 / 45 / 75 / 75 / 5 / 3 / 24 / 0 %**, en el orden de
la tabla de perfiles. Mantiene los azules, violetas y blanco del perfil
alto y añade Green al 5 % y Deep Red al 3 %. El perfil alto sigue siendo
la referencia medida de la transición y del modelo de interpolación.

| Zona | B de referencia (≈) |
| --- | ---: |
| Arena derecha frontal | 65 |
| Arena central frontal | 130 |
| Roca baja izquierda frontal | 90 |
| Arena derecha trasera | 50 |
| Arena central trasera | 95 |
| Roca izquierda trasera | 100 |
| Masa izquierda | 115 |
| Masa centro | 125 |
| Masa top | 145 |
| Masa terraza | 90 |

En los puntos repetidos se toma la media de las dos lecturas directas de B.
A esa media se le aplica ×1,25 y se redondea a múltiplos de cinco.
En particular, la cima dio 130 en la primera pasada y 105 al repetir.
La media sirve como referencia provisional para ese punto.

La transición a B se puede comprobar manteniendo el horario y midiendo
en los puntos ocupados. El horario final queda por decidir según la dosis
diaria y la respuesta observada. Para modelar intensidades intermedias
de B haría falta otra serie con sus propias proporciones de canales.

## Qué significa para el hardscape

La tabla interpreta el **perfil B como objetivo final**. Cada valor es el
PPFD aproximado de referencia en µmol fotones·m⁻²·s⁻¹. Las ubicaciones son
candidatas y la aclimatación inicial se ajusta al ejemplar.

| Zona | PPFD de referencia con B (≈) | Uso propuesto |
| --- | ---: | --- |
| Arena derecha frontal | 65 | Primer punto que valoraría para una *Ricordea florida* sobre una piedra separable. Es una transición entre la sombra de la terraza y la arena abierta. Buscar flujo indirecto. |
| Arena central frontal | 130 | Sector más iluminado de la arena. Mantenerlo abierto al inicio y reservarlo para una pieza cuyo ejemplar tolere esa exposición y deje margen para sifonar. |
| Roca baja izquierda frontal | 90 | Ubicación prevista para zoas en soporte separable. Los 90 corresponden al objetivo B. Para introducir el frag, ajustar según su luz de procedencia. |
| Arena derecha trasera | 50 | Punto de menor exposición de B. Ofrece una alternativa de aclimatación para una pieza de luz baja si el flujo y el acceso encajan. |
| Arena central trasera | 95 | Candidata para una *Micromussa* pequeña en base estable, con flujo indirecto y espacio para el tejido expandido. Comprobar la luz a la altura de la pieza. |
| Roca izquierda trasera | 100 | GSP en soporte aislado como primera opción. Con B queda por encima de la roca de los zoas. Si se elige xenia pulsante, valorar una posición menos expuesta si el esqueje procede de menos luz. |
| Masa izquierda | 115 | Superficie baja de la masa principal con más exposición que las rocas aisladas. Reserva para futuras piezas que toleren ese nivel y puedan mantenerse separadas de colonias expansivas. |
| Masa centro | 125 | Superficie intermedia cercana en exposición a la arena central frontal. Ofrece soporte elevado para una futura pieza compatible si el flujo y el espacio son adecuados. |
| Masa top | 145 | Zona más iluminada del mapa de referencia. La diferencia entre pasadas aconseja confirmar el pico antes de escoger una pieza por esa exposición. |
| Masa terraza | 90 | Reserva posterior para Duncan, martillo o frogspawn. A esta exposición, comparar luz de procedencia, flujo y espacio de expansión. Una antorcha requiere especial margen para sus tentáculos. |

## Modelo de PPFD por zona

El mapa de referencia del perfil alto sirve para consultar la exposición por zona. Para calcular
intensidades intermedias con el mismo montaje y la misma proporción entre
canales, se interpolan las **lecturas directas** del perfil bajo y alto de
cada zona. El perfil bajo usa un tercio de las consignas del alto.

1. Expresar la intensidad relativa como fracción `s` entre `1/3` y `1`.
   Las consignas teóricas de myAI son las del perfil alto multiplicadas por `s`.
2. Calcular la posición entre perfiles con `t = (s − 1/3) / (1 − 1/3)`.
3. Calcular `PPFD previsto = bajo + t × (alto − bajo)`.
4. Multiplicar el PPFD previsto por 1,25 y redondear para comunicar el
   PPFD de referencia previsto.

Al **60 %** del perfil alto, `t = 0,40`. Las consignas teóricas son
UV y Violet al 27 %, Royal Blue y Blue al 45 %, Cool White al 14,4 %
y los demás canales al 0 %. Si se redondean, anotar los valores
realmente aplicados al registrar una medición.

| Zona | Referencia prevista (≈) |
| --- | ---: |
| Arena derecha frontal | 35 |
| Arena central frontal | 75 |
| Roca baja izquierda frontal | 55 |
| Arena derecha trasera | 30 |
| Arena central trasera | 60 |
| Roca izquierda trasera | 55 |
| Masa izquierda | 70 |
| Masa centro | 75 |
| Masa top | 85 |
| Masa terraza | 50 |

Valores en µmol fotones·m⁻²·s⁻¹. Si solo se dispone de la lectura del perfil
alto, se puede aproximar con `PPFD alto × (0,071 + 0,929 × s)`. Este
atajo usa el cociente entre las medias baja y alta (28,6 ÷ 75,0) y pierde
las diferencias espaciales. Al 60 % da unos 44 para una lectura alta de
70, frente a 43 con la interpolación de las dos rocas de los primeros corales.

El modelo se apoya en dos intensidades y se usa dentro del intervalo medido.
Una comprobación intermedia en las dos rocas y la terraza permitirá valorar
cuánto se acerca al resultado real. Confirmar en el soporte del coral antes
de ajustar su exposición y volver a medir si cambia el montaje o la
proporción entre canales. Las pruebas A y B sirven para comparar espectros.

Para estimar el DLI de referencia se usa el PPFD previsto de meseta
multiplicado por 1,25 antes de redondear. El
cálculo de las rampas usa el supuesto independiente de PPFD lineal en el
tiempo, pues la interpolación de intensidades deja fuera el tramo entre
apagado y un tercio del perfil alto.

## Fotoperiodo y dosis diaria

Para rampas lineales de PPFD, las horas equivalentes al pico son la meseta
más la mitad de la duración de ambas rampas. El DLI de la pantalla se
estima como **PPFD de pico × horas equivalentes × 0,0036**. La tabla
compara los horarios al mismo pico, con un PPFD de referencia de ≈90.
El cálculo utiliza el valor previo al redondeo. La luz ambiental y
las desviaciones respecto a una rampa lineal quedan fuera del cálculo.

| Horario | Horas equivalentes | DLI de referencia (pico ≈90) |
| --- | ---: | ---: |
| 5 h, rampas de 30 min | 4,5 | 1,42 |
| 6 h, rampas de 30 min | 5,5 | 1,73 |
| 10 h, meseta de 5 h y rampas de 2,5 h | 7,5 | 2,36 |

DLI en mol·m⁻²·día⁻¹. Pasar de 5 h a ese perfil de 10 h supone **un 67 % más
de dosis** al mismo pico. La duración de las rampas explica por qué dos
programas de seis horas también pueden tener dosis distintas.

## Propuesta de aplicación

1. **Maduración sin corales.** Conservar el perfil bajo documentado de
   12:00 a 17:00, hora canaria, con rampas de 30 min. Cambiar al 40 % y
   seis horas solo si hay un motivo concreto, como una ventana de observación
   distinta o una respuesta a lo que se observe en el acuario.
2. **Preparar los primeros Zoanthus y GSP.** Mantener inicialmente las cinco
   horas y medir a la altura de los pólipos durante la meseta, con posición
   de lámpara, nivel de agua y bombas comparables. Si se desconoce el PAR
   de procedencia, usar como referencias iniciales **≈75–90 de PPFD de referencia para
   zoas** y **≈65–90 para GSP**. El 60 % relativo de myAI puede servir
   como prueba. La lectura en cada soporte decidirá el ajuste.
3. **Tras el asentamiento.** Si interesa alargar el día, probar seis horas
   con el mismo pico y observar extensión y color. Si aparece retracción
   persistente o pérdida de color, revisar también flujo y parámetros.
   Cambiar una variable cada vez facilita interpretar lo observado.
4. **Añadir el primer LPS cuando la pieza y la ubicación encajen.** Confirmar
   estabilidad de KH, salinidad, temperatura y nutrientes, junto con flujo
   y espacio disponible. Medir el punto exacto y elegir entre terraza y
   arena según la pieza.
5. **Valorar la transición al perfil B y estabilizar el horario según la respuesta.** Los escalones 40/60/85/100 %
   y el horario final 09:00–19:00 del borrador quedan como opciones. Repetir
   el mapa completo si cambia materialmente el montaje o perfil y usar
   medidas puntuales para ajustes menores. Anotar el PPFD directo y dejar
   el ×1,25 y el PPFD de referencia identificados por separado.

## Referencias y trazabilidad

- [Registro de las dos series originales](../../04_operaciones/2026/11/2026-11-21.md)
- [Configuración de iluminación de Veril](../../02_configuracion/01_dimensiones/04_iluminacion.md)
- [Ficha del DanoPlus y fundamento del ×1,25](../../01_verilpedia/04_hardware/danoplus-dp-414/danoplus-dp-414.md#estimación-orientativa-del-mapa-de-veril)
- [Comparaciones de usuarios en Reef2Reef](https://www.reef2reef.com/threads/vbr-aqua-par-meter-for-aquarium-r-g-b-par-seperately/page-5)
- [Candidatos de coral y criterios de aplicación](../../02_configuracion/03_biologia/02_candidatos/02_corales-y-analogos.md)
- [Escenario unificado de Veril](../../02_configuracion/03_biologia/03_escenarios/01_escenario-unificado-veril.md)
- [AquaIllumination, Prime 16HD y redistribución de potencia](https://www.aquaillumination.com/products/prime)
- [Experimento de irradiancia, fotoperiodo y crecimiento en Galaxea fascicularis](https://www.cambridge.org/core/journals/journal-of-the-marine-biological-association-of-the-united-kingdom/article/abs/light-intensity-photoperiod-duration-daily-light-flux-and-coral-growth-of-galaxea-fascicularis-in-an-aquarium-setting-a-matter-of-photons/CC641AF80B0994F8940155BDFC7EBC99). Informa el razonamiento sobre dosis diaria. Los objetivos por especie se valoran con sus propias fichas y el ejemplar concreto.
