# 2026-09-23 — Pesaje y medición del desplazamiento del hardscape

## Estado

Operación documentada a partir de medidas físicas comunicadas por el propietario; volumen calculado con dimensiones interiores aproximadas.

## Ejecución observada

Se retiró toda la roca del display. Al retirarla, el nivel del agua del display
bajó **12 mm**. Las piezas se pesaron fuera del display:

| Elemento descrito por el propietario | Masa comunicada |
| --- | ---: |
| Isla pequeña de la esquina trasera izquierda | 150 g |
| Isla de la esquina frontal izquierda, con zoas | 250 g |
| Estructura principal | 7 kg |
| **Total** | **7,4 kg** |

Después se devolvió la roca al display y, tras reponer agua evaporada en una
cantidad no medida, el nivel volvió a quedar a **37 mm del borde superior**.
No se midió la cantidad de agua añadida.

## Cálculo del desplazamiento

La planta interior observada del display es de aproximadamente **594 × 308 mm**.
Tomando el descenso comunicado de **12 mm** como variación de nivel y
aproximando la sección del display a un rectángulo constante:

```text
Área de la planta = 594 × 308 = 182.952 mm²
Volumen equivalente = 182.952 × 12 = 2.195.424 mm³ ≈ 2,20 L
```

Por tanto, el cambio de nivel corresponde a un desplazamiento equivalente
estimado de **2,20 L**. Es un cálculo geométrico a partir del nivel observado,
no una conversión del peso a volumen. Las dimensiones son aproximadas y no se
registraron las condiciones hidráulicas ni los niveles de las cámaras durante
la prueba; el resultado no establece el volumen operativo total del sistema.

## Resultado y límites

- Masa total de las tres partes pesadas: **7,4 kg**.
- Desplazamiento equivalente calculado a partir de 12 mm: **aproximadamente 2,20 L**.
- Tras devolver la roca y reponer agua evaporada (cantidad desconocida), el
  nivel observado quedó a **37 mm del borde**.
- La reposición no permite calcular el agua evaporada ni el volumen de agua del
  display o del sistema.
- El peso por sí solo no permite calcular el volumen desplazado sin conocer la
  densidad y otras propiedades del material; por ello se conserva como medida
  independiente.

## Telemetría asociada

No se incorporó telemetría de Home Assistant: las magnitudes de esta operación
son medidas físicas comunicadas (nivel y peso), y no se identificó una lectura
de nivel pertinente para contrastarlas.

## Fuentes internas

- [Dimensiones interiores y estimación del volumen del display](../../../02_configuracion/01_dimensiones/02_espacial.md#volumen-de-agua-del-display)
- [Nivel observado el 13 de septiembre](2026-09-13-reposicion-manual-y-observacion-nivel.md)
