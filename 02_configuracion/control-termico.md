# Control térmico de Veril

## Alcance y objetivo

Esta ficha describe el plan térmico vigente y su implementación piloto en Home Assistant. La temperatura que se intenta proteger es la del agua, medida por `off-sns-05`, cuya sonda está sumergida en la cámara del skimmer. El Rowenta climatiza el despacho; sus 24 o 25 °C son consignas del aire acondicionado, no objetivos directos del agua.

El régimen bajo del agua distingue 25–26 °C como zona preferida, 24,5–26,5 °C como objetivo operativo normal, 24–24,5 °C como fresco todavía razonablemente normal, 23–24 °C como excursión fría tolerable que se investiga si persiste, <23 °C como fuera del objetivo y <22 °C como prioridad local de revisión. Los límites de 23 y 22 °C son escalones operativos, no umbrales universales de lesión. En la parte alta, desde 28 °C se entra en protección; 28,5, 29 y 30 °C corresponden a aviso, crítico y emergencia. Son bandas de gestión de Veril. La definición completa está en [Configuración integrada, régimen térmico](README.md#régimen-térmico-adoptado).

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

En esta tabla, **ventilador `high` se refiere al ventilador interno del Rowenta**. El piloto no incluye un ventilador adicional dirigido a la superficie del acuario. Ese sería otro mecanismo —refrigeración evaporativa— y no forma parte de las reglas actuales; aumentaría la pérdida de agua y dependería de reposición con RO/DI. Véanse los límites generales de [temperatura y evaporación](../01_verilpedia/03_parametros/temperatura.md).

## Extremo frío y preparación de calefacción

La parte baja se organiza por función, no como espejo biológico de la banda alta: **24,0–24,5 °C** es fresca pero razonablemente normal; **23,0–24,0 °C** es excursión fría tolerable y debe investigarse si persiste; **22,0–23,0 °C** queda por debajo del objetivo operativo; **<22,0 °C** exige revisión prioritaria. La categoría de 22 °C es un guardarraíl local, no un umbral fisiológico publicado ni una afirmación de daño inmediato.

Si se observa menos de 24,0 °C se valorarán estabilidad, duración y tendencia; en 23,0–24,0 °C se investigará especialmente si la excursión persiste. Por debajo de 23,0 °C se validarán la antigüedad de la telemetría de `off-sns-05` (máximo operativo actual: 20 min) y, si es posible, una medición independiente. Por debajo de 22,0 °C la comprobación será prioritaria. Después se valorarán temperatura ambiente y los mínimos propios de la fauna presente. **No hay alarma ni acción automática de calentamiento instalada.** El plan superior de refrigeración no se altera por esta revisión.

Las fuentes no definen una frontera biológica universal a 23 °C. Tropical Marine Centre da 23–26 °C como guía para corales, pero en otra guía general indica 24–26 °C como óptimo marino y aconseja evitar <24 °C para peces tropicales; se conserva como recomendación comercial general, no como umbral experimental. En *Acropora millepora*, 23 °C durante 10 semanas se asoció a mayor pigmentación y densidad de Symbiodiniaceae bajo un protocolo concreto. En cambio, un estudio de diez especies de peces damisela encontró que entre 29 y 23 °C disminuyó el rendimiento de natación y el margen para actividad, con magnitud dependiente de la especie. Estas pruebas no demuestran daño agudo en Veril, pero apoyan separar excursiones tolerables de un régimen normal para una comunidad mixta ([guía coralina TMC](https://www.tropicalmarinecentre.com/en/downloads/files/care_sheets/Corals/Corals.pdf), [guía general TMC](https://tropicalmarinecentre.com/uk/fan-and-temperature-control), [Nielsen et al. 2020](https://doi.org/10.1007/s00338-019-01881-x), [Johansen et al. 2015](https://doi.org/10.1093/conphys/cov039), [Helgoe et al. 2024](https://doi.org/10.1111/brv.13042)).

Antes de comprar o conectar un calentador:

1. Revisar el límite inferior de temperatura de cada especie finalmente elegida y conservar como requisito del sistema el más restrictivo compatible con la comunidad.
2. Registrar el mínimo estacional del despacho y del agua, distinguiendo lecturas frescas de valores retenidos y contrastando `off-sns-05` con un termómetro independiente.
3. Elegir un calentador marino adecuado al volumen nominal adoptado de **75 L**, al diferencial entre el ambiente frío previsto y el objetivo, y a las condiciones de circulación y montaje. La potencia no se resolverá únicamente a partir de los litros.
4. Mantener el termostato integrado del calentador como regulación local y prever una protección independiente contra sobrecalentamiento. HA podrá supervisar y alarmar, pero no se considerará el único corte de seguridad.
5. Definir y probar la coordinación calefacción–Rowenta con una zona muerta que impida órdenes opuestas, junto con consignas, persistencias de alarma, estado ante sensor obsoleto y recuperación tras un reinicio.
6. Probar la lectura y el ciclo del termostato con un instrumento independiente antes de confiarle el mantenimiento del agua; validar la ubicación del calentador en circulación y su separación de la sonda.

Para una calefacción futura, el principio de diseño es no esperar a <23 °C: el calentador debería ayudar a mantener el mínimo habitual aproximadamente en **24,5–25 °C**. Ese es un objetivo de diseño, no una consigna ni un umbral ON/OFF adoptado. La histéresis, tiempos, alarmas, acción al perder telemetría y coordinación con el Rowenta se definirán con la fauna elegida, el calentador concreto y datos reales de inercia. No se ha cambiado el controlador de HA; Veril no tiene alarma fría ni acción automática de calentamiento activa.

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
