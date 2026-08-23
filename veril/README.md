# Implementación concreta de Veril

## Propósito

Este directorio documenta las decisiones, pendientes y criterios de aceptación de la implementación vigente de Veril. No contiene fichas generales reutilizables.

La definición general pertenece al [modelo de dimensiones](../fichas/dimensiones/modelo.md) y a las [fichas de dimensiones](../fichas/dimensiones/README.md). La configuración conjunta se documenta exclusivamente en [configuracion.md](configuracion.md).

La aplicación concreta de Química se encuentra en las [fichas de parámetros](../fichas/parametros/README.md), el [plan de ciclado](../ciclado/plan.md) y el [plan de maduración](../maduracion/plan.md). La aplicación concreta de Procesamiento se comprueba mediante su dimensión, el hardware correspondiente y esos planes operativos.

## Documentos

- [Configuración integrada](configuracion.md): relación entre las dimensiones, decisiones conjuntas y criterios globales de aceptación
- [Infraestructura](infraestructura.md): aplicación de la arquitectura AIO, cámaras, niveles, acceso y seguridad
- [Espacial](espacial.md): composición rocosa, sustrato, geometría, apoyos, playa y canal
- [Hidráulica](hidraulica.md): bombas, retorno, rutas de flujo y comprobaciones
- [Iluminación](iluminacion.md): luminaria, posición, cobertura, sombras y *shade*
- [Biología](biologia.md): colonización, población compatible y evolución
- [Química](quimica.md): aplicación de la dimensión química mediante parámetros, relaciones y tendencias
- [Procesamiento](procesamiento.md): aplicación del método Berlín, skimmer, superficies colonizadas y retirada

Cada ficha es propietaria de su materia. Las relaciones con otros aspectos deben expresarse mediante enlaces y consecuencias concretas, sin repetir las definiciones generales ni la configuración integrada.

Las fichas específicas de microfauna se encuentran en [`fichas/biologia/veril/`](../fichas/biologia/veril/); sus funciones generales pertenecen a las fichas de referencia de `fichas/biologia/`.
