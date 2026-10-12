"""Comprobación CAD, sin aceptación física. Ejecutar tras montar el documento."""
import itertools,time,json,hashlib
checks=[];t0=time.time()

def overlap(a,b):
 A=a.BoundBox;B=b.BoundBox
 return all(min(getattr(A,k+'Max'),getattr(B,k+'Max'))-max(getattr(A,k+'Min'),getattr(B,k+'Min'))>1e-6 for k in 'XYZ')

def check(na,a,nb,b):
 if not overlap(a,b):return
 vol=a.common(b).Volume
 checks.append({'a':na,'b':nb,'overlap_mm3':vol})

for (na,a),(nb,b) in itertools.combinations(printed_shapes,2):check(na,a,nb,b)
for (na,a),(nb,b) in itertools.combinations(hardware_shapes,2):check(na,a,nb,b)
for na,a in printed_shapes:
 for nb,b in hardware_shapes:check(na,a,nb,b)
balls=[]
for m in [0,1]:
 for sx in [-1,1]:
  for sy in [-1,1]:
   for j in range(5):
    center=App.Vector(P['centerX']+sx*P['pitch']/2,sy*P['pitch']/2,P['baseZ']+P['seat']+m*P['module']+29*j)
    sh=Part.makeCylinder(15.5,29,center).cut(Part.makeCylinder(5.25,29,center));balls.append(('bola'+str((m,sx,sy,j)),sh))
for na,a in printed_shapes+hardware_shapes:
 for nb,b in balls:check(na,a,nb,b)
for n in ['HotelPodsReference','UpperHotelPodsReference']:
 ref=d.getObject(n).Shape.copy()
 for na,a in printed_shapes+hardware_shapes:check(na,a,n,ref)
# Vidrios reales simplificados del contexto, excluyendo herramientas y agua.
ctx=d.getObject('ContextoC1')
for o in ctx.Group:
 if not hasattr(o,'Shape') or not o.Visibility or o.Name in ['C1Perforacion','C1NivelAgua','C1PasoLibre','C1LacobelBase']:continue
 for na,a in printed_shapes+hardware_shapes:check(na,a,o.Name,o.Shape)
print('Checks',len(checks),'seconds',time.time()-t0)
print('INTERFERENCIAS',[c for c in checks if c['overlap_mm3']>0.01])
report={'stage':'CAD_candidato_no_laminado_no_ensayado','date':'2026-10-12','printed_instances':16,'hardware_instances':104,'bolted_joints':26,'checks':checks,'check_seconds':time.time()-t0,'master_shapes':{},'sketches':{},'parameters_mm':P,'external_links':[],'references':{}}
for o in d.Maestras.Group:
 report['master_shapes'][o.Name]={'valid':o.Shape.isValid(),'solids':len(o.Shape.Solids),'volume_mm3':o.Shape.Volume,'bbox_mm':[o.Shape.BoundBox.XLength,o.Shape.BoundBox.YLength,o.Shape.BoundBox.ZLength]}
for o in d.Objects:
 if o.TypeId=='Sketcher::SketchObject':report['sketches'][o.Name]=o.FullyConstrained
 if o.TypeId=='App::Link' and o.LinkedObject.Document!=d:report['external_links'].append(o.Name)
for n in ['Array','Array001']:
 a=d.getObject(n);report['references'][n]={'valid':a.Shape.isValid(),'solids':len(a.Shape.Solids),'volume_mm3':a.Shape.Volume,'matches_source_volume':abs(a.Shape.Volume-src.getObject(n).Shape.Volume)<1e-6}
report['mass_full_solid_g']=sum(sh.Volume for n,sh in printed_shapes)*1.23/1000
(ROOT/'comprobacion-cad.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
