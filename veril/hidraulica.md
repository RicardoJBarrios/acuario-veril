# Veril: hidráulica

> La [dimensión hidráulica](../fichas/dimensiones/dimension-hidraulica.md) define el régimen de movimiento, renovación y transporte del agua. La [dimensión de procesamiento](../fichas/dimensiones/dimension-procesamiento.md) explica la función de la circulación en el transporte, la oxigenación y el procesamiento. La [dimensión de infraestructura](../fichas/dimensiones/dimension-infraestructura.md) establece los límites del retorno, los niveles y la seguridad. Esta ficha registra la implementación hidráulica de Veril.

## Objetivo de diseño

La circulación prevista deberá rodear, atravesar y pasar por debajo de la estructura, manteniendo renovadas las distintas zonas del display sin generar chorros concentrados ni áreas permanentemente estancadas.

La superficie deberá presentar un movimiento amplio y continuo, con ondulaciones moderadas y sin aspiración persistente de aire.

## Nivel, retorno y seguridad

El display tendrá un margen libre suficiente para admitir el movimiento del agua sin salpicaduras ni desbordamientos. La evaporación se compensará en la cámara de retorno mediante el ATO.

Cuando la bomba de retorno se detenga, el agua ocupará parcialmente el compartimento técnico. La instalación deberá conservar un margen seguro para el volumen de retrosifonado y permitir el reinicio de la bomba sin aspiración de aire persistente.

La aceptación de estos niveles y del volumen de parada pertenece a la [dimensión de infraestructura](../fichas/dimensiones/dimension-infraestructura.md).

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

## Adaptación al crecimiento

La circulación deberá conservar capacidad de adaptación a los cambios de rugosidad y ocupación que produzca el crecimiento biológico. La relación entre crecimiento, población y carga se documenta en [biología](biologia.md).

La posición de la roca que condiciona estas rutas se documenta en [roca](roca.md). La forma de la playa y el canal se documenta en [sustrato](sustrato.md). La distribución de luz sobre las superficies se documenta en [iluminación](iluminacion.md).

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
