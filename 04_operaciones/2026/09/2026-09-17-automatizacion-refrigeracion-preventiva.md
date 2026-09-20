# 17 de septiembre de 2026: automatización de la refrigeración preventiva del despacho

## Alcance y evidencia

El 17 de septiembre de 2026 se añadió la automatización `automation.veril_iniciar_refrigeracion_preventiva_del_despacho` para usar el aire acondicionado del despacho como medida de refrigeración ambiental de Veril. Esta entrada registra la configuración declarada y sus condiciones de seguridad; no acredita todavía cuánto baja la temperatura del agua durante una sesión real.

La autoridad de la integración y de la automatización es la [ficha local del climatizador Rowenta](../../../../../sistemas/homelab/domotica/home-assistant/documentacion/integraciones/off-clm-01-rowenta.md#automatización-térmica-de-veril). El régimen térmico que da sentido a esta actuación está en [Régimen térmico adoptado](../../../02_configuracion/README.md#régimen-térmico-adoptado).

## Configuración aplicada

La automatización ordena una sesión de refrigeración a **24 °C** y ventilador alto cuando se cumplen simultáneamente estas condiciones:

- El sensor de agua `off-sns-05` alcanza al menos 28,0 °C y su lectura tiene menos de 90 minutos.
- Al menos dos de los tres sensores ambientales del despacho (`off-sns-01`, `off-sns-06` y `off-sns-08`) alcanzan al menos 28,5 °C y sus lecturas tienen menos de 90 minutos.
- El estado manual sincronizado del climatizador está confirmado y su estado de alimentación declarado es apagado.

El apagado automático se aplica incluso si el climatizador se encendió manualmente. Requiere que el agua permanezca por debajo de **27,2 °C durante 45 minutos** y que, al final de ese periodo, al menos dos de los tres sensores ambientales indiquen como máximo **27,0 °C**.

La automatización no actúa con datos necesarios `unknown` o `unavailable`. Si Home Assistant o las automatizaciones se recargan durante el periodo de 45 minutos, el temporizador vuelve a empezar y se mantiene la refrigeración hasta completar de nuevo el periodo: es el comportamiento conservador configurado.

## Marcas para la comprobación posterior

Cada inicio automático deja en el Libro de registro de Home Assistant el evento:

`Veril — Refrigeracion automatica iniciada: consigna 24 C.`

Cada apagado automático deja:

`Veril — Refrigeracion apagada por automatizacion: recuperacion termica estable.`

Estas dos marcas se usarán para comparar el momento de cada orden con los históricos de `off-sns-05` y de los tres sensores ambientales. Permiten medir la dirección, el desfase y la magnitud de la respuesta del agua; una orden registrada no equivale por sí sola a una reducción física demostrada.

## Estado tras el cambio

**Configuración documentada:** La automatización y sus marcadores de inicio y apagado están definidos en Home Assistant.

**Pendiente de comprobar:** Primera sesión automática completa, historial asociado y efecto observable sobre la temperatura del agua. Antes de permitir una orden física, el panel del climatizador y sus *shadows* deben estar sincronizados manualmente; el aparato no aporta realimentación propia de su estado.
