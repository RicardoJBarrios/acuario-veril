# Veril: hidráulica

> La [dimensión hidráulica](../../01_verilpedia/01_dimensiones/03_hidraulica.md) define el régimen de movimiento, renovación y transporte del agua. La [dimensión de procesamiento](../../01_verilpedia/01_dimensiones/07_procesamiento.md) utiliza las condiciones hidráulicas para conectar las superficies activas y los mecanismos de exportación. La [dimensión de infraestructura](../../01_verilpedia/01_dimensiones/01_infraestructura.md) establece los límites del retorno, los niveles y la seguridad. Esta ficha registra la implementación hidráulica de Veril.

## Objetivo de diseño

La circulación prevista deberá rodear, atravesar y pasar por debajo de la estructura, manteniendo renovadas las distintas zonas del display sin generar chorros concentrados ni áreas permanentemente estancadas.

La superficie deberá presentar un movimiento amplio y continuo, con ondulaciones moderadas y sin aspiración persistente de aire.

## Estado de la decisión

**Adoptado:** La circulación de Veril combina la Mantis Tourbon 60 instalada para movimiento y la Jebao DC-650 instalada para retorno. El nivel de la cámara de retorno se estabiliza mediante el [D-D H2Ocean Compact ATO Gen 2 (DDATO2)](../../01_verilpedia/04_hardware/dd-h2ocean-compact-ato-gen-2/dd-h2ocean-compact-ato-gen-2.md).

**Previsto:** El campo de flujo deberá rodear, atravesar y pasar por debajo de la composición espacial, manteniendo renovadas las zonas funcionales sin desplazar el sustrato.

**Observado:** La [prueba dinámica del 17 de septiembre](../../04_operaciones/2026/09/2026-09-17.md#prueba-dinámica-de-circulación), con la Tourbon entonces al 40 %, mostró partículas finas en superficie recorriendo un circuito circular alrededor de la roca.

**Pendiente:** La distribución real en huecos, corredor trasero y zonas inferiores, el tiempo de renovación, la respuesta del sustrato, el volumen de retrosifonado y el reinicio tras una parada deben validarse con la composición instalada.

### Identificación y caudal del retorno

El **19 de octubre de 2026** el propietario corrigió la identificación de la bomba instalada: es una **Sicce Micra**, no una Micra Plus. Encontró su filtro bastante obstruido, lo lavó y reinstaló la bomba. Las recogidas manuales en el pico de pato dieron **500 ml en 15 s antes (120 L/h)** y **850 ml en 10 s después (306 L/h)**. Sobre los 60 L nominales del display son **2 y 5,1 veces/h**; sobre los 75 L nominales del sistema completo, **1,6 y 4,08 veces/h**. Son referencias de caudal medidas en esa intervención, sin demostrar renovación uniforme ni estabilidad a largo plazo.

El propietario consideró insuficiente el caudal inicial y comunicó la compra de una **Jebao DC Pump Marine Aqua DC-650** el 19/10/2026. El 31/10/2026 comunicó que instaló la DC-650, retiró, limpió y guardó la Sicce Micra, y comprobó y validó el funcionamiento de la nueva bomba. No se comunicaron ajustes ni mediciones de caudal de esta instalación. La [operación del 19 de octubre](../../04_operaciones/2026/10/2026-10-19.md#limpieza-y-medición-del-caudal-de-retorno) conserva la evidencia del equipo anterior; la [operación del 31 de octubre](../../04_operaciones/2026/10/2026-10-31.md#instalación-del-ato-y-sustitución-de-la-bomba-de-retorno) registra la sustitución. Las especificaciones de la Micra Plus documentada anteriormente no se atribuyen a la Micra.

### Disposición y ajuste vigente de la Mantis

La Mantis Tourbon 60 está instalada con esta disposición y ajuste vigente:

- A unos **12 cm** del borde del acuario, interpretados junto con un nivel de agua situado aproximadamente 37 mm por debajo de dicho borde.
- A unos **53 mm** de la parte trasera, menos el grosor del cristal trasero.
- Orientada hacia el frente.
- `Constant mode`, `Flow percent: 50 %`, `Cycle: 0,4 s` y `Master` configurado.

El 17 de septiembre se documentó el ajuste anterior de 40 % y el 18 de septiembre se cambió el porcentaje al 50 %. Los demás valores de esta lista son los últimos comunicados y no se han vuelto a comprobar durante ese cambio.

La salida del retorno se describe como situada en la parte superior derecha del display, en continuidad con la cámara Retorno. El efecto conjunto de las bombas se ha observado en superficie, pero la aceptación de renovación de todas las zonas sigue pendiente de pruebas específicas.

Para describir la escala del display se adopta la referencia redondeada de **unos 60 L con arena** (cálculo geométrico detallado: aproximadamente 59,86 L bajo la hipótesis de 3 cm de arena y 2 cm de margen libre). El volumen nominal del sistema completo se estima en **unos 75 L**, incluidas las cámaras técnicas. Son referencias aproximadas, no mediciones exactas. Esta cifra del display sirve para interpretar la escala del movimiento interno, pero no convierte el caudal nominal en una renovación uniforme de todo el volumen. El cálculo y sus límites constan en la [operación del 23 de septiembre](../../04_operaciones/2026/09/2026-09-23.md#pesaje-y-medición-del-desplazamiento-del-hardscape).

Con la composición instalada, la trayectoria esperada será:

```text
retorno superior derecho → zona superior y abierta → lateral izquierdo
      → descenso y zona frontal → lateral derecho → retorno técnico
```

Este esquema es una simulación cualitativa basada en la geometría disponible y no un cálculo CFD. Puede funcionar como circulación circular si las boquillas se orientan tangencialmente y no enfrentadas entre sí. La orientación final deberá evitar que el retorno cree un cortocircuito inmediato hacia la entrada técnica y que la Tourbon proyecte todo su caudal contra una cara rocosa.

La masa rocosa deja un corredor perimetral mínimo de **40 mm** en frontal y trasera y de **30 mm** en los laterales. Estos márgenes son suficientes para conservar una ruta potencial de circulación, pero no demuestran por sí solos que el agua se renueve. La terraza central y la torre derecha son los puntos con mayor probabilidad de producir zonas de baja velocidad debajo, detrás o en sus encuentros con la base.

Como referencia para futuras pruebas, una orientación alternativa podría:

- Retorno dirigido a lo largo de la zona abierta, con una ligera componente hacia la superficie
- Tourbon dirigida desde el lateral izquierdo hacia la zona derecha, con una ligera inclinación hacia el frente o hacia abajo
- Evitar un chorro perpendicular contra la pared rocosa principal
- Mantener libre el paso bajo la terraza central y el corredor trasero

La orientación exacta podrá invertirse durante la prueba si el movimiento observado demuestra que el giro se cierra en la superficie pero deja sin renovación el corredor, el arco o la base de la torre.

### Escenarios de caudal para el display de 60 L

La Tourbon 60 declara hasta **4.000 L/h**. Como referencia de ajuste, los porcentajes siguientes equivalen aproximadamente a estas relaciones sobre los 60 L del display:

| Ajuste Tourbon | Caudal nominal aproximado | Relación nominal sobre el display |
| ---: | ---: | ---: |
| 40 % | 1.600 L/h | 27 veces por hora |
| 50 % | 2.000 L/h | 33 veces por hora |
| 60 % | 2.400 L/h | 40 veces por hora |
| 80 % | 3.200 L/h | 53 veces por hora |
| 100 % | 4.000 L/h | 67 veces por hora |

La bomba de retorno aporta un caudal real inferior a su máximo nominal cuando se consideran altura, tubo, curvas y restricciones. La cifra final no se sumará como si todo el caudal atravesara cada punto del display: la Tourbon produce movimiento interno y la bomba de retorno aporta renovación desde el compartimento técnico.

El ajuste inicial recomendado para la prueba será **40–50 % de la Tourbon**. Se podrá explorar el entorno de **50–60 %** si no se desplaza la arena y las zonas inferiores necesitan más renovación. No se utilizará el 80–100 % como punto de partida.

### Riesgos que deben comprobarse

- La plataforma central puede desviar el flujo por arriba y dejar una zona protegida debajo
- La torre derecha puede formar una bolsa de baja renovación en su parte posterior
- El corredor trasero de 40 mm puede transportar el agua, pero también concentrar detritos si no recibe suficiente velocidad
- La salida del retorno puede crear un circuito corto hacia la entrada técnica si apunta hacia el separador
- La Tourbon puede desplazar la cama de arena de 3 cm si apunta directamente al sustrato o a una salida del arco

La aceptación hidráulica requerirá comprobar el movimiento en superficie, el paso bajo la terraza, el corredor trasero, la cara posterior de la torre y las zonas alrededor de la isla. Se utilizará una pequeña cantidad de partículas inertes y se observará si quedan suspendidas, avanzan hacia la entrada o se depositan repetidamente en el mismo punto.

## Nivel, retorno y seguridad

### Alimentación y protección eléctrica del retorno

La toma SONOFF S60ZBTPF `off-act-02`, integrada mediante Zigbee2MQTT, está asociada en Home Assistant a la bomba de retorno Jebao DC-650 desde el 31/10/2026. La toma apareció `ON` y comunicó 9,74 W ese día; esta lectura no mide el caudal. La configuración local vigente del enchufe es:

- `inching_control`: `DISABLE`; `inching_mode`: `OFF`.
- Protección de la toma (`outlet_control_protect`): activada.
- Protección por máximo de potencia: activada, **20 W**.
- Protección por máximo de corriente: activada, **0,3 A**.
- Límites mínimos de potencia/corriente y límites de tensión mínimo/máximo: desactivados.

Estos máximos se eligieron a partir del histórico de la bomba anterior en Veril, no son especificaciones del fabricante ni umbrales universalmente seguros: se observaron 6,50 W de potencia mediana, 7,27 W de máximo y 0,05–0,06 A en las muestras positivas de corriente. Tras la sustitución por la DC-650, los límites de 20 W y 0,3 A siguen configurados, pero su adecuación a la nueva bomba no se ha establecido con la lectura aislada de 9,74 W. No se ha probado deliberadamente el disparo de la protección. La protección eléctrica tampoco confirma caudal, nivel, cebado o funcionamiento hidráulico.

La configuración fue aplicada y leída de vuelta en Zigbee2MQTT el 29/09/2026; en esa lectura el enchufe aparecía `OFF`, 0 W y 0 A. El registro describe el momento, la telemetría y sus límites: [ajuste de protección del enchufe del retorno](../../04_operaciones/2026/09/2026-09-29.md#ajuste-de-la-protección-del-enchufe-del-retorno). La correspondencia física de la etiqueta sigue pendiente, según el inventario de `off-act-02`.

El display tendrá un margen libre suficiente para admitir el movimiento del agua sin salpicaduras ni desbordamientos. La evaporación se compensará en la cámara de retorno mediante el ATO.

Cuando la bomba de retorno se detenga, el agua ocupará parcialmente el compartimento técnico. La instalación deberá conservar un margen seguro para el volumen de retrosifonado y permitir el reinicio de la bomba sin aspiración de aire persistente.

La aceptación de estos niveles y del volumen de parada pertenece a la [dimensión de infraestructura](../../01_verilpedia/01_dimensiones/01_infraestructura.md).

## Reposición automática y consecuencias hidráulicas

Veril utilizará el [D-D H2Ocean Compact ATO Gen 2 (DDATO2)](../../01_verilpedia/04_hardware/dd-h2ocean-compact-ato-gen-2/dd-h2ocean-compact-ato-gen-2.md), con un [depósito GRAF de 15 litros](../../01_verilpedia/04_hardware/dd-h2ocean-compact-ato/graf-barril-agroalimentario-15l.md) reservado para agua RO/DI. El sensor se instalará en la cámara de retorno, donde la evaporación modifica directamente el nivel que condiciona la bomba de retorno.

Su consecuencia hidráulica principal será mantener el nivel operativo de la cámara de retorno dentro del rango del que dependen la aspiración de la bomba y la continuidad del retorno. Las funciones y especificaciones de la unidad DDATO2 se documentan en su [ficha Gen 2](../../01_verilpedia/04_hardware/dd-h2ocean-compact-ato-gen-2/dd-h2ocean-compact-ato-gen-2.md); la ficha del Compact ATO anterior conserva los datos de esa generación. La aplicación en Veril y la [dimensión de infraestructura](../../01_verilpedia/01_dimensiones/01_infraestructura.md) describen la ubicación prevista del sensor y el equipo.

El ATO no aumenta la circulación, no sustituye la prueba de parada ni corrige por sí mismo la salinidad. La autonomía real del depósito y la respuesta del nivel durante el funcionamiento y los cortes quedan pendientes de validación en la instalación final.

## Corredor trasero

Existirá una ruta continua detrás de la estructura, con entrada y salida, que forme parte de la circulación general y permita renovar el agua y evacuar detritos.

La continuidad del corredor se comprobará después de colocar la roca y antes de fijar la composición definitiva.

## Equipos y configuración

La [Mantis Tourbon 60](../../01_verilpedia/04_hardware/mantis-tourbon-60/mantis-tourbon-60.md) es la bomba principal de movimiento. La [Jebao DC-650](../../01_verilpedia/04_hardware/jebao-dc-650/jebao-dc-650.md) es la bomba de retorno instalada; el propietario informó que comprobó y validó su funcionamiento. El ATO DDATO2 está instalado y su bomba se encuentra en un barril de 15 L con unos 10 L de agua RODI, según la operación del 31/10/2026. Los niveles y la respuesta durante ciclos siguen formando parte de la aceptación hidráulica.

La bomba de retorno ya dispone de su tubo instalado. El [tubo Eheim adquirido](../../01_verilpedia/05_productos/07_eheim-4005843/eheim-4005843.md), de **3 m y 16/22 mm**, referencia **4005843**, es material auxiliar para llenar el display, trasvasar agua y mover agua entre recipientes o cámaras durante el montaje y el mantenimiento. No forma parte del recorrido hidráulico permanente del retorno.

La bomba principal generará circulación global y turbulencias distribuidas. El retorno constituirá un segundo vector de flujo integrado con ella.

La entrada del retorno estará protegida por una rejilla circular. La salida utilizará una boquilla plana y ensanchada, formada por varias secciones orientables, cuya función será distribuir el flujo sin crear una corriente dominante.

El comportamiento final depende de la resistencia real del circuito, la disposición de la estructura y la relación entre ambas bombas. El ajuste actual de la Mantis está documentado, pero la aceptación de la regulación hidráulica sigue pendiente de pruebas que cubran todas las zonas del conjunto.

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

La circulación deberá conservar capacidad de adaptación a los cambios de rugosidad y ocupación que produzca el crecimiento biológico. La relación entre crecimiento, población y carga se documenta en [biología](06_biologia.md).

La posición de la roca y la forma de la playa y el canal se documentan en la [dimensión espacial de Veril](02_espacial.md). La distribución de luz sobre las superficies se documenta en [iluminación](04_iluminacion.md).

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
- Niveles compatibles con la [dimensión de infraestructura](../../01_verilpedia/01_dimensiones/01_infraestructura.md)

## Fuentes de diseño

- [Técnica de la urna](../../01_verilpedia/04_hardware/urna/tecnica.md)
- [Ficha de la Mantis Tourbon 60](../../01_verilpedia/04_hardware/mantis-tourbon-60/mantis-tourbon-60.md)
- [Ficha de la Sicce Micra](../../01_verilpedia/04_hardware/sicce-micra/sicce-micra.md)
- [Ficha de la Jebao DC-650](../../01_verilpedia/04_hardware/jebao-dc-650/jebao-dc-650.md): instalada como bomba de retorno
- [Ficha de la Sicce Micra Plus 600](../../01_verilpedia/04_hardware/sicce-micra-plus-600/sicce-micra-plus-600.md): referencia anterior; sus especificaciones no corresponden a la Sicce Micra retirada ni a la Jebao DC-650 instalada
