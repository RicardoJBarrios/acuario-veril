# Control térmico de Veril

## Alcance y objetivo

Esta ficha describe el plan térmico vigente y su implementación piloto en Home Assistant. La temperatura que se intenta proteger es la del agua, medida por `off-sns-05`, cuya sonda está sumergida en la cámara del skimmer. El Rowenta climatiza el despacho; sus 24 o 25 °C son consignas del aire acondicionado, no objetivos directos del agua.

La envolvente adoptada para el agua es 25–26 °C como zona preferida, 24,5–26,5 °C como intervalo óptimo y 24–27,5 °C como intervalo aceptable. Desde 28 °C el criterio local es entrar en protección; 28,5, 29 y 30 °C corresponden a aviso, crítico y emergencia. Son bandas de gestión de Veril, no límites biológicos universales. La definición completa está en [Configuración integrada, régimen térmico](README.md#régimen-térmico-adoptado).

## Diseño del controlador

El control combina la temperatura real del agua con señales del entorno para adelantarse a la acumulación de calor. Los sensores `off-sns-01`, `off-sns-06` y `off-sns-08` describen tres ubicaciones del despacho y se evalúan por separado; la previsión horaria de Home Assistant aporta una señal anticipativa exterior. Ninguna de estas señales sustituye a una lectura válida del agua.

La instalación actual usa un único evaluador de estados. Las derivadas de temperatura del agua de 30 y 60 minutos se conservan fuera de los disparadores: todavía no se consideran suficientemente validadas para decidir órdenes. El estado térmico del agua y el estado de la telemetría son cuestiones distintas.

## Lógica piloto instalada

| Condición de entrada o salida | Estado/acción del Rowenta |
| --- | --- |
| Agua ≥27,0 °C durante 10 min y, además, 2 de 3 sensores ambientales frescos ≥29,0 °C; o previsión horaria ≥30,0 °C dentro de las próximas 6 h | Preventivo: frío, consigna 25 °C, ventilador alto |
| Agua ≥27,5 °C durante 5 min | Refrigeración: frío, consigna 25 °C, ventilador alto |
| Agua ≥28,0 °C | Protección: frío, consigna 24 °C, ventilador alto |
| Desde Protección, agua <27,5 °C durante 15 min | Reducir a refrigeración: frío, consigna 25 °C, ventilador alto |
| En una sesión bajo control de la automatización, agua ≤26,5 °C durante 15 min | Enviar apagado y volver a Normal |

La temperatura exterior prevista puede anticipar carga térmica, pero no enciende el Rowenta por sí sola: la condición de agua ≥27,0 °C durante 10 min también debe cumplirse. El umbral preventivo interior requiere dos sensores frescos; la rama de respaldo por temperatura del agua no depende de ellos.

## Protección, autoridad y límites

- `off-sns-05` se considera utilizable si Zigbee2MQTT comunicó en los últimos 20 min. Si la telemetría supera esa edad, no está disponible o la sincronización IR se pierde, el controlador inhibe nuevas órdenes y notifica la incidencia; no inventa una temperatura ni apaga a ciegas una sesión en curso.
- Hay un mínimo de 3 min entre un comando de apagado y un nuevo encendido. La marca del último apagado se conserva en `input_datetime.veril_thermal_last_ac_power_off`.
- La automatización está configurada para iniciar habilitada tras reiniciar Home Assistant. La marca de 3 min se persiste, pero su comportamiento después de un reinicio aún no se ha probado en un ciclo físico.
- Las alarmas son 28,5 °C (`warning`), 29 °C (`critical`) y 30 °C (`emergency`).
- El Rowenta recibe órdenes por infrarrojos unidireccionales. Los *shadows* de HA describen órdenes/valores estimados y no verifican el estado físico. La verificación física depende de observación directa.
- El piloto mantiene los valores medidos del despacho y la previsión como contexto de carga. Aún no se ha aislado cuánto del calentamiento del agua corresponde al clima exterior, fuentes internas o su retardo.
- No hay calentador instalado. Esta configuración no controla calefacción ni establece una zona muerta calefacción–refrigeración.

## Estado de validación

El piloto se instaló el 27 de septiembre de 2026 y la comprobación de configuración de Home Assistant no devolvió errores. En el último estado de HA registrado en la operación, a las 17:28 WEST, el agua estaba en 28,8 °C, el controlador en `protection` y la alarma en `warning`; el último valor numérico de agua se había actualizado a las 17:11 WEST. Después, el propietario confirmó que el Rowenta estaba en frío, a 24 °C y con ventilador alto. La integración no proporciona confirmación física de retorno.

La automatización está en servicio como piloto, no validada como control eficaz. La transición automática a 25 °C y el apagado a ≤26,5 °C durante 15 min todavía no se han observado. El descenso aislado de 28,9 a 28,8 °C no demuestra un efecto causal del Rowenta. Las series anteriores y los límites de interpretación están en el [registro de puesta en servicio y mediciones](../04_operaciones/2026/09/2026-09-27-puesta-en-servicio-control-termico.md).

## Seguimiento necesario

Registrar episodios físicos con hora de inicio y fin, modo, consigna y ventilador confirmados por observación; temperatura del agua y edad de su mensaje; los tres sensores ambientales y su humedad; previsión horaria y temperatura exterior observada de Santa Cruz cuando esté disponible; y cambios concurrentes conocidos. Mantener las marcas horarias y no interpolar mediciones asíncronas. Un episodio antes/después es una observación contextual, no una prueba causal por sí solo.

Revisar el piloto tras varios episodios para comprobar la respuesta del aire y del agua, el retardo, el comportamiento de las ramas ambientales y meteorológicas, los falsos arranques, la telemetría y las salidas automáticas. No introducir derivadas como disparadores, ni cambiar umbrales, consignas o política ante pérdida de sensor sin documentar y revisar primero la evidencia.
