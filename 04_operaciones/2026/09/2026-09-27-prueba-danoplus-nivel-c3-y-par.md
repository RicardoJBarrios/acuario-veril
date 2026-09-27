# 2026-09-27 — Prueba del DanoPlus, PAR ambiental y nivel de C3

## Estado

Operación documentada a partir de mediciones comunicadas por el propietario.
Los valores PAR son lecturas manuales del DanoPlus. Los volúmenes, tasas y DLI
son cálculos aproximados con las hipótesis expresadas abajo.

## Preparación comunicada

El propietario probó el medidor DanoPlus **S/N A26121206** y midió la luz
ambiental en varios puntos del tanque antes de disponer de una **AI Prime
16HD**. La luminaria todavía no está en Veril, por lo que estas lecturas no
comparan su aporte con el de la iluminación ambiental. El propietario confirmó
que el medidor se calibró esa misma mañana, antes de las medidas, siguiendo el
manual.

La ficha del [DanoPlus DP-414](../../../01_verilpedia/04_hardware/danoplus-dp-414/danoplus-dp-414.md)
describe el procedimiento del fabricante como calibración de punto cero al
cubrir por completo el sensor. La calibración comunicada no implica una
comparación de exactitud con un medidor patrón ni una aceptación metrológica de
la unidad de Veril. No se anotaron la hora de calibración, repeticiones de
control ni fuente externa de referencia.

## Lecturas PAR comunicadas

Las horas se conservan tal como se comunicaron; se interpretan como hora local
de Canarias. Los puntos corresponden a la cima, terraza, roca baja y arena del
hardscape. Unidad: **µmol fotones·m⁻²·s⁻¹ (PAR)**.

| Hora | Cima | Terraza | Roca baja | Arena |
| --- | ---: | ---: | ---: | ---: |
| 09:00 | 0,6 | 0,4 | 0,4 | 0,4 |
| 11:30 | 5,6 | 5,0 | 4,0 | 3,3 |
| 13:55 | 7,0 | 6,3 | 5,0 | 3,6 |
| 16:30 | 2,5 | 2,0 | 1,5 | 0,9 |

La AI Prime 16HD aún no está disponible ni instalada en Veril. La luz superior
de la habitación estaba encendida, condición que el propietario indica que se
da en aproximadamente el 90 % de las ocasiones durante ese tramo. El
propietario considera insignificante su aportación, aunque no se midió por
separado. No hubo medición simultánea en el exterior. Por ello, los datos
representan PAR ambiental combinado en los puntos del tanque antes de instalar
la Prime; no son una medición aislada de luz solar.

## Estimación del DLI ambiental

Como estimación exploratoria se integraron las cuatro lecturas de luz ambiental
combinada mediante interpolación lineal por tramos. Para cerrar el cálculo se
supuso PAR cero al amanecer y al ocaso, usando la ventana solar **07:55–19:55**
indicada en la conversación y no contrastada en este registro. No se midió el
PAR antes de las 09:00 ni después de las 16:30; por tanto, esos extremos son
una simplificación del cálculo y no una observación de que la luz combinada
fuera cero. El método trapezoidal da:

| Zona | DLI aproximado |
| --- | ---: |
| Cima | 0,14 mol fotones·m⁻²·día⁻¹ |
| Terraza | 0,13 mol fotones·m⁻²·día⁻¹ |
| Roca baja | 0,10 mol fotones·m⁻²·día⁻¹ |
| Arena | 0,07 mol fotones·m⁻²·día⁻¹ |

No son integrales medidas de forma continua. Dependen de la interpolación, de
la extrapolación simplificada a cero en los extremos y de que no hubiera
máximos relevantes entre las cuatro tandas. Incluyen la luz superior de la
habitación, cuya contribución el propietario considera insignificante pero no
se cuantificó. Describen únicamente la luz ambiental combinada de este día y
no constituyen una integral diaria observada, curva solar aislada, curva
estacional ni objetivo de iluminación.

El máximo comunicado fue **7,0 PAR** en la cima a las 13:55. Como referencia
aritmética, 100 PAR durante 8 horas equivaldrían a un DLI de 2,88 mol
fotones·m⁻²·día⁻¹; el DLI exploratorio de la cima sería alrededor del 5 % de
ese ejemplo. La comparación es ilustrativa y no representa una lectura real de
la Prime ni prescribe potencia, altura o fotoperiodo.

## Nivel de agua y estimación de pérdida

El propietario midió el nivel de C3 a **16 cm (160 mm) del borde superior**.
Como referencia, después de la reposición del 26 de septiembre la lectura
comunicada para C3 había quedado a **117 mm del borde**. La diferencia entre
las cotas es, por tanto, **43 mm**, suponiendo que se usó la misma arista y el
mismo punto de referencia.

La huella interior documentada para Retorno/C3 es aproximadamente **139 × 77
mm**, con un área de 10.703 mm². Aplicando esa área completa al descenso de
nivel:

```text
10.703 mm² × 43 mm = 460.229 mm³ ≈ 0,46 L
```

Esto equivale geométricamente a unos **0,46 L por cada 24 horas**. Si el
intervalo real hubiera sido de unas 23 horas, la tasa normalizada sería de
aproximadamente **0,48 L/día**. No se registró la hora exacta de la medición de
hoy, por lo que se conserva como orden de magnitud, no como una tasa precisa.

El cálculo usa toda la sección de la cámara y no descuenta la bomba, sensores u
otros objetos sumergidos. Tampoco se registraron posibles salpicaduras,
retiradas, fugas, transferencias o reposiciones entre ambas cotas. En
consecuencia, se documenta como **descenso aparente compatible con pérdida por
evaporación**, bajo la hipótesis de que no hubo otros cambios de agua, y no
como una medición directa del volumen evaporado.

La lectura de 117 mm del 26 de septiembre se tomó después de añadir unos 1,85
L de agua del barril, identificada entonces como agua salada. Esa condición es
parte del contexto de la cota de referencia y no se interpreta como una
reposición de evaporación con RO/DI.

## Interpretación y límites

- En esta serie de luz ambiental combinada el PAR fue bajo y descendió desde el máximo de las 13:55 hasta las 16:30. Cuatro tandas no descartan picos entre lecturas ni describen otros días.
- La medición ambiental previa a disponer de la Prime no permite fijar por sí sola una potencia, altura o programación para la iluminación artificial.
- La calibración de cero indicada por el manual no prueba exactitud espectral ni comparabilidad con un Apogee u otro patrón.
- La estimación de 0,46–0,48 L/día depende de intervalo aproximado, geometría idealizada y ausencia de otras entradas o salidas; no es telemetría ni una medida de volumen recogido.
- La lectura aislada de nivel no permite calcular el consumo medio estacional ni dimensionar por sí sola un depósito de reposición.

El registro del 26 de septiembre indica que no se había identificado una
entidad de Home Assistant que mida el nivel de C3. No se volvió a consultar
Home Assistant para esta operación. Se conservan las lecturas manuales; no se
aportó telemetría ambiental pertinente para las horas de lectura PAR.

## Pendientes derivados

- [ ] Registrar la hora exacta y el mismo punto de referencia en futuras medidas de C3
- [ ] Repetir lecturas PAR en los mismos puntos y condiciones si se quiere comparar otro día o evaluar otra estación
- [ ] Registrar posición, profundidad y orientación del sensor para comparar las lecturas PAR con un mapa posterior de la AI Prime 16HD
- [ ] Comparar el DanoPlus con un instrumento subacuático de referencia si se necesita evaluar exactitud absoluta

## Fuentes internas

- [DanoPlus DP-414: especificaciones, calibración de cero y límites](../../../01_verilpedia/04_hardware/danoplus-dp-414/danoplus-dp-414.md)
- [Técnica de la urna: dimensiones de C3/Retorno](../../../01_verilpedia/04_hardware/urna/tecnica.md)
- [Reposición manual y lectura de salinidad del 26 de septiembre](2026-09-26-reposicion-manual-y-lectura-de-salinidad.md)
- [Operación del 23 de septiembre: estimación geométrica de Retorno](2026-09-23-pesaje-y-desplazamiento-del-hardscape.md)
- [Configuración de iluminación de Veril](../../../02_configuracion/01_dimensiones/04_iluminacion.md)
