# Veril: infraestructura

> La [dimensión de infraestructura](../fichas/dimensiones/dimension-infraestructura.md) define la organización física del sistema. Esta ficha registra cómo se concreta en Veril y remite los detalles de producto y fabricación a sus documentos propietarios.

## Configuración adoptada

Veril utiliza una urna AIO de pequeño volumen con un compartimento técnico lateral integrado. El display tiene aproximadamente **60 × 32 × 40 cm**. La zona técnica forma parte de la misma urna y aloja el recorrido de entrada, el skimmer, el calentador, el retorno, el ATO y los sensores.

La distribución concreta de las cámaras está documentada en la [técnica de la urna](../fichas/hardware/urna/tecnica.md). Esta ficha conserva únicamente sus consecuencias sobre volumen funcional, acceso, niveles, seguridad y mantenimiento.

## Entorno de instalación

Veril se instalará en un despacho de aproximadamente **9 m²**, situado en Santa Cruz de Tenerife, en la cuarta planta de un edificio de cinco. El despacho dispone de una ventana de dos hojas con cristal esmerilado, sin persianas ni cortinas, orientada a un patio interior, además de aire acondicionado portátil y ventilador de techo. Se utiliza habitualmente durante jornadas superiores a diez horas. La urna se sitúa a la izquierda del escritorio. También contiene un rack, una impresora 3D y una cantidad importante de equipo informático que permanece encendido total o parcialmente durante la jornada.

Este entorno forma parte de las condiciones físicas de la instalación porque puede afectar a:

- La temperatura del agua y la capacidad de disipar el calor de la iluminación y los equipos sumergidos
- La carga térmica acumulada del rack, la impresora 3D y el equipo informático
- La evaporación y el consumo del depósito del ATO
- La humedad ambiental, la condensación y la corrosión de elementos próximos
- La incidencia de radiación solar directa o indirecta sobre la urna
- La ventilación, las corrientes de aire y la distribución térmica del despacho
- El ruido y la convivencia entre el acuario, el aire acondicionado y la ocupación prolongada del espacio

El rack, la impresora 3D y el equipo informático se considerarán fuentes adicionales de calor. Su efecto dependerá de la potencia realmente disipada, el tiempo de funcionamiento, la proximidad a la urna y la capacidad de renovación del aire. La impresora 3D puede introducir además necesidades específicas de ventilación durante su funcionamiento, que se evaluarán sin asumir que el aire del despacho es térmicamente o ambientalmente neutro.

La ventana puede intervenir en la ventilación del despacho, pero no se considerará por sí sola una fuente de refrigeración controlada. Al dar a un patio interior y encontrarse en una planta alta, la exposición solar directa puede ser distinta de la de una fachada exterior abierta, aunque seguirá existiendo entrada de luz ambiental y posibles ganancias térmicas. El cristal esmerilado limita la visibilidad y difunde parcialmente la luz, pero no debe interpretarse como una protección solar equivalente a una persiana o cortina. La radiación incidente y su efecto real sobre la temperatura de la urna se evaluarán en el funcionamiento cotidiano.

El aire acondicionado portátil se sitúa en el suelo, a la derecha de la urna y entre esta y la ventana. Su tubo de extracción conduce el aire caliente al exterior a través de la ventana. Se considerará un medio de control ambiental del despacho y una fuente local de movimiento y descarga térmica, no un sustituto del control térmico del acuario. Su posición debe conservar espacio suficiente para la extracción, el acceso y la ausencia de obstrucciones.

El ventilador de techo se considerará un medio de distribución del aire del despacho. No se dirigirá un chorro de aire de forma continua hacia la superficie del agua, la urna o los sensores sin evaluar antes sus efectos sobre evaporación, salpicaduras, lecturas y estabilidad.

La temperatura objetivo del agua y su justificación se documentan en la [configuración integrada](configuracion.md#régimen-térmico-adoptado). Las consecuencias sobre evaporación y circulación se mantienen en las fichas específicas de [hidráulica](hidraulica.md) y [química](quimica.md).

## Estado de la decisión

**Adoptado:** Se mantiene como línea de Veril una urna AIO lateral de pequeño volumen, con el compartimento técnico integrado en la propia urna.

**Previsto:** La zona técnica alojará la entrada, el skimmer, el calentador, el retorno, el ATO y los sensores según la distribución documentada en la ficha técnica.

**Pendiente:** Aún deben comprobarse en la instalación final la estabilidad del soporte, los niveles operativos, el volumen de retrosifonado, el reinicio tras una parada y el acceso real para mantenimiento.

## Documentos propietarios

- [Display de la urna](../fichas/hardware/urna/display.md): dimensiones, volumen y características del display
- [Técnica de la urna](../fichas/hardware/urna/tecnica.md): cámaras, recorrido, equipos y niveles
- [Fabricación de la urna](../fichas/hardware/urna/fabricacion.md): construcción, soporte y comprobaciones físicas
- [Configuración integrada](configuracion.md): relación de esta infraestructura con las demás dimensiones

## Consecuencias para Veril

La arquitectura AIO lateral determina que:

- El volumen técnico no pueda tratarse como un sump externo independiente
- La cámara de retorno sea el punto crítico para evaporación, ATO, nivel mínimo y aspiración de aire
- El espacio disponible para equipos y mantenimiento esté limitado por la anchura de las cámaras
- La posición de la roca y el sustrato deba conservar acceso a la rejilla, las cámaras y los equipos
- La parada del retorno deba comprobarse junto con el volumen de retrosifonado y el margen libre
- La limpieza y la retirada de equipos formen parte de la aceptación de la configuración

Estas consecuencias no sustituyen las pruebas de la urna ni las fichas de los equipos. La aceptación se realizará mediante comprobaciones físicas, de niveles, de parada, de reinicio y de acceso.

## Criterios de aceptación pendientes

- La urna y su soporte mantienen la geometría y la estabilidad previstas
- Las tres cámaras conservan el acceso necesario para retirar y mantener sus equipos
- El compartimento técnico recibe el volumen de retrosifonado sin desbordarse
- El retorno reinicia sin aspiración persistente de aire
- El sensor del ATO y los sensores de temperatura permanecen accesibles
- La roca y el sustrato no bloquean entradas, pasos, rejillas ni equipos
- La limpieza ordinaria puede realizarse sin desmontar innecesariamente el sistema

El estado de estas comprobaciones se actualizará cuando se realice el montaje y las pruebas correspondientes.
