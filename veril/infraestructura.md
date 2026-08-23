# Veril: infraestructura

> La [dimensión de infraestructura](../fichas/dimensiones/dimension-infraestructura.md) define la organización física del sistema. Esta ficha registra cómo se concreta en Veril y remite los detalles de producto y fabricación a sus documentos propietarios.

## Configuración adoptada

Veril utiliza una urna AIO de pequeño volumen con un compartimento técnico lateral integrado. El display tiene aproximadamente **60 × 32 × 40 cm**. La zona técnica forma parte de la misma urna y aloja el recorrido de entrada, el skimmer, el calentador, el retorno, el ATO y los sensores.

La distribución concreta de las cámaras está documentada en la [técnica de la urna](../fichas/hardware/urna/tecnica.md). Esta ficha conserva únicamente sus consecuencias sobre volumen funcional, acceso, niveles, seguridad y mantenimiento.

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
