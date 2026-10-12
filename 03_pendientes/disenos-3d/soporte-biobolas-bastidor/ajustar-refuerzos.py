"""Ajuste mínimo de la revisión ya creada, dentro del hilo GUI de FreeCAD."""
from pathlib import Path
exec(compile((Path(doc.FileName).parent/'completar-bastidor.py').read_text(),
             'completar-bastidor.py','exec'))
for alias,value in [('ribWidth',12),('keeperWidth',4),('stackKeyLength',14.6),
                    ('lidKeyLength',26.6),('handleKeyLength',28.6)]:
    for row in range(2,100):
        if doc.RevisionParameters.get('A'+str(row))==alias:
            doc.RevisionParameters.set('B'+str(row),'='+str(value)+' mm');break
for name in ['StackKey','LidKey','HandleKey']:
    profile=doc.getObject(name+'KeeperProfile')
    for ci in range(profile.ConstraintCount):
        cn=profile.Constraints[ci].Name
        if cn in ['V0Y','V1Y']:
            profile.setExpression('Constraints['+str(ci)+']','3.5 mm-4.2 mm/2')
        elif cn in ['V2Y','V3Y']:
            profile.setExpression('Constraints['+str(ci)+']','3.5 mm+4.2 mm/2')
for name in ['PanelA','PanelB']:
    profile=doc.getObject(name+'ReliefProfile')
    for ci in range(profile.ConstraintCount):
        if profile.Constraints[ci].Name in ['V16Y','V17Y']:
            profile.setExpression('Constraints['+str(ci)+']',expression('panelHeight-8 mm'))
profile=doc.FBHotelProfile
for path,expr in list(profile.ExpressionEngine):
    if '16.55 mm' in expr:
        profile.setExpression(path,expr.replace('16.55 mm',
            '(RevisionParameters.columnPitch/2-RevisionParameters.ribWidth/2-0.2 mm)'))
for item in doc.StackingLocks.Group:
    pos=item.Placement.Base
    pos.z=val('modulePitch')-(8.6 if item.Name.startswith('RStackKey') else 5.1)
    item.Placement.Base=pos
for item in doc.Suspension.Group:
    if item.Name.startswith(('RLidKey','RHandleKey')):
        pos=item.Placement.Base;pos.z=-8.6;item.Placement.Base=pos
    elif item.Name.startswith(('RLidKeeper','RHandleKeeper')):
        pos=item.Placement.Base;pos.z=-5.1;item.Placement.Base=pos
doc.recompute()
for item in doc.RevisionMasters.Group:
    item.Tip.ViewObject.ShapeColor=item.ViewObject.ShapeColor;item.Visibility=False
    assert item.Shape.isValid() and len(item.Shape.Solids)==1,item.Name
doc.save()
print('REFUERZOS_ACTUALIZADOS')
