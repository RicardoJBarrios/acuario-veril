# 11 de octubre de 2026 — Rotura de la tapa al retirar soportes

## Incidencia comunicada

El propietario comunicó que la impresión de la tapa del soporte de biobolas
acabó ese día. La retirada de los soportes resultó prácticamente imposible y la
pieza se rompió durante esa operación. No se indicó la zona de rotura, el
material y lote usados, ni se aportó una fotografía. Tampoco se confirmó qué
G-code se envió exactamente. El único laminado previo de la tapa conservado en
la entrega es [VBTAPA.GCO](../../../03_pendientes/disenos-3d/soporte-biobolas-impresion/VBTAPA.GCO),
con soportes normales snug en todas partes; se mantiene solo como trazabilidad y
no debe reutilizarse.

El propietario observó una abertura interior de **9 mm** en el gancho que recibe
el cristal. No se comunicó qué instrumento se usó para esa medida. Confirmó que
no pondrá almohadillas y fijó como objetivo una abertura de **6,5 mm** para el
vidrio nominal de 6 mm.

## Acción realizada tras la incidencia

Se conservó sin cambios el FCStd original y se creó el derivado paramétrico
[soporte-biobolas-tapa-fdm.FCStd](../../../03_pendientes/disenos-3d/soporte-biobolas-tapa-fdm.FCStd).
La variante usa 0 mm de almohadilla, 0,25 mm de holgura por cara y 3,2 mm de
pared exterior del gancho (antes 6 mm). Se alineó el borde inferior de las
cartelas con el plano de la base para imprimir esa zona apoyada en cama.

Se generó el proyecto de Orca [tapa-base-cama--kp3-winkle-petg.3mf](../../../03_pendientes/disenos-3d/soporte-biobolas-impresion/tapa-base-cama--kp3-winkle-petg.3mf),
el laminado [tapa-base-cama-laminado.3mf](../../../03_pendientes/disenos-3d/soporte-biobolas-impresion/laminados/tapa-base-cama/tapa-base-cama-laminado.3mf)
y el archivo [VBTAPB.GCO](../../../03_pendientes/disenos-3d/soporte-biobolas-impresion/VBTAPB.GCO),
con soportes desactivados. Orca estima **5 h 36 min 33 s y 60,66 g**. El
laminado conserva un puente de hasta unos 55 mm en la silla del cristal.

## Pendiente

La tapa nueva aún no se ha impreso. Deben comprobarse la calidad del puente, el
ajuste de 6,5 mm en el cristal desnudo y la resistencia de la tapa con la carga
real fuera del acuario. El resultado de la primera impresión no permite
atribuir la rotura a una zona concreta ni validar por sí solo el nuevo diseño.

La ficha y las decisiones del diseño permanecen en
[soporte-biobolas.md](../../../03_pendientes/disenos-3d/soporte-biobolas.md).
