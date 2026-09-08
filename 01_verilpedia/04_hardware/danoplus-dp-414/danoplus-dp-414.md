# DanoPlus DP-414

## Identificación y función en Veril

El **DanoPlus DP-414** es el sensor previsto para medir el PPFD bajo el agua y construir el mapa de exposición lumínica de Veril. No forma parte del régimen de iluminación ni determina por sí mismo qué organismos son compatibles con una zona.

La unidad de medida principal será el PPFD registrado en µmol fotones m⁻² s⁻¹ dentro del intervalo PAR. Los valores se relacionarán con la posición, profundidad, espectro, fotoperiodo y estado de la luminaria.

## Estado de la decisión

**Seleccionado:** Se utilizará el DP-414 como instrumento propio para el mapa de PPFD de Veril, siempre que la unidad recibida corresponda al modelo documentado y el sensor no presente daños.

**Previsto:** El sensor se empleará sumergido, unido a la varilla telescópica, con una orientación y un protocolo de posición constantes.

**Pendiente:** Deben registrarse la unidad recibida, el número de serie o lote, la revisión identificable, el estado del sensor y, si resulta posible, una comparación puntual con un medidor subacuático de referencia.

## Especificaciones documentadas

| Campo | Valor documentado |
| --- | --- |
| Fabricante | DanoPlus |
| Modelo comercial | DP-414 |
| Identificación alternativa documentada | KIB0414 en el manual consultado |
| Tipo | Medidor cuántico de PPFD para medición subacuática |
| Sensor | Sensor cuántico declarado IP68 |
| Intervalo espectral declarado | 400–700 nm ±10 nm |
| Rango de medición declarado | 0–4000 µmol fotones m⁻² s⁻¹ |
| Resolución indicada | 0,1 hasta 999 y 1 por encima de 1000, según la documentación consultada |
| Registro interno | Hasta 100 valores |
| Cable | Aproximadamente 79 pulgadas, según el fabricante |
| Varilla | Telescópica sólida de aproximadamente 37 pulgadas, según el fabricante |
| Alimentación | 2 pilas AAA en el manual oficial en español; algunas copias secundarias indican 3 |
| Unidad principal | No sumergible |

Las especificaciones anteriores son declaraciones del fabricante o de su manual. No equivalen a una validación independiente de exactitud, linealidad, respuesta espectral o repetibilidad de la unidad de Veril.

El manual oficial en español se conserva en [DanoPlus DP-414: manual de uso](danoplus-dp-414-manual-es.pdf). La página del fabricante también identifica el equipo como **414_E**, mientras que otras copias del manual utilizan **KIB0414** o **CD50**. Al recibir la unidad se registrará la identificación impresa en el producto y se conservarán esas variantes como referencias del mismo conjunto documental, sin asumir que todas las revisiones sean idénticas.

## Funciones del manual

El manual documenta las siguientes operaciones:

- Medición en tiempo real
- Retención de la lectura mediante `HOLD`
- Registro manual de hasta 100 valores
- Consulta y borrado de los registros almacenados
- Calibración del punto cero cubriendo completamente el sensor
- Restablecimiento de fábrica
- Apagado automático tras aproximadamente tres minutos sin operación
- Ajuste de la inclinación del sensor hasta aproximadamente 180°

La calibración descrita es una calibración del cero en oscuridad. No es una calibración de exactitud frente a una fuente patrón ni proporciona por sí sola un factor de corrección para mediciones subacuáticas.

## Limitaciones de medición

El sensor no se considerará una referencia metrológica absoluta sin una comparación documentada con un medidor subacuático de referencia. Las comparativas disponibles de medidores económicos muestran factores de corrección variables según la unidad, la revisión del sensor, el espectro y la posición.

No se aplicará automáticamente un multiplicador publicado para otra unidad. Si se dispone de una comparación con un Apogee MQ-510 u otro instrumento de referencia, el factor obtenido se registrará junto al número de unidad, las condiciones y el espectro utilizado. Hasta entonces, los valores podrán utilizarse como referencia espacial y comparativa interna, pero no como cifras absolutas con precisión de laboratorio.

La orientación del sensor debe permanecer constante. Una inclinación distinta, una sombra de la varilla, burbujas, suciedad o una posición diferente sobre una superficie rugosa pueden alterar la lectura. El sensor no se dejará instalado permanentemente en el acuario.

## Reseñas y pruebas independientes

La evidencia independiente disponible es limitada y no constituye una certificación de exactitud. Las experiencias siguientes se conservarán como observaciones de usuarios o pruebas concretas, no como valores universales para todas las unidades:

- Serious Reefs comparó el DP-414 y el VBR-Aqua con un Apogee MQ-510 y resumió que ambos podían utilizarse como opciones económicas después de aplicar una corrección aproximada, aunque prefirió el DanoPlus y señaló dificultades en el violeta y el índigo
- En Reef2Reef, usuarios que compararon unidades DanoPlus con Apogee comunicaron factores de aproximadamente 1,2–1,3 en algunas unidades
- En el mismo debate se afirmó que algunas cajas recientes identificadas con un punto verde se acercaban a Apogee sin corrección, pero otro usuario con una unidad equivalente siguió observando la necesidad de un factor de 1,2–1,3
- Una prueba publicada en Reddit comparó aproximadamente 230 PPFD del DanoPlus con 355 PPFD del Apogee en el mismo punto, lo que muestra que una unidad concreta puede presentar un sesgo importante
- Las experiencias generales de usuarios valoran el precio, la varilla y la utilidad para evitar ajustar la luz a ciegas, pero no permiten establecer una exactitud común a todas las revisiones

Estas diferencias no demuestran necesariamente que el instrumento sea inútil. Sí demuestran que la cifra mostrada no debe tratarse como intercambiable con la de un Apogee sin validar la unidad concreta.

## Puntos débiles conocidos

### Exactitud y corrección no universal

El fabricante publica una repetibilidad de ±1 µmol fotones m⁻² s⁻¹, pero la repetibilidad declarada no equivale a exactitud frente a un patrón. Las comparativas independientes muestran factores distintos según la unidad, el sensor, el espectro y la posición.

No se utilizará un factor genérico como 1,25×, 1,35× o 1,7× sin justificarlo con una comparación de la unidad concreta. Para Veril, la prioridad será que el mapa sea repetible; si se obtiene una referencia externa, el factor se registrará con sus condiciones y no se extrapolará automáticamente a otra unidad.

### Respuesta espectral limitada

El intervalo declarado es 400–700 nm con una tolerancia de aproximadamente ±10 nm. Esto permite medir PPFD dentro del intervalo PAR convencional, pero no convierte el equipo en un espectrómetro ni describe la distribución espectral de la AI Prime 16HD Reef.

La respuesta en el extremo violeta, especialmente cerca de 400–420 nm, puede ser una fuente de diferencia frente a otros sensores. No se interpretará el valor de PPFD como una medida de PUR ni como una descripción de qué bandas utiliza un organismo.

### Orientación y geometría

El sensor puede inclinarse para adaptarse a la posición de medida, pero esa articulación introduce una variable que debe fijarse. La orientación, la sombra de la varilla, el reflejo del cristal, las burbujas y la rugosidad de la superficie pueden modificar la lectura.

El mapa de Veril utilizará una orientación definida y repetible. Si una zona exige medir sobre una superficie inclinada, se registrará esa condición en lugar de comparar el valor directamente con una superficie horizontal sin contexto.

### Memoria y registro manual

La memoria de 100 lecturas no conserva por sí sola coordenadas, profundidad, hora, programación de la luminaria ni condiciones hidráulicas. La memoria se utilizará como apoyo, pero el mapa definitivo se registrará fuera del instrumento con la plantilla de medición de Veril.

El apagado automático tras aproximadamente tres minutos puede interrumpir una sesión lenta. Se comprobará el estado del instrumento durante el muestreo y se evitará interpretar una lectura perdida como un cambio lumínico.

### Protección y mantenimiento

El IP68 se declara para el sensor, no para la unidad principal, el cable completo ni el conector. El manual no establece en la ficha consultada una profundidad máxima ni una duración máxima de inmersión. Por ello, el sensor se utilizará durante la medición, se enjuagará después y no se dejará instalado permanentemente.

La superficie óptica es sensible a suciedad y arañazos. Un sensor contaminado, un conector con humedad o un cable deteriorado pueden producir lecturas inestables y no deben resolverse aplicando un factor de corrección.

### Documentación del fabricante

El manual oficial es breve y no aporta un certificado de calibración individual, una curva de respuesta espectral detallada, incertidumbre expandida, profundidad máxima de ensayo ni resultados de comparación frente a un estándar subacuático. La declaración de repetibilidad debe conservarse como especificación del fabricante, no como prueba independiente de exactitud.

## Uso previsto en el mapa de Veril

El mapa se realizará con la AI Prime 16HD Reef en la configuración que se quiera documentar y con la geometría operativa del aquascape instalada. Cada punto deberá conservar:

- Fecha y hora
- Altura de la luminaria sobre el agua
- Estado de los canales y programación activa
- Profundidad y posición horizontal del sensor
- Orientación del sensor y método de sujeción
- Estado de la superficie del agua y de la circulación
- Valor mostrado por el DP-414
- Factor de corrección utilizado, si existe
- Relación del punto con roca, sustrato, islas, terrazas, sombras o espacios previstos

El mapa se utilizará para clasificar zonas de exposición y relacionarlas con las necesidades documentadas de los organismos. No se asignarán corales únicamente por el valor de un punto ni se interpretará el mapa como una medición del espectro completo.

## Procedimiento de aceptación

1. Comprobar que el modelo y el sensor recibidos corresponden al DP-414 documentado
2. Revisar carcasa, cable, conector, sensor, varilla y compartimento de pilas
3. Confirmar que la unidad principal permanece fuera del agua
4. Encender el instrumento y verificar que la lectura responde a cambios de iluminación
5. Colocar el sensor plano o en la orientación definida para el protocolo
6. Comprobar que la varilla no proyecta sombra sobre el sensor ni modifica su posición
7. Realizar lecturas repetidas en un punto de control para evaluar la repetibilidad local
8. Registrar la medición de referencia, si se dispone de otro instrumento
9. Documentar cualquier factor de corrección antes de construir el mapa definitivo
10. Guardar el mapa junto con la configuración de la luminaria y la geometría del aquascape

El DP-414 se considerará adecuado para el mapa cuando produzca lecturas repetibles bajo la misma configuración, pueda colocarse en las zonas relevantes y sus limitaciones estén registradas. La exactitud absoluta no se dará por demostrada solo por la resolución mostrada o por la declaración IP68.

## Mantenimiento y seguridad

Después de cada sesión se enjuagará el sensor con agua dulce adecuada, se inspeccionará el cable y se dejará secar antes de guardarlo. No se sumergirá la unidad principal ni se utilizará el instrumento si el cable, el conector o la carcasa del sensor presentan daños.

La varilla se manejará sin golpear el cristal, la roca, el sustrato ni los corales. Las mediciones se realizarán con la alimentación y los equipos en la configuración definida para el mapa; cualquier parada de bombas o cambio temporal deberá registrarse porque modifica las condiciones de exposición y la estabilidad del sensor.

## Fuentes

- [DanoPlus: DP-414](https://www.danoplus.com/products/dp-414/)
- [DanoPlus: categoría de medidores de luz](https://www.danoplus.com/category/light-lux-meters/)
- [DanoPlus: manuales y software del modelo 414](https://www.cd50.net/414/)
- [Manual local en español del DP-414](danoplus-dp-414-manual-es.pdf)
- [Manual del DanoPlus KIB0414](https://manuals.plus/asin/B0D3LVT1MR)
- [Comparativa de DanoPlus, VBR-Aqua y Apogee publicada por Serious Reefs](https://www.patreon.com/SeriousReefs/posts/mq510-575-par-vs-151737140)
- [Comparativa de usuarios entre DanoPlus y Apogee](https://www.reef2reef.com/threads/vbr-aqua-par-meter-for-aquarium-r-g-b-par-seperately/page-5)
- [Prueba comparativa de DanoPlus y Apogee en ReefTank](https://www.reddit.com/r/ReefTank/comments/1p2v9of/would_this_par_meter_do_the_job_thoughts/)
