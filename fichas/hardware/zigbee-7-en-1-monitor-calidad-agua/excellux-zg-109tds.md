# Excellux ZG-109TDS

## Identificación

- **Fabricante:** Excellux según la identificación de Zigbee2MQTT; no aparece identificado en el manual adjunto
- **Modelo:** ZG-109TDS
- **Tipo:** Monitor multiparámetro Zigbee para agua dulce y agua salada
- **Protocolo:** Zigbee 3.0
- **Integración prevista:** Zigbee2MQTT mediante Home Assistant

## Ficha normalizada

| Campo | Valor |
| --- | --- |
| `hardware_id` | `ZG_109TDS` |
| `category` | `aquarium_water_monitoring` |
| `vendor` | Excellux |
| `model` | `ZG-109TDS` |
| `hardware_kind` | `physical` |
| `physical_type` | `zigbee_water_quality_monitor` |
| `protocol` | Zigbee 3.0 |
| `integration` | Zigbee2MQTT + Home Assistant |
| `measurements` | TDS, EC, salinidad, SG, temperatura de sonda, temperatura del aire y humedad |

## Función en Veril

Se añade este monitor multiparámetro como equipo de observación complementaria de la calidad del agua. La variante prevista es la **ZG-109TDS**, anunciada como monitor 7 en 1 para **TDS, EC, salinidad, gravedad específica, temperatura de la sonda, temperatura del aire y humedad del aire**.

La ficha no lo convierte en el método de referencia del acuario. Las lecturas se contrastarán con los tests y equipos específicos de Veril antes de utilizarlas para decidir cambios de agua, ajustes de salinidad o correcciones químicas.

## Documentación

La variante seleccionada para Veril es la **ZG-109TDS**, destinada a agua dulce y agua salada.

El manual adjunto se conserva como [`manual-adjunto.pdf`](manual-adjunto.pdf). Sus instrucciones son documentación del fabricante o vendedor; no constituyen por sí mismas una decisión de uso de Veril.

Zigbee2MQTT identifica el modelo como **Excellux ZG-109TDS**. Esta identificación de integración no demuestra por sí sola la marca física de la unidad comprada, por lo que se comprobará contra la etiqueta del equipo recibido.

## Información confirmada por las imágenes del anuncio

Las imágenes aportadas identifican expresamente el modelo **ZG-109TDS** y muestran estas siete funciones:

- TDS
- EC
- Salinidad
- SG o gravedad específica
- Temperatura de la sonda de agua
- Temperatura del aire
- Humedad del aire

También anuncian:

- Registro remoto y seguimiento histórico mediante Zigbee2MQTT
- Avisos de límites desde el panel de Home Assistant
- Informe de datos cada 10 minutos como intervalo predeterminado
- Alimentación mediante dos pilas LR03/AAA de 1,5 V
- Uso en acuarios y otros sistemas pequeños de agua en circuito cerrado
- Exclusión de piscinas, grandes estanques exteriores y sistemas industriales de tratamiento de aguas

Una de las imágenes muestra para la sonda un rango de **−40–120 °C**, mientras que el texto de la variante y el manual adjunto indican **0–60 °C**. Hasta comprobar el equipo y su firmware, se conservará como rango operativo documentado el del manual: **0–60 °C**.

## Datos disponibles en Zigbee2MQTT

Actualmente el dispositivo funciona con **Zigbee2MQTT a través de Home Assistant** y requiere un coordinador o gateway Zigbee compatible con Zigbee2MQTT. No se documenta compatibilidad actual con **Smart Life, Tuya, eWeLink ni ZHA**.

El **ZBBridge-P no se utilizará para este monitor**: el bridge previsto para el termómetro SONOFF no es el coordinador indicado para este dispositivo. La integración dependerá de la compatibilidad real del modelo con la versión instalada de Zigbee2MQTT.

La lista completa de entidades, controles, calibraciones y umbrales está en [Home Assistant y Zigbee2MQTT](home-assistant-zigbee2mqtt.md).

En Zigbee2MQTT se publican, según la versión instalada, avisos de sonda, temperatura, humedad, TDS y EC; modo `freshwater`/`seawater`; batería; temperatura de sonda; temperatura del aire; humedad; TDS; salinidad; EC; gravedad específica; intervalo de muestreo; calibraciones y umbrales configurables.

## Especificaciones

| Campo | Dato publicado |
| --- | --- |
| Protocolo inalámbrico | Zigbee |
| Alimentación | 3 V CC |
| Corriente en espera | ≤20 µA |
| Rango de la sonda | 0–60 °C |
| Temperatura de funcionamiento | 10–60 °C |
| Humedad de funcionamiento | 0–99 % HR |
| Modelo | ZG-109TDS |
| EC | 0–20.000 µS/cm, ±2 % FS |
| TDS | 0–13.000 ppm, ±2 % FS |
| Gravedad específica | 1,000–1,050, ±0,001 |

La documentación no atribuye a la ZG-109TDS medición de pH, ORP ni cloro libre. La descripción anterior que asociaba esas funciones a este equipo queda corregida.

## Encaje con agua marina

La ZG-109TDS cubre numéricamente el entorno de 35 ppt previsto para Veril mediante su modo de agua salada y su rango de gravedad específica hasta 1,050. La información facilitada para el producto publica la salinidad como **0,0–50,0 %**, mientras que el manual gráfico adjunto parece representar una escala de **0–50,0 ‰**. Esta discrepancia de unidades queda pendiente de confirmación en el equipo recibido; no se convertirá una lectura en ppt sin verificar qué escala utiliza el firmware.

El rango de EC publicado para ZG-109TDS llega a 20.000 µS/cm, mientras que el agua marina natural suele superar ese valor. Por tanto, no se asumirá que la lectura de EC sea válida para agua marina solo porque el dispositivo muestre esa magnitud.

El TDS tampoco se tratará como una medida directa de la salinidad marina: depende de la conversión utilizada por el instrumento y no sustituye la medición de salinidad con refractómetro o instrumento calibrado para agua marina.

## Instalación

- Confirmar al recibirlo el modelo ZG-109TDS, las sondas incluidas, la escala de salinidad y el gateway compatible con Zigbee2MQTT
- Revisar si el cuerpo flota de forma estable y si las sondas quedan completamente sumergidas según las instrucciones de la variante recibida
- No dejarlo atrapado contra la pared, el rebosadero, una bomba o la pantalla
- Calibrar cada función con las soluciones apropiadas antes de comparar sus lecturas
- Comparar temperatura y salinidad con los métodos de referencia del acuario
- Registrar divergencias por parámetro y no corregir el agua a partir de una lectura aislada
- Retirar el equipo si aparecen corrosión, depósitos, daño en las sondas o pérdida de estanqueidad

## Limitaciones

- El equipo requiere Zigbee2MQTT mediante Home Assistant y no se documenta compatibilidad actual con ZHA, Tuya, Smart Life ni eWeLink
- La etiqueta «7 en 1» y la ficha comercial no demuestran exactitud en agua marina
- La unidad de salinidad publicada por el anuncio y la representada en el manual deben verificarse
- IP67 y diseño flotante no garantizan resistencia indefinida al agua salada ni a la bioincrustación
- El monitor será una fuente de tendencia y alerta hasta completar su comparación con métodos independientes
- No se usará como sustituto de los tests de amonio, nitrito, nitrato, fosfato o alcalinidad

## Fuentes

- [Producto enlazado en AliExpress](https://es.aliexpress.com/item/1005012700289775.html)
- [Manual adjunto](manual-adjunto.pdf)
- [Manual coincidente localizado para un monitor Zigbee 7 en 1](https://manuals.plus/m/509786b9b0c91df9379ec221ce02d0dcfbc89419f0532a745f38284d6eee7726)
