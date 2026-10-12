"""Revisión funcional nativa. Ejecutar funciones por bloques en el hilo GUI.

Conserva el CAD inicial oculto; no modifica las referencias de C1/bolas/hoteles.
Las cotas y holguras son candidatas: no acreditan resistencia o encaje físico.
"""
import math
import re
import FreeCAD as App
import FreeCADGui as Gui
import Part
import Sketcher

from pathlib import Path
matches=[d for d in App.listDocuments().values()
         if d.FileName and Path(d.FileName).name=='soporte-biobolas-bastidor.FCStd']
if len(matches)!=1:
    raise RuntimeError('Abrir un único soporte-biobolas-bastidor.FCStd antes de ejecutar')
doc=matches[0]

VALUES = {
    'outerWidth':81, 'frameWidth':6, 'baseHeight':6, 'seatHeight':3,
    'ribWidth':12, 'columnPitch':36.5, 'modulePitch':150,
    'panelWidth':68.2, 'panelHeight':147, 'panelThickness':3.2,
    'railWidth':10, 'diagonalWidth':10, 'panelOffset':34.4,
    'cornerPad':10, 'cornerPadCenter':35.5, 'cornerNotch':9,
    'jointCenter':31, 'forkHalfWidth':3.1,
    'outerLeafInner':37.9, 'innerLeafOuter':34.1, 'innerLeafInner':31.8,
    'forkHeight':31, 'pinCenterA':19, 'pinCenterB':26,
    'panelKeyWidth':4, 'panelHole':4.4, 'panelKeyLength':10.3,
    'panelHeadWidth':6.2, 'panelHeadHeight':0.8,
    'stackCenter':36.9, 'stackKeyWidth':3.6, 'stackKeyThickness':5.2,
    'stackHoleWidth':4, 'stackHoleThickness':5.6, 'stackHeadWidth':5.6,
    'stackHeadHeight':3, 'stackKeyLength':14.6,
    'lidHeight':8, 'hangerThickness':8, 'hangerBaseHeight':16,
    'glassInner':40.5, 'glassThickness':6, 'glassOpening':6.5,
    'glassTop':390, 'hookWall':16, 'hookTop':16, 'hookDrop':24,
    'hangerLegWidth':18, 'hangerDiagonalWidth':10,
    'handleThickness':8, 'handleHeight':48, 'handleRail':12,
    'centerX':29, 'centerY':0, 'baseZ':25,
    'lidKeyLength':32.6, 'handleKeyLength':21.6,
    'keeperLength':6.4, 'keeperWidth':4, 'keeperThickness':3,
    'braceExtra':2,
    'handleCenter':27, 'handleWidth':64, 'handleFootSeat':8,
    'handleHeadHeight':2, 'handleCrossbarWidth':16,
    'panelTipY':29.4, 'panelWindowCenter':1.6, 'panelKeeperLength':5.4,
}


def setup():
    if doc.getObject('RevisionParameters'):
        raise RuntimeError('La revisión ya existe: editarla, no recrearla')
    history=doc.addObject('App::DocumentObjectGroup','AntecedenteCADInicial')
    history.Label='Antecedente — CAD inicial oculto'
    for n in ['Module1','Module2','PrintableMasters','BastidorParameters']:
        o=doc.getObject(n); history.addObject(o);o.Visibility=False
    history.Visibility=False
    sheet=doc.addObject('Spreadsheet::Sheet','RevisionParameters')
    sheet.Label='Revisión funcional — cotas candidatas (mm)'
    sheet.set('A1','Parámetro');sheet.set('B1','Valor candidato')
    for i,(name,value) in enumerate(VALUES.items(),2):
        sheet.set('A'+str(i),name);sheet.set('B'+str(i),'='+str(value)+' mm')
        sheet.setAlias('B'+str(i),name)
    sheet.setColumnWidth('A',210);sheet.setColumnWidth('B',180)
    group=doc.addObject('App::DocumentObjectGroup','RevisionMasters')
    group.Label='Piezas funcionales — maestras para fabricación'
    doc.recompute()


def val(alias):
    return float(getattr(doc.RevisionParameters,alias).Value)


def expression(expr):
    for alias in sorted(VALUES,key=len,reverse=True):
        expr=re.sub(r'\b'+alias+r'\b','RevisionParameters.'+alias,expr)
    return expr


def number(expr):
    return float(eval(expr.replace(' mm','').replace('^','**'),{'__builtins__':{},'sqrt':math.sqrt},
                      {name:val(name) for name in VALUES}))


def rect(x0,y0,x1,y1):
    return [(x0,y0),(x1,y0),(x1,y1),(x0,y1)]


def sketch(body,name,polygons,z='0 mm',placement=None):
    o=doc.addObject('Sketcher::SketchObject',name);body.addObject(o)
    if placement:
        o.Placement=placement
    else:
        o.Placement.Base.z=number(z)
        o.setExpression('Placement.Base.z',expression(z))
    for poly in polygons:
        indices=[]
        for a,b in zip(poly,poly[1:]+poly[:1]):
            indices.append(o.addGeometry(Part.LineSegment(
                App.Vector(number(a[0]),number(a[1]),0),
                App.Vector(number(b[0]),number(b[1]),0)),False))
        for j,(i,point) in enumerate(zip(indices,poly)):
            o.addConstraint(Sketcher.Constraint('Coincident',i,2,indices[(j+1)%len(indices)],1))
            for axis,expr,line in [('X',point[0],-2),('Y',point[1],-1)]:
                v=number(expr)
                if abs(v)<1e-9:
                    o.addConstraint(Sketcher.Constraint('PointOnObject',i,1,line))
                else:
                    ci=o.addConstraint(Sketcher.Constraint('Distance'+axis,i,1,v))
                    o.renameConstraint(ci,'V'+str(i)+axis)
                    o.setExpression('Constraints['+str(ci)+']',expression(expr))
    return o


def feature(body,profile,name,length,pocket=False):
    o=body.newObject('PartDesign::Pocket' if pocket else 'PartDesign::Pad',name)
    o.Profile=profile;o.Length=number(length)
    o.setExpression('Length',expression(length));o.Refine=True
    doc.recompute()
    for item in body.Group:
        item.Visibility=False
    o.Visibility=True
    if o.Shape.isNull() or not o.Shape.isValid() or len(o.Shape.Solids)!=1:
        raise RuntimeError('Primer fallo en '+name)
    return o


def body(name,label,color):
    o=doc.addObject('PartDesign::Body',name);o.Label=label
    doc.RevisionMasters.addObject(o);o.ViewObject.ShapeColor=color
    return o


def ring(body,name,z,height):
    outer=rect('-outerWidth/2','-outerWidth/2','outerWidth/2','outerWidth/2')
    inner=rect('-outerWidth/2+frameWidth','-outerWidth/2+frameWidth',
               'outerWidth/2-frameWidth','outerWidth/2-frameWidth')
    feature(body,sketch(body,name+'Profile',[outer,inner],z),name+'Pad',height)
    blocks=[]
    for sx in [-1,1]:
        for sy in [-1,1]:
            x=str(sx)+'*cornerPadCenter';y=str(sy)+'*cornerPadCenter'
            blocks.append(rect(x+'-cornerPad/2',y+'-cornerPad/2',
                               x+'+cornerPad/2',y+'+cornerPad/2'))
    feature(body,sketch(body,name+'CornerProfile',blocks,z),name+'CornerPad',height)


def fork(body,name,z):
    leaves=[]
    for sign in [-1,1]:
        x=str(sign)+'*jointCenter'
        for lo,hi in [('-outerWidth/2','-outerLeafInner'),
                      ('-innerLeafOuter','-innerLeafInner'),
                      ('innerLeafInner','innerLeafOuter'),
                      ('outerLeafInner','outerWidth/2')]:
            leaves.append(rect(x+'-forkHalfWidth',lo,x+'+forkHalfWidth',hi))
            leaves.append(rect(lo,x+'-forkHalfWidth',hi,x+'+forkHalfWidth'))
    feature(body,sketch(body,name+'Profile',leaves,z),name+'Pad','forkHeight')


def horizontal_holes(body,name,top=False):
    for side in range(4):
        a='pinCenterA' if side%2==0 else 'pinCenterB'
        # Top-frame master has its ring at Z=forkHeight-3.
        center='forkHeight-'+a if top else a
        polys=[rect(str(sign)+'*jointCenter-panelHole/2',center+'-panelHole/2',
                    str(sign)+'*jointCenter+panelHole/2',center+'+panelHole/2') for sign in [-1,1]]
        rot=App.Rotation(App.Vector(0,0,1),side*90)
        pos=rot.multVec(App.Vector(0,-val('outerWidth')/2,0))
        place=App.Placement(pos,rot.multiply(App.Rotation(App.Vector(1,0,0),90)))
        feature(body,sketch(body,name+str(side)+'Profile',polys,placement=place),
                name+str(side)+'Pocket','outerWidth/2-innerLeafInner+0.3 mm',True)
        seats=[rect(str(sign)+'*jointCenter-panelHeadWidth/2-0.1 mm',
                    center+'-panelHeadWidth/2-0.1 mm',
                    str(sign)+'*jointCenter+panelHeadWidth/2+0.1 mm',
                    center+'+panelHeadWidth/2+0.1 mm') for sign in [-1,1]]
        feature(body,sketch(body,name+str(side)+'HeadProfile',seats,placement=place),
                name+str(side)+'HeadPocket','panelHeadHeight',True)


def vertical_holes(body,name,z,length,handle=False):
    polygons=[]
    for sx in [-1,1]:
        for sy in [-1,1]:
            x=str(sx)+'*stackCenter';y=str(sy)+'*stackCenter'
            polygons.append(rect(x+'-stackHoleWidth/2',y+'-stackHoleThickness/2',
                                 x+'+stackHoleWidth/2',y+'+stackHoleThickness/2'))
    if handle:
        for sy in [-1,1]:
            y=str(sy)+'*handleCenter'
            polygons.append(rect('-stackHoleWidth/2',y+'-stackHoleThickness/2',
                                 'stackHoleWidth/2',y+'+stackHoleThickness/2'))
    feature(body,sketch(body,name+'Profile',polygons,z),name+'Pocket',length,True)


def build_base():
    b=body('FunctionalBase','Base reforzada y horquillas',(0.15,0.4,0.8))
    ring(b,'FBPerimeter','0 mm','baseHeight')
    for axis in ['X','Y']:
        for sign in [-1,1]:
            c=str(sign)+'*columnPitch/2';span='outerWidth/2-frameWidth+0.1 mm'
            poly=rect(c+'-ribWidth/2','-('+span+')',c+'+ribWidth/2',span)
            if axis=='Y':poly=[(y,x) for x,y in poly]
            n='FBRib'+axis+str(sign).replace('-','N')
            feature(b,sketch(b,n+'Profile',[poly]),n+'Pad','seatHeight')
    for sx in [-1,1]:
        for sy in [-1,1]:
            for axis in ['X','Y']:
                x=str(sx)+'*columnPitch/2';y=str(sy)+'*columnPitch/2'
                ax='4.25 mm' if axis=='X' else '1 mm';ay='1 mm' if axis=='X' else '4.25 mm'
                n='FBMast'+str(sx).replace('-','N')+str(sy).replace('-','N')+axis
                feature(b,sketch(b,n+'Profile',[rect(x+'-'+ax,y+'-'+ay,x+'+'+ax,y+'+'+ay)],
                                 'seatHeight-0.2 mm'),n+'Pad','modulePitch-seatHeight-2 mm+0.2 mm')
    fork(b,'FBFork','0 mm')
    horizontal_holes(b,'FBKey')
    vertical_holes(b,'FBStack','baseHeight','baseHeight')
    relief=[]
    for sign in [-1,1]:
        lo,hi=('columnPitch/2-ribWidth/2-0.2 mm','17.15 mm') if sign>0 else (
               '-17.15 mm','-(columnPitch/2-ribWidth/2-0.2 mm)')
        relief.append(rect(lo,'-1.8 mm',hi,'1.8 mm'))
        relief.append(rect('-1.8 mm',lo,'1.8 mm',hi))
    feature(b,sketch(b,'FBHotelProfile',relief,'seatHeight'),'FBHotelPocket','seatHeight',True)
    panel_seats(b,'FBPanelSeats','baseHeight')
    b.Visibility=False;doc.save()


def build_panel(name,alias):
    b=body(name,'Panel X — patrón '+alias,(1.0,0.48,0.1))
    out=rect('-panelWidth/2','0 mm','panelWidth/2','panelHeight')
    inner=rect('-panelWidth/2+railWidth','railWidth',
               'panelWidth/2-railWidth','panelHeight-railWidth')
    feature(b,sketch(b,name+'FrameProfile',[out,inner]),name+'FramePad','panelThickness')
    # Las diagonales se unen en el cruce; la longitud libre se reduce.
    run='panelWidth-railWidth';rise='panelHeight-railWidth'
    ox='diagonalWidth/2*('+rise+')/sqrt(('+run+')^2+('+rise+')^2)'
    oy='diagonalWidth/2*('+run+')/sqrt(('+run+')^2+('+rise+')^2)'
    # Python usa **; FreeCAD usa ^. Se calculan los vértices por ambos lenguajes.
    def xy(e):return e.replace('^','**')
    a='-panelWidth/2+railWidth/2';c='panelWidth/2-railWidth/2'
    low='railWidth/2';high='panelHeight-railWidth/2'
    for i,reverse in enumerate([False,True]):
        x1,x2=(c,a) if reverse else (a,c)
        sy='-' if reverse else '+'
        ty='+' if reverse else '-'
        poly=[(x1+'-('+ox+')',low+sy+'('+oy+')'),
              (x2+'-('+ox+')',high+sy+'('+oy+')'),
              (x2+'+('+ox+')',high+ty+'('+oy+')'),
              (x1+'+('+ox+')',low+ty+'('+oy+')')]
        feature(b,sketch(b,name+'Diagonal'+str(i)+'Profile',[poly]),
                name+'Diagonal'+str(i)+'Pad','panelThickness')
    cuts=[]
    for sign in [-1,1]:
        lo,hi=('-panelWidth/2','-cornerPadCenter+cornerPad/2') if sign<0 else (
               'cornerPadCenter-cornerPad/2','panelWidth/2')
        cuts.extend([rect(lo,'0 mm',hi,'cornerNotch'),
                     rect(lo,'panelHeight-cornerNotch',hi,'panelHeight')])
    feature(b,sketch(b,name+'ReliefProfile',cuts,'panelThickness'),
            name+'ReliefPocket','panelThickness',True)
    holes=[]
    for sign in [-1,1]:
        x=str(sign)+'*jointCenter'
        for y in [alias+'-seatHeight','modulePitch-'+alias+'-seatHeight']:
            holes.append(rect(x+'-panelHole/2',y+'-panelHole/2',
                              x+'+panelHole/2',y+'+panelHole/2'))
    feature(b,sketch(b,name+'KeyProfile',holes,'panelThickness'),
            name+'KeyPocket','panelThickness',True)
    reinforce_panel(b)
    b.Visibility=False;doc.save()


def build_upper():
    b=body('FunctionalUpper','Marco superior — imprimir invertido',(0.15,0.4,0.8))
    ring(b,'FUPerimeter','forkHeight-3 mm','3 mm')
    fork(b,'FUFork','0 mm');horizontal_holes(b,'FUKey',True)
    vertical_holes(b,'FUStack','forkHeight','3 mm',False)
    panel_seats(b,'FUPanelSeats','forkHeight')
    b.Visibility=False;doc.save()


def make_key(name,width,thickness,length,head_width,head_height,slot_z,slot_y,slot_width,slot_height):
    b=body(name,name+' — pasador plano',(0.8,0.7,0.1))
    feature(b,sketch(b,name+'StemProfile',[rect('-'+width+'/2','0 mm',width+'/2',length)]),
            name+'StemPad',thickness)
    feature(b,sketch(b,name+'HeadProfile',[rect('-'+head_width+'/2',length,
                                                head_width+'/2',length+'+'+head_height)]),
            name+'HeadPad',thickness)
    # Ventana transversal normal a X; el eje longitudinal es Y.
    place=App.Placement(App.Vector(-number(width)/2,0,0),
                        App.Rotation(App.Vector(0,1,0),-90))
    # RX mapping: sketch X maps +Z, sketch Y maps +Y; normal -X.
    hole=rect(slot_z+'-'+slot_width+'/2',slot_y+'-'+slot_height+'/2',
              slot_z+'+'+slot_width+'/2',slot_y+'+'+slot_height+'/2')
    feature(b,sketch(b,name+'KeeperProfile',[hole],placement=place),
            name+'KeeperPocket',width,True)
    b.Visibility=False
    return b


def build_keys():
    make_key('PanelKey','panelKeyWidth','panelKeyWidth','panelKeyLength',
             'panelHeadWidth','panelHeadHeight','panelKeyWidth/2','panelWindowCenter','1.8 mm','1.4 mm')
    panel_key_tip(doc.PanelKey)
    for n,l in [('StackKey','stackKeyLength'),('LidKey','lidKeyLength'),('HandleKey','handleKeyLength')]:
        make_key(n,'stackKeyWidth','stackKeyThickness',l,'stackHeadWidth',
                 'handleHeadHeight' if n=='HandleKey' else 'stackHeadHeight',
                 'stackKeyThickness/2','3.5 mm','3.2 mm','4.2 mm')
    # Chavetas transversales: la ligera cuña solo retiene su posición de montaje.
    # Su migración en húmedo es un criterio obligatorio de ensayo.
    for name,L,W,T in [('PanelKeeper','panelKeeperLength','1.2 mm','1.6 mm'),
                       ('StructuralKeeper','keeperLength','keeperWidth','keeperThickness')]:
        b=body(name,name+' — chaveta transversal',(0.8,0.25,0.65))
        poly=[('-'+L+'/2','-'+W+'/2'),(L+'/2','-'+W+'/2'),
              (L+'/2',W+'/2-0.1 mm'),('-'+L+'/2',W+'/2+0.1 mm')]
        feature(b,sketch(b,name+'Profile',[poly]),name+'Pad',T)
        # Cabeza fuera de la ventana, más alta pero con misma anchura axial.
        feature(b,sketch(b,name+'HeadProfile',[rect('-'+L+'/2','-'+W+'/2',
                                                   '-'+L+'/2+'+('0.6 mm' if name=='PanelKeeper' else '0.8 mm'),W+'/2')]),
                name+'HeadPad',T+'+0.6 mm')
        b.Visibility=False
    doc.save()


def build_lid():
    b=body('LidFrame','Tapa — marco estructural abierto',(0.16,0.58,0.7))
    ring(b,'LFPerimeter','0 mm','lidHeight')
    add_handle_crossbars(b)
    vertical_holes(b,'LFKey','lidHeight','lidHeight',True)
    b.Visibility=False
    h=body('HangerPlate','Escuadra triangulada — impresión acostada',(0.3,0.65,0.35))
    gi='glassInner-(glassOpening-glassThickness)/2'
    go=gi+'+glassOpening';end=go+'+hookWall'
    height='glassTop-(baseZ+2*modulePitch+lidHeight)'
    # Perfil abierto de silla: apoyo nominal en canto Z=390 mm.
    poly=[('-outerWidth/2','0 mm'),(gi,'0 mm'),(gi,height),
          (go,height),(go,height+'-hookDrop'),(end,height+'-hookDrop'),
          (end,height+'+hookTop'),(gi+'-hangerLegWidth',height+'+hookTop'),
          (gi+'-hangerLegWidth','hangerBaseHeight'),('-outerWidth/2','hangerBaseHeight')]
    feature(h,sketch(h,'HPOutlineProfile',[poly]),'HPOutlinePad','hangerThickness')
    # Brace between left load corner and upper hanger leg.
    x1='-stackCenter';y1='hangerBaseHeight/2'
    x2=gi+'-hangerLegWidth/2';y2=height+'-5 mm'
    run='('+x2+')-('+x1+')';rise='('+y2+')-('+y1+')'
    ox='hangerDiagonalWidth/2*('+rise+')/sqrt(('+run+')^2+('+rise+')^2)'
    oy='hangerDiagonalWidth/2*('+run+')/sqrt(('+run+')^2+('+rise+')^2)'
    diag=[(x1+'-('+ox+')',y1+'+('+oy+')'),(x2+'-('+ox+')',y2+'+('+oy+')'),
          (x2+'+('+ox+')',y2+'-('+oy+')'),(x1+'+('+ox+')',y1+'-('+oy+')')]
    feature(h,sketch(h,'HPBraceProfile',[diag]),'HPBracePad','hangerThickness')
    # Llaves verticales atraviesan el travesaño inferior de la escuadra.
    place=App.Placement(App.Vector(0,val('hangerBaseHeight'),0),
                        App.Rotation(App.Vector(1,0,0),-90))
    holes=[rect(str(sign)+'*stackCenter-stackHoleWidth/2',
                '-hangerThickness/2-stackHoleThickness/2',
                str(sign)+'*stackCenter+stackHoleWidth/2',
                '-hangerThickness/2+stackHoleThickness/2') for sign in [-1,1]]
    feature(h,sketch(h,'HPKeyProfile',holes,placement=place),'HPKeyPocket','hangerBaseHeight',True)
    hanger_key_access(h)
    h.Visibility=False
    a=body('CenteredHandle','Asa centrada — imprimir acostada',(0.18,0.62,0.75))
    out=rect('-handleWidth/2','0 mm','handleWidth/2','handleHeight')
    inner=rect('-handleWidth/2+handleRail','handleRail',
               'handleWidth/2-handleRail','handleHeight-handleRail')
    feature(a,sketch(a,'CHProfile',[out,inner]),'CHPad','handleThickness')
    place=App.Placement(App.Vector(0,val('handleRail'),0),
                        App.Rotation(App.Vector(1,0,0),-90))
    holes=[rect(str(sign)+'*handleCenter-stackHoleThickness/2',
                '-handleThickness/2-stackHoleWidth/2',
                str(sign)+'*handleCenter+stackHoleThickness/2',
                '-handleThickness/2+stackHoleWidth/2') for sign in [-1,1]]
    feature(a,sketch(a,'CHKeyProfile',holes,placement=place),'CHKeyPocket','handleRail',True)
    handle_key_access(a)
    a.Visibility=False;doc.save()


def link(parent,source,name,position,rotation=None):
    o=doc.addObject('App::Link',name);o.setLink(source);parent.addObject(o)
    o.Placement=App.Placement(App.Vector(*position),rotation or App.Rotation())
    o.Visibility=True
    return o


def place_vertical_key(parent,source,name,x,y,z):
    return link(parent,source,name,(x,y+val('stackKeyThickness')/2,z),
                App.Rotation(App.Vector(1,0,0),90))


def place_structural_keeper(parent,name,x,y,z):
    if abs(x)>1:x+=(0.4 if x>0 else -0.4)
    return link(parent,doc.StructuralKeeper,name,(x,y+val('keeperThickness')/2,z),
                App.Rotation(App.Vector(1,0,0),90))


def assemble():
    for i in [1,2]:
        part=doc.addObject('App::Part','RevisionModule'+str(i));part.Label='Módulo funcional '+str(i)
        part.Placement.Base=App.Vector(val('centerX'),val('centerY'),val('baseZ')+(i-1)*val('modulePitch'))
        for axis,e in [('x','centerX'),('y','centerY'),('z','baseZ'+(' + modulePitch' if i==2 else ''))]:
            part.setExpression('Placement.Base.'+axis,expression(e))
        link(part,doc.FunctionalBase,'RBase'+str(i),(0,0,0))
        link(part,doc.FunctionalUpper,'RUpper'+str(i),(0,0,val('modulePitch')-val('forkHeight')))
        for side in range(4):
            rz=App.Rotation(App.Vector(0,0,1),side*90)
            pos=rz.multVec(App.Vector(0,-val('panelOffset'),val('seatHeight')))
            source=doc.PanelA if side%2==0 else doc.PanelB
            link(part,source,'RPanel'+str(i)+'S'+str(side),(pos.x,pos.y,pos.z),
                 rz.multiply(App.Rotation(App.Vector(1,0,0),90)))
            center=val('pinCenterA' if side%2==0 else 'pinCenterB')
            for level,z in [('B',center),('T',val('modulePitch')-center)]:
                for sign in [-1,1]:
                    suffix=str(i)+str(side)+level+str(sign).replace('-','N')
                    # Key native Y is longitudinal; rotate it onto the front normal.
                    pos=rz.multVec(App.Vector(sign*val('jointCenter')+val('panelKeyWidth')/2,
                                              -30,z))
                    rotation=rz.multiply(App.Rotation(App.Vector(0,1,0),90)).multiply(
                        App.Rotation(App.Vector(0,0,1),180))
                    # Explicit placement uses a basis: local X -> -Z, Y -> -Y, Z -> -X.
                    # Rotation below is obtained from three orthogonal basis vectors.
                    rotation=rz.multiply(App.Rotation(App.Vector(1,0,0),180))
                    # X -> +Z, Y -> -Y, Z -> +X; base Z starts at x-center-width/2.
                    pos=rz.multVec(App.Vector(sign*val('jointCenter'),-val('panelTipY'),z+val('panelKeyWidth')/2))
                    link(part,doc.PanelKey,'RPanelKey'+suffix,(pos.x,pos.y,pos.z),rotation)
                    # Pin cross-window normal local X maps Z: keeper axis is vertical.
                    # Keeper local X -> Z, local Y -> Y, local Z -> -X.
                    kr=rz.multiply(App.Rotation(App.Vector(1,0,0),180))
                    kp=rz.multVec(App.Vector(sign*val('jointCenter'),-31,z+0.8))
                    link(part,doc.PanelKeeper,'RPanelKeeper'+suffix,(kp.x,kp.y,kp.z),kr)
    joint=doc.addObject('App::Part','StackingLocks');joint.Label='Bloqueo entre módulos'
    joint.Placement.Base=App.Vector(val('centerX'),val('centerY'),val('baseZ'))
    for sx in [-1,1]:
        for sy in [-1,1]:
            suffix=str(sx).replace('-','N')+str(sy).replace('-','N')
            x=sx*val('stackCenter');y=sy*val('stackCenter')
            place_vertical_key(joint,doc.StackKey,'RStackKey'+suffix,x,y,val('modulePitch')-8.6)
            place_structural_keeper(joint,'RStackKeeper'+suffix,x,y,val('modulePitch')-5.1)
    lid=doc.addObject('App::Part','Suspension');lid.Label='Tapa, escuadras y asa'
    lid.Placement.Base=App.Vector(val('centerX'),val('centerY'),val('baseZ')+2*val('modulePitch'))
    link(lid,doc.LidFrame,'RLidFrame',(0,0,0))
    for sy in [-1,1]:
        y=sy*val('stackCenter')
        link(lid,doc.HangerPlate,'RHanger'+str(sy).replace('-','N'),
             (0,y+val('hangerThickness')/2,val('lidHeight')),
             App.Rotation(App.Vector(1,0,0),90))
        for sx in [-1,1]:
            x=sx*val('stackCenter');suffix=str(sx).replace('-','N')+str(sy).replace('-','N')
            place_vertical_key(lid,doc.LidKey,'RLidKey'+suffix,x,y,-8.6)
            place_structural_keeper(lid,'RLidKeeper'+suffix,x,y,-5.1)
    # Handle plane: local X -> global Y, local Y -> global Z, local Z -> global X.
    hr=App.Rotation(App.Vector(0,1,0),App.Vector(0,0,1),App.Vector(1,0,0),'ZXY')
    link(lid,doc.CenteredHandle,'RHandle',
         (-val('handleThickness')/2,0,val('lidHeight')),hr)
    for sy in [-1,1]:
        y=sy*val('handleCenter');suffix=str(sy).replace('-','N')
        place_vertical_key(lid,doc.HandleKey,'RHandleKey'+suffix,0,y,-5.6)
        place_structural_keeper(lid,'RHandleKeeper'+suffix,0,y,-2.1)
    doc.recompute()
    doc.RevisionMasters.Visibility=False
    Gui.activeDocument().activeView().viewAxonometric();Gui.activeDocument().activeView().fitAll()
    doc.save()


def finish_view():
    doc.RevisionMasters.Visibility=False
    doc.AntecedenteCADInicial.Visibility=False
    doc.recompute();doc.save()
    print('MAESTROS',[(o.Name,o.Shape.isValid(),len(o.Shape.Solids),o.Shape.Volume)
                      for o in doc.RevisionMasters.Group])


def clipped(poly,axis,bound,keep_less):
    """Recorte simbólico para nervios sin invadir las horquillas de esquina."""
    result=[]
    for a,b in zip(poly,poly[1:]+poly[:1]):
        av,bv=number(a[axis]),number(b[axis]);limit=number(bound)
        ain=av<=limit+1e-9 if keep_less else av>=limit-1e-9
        bin=bv<=limit+1e-9 if keep_less else bv>=limit-1e-9
        if ain:result.append(a)
        if ain!=bin:
            other=1-axis
            value='('+a[other]+')+(('+b[other]+')-('+a[other]+'))*(('+bound+')-('+a[axis]+'))/(('+b[axis]+')-('+a[axis]+'))'
            result.append((bound,value) if axis==0 else (value,bound))
    return result


def reinforce_panel(b):
    run='panelWidth-railWidth';rise='panelHeight-railWidth'
    ox='diagonalWidth/2*('+rise+')/sqrt(('+run+')^2+('+rise+')^2)'
    oy='diagonalWidth/2*('+run+')/sqrt(('+run+')^2+('+rise+')^2)'
    a='-panelWidth/2+railWidth/2';c='panelWidth/2-railWidth/2'
    low='railWidth/2';high='panelHeight-railWidth/2'
    for i,reverse in enumerate([False,True]):
        x1,x2=(c,a) if reverse else (a,c);sy='-' if reverse else '+';ty='+' if reverse else '-'
        poly=[(x1+'-('+ox+')',low+sy+'('+oy+')'),(x2+'-('+ox+')',high+sy+'('+oy+')'),
              (x2+'+('+ox+')',high+ty+'('+oy+')'),(x1+'+('+ox+')',low+ty+'('+oy+')')]
        limit='cornerPadCenter-cornerPad/2-4 mm'
        for axis,bound,less in [(0,limit,True),(0,'-('+limit+')',False),
                                (1,'railWidth',False),(1,'panelHeight-railWidth',True)]:
            poly=clipped(poly,axis,bound,less)
        feature(b,sketch(b,b.Name+'Rib'+str(i)+'Profile',[poly],'panelThickness'),
                b.Name+'Rib'+str(i)+'Pad','braceExtra')


def build_coupons():
    group=doc.addObject('App::DocumentObjectGroup','FitCoupons')
    group.Label='Probetas — fabricar antes del conjunto'
    b=body('ForkCoupon','Probeta de horquilla — orientación vertical',(0.2,0.5,0.8))
    feature(b,sketch(b,'FCBaseProfile',[rect('-5 mm','-4.35 mm','5 mm','4.35 mm')]),
            'FCBasePad','baseHeight')
    leaves=[rect('-forkHalfWidth','-4.35 mm','forkHalfWidth','-1.75 mm'),
            rect('-forkHalfWidth','2.05 mm','forkHalfWidth','4.35 mm')]
    feature(b,sketch(b,'FCForkProfile',leaves,'baseHeight'),'FCForkPad','23 mm')
    place=App.Placement(App.Vector(0,-4.35,0),App.Rotation(App.Vector(1,0,0),90))
    feature(b,sketch(b,'FCKeyProfile',[rect('-panelHole/2','pinCenterA-panelHole/2',
                                           'panelHole/2','pinCenterA+panelHole/2')],placement=place),
            'FCKeyPocket','8.7 mm',True)
    feature(b,sketch(b,'FCHeadProfile',[rect('-panelHeadWidth/2-0.1 mm',
                'pinCenterA-panelHeadWidth/2-0.1 mm','panelHeadWidth/2+0.1 mm',
                'pinCenterA+panelHeadWidth/2+0.1 mm')],placement=place),
            'FCHeadPocket','panelHeadHeight',True)
    group.addObject(b);b.Visibility=False
    p=body('TongueCoupon','Probeta de panel — imprimir acostada',(1.0,0.48,0.1))
    feature(p,sketch(p,'TCProfile',[rect('-5 mm','0 mm','5 mm','23 mm')]),'TCPad','panelThickness')
    feature(p,sketch(p,'TCKeyProfile',[rect('-panelHole/2','pinCenterA-baseHeight-panelHole/2',
                'panelHole/2','pinCenterA-baseHeight+panelHole/2')],'panelThickness'),
            'TCKeyPocket','panelThickness',True)
    group.addObject(p);p.Visibility=False
    for name,height in [('StackUpperCoupon','baseHeight'),('StackLowerCoupon','3 mm')]:
        c=body(name,'Probeta de esquina '+height,(0.2,0.5,0.8))
        feature(c,sketch(c,name+'Profile',[rect('-5 mm','-5 mm','5 mm','5 mm')]),name+'Pad',height)
        x='stackCenter-cornerPadCenter'
        poly=rect(x+'-stackHoleWidth/2',x+'-stackHoleThickness/2',
                  x+'+stackHoleWidth/2',x+'+stackHoleThickness/2')
        feature(c,sketch(c,name+'KeyProfile',[poly],height),name+'Pocket',height,True)
        group.addObject(c);c.Visibility=False
    g=body('GlassCoupon','Probeta de silla 6,5 mm — acostada',(0.3,0.65,0.35))
    outer=rect('0 mm','0 mm','hangerLegWidth+glassOpening+hookWall','hookDrop+hookTop')
    feature(g,sketch(g,'GCProfile',[outer]),'GCPad','hangerThickness')
    slot=rect('hangerLegWidth','0 mm','hangerLegWidth+glassOpening','hookDrop')
    feature(g,sketch(g,'GCSlotProfile',[slot],'hangerThickness'),'GCSlotPocket','hangerThickness',True)
    group.addObject(g);g.Visibility=False
    # Las probetas son también maestras exportables, pero no están en el montaje.
    group.Visibility=False;doc.RevisionMasters.Visibility=False;doc.save()


def build_load_coupons():
    for name,width,thickness,height,hole_width,hole_thickness in [
        ('HangerJointCoupon','12 mm','hangerThickness','hangerBaseHeight','stackHoleWidth','stackHoleThickness'),
        ('HandleJointCoupon','12 mm','handleThickness','handleRail','stackHoleThickness','stackHoleWidth')]:
        b=body(name,name+' — orientación idéntica a la pieza final',(0.2,0.6,0.65))
        feature(b,sketch(b,name+'Profile',[rect('-'+width+'/2','0 mm',width+'/2',height)]),
                name+'Pad',thickness)
        place=App.Placement(App.Vector(0,number(height),0),App.Rotation(App.Vector(1,0,0),-90))
        poly=rect('-'+hole_width+'/2','-'+thickness+'/2-'+hole_thickness+'/2',
                  hole_width+'/2','-'+thickness+'/2+'+hole_thickness+'/2')
        feature(b,sketch(b,name+'KeyProfile',[poly],placement=place),name+'Pocket',height,True)
        doc.FitCoupons.addObject(b);b.Visibility=False
    b=body('SeatRibCoupon','Nervio de asiento — prueba de flexión',(0.2,0.5,0.8))
    span='outerWidth/2-frameWidth'
    feature(b,sketch(b,'SRProfile',[rect('-ribWidth/2','-('+span+')','ribWidth/2',span)]),
            'SRPad','seatHeight')
    poly=rect('-ribWidth/2','-1.8 mm','17.15 mm-columnPitch/2','1.8 mm')
    feature(b,sketch(b,'SRHotelProfile',[poly],'seatHeight'),'SRHotelPocket','seatHeight',True)
    doc.FitCoupons.addObject(b);b.Visibility=False
    doc.FitCoupons.Visibility=False;doc.RevisionMasters.Visibility=False;doc.save()


def build_fork_b_coupon():
    doc.FCForkPad.setExpression('Length',expression('forkHeight-baseHeight'))
    b=body('ForkCouponB','Horquilla B — extremo con menor ligamento',(0.2,0.5,0.8))
    feature(b,sketch(b,'FCBBaseProfile',[rect('-5 mm','-4.35 mm','5 mm','4.35 mm')]),
            'FCBBasePad','baseHeight')
    leaves=[rect('-forkHalfWidth','-4.35 mm','forkHalfWidth','-1.75 mm'),
            rect('-forkHalfWidth','2.05 mm','forkHalfWidth','4.35 mm')]
    feature(b,sketch(b,'FCBForkProfile',leaves,'baseHeight'),
            'FCBForkPad','forkHeight-baseHeight')
    place=App.Placement(App.Vector(0,-4.35,0),App.Rotation(App.Vector(1,0,0),90))
    hole=rect('-panelHole/2','pinCenterB-panelHole/2','panelHole/2','pinCenterB+panelHole/2')
    feature(b,sketch(b,'FCBKeyProfile',[hole],placement=place),'FCBKeyPocket','8.7 mm',True)
    head=rect('-panelHeadWidth/2-0.1 mm','pinCenterB-panelHeadWidth/2-0.1 mm',
              'panelHeadWidth/2+0.1 mm','pinCenterB+panelHeadWidth/2+0.1 mm')
    feature(b,sketch(b,'FCBHeadProfile',[head],placement=place),'FCBHeadPocket','panelHeadHeight',True)
    doc.FitCoupons.addObject(b);b.Visibility=False
    doc.FitCoupons.Visibility=False;doc.RevisionMasters.Visibility=False;doc.save()


def panel_seats(b,name,z):
    s='cornerPadCenter-cornerPad/2+0.2 mm'
    cuts=[rect('-('+s+')','-panelOffset-panelThickness-0.2 mm',s,'-panelOffset+0.2 mm'),
          rect('-('+s+')','panelOffset-0.2 mm',s,'panelOffset+panelThickness+0.2 mm'),
          rect('-panelOffset-panelThickness-0.2 mm','-('+s+')','-panelOffset+0.2 mm',s),
          rect('panelOffset-0.2 mm','-('+s+')','panelOffset+panelThickness+0.2 mm',s)]
    feature(b,sketch(b,name+'Profile',cuts,z),name+'Pocket','3 mm',True)


def add_handle_crossbars(b):
    cuts=[]
    for sign in [-1,1]:
        c=str(sign)+'*handleCenter'
        cuts.append(rect('-outerWidth/2+frameWidth-0.1 mm',c+'-handleCrossbarWidth/2',
                         'outerWidth/2-frameWidth+0.1 mm',c+'+handleCrossbarWidth/2'))
    feature(b,sketch(b,'LFHandleBeamsProfile',cuts),'LFHandleBeamsPad','lidHeight')


def hanger_key_access(b):
    slot=rect('stackCenter-stackHeadWidth/2-0.2 mm','hangerBaseHeight',
              'glassInner-(glassOpening-glassThickness)/2+0.2 mm',
              'glassTop-(baseZ+2*modulePitch+lidHeight)')
    feature(b,sketch(b,'HPAccessProfile',[slot],'hangerThickness'),
            'HPAccessPocket','hangerThickness',True)


def handle_key_access(b):
    slots=[]
    for sign in [-1,1]:
        lo,hi=('-handleWidth/2-0.2 mm','-handleCenter+stackHeadWidth/2+0.2 mm') if sign<0 else (
               'handleCenter-stackHeadWidth/2-0.2 mm','handleWidth/2+0.2 mm')
        slots.append(rect(lo,'handleFootSeat',hi,'handleHeight'))
    feature(b,sketch(b,'CHAccessProfile',slots,'handleThickness'),
            'CHAccessPocket','handleThickness',True)


def panel_key_tip(b):
    w='panelKeyWidth/2'
    left=[('-'+w,'0 mm'),('-'+w+'+0.4 mm','0 mm'),('-'+w,'2.3 mm')]
    right=[(w,'0 mm'),(w+'-0.4 mm','0 mm'),(w,'2.3 mm')]
    feature(b,sketch(b,'PKTipProfile',[left,right],'panelKeyWidth'),
            'PKTipPocket','panelKeyWidth',True)
