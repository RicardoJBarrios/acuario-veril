# 2026-09-29 — Ajuste de la protección del enchufe del retorno

## Estado

Configuración aplicada y verificada mediante Zigbee2MQTT. No se comprobó el caudal físico de la bomba.

## Contexto

El enchufe SONOFF S60ZBTPF `off-act-02` alimenta provisionalmente la bomba de retorno Sicce Micra Plus 600. Tras una prueba manual anterior, el usuario informó que la salida se apagaba y volvía a encenderse de inmediato, aunque Home Assistant la mostraba apagada; identificó `Inching control set` como causa y lo desactivó. Antes de este ajuste, la lectura de Zigbee2MQTT ya mostraba `inching_control: DISABLE` y `inching_mode: OFF`; esta operación no cambió esos dos parámetros.

El histórico eléctrico consultado para caracterizar la carga mostró una potencia mediana de 6,50 W, percentil 95 de 6,87 W, percentil 99 de 7,01 W y máximo de 7,27 W. Las muestras positivas de corriente estuvieron entre 0,05 y 0,06 A. Estos datos describen el consumo observado; no demuestran el caudal ni el estado mecánico de la bomba.

## Ejecución

El 29/09/2026 se modificó en Zigbee2MQTT la configuración de protección de `off-act-02`:

| Parámetro | Valor aplicado |
| --- | --- |
| Protección de la toma (`outlet_control_protect`) | Activada |
| Máximo de potencia | Activado, 20 W |
| Máximo de corriente | Activado, 0,3 A |
| Mínimo de potencia | Desactivado |
| Mínimo de corriente | Desactivado |
| Tensión mínima y máxima | Desactivadas |
| Control de inching | Sin cambios: desactivado (`DISABLE`) |
| Modo de inching | Sin cambios: `OFF` |

Los límites de 20 W y 0,3 A se adoptaron como guardarraíles iniciales con margen sobre el consumo registrado de esta unidad. No son límites certificados por Sicce, umbrales probados de disparo ni una protección contra falta de caudal o funcionamiento en seco.

## Evidencia digital

La lectura de vuelta de Zigbee2MQTT a las **18:14:36 UTC** del 29/09/2026 informó:

- Salida: `OFF`.
- Potencia: 0 W.
- Corriente: 0 A.
- Protección de toma activada y máximos de 20 W y 0,3 A habilitados.
- Inching desactivado, modo `OFF`.

Home Assistant había mostrado `switch.0xa4c1380b0c1effff` apagado a las **17:57:00.988982 UTC**, antes de aplicar los límites. Esa lectura previa no se presenta como confirmación posterior del cambio. La consulta de Zigbee2MQTT confirma los parámetros reportados por el dispositivo, no el estado físico del flujo.

## Límites y pendientes

- No se accionó el enchufe durante esta operación ni se probó deliberadamente el disparo de las protecciones.
- No se comprobó físicamente que la Sicce estuviera moviendo agua; la lectura `OFF`, 0 W y 0 A corresponde solo al momento de la consulta.
- La identificación física de la etiqueta `off-act-02` sigue pendiente de confirmación.
- Si una protección llegara a dispararse en uso normal, revisar la causa antes de rearmarla; no elevar automáticamente los límites.

## Referencias

- [Configuración hidráulica vigente: alimentación y protección eléctrica del retorno](../../../02_configuracion/01_dimensiones/03_hidraulica.md#alimentación-y-protección-eléctrica-del-retorno)
- [Integración de la Sicce Micra Plus 600 con Home Assistant y Zigbee2MQTT](../../../01_verilpedia/04_hardware/sicce-micra-plus-600/home-assistant-zigbee2mqtt.md)
