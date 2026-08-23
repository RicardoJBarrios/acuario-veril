# D-D H2Ocean Compact ATO

- **Fabricante:** D-D The Aquarium Solution
- **Modelo:** H2Ocean Compact ATO
- **Tipo:** sistema automático de reposición de agua
- **Entorno:** acuarios de agua dulce o marina

## Ficha normalizada

| Campo | Valor |
| --- | --- |
| `hardware_id` | `DD_H2Ocean_Compact_ATO` |
| `category` | `aquarium` |
| `vendor` | `D-D The Aquarium Solution` |
| `model` | `H2Ocean Compact ATO` |
| `hardware_kind` | `physical` |
| `physical_type` | `automatic_top_off` |
| `sensor` | doble sensor óptico |
| `actuator` | bomba CC incluida |
| `connectivity` | ninguna |
| `software` | control embebido no actualizable por el usuario |
| `mounting` | soporte magnético |

## Componentes incluidos

Según el manual oficial, la caja contiene:

- Controlador Compact ATO con doble sensor óptico
- Adaptador de alimentación universal
- Soporte universal para el tubo, compatible con acuarios con o sin marco de hasta 12,7 mm
- Bomba de reposición CC sin escobillas
- Rompe-sifón, integrado en el tubo de reposición
- Tubo de 200 cm

El depósito de reposición no forma parte del ATO y se documenta por separado en [Barril agroalimentario GRAF de 15 l](graf-barril-agroalimentario-15l.md).

## Funcionamiento

El controlador detecta el descenso del nivel mediante dos sensores ópticos y activa la bomba del depósito de reposición. El diseño no contiene flotadores móviles en el sensor y añade una lógica de seguridad y una alarma visual.

En un acuario marino debe reponer agua dulce, preferiblemente RO/DI: la sal no se evapora.

## Especificaciones

| Parámetro | Valor declarado |
| --- | --- |
| Entrada de la fuente | 100–240 V CA, 50/60 Hz |
| Bomba | corriente continua |
| Caudal máximo | 280 L/h |
| Altura máxima de impulsión | 2,5 m |
| Grosor máximo de cristal | 12,5 mm |
| Tubo incluido | 2 m |
| Diámetro del tubo | 9 mm exterior; 6,5 mm interior |
| Tamaño de acuario recomendado | más de 50 L |
| Sensores | dos ópticos |
| Garantía limitada del manual | 1 año, con instalación y uso correctos |

El caudal máximo y la altura máxima de impulsión no se alcanzan simultáneamente. La altura, la longitud y el recorrido del tubo reducen el caudal real.

La bomba es una bomba de corriente continua sin escobillas, con una altura máxima declarada de 250 cm y un caudal máximo de 280 l/h. Esos valores son límites de la bomba y no un caudal garantizado en la instalación de Veril.

## Instalación confirmada para Veril

Veril utilizará el H2Ocean Compact ATO con un [Barril agroalimentario GRAF de 15 l](graf-barril-agroalimentario-15l.md) reservado para agua RO/DI.

### Altura de impulsión prevista

El depósito estará en el suelo y la urna se apoyará sobre una mesa con:

- Patas de 71 cm
- Tapa de 32 mm
- Urna de 40 cm de altura

La superficie de apoyo de la urna quedará aproximadamente a **74,2 cm sobre el suelo** y el borde superior de la urna aproximadamente a **114,2 cm**. La salida del tubo del ATO no tiene que situarse en el borde superior: debe quedar por encima del nivel máximo del agua del sump y sin sumergirse durante el funcionamiento normal.

Tomando como referencia conservadora una bomba situada cerca del fondo del barril y una salida próxima a la parte alta del compartimento técnico, la elevación vertical prevista será aproximadamente de **1,0–1,2 m**. La altura real dependerá de la posición final de la bomba, del nivel de salida y del recorrido del tubo.

La bomba declara una altura máxima de impulsión de **2,5 m**. Por tanto, la instalación prevista queda con un margen vertical aproximado de **1,3–1,5 m** frente a ese límite. No se aprecia un problema de altura para llevar el agua desde el barril colocado en el suelo hasta la cámara de retorno.

El tubo incluido mide 2 m. La ruta definitiva debe mantenerse dentro de esa longitud, evitando bucles innecesarios, estrangulamientos y curvas cerradas. La altura máxima declarada y el caudal máximo de 280 l/h no se alcanzan simultáneamente, por lo que el caudal real debe comprobarse una vez instalado.

**Conclusión de compatibilidad:** la subida desde el barril situado en el suelo hasta la cámara de retorno es compatible con la capacidad declarada del H2Ocean Compact ATO. La elevación estimada de 1,0–1,2 m queda claramente por debajo de los 2,5 m máximos de la bomba y el recorrido previsto cabe, en principio, dentro de los 2 m de tubo incluido.

- El sensor óptico se instalará en la cámara de retorno, donde la evaporación modifica realmente el nivel
- La bomba se colocará dentro de un depósito alimentario cerrado y reservado para RO/DI
- La salida del tubo quedará por encima del nivel máximo del depósito y del agua cuando sea necesario para impedir el sifonado
- El rompe-sifón se colocará por encima del nivel máximo del agua del depósito
- El extremo de salida del tubo no quedará sumergido en el agua de la cámara de retorno durante el funcionamiento normal
- El cableado y la tubería quedarán sujetos, sin pinzamientos y con bucle antigoteo
- El depósito no contendrá agua salada, suplementos ni productos de mantenimiento

El sensor se instalará a la altura normal de trabajo, haciendo que el nivel alcance el sensor óptico inferior. Debe quedar alejado de microburbujas, turbulencias directas, salpicaduras y zonas donde pueda acumularse sal o biofilm.

## Pruebas obligatorias

1. Activación al bajar el nivel
2. Parada en el nivel establecido
3. Respuesta del segundo sensor o de la protección disponible
4. Ausencia de sifón con la bomba apagada
5. Comportamiento al vaciarse el depósito
6. Comportamiento tras un corte eléctrico

## Criterios de aceptación

- Nivel estable sin ciclos excesivamente cortos
- El caudal no remueve sedimento ni salpica los sensores
- Autonomía suficiente sin ocultar una fuga
- Sensor accesible para limpieza e inspección
- La bomba no puede vaciar el depósito hacia la urna por sifón
- La cámara de retorno conserva un nivel seguro cuando el depósito se agota

La doble óptica reduce el riesgo, pero no constituye por sí sola una protección independiente contra inundaciones o reposición excesiva. El primer rellenado debe vigilarse porque el límite temporal de seguridad se establece a partir de esa referencia inicial.

### Smart Level

El controlador registra la duración del primer rellenado y activa una alarma visual si un rellenado posterior dura seis veces más. Por ejemplo, si el primer ciclo dura 10 segundos, la alarma puede activarse al superar 60 segundos.

Esta función puede detectar, entre otras situaciones:

- Interferencia de microburbujas
- Sobrellenado o lectura anómala del sensor
- Fallo del sensor o del controlador
- Depósito vacío, para evitar que la bomba funcione en seco

El primer rellenado no dispone de ese límite temporal aprendido. Tras resolver una alerta, el manual indica apagar y volver a encender el equipo para reiniciarlo.

En acuarios muy pequeños, el sensor superior puede activarse brevemente después de cada reposición; el manual lo considera un comportamiento normal si no aparece una alerta roja.

## Interfaz e indicadores

| Indicador | Significado |
| --- | --- |
| LED azul y rojo alternos | Inicialización |
| LED azul fijo | Alimentación conectada y equipo preparado |
| LED azul intermitente | Reposición o bombeo |
| LED azul que parpadea rápidamente durante poco tiempo | El sensor de seguridad detecta un cambio de nivel |
| LED rojo intermitente | Alerta Smart Level; revisar microburbujas, sobrellenado o depósito vacío |

## Mantenimiento

- Limpiar periódicamente sensores, bomba y tubo
- Retirar sal, carbonatos, algas y biofilm
- Verificar que la bomba no funcione en seco
- Repetir las pruebas de seguridad después de limpiar o cambiar la disposición
- Inspeccionar cableado y conectores antes de volver a energizar

## Integración con supervisión

El ATO funcionará de forma autónoma con sus protecciones nativas. La supervisión externa podrá observar consumo, disponibilidad y anomalías si la integración lo permite, pero no sustituirá las protecciones del equipo ni la comprobación visual.

No se aplicarán ventanas horarias ni cortes automáticos hasta comprobar con el equipo real que conserva sus protecciones, reinicia de forma fiable y no produce oscilaciones de nivel o salinidad.

La integración prevista mediante un [SONOFF S60ZBTPF y Zigbee2MQTT](home-assistant-zigbee2mqtt.md) puede añadir límites de tiempo, ventanas de habilitación, registro y corte de emergencia. No mide el nivel de agua y no sustituye Smart Level.

El fabricante ofrece como accesorio opcional un Smart AC Switch. No forma parte del equipo documentado para Veril y no se considerará necesario para la instalación base.

## Fuente interna

- [Manual oficial H2Ocean Compact ATO](./h2ocean-compact-ato-manual.pdf)

## Fuente externa

- [D-D: H2Ocean Compact ATO](https://www.theaquariumsolution.com/product/8111/451)

## Estado en Veril

**Confirmado:** equipo seleccionado para la reposición automática de Veril.

**Pendiente de ejecución:** ubicación definitiva del depósito, recorrido y fijación del tubo, marcas de nivel mínimo y máximo, autonomía real y validación completa después de un corte eléctrico.
