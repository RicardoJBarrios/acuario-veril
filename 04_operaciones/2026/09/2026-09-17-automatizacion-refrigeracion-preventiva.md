# 17 de septiembre de 2026 — Automatización de la refrigeración preventiva del despacho

Se añadió la automatización
`automation.veril_iniciar_refrigeracion_preventiva_del_despacho` para utilizar
el aire acondicionado del despacho como refrigeración ambiental de Veril.

## Configuración aplicada

La automatización ordena una sesión de refrigeración a **24 °C** y ventilador alto cuando se cumplen simultáneamente estas condiciones:

- El sensor de agua `off-sns-05` alcanza al menos 28,0 °C y su lectura tiene menos de 90 minutos.
- Al menos dos de los tres sensores ambientales del despacho (`off-sns-01`, `off-sns-06` y `off-sns-08`) alcanzan al menos 28,5 °C y sus lecturas tienen menos de 90 minutos.
- El estado manual sincronizado del climatizador está confirmado y su estado de alimentación declarado es apagado.

El apagado automático se aplica incluso si el climatizador se encendió manualmente. Requiere que el agua permanezca por debajo de **27,2 °C durante 45 minutos** y que, al final de ese periodo, al menos dos de los tres sensores ambientales indiquen como máximo **27,0 °C**.

La automatización no actúa con datos necesarios `unknown` o `unavailable`. Si Home Assistant o las automatizaciones se recargan durante el periodo de 45 minutos, el temporizador vuelve a empezar y se mantiene la refrigeración hasta completar de nuevo el periodo.

## Marcas configuradas en Home Assistant

Cada inicio automático deja en el Libro de registro de Home Assistant el evento:

`Veril — Refrigeracion automatica iniciada: consigna 24 C.`

Cada apagado automático deja:

`Veril — Refrigeracion apagada por automatizacion: recuperacion termica estable.`

## Referencias

- [Ajuste del 22 de septiembre](2026-09-22-ajuste-refrigeracion-preventiva-bajo-27.md).
- [Ajuste del 23 de septiembre](2026-09-23-ajuste-control-termico-agua.md).
- [Revisión del 24 de septiembre](2026-09-24-revision-observacion-control-termico.md).
