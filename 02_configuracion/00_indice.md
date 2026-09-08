# Implementación concreta de Veril

## Propósito

Este directorio documenta las decisiones, pendientes y criterios de aceptación de la implementación vigente de Veril. No contiene fichas generales reutilizables.

La definición general pertenece al [modelo de dimensiones](../01_verilpedia/01_dimensiones/README.md) y a las fichas de dimensiones. La configuración conjunta se documenta exclusivamente en [configuración integrada](README.md).

La aplicación concreta de Química se encuentra en las [fichas de parámetros](../01_verilpedia/03_parametros/README.md), el [plan de ciclado](../03_pendientes/ciclado/plan.md) y el [plan de maduración](../03_pendientes/maduracion/plan.md). La aplicación concreta de Procesamiento se comprueba mediante su dimensión, el hardware correspondiente y esos planes operativos.

## Documentos

- [Configuración integrada](README.md): relación entre las dimensiones, decisiones conjuntas y criterios globales de aceptación
- [Infraestructura](01_dimensiones/01_infraestructura.md): aplicación de la arquitectura AIO, cámaras, niveles, acceso y seguridad
- [Espacial](01_dimensiones/02_espacial.md): composición rocosa, sustrato, geometría, apoyos, playa y canal
- [Hidráulica](01_dimensiones/03_hidraulica.md): bombas, retorno, rutas de flujo y comprobaciones
- [Iluminación](01_dimensiones/04_iluminacion.md): luminaria, posición, cobertura, sombras y *shade*
- [Química](01_dimensiones/05_quimica.md): aplicación de la dimensión química mediante parámetros, relaciones y tendencias
- [Biología](01_dimensiones/06_biologia.md): colonización, población compatible y evolución
- [Procesamiento](01_dimensiones/07_procesamiento.md): aplicación del método Berlín, skimmer, superficies colonizadas y retirada

## Estructura del directorio

- [Hardscape](02_hardscape/README.md): composición, plantilla, inventario fotográfico y registro visual de la roca
- [Biología específica](03_biologia/README.md): criterios de selección, candidatos y escenarios del proyecto
- [Identidad gráfica](identidad-grafica.md): nombre, logotipo y criterios visuales de Veril

Los documentos de `01_dimensiones/` mantienen la correspondencia con las siete dimensiones generales de [Verilpedia](../01_verilpedia/01_dimensiones/README.md). `README.md` integra sus decisiones sin sustituir las fichas propietarias. Los directorios `02` y `03` reúnen bloques específicos del proyecto que necesitan más de un documento o recursos visuales.

Cada ficha es propietaria de su materia. Las relaciones con otros aspectos deben expresarse mediante enlaces y consecuencias concretas, sin repetir las definiciones generales ni la configuración integrada.

La función general de la microfauna pertenece a las fichas de [Verilpedia](../01_verilpedia/02_biologia/01_microorganismos/02_microfauna/README.md). Su papel esperado en Veril se resume en [Biología](01_dimensiones/06_biologia.md), y su incorporación, si procede, se decide en el [plan de microfauna de maduración](../03_pendientes/maduracion/plan-microfauna.md).

Las actuaciones que materializan o comprueban esta configuración se registran en [Operaciones](../04_operaciones/README.md). Estas fichas pueden resumir el estado vigente y enlazar la operación que lo acredita, pero no sustituyen su registro fechado.
