# Implementación concreta de Veril

## Propósito

Este directorio documenta las decisiones, pendientes y criterios de aceptación de la implementación vigente de Veril. No contiene fichas generales reutilizables.

La definición general pertenece al [modelo de dimensiones](../01_fichas/01_dimensiones/00_modelo.md) y a las [fichas de dimensiones](../01_fichas/01_dimensiones/00_README.md). La configuración conjunta se documenta exclusivamente en [configuración integrada](00_configuracion.md).

La aplicación concreta de Química se encuentra en las [fichas de parámetros](../01_fichas/03_parametros/README.md), el [plan de ciclado](../03_ciclado/plan.md) y el [plan de maduración](../04_maduracion/plan.md). La aplicación concreta de Procesamiento se comprueba mediante su dimensión, el hardware correspondiente y esos planes operativos.

## Documentos

- [Configuración integrada](00_configuracion.md): relación entre las dimensiones, decisiones conjuntas y criterios globales de aceptación
- [Infraestructura](01_infraestructura.md): aplicación de la arquitectura AIO, cámaras, niveles, acceso y seguridad
- [Espacial](02_espacial.md): composición rocosa, sustrato, geometría, apoyos, playa y canal
- [Hidráulica](03_hidraulica.md): bombas, retorno, rutas de flujo y comprobaciones
- [Iluminación](04_iluminacion.md): luminaria, posición, cobertura, sombras y *shade*
- [Química](05_quimica.md): aplicación de la dimensión química mediante parámetros, relaciones y tendencias
- [Biología](06_biologia.md): colonización, población compatible y evolución
- [Procesamiento](07_procesamiento.md): aplicación del método Berlín, skimmer, superficies colonizadas y retirada

Cada ficha es propietaria de su materia. Las relaciones con otros aspectos deben expresarse mediante enlaces y consecuencias concretas, sin repetir las definiciones generales ni la configuración integrada.

La función general de la microfauna pertenece a las fichas de referencia de `01_fichas/02_biologia/`. Su papel esperado en Veril se resume en [Biología](06_biologia.md), y su incorporación, si procede, se decide en el [plan de microfauna de maduración](../04_maduracion/plan-microfauna.md).
