# Hanna HI736 Marine Phosphorus ULR Checker

El **HI736** es un fotómetro de Hanna Instruments para agua salada. El
ensayo colorimétrico con ácido ascórbico informa el resultado como fósforo
(P) en ppb. Para comparar con objetivos expresados como fosfato (PO₄), se
convierte la lectura a ppm de PO₄. La referencia del modelo es **HI736**.

## Identificación y estado

| Campo | Dato |
| --- | --- |
| Fabricante y modelo | Hanna Instruments HI736 Checker HC |
| Método | Colorimetría con ácido ascórbico y LED de 525 nm |
| Muestra | 10 mL de agua salada |
| Equipo | Dos cubetas con tapa, pila AAA y reactivos de inicio para seis pruebas según el manual |
| Reactivos y control | Recambio HI736-25 para 25 pruebas y kit de patrones certificados HI736-11 |
| Encaje en Veril | Referencia prioritaria para seguimiento de fosfato bajo |

## Rango, resolución y exactitud declarada

| Magnitud | Lectura como P | Equivalencia como PO₄ |
| --- | ---: | ---: |
| Rango | 0–200 ppb | 0–0,613 ppm |
| Resolución | 1 ppb | ≈0,0031 ppm |
| Exactitud a 25 °C | ±5 ppb ±5 % de la lectura | ±0,0153 ppm ±5 % de la lectura |

**ppm de PO₄ = ppb de P × 3,066 ÷ 1000**. El factor 3,066 es la razón
entre las masas molares del fosfato y del fósforo. La división por 1000
convierte de ppb a ppm. Por ejemplo, **10 ppb de P ≈ 0,031 ppm de PO₄**.
Conservar la lectura original junto al valor convertido permite revisar
el cálculo y evita confundir las unidades.

Frente al [HI774](../21_hanna-hi774/hanna-hi774.md), el HI736 ofrece una
resolución más fina y un término fijo de exactitud declarado algo menor
en unidades de PO₄. El HI774 lee directamente en ppm de PO₄ y llega a
0,90 ppm. La resolución de pantalla no indica por sí sola la repetibilidad
ni la exactitud que se obtendrá con una muestra real.

## Procedimiento resumido del fabricante

1. Cargar 10 mL de muestra sin partículas, tapar y hacer el cero con la
   cubeta limpia y seca por fuera.
2. Añadir el reactivo correspondiente al formato del kit. El manual
   admite el sobre HI736-0 o la combinación de indicador HI736IND-0 y
   polvo sulfámico que Hanna describe para el formato de dos sobres.
3. Agitar suavemente durante **2 minutos** hasta disolver el polvo.
   Retirar las burbujas, limpiar la cubeta y volver a colocarla.
4. Mantener pulsado el botón para iniciar la cuenta atrás de **3 minutos**.
   Registrar la lectura en ppb de P y convertirla si se necesita compararla
   con valores en ppm de PO₄. Desechar la muestra reaccionada y limpiar la cubeta.

## Encaje previsto en Veril

El [plan de medición](../../../03_pendientes/operacion-recurrente/02_medicion-y-tests.md)
prioriza el HI736 para seguir fosfato bajo durante la maduración. El HI774
queda como alternativa si interesa leer directamente en ppm de PO₄ o medir
por encima de 0,613 ppm. El HI736 permite hacer mediciones puntuales del
acuario y comparar muestras como el agua del remojo de roca. La prioridad
documental no acredita una compra.

## Buenas prácticas, límites y debilidades

- Usar la misma cubeta para el cero y la lectura. Partículas, huellas,
  gotas por fuera y burbujas pueden alterar el paso de luz.
- Mantener los reactivos secos y dentro de su caducidad. Respetar la
  disolución y el tiempo de reacción en cada medida.
- El resultado corresponde al fosfato reactivo expresado como P.
  La conversión a PO₄ no representa fósforo total ni la reserva adsorbida.
- El kit certificado HI736-11 comprueba la respuesta del instrumento.
  La preparación de la muestra y el estado del reactivo siguen influyendo
  en la lectura.
- Un cero parpadeante indica que la muestra absorbe menos que la referencia.
  Revisar la preparación y repetir. Un máximo parpadeante indica fuera de
  rango. Revisar la muestra y seguir el procedimiento del fabricante.
- Al comparar aguas, aplicar el mismo procedimiento y repetir las lecturas
  dudosas. Una diferencia de unas pocas milésimas de ppm requiere más
  evidencia que una lectura aislada de cada muestra.

## Enlaces de trabajo

- [Fosfato en Verilpedia](../../03_parametros/fosfato.md)
- [Salifert Phosphate Profi Test](../16_salifert-phosphate/salifert-phosphate.md)
- [Plan de medición y criterios de calidad](../../../03_pendientes/operacion-recurrente/02_medicion-y-tests.md#criterios-de-calidad-de-medida)

## Fuentes

- [Manual de Hanna para HI736](https://www.documentation.hannainst.com/manuals/download/7604)
- [Comparativa oficial de Checkers de fósforo y fosfato](https://pages.hannainst.com/hubfs/PDF/Aquarium/Phosphate-Checker-Comparison-V1.pdf)
