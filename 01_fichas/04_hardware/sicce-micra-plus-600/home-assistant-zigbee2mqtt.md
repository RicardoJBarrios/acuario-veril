# Integración de la Sicce Micra Plus 600 con Home Assistant

## Alcance

La Sicce Micra Plus 600 se alimentará mediante una unidad independiente del [SONOFF S60ZBTPF](../sonoff-s60zbtpf/sonoff-s60zbtpf.md), integrada en Home Assistant a través de Zigbee2MQTT.

El enchufe permitirá supervisar la alimentación del retorno y aplicar un corte seguro durante el mantenimiento. No medirá el nivel de la cámara, el caudal, la presión, la presencia de aire ni el estado del rebosadero.

## Recorrido eléctrico

```text
Red eléctrica
    ↓
SONOFF S60ZBTPF
    ↓
Alimentación de la Sicce Micra Plus 600
    ↓
Bomba sumergible en la cámara de retorno
    ↓
Retorno al display
```

El enchufe no controlará la regulación mecánica de la bomba. La Micra Plus 600 permanecerá sumergida y su ajuste hidráulico se realizará en la propia bomba y en la instalación de tubería.

## Entidades y calibración

Se conservará un nombre estable, por ejemplo:

```text
switch.veril_micra_plus_600_alimentacion
```

Como mínimo se habilitarán:

- Estado de la salida del enchufe
- Potencia instantánea
- Corriente y tensión
- Energía acumulada, si la entidad se publica correctamente
- Disponibilidad Zigbee
- Comportamiento tras recuperar la alimentación

Se medirá el consumo con la bomba en espera operativa y con la tubería, altura y regulación definitivas. Los umbrales se establecerán después de comprobar varios rearranques y no se copiarán directamente de los 6,5 W declarados.

## Funcionamiento normal y alarmas

La Micra permanecerá encendida cuando el retorno deba funcionar. Home Assistant generará una alarma si:

- El enchufe queda apagado fuera de una ventana de mantenimiento autorizada
- El enchufe está encendido, pero el consumo permanece en cero o por debajo del mínimo calibrado después del arranque
- El consumo queda fuera del intervalo calibrado durante un periodo sostenido
- El dispositivo Zigbee aparece no disponible
- La bomba no recupera el estado esperado después de un corte
- El retorno no recupera el nivel y el funcionamiento observados durante la prueba de aceptación

La última condición requiere observación del sistema o un sensor adicional. El S60ZBTPF no puede detectar por sí solo una cámara vacía, un tubo obstruido, aire en la bomba, un sifón o un caudal insuficiente.

Un consumo normal tampoco demuestra que la bomba esté moviendo el caudal correcto. La alarma eléctrica se tratará como indicio y activará una inspección del nivel, la tubería, el rotor y el rebosadero.

## Corte, mantenimiento y recuperación

El corte automático podrá utilizarse ante una fuga, un riesgo eléctrico o una condición hidráulica peligrosa confirmada por otro medio. No se apagará y encenderá la bomba repetidamente para regular el nivel.

Durante el mantenimiento se apagará el enchufe desde Home Assistant y se confirmará la ausencia de tensión antes de retirar la bomba. El `power_on_behavior` se configurará y probará con la Micra conectada.

Después de un corte se comprobará:

- Que el enchufe publica su estado real
- Que la bomba rearranca sin funcionar en seco
- Que la cámara de retorno mantiene un nivel seguro
- Que el rebosadero admite el caudal
- Que no aparecen microburbujas persistentes, ruido o fugas

El rearme será manual cuando haya una alarma hidráulica o eléctrica.

## Registro útil

Se conservarán:

- Encendidos, apagados y duración de cada estado
- Potencia, corriente, tensión y energía
- Disponibilidad Zigbee y cortes eléctricos
- Regulación de la bomba y altura de impulsión
- Nivel mínimo, operativo y máximo de la cámara
- Alarmas, inspecciones y rearme manual

## Pruebas de aceptación

1. Encendido y apagado manual desde Home Assistant
2. Confirmación del estado real del enchufe
3. Publicación de potencia, corriente y tensión
4. Calibración del consumo con la instalación definitiva
5. Simulación de ausencia de consumo y comprobación de la alarma
6. Detección de pérdida de disponibilidad Zigbee
7. Corte durante mantenimiento y comprobación de ausencia de tensión
8. Recuperación después de un corte eléctrico
9. Rearranque sin funcionamiento en seco
10. Confirmación del nivel de la cámara y del comportamiento del rebosadero
11. Comprobación de que no se crea un ciclo automático de encendido y apagado

## Límites

Home Assistant no sustituye:

- La comprobación del nivel de la cámara de retorno
- La medición del caudal real
- La limpieza del rotor y de la entrada
- La revisión del tubo, las conexiones y el rebosadero
- La protección frente a funcionamiento en seco
- La protección eléctrica y frente a salpicaduras

## Fuentes

- [Ficha de la Sicce Micra Plus 600](sicce-micra-plus-600.md)
- [Ficha del SONOFF S60ZBTPF](../sonoff-s60zbtpf/sonoff-s60zbtpf.md)
- [SONOFF S60ZBTPF en Zigbee2MQTT](https://www.zigbee2mqtt.io/devices/S60ZBTPF.html)
- [Integración de Zigbee2MQTT con Home Assistant](https://www.zigbee2mqtt.io/guide/usage/integrations/home_assistant.html)

