# Integración de la AI Prime™ 16HD Reef con Home Assistant

## Alcance

La AI Prime 16HD Reef se alimentará mediante una unidad independiente del [SONOFF S60ZBTPF](../sonoff-s60zbtpf/sonoff-s60zbtpf.md), integrada en Home Assistant a través de Zigbee2MQTT.

El enchufe será una capa externa de alimentación, supervisión y corte. Mobius seguirá controlando la intensidad, el espectro y la programación de la luminaria; el enchufe no sustituirá esas funciones.

## Recorrido eléctrico

```text
Red eléctrica
    ↓
SONOFF S60ZBTPF
    ↓
Adaptador de la AI Prime 16HD Reef
    ↓
Luminaria y control Mobius
```

## Entidad y pruebas

Se conservará un nombre estable, por ejemplo:

```text
switch.veril_ai_prime_16hd_reef_alimentacion
```

Se comprobarán el estado de la salida, potencia, corriente, tensión, energía acumulada si se publica correctamente, disponibilidad Zigbee y comportamiento tras recuperar la alimentación. Antes de fijar umbrales se registrará el consumo durante apagado, arranque y funcionamiento estable.

Después de un corte se comprobará que el enchufe publica su estado real, el adaptador arranca sin anomalías, Mobius conserva o recupera la programación prevista y Home Assistant registra el corte y la recuperación. Una potencia normal no demuestra que el espectro ni el PAR sean los previstos.

## Fuentes

- [Ficha de la AI Prime 16HD Reef](ai-prime-16hd-reef.md)
- [Ficha del SONOFF S60ZBTPF](../sonoff-s60zbtpf/sonoff-s60zbtpf.md)
- [SONOFF S60ZBTPF en Zigbee2MQTT](https://www.zigbee2mqtt.io/devices/S60ZBTPF.html)
- [Integración de Zigbee2MQTT con Home Assistant](https://www.zigbee2mqtt.io/guide/usage/integrations/home_assistant.html)
