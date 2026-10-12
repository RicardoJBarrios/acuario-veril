"""Construcción inicial revisada para ejecutar en el hilo GUI de FreeCAD.

Parte del FCStd que ya contiene C1 y las dos matrices de bolas, importados
del original con sus dependencias. No lamina ni acciona una impresora.
"""
import math
import FreeCAD as App
import FreeCADGui as Gui
import Part
import Sketcher

doc = App.getDocument("SoporteBiobolasBastidor")
if doc.getObject("BastidorParameters"):
    raise RuntimeError("El bastidor ya existe: editar sus parámetros, no recrearlo")

parameters = doc.addObject("Spreadsheet::Sheet", "BastidorParameters")
parameters.Label = "Bastidor — parámetros candidatos (mm)"
rows = [
    ("outerWidth", "81 mm"),
    ("frameWidth", "6 mm"),
    ("frameHeight", "6 mm"),
    ("seatHeight", "3 mm"),
    ("ribWidth", "3 mm"),
    ("columnPitch", "36.5 mm"),
    ("modulePitch", "150 mm"),
    ("panelWidth", "75 mm"),
    ("panelHeight", "=modulePitch - seatHeight"),
    ("panelThickness", "3 mm"),
    ("panelRailWidth", "6 mm"),
    ("diagonalWidth", "6 mm"),
    ("upperFrameHeight", "3 mm"),
    ("baseZ", "25 mm"),
    ("centerX", "29 mm"),
    ("centerY", "0 mm"),
    ("mastLength", "145 mm"),
    ("mastEnvelope", "8.5 mm"),
    ("mastArmThickness", "2 mm"),
    ("gridHalfSpan", "=outerWidth / 2 - frameWidth + 0.1 mm"),
    ("diagonalRun", "=panelWidth - panelRailWidth"),
    ("diagonalRise", "=panelHeight - panelRailWidth"),
    ("diagOffsetX", "=diagonalWidth / 2 * diagonalRise / sqrt(diagonalRun ^ 2 + diagonalRise ^ 2)"),
    ("diagOffsetY", "=diagonalWidth / 2 * diagonalRun / sqrt(diagonalRun ^ 2 + diagonalRise ^ 2)"),
]
parameters.set("A1", "Parámetro")
parameters.set("B1", "Valor")
for number, (alias, value) in enumerate(rows, 2):
    parameters.set("A" + str(number), alias)
    parameters.set("B" + str(number), value if value.startswith("=") else "=" + value)
    parameters.setAlias("B" + str(number), alias)
parameters.setColumnWidth("A", 190)
parameters.setColumnWidth("B", 170)
doc.recompute()

masters = doc.addObject("App::DocumentObjectGroup", "PrintableMasters")
masters.Label = "Piezas maestras — orientación de fabricación"


def p(alias):
    return float(getattr(parameters, alias).Value)


def expression(alias):
    return "BastidorParameters." + alias


def coordinate_sketch(body, name, polygons, z=0.0, z_expression=None):
    """Vértices dimensionados y aristas coincidentes, sin referencias a caras."""
    sketch = doc.addObject("Sketcher::SketchObject", name)
    body.addObject(sketch)
    sketch.Placement.Base.z = z
    if z_expression:
        sketch.setExpression("Placement.Base.z", z_expression)
    for polygon in polygons:
        indices = []
        for a, b in zip(polygon, polygon[1:] + polygon[:1]):
            indices.append(sketch.addGeometry(Part.LineSegment(
                App.Vector(a[0], a[1], 0), App.Vector(b[0], b[1], 0)), False))
        for vertex, i in zip(polygon, indices):
            nxt = indices[(indices.index(i) + 1) % len(indices)]
            sketch.addConstraint(Sketcher.Constraint("Coincident", i, 2, nxt, 1))
            for axis, value, expr, line in [
                ("X", vertex[0], vertex[2], -2),
                ("Y", vertex[1], vertex[3], -1),
            ]:
                if abs(value) < 1e-9:
                    sketch.addConstraint(Sketcher.Constraint("PointOnObject", i, 1, line))
                else:
                    ci = sketch.addConstraint(Sketcher.Constraint("Distance" + axis, i, 1, value))
                    sketch.renameConstraint(ci, "V" + str(i) + axis)
                    if expr:
                        sketch.setExpression("Constraints[" + str(ci) + "]", expr)
    return sketch


def rectangle(x0, y0, x1, y1, ex0, ey0, ex1, ey1):
    return [(x0, y0, ex0, ey0), (x1, y0, ex1, ey0),
            (x1, y1, ex1, ey1), (x0, y1, ex0, ey1)]


def extrude(body, sketch, name, length, length_expr, pocket=False):
    feature = body.newObject("PartDesign::Pocket" if pocket else "PartDesign::Pad", name)
    feature.Profile = sketch
    feature.Length = length
    feature.setExpression("Length", length_expr)
    feature.Refine = True
    doc.recompute()
    sketch.Visibility = False
    for other in body.Group:
        if other != feature:
            other.Visibility = False
    if feature.Shape.isNull() or not feature.Shape.isValid() or len(feature.Shape.Solids) != 1:
        raise RuntimeError("Operación inválida: " + feature.Name)
    return feature


W = p("outerWidth")
F = p("frameWidth")
Q = expression("outerWidth") + " / 2"
INNER = Q + " - " + expression("frameWidth")
outer = rectangle(-W/2, -W/2, W/2, W/2, "-("+Q+")", "-("+Q+")", Q, Q)
inner = rectangle(-W/2+F, -W/2+F, W/2-F, W/2-F,
                  "-("+INNER+")", "-("+INNER+")", INNER, INNER)

base = doc.addObject("PartDesign::Body", "BaseWithGuides")
base.Label = "Base reforzada y mástiles — candidata"
masters.addObject(base)
base_sk = coordinate_sketch(base, "BasePerimeterProfile", [outer, inner])
extrude(base, base_sk, "BasePerimeterPad", p("frameHeight"), expression("frameHeight"))

for axis in ["X", "Y"]:
    for sign in [-1, 1]:
        center = sign*p("columnPitch")/2
        center_expr = ("-" if sign < 0 else "") + expression("columnPitch") + " / 2"
        low = "("+center_expr+") - " + expression("ribWidth") + " / 2"
        high = "("+center_expr+") + " + expression("ribWidth") + " / 2"
        span = p("gridHalfSpan")
        if axis == "X":
            poly = rectangle(center-p("ribWidth")/2, -span, center+p("ribWidth")/2, span,
                             low, "-"+expression("gridHalfSpan"), high, expression("gridHalfSpan"))
        else:
            poly = rectangle(-span, center-p("ribWidth")/2, span, center+p("ribWidth")/2,
                             "-"+expression("gridHalfSpan"), low, expression("gridHalfSpan"), high)
        suffix = axis + ("Neg" if sign < 0 else "Pos")
        sketch = coordinate_sketch(base, "SeatRibProfile"+suffix, [poly])
        extrude(base, sketch, "SeatRibPad"+suffix, p("seatHeight"), expression("seatHeight"))


def side_seats():
    s = p("outerWidth")/2-p("frameWidth")
    h = p("outerWidth")/2
    t = p("panelThickness")
    es = expression("outerWidth") + " / 2 - " + expression("frameWidth")
    eh = expression("outerWidth") + " / 2"
    et = expression("panelThickness")
    return [
        rectangle(-s, -h, s, -h+t, "-("+es+")", "-("+eh+")", es, "-("+eh+")+"+et),
        rectangle(-s, h-t, s, h, "-("+es+")", eh+"-"+et, es, eh),
        rectangle(-h, -s, -h+t, s, "-("+eh+")", "-("+es+")", "-("+eh+")+"+et, es),
        rectangle(h-t, -s, h, s, eh+"-"+et, "-("+es+")", eh, es),
    ]


seat_sk = coordinate_sketch(base, "PanelSeatsBaseProfile", side_seats(),
                            p("frameHeight"), expression("frameHeight"))
extrude(base, seat_sk, "PanelSeatsBasePocket", p("frameHeight")-p("seatHeight"),
        expression("frameHeight")+"-"+expression("seatHeight"), True)

# Mástiles conservados: brazos cruzados, Ø de referencia aún sin compensar.
for sx in [-1, 1]:
    for sy in [-1, 1]:
        cx, cy = sx*p("columnPitch")/2, sy*p("columnPitch")/2
        ex = ("-" if sx < 0 else "") + expression("columnPitch") + " / 2"
        ey = ("-" if sy < 0 else "") + expression("columnPitch") + " / 2"
        for axis in ["X", "Y"]:
            ax = p("mastEnvelope")/2 if axis == "X" else p("mastArmThickness")/2
            ay = p("mastArmThickness")/2 if axis == "X" else p("mastEnvelope")/2
            eax = expression("mastEnvelope" if axis == "X" else "mastArmThickness")+" / 2"
            eay = expression("mastArmThickness" if axis == "X" else "mastEnvelope")+" / 2"
            poly = rectangle(cx-ax, cy-ay, cx+ax, cy+ay,
                "("+ex+")-("+eax+")", "("+ey+")-("+eay+")",
                "("+ex+")+("+eax+")", "("+ey+")+("+eay+")")
            suffix = ("N" if sx < 0 else "P")+("N" if sy < 0 else "P")+axis
            sketch = coordinate_sketch(base, "MastProfile"+suffix, [poly],
                                       p("seatHeight")-.2, expression("seatHeight")+" - 0.2 mm")
            extrude(base, sketch, "MastPad"+suffix, p("mastLength")+.2,
                    expression("mastLength")+" + 0.2 mm")

# Holgura local de 0,2 mm alrededor de los cuatro pies del hotel existente.
# Se conservan 2,6 mm de nervio en estos pequeños tramos; no se altera el asiento.
hotel_reliefs = []
for sign in [-1, 1]:
    lo, hi = (16.55, 17.15) if sign > 0 else (-17.15, -16.55)
    hotel_reliefs.append(rectangle(lo, -1.8, hi, 1.8, None, None, None, None))
    hotel_reliefs.append(rectangle(-1.8, lo, 1.8, hi, None, None, None, None))
sk = coordinate_sketch(base, "HotelFeetReliefProfile", hotel_reliefs,
                       p("seatHeight"), expression("seatHeight"))
extrude(base, sk, "HotelFeetReliefPocket", p("seatHeight"), expression("seatHeight"), True)

panel = doc.addObject("PartDesign::Body", "SidePanel")
panel.Label = "Panel triangulado — impresión acostada"
masters.addObject(panel)
w, h, r = p("panelWidth"), p("panelHeight"), p("panelRailWidth")
ew, eh, er = expression("panelWidth"), expression("panelHeight"), expression("panelRailWidth")
frame_outer = rectangle(-w/2, 0, w/2, h, "-"+ew+" / 2", None, ew+" / 2", eh)
frame_inner = rectangle(-w/2+r, r, w/2-r, h-r,
    "-"+ew+" / 2 + "+er, er, ew+" / 2 - "+er, eh+"-"+er)
sk = coordinate_sketch(panel, "PanelFrameProfile", [frame_outer, frame_inner])
extrude(panel, sk, "PanelFramePad", p("panelThickness"), expression("panelThickness"))
dx, dy = p("diagOffsetX"), p("diagOffsetY")
a, b = -w/2+r/2, r/2
c, e = w/2-r/2, h-r/2
ea, eb = "-"+ew+" / 2 + "+er+" / 2", er+" / 2"
ec, ee = ew+" / 2 - "+er+" / 2", eh+" - "+er+" / 2"
ox, oy = expression("diagOffsetX"), expression("diagOffsetY")
diag = [(a-dx, b+dy, ea+"-"+ox, eb+"+"+oy),
        (c-dx, e+dy, ec+"-"+ox, ee+"+"+oy),
        (c+dx, e-dy, ec+"+"+ox, ee+"-"+oy),
        (a+dx, b-dy, ea+"+"+ox, eb+"-"+oy)]
sk = coordinate_sketch(panel, "PanelDiagonalProfile", [diag])
extrude(panel, sk, "PanelDiagonalPad", p("panelThickness"), expression("panelThickness"))

# Rebajes en extremos: dejan los bloques de esquina de los marcos conectados.
notches = []
for sign in [-1, 1]:
    x0, x1 = (-w/2, -w/2+r/2) if sign < 0 else (w/2-r/2, w/2)
    ex0, ex1 = (("-"+ew+" / 2", "-"+ew+" / 2 + "+er+" / 2") if sign < 0
                 else (ew+" / 2 - "+er+" / 2", ew+" / 2"))
    notches.append(rectangle(x0, 0, x1, p("frameHeight")-p("seatHeight"),
        ex0, None, ex1, expression("frameHeight")+"-"+expression("seatHeight")))
    notches.append(rectangle(x0, h-p("upperFrameHeight"), x1, h,
        ex0, eh+"-"+expression("upperFrameHeight"), ex1, eh))
sk = coordinate_sketch(panel, "PanelCornerReliefProfile", notches,
                       p("panelThickness"), expression("panelThickness"))
extrude(panel, sk, "PanelCornerReliefPocket", p("panelThickness"), expression("panelThickness"), True)

ring = doc.addObject("PartDesign::Body", "UpperFrame")
ring.Label = "Marco superior — alojamientos de panel, bloqueo pendiente"
masters.addObject(ring)
sk = coordinate_sketch(ring, "UpperFrameProfile", [outer, inner])
extrude(ring, sk, "UpperFramePad", p("upperFrameHeight"), expression("upperFrameHeight"))
sk = coordinate_sketch(ring, "UpperPanelSeatsProfile", side_seats(),
                       p("upperFrameHeight"), expression("upperFrameHeight"))
extrude(ring, sk, "UpperPanelSeatsPocket", p("upperFrameHeight"), expression("upperFrameHeight"), True)

base.ViewObject.ShapeColor = (0.12, .40, .82)
ring.ViewObject.ShapeColor = (0.12, .40, .82)
panel.ViewObject.ShapeColor = (1.0, .48, .10)


def instance(part, source, name, placement):
    link = doc.addObject("App::Link", name)
    link.setLink(source)
    part.addObject(link)
    link.Placement = placement
    link.Visibility = True
    return link


for module_index in [0, 1]:
    assembly = doc.addObject("App::Part", "Module"+str(module_index+1))
    assembly.Label = "Módulo "+str(module_index+1)+" — mismo juego de piezas"
    assembly.Placement.Base = App.Vector(p("centerX"), p("centerY"),
                                         p("baseZ") + module_index*p("modulePitch"))
    assembly.setExpression("Placement.Base.x", expression("centerX"))
    assembly.setExpression("Placement.Base.y", expression("centerY"))
    assembly.setExpression("Placement.Base.z", expression("baseZ") +
                           (" + "+expression("modulePitch") if module_index else ""))
    instance(assembly, base, "BaseModule"+str(module_index+1), App.Placement())
    top = instance(assembly, ring, "TopModule"+str(module_index+1),
        App.Placement(App.Vector(0, 0, p("modulePitch")-p("upperFrameHeight")), App.Rotation()))
    top.setExpression("Placement.Base.z", expression("modulePitch")+"-"+expression("upperFrameHeight"))
    for side in range(4):
        rotation = App.Rotation(App.Vector(0,0,1), side*90)
        position = rotation.multVec(App.Vector(0, -p("outerWidth")/2+p("panelThickness"), p("seatHeight")))
        inst = instance(assembly, panel, "PanelM"+str(module_index+1)+"S"+str(side+1),
            App.Placement(position, rotation.multiply(App.Rotation(App.Vector(1,0,0),90))))
        inst.setExpression("Placement.Base.z", expression("seatHeight"))
        if side == 0:
            inst.setExpression("Placement.Base.y", "-"+expression("outerWidth")+" / 2 + "+expression("panelThickness"))
        elif side == 1:
            inst.setExpression("Placement.Base.x", expression("outerWidth")+" / 2 - "+expression("panelThickness"))
        elif side == 2:
            inst.setExpression("Placement.Base.y", expression("outerWidth")+" / 2 - "+expression("panelThickness"))
        else:
            inst.setExpression("Placement.Base.x", "-"+expression("outerWidth")+" / 2 + "+expression("panelThickness"))

for body in [base, panel, ring]:
    body.Visibility = False
doc.getObject("Body").Visibility = False
doc.getObject("Body").ViewObject.ShapeColor = (.84,.81,.70)
doc.getObject("C1NivelAgua").ViewObject.Transparency = 92
doc.recompute()
Gui.activeDocument().activeView().viewAxonometric()
Gui.activeDocument().activeView().fitAll()
doc.save()
print("CAD_INICIAL_GUARDADO", doc.FileName)
print("SOLIDOS_MAESTROS", [(o.Name,len(o.Shape.Solids),o.Shape.isValid()) for o in [base,panel,ring]])
print("SKETCHES", [(o.Name,o.FullyConstrained) for o in doc.Objects if o.TypeId == "Sketcher::SketchObject"])
