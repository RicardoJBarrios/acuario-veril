"""Auditoría de 3MF y G-code, sin enviar instrucciones a la impresora."""
from pathlib import Path
from collections import Counter
from xml.etree import ElementTree as ET
from zipfile import ZipFile
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'impresion'
manifest=json.loads((OUT/'piezas.json').read_text())
CORE='{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}'
FIELDS=['printer_settings_id','printer_model','filament_settings_id','filament_type',
 'nozzle_diameter','printable_area','printable_height','gcode_flavor',
 'layer_height','initial_layer_print_height','nozzle_temperature','nozzle_temperature_initial_layer',
 'hot_plate_temp','hot_plate_temp_initial_layer','textured_plate_temp','textured_plate_temp_initial_layer',
 'filament_flow_ratio','filament_max_volumetric_speed','filament_density',
 'initial_layer_speed','initial_layer_infill_speed','outer_wall_speed','inner_wall_speed',
 'sparse_infill_speed','internal_solid_infill_speed','top_surface_speed','bridge_speed','travel_speed',
 'default_acceleration','outer_wall_acceleration','inner_wall_acceleration','initial_layer_acceleration',
 'retraction_length','retraction_speed','deretraction_speed','enable_pressure_advance','pressure_advance',
 'fan_min_speed','fan_max_speed','close_fan_the_first_x_layers','full_fan_speed_layer',
 'wall_loops','top_shell_layers','bottom_shell_layers','sparse_infill_density','sparse_infill_pattern',
 'enable_support','support_type','brim_type','brim_width','brim_object_gap','raft_layers',
 'xy_hole_compensation','xy_contour_compensation','elefant_foot_compensation','print_sequence']


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def audit_project(path):
    with ZipFile(path) as z:
        assert z.testzip() is None
        cfg=json.loads(z.read('Metadata/project_settings.config'))
        root=ET.fromstring(z.read('3D/3dmodel.model'))
        objects=root.findall(CORE+'resources/'+CORE+'object')
        for obj in objects:
            vertices=[tuple(float(v.get(a)) for a in ['x','y','z']) for v in obj.findall('.//'+CORE+'vertex')]
            facets=[tuple(int(t.get(a)) for a in ['v1','v2','v3']) for t in obj.findall('.//'+CORE+'triangle')]
            assert vertices and facets
            edges=Counter()
            for a,b,c in facets:
                for u,v in [(a,b),(b,c),(c,a)]:edges[tuple(sorted((u,v)))]+=1
            assert all(n==2 for n in edges.values()),'Malla no cerrada: '+str(path)+' '+obj.get('name')
            assert min(v[2] for v in vertices)>=-1e-6
            assert max(v[2] for v in vertices)<=180
        assert cfg['enable_support']=='0'
        assert cfg['sparse_infill_density']=='100%'
        return {'zip_valid':True,'closed_meshes':True,'objects':len(objects),
                'settings':{k:cfg[k] for k in FIELDS if k in cfg}}


def audit_gcode(path):
    data=path.read_text(errors='strict');cfg={};types=Counter()
    bounds={'x':[float('inf'),float('-inf')],'y':[float('inf'),float('-inf')],'z':[float('inf'),float('-inf')]}
    position={a:0.0 for a in ['x','y','z']};arcs=0;absolute=True
    for line in data.splitlines():
        setting=re.match(r'; ([A-Za-z0-9_]+) = (.*)$',line)
        if setting and setting[1] in FIELDS:cfg[setting[1]]=setting[2]
        if line.startswith(';TYPE:'):types[line[6:].strip()]+=1
        command=line.split(';',1)[0].strip()
        if not command:continue
        op=command.split()[0]
        args={a.lower():float(v) for a,v in re.findall(r'([XYZ])\s*(-?(?:\d+(?:\.\d*)?|\.\d+))',command)}
        if op=='G90':absolute=True
        elif op=='G91':absolute=False
        elif op=='G92':position.update(args)
        elif op=='G28':
            axes=[a for a in position if re.search(r'\b'+a.upper()+r'\b',command)]
            for a in axes or position:position[a]=0.0
        elif op in ['G0','G1','G2','G3']:
            if op in ['G2','G3']:arcs+=1
            for axis,value in args.items():position[axis]=value if absolute else position[axis]+value
            for axis,v in position.items():
                bounds[axis][0]=min(bounds[axis][0],v);bounds[axis][1]=max(bounds[axis][1],v)
    assert not arcs,'Revisar envolvente de arcos antes de aceptar'
    assert all(bounds[a][0]>=-1e-6 and bounds[a][1]<=180.000001 for a in ['x','y','z']),bounds
    assert cfg.get('enable_support')=='0'
    assert cfg.get('sparse_infill_density')=='100%'
    assert not any('support' in typ.lower() for typ in types)
    time=re.search(r'; estimated printing time \(normal mode\) = (.+)',data)
    mass=re.search(r'; (?:total )?filament (?:weight|used \[g\])\s*(?:\[g\])?\s*=\s*([\d.]+)',data)
    layers=re.search(r'; total layer number: (\d+)',data)
    if not layers:layers=re.search(r'; layer_count = (\d+)',data)
    return {'bytes':path.stat().st_size,'sha256':sha(path),'settings':cfg,'bounds_mm':bounds,
            'supports_generated':False,'feature_types':dict(types),'arc_moves':arcs,
            'estimated_time':time[1].strip() if time else None,
            'estimated_mass_g':float(mass[1]) if mass else None,
            'layers':int(layers[1]) if layers else None,'physical_print_tested':False}


result={'source_fcstd_sha256':manifest['source_fcstd_sha256'],'jobs':[],'stage':'laminado_candidato'}
assert sha(ROOT/'soporte-biobolas-bastidor.FCStd')==manifest['source_fcstd_sha256']
for job in manifest['jobs']:
    project=OUT/job['project'];gcode=OUT/'gcode'/job['gcode']
    assert sha(project)==job['project_sha256']
    p=audit_project(project);g=audit_gcode(gcode)
    sliced=OUT/'laminados'/job['slug']/(job['slug']+'-laminado.3mf')
    with ZipFile(sliced) as z:
        assert z.testzip() is None
        embedded=[n for n in z.namelist() if n.endswith('.gcode')]
        assert len(embedded)==1 and z.read(embedded[0])==gcode.read_bytes()
        stats=ET.fromstring(z.read('Metadata/slice_info.config'))
        stats={e.get('key'):e.get('value') for e in stats.findall('./plate/metadata')}
        assert stats['support_used']=='false' and stats['outside']=='false'
    assert p['objects']==job['objects']
    item=dict(job);item.update({'project_check':p,'gcode_check':g})
    item['sliced_project_check']={'sha256':sha(sliced),'embedded_gcode_matches':True,
                                'support_used':stats['support_used'],'outside':stats['outside']}
    item['cli_warning_lines']=[s for s in (OUT/'laminados'/job['slug']/'orca-cli.log').read_text().splitlines()
                               if any(w in s.lower() for w in ['warning','error','warn:'])]
    result['jobs'].append(item)
    print('VERIFICADO',job['slug'],g['estimated_time'],g['estimated_mass_g'],'g',g['layers'],'capas')
(OUT/'comprobacion-laminado.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
