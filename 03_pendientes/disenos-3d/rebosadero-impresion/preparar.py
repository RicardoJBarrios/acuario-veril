"""Create standalone Orca projects from exported CAD meshes and an identified recipe."""
from pathlib import Path
import hashlib, json, zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent / 'soporte-biobolas-impresion/probeta-cristal-ajuste--kp3-winkle-petg.3mf'
NS = 'http://schemas.microsoft.com/3dmanufacturing/core/2015/02'
ET.register_namespace('', NS)

def q(name):
    return '{'+NS+'}'+name

with zipfile.ZipFile(BASE) as source:
    original_config = json.loads(source.read('Metadata/project_settings.config'))
    packaging = {name: source.read(name) for name in ['[Content_Types].xml', '_rels/.rels']}

items = json.loads((ROOT / 'modelos/geometria.json').read_text())
manifest = []
for item in items:
    slug = item['slug']
    cfg = dict(original_config)
    for key in list(cfg):
        if any(word in key.lower() for word in ['printhost', 'print_host', 'api_key', 'password', 'access_token']) or key == 'host_type':
            del cfg[key]
    cfg.update({
        'print_settings_id': 'Veril rebosadero '+slug+' KP3 PETG',
        'enable_support': '0', 'wall_loops': '5',
        'sparse_infill_pattern': 'gyroid',
        'sparse_infill_density': '100%' if slug == 'placa-20mm' else '30%',
        'brim_type': 'outer_only', 'brim_width': '5' if slug == 'estructura' else '3',
        'brim_object_gap': '0.1', 'raft_layers': '0',
    })
    if slug == 'estructura':
        cfg['machine_end_gcode'] = ('G91 ; relative positioning\nG1 E-1 F2100\n'
            'G90 ; absolute positioning\nG1 Z179.2 F1200 ; bounded final clearance below 180 mm\n'
            'G1 X0 Y179 F3000\nM104 S0 ; turn off hotend\nM140 S0 ; turn off bed\n'
            'M107 ; turn off fan\nM84 ; disable motors')
    model = ET.Element(q('model'), {'unit':'millimeter','{http://www.w3.org/XML/1998/namespace}lang':'es-ES'})
    for name, value in [('Application','OrcaSlicer-2.4.2'),('OrcaSlicer','2.4.2'),('BambuStudio:3mfVersion','1'),('Title','Veril rebosadero — '+slug)]:
        ET.SubElement(model,q('metadata'),{'name':name}).text=value
    resources=ET.SubElement(model,q('resources'))
    obj=ET.SubElement(resources,q('object'),{'id':'1','type':'model','name':slug})
    mesh=ET.SubElement(obj,q('mesh'))
    vertices=ET.SubElement(mesh,q('vertices'))
    for v in item['vertices']:
        ET.SubElement(vertices,q('vertex'),dict(zip(['x','y','z'],[f'{x:.9f}' for x in v])))
    triangles=ET.SubElement(mesh,q('triangles'))
    for t in item['triangles']:
        ET.SubElement(triangles,q('triangle'),dict(zip(['v1','v2','v3'],map(str,t))))
    size=item['dimensions_mm']
    build=ET.SubElement(model,q('build'))
    ET.SubElement(build,q('item'),{'objectid':'1','transform':f'1 0 0 0 1 0 0 0 1 {90-size[0]/2:.9f} {90-size[1]/2:.9f} 0'})
    settings=ET.Element('config')
    obj=ET.SubElement(settings,'object',{'id':'1'})
    for key,value in [('name',slug),('extruder','1')]: ET.SubElement(obj,'metadata',{'key':key,'value':value})
    part=ET.SubElement(obj,'part',{'id':'1','subtype':'normal_part'})
    for key,value in [('name',slug),('extruder','1')]: ET.SubElement(part,'metadata',{'key':key,'value':value})
    plate=ET.SubElement(settings,'plate')
    for key,value in [('plater_id','1'),('plater_name',slug),('locked','false')]: ET.SubElement(plate,'metadata',{'key':key,'value':value})
    inst=ET.SubElement(plate,'model_instance')
    for key,value in [('object_id','1'),('instance_id','0'),('identify_id','1')]: ET.SubElement(inst,'metadata',{'key':key,'value':value})
    path=ROOT/(slug+'--kp3-winkle-petg.3mf')
    with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as output:
        for name,data in packaging.items(): output.writestr(name,data)
        output.writestr('3D/3dmodel.model',ET.tostring(model,encoding='utf-8',xml_declaration=True))
        output.writestr('Metadata/model_settings.config',ET.tostring(settings,encoding='utf-8',xml_declaration=True))
        output.writestr('Metadata/project_settings.config',json.dumps(cfg,indent=2))
    manifest.append({k:v for k,v in item.items() if k not in ['vertices','triangles']})
(ROOT/'piezas.json').write_text(json.dumps(manifest,indent=2)+'\n')
(ROOT/'receta-origen.json').write_text(json.dumps({'project':str(BASE.relative_to(ROOT.parent)), 'sha256':hashlib.sha256(BASE.read_bytes()).hexdigest(),'orca_version':'2.4.2'},indent=2)+'\n')
print('Tres proyectos preparados; receta de referencia conservada.')
