# Implementación concreta de Veril

## Propósito

Este directorio documenta cómo se concretan en Veril las dimensiones, la configuración biológica y las decisiones de diseño descritas en `fichas/`. El display útil es de aproximadamente **60 × 32 × 40 cm**. No contiene fichas generales reutilizables.

La definición general de cada dimensión pertenece a las fichas de [dimensiones](../fichas/dimensiones/README.md). La [dimensión espacial](../fichas/dimensiones/dimension-espacial.md), la [dimensión de infraestructura](../fichas/dimensiones/dimension-infraestructura.md), la [dimensión biológica](../fichas/dimensiones/dimension-biologica.md), la [dimensión hidráulica](../fichas/dimensiones/dimension-hidraulica.md), la [dimensión de iluminación](../fichas/dimensiones/dimension-iluminacion.md), la [dimensión química](../fichas/dimensiones/dimension-quimica.md) y la [dimensión de procesamiento](../fichas/dimensiones/dimension-procesamiento.md) establecen las restricciones que esta implementación debe satisfacer.

Estas fichas no vuelven a explicar esas dimensiones. Registran decisiones de Veril, fuentes de diseño, pendientes y criterios de aceptación observables.

## Documentos

- [Roca](roca.md): aplicación de la dimensión espacial a la composición, geometría, apoyos y estabilidad
- [Sustrato](sustrato.md): producto, granulometría, profundidad y distribución previstas
- [Hidráulica](hidraulica.md): aplicación de la dimensión hidráulica a bombas, retorno, rutas de flujo y comprobaciones
- [Iluminación](iluminacion.md): aplicación de la dimensión de iluminación a luminaria, posición, cobertura, sombras y *shade*
- [Biología](biologia.md): aplicación de las dimensiones biológica y espacial a colonización, población compatible y evolución

## Responsabilidad de cada ficha

Cada documento es propietario de su materia. Las relaciones con otros aspectos se expresan mediante enlaces, sin repetir explicaciones generales:

- [Roca](roca.md) conserva la decisión geométrica y estructural del hardscape
- [Sustrato](sustrato.md) conserva la decisión de sustrato, playa y canal
- [Hidráulica](hidraulica.md) conserva la decisión de bombas, retorno y rutas de flujo
- [Iluminación](iluminacion.md) conserva la decisión de luminaria, posición y cobertura
- [Biología](biologia.md) conserva la decisión de colonización, población y crecimiento

Las imágenes conceptuales y la composición visual se documentan en [Roca](roca.md). La integración final de las dimensiones y de estas decisiones se documentará en la ficha específica de configuración del sistema.
