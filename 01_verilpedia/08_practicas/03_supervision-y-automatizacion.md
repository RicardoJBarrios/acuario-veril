# Supervisión y automatización de un acuario

## Finalidad

La supervisión digital permite registrar estados, detectar desviaciones y avisar al cuidador. La automatización añade acciones predeterminadas. Son funciones distintas: disponer de una entidad o una alarma no demuestra que el equipo físico funcione ni autoriza por sí solo a cambiar su estado eléctrico.

## Cadena de observación

Una lectura útil depende de toda la cadena:

```text
fenómeno físico → sensor → red o pasarela → integración → entidad → registro → aviso o acción
```

Cada tramo puede fallar de forma independiente. Una entidad `unavailable` puede reflejar un problema de descubrimiento o comunicación y no una avería física; una entidad disponible puede publicar una medida incorrecta por colocación, calibración o método.

## Prioridades

- Detectar pérdida de comunicación y distinguirla de un valor normal
- Registrar temperatura, fugas, niveles o consumo con contexto y unidades
- Mantener alarmas accionables, con destinatario y respuesta definida
- Probar el comportamiento tras cortes eléctricos y reinicios
- Evitar ciclos de conmutación por lecturas aisladas o inestables
- Conservar control local seguro cuando la plataforma central no esté disponible

## Modos operativos

Los modos como normal, alimentación, mantenimiento, ausencia o emergencia deben definir qué equipos cambian, durante cuánto tiempo y cómo se recupera el estado seguro. Un modo temporal necesita caducidad o confirmación para evitar que una bomba, un calentador o un skimmer permanezcan en un estado accidental.

## Límites de la actuación automática

Apagar una carga puede eliminar un riesgo y crear otro. Antes de automatizar una respuesta se evalúan la pérdida de circulación, oxigenación, control térmico, reposición o filtración que puede provocar. Las acciones eléctricas sobre equipos críticos requieren pruebas controladas y una vía de aviso.

La supervisión no sustituye la inspección física, una referencia independiente ni el mantenimiento. Las tendencias se interpretan con la ubicación del sensor, su frecuencia de actualización, los cambios de configuración y las intervenciones realizadas.
