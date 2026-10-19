# 29 de septiembre de 2026 — Revisión del extremo frío y actualización del panel térmico

## Clasificación adoptada

Durante la revisión se adoptaron estas bandas locales:

| Temperatura | Clasificación |
| --- | --- |
| 24–24,5 °C | Fresca, razonablemente normal |
| 23–24 °C | Excursión fría tolerable; investigar si persiste |
| <23 °C | Fuera del objetivo operativo |
| <22 °C | Prioridad local de revisión |

Para el diseño de calefacción futura se adoptó como referencia un mínimo
habitual aproximado de **24,5–25 °C**.

## Cambio realizado en Home Assistant

Se modificó la presentación del dashboard `acuario-veril`:

- Se amplió la escala del gauge de `sensor.0xa4c13810b72fffff_temperature` de **22–31 °C** a **20–31 °C**.
- Se actualizó la tarjeta «Rango térmico objetivo» con bandas de frío y calor, diferenciando 24,0–24,5 °C de valores inferiores a 24,0 °C.
- Se añadió la tarjeta «Frío y calefacción».

La configuración se guardó y leyó de vuelta: el gauge mostró `min: 20` y
`max: 31`, y se confirmaron ambas tarjetas.

## Telemetría asociada de Home Assistant

| Variable | Entidad | Valor observado | Momento | Alcance |
| --- | --- | --- | --- | --- |
| Temperatura del agua | `sensor.0xa4c13810b72fffff_temperature` (`off-sns-05`) | 26,6 °C | Estado actualizado 19:14:18 UTC; consultado a las 19:30 UTC | Lectura retenida del sensor, no una nueva medición a las 19:30 |
| Antigüedad del último mensaje Zigbee | `sensor.veril_water_sensor_age` | 5,7 min | 19:30 UTC | Confirma comunicación reciente, no que el valor numérico de temperatura se actualizara en ese momento |
| Automatización térmica | `automation.veril_iniciar_refrigeracion_preventiva_del_despacho` | `on` | 19:30 UTC | La automatización de refrigeración continúa habilitada; no se modificó |
| Estado del controlador | `input_select.veril_thermal_controller_state` | `normal` | Última actualización 16:54 UTC | Estado digital retenido |

## Referencias

- [Régimen térmico adoptado](../../../02_configuracion/README.md#régimen-térmico-adoptado)
- [Plan de control térmico y calefacción futura](../../../02_configuracion/control-termico.md#extremo-frío-y-preparación-de-calefacción)
- [Puesta en servicio y mediciones iniciales del control térmico](2026-09-27-puesta-en-servicio-control-termico.md)
- [Guía de cuidado de corales de Tropical Marine Centre](https://www.tropicalmarinecentre.com/en/downloads/files/care_sheets/Corals/Corals.pdf)
- [Tropical Marine Centre: control de temperatura y orientación general sobre peces tropicales](https://tropicalmarinecentre.com/uk/fan-and-temperature-control)
- [Johansen et al. (2015), rendimiento natatorio de diez especies de peces damisela a 23 °C frente a 29 °C](https://doi.org/10.1093/conphys/cov039)
- [Estudio experimental de *Acropora millepora* con tratamiento a 23 °C](https://doi.org/10.1007/s00338-019-01881-x)
- [Helgoe et al. (2024), mecanismos de blanqueamiento, incluidos los desencadenados por frío](https://doi.org/10.1111/brv.13042)
