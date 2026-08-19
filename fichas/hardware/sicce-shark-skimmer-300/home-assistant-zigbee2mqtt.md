# Integración del Sicce Shark SKIMMER 300 con Home Assistant

## Alcance

El Sicce Shark SKIMMER 300 se alimentará mediante una unidad independiente del [SONOFF S60ZBTPF](../sonoff-s60zbtpf/sonoff-s60zbtpf.md), integrada en Home Assistant a través de Zigbee2MQTT.

El Sonoff permitirá cortar la alimentación, registrar el consumo y aplicar políticas de funcionamiento. No medirá el nivel de agua, la producción de espuma, el caudal, el aire ni el llenado de la copa.

## Recorrido eléctrico

```text
Red eléctrica
    ↓
SONOFF S60ZBTPF
    ↓
Alimentación del Sicce Shark SKIMMER 300
    ↓
Bomba y control electromecánico del skimmer
```

El enchufe no sustituirá el ajuste de entrada de agua, aire, altura ni copa del skimmer.

## Entidades y nombre

Se conservará un nombre estable, por ejemplo:

```text
switch.veril_skimmer_alimentacion
```

Home Assistant deberá recibir, como mínimo:

- Estado del enchufe
- Potencia instantánea
- Corriente
- Tensión
- Energía acumulada, si Zigbee2MQTT la publica correctamente
- Disponibilidad del dispositivo Zigbee
- Comportamiento tras recuperar la alimentación

La entidad no se considerará validada hasta probar órdenes, estados, mediciones y recuperación tras reinicio.

## Política de funcionamiento

### Funcionamiento normal

La pauta de encendido se definirá según la finalidad del skimmer:

- Intercambio gaseoso y aireación
- Exportación de materia orgánica
- Funcionamiento durante maduración
- Funcionamiento durante mantenimiento o alimentación

El Sonoff no debe conmutar repetidamente el skimmer para regular la espuma. El ajuste corresponde al propio equipo y a su nivel de agua; el enchufe solo aplicará estados operativos completos.

### Ventanas y pausas

Home Assistant podrá aplicar ventanas de funcionamiento o pausas programadas cuando exista una razón documentada, como alimentación, aditivos, mantenimiento o una pauta concreta de maduración.

No se apagará el skimmer automáticamente solo porque la potencia varíe dentro del funcionamiento normal. La potencia no es una medición fiable de la calidad de la espuma.

### Estado tras un corte

El `power_on_behavior` se configurará y probará según la pauta vigente del skimmer. Si se decide que no debe arrancar sin supervisión, se utilizará el estado apagado tras recuperar la alimentación y se generará una alerta para revisar el equipo.

Tras cada rearranque se comprobará:

- Nivel de agua de la cámara 2
- Toma de aire y tubo Venturi
- Ausencia de rebose de la copa
- Ausencia de microburbujas persistentes
- Funcionamiento de la bomba

## Condiciones de corte

Home Assistant podrá apagar y alertar cuando se produzca cualquiera de estas condiciones:

- El equipo debe permanecer apagado por mantenimiento
- Se detecta una fuga, desbordamiento o riesgo eléctrico
- La cámara del skimmer queda fuera de su nivel operativo
- La copa está llena o no está correctamente instalada
- Se activa una pausa documentada de alimentación o aditivos
- El dispositivo Zigbee queda no disponible durante una operación que requiera confirmación
- Se detecta un estado de alimentación anómalo

La potencia anómala puede indicar rotor bloqueado, toma de aire obstruida, funcionamiento sin agua o fallo eléctrico, pero no permite diagnosticar por sí sola cuál es la causa.

## Uso durante el ciclado y la maduración

La automatización no decidirá por sí sola cuándo encender o apagar el skimmer durante el ciclado o la maduración. La pauta deberá proceder del plan operativo correspondiente y quedar reflejada como una condición explícita.

Una orden de Home Assistant no convierte el skimmer en un sensor del estado biológico del acuario. El estado del equipo y el estado del sistema se registrarán por separado.

## Registro y avisos

Se registrarán:

- Encendidos y apagados
- Duración de cada estado
- Potencia, corriente y tensión
- Disponibilidad Zigbee
- Cortes eléctricos y reinicios
- Pausas por alimentación, aditivos o mantenimiento
- Avisos de potencia anómala
- Reboses o problemas de espuma observados manualmente

Se generará una alerta si el skimmer permanece apagado fuera de una ventana autorizada o no recupera el estado esperado tras un reinicio.

## Pruebas de aceptación

1. Encendido y apagado manual desde Home Assistant
2. Confirmación del estado real del Sonoff
3. Publicación de potencia, corriente y tensión
4. Aplicación de una pausa programada
5. Recuperación después de un corte eléctrico
6. Comprobación del comportamiento configurado tras recuperar la alimentación
7. Detección de pérdida de disponibilidad Zigbee2MQTT
8. Rearranque del skimmer sin rebose de la copa
9. Comprobación de que una pérdida de Home Assistant no deja una conmutación repetitiva
10. Desconexión manual segura durante el mantenimiento

## Límites

El sistema no debe utilizarse para ocultar un problema mecánico o hidráulico. Home Assistant no sustituye:

- Limpieza de copa, cuello, rotor, Venturi y cámara
- Comprobación del nivel de agua
- Ajuste de aire y entrada de agua
- Comprobación de salpicaduras y microburbujas
- Protección eléctrica y diferencial
- Supervisión durante el uso temporal sin copa

## Fuentes

- [Ficha del SONOFF S60ZBTPF](../sonoff-s60zbtpf/sonoff-s60zbtpf.md)
- [Ficha del Sicce Shark SKIMMER 300](sicce-shark-skimmer-300.md)
- [SONOFF S60ZBTPF/S60ZBTPG](https://sonoff.tech/products/sonoff-iplug-zigbee-smart-plug-s60-series)
- [SONOFF S60ZBTPF en Zigbee2MQTT](https://www.zigbee2mqtt.io/devices/S60ZBTPF.html)
- [Integración de Zigbee2MQTT con Home Assistant](https://www.zigbee2mqtt.io/guide/usage/integrations/home_assistant.html)
