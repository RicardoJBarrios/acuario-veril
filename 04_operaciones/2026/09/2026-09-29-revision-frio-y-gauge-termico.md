# 2026-09-29 — Revisión del extremo frío y actualización del panel térmico

## Estado

La revisión inicial documentó 24,0 °C como límite inferior y cambió el gauge y las tarjetas de `acuario-veril`. Más tarde se contrastó una propuesta adicional y se afinó la clasificación: 24–24,5 °C fresca pero razonablemente normal; 23–24 °C excursión fría tolerable, investigar si persiste; <23 °C fuera del objetivo operativo; <22 °C prioridad local de revisión. El gauge y las tarjetas de Home Assistant aún requieren reflejar estas bandas. No se instaló calentador ni se modificó la automatización térmica.

## Decisión y alcance

La clasificación baja se estableció usando tanto guías de TMC como estudios experimentales con corales y peces. Las guías generales discrepan en su alcance: TMC publica 23–26 °C para corales y también aconseja 24–26 °C como óptimo marino y precaución por debajo de 24 °C para peces tropicales. El estudio de *A. millepora* a 23 °C no se generaliza a la comunidad mixta; el estudio de diez peces damisela halló reducciones subletales de rendimiento entre 29 y 23 °C, variables entre especies. La lectura de la evidencia no establece daño agudo a 23 °C ni umbral a 22 °C. Se adopta como gestión local 24–24,5 °C fresca, 23–24 °C excursión a investigar si persiste, <23 °C fuera del objetivo y <22 °C prioridad de revisión. Para calefacción futura, se adopta como principio de diseño mantener el mínimo habitual aproximadamente en 24,5–25 °C, sin fijar todavía umbrales ON/OFF ni modificar el piloto.

Una lectura inferior a 23,0 °C queda fuera de la envolvente general y requiere comprobar la frescura de `off-sns-05` y, cuando sea posible, contrastar con un termómetro independiente, además de valorar duración, tendencia y fauna presente. Veril no tiene calentador ni alarma o acción automática de calefacción. No se fijaron niveles de emergencia fría, consigna de calentador, potencia ni histéresis; quedan ligados a la fauna seleccionada, al registro de mínimos estacionales y al equipo real.

La ficha de configuración amplía los requisitos previos a instalar calefacción: termostato integrado comprobado, límite independiente frente a sobretemperatura, coordinación con el Rowenta mediante zona muerta, y validación de ubicación/sonda. Estas tareas son requisitos de diseño futuro, no equipos o automatizaciones instalados.

## Cambio inicial en Home Assistant y rectificación pendiente

En la actuación inicial del 29 de septiembre, el dashboard de almacenamiento `acuario-veril` se modificó únicamente en su presentación:

- Gauge de `sensor.0xa4c13810b72fffff_temperature`: escala visual ampliada de **22–31 °C** a **20–31 °C**. Los segmentos muestran frío bajo el límite aceptable, banda baja de vigilancia, zona óptima y bandas cálidas ya adoptadas. Los extremos de la escala son visuales, no nuevos umbrales biológicos.
- Tarjeta **«Rango térmico objetivo»**: ahora incluye bandas de frío y calor y diferencia 24,0–24,5 °C de valores inferiores a 24,0 °C.
- Nueva tarjeta **«Frío y calefacción»**: indica que no hay calentador ni alarma/control de calefacción y muestra las comprobaciones necesarias ante una lectura inferior al límite.

En esa actuación inicial, la configuración completa se guardó y leyó de vuelta; se confirmaron el gauge con `min: 20`, `max: 31` y las dos tarjetas. En esta sesión no fue posible actualizar el dashboard: no hay herramienta MCP de Home Assistant expuesta ni están configuradas `HOME_ASSISTANT_URL` y `HOME_ASSISTANT_TOKEN` para la API local. Por tanto, el contenido del gauge y las tarjetas puede seguir mostrando límites anteriores; queda pendiente sincronizarlo con las bandas 24/23/22 °C. No se cambió ninguna automatización ni estado de actuador.

## Telemetría asociada de Home Assistant

| Variable | Entidad | Valor observado | Momento | Alcance |
| --- | --- | --- | --- | --- |
| Temperatura del agua | `sensor.0xa4c13810b72fffff_temperature` (`off-sns-05`) | 26,6 °C | Estado actualizado 19:14:18 UTC; consultado a las 19:30 UTC | Lectura retenida del sensor, no una nueva medición a las 19:30 |
| Antigüedad del último mensaje Zigbee | `sensor.veril_water_sensor_age` | 5,7 min | 19:30 UTC | Confirma comunicación reciente, no que el valor numérico de temperatura se actualizara en ese momento |
| Automatización térmica | `automation.veril_iniciar_refrigeracion_preventiva_del_despacho` | `on` | 19:30 UTC | La automatización de refrigeración continúa habilitada; no se modificó |
| Estado del controlador | `input_select.veril_thermal_controller_state` | `normal` | Última actualización 16:54 UTC | Estado digital retenido; no representa una acción física nueva |

La lectura del agua estaba dentro del intervalo aceptable en la consulta, por lo que no se observó un episodio frío. HA no ofrece aquí una confirmación independiente de temperatura ni prueba física del funcionamiento del Rowenta.

## Referencias

- [Régimen térmico adoptado](../../../02_configuracion/README.md#régimen-térmico-adoptado)
- [Plan de control térmico y calefacción futura](../../../02_configuracion/control-termico.md#extremo-frío-y-preparación-de-calefacción)
- [Puesta en servicio y mediciones iniciales del control térmico](2026-09-27-puesta-en-servicio-control-termico.md)
- [Guía de cuidado de corales de Tropical Marine Centre](https://www.tropicalmarinecentre.com/en/downloads/files/care_sheets/Corals/Corals.pdf)
- [Tropical Marine Centre: control de temperatura y orientación general sobre peces tropicales](https://tropicalmarinecentre.com/uk/fan-and-temperature-control)
- [Johansen et al. (2015), rendimiento natatorio de diez especies de peces damisela a 23 °C frente a 29 °C](https://doi.org/10.1093/conphys/cov039)
- [Estudio experimental de *Acropora millepora* con tratamiento a 23 °C](https://doi.org/10.1007/s00338-019-01881-x)
- [Helgoe et al. (2024), mecanismos de blanqueamiento, incluidos los desencadenados por frío](https://doi.org/10.1111/brv.13042)
