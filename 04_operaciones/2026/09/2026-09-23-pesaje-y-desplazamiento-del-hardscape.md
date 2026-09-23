# 2026-09-23 — Pesaje y medición del desplazamiento del hardscape

## Estado

Operación documentada a partir de medidas físicas comunicadas por el propietario. El cálculo por tramos es geométrico. El propietario confirma que el nivel de Entrada también descendió 12 mm al retirar la roca. El nivel de Retorno a 75 mm bajo el borde es un objetivo para una futura operación con ATO, no una medida ya ejecutada.

## Ejecución observada

Se retiró toda la roca del display. Al retirarla, el nivel del agua del display
bajó **12 mm**. Las piezas se pesaron fuera del display:

| Elemento descrito por el propietario | Masa comunicada |
| --- | ---: |
| Isla pequeña de la esquina trasera izquierda | 150 g, comunicado |
| Isla de la esquina frontal izquierda, con zoas | 250 g, comunicado |
| Estructura principal | Aproximadamente 7 kg, comunicado |
| **Suma aritmética de los valores comunicados** | **Aproximadamente 7,4 kg** |

El propietario comunica también que la roca que no se utilizó en el hardscape
pesa **aproximadamente 2,5 kg**. Se trata de material no instalado, separado
del conjunto pesado para el display. No consta la fecha concreta de ese pesaje.

Como referencia nominal sencilla para la masa total de roca de Veril se adopta
**unos 7,5 kg**. Es un redondeo orientativo de las masas comunicadas, no un
repesaje de precisión ni una conversión a volumen.

Después se devolvió la roca al display y, tras reponer agua evaporada en una
cantidad no medida, el nivel volvió a quedar a **37 mm del borde superior**.
No se midió la cantidad de agua añadida.

Al retirar la roca, también bajó **12 mm** el nivel de la cámara **Entrada**,
confirmado posteriormente por el propietario. El nivel de la cámara **Skimmer**
no bajó: su superficie quedó aproximadamente **50 mm
por debajo del borde**, en el escalón hacia Retorno.

## Geometría y volumen bruto

Se utilizan las dimensiones interiores comunicadas para cada tramo. Desde la
cara superior del fondo hasta el borde hay aproximadamente **390 mm**. Por
tanto, el nivel del display y Entrada a 37 mm bajo el borde corresponde a una
columna de **353 mm**; el nivel de Skimmer a 50 mm bajo el borde corresponde
a **340 mm**. Se incluye el paso rectangular sumergido entre Entrada y
Skimmer, de **139 × 6 × 50 mm**. Se omite el orificio circular de entrada
Display–Entrada, tal como se acordó, porque no se ha medido su volumen con
precisión.

| Tramo | Dimensiones usadas | Altura de agua | Volumen geométrico |
| --- | ---: | ---: | ---: |
| Display | 594 × 308 mm | 353 mm | 64,582 L |
| Entrada | 139 × 86 mm | 353 mm | 4,220 L |
| Skimmer | 139 × 134 mm | 340 mm | 6,333 L |
| Paso inferior Entrada–Skimmer | 139 × 6 × 50 mm | incluido | 0,042 L |
| **Total bruto** |  |  | **75,176 L** |

Este subtotal no incluye la cámara Retorno. Es volumen geométrico hasta los
niveles indicados, antes de restar los objetos sumergidos.

## Skimmer sumergido

La envolvente sumergida comunicada para el Sicce Shark 300 es de **81 × 110 ×
151 mm**:

```text
Volumen de la envolvente = 81 × 110 × 151 = 1.345.410 mm³ ≈ 1,345 L
```

Se usa como prisma envolvente para esta estimación. No equivale a una medición
del volumen sólido exacto del skimmer, cuya forma puede dejar espacios dentro
de esa caja. Al no cambiar el nivel de Skimmer durante la retirada de la roca,
esta envolvente se descuenta del volumen actual, pero no de la variación de
nivel atribuida a la roca.

## Desplazamiento inferido de la roca

El descenso comunicado y confirmado fue **12 mm tanto en el display como en
Entrada**. Skimmer no bajó. Se suman únicamente las superficies que cambiaron
de nivel: Display y Entrada.

```text
Área Display = 594 × 308 = 182.952 mm²
Área Entrada = 139 × 86 = 11.954 mm²
Volumen inferido = (182.952 + 11.954) × 12
                 = 2.338.872 mm³ ≈ 2,339 L
```

El paso rectangular Entrada–Skimmer permanece sumergido y no cambia de
volumen entre las dos lecturas. El orificio circular Display–Entrada se omite
por falta de una medida geométrica exacta. El peso de la roca no se convierte
a volumen: las **tres masas comunicadas suman 7,4 kg**, pero no se conoce la
densidad efectiva del material.

No se registraron el estado del retorno ni las cotas exactas de cada cámara y
Retorno antes y después. Tampoco quedó acotado si la reposición de agua
evaporada ocurrió antes o después de la lectura de 12 mm. Por ello, el cálculo
representa el desplazamiento de roca solo bajo la condición de que durante esa
comparación no hubiera una transferencia neta de agua hacia o desde Retorno ni
una reposición.

## Estimación geométrica incluyendo Retorno

Para estimar un estado operativo futuro, se toma como objetivo que Retorno
quede a **75 mm bajo el borde superior**, con ATO. Es una hipótesis de cálculo
indicada por el propietario, no un nivel ya ajustado o medido. Con una altura
interior aproximada de 390 mm, la columna resultante sería de 315 mm. La cámara
Retorno tiene una huella interior de 139 × 77 mm:

```text
Volumen geométrico de Retorno = 139 × 77 × 315 / 1.000.000
                              = 3,371445 L
```

La bomba Sicce Micra Plus 600 está destinada a esta cámara. La ficha técnica
publica dimensiones aproximadas de 52 × 43 × 57 mm: su prisma envolvente sería
0,127452 L. Se descuenta como una **cota superior aproximada** de lo que puede
ocupar la bomba; no es su volumen sólido real, ya que la carcasa y sus huecos
no llenan necesariamente ese prisma. La bomba tiene que estar sumergida para
funcionar, pero no se midió su desplazamiento por inmersión.

La salida documentada admite tubo flexible de 12 × 16 mm (diámetro interior ×
exterior). El volumen de material de la pared del tubo es aproximadamente
0,088 L por metro sumergido, calculado como cilindro anular. No se conoce la
longitud sumergida de la salida instalada en Retorno, por lo que no se descuenta
un total inventado. El lumen del tubo contiene agua del sistema y no se cuenta
como volumen desplazado. El tubo Eheim auxiliar de 16/22 mm no se atribuye a
esta salida: está documentado como material auxiliar, no como recorrido
permanente del retorno.

Sumando el volumen geométrico de Retorno al subtotal bruto anterior, Display +
Entrada + Skimmer + paso + Retorno dan **78,548 L**. Restando la envolvente del
skimmer, el desplazamiento inferido de la roca y la envolvente superior de la
Micra, quedan **74,736 L**. Este valor aún no descuenta la pared del tramo de
tubo sumergido ni otros elementos alojados en el agua; además hereda las
condiciones e incertidumbres de las mediciones anteriores. Por ello es una
estimación de trabajo, no el volumen neto definitivo del sistema.

## Referencias prácticas para dosificación

Como convención nominal vigente y simplificada para Veril, se utilizarán
**75 L para el sistema completo** y **60 L para el display con arena** en
referencias y cálculos. El cálculo detallado disponible para el display es
61,69 L bajo la hipótesis de 2 cm de arena y 2 cm de margen superior; se usa
60 L como redondeo, no como nueva medición. Los 75 L son también un nominal
redondeado: la estimación de cámaras previa a descontar la pared sumergida del
tubo y otros elementos es 74,736 L, y el nivel de Retorno a 75 mm es todavía
un objetivo futuro. La arena y los elementos no cuantificados añaden
incertidumbre.

Estas cifras son la base nominal a utilizar por defecto en Veril. Siguen siendo
aproximaciones documentales, no una medición exacta del agua neta; la
convención solo se cambiará si el propietario decide adoptar otra base.

## Estimación parcial de agua

En los tres tramos Display, Entrada y Skimmer, restando del volumen bruto la
envolvente del skimmer y el desplazamiento inferido de la roca:

```text
75,176 − 1,345 − 2,339 ≈ 71,492 L
```

Es una estimación del agua en Display, Entrada y Skimmer bajo las condiciones
anteriores, no el volumen operativo total del acuario. No incluye Retorno ni
descuenta otros equipos o sustrato.

## Resultado y límites

- Masa orientativa nominal de la roca de Veril: **unos 7,5 kg**.
- Suma aritmética de las tres masas comunicadas: **aproximadamente 7,4 kg**; la estructura principal se dio como unos 7 kg.
- Masa comunicada de la roca no utilizada y no instalada: **aproximadamente 2,5 kg**; fecha del pesaje no especificada.
- Volumen geométrico bruto de Display + Entrada + Skimmer + paso inferior: **75,176 L** hasta los niveles comunicados.
- Envolvente rectangular sumergida del skimmer: **1,345 L**, aproximada.
- Desplazamiento inferido de la roca: **2,339 L**, calculado con el descenso confirmado de 12 mm en display y Entrada; depende de que no hubiera intercambio neto con Retorno ni reposición durante la comparación.
- Agua estimada en Display, Entrada y Skimmer tras descontar solo skimmer y roca: **71,492 L**, incompleta.
- Volumen geométrico de Retorno al nivel objetivo (75 mm bajo el borde): **3,371 L**; el nivel es previsto, aún no medido en operación con ATO.
- Envolvente de la Micra Plus: **0,127 L** como máximo geométrico aproximado, no desplazamiento sólido medido.
- Estimación conjunta tras descontar roca, skimmer y envolvente de bomba: **74,736 L**, antes de descontar el tubo sumergido y otros elementos; no es el volumen neto final.
- Tras devolver la roca y reponer agua evaporada (cantidad desconocida), el
  nivel observado quedó a **37 mm del borde**.
- La cámara Skimmer quedó a **50 mm del borde** y su nivel no varió al retirar
  la roca.
- La salida de la Micra Plus está documentada para tubo de 12 × 16 mm. Cada
  metro de pared sumergida representa aproximadamente 0,088 L; falta medir la
  longitud sumergida instalada.
- La reposición no permite calcular el agua evaporada.
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
