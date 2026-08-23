# Veril: hidráulica

> La [dimensión hidráulica](../fichas/dimensiones/dimension-hidraulica.md) define el régimen de movimiento, renovación y transporte del agua. La [dimensión de procesamiento](../fichas/dimensiones/dimension-procesamiento.md) utiliza las condiciones hidráulicas para conectar las superficies activas y los mecanismos de exportación. La [dimensión de infraestructura](../fichas/dimensiones/dimension-infraestructura.md) establece los límites del retorno, los niveles y la seguridad. Esta ficha registra la implementación hidráulica de Veril.

## Objetivo de diseño

La circulación prevista deberá rodear, atravesar y pasar por debajo de la estructura, manteniendo renovadas las distintas zonas del display sin generar chorros concentrados ni áreas permanentemente estancadas.

La superficie deberá presentar un movimiento amplio y continuo, con ondulaciones moderadas y sin aspiración persistente de aire.

## Estado de la decisión

**Adoptado:** La circulación de Veril combinará la Mantis Tourbon 60 para movimiento y la Sicce Micra Plus 600 para retorno. El nivel de la cámara de retorno se estabilizará mediante el [D-D H2Ocean Compact ATO](../fichas/hardware/dd-h2ocean-compact-ato/dd-h2ocean-compact-ato.md), definido físicamente en Infraestructura.

**Previsto:** El campo de flujo deberá rodear, atravesar y pasar por debajo de la composición espacial, manteniendo renovadas las zonas funcionales sin desplazar el sustrato.

**Pendiente:** La distribución real, el comportamiento del corredor trasero, el tiempo de renovación, la respuesta del sustrato, el volumen de retrosifonado y el reinicio tras una parada deben validarse con la composición instalada.

## Nivel, retorno y seguridad

El display tendrá un margen libre suficiente para admitir el movimiento del agua sin salpicaduras ni desbordamientos. La evaporación se compensará en la cámara de retorno mediante el ATO.

Cuando la bomba de retorno se detenga, el agua ocupará parcialmente el compartimento técnico. La instalación deberá conservar un margen seguro para el volumen de retrosifonado y permitir el reinicio de la bomba sin aspiración de aire persistente.

La aceptación de estos niveles y del volumen de parada pertenece a la [dimensión de infraestructura](../fichas/dimensiones/dimension-infraestructura.md).

## Reposición automática y consecuencias hidráulicas

Veril utilizará el [D-D H2Ocean Compact ATO](../fichas/hardware/dd-h2ocean-compact-ato/dd-h2ocean-compact-ato.md), con un [depósito GRAF de 15 litros](../fichas/hardware/dd-h2ocean-compact-ato/graf-barril-agroalimentario-15l.md) reservado para agua RO/DI. El sensor se instalará en la cámara de retorno, donde la evaporación modifica directamente el nivel que condiciona la bomba de retorno.

Su consecuencia hidráulica principal será mantener el nivel operativo de la cámara de retorno dentro del rango del que dependen la aspiración de la bomba y la continuidad del retorno. Las protecciones, la autonomía, los riesgos de sobrellenado, el sifonado, el funcionamiento en seco y la limpieza de sensores pertenecen a la [ficha del ATO](../fichas/hardware/dd-h2ocean-compact-ato/dd-h2ocean-compact-ato.md) y a la [dimensión de infraestructura](../fichas/dimensiones/dimension-infraestructura.md).

El ATO no aumenta la circulación, no sustituye la prueba de parada ni corrige por sí mismo la salinidad. La autonomía real del depósito y la respuesta del nivel durante el funcionamiento y los cortes quedan pendientes de validación en la instalación final.

## Corredor trasero

Existirá una ruta continua detrás de la estructura, con entrada y salida, que forme parte de la circulación general y permita renovar el agua y evacuar detritos.

La continuidad del corredor se comprobará después de colocar la roca y antes de fijar la composición definitiva.

## Equipos y configuración

La [Mantis Tourbon 60](../fichas/hardware/mantis-tourbon-60/mantis-tourbon-60.md) será la bomba principal de movimiento. La [Sicce Micra Plus 600](../fichas/hardware/sicce-micra-plus-600/sicce-micra-plus-600.md) será la bomba de retorno.

La bomba principal generará circulación global y turbulencias distribuidas. El retorno constituirá un segundo vector de flujo integrado con ella.

La entrada del retorno estará protegida por una rejilla circular. La salida utilizará una boquilla plana y ensanchada, formada por varias secciones orientables, cuya función será distribuir el flujo sin crear una corriente dominante.

El comportamiento final dependerá de la resistencia real del circuito, la disposición de la estructura y la relación entre ambas bombas. La regulación operativa se comprobará una vez montado el conjunto.

## Rutas que deben mantenerse funcionales

La circulación deberá alcanzar de forma conectada:

- La superficie
- Las caras expuestas
- Los pasos y espacios inferiores
- El corredor trasero
- Las zonas situadas alrededor de las islas

La estructura deberá conservar rutas potenciales de renovación alrededor y, cuando proceda, a través de las masas. La existencia de un hueco no se considerará suficiente si el agua no se renueva en él.

## Gradiente hidráulico de referencia

| Zona | Flujo relativo deseado |
| --- | --- |
| Superficie | Medio-alto |
| Zonas altas y expuestas | Medio-alto y turbulento |
| Terrazas y caras abiertas | Medio |
| Interior de pasos | Bajo-medio |
| Refugios profundos | Bajo |
| Espacios inferiores | Bajo-medio, pero renovado |
| Corredor trasero | Medio y continuo |

Una zona protegida puede tener flujo bajo, pero no deberá convertirse en un depósito permanente de agua estancada o detritos.

Estas condiciones son objetivos de diseño, no resultados demostrados. Su cumplimiento queda pendiente de las pruebas realizadas con la composición rocosa y el sustrato instalados.

## Adaptación al crecimiento

La circulación deberá conservar capacidad de adaptación a los cambios de rugosidad y ocupación que produzca el crecimiento biológico. La relación entre crecimiento, población y carga se documenta en [biología](biologia.md).

La posición de la roca y la forma de la playa y el canal se documentan en la [dimensión espacial de Veril](espacial.md). La distribución de luz sobre las superficies se documenta en [iluminación](iluminacion.md).

## Criterios de aceptación

Durante el montaje y las pruebas se comprobará:

- Movimiento superficial continuo sin aspiración persistente de aire
- Renovación alrededor y debajo de las masas
- Continuidad del corredor trasero
- Ausencia de chorros localizados que desplacen el sustrato o alteren la composición
- Ausencia de bolsas de agua sin renovación observable
- Ausencia de acumulaciones permanentes en pasos, refugios y espacios inferiores
- Funcionamiento coordinado de la bomba principal y el retorno
- Reinicio seguro después de una parada
- Niveles compatibles con la [dimensión de infraestructura](../fichas/dimensiones/dimension-infraestructura.md)

## Fuentes de diseño

- [Técnica de la urna](../fichas/hardware/urna/tecnica.md)
- [Ficha de la Mantis Tourbon 60](../fichas/hardware/mantis-tourbon-60/mantis-tourbon-60.md)
- [Ficha de la Sicce Micra Plus 600](../fichas/hardware/sicce-micra-plus-600/sicce-micra-plus-600.md)
