#!/usr/bin/env python3
"""Build a base-on-bed Orca project from the validated FreeCAD STL export."""
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZIP_DEFLATED, ZipFile
import argparse
import json
import struct

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "tapa--kp3-winkle-petg.3mf"
STL = ROOT / "modelos" / "tapa-base-cama-6_5.stl"
OUTPUT = ROOT / "tapa-base-cama--kp3-winkle-petg.3mf"
MODEL_PATH = "3D/3dmodel.model"
SETTINGS_PATH = "Metadata/project_settings.config"
CORE = "http://schemas.microsoft.com/3dmanufacturing/core/2015/02"
ET.register_namespace("", CORE)
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--stl", type=Path, default=STL)
parser.add_argument("--output", type=Path, default=OUTPUT)
args = parser.parse_args()
STL = args.stl
OUTPUT = args.output

raw = STL.read_bytes()
if len(raw) < 84:
    raise SystemExit("STL incompleto")
count = struct.unpack_from("<I", raw, 80)[0]
if len(raw) != 84 + 50 * count:
    raise SystemExit("La exportación STL no tiene estructura binaria válida")

vertices = []
vertex_ids = {}
triangles = []
for i in range(count):
    offset = 84 + i * 50
    coords = struct.unpack_from("<12f", raw, offset)
    ids = []
    for j in range(3):
        point = tuple(round(float(v), 5) for v in coords[3 + 3 * j : 6 + 3 * j])
        if point not in vertex_ids:
            vertex_ids[point] = len(vertices)
            vertices.append(point)
        ids.append(vertex_ids[point])
    triangles.append(ids)

with ZipFile(SOURCE) as src:
    files = {name: src.read(name) for name in src.namelist()}

root = ET.fromstring(files[MODEL_PATH])
mesh = root.find(f".//{{{CORE}}}mesh")
if mesh is None:
    raise SystemExit("El proyecto de partida no contiene una malla")
vnode = mesh.find(f"{{{CORE}}}vertices")
tnode = mesh.find(f"{{{CORE}}}triangles")
for child in list(vnode):
    vnode.remove(child)
for child in list(tnode):
    tnode.remove(child)
for x, y, z in vertices:
    ET.SubElement(vnode, f"{{{CORE}}}vertex", {"x": str(x), "y": str(y), "z": str(z)})
for v1, v2, v3 in triangles:
    ET.SubElement(tnode, f"{{{CORE}}}triangle", {"v1": str(v1), "v2": str(v2), "v3": str(v3)})

obj = root.find(f".//{{{CORE}}}object")
if obj is not None:
    obj.set("name", "tapa-base-cama-6_5")
meta = root.find(f"{{{CORE}}}metadata[@name='Title']")
if meta is not None:
    meta.text = "Veril biobolas - tapa base en cama, abertura 6.5 mm"

# Put the already-normalized CAD mesh at the center of the 180 x 180 mm bed.
build_item = root.find(f".//{{{CORE}}}build/{{{CORE}}}item")
if build_item is None:
    raise SystemExit("No se encontró el elemento build")
build_item.set("transform", "1 0 0 0 1 0 0 0 1 90 90 0")
files[MODEL_PATH] = ET.tostring(root, encoding="utf-8", xml_declaration=True)

model_settings_path = "Metadata/model_settings.config"
model_settings = ET.fromstring(files[model_settings_path])
for node in model_settings.iter("metadata"):
    if node.get("key") in ("name", "plater_name"):
        node.set("value", "tapa-base-cama-6_5")
files[model_settings_path] = ET.tostring(
    model_settings, encoding="utf-8", xml_declaration=True
)

settings = json.loads(files[SETTINGS_PATH])
settings["enable_support"] = "0"
settings["support_type"] = "normal(auto)"
settings["print_settings_id"] = "Veril tapa base en cama 6.5 mm KP3 PETG candidato sin soportes"
files[SETTINGS_PATH] = json.dumps(settings, ensure_ascii=False, separators=(",", ":")).encode("utf-8")

with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as dst:
    for name, data in files.items():
        dst.writestr(name, data)

print(f"Creado: {OUTPUT}")
print(f"Facetas: {count}; vértices únicos: {len(vertices)}")
print(f"Envolvente STL: X {min(x for x,_,_ in vertices):.3f}..{max(x for x,_,_ in vertices):.3f}, Y {min(y for _,y,_ in vertices):.3f}..{max(y for _,y,_ in vertices):.3f}, Z {min(z for _,_,z in vertices):.3f}..{max(z for _,_,z in vertices):.3f} mm")
