#!/usr/bin/env python3
"""Añade soportes manuales solo bajo la silla, su pared exterior y el asa."""
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZIP_DEFLATED, ZipFile
import argparse
import json
import math

ROOT = Path(__file__).resolve().parent
CORE = "http://schemas.microsoft.com/3dmanufacturing/core/2015/02"
ET.register_namespace("", CORE)
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--source", type=Path, default=ROOT / "tapa-base-cama--kp3-winkle-petg.3mf")
parser.add_argument("--output", type=Path, default=ROOT / "tapa-soporte-local--kp3-winkle-petg.3mf")
args = parser.parse_args()
with ZipFile(args.source) as src:
    files = {name: src.read(name) for name in src.namelist()}

model = ET.fromstring(files["3D/3dmodel.model"])
vertices = [tuple(float(v.get(k)) for k in ("x", "y", "z"))
            for v in model.findall(f".//{{{CORE}}}vertex")]
selected = []
for index, triangle in enumerate(model.findall(f".//{{{CORE}}}triangle")):
    points = [vertices[int(triangle.get(k))] for k in ("v1", "v2", "v3")]
    a = [points[1][j] - points[0][j] for j in range(3)]
    b = [points[2][j] - points[0][j] for j in range(3)]
    normal = (a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0])
    length = math.sqrt(sum(v*v for v in normal))
    zs = [p[2] for p in points]
    # Exportación CAD normalizada: cara inferior del asa/pared a Z=53 y
    # de la silla a Z=65. No se pintan los cierres inferiores ni sus chaflanes.
    if length and normal[2]/length < -0.99 and min(zs) > 52.9 and max(zs)-min(zs) < 0.02:
        # Orca 2.4.2: estado ENFORCER=1, hoja sin subdividir => hexadecimal 4.
        # Fuente: src/libslic3r/{TriangleSelector.cpp,Model.cpp,Format/bbs_3mf.cpp}.
        triangle.set("paint_supports", "4")
        selected.append(index)
    else:
        triangle.attrib.pop("paint_supports", None)
if len(selected) != 24:
    raise SystemExit(f"La malla cambió: se esperaban 24 facetas de apoyo, se encontraron {len(selected)}; revisar la selección.")
for obj in model.findall(f".//{{{CORE}}}object"):
    obj.set("name", "tapa-soporte-local-6_5")
title = model.find(f"{{{CORE}}}metadata[@name='Title']")
if title is not None:
    title.text = "Veril tapa base en cama 6.5 mm, soportes localizados"
files["3D/3dmodel.model"] = ET.tostring(model, encoding="utf-8", xml_declaration=True)

model_settings = ET.fromstring(files["Metadata/model_settings.config"])
for node in model_settings.iter("metadata"):
    if node.get("key") in ("name", "plater_name"):
        node.set("value", "tapa-soporte-local-6_5")
files["Metadata/model_settings.config"] = ET.tostring(model_settings, encoding="utf-8", xml_declaration=True)

settings = json.loads(files["Metadata/project_settings.config"])
settings.update({
    "enable_support": "1",
    "support_type": "normal(manual)",
    "support_style": "snug",
    "support_on_build_plate_only": "0",
    "bridge_no_support": "0",
    "support_top_z_distance": "0.3",
    "support_bottom_z_distance": "0.3",
    "support_object_xy_distance": "0.5",
    "support_interface_top_layers": "2",
    "support_interface_bottom_layers": "2",
    "support_interface_spacing": "0.6",
    "support_bottom_interface_spacing": "0.6",
    "support_base_pattern_spacing": "4",
    "support_speed": "40",
    "support_interface_speed": "30",
    "print_settings_id": "Veril tapa base en cama 6.5 mm KP3 PETG soporte localizado normal",
})
files["Metadata/project_settings.config"] = json.dumps(settings, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
with ZipFile(args.output, "w", ZIP_DEFLATED) as dst:
    for name, data in files.items():
        dst.writestr(name, data)
print(f"Creado: {args.output}; facetas con soporte manual: {len(selected)}")
