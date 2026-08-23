# Mantis Tourbon 60 Wave Maker

## Identificación

| Parámetro | Valor documentado |
| --- | --- |
| Fabricante | Mantis Aquarium Technology Co., Ltd. |
| Modelo | Tourbon 60 |
| Tipo | Bomba de movimiento y generadora de olas |
| Caudal máximo declarado | 4.000 l/h |
| Consumo declarado | 3–15 W en la tabla oficial; varias tiendas publican 8 W para la Tourbon 60 |
| Alimentación | DC 24 V según la tabla oficial |
| Montaje | Imán exterior, con orientación regulable |
| Grosor máximo de cristal | 10 mm |
| Uso declarado | Agua dulce y agua marina |
| Control | Controlador cableado incluido |
| Comunicación de red | La web oficial enlaza una aplicación; no está confirmado que la Tourbon 60 de Veril sea compatible con ella |

La Tourbon 60 es la bomba de circulación seleccionada para el display de Veril. El caudal máximo es una cifra de catálogo, no una medición de caudal útil dentro de la urna. La roca, el nivel, la orientación, la altura, el sustrato y los corales modificarán el movimiento real.

El manual público de la serie disponible describe la instalación, los modos, las protecciones y el mantenimiento, pero su tabla de parámetros muestra explícitamente las Tourbon 100 y 200 y no incluye una fila independiente para la Tourbon 60. La página oficial sí publica una tabla específica para esta variante: 24 V CC, 4.000 l/h, 3–15 W, cristal de hasta 10 mm y acuarios de 40–60 cm. Varias fichas comerciales publican **8 W** como consumo máximo, por lo que el consumo exacto se comprobará en la etiqueta y la fuente de la unidad recibida.

## Función en Veril

La bomba generará circulación interna alrededor de la roca, el corredor trasero, las microislas y la superficie. No sustituye al retorno: el retorno mantiene la renovación entre display y sump, mientras la Tourbon 60 distribuye el movimiento dentro del display y reduce zonas de acumulación.

El máximo nominal equivale aproximadamente a **42 veces** el volumen geométrico de 96 L. Ese múltiplo no será un objetivo de funcionamiento. La intensidad se establecerá por el comportamiento del agua y de los organismos, no por una relación fija entre litros por hora y litros de urna.

## Construcción y montaje

La bomba utiliza un conjunto compacto con rotor, eje, jaulas de flujo, casquillos y elementos elastoméricos. El eje se documenta como cerámico en las fichas técnicas disponibles. El soporte magnético permite fijarla al vidrio y orientar el cuerpo con varios ángulos.

La bomba trabaja mediante un adaptador externo de baja tensión y un controlador cableado. El cable de la bomba utiliza un conector de tres pines con el controlador; el adaptador se conecta después al controlador. No se conectará la bomba directamente a la red eléctrica.

## Modos de funcionamiento

El controlador incorpora cinco modos principales:

- **Flujo constante:** mantiene una salida continua con la intensidad seleccionada. Es el modo inicial más fácil de interpretar.
- **Flujo de onda:** aumenta y reduce progresivamente la velocidad. El tiempo de subida y bajada se regula mediante el control de frecuencia.
- **Modo pulsante:** alterna un pico de flujo con una reducción rápida hacia la potencia mínima. Puede producir una oscilación más marcada y desplazar el sustrato si se ajusta demasiado alto.
- **Modo aleatorio:** cambia de forma variable la velocidad y la intensidad hasta el máximo configurado. Es difícil comparar su efecto sin registrar observaciones durante un periodo suficiente.
- **Modo ciclo:** alterna automáticamente los cuatro modos anteriores y cambia al siguiente después de diez ciclos.

La frecuencia y la intensidad se regulan desde el controlador. El enlace de dos bombas, si se utiliza con otra unidad compatible, permite designar una unidad maestra y otra subordinada para generar ondas alternas. Veril utiliza una sola Tourbon 60, por lo que esa función no forma parte de la configuración.

## Funciones auxiliares del controlador

- **Pausa de alimentación:** una pulsación prolongada detiene la bomba durante aproximadamente 20 minutos y después reanuda el modo seleccionado.
- **Modo nocturno:** un sensor de luz reduce el caudal cuando detecta poca iluminación ambiental. No conoce la hora ni el estado biológico del acuario.
- **Bloqueo:** impide cambiar accidentalmente la configuración desde los botones.

El controlador y el manual suministrado no documentan una interfaz de red, un protocolo, una API ni un procedimiento de emparejamiento con una aplicación. La web oficial sí incluye un enlace general de descarga de una aplicación, pero no identifica en esa página la compatibilidad concreta con la Tourbon 60 ni sustituye la verificación de la unidad recibida. El enlace entre dos controladores es una función local del equipo y no una integración de red.

## Protecciones documentadas

La electrónica incluye varias respuestas de protección:

- **Escasez de agua:** reduce la bomba a la velocidad más baja.
- **Rotor bloqueado o sucio:** detiene o limita el funcionamiento y vuelve a comprobar el estado aproximadamente cada 30 segundos hasta que se resuelva el bloqueo.
- **Tensión fuera de rango:** entra en protección si detecta una tensión inferior a 9 V o superior a 38 V en el circuito indicado por el manual.
- **Pérdida de fase:** detiene el motor si detecta una anomalía en los grupos de bobinas.
- **Controlador sin bomba conectada:** puede dejar el indicador de bloqueo parpadeando; para recuperar el funcionamiento se desconecta la alimentación, se conecta correctamente la bomba y se vuelve a alimentar el conjunto.

Estas protecciones no sustituyen la inspección. Una bomba parcialmente obstruida puede seguir moviendo agua sin aportar el caudal previsto.

## Integración física en Veril

La bomba se instalará en:

- lateral izquierdo del display;
- tercio superior, aproximadamente 8–12 cm bajo la superficie como punto de partida;
- orientación inicial hacia la derecha, ligeramente hacia atrás y hacia arriba;
- posición que cree renovación del corredor trasero sin golpear directamente el sustrato, el cristal opuesto o un coral.

La posición final se ajustará después de instalar la roca, el sustrato y el nivel operativo real. El cable y el imán deben permanecer accesibles para inspección, retirada y limpieza.

La colocación se aceptará cuando:

- la superficie presente movimiento continuo sin salpicaduras;
- el corredor trasero reciba renovación sin crear un chorro aislado;
- no haya zonas de detrito que permanezcan inmóviles de forma persistente;
- el sustrato no se desplace continuamente ni forme cráteres;
- las microislas no vibren ni reciban un flujo que desplace sus organismos;
- el flujo no retraiga de forma sostenida a los corales ni los golpee directamente;
- la bomba no produzca vibración anómala, ruido creciente o calentamiento excesivo.

## Puesta en marcha

1. Limpiar y secar el vidrio en la zona de montaje.
2. Conectar el cable de tres pines de la bomba al controlador antes de alimentar el sistema.
3. Conectar el adaptador de baja tensión al controlador y después a la red.
4. Montar las dos partes del imán lentamente y de forma desplazada, evitando atrapamientos de los dedos y golpes sobre el vidrio.
5. Comenzar en flujo constante y con la intensidad mínima que permita observar el recorrido del agua.
6. Comprobar la superficie, el corredor trasero, el sustrato y las zonas protegidas.
7. Registrar cada cambio de intensidad, modo u orientación por separado.

Los modos de pulsos, onda, aleatorio y ciclo se probarán solo después de validar la orientación básica. No se cambiarán a la vez el modo, la posición y la geometría de la roca, porque se perdería la capacidad de interpretar el efecto.

## Mantenimiento

Antes de manipular la bomba se desconectará el adaptador de la red. Para la limpieza:

1. Retirar el imán exterior con cuidado y separar las dos partes.
2. Extraer las tapas de los impulsores siguiendo el sentido indicado por el manual.
3. Retirar jaulas de flujo, casquillos, gomas y rotor.
4. Eliminar algas, carbonato, sustrato y detrito sin dañar el eje cerámico ni las superficies de apoyo.
5. Comprobar que el rotor gira libremente y que las gomas permanecen asentadas.
6. Montar de nuevo el conjunto y probarlo en agua antes de devolverlo a su posición definitiva.

Se revisará la bomba si aparece pérdida progresiva de caudal, ruido, vibración, reinicios del controlador, funcionamiento intermitente o aumento de temperatura. La limpieza no se hará únicamente por calendario: también se activará por cambios observables de rendimiento.

## Integración eléctrica y supervisión

El controlador no dispone de una integración de red documentada. El adaptador se conectará a una unidad independiente del [SONOFF S60ZBTPF](../sonoff-s60zbtpf/sonoff-s60zbtpf.md) para permitir un corte general y una supervisión eléctrica, pero el enchufe no sustituirá al controlador ni se utilizará para crear las ondas o las pausas de alimentación.

La integración detallada con Home Assistant y el [SONOFF S60ZBTPF](../sonoff-s60zbtpf/sonoff-s60zbtpf.md), incluyendo calibración de consumo, alarmas y pruebas de recuperación, está documentada en la [ficha de integración de la Tourbon 60](home-assistant-zigbee2mqtt.md). El consumo eléctrico no demuestra que el rotor esté entregando el caudal correcto: la supervisión debe complementarse con observación del flujo y mantenimiento del conjunto.

## Experiencia de uso y evidencia disponible

La evidencia práctica específica de la Tourbon 60 es muy escasa. No se ha localizado una prueba independiente que publique caudal medido, consumo real, nivel de ruido, temperatura o duración del conjunto bajo condiciones controladas.

La página oficial de Mantis muestra una única reseña de usuario, fechada el 25 de julio de 2024, que indica que el control mediante la aplicación es fácil y cómodo. No identifica de forma visible la variante utilizada, no aporta mediciones ni describe el acuario. La reseña se conserva como indicio de experiencia de control, pero no valida la compatibilidad de la Tourbon 60 de Veril con la aplicación ni permite valorar su rendimiento.

Coral Center y AQ-Arium publican para la Tourbon 60 un caudal máximo de 4.000 l/h, 8 W, 24 V CC y compatibilidad con cristal de hasta 10 mm. Coral Center añade unas dimensiones de 67 mm de longitud, 55 mm de diámetro y 10,3 mm para el imán exterior. AQ-Arium especifica además el contenido comercial del conjunto: adaptador, motor húmedo, controlador, imán y manual. Son fichas comerciales, no ensayos independientes.

El vídeo de AquariumWorldEsp muestra un desembalaje, instalación y prueba de una **Tourbon 200**, no de la Tourbon 60. Permite observar el controlador, la selección de modos, la regulación por porcentaje y una percepción subjetiva de un flujo intenso con la unidad ajustada al 40 %. El autor no mide caudal, ruido ni consumo, y sus observaciones no se trasladan a la Tourbon 60. Se conserva como evidencia práctica de la interfaz y del comportamiento general de la familia, no como validación del modelo seleccionado.

Existe una experiencia publicada con una **Tourbon 100**, distinta de la Tourbon 60, instalada en un acuario marino y ajustada al 60 % de su caudal nominal. No aporta mediciones de ruido, caudal real ni durabilidad y no se utilizará para transferir resultados a la Tourbon 60.

Las páginas comerciales que describen la Tourbon 60 repiten principalmente las especificaciones del producto. Las afirmaciones de funcionamiento silencioso, durabilidad y bajo calentamiento se consideran características declaradas, no resultados independientes.

Por tanto, la aceptación de la unidad de Veril se basará en una prueba propia:

- registrar consumo si se dispone de medidor;
- observar ruido y vibración en silencio ambiental;
- comprobar el movimiento con partículas inocuas o alimento antes de introducir animales;
- comprobar la respuesta de el sustrato y de las microislas;
- registrar el comportamiento del controlador en modo constante y en un modo variable;
- repetir la observación después de la primera limpieza.

## Limitaciones

- El caudal de 4.000 l/h es nominal y no equivale al caudal real dentro del aquascape.
- No se dispone de un mapa hidráulico ni de una medición de distribución para la urna de Veril.
- El sensor nocturno depende de la iluminación ambiental y puede activarse de forma no prevista si cambia la luz de la habitación.
- Las protecciones electrónicas no detectan todas las pérdidas de rendimiento causadas por suciedad o desgaste.
- La compatibilidad del imán debe comprobarse sobre el espesor y el cristal reales de la urna.
- La bomba no debe funcionar fuera del agua para probarla.
- La ausencia de una prueba independiente de ruido y durabilidad impide convertir “ultrasilenciosa” o “duradera” en criterios garantizados.

## Fuentes

- [Mantis Aquarium: Tourbon Wave Pump](https://mantisaquarium.com/wave-pump/)
- [Mantis Aquarium: ficha oficial de Tourbon Wave Pump](https://mantisaquarium.com/wave-pump/tourbon-wave-pump/)
- [Mantis Aquarium: página general del fabricante](https://mantisaquarium.com/)
- [Manual de la serie Mantis Tourbon](mantis-tourbon-manual.pdf)
- [Manual público de la serie Tourbon](https://www.aquaticline.es/wp-content/uploads/sites/3/2021/07/Instrucciones-Nuevas-Tourbon-Series-1.pdf)
- [Tropical Nature: Tourbon 60, 4.000 l/h](https://tropicalnature.it/en/product-detail/6317/pumps-movement/mantis-tourbon-60-4000l-h)
- [A.G.P.: Tourbon 60 / 100 / 200](https://www.agpsrl.eu/apparecchiature-tecniche/pompe-di-movimento/tourbon-60-100-200.html)
- [Aquaristic Online: Mantis Tourbon Wavemaker 60](https://www.aquaristiconline.com.au/collections/mantis/products/mantis-tourbon-wavemaker-60)
- [DaniReef: experiencia con una Tourbon 100 en un acuario marino](https://forum.danireef.com/viewtopic.php?f=34&t=34195) — variante distinta, no transferible a la Tourbon 60
- [Coral Center: Mantis Tourbon Pump](https://coralcenter.es/producto/equipamiento/bombas/bombas-de-movimiento/mantis-tourbon-pump/)
- [AQ-Arium: Tourbon Wave Pump Mantis, nueva versión](https://www.aq-arium.com/aqmarine/acuario-marino/tourbon-wave-pump-mantis-nueva-version/)
- [AquariumWorldEsp: unboxing y prueba de una Tourbon 200](https://www.youtube.com/watch?v=IjscbS5rOH8) — variante distinta, no transferible a la Tourbon 60
- [Hidráulica de Veril](../../../02_veril/03_hidraulica.md)
