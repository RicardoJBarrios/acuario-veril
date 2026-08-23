# Integración del H2Ocean Compact ATO con Home Assistant

## Alcance

El D-D H2Ocean Compact ATO se conectará a la red eléctrica a través de un [SONOFF S60ZBTPF](../sonoff-s60zbtpf/sonoff-s60zbtpf.md). El enchufe se integrará en Home Assistant mediante **Zigbee2MQTT**.

El Sonoff será una capa externa de supervisión y corte de alimentación. No sustituirá:

- La doble detección óptica del H2Ocean Compact ATO
- La función Smart Level del controlador
- La protección antisifón del tubo
- Las comprobaciones físicas del depósito, la bomba y el sensor

El Sonoff no mide el nivel de agua y no puede determinar por sí solo si el ATO ha repuesto correctamente.

## Componentes y recorrido

```text
Red eléctrica
    ↓
SONOFF S60ZBTPF
    ↓
Adaptador de alimentación del H2Ocean Compact ATO
    ↓
Controlador H2Ocean
    ↓
Bomba de reposición en el barril GRAF de 15 l
```

El enchufe no se intercalará en el tubo de agua ni controlará directamente la bomba de corriente continua. Cortará la alimentación del adaptador del ATO.

## Capacidades relevantes del Sonoff

Las características generales del enchufe están documentadas en la [ficha del SONOFF S60ZBTPF](../sonoff-s60zbtpf/sonoff-s60zbtpf.md). Para el ATO se utilizarán principalmente:

- Conmutación remota de la salida
- Medición de tensión, corriente, potencia y energía
- Protección configurable frente a sobrecarga
- Comportamiento configurable al recuperar la alimentación
- Función de apagado temporizado, si el firmware y la integración la exponen
- Función de router Zigbee para ampliar la red mallada

El consumo del adaptador del ATO queda muy por debajo de la capacidad eléctrica declarada del enchufe, pero la protección eléctrica del Sonoff no es una protección hidráulica.

## Integración con Zigbee2MQTT

El dispositivo se incorporará a Zigbee2MQTT y se habilitará el descubrimiento MQTT de Home Assistant. Se conservará un nombre estable, por ejemplo:

```text
switch.veril_ato_alimentacion
```

Como mínimo deben quedar disponibles en Home Assistant:

- Estado de la salida del enchufe
- Potencia instantánea
- Corriente
- Tensión
- Energía acumulada, si la entidad se publica correctamente
- Estado de disponibilidad del dispositivo Zigbee
- Comportamiento configurado tras recuperar la alimentación

La potencia y la corriente permitirán distinguir entre estos estados operativos aproximados:

- **Enchufe apagado:** salida `OFF` y consumo nulo o residual del adaptador
- **ATO alimentado en espera:** salida `ON` y consumo bajo del controlador
- **ATO realizando una reposición:** aumento de potencia y corriente mientras funciona la bomba

Los umbrales exactos se establecerán después de medir el adaptador en reposo y durante varios ciclos reales. No se utilizará un valor universal sin calibración.

La integración se validará con el dispositivo real. No se considerará suficiente que el enchufe aparezca emparejado: debe responder a órdenes, publicar su estado y volver a estar disponible después de reiniciar Zigbee2MQTT y Home Assistant.

## Estado eléctrico por defecto

El `power_on_behavior` se configurará en **off** o en el modo más seguro que permita la instalación y que haya sido probado. Después de un corte eléctrico, el ATO no debe arrancar de forma inesperada sin que Home Assistant haya recuperado el estado del sistema.

Esta decisión no elimina la necesidad de probar el comportamiento real del Sonoff después de un corte. El coordinador Zigbee, Zigbee2MQTT, Home Assistant y el propio enchufe pueden recuperar el servicio en momentos diferentes.

## Política de funcionamiento

### Estado normal

El ATO permanecerá alimentado durante las ventanas permitidas para que su propio sensor mantenga el nivel. La automatización no encenderá y apagará el enchufe con la frecuencia de cada reposición: el controlador H2Ocean debe gobernar la bomba y el Sonoff debe actuar como barrera.

### Límite de tiempo

La integración podrá aplicar dos límites distintos:

1. **Tiempo máximo de alimentación del enchufe:** impide que el adaptador permanezca conectado indefinidamente si el ATO queda habilitado fuera de la ventana permitida
2. **Tiempo máximo de consumo de la bomba:** detecta que la potencia o la corriente permanecen por encima del umbral de reposición durante demasiado tiempo

Si se supera cualquiera de los límites, Home Assistant:

1. Apagará el Sonoff
2. Marcará el ATO como bloqueado
3. Emitirá una alerta visible y, si está configurado, una notificación
4. Registrará la hora, la duración y la potencia observada
5. Exigirá una revisión manual antes de volver a habilitarlo

El límite no se fijará por la capacidad eléctrica del Sonoff. Se determinará después de medir varios ciclos normales de reposición con el equipo instalado, manteniendo un margen suficiente para la variación normal y siendo siempre inferior al tiempo que podría introducir un volumen de agua peligroso.

Mientras ese tiempo no esté medido, el sistema no se considerará validado para funcionamiento desatendido.

### Apagado temporizado

El apagado temporizado podrá implementarse en Home Assistant o mediante la función `inching` del S60ZBTPF si la versión de firmware y Zigbee2MQTT la exponen correctamente. La función no se considerará validada hasta comprobar que:

- El temporizador se inicia cuando corresponde
- El enchufe se apaga realmente al terminar
- No se produce un ciclo automático de encendido y apagado
- El estado publicado coincide con el estado eléctrico real

Como criterio de seguridad, el control principal permanecerá en Home Assistant, con una automatización de apagado y una alarma si la salida o el consumo siguen activos después del plazo.

### Ventanas de habilitación

Home Assistant podrá habilitar el enchufe solo durante las ventanas horarias definidas para Veril. Fuera de ellas, el enchufe permanecerá apagado.

Las ventanas no deben crear una oscilación de salinidad innecesaria. Si el nivel y la salinidad se desvían mientras el ATO está bloqueado, se ampliarán las ventanas o se permitirá el funcionamiento continuo con límite de tiempo. La programación horaria es una capa de seguridad y mantenimiento, no un objetivo biológico.

La configuración inicial deberá incluir una ventana suficientemente amplia para cubrir la evaporación esperada y evitar que el sistema acumule horas de funcionamiento sin reposición.

## Condiciones que deben bloquear el ATO

Home Assistant apagará y bloqueará el Sonoff cuando se produzca cualquiera de estas condiciones:

- Se supera el tiempo máximo de una activación
- La bomba mantiene un consumo superior al umbral durante más tiempo del permitido
- La potencia permanece en el patrón de reposición cuando el enchufe debería estar en espera
- El enchufe no confirma el estado solicitado
- Zigbee2MQTT pierde el dispositivo durante una activación
- El enchufe aparece no disponible
- Se detecta una potencia anómala respecto al consumo de la bomba
- Se produce una alerta de Smart Level del H2Ocean
- El depósito está vacío o no puede comprobarse su nivel
- Se activa un modo de mantenimiento
- Se detecta una fuga, desbordamiento o comportamiento hidráulico anómalo

La detección de potencia no sustituye a la detección de nivel. Una bomba puede consumir energía y no mover agua por falta de agua, obstrucción, tubo suelto o aire en el circuito.

Del mismo modo, un consumo bajo o nulo no demuestra por sí solo que el ATO esté correctamente apagado: el umbral debe interpretarse junto con el estado `ON/OFF`, la disponibilidad Zigbee y el comportamiento observado del controlador.

## Rearme

Un corte automático no se rearmará de forma indefinida ni mediante un ciclo automático. El procedimiento será:

1. Revisar el nivel del display y de la cámara de retorno
2. Revisar el depósito GRAF, la bomba, el tubo y el rompe-sifón
3. Revisar el sensor óptico y la presencia de microburbujas
4. Consultar el estado y los registros de Zigbee2MQTT y Home Assistant
5. Confirmar que no existe fuga ni sobrellenado
6. Restablecer el enchufe manualmente
7. Observar el primer ciclo completo

Si la causa no está clara, el ATO permanecerá apagado y la reposición se hará manualmente con RO/DI hasta resolverla.

## Alarmas y registro

Se registrarán como mínimo:

- Inicio y fin de cada activación del Sonoff
- Duración de cada ciclo
- Potencia y corriente observadas
- Estado de disponibilidad Zigbee
- Alertas del H2Ocean Compact ATO
- Activaciones del límite de tiempo
- Cortes eléctricos y reinicios
- Bloqueos y rearme manual
- Consumo diario y acumulado del ATO

Las alarmas críticas serán:

- ATO encendido más allá del límite
- ATO no disponible durante una ventana de funcionamiento
- Sonoff apagado cuando el nivel del retorno requiere reposición
- Potencia anómala o bomba aparentemente activa sin ciclo normal
- Reposición repetitiva o excesivamente frecuente
- Pérdida de comunicación tras un reinicio

## Pruebas de aceptación

La integración se aceptará cuando se hayan probado, con el ATO instalado:

1. Encendido y apagado manual desde Home Assistant
2. Publicación correcta del estado en Zigbee2MQTT y Home Assistant
3. Medición de potencia, corriente y tensión
4. Calibración del consumo en espera y durante una reposición
5. Detección de una reposición activa mediante potencia y corriente
6. Activación y cumplimiento del límite de tiempo del enchufe
7. Activación y cumplimiento del límite de tiempo de consumo de la bomba
8. Apagado temporizado y confirmación del estado real
9. Apagado fuera de una ventana permitida
10. Bloqueo y aviso después de superar un límite
11. Rearme manual sin bucle de encendido y apagado
12. Comportamiento del `power_on_behavior` tras un corte eléctrico
13. Pérdida y recuperación de Zigbee2MQTT
14. Pérdida y recuperación de Home Assistant
15. ATO apagado con reposición manual segura
16. Ausencia de sifón y de desbordamiento durante todos los escenarios

## Límites de la automatización

Home Assistant no debe utilizarse para ocultar una instalación hidráulica insegura. La automatización no corrige:

- Un depósito mal cerrado o contaminado
- Un tubo sumergido que permita sifonado
- Un sensor instalado entre microburbujas
- Una bomba funcionando en seco
- Una cámara de retorno sin volumen de seguridad
- Un rebosadero obstruido
- Una fuga o una mala nivelación

## Fuentes

- [Ficha oficial SONOFF S60ZBTPF/S60ZBTPG](https://sonoff.tech/products/sonoff-iplug-zigbee-smart-plug-s60-series)
- [Dispositivo S60ZBTPF en Zigbee2MQTT](https://www.zigbee2mqtt.io/devices/S60ZBTPF.html)
- [Guía de integración de Zigbee2MQTT con Home Assistant](https://www.zigbee2mqtt.io/guide/usage/integrations/home_assistant.html)
- [Ficha del H2Ocean Compact ATO](dd-h2ocean-compact-ato.md)
