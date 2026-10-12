"""Comprobaciones y exportación desde FreeCAD, en el hilo GUI.

No altera geometría de fabricación. Las rotaciones y normalizaciones se hacen
en copias de TopoShape; conserva el CAD y su posición de montaje.
"""
import json
import hashlib
from pathlib import Path
import FreeCAD as App
import FreeCADGui as Gui

folder=Path(doc.FileName).parent
doc.recompute()
assert cad_checks_done
assert not [c for c in cad_checks if c['common_mm3']>1e-6]
assert all(o.FullyConstrained for o in doc.Objects if o.TypeId=='Sketcher::SketchObject')
assert not [(o.Name,str(o.State)) for o in doc.Objects if 'Invalid' in o.State]
assert abs(doc.CenteredHandle.Shape.BoundBox.XLength-val('handleWidth'))<1e-6
assert abs(doc.PanelA.Shape.BoundBox.XLength-val('panelWidth'))<1e-6
assert all(c['head_contact_distance_mm']<1e-6 for c in engagement_checks)

# Variación de un parámetro estructural y restauración exacta del volumen.
sheet=doc.RevisionParameters
row=next(i for i in range(2,100) if sheet.get('A'+str(i))=='braceExtra')
before=doc.PanelA.Shape.Volume
sheet.set('B'+str(row),'=2.1 mm');doc.recompute()
changed=doc.PanelA.Shape.Volume
trial=doc.PanelA.Shape.isValid() and len(doc.PanelA.Shape.Solids)==1
sheet.set('B'+str(row),'=2 mm');doc.recompute()
restored=doc.PanelA.Shape.Volume
assert trial and abs(restored-before)<1e-6 and changed>before

for o in doc.RevisionMasters.Group:
    o.Tip.ViewObject.ShapeColor=o.ViewObject.ShapeColor;o.Visibility=False
doc.FitCoupons.Visibility=False;doc.AntecedenteCADInicial.Visibility=False
view=Gui.activeDocument().activeView();view.viewAxonometric();view.fitAll()
view.saveImage(str(folder/'vista-conjunto-funcional.png'),1200,1200,'Current')
visible=[(o,o.Visibility) for o in [doc.ContextoC1,doc.Array,doc.Array001]]
for o,v in visible:o.Visibility=False
view.fitAll();view.saveImage(str(folder/'vista-estructura-funcional.png'),1200,1200,'Current')
view.viewFront();view.fitAll();view.saveImage(str(folder/'vista-frontal-funcional.png'),1200,1200,'Current')
for o,v in visible:o.Visibility=v
view.viewAxonometric();view.fitAll()
doc.save()
source_sha=hashlib.sha256(Path(doc.FileName).read_bytes()).hexdigest()

parents=[doc.RevisionModule1,doc.RevisionModule2,doc.StackingLocks,doc.Suspension]
world={}
for parent in parents:
    for o in parent.Group:
        s=o.Shape.copy();s.Placement=parent.Placement.multiply(s.Placement);world[o.Name]=s
report={'date':'2026-10-12','stage':'CAD_funcional_candidato',
    'source_sha256':source_sha,'parameters_mm':{a:val(a) for a in VALUES},
    'master_shapes':{},'sketches':[],
    'assembled_volume_mm3':sum(s.Volume for s in world.values()),
    'assembled_bounds_mm':[min(s.BoundBox.XMin for s in world.values()),max(s.BoundBox.XMax for s in world.values()),
                          min(s.BoundBox.YMin for s in world.values()),max(s.BoundBox.YMax for s in world.values()),
                          min(s.BoundBox.ZMin for s in world.values()),max(s.BoundBox.ZMax for s in world.values())],
    'checks':cad_checks,'check_seconds':cad_check_seconds,
    'engagement_checks':engagement_checks,
    'ball_collision_method':'Envolventes anulares conservadoras Ø31, altura29, paso29, agujeroØ10.5; no se usa el detalle de los poros.',
    'parameter_test':{'alias':'braceExtra','before_mm':2,'test_mm':2.1,
                      'valid_single_solid':trial,'before_volume_mm3':before,
                      'test_volume_mm3':changed,'restored_volume_mm3':restored},
    'external_links':[(o.Name,r.Name) for o in doc.Objects for r in o.OutList if r.Document!=doc],
    'open_documents':list(App.listDocuments()),
}
names=[]
for o in doc.RevisionMasters.Group:
    quantity=sum(1 for parent in parents for l in parent.Group if l.LinkedObject==o)
    if quantity or o in doc.FitCoupons.Group:
        if o.Name not in names:names.append(o.Name)
    b=o.Shape.BoundBox
    report['master_shapes'][o.Name]={'valid':o.Shape.isValid(),'solids':len(o.Shape.Solids),
        'bounds_mm':[b.XLength,b.YLength,b.ZLength],'volume_mm3':o.Shape.Volume,
        'quantity':quantity,'tip_state':list(o.Tip.State)}
report['sketches']=[{'name':o.Name,'fully_constrained':o.FullyConstrained} for o in doc.Objects if o.TypeId=='Sketcher::SketchObject']
assert not report['external_links']
(folder/'comprobacion-cad-funcional.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
for o in doc.FitCoupons.Group:
    if o.Name not in names:names.append(o.Name)

meshes={};step_dir=folder/'impresion'/'modelos';step_dir.mkdir(parents=True,exist_ok=True)
for name in names:
    o=doc.getObject(name);s=o.Shape.copy()
    if name=='FunctionalUpper':s.rotate(App.Vector(0,0,0),App.Vector(1,0,0),180)
    b=s.BoundBox;s.translate(App.Vector(-b.XMin,-b.YMin,-b.ZMin));b=s.BoundBox
    assert max(b.XLength,b.YLength,b.ZLength)<=180,name
    vertices,triangles=s.tessellate(0.05)
    # Soldadura de vértices coincidentes: no reparación ni simplificación.
    unique=[];indices={};mapping=[]
    for vertex in vertices:
        key=tuple(round(v,7) for v in (vertex.x,vertex.y,vertex.z))
        if key not in indices:indices[key]=len(unique);unique.append(key)
        mapping.append(indices[key])
    facets=[tuple(mapping[v] for v in triangle) for triangle in triangles]
    assert all(len(set(t))==3 for t in facets),name
    meshes[name]={'bounds_mm':[b.XLength,b.YLength,b.ZLength],
                  'vertices':unique,'triangles':facets,
                  'source_volume_mm3':o.Shape.Volume,
                  'print_rotation':'RX180' if name=='FunctionalUpper' else 'CAD_XY',
                  'source_object':name}
    s.exportStep(str(step_dir/(name+'.step')))
manifest={'source_fcstd':Path(doc.FileName).name,'source_sha256':source_sha,
          'deflection_mm':0.05,'units':'mm','meshes':meshes}
(folder/'mallas-fabricacion.json').write_text(json.dumps(manifest,ensure_ascii=False)+'\n')
print('CAD_FINAL_VERIFICADO',len(world),'piezas',len(cad_checks),'comprobaciones',len(report['sketches']),'sketches')
print('EXPORTADAS',len(meshes),'maestras y probetas')
