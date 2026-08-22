# Implementación espacial de Veril

## Propósito

Este directorio documenta exclusivamente la implementación concreta del aquascape de Veril. El display útil es de aproximadamente **60 × 32 × 40 cm**. No contiene fichas generales reutilizables.

La definición general del aquascape pertenece a la [dimensión espacial](../fichas/dimensiones/dimension-espacial.md). La [dimensión física](../fichas/dimensiones/dimension-fisica.md), la [dimensión de comunidad](../fichas/dimensiones/dimension-comunidad.md) y la [dimensión de procesamiento](../fichas/dimensiones/dimension-procesamiento.md) establecen las restricciones que esta implementación debe satisfacer.

Estas fichas no vuelven a explicar esas dimensiones. Registran decisiones de Veril, fuentes de diseño, pendientes y criterios de aceptación.

## Documentos

- [Roca](roca.md): composición, geometría, apoyos y estabilidad de Veril
- [Sustrato](sustrato.md): producto, granulometría, profundidad y distribución previstas
- [Hidrodinámica](hidrodinamica.md): bombas, retorno, rutas de flujo y comprobaciones
- [Iluminación](iluminacion.md): luminaria, posición, cobertura, sombras y shade
- [Biología](biologia.md): colonización, pared viva, población compatible y evolución

## Responsabilidad de cada ficha

Cada documento es propietario de su materia. Las relaciones con otros aspectos se expresan mediante enlaces, sin repetir explicaciones generales:

- [Roca](roca.md) conserva la decisión geométrica y estructural del hardscape
- [Sustrato](sustrato.md) conserva la decisión de sustrato, playa y canal
- [Hidrodinámica](hidrodinamica.md) conserva la decisión de bombas, retorno y rutas de flujo
- [Iluminación](iluminacion.md) conserva la decisión de luminaria, posición y cobertura
- [Biología](biologia.md) conserva la decisión de colonización, población y crecimiento

Las imágenes conceptuales y la composición visual se documentan en [Roca](roca.md). La integración final de las dimensiones y de estas decisiones se documentará en la ficha específica de configuración del sistema.
