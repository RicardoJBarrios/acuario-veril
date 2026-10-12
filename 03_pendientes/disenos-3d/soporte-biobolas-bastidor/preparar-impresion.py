"""Proyectos Orca independientes con mallas exportadas del FCStd final.

Reutiliza identidad/receta KP3-PETG anterior; sustituye toda la geometría.
No modifica perfiles globales ni inicia una impresión.
"""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from xml.etree import ElementTree as ET
import hashlib
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'impresion';OUT.mkdir(exist_ok=True)
CORE='http://schemas.microsoft.com/3dmanufacturing/core/2015/02'
ET.register_namespace('',CORE)
manifest=json.loads((ROOT/'mallas-fabricacion.json').read_text())
meshes=manifest['meshes']
template=ROOT.parent/'soporte-biobolas-impresion/modulo--kp3-winkle-petg.3mf'
with ZipFile(template) as z:
    inherited={n:z.read(n) for n in ['[Content_Types].xml','_rels/.rels']}
    settings=json.loads(z.read('Metadata/project_settings.config'))
for key in list(settings):
    if any(s in key.lower() for s in ['print_host','printhost','password','api_key','access_code','secret','token']):
        settings.pop(key)
settings.update({'enable_support':'0','wall_loops':'6','sparse_infill_density':'100%',
                 'sparse_infill_pattern':'rectilinear','brim_type':'outer_only',
                 'brim_object_gap':'0.1','raft_layers':'0','layer_height':'0.2',
                 'initial_layer_print_height':'0.24'})


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def layout(items,padding):
    items=sorted(items,key=lambda x:meshes[x]['bounds_mm'][1],reverse=True)
    placed=[];x=y=padding+2;row_h=0
    for name in items:
        width,height,_=meshes[name]['bounds_mm']
        if x+width+padding>178:
            x=padding+2;y+=row_h+2*padding+2;row_h=0
        if y+height+padding>178:raise RuntimeError('La placa no cabe: '+name)
        placed.append((name,x,y));x+=width+2*padding+2;row_h=max(row_h,height)
    # Centrar la envolvente sin cambiar escala ni Z.
    xmax=max(x+meshes[n]['bounds_mm'][0] for n,x,y in placed)
    ymax=max(y+meshes[n]['bounds_mm'][1] for n,x,y in placed)
    xmin=min(x for n,x,y in placed);ymin=min(y for n,x,y in placed)
    dx=90-(xmin+xmax)/2;dy=90-(ymin+ymax)/2
    return [(n,x+dx,y+dy) for n,x,y in placed]


def project(slug,items,gcode,repeat,brim,purpose):
    placed=layout(items,brim)
    model=ET.Element('{'+CORE+'}model',{'unit':'millimeter','xml:lang':'en-US'})
    ET.SubElement(model,'{'+CORE+'}metadata',{'name':'Title'}).text='Veril bastidor '+slug
    resources=ET.SubElement(model,'{'+CORE+'}resources');build=ET.SubElement(model,'{'+CORE+'}build')
    cfg=ET.Element('config');plate=ET.Element('plate')
    for key,value in [('plater_id','1'),('plater_name',slug),('locked','false')]:
        ET.SubElement(plate,'metadata',{'key':key,'value':value})
    for oid,(name,x,y) in enumerate(placed,1):
        geom=meshes[name];obj=ET.SubElement(resources,'{'+CORE+'}object',{'id':str(oid),'type':'model','name':name})
        mesh=ET.SubElement(obj,'{'+CORE+'}mesh');verts=ET.SubElement(mesh,'{'+CORE+'}vertices')
        tris=ET.SubElement(mesh,'{'+CORE+'}triangles')
        for vx,vy,vz in geom['vertices']:
            ET.SubElement(verts,'{'+CORE+'}vertex',{'x':format(vx+x,'.7f'),'y':format(vy+y,'.7f'),'z':format(vz,'.7f')})
        for a,b,c in geom['triangles']:
            ET.SubElement(tris,'{'+CORE+'}triangle',{'v1':str(a),'v2':str(b),'v3':str(c)})
        ET.SubElement(build,'{'+CORE+'}item',{'objectid':str(oid)})
        co=ET.SubElement(cfg,'object',{'id':str(oid)})
        for key,value in [('name',name),('extruder','1')]:ET.SubElement(co,'metadata',{'key':key,'value':value})
        part=ET.SubElement(co,'part',{'id':str(oid),'subtype':'normal_part'})
        for key,value in [('name',name),('extruder','1')]:ET.SubElement(part,'metadata',{'key':key,'value':value})
        instance=ET.SubElement(plate,'model_instance')
        for key,value in [('object_id',str(oid)),('instance_id','0'),('identify_id',str(oid))]:
            ET.SubElement(instance,'metadata',{'key':key,'value':value})
    cfg.append(plate)
    effective=dict(settings);effective.update({'brim_width':str(brim),
        'print_settings_id':'Veril bastidor '+slug+' KP3 PETG 0.20 candidato'})
    path=OUT/(slug+'--kp3-winkle-petg.3mf')
    with ZipFile(path,'w',ZIP_DEFLATED) as z:
        for name,data in inherited.items():z.writestr(name,data)
        z.writestr('3D/3dmodel.model',ET.tostring(model,encoding='utf-8',xml_declaration=True))
        z.writestr('Metadata/model_settings.config',ET.tostring(cfg,encoding='utf-8',xml_declaration=True))
        z.writestr('Metadata/project_settings.config',json.dumps(effective,ensure_ascii=False).encode())
    return {'slug':slug,'project':path.name,'project_sha256':sha(path),'gcode':gcode,
            'repeat_count':repeat,'brim_mm':brim,'objects':len(items),'parts':items,
            'purpose':purpose,'placements':[{'name':n,'x_mm':x,'y_mm':y} for n,x,y in placed]}


jobs=[]
for name,slug,gcode,repeat in [
 ('FunctionalBase','base','BASTBASE.GCO',2),('PanelA','panel-a','BASTPA.GCO',4),
 ('PanelB','panel-b','BASTPB.GCO',4),('FunctionalUpper','marco-superior','BASTSUP.GCO',2),
 ('LidFrame','tapa','BASTTAPA.GCO',1),('HangerPlate','escuadra','BASTCOLG.GCO',2),
 ('CenteredHandle','asa','BASTASA.GCO',1)]:
    jobs.append(project(slug,[name],gcode,repeat,5,'pieza completa candidata'))
jobs.append(project('cierres-panel',['PanelKey']*32+['PanelKeeper']*32,'BASTPIN.GCO',1,3,'32 pasadores y 32 chavetas de panel'))
jobs.append(project('cierres-estructurales',['StackKey']*4+['LidKey']*4+['HandleKey']*2+['StructuralKeeper']*10,
                    'BASTSEG.GCO',1,3,'apilamiento, suspensión y asa'))
coupons=[n for n in meshes if n.endswith('Coupon') or n.endswith('CouponB')]
coupons+=['PanelKey','PanelKeeper','StackKey','LidKey','HandleKey','StructuralKeeper']
jobs.append(project('probetas',coupons,'BASTTEST.GCO',1,3,'imprimir primero: ajuste y ensayo'))
(OUT/'piezas.json').write_text(json.dumps({'source_fcstd_sha256':manifest['source_sha256'],
    'template':str(template.relative_to(ROOT.parent)),'template_sha256':sha(template),
    'recipe_status':'candidato','jobs':jobs},ensure_ascii=False,indent=2)+'\n')
print('PROYECTOS_CREADOS',len(jobs))
