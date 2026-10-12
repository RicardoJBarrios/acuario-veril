"""Último ajuste FDM: paredes de punta y esquinas, sin cambiar la envolvente."""
from pathlib import Path
exec(compile((Path(doc.FileName).parent/'completar-bastidor.py').read_text(),
             'completar-bastidor.py','exec'))
def cell_text(address):
    try:return doc.RevisionParameters.get(address)
    except ValueError:return ''
next_row=max(i for i in range(1,100) if cell_text('A'+str(i)))+1
for alias,value in {'panelKeyLength':10.3,'stackCenter':36.9,'stackHeadWidth':5.6,
                    'panelTipY':29.4,'panelWindowCenter':1.6,'panelKeeperLength':5.4}.items():
    if hasattr(doc.RevisionParameters,alias):
        row=next(i for i in range(2,100) if cell_text('A'+str(i))==alias)
    else:
        row=next_row;next_row+=1
        doc.RevisionParameters.set('A'+str(row),alias)
        doc.RevisionParameters.set('B'+str(row),'='+str(value)+' mm')
        doc.RevisionParameters.setAlias('B'+str(row),alias)
    doc.RevisionParameters.set('B'+str(row),'='+str(value)+' mm')
doc.recompute()
profile=doc.PanelKeyKeeperProfile
for ci,c in enumerate(profile.Constraints):
    if c.Name in ['V0Y','V1Y']:
        profile.setExpression('Constraints['+str(ci)+']',expression('panelWindowCenter-1.4 mm/2'))
    elif c.Name in ['V2Y','V3Y']:
        profile.setExpression('Constraints['+str(ci)+']',expression('panelWindowCenter+1.4 mm/2'))
for profile in [doc.PanelKeeperProfile,doc.PanelKeeperHeadProfile]:
    for path,expr in list(profile.ExpressionEngine):
        expr=expr.replace('6.2 mm','RevisionParameters.panelKeeperLength')
        if profile==doc.PanelKeeperHeadProfile:expr=expr.replace('0.8 mm','0.6 mm')
        profile.setExpression(path,expr)
for ci,c in enumerate(doc.HPAccessProfile.Constraints):
    if c.Name in ['V1X','V2X']:
        doc.HPAccessProfile.setExpression('Constraints['+str(ci)+']',
            expression('glassInner-(glassOpening-glassThickness)/2+0.2 mm'))
for i in [1,2]:
    for side in range(4):
        rz=App.Rotation(App.Vector(0,0,1),side*90)
        center=val('pinCenterA' if side%2==0 else 'pinCenterB')
        for level,z in [('B',center),('T',val('modulePitch')-center)]:
            for sign in [-1,1]:
                suffix=str(i)+str(side)+level+str(sign).replace('-','N')
                rotation=rz.multiply(App.Rotation(App.Vector(1,0,0),180))
                pos=rz.multVec(App.Vector(sign*val('jointCenter'),-val('panelTipY'),z+2))
                obj=doc.getObject('RPanelKey'+suffix)
                obj.setExpression('Placement.Base.z',None)
                obj.Placement=App.Placement(pos,rotation)
                pos=rz.multVec(App.Vector(sign*val('jointCenter'),-31,z+0.8))
                obj=doc.getObject('RPanelKeeper'+suffix)
                obj.setExpression('Placement.Base.z',None)
                obj.Placement=App.Placement(pos,rotation)
for sx in [-1,1]:
    for sy in [-1,1]:
        suffix=str(sx).replace('-','N')+str(sy).replace('-','N')
        for obj in [doc.getObject('RStackKey'+suffix),doc.getObject('RLidKey'+suffix)]:
            p=obj.Placement.Base;p.x=sx*val('stackCenter')
            p.y=sy*val('stackCenter')+val('stackKeyThickness')/2;obj.Placement.Base=p
        for obj in [doc.getObject('RStackKeeper'+suffix),doc.getObject('RLidKeeper'+suffix)]:
            p=obj.Placement.Base;p.x=sx*(val('stackCenter')+0.4)
            p.y=sy*val('stackCenter')+val('keeperThickness')/2;obj.Placement.Base=p
for sy in [-1,1]:
    obj=doc.getObject('RHanger'+str(sy).replace('-','N'));p=obj.Placement.Base
    p.y=sy*val('stackCenter')+val('hangerThickness')/2;obj.Placement.Base=p
doc.recompute()
panel_key_tip(doc.PanelKey)
for obj in doc.RevisionMasters.Group:
    obj.Tip.ViewObject.ShapeColor=obj.ViewObject.ShapeColor;obj.Visibility=False
    assert obj.Shape.isValid() and len(obj.Shape.Solids)==1,obj.Name
doc.recompute();doc.save()
print('FDM_AJUSTADO')
