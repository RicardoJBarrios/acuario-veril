# Integración de la Mantis Tourbon 60 con Home Assistant

## Alcance

La Mantis Tourbon 60 se alimentará mediante una unidad independiente del [SONOFF S60ZBTPF](../sonoff-s60zbtpf/sonoff-s60zbtpf.md), integrada en Home Assistant a través de Zigbee2MQTT.

El enchufe permitirá cortar la alimentación, registrar el consumo y generar avisos si el patrón eléctrico deja de ser compatible con el funcionamiento esperado. No sustituirá al controlador de la bomba ni confirmará el caudal, la orientación, la limpieza o el movimiento real del agua.

## Recorrido eléctrico

```text
Red eléctrica
    ↓
SONOFF S60ZBTPF
    ↓
Adaptador de la Mantis Tourbon 60
    ↓
Controlador de la bomba
    ↓
Bomba de movimiento
```

El enchufe se colocará antes del adaptador. No se conectará la bomba directamente a la red eléctrica ni se utilizará el S60ZBTPF para crear ondas, regular intensidad o aplicar la pausa de alimentación del controlador.

## Entidades y calibración

Se conservará un nombre estable, por ejemplo:

```text
switch.veril_mantis_tourbon_60_alimentacion
```

Como mínimo se habilitarán:

- Estado de la salida del enchufe
- Potencia instantánea
- Corriente y tensión
- Energía acumulada, si la entidad se publica correctamente
- Disponibilidad del dispositivo Zigbee
- Comportamiento tras recuperar la alimentación

Antes de crear umbrales se registrará el consumo del conjunto con la bomba en flujo constante, en cada intensidad prevista y después de una limpieza. Los modos de onda, pulsante, aleatorio y ciclo pueden cambiar el consumo; por ello no se utilizará un único umbral universal.

## Funcionamiento normal

El enchufe permanecerá encendido cuando la Tourbon 60 deba mantener la circulación interna. El controlador local gobernará el modo y la intensidad. Home Assistant podrá apagarla durante una intervención, una alimentación o una condición de seguridad documentada.

Cada cambio de modo, intensidad u orientación se anotará junto con el consumo observado. La potencia se interpretará junto con el estado del enchufe, la disponibilidad Zigbee y la observación del flujo.

## Alarmas

Home Assistant generará una alarma si se produce cualquiera de estas condiciones:

- El enchufe queda apagado fuera de una ventana de mantenimiento autorizada
- El enchufe está encendido, pero el consumo permanece en cero o por debajo del mínimo calibrado después del tiempo de arranque
- El consumo queda claramente por debajo o por encima del patrón calibrado durante un periodo sostenido
- El enchufe aparece no disponible mientras la bomba debe funcionar
- La bomba no recupera el estado esperado después de un corte eléctrico
- El consumo cambia de forma persistente después de una limpieza o sin una modificación registrada del ajuste

La alarma de consumo anómalo no diagnosticará por sí sola rotor bloqueado, suciedad, falta de agua, fallo del controlador o caudal insuficiente. Requerirá inspección visual y revisión del conjunto.

## Corte y recuperación

El corte automático solo se utilizará ante una condición de seguridad definida, como riesgo eléctrico, fuga o sobrecalentamiento observado. Una alarma de potencia baja no apagará automáticamente la bomba sin una política probada, porque el corte elimina temporalmente la circulación del display.

El `power_on_behavior` del S60ZBTPF se configurará y probará con el controlador conectado. Tras una interrupción se comprobará que:

- El enchufe publica su estado real
- El controlador vuelve al modo previsto
- La bomba arranca sin ruido, vibración o reinicios anómalos
- La circulación vuelve a ser visible
- Home Assistant registra el corte y la recuperación

El rearme no se repetirá automáticamente si la causa del fallo no está clara.

## Registro útil

Se conservarán:

- Encendidos, apagados y duración de cada estado
- Potencia, corriente y tensión
- Energía diaria y acumulada
- Disponibilidad Zigbee y reinicios
- Modo e intensidad del controlador cuando se cambien
- Limpiezas, ajustes de posición y observaciones del flujo
- Alarmas y rearme manual

## Pruebas de aceptación

1. Encendido y apagado manual desde Home Assistant
2. Confirmación de que el estado publicado coincide con el estado eléctrico
3. Publicación de potencia, corriente y tensión
4. Registro de consumos por modo e intensidad
5. Simulación de enchufe encendido con adaptador desconectado y comprobación de la alarma
6. Detección de pérdida de disponibilidad Zigbee
7. Recuperación después de un corte eléctrico
8. Comprobación del comportamiento del controlador después de recuperar la alimentación
9. Confirmación de que una alarma no provoca ciclos repetidos de encendido y apagado
10. Desconexión segura durante la limpieza

## Límites

El sistema no sustituye:

- La inspección del movimiento superficial y del corredor trasero
- La comprobación de sustrato desplazado o zonas de detrito
- La limpieza del rotor y de las jaulas de flujo
- La revisión del controlador, el adaptador y los conectores
- La protección eléctrica y frente a salpicaduras

## Fuentes

- [Ficha de la Mantis Tourbon 60](mantis-tourbon-60.md)
- [Ficha del SONOFF S60ZBTPF](../sonoff-s60zbtpf/sonoff-s60zbtpf.md)
- [SONOFF S60ZBTPF en Zigbee2MQTT](https://www.zigbee2mqtt.io/devices/S60ZBTPF.html)
- [Integración de Zigbee2MQTT con Home Assistant](https://www.zigbee2mqtt.io/guide/usage/integrations/home_assistant.html)

