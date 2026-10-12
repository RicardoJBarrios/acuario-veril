"""Corrección de encuentros tras la comprobación geométrica, en hilo GUI."""
from pathlib import Path
exec(compile((Path(doc.FileName).parent/'completar-bastidor.py').read_text(),
             'completar-bastidor.py','exec'))
updates={'panelWidth':68.2,'forkHeight':31,'pinCenterB':26,'hangerLegWidth':18,
         'handleKeyLength':21.6,'handleCenter':27,'handleWidth':64,'handleFootSeat':8,
         'handleHeadHeight':2,'handleCrossbarWidth':16}
def cell_text(address):
    try:return doc.RevisionParameters.get(address)
    except ValueError:return ''
next_row=max(i for i in range(1,100) if cell_text('A'+str(i)))+1
for alias,value in updates.items():
    if hasattr(doc.RevisionParameters,alias):
        row=next(i for i in range(2,100) if cell_text('A'+str(i))==alias)
    else:
        row=next_row;next_row+=1
        doc.RevisionParameters.set('A'+str(row),alias)
        doc.RevisionParameters.set('B'+str(row),'='+str(value)+' mm')
        doc.RevisionParameters.setAlias('B'+str(row),alias)
    doc.RevisionParameters.set('B'+str(row),'='+str(value)+' mm')
doc.recompute()
for name in ['PanelA','PanelB']:
    profile=doc.getObject(name+'ReliefProfile')
    for idx in range(profile.GeometryCount-1,15,-1):profile.delGeometry(idx)
profile=doc.FUStackProfile
for idx in range(profile.GeometryCount-1,15,-1):profile.delGeometry(idx)
for profile in [doc.CHProfile,doc.CHKeyProfile]:
    for path,expr in list(profile.ExpressionEngine):
        replacement=expr.replace('RevisionParameters.outerWidth','RevisionParameters.handleWidth')
        if profile==doc.CHKeyProfile:
            replacement=replacement.replace('RevisionParameters.stackCenter','RevisionParameters.handleCenter')
        if replacement!=expr:profile.setExpression(path,replacement)
# Solo los dos últimos rectángulos del marco de tapa son las llaves del asa.
profile=doc.LFKeyProfile
for ci,c in enumerate(profile.Constraints):
    if c.Name in ['V'+str(i)+'Y' for i in range(16,24)]:
        expr=next(expr for path,expr in profile.ExpressionEngine if path.endswith('.'+c.Name))
        profile.setExpression('Constraints['+str(ci)+']',expr.replace('RevisionParameters.stackCenter','RevisionParameters.handleCenter'))
doc.HandleKeyHeadPad.setExpression('Length',expression('handleHeadHeight'))
for i in [1,2]:
    doc.getObject('RUpper'+str(i)).setExpression('Placement.Base.z',expression('modulePitch-forkHeight'))
    for side in [1,3]:
        for level in ['B','T']:
            for sign in [-1,1]:
                suffix=str(i)+str(side)+level+str(sign).replace('-','N')
                e='pinCenterB' if level=='B' else 'modulePitch-pinCenterB'
                for prefix in ['RPanelKey','RPanelKeeper']:
                    doc.getObject(prefix+suffix).setExpression('Placement.Base.z',expression(e))
for sy in [-1,1]:
    suffix=str(sy).replace('-','N')
    k=doc.getObject('RHandleKey'+suffix);p=k.Placement.Base
    p.y=sy*val('handleCenter')+val('stackKeyThickness')/2;p.z=-5.6;k.Placement.Base=p
    k=doc.getObject('RHandleKeeper'+suffix);p=k.Placement.Base
    p.y=sy*val('handleCenter')+val('keeperThickness')/2;p.z=-2.1;k.Placement.Base=p
doc.RHandle.setExpression('Placement.Base.z',expression('lidHeight'))
doc.recompute()
panel_seats(doc.FunctionalBase,'FBPanelSeats','baseHeight')
panel_seats(doc.FunctionalUpper,'FUPanelSeats','forkHeight')
add_handle_crossbars(doc.LidFrame)
# Los pasos nuevos en los travesaños utilizan los mismos taladros paramétricos.
vertical_holes(doc.LidFrame,'LFBeamKey','lidHeight','lidHeight',True)
hanger_key_access(doc.HangerPlate)
handle_key_access(doc.CenteredHandle)
for item in doc.RevisionMasters.Group:
    item.Tip.ViewObject.ShapeColor=item.ViewObject.ShapeColor;item.Visibility=False
    assert item.Shape.isValid() and len(item.Shape.Solids)==1,item.Name
doc.recompute();doc.save()
print('ENCUENTROS_CORREGIDOS')
