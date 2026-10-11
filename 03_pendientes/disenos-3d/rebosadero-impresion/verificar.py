"""Check output provenance, effective recipe and all interpreted XYZ movements."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from collections import Counter
import hashlib, json, re, zipfile
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parent
KEYS='printer_settings_id printer_model printable_area printable_height gcode_flavor nozzle_diameter filament_settings_id filament_type filament_diameter filament_density print_settings_id layer_height initial_layer_print_height nozzle_temperature nozzle_temperature_initial_layer hot_plate_temp hot_plate_temp_initial_layer filament_flow_ratio filament_max_volumetric_speed retraction_length retraction_speed deretraction_speed z_hop enable_pressure_advance pressure_advance fan_min_speed fan_max_speed close_fan_the_first_x_layers full_fan_speed_layer slow_down_layer_time slow_down_min_speed wall_loops top_shell_layers bottom_shell_layers sparse_infill_pattern sparse_infill_density initial_layer_speed initial_layer_infill_speed outer_wall_speed inner_wall_speed sparse_infill_speed internal_solid_infill_speed top_surface_speed bridge_speed travel_speed default_acceleration initial_layer_acceleration outer_wall_acceleration inner_wall_acceleration travel_acceleration bridge_acceleration outer_wall_line_width inner_wall_line_width sparse_infill_line_width internal_solid_infill_line_width top_surface_line_width enable_support support_type support_style support_on_build_plate_only support_top_z_distance support_bottom_z_distance support_object_xy_distance support_interface_top_layers support_interface_bottom_layers support_base_pattern_spacing support_interface_spacing brim_type brim_width brim_object_gap raft_layers skirt_loops skirt_distance xy_contour_compensation xy_hole_compensation elefant_foot_compensation print_sequence machine_start_gcode machine_end_gcode'.split()

def file_info(path):
    return {'path':str(path.relative_to(ROOT)), 'bytes':path.stat().st_size, 'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}

report={'checked_at':datetime.now(ZoneInfo('Atlantic/Canary')).isoformat(),
        'cad_source':{'path':'../rebosadero.FCStd','sha256':hashlib.sha256((ROOT.parent/'rebosadero.FCStd').read_bytes()).hexdigest()},
        'method':'OrcaSlicer 2.4.2 CLI --datadir aislado --slice 0 con perfiles embebidos; sin --no-check',
        'physical_print':'pendiente','pieces':[]}
for item in json.loads((ROOT/'piezas.json').read_text()):
    slug=item['slug']
    project=ROOT/(slug+'--kp3-winkle-petg.3mf')
    sliced=ROOT/'laminados'/slug/(slug+'-laminado.3mf')
    gc=ROOT/item['gcode']
    text=gc.read_text()
    with zipfile.ZipFile(project) as z:
        assert z.testzip() is None
        config=json.loads(z.read('Metadata/project_settings.config'))
        for name in z.namelist():
            if name.endswith(('.xml','.model')):ET.fromstring(z.read(name))
    with zipfile.ZipFile(sliced) as z:
        assert z.testzip() is None
        stats=ET.fromstring(z.read('Metadata/slice_info.config'))
        meta={e.attrib['key']:e.attrib['value'] for e in stats.findall('./plate/metadata')}
        embedded=[n for n in z.namelist() if n.endswith('.gcode')]
        assert len(embedded)==1 and z.read(embedded[0])==gc.read_bytes()
        assert meta['support_used']=='false' and meta['outside']=='false'
    block=text.split('; CONFIG_BLOCK_START',1)[1].split('; CONFIG_BLOCK_END',1)[0]
    effective={}
    for line in block.splitlines():
        if ' = ' in line:
            k,v=line.removeprefix('; ').split(' = ',1)
            if k in KEYS:effective[k]=v
    assert effective['enable_support']=='0'
    axes={a:0.0 for a in 'XYZ'}
    axis_absolute=True
    e_absolute=False
    e_position=0.0
    mins={a:float('inf') for a in axes}
    maxs={a:float('-inf') for a in axes}
    violations=[]
    layer=None;feature='Custom';features=Counter();segments=[]
    for number,line in enumerate(text.split('; CONFIG_BLOCK_START',1)[0].splitlines(),1):
        if line.startswith(';Z:'):layer=float(line[3:])
        if line.startswith(';TYPE:'):feature=line[6:]
        command=line.split(';',1)[0].strip()
        if not command:continue
        op=command.split()[0]
        args={a:float(v) for a,v in re.findall(r'([XYZE])\s*(-?(?:\d+(?:\.\d*)?|\.\d+))',command)}
        if op=='G90':axis_absolute=True
        elif op=='G91':axis_absolute=False
        elif op=='M82':e_absolute=True
        elif op=='M83':e_absolute=False
        elif op=='G92':
            for a in axes:
                if a in args:axes[a]=args[a]
            if 'E' in args:e_position=args['E']
        elif op=='G28':
            chosen=[a for a in axes if re.search(r'\b'+a+r'\b',command)]
            for a in chosen or axes:axes[a]=0.0
        elif op in ['G0','G1']:
            start=dict(axes)
            for a in axes:
                if a in args:axes[a]=args[a] if axis_absolute else axes[a]+args[a]
                mins[a]=min(mins[a],axes[a]);maxs[a]=max(maxs[a],axes[a])
                if axes[a]<-0.001 or axes[a]>180.001:violations.append({'line':number,'axis':a,'value':axes[a]})
            de=(args['E']-e_position if e_absolute else args['E']) if 'E' in args else 0
            if 'E' in args:e_position=args['E'] if e_absolute else e_position+args['E']
            if de>0 and (abs(start['X']-axes['X'])+abs(start['Y']-axes['Y']))>1e-7:
                features[feature]+=1
                segments.append([start['X'],start['Y'],start['Z'],axes['X'],axes['Y'],axes['Z'],feature,layer])
    assert not violations,violations[:10]
    assert not any('support' in f.lower() for f in features)
    layers=int(re.search(r'; total layer number: (\d+)',text).group(1))
    maximum_layer=float(re.search(r'; max_z_height: ([\d.]+)',text).group(1))
    timestr=re.search(r'; estimated printing time \(normal mode\) = (.+)',text).group(1)
    seconds=sum(int(n)*{'h':3600,'m':60,'s':1}[u] for n,u in re.findall(r'(\d+)([hms])',timestr))
    assert seconds==int(meta['prediction'])
    mass=float(re.search(r'; total filament used \[g\] = ([\d.]+)',text).group(1))
    info={'identity':item,'project':file_info(project),'sliced_project':file_info(sliced),'stl':file_info(ROOT/'modelos'/(slug+'.stl')),'gcode':file_info(gc),
          'generated_header':re.search(r'; generated by (.+)',text).group(1),'project_settings':{k:config[k] for k in KEYS if k in config},'effective_gcode_settings':effective,
          'layers':layers,'maximum_layer_z_mm':maximum_layer,'estimated_time':timestr,'estimated_time_seconds':seconds,'estimated_mass_g':mass,
          'movement_bounds_mm':{'min':mins,'max':maxs},'movement_violations':violations,'extrusion_features':dict(features),'support_used':meta['support_used'],'outside':meta['outside'],
          'preview':{'path':f'laminados/{slug}/vista-previa.png','method':'reconstruccion de segmentos de extrusion del G-code; revision visual por el agente'},
          'cli_log':str((ROOT/'laminados'/slug/'orca-cli.log').relative_to(ROOT))}
    report['pieces'].append(info)
    (ROOT/'laminados'/slug/'trayectorias.json').write_text(json.dumps(segments))
(ROOT/'comprobacion-laminado.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps([{ 'piece':p['identity']['slug'],'time':p['estimated_time'],'grams':p['estimated_mass_g'],'max_movements':p['movement_bounds_mm']['max'],'support':p['support_used']} for p in report['pieces']],indent=2))
