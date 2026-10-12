"""CAD nativo candidato M4. Ejecutar por bloques en FreeCAD GUI, nunca dos veces."""
import FreeCAD as App, FreeCADGui as Gui, Part, Sketcher
import math,re,json,ast
from pathlib import Path
ROOT=Path(__file__).resolve().parent
P={'outer':81,'rim':6,'baseHeight':6,'seat':3,'rib':12,'pitch':36.5,'module':150,
'panelWidth':68.2,'panelHeight':143.8,'panelT':2.4,'rail':8,'diag':8,'panelOffset':34.3,
'bossOuter':34.1,'bossT':3.2,'bossWidth':15,'bossHeight':18,'lowerBolt':13,'upperBolt':142,
'upperHeight':13,'corner':35.5,'cornerWidth':10,'cornerCap':5,'hole':4.4,
'cornerRelief':16,'cornerStrip':10,'lidT':6,'crossbar':20,'handleCenter':26,
'hangerT':6,'hangerFootT':8,'hangerBeam':14,'leg':18,'hangerDiag':6,
'glassInner':40.5,'glassThickness':6,'glassOpening':6.5,'hookWall':16,'hookTop':16,'drop':24,
'handleWidth':62,'handleHeight':48,'handleRail':14,'handleT':4,'handleFootT':8,'handleSeat':8,
'washerT':0.8,'washerOD':9,'washerID':4.3,'nutSW':7,'nutH':3.2,'headH':2.8,'boltD':4,
'centerX':29,'baseZ':25,'glassTop':390,'handleRise':0}

def setup():
 global d
 if 'BiobolasAtornillado' in App.listDocuments():raise RuntimeError('Documento ya creado')
 src=App.getDocument('SoporteBiobolasBastidor')
 d=App.newDocument('BiobolasAtornillado');d.Label='Biobolas — simplificado con tornillería M4'
 refs=d.addObject('App::DocumentObjectGroup','Referencias')
 for n in ['ContextoC1','Array','Array001','HotelPodsReference','UpperHotelPodsReference']:
  o=d.copyObject(src.getObject(n),True);refs.addObject(o)
 for o in d.Objects:
  if o.TypeId=='Sketcher::SketchObject':o.Visibility=False
 sheet=d.addObject('Spreadsheet::Sheet','Parametros')
 for i,(k,v) in enumerate(P.items(),2):sheet.set('A'+str(i),k);sheet.set('B'+str(i),str(v)+' mm');sheet.setAlias('B'+str(i),k)
 sheet.setColumnWidth('A',180);sheet.setColumnWidth('B',120)
 d.addObject('App::DocumentObjectGroup','Maestras');d.addObject('App::DocumentObjectGroup','TornilleriaReferencia')
 d.recompute();restore_ball_references(src);d.saveAs(str(ROOT/'soporte-biobolas-atornillado.FCStd'))

def ex(s):
 def walk(n):
  if isinstance(n,ast.Constant):return str(n.value),0
  if isinstance(n,ast.Name):return ('Parametros.'+n.id,1) if n.id in P else (n.id,0)
  if isinstance(n,ast.Attribute):return ast.unparse(n),1
  if isinstance(n,ast.UnaryOp):
   a,u=walk(n.operand);return ('-' if isinstance(n.op,ast.USub) else '+')+'('+a+')',u
  if isinstance(n,ast.Call):
   a,u=walk(n.args[0]);return 'sqrt('+a+')',u/2
  a,u=walk(n.left);b,w=walk(n.right)
  if isinstance(n.op,(ast.Add,ast.Sub)):
   if u!=w:
    if u==0:a='('+a+') * (1 mm)';u=w
    elif w==0:b='('+b+') * (1 mm)';w=u
    else:raise ValueError('Dimensiones incompatibles')
   return '('+a+(' + ' if isinstance(n.op,ast.Add) else ' - ')+b+')',u
  if isinstance(n.op,ast.Mult):return '('+a+' * '+b+')',u+w
  if isinstance(n.op,ast.Div):return '('+a+' / '+b+')',u-w
  if isinstance(n.op,ast.Pow):return '('+a+' ^ '+b+')',u*float(ast.literal_eval(n.right))
  raise ValueError(n)
 a,u=walk(ast.parse(str(s).replace('^','**'),mode='eval').body)
 return a+' * (1 mm)' if u==0 else a

def v(s):return float(eval(str(s),{'__builtins__':{},'sqrt':math.sqrt},P))
def rect(a,b,c,e):return [(str(a),str(b)),(str(c),str(b)),(str(c),str(e)),(str(a),str(e))]
def sk(b,n,polys,z='0',placement=None,circles=None):
 s=d.addObject('Sketcher::SketchObject',n);b.addObject(s)
 if placement:s.Placement=placement
 else:s.Placement.Base.z=v(z);s.setExpression('Placement.Base.z',ex(z))
 for poly in polys:
  for a,c in zip(poly,poly[1:]+poly[:1]):
   i=s.addGeometry(Part.LineSegment(App.Vector(v(a[0]),v(a[1]),0),App.Vector(v(c[0]),v(c[1]),0)),False)
   # Cuatro coordenadas fijadas mediante expresiones, sin referencias topológicas.
   for point,e in [(1,a),(2,c)]:
    for axis,j in [('X',0),('Y',1)]:
     q=v(e[j])
     if abs(q)<1e-9:s.addConstraint(Sketcher.Constraint('PointOnObject',i,point,-2 if axis=='X' else -1))
     else:
      ci=s.addConstraint(Sketcher.Constraint('Distance'+axis,i,point,q));s.setExpression('Constraints['+str(ci)+']',ex(e[j]))
 if circles:
  for x,y,r in circles:
   i=s.addGeometry(Part.Circle(App.Vector(v(x),v(y),0),App.Vector(0,0,1),v(r)),False)
   for axis,q in [('X',x),('Y',y)]:
    if abs(v(q))<1e-9:s.addConstraint(Sketcher.Constraint('PointOnObject',i,3,-2 if axis=='X' else -1))
    else:
     ci=s.addConstraint(Sketcher.Constraint('Distance'+axis,i,3,v(q)));s.setExpression('Constraints['+str(ci)+']',ex(q))
   ci=s.addConstraint(Sketcher.Constraint('Radius',i,v(r)));s.setExpression('Constraints['+str(ci)+']',ex(r))
 return s

def feat(b,n,s,L,pocket=False):
 f=b.newObject('PartDesign::Pocket' if pocket else 'PartDesign::Pad',n);f.Profile=s;f.Length=v(L);f.setExpression('Length',ex(L));f.Refine=True
 d.recompute()
 if f.Shape.isNull() or not f.Shape.isValid() or len(f.Shape.Solids)!=1:raise RuntimeError(n+' shape error '+str(f.State))
 for o in b.Group:o.Visibility=False
 f.Visibility=True
 return f

def body(n,label,color,hardware=False):
 b=d.addObject('PartDesign::Body',n);b.Label=label;(d.TornilleriaReferencia if hardware else d.Maestras).addObject(b);b.ViewObject.ShapeColor=color;return b

def ring(b,n,H):
 ringZ='upperHeight-seat' if n=='MarcoAro' else '0'
 ringH='seat' if n=='MarcoAro' else H
 feat(b,n+'Pad',sk(b,n+'Perfil',[rect('-outer/2','-outer/2','outer/2','outer/2'),rect('-outer/2+rim','-outer/2+rim','outer/2-rim','outer/2-rim')],ringZ),ringH)
 polys=[]
 for a in [-1,1]:
  for c in [-1,1]:polys.append(rect(f'{a}*corner-cornerWidth/2',f'{c}*corner-cornerWidth/2',f'{a}*corner+cornerWidth/2',f'{c}*corner+cornerWidth/2'))
 feat(b,n+'EsquinasPad',sk(b,n+'EsquinasPerfil',polys,'upperHeight-cornerCap' if n=='MarcoAro' else '0'),'cornerCap' if n=='MarcoAro' else H)

def pads4(inner,outer,width):
 out=[]
 for side in range(4):
  poly=rect('-('+width+')/2','-('+outer+')','('+width+')/2','-('+inner+')')
  for k in range(side):poly=[('-('+y+')',x) for x,y in poly]
  out.append(poly)
 return out

def central_bores(b,n,z):
 for side in range(4):
  r=App.Rotation(App.Vector(0,0,1),side*90);pos=r.multVec(App.Vector(0,-P['bossOuter'],0))
  place=App.Placement(pos,r.multiply(App.Rotation(App.Vector(1,0,0),90)))
  feat(b,n+str(side)+'Pocket',sk(b,n+str(side)+'Perfil',[rect('-hole/2',z+'-hole/2','hole/2',z+'+hole/2')],placement=place),'bossT',True)

def corner_bores(b,n,z,H,handle=False):
 holes=[(f'{a}*corner',f'{c}*corner','hole/2') for a in [-1,1] for c in [-1,1]]
 if handle:holes += [('0',f'{a}*handleCenter','hole/2') for a in [-1,1]]
 feat(b,n+'Pocket',sk(b,n+'Perfil',[],z,circles=holes),H,True)

def build_base():
 b=d.getObject('Base')
 if b is None:
  b=body('Base','Base y guías centrales conservadas',(0.2,0.45,0.8));ring(b,'BaseAro','baseHeight')
 for axis in range(2):
  if d.getObject("BaseNervio"+str(axis)+"Pad"):continue
  polys=[]
  for sign in [-1,1]:
   poly=rect(f'{sign}*pitch/2-rib/2','-outer/2+rim-0.1',f'{sign}*pitch/2+rib/2','outer/2-rim+0.1')
   if axis:poly=[(y,x) for x,y in poly]
   polys.append(poly)
  feat(b,'BaseNervio'+str(axis)+'Pad',sk(b,'BaseNervio'+str(axis)+'Perfil',polys),'seat')
 feat(b,'BaseApoyosPad',sk(b,'BaseApoyosPerfil',pads4('bossOuter-bossT','outer/2','bossWidth')),'seat')
 feat(b,'BaseBossPad',sk(b,'BaseBossPerfil',pads4('bossOuter-bossT','bossOuter','bossWidth'),'seat'),'bossHeight-seat')
 for axis in range(2):
  polys=[]
  for sx in [-1,1]:
   for sy in [-1,1]:
    x=f'{sx}*pitch/2';y=f'{sy}*pitch/2';a='4.25' if axis==0 else '1';c='1' if axis==0 else '4.25'
    polys.append(rect(x+'-'+a,y+'-'+c,x+'+'+a,y+'+'+c))
  feat(b,'Guia'+str(axis)+'Pad',sk(b,'Guia'+str(axis)+'Perfil',polys,'seat'),'module-seat-2')
 relief=[]
 for sg in [-1,1]:
  lo,hi=('pitch/2-rib/2-0.2','17.15') if sg>0 else ('-17.15','-(pitch/2-rib/2-0.2)')
  relief.extend([rect(lo,'-1.8',hi,'1.8'),rect('-1.8',lo,'1.8',hi)])
 feat(b,'HotelPocket',sk(b,'HotelPerfil',relief,'seat'),'seat',True)
 feat(b,'BaseGuiadoPocket',sk(b,'BaseGuiadoPerfil',pads4('panelOffset-0.2','panelOffset+panelT+0.2','panelWidth+0.4'),'baseHeight'),'baseHeight-seat',True)
 central_bores(b,'BaseTornillo','lowerBolt');corner_bores(b,'BaseApilado','baseHeight','baseHeight')
 b.Visibility=False;d.save()

def build_panel():
 b=body('Panel','Panel único X de 2,4 mm',(1.0,0.55,0.18))
 feat(b,'PanelAroPad',sk(b,'PanelAroPerfil',[rect('-panelWidth/2','0','panelWidth/2','panelHeight'),rect('-panelWidth/2+rail','rail','panelWidth/2-rail','panelHeight-rail')]),'panelT')
 for i,rev in enumerate([False,True]):
  run='panelWidth-rail';rise='panelHeight-rail';L='sqrt(('+run+')**2+('+rise+')**2)';ox='diag/2*('+rise+')/'+L;oy='diag/2*('+run+')/'+L
  x1,x2=('panelWidth/2-rail/2','-panelWidth/2+rail/2') if rev else ('-panelWidth/2+rail/2','panelWidth/2-rail/2')
  low='rail/2';high='panelHeight-rail/2';sg='-' if rev else '+';tg='+' if rev else '-'
  poly=[(x1+'-('+ox+')',low+sg+'('+oy+')'),(x2+'-('+ox+')',high+sg+'('+oy+')'),(x2+'+('+ox+')',high+tg+'('+oy+')'),(x1+'+('+ox+')',low+tg+'('+oy+')')]
  feat(b,'Diagonal'+str(i)+'Pad',sk(b,'Diagonal'+str(i)+'Perfil',[poly]),'panelT')
 polys=[]
 for y in ['0','panelHeight-12']:
  polys.append(rect('-bossWidth/2',y,'bossWidth/2',y+'+12'))
 feat(b,'PanelOrejetasPad',sk(b,'PanelOrejetasPerfil',polys),'panelT')
 cuts=[]
 for a,c in [('-panelWidth/2','-panelWidth/2+cornerStrip'),('panelWidth/2-cornerStrip','panelWidth/2')]:
  cuts.extend([rect(a,'0',c,'cornerRelief'),rect(a,'panelHeight-cornerRelief',c,'panelHeight')])
 feat(b,'PanelEsquinasPocket',sk(b,'PanelEsquinasPerfil',cuts,'panelT'),'panelT',True)
 feat(b,'PanelTornilloPocket',sk(b,'PanelTornilloPerfil',[],'panelT',circles=[('0','lowerBolt-seat','hole/2'),('0','upperBolt-seat','hole/2')]),'panelT',True)
 b.Visibility=False;d.save()

def build_upper():
 b=body('Marco','Marco superior guiado',(0.2,0.45,0.8));ring(b,'MarcoAro','upperHeight')
 feat(b,'MarcoApoyosPad',sk(b,'MarcoApoyosPerfil',pads4('bossOuter-bossT','outer/2','bossWidth'),'upperHeight-seat'),'seat')
 feat(b,'MarcoBossPad',sk(b,'MarcoBossPerfil',pads4('bossOuter-bossT','bossOuter','bossWidth')),'upperHeight')
 feat(b,'MarcoGuiadoPocket',sk(b,'MarcoGuiadoPerfil',pads4('panelOffset-0.2','panelOffset+panelT+0.2','panelWidth+0.4'),'upperHeight-seat'),'upperHeight-seat',True)
 cuts=[]
 for a in [-1,1]:
  for c in [-1,1]:cuts.append(rect(f'{a}*corner-cornerWidth/2',f'{c}*corner-cornerWidth/2',f'{a}*corner+cornerWidth/2',f'{c}*corner+cornerWidth/2'))
 feat(b,'MarcoTuercasPocket',sk(b,'MarcoTuercasPerfil',cuts,'upperHeight-cornerCap'),'upperHeight-cornerCap',True)
 central_bores(b,'MarcoTornillo','upperBolt-module+upperHeight');corner_bores(b,'MarcoApilado','upperHeight','upperHeight')
 add_upper_guides(b)
 b.Visibility=False;d.save()

def build_lid():
 b=body('Tapa','Tapa abierta de 6 mm',(0.1,0.65,0.7));ring(b,'TapaAro','lidT')
 polys=[rect('-outer/2+rim-0.1',f'{a}*handleCenter-crossbar/2','outer/2-rim+0.1',f'{a}*handleCenter+crossbar/2') for a in [-1,1]]
 feat(b,'TapaTravesanosPad',sk(b,'TapaTravesanosPerfil',polys,'handleRise'),'lidT');corner_bores(b,'TapaTornillos','lidT+handleRise','lidT+handleRise',True);b.Visibility=False
 h=body('Escuadra','Escuadra 6 mm con pie local de 8 mm',(0.3,0.7,0.35))
 gi='glassInner-(glassOpening-glassThickness)/2';go='('+gi+')+glassOpening';end='('+go+')+hookWall';H='glassTop-baseZ-2*module-lidT'
 poly=[('-outer/2','0'),(gi,'0'),(gi,H),(go,H),(go,H+'-drop'),(end,H+'-drop'),(end,H+'+hookTop'),(gi+'-leg',H+'+hookTop'),(gi+'-leg','hangerBeam'),('-outer/2','hangerBeam')]
 feat(h,'EscuadraPad',sk(h,'EscuadraPerfil',[poly]),'hangerT')
 x1='-corner';y1='hangerBeam/2';x2=gi+'-leg/2';y2=H+'-5';run='('+x2+')-('+x1+')';rise='('+y2+')-('+y1+')';L='sqrt(('+run+')**2+('+rise+')**2)';ox='hangerDiag/2*('+rise+')/'+L;oy='hangerDiag/2*('+run+')/'+L
 poly=[(x1+'-('+ox+')',y1+'+('+oy+')'),(x2+'-('+ox+')',y2+'+('+oy+')'),(x2+'+('+ox+')',y2+'-('+oy+')'),(x1+'+('+ox+')',y1+'-('+oy+')')]
 feat(h,'EscuadraDiagonalPad',sk(h,'EscuadraDiagonalPerfil',[poly]),'hangerT')
 feat(h,'EscuadraPiePad',sk(h,'EscuadraPiePerfil',[rect('-outer/2','0',gi,'hangerBeam')]),'hangerFootT')
 # Taladros verticales, en cara de datum independiente.
 place=App.Placement(App.Vector(0,P['hangerBeam'],0),App.Rotation(App.Vector(1,0,0),-90))
 feat(h,'EscuadraTaladrosPocket',sk(h,'EscuadraTaladrosPerfil',[],placement=place,circles=[(f'{a}*corner','-hangerFootT/2','hole/2') for a in [-1,1]]),'hangerBeam',True)
 feat(h,'EscuadraAccesoPocket',sk(h,'EscuadraAccesoPerfil',[rect('corner-washerOD/2-0.2','hangerBeam','outer/2+0.2',H+'-5')],'hangerFootT'),'hangerFootT',True)
 h.Visibility=False
 a=body('Asa','Asa centrada 4 mm y pie local de 8 mm',(0.1,0.65,0.7))
 feat(a,'AsaPad',sk(a,'AsaPerfil',[rect('-handleWidth/2','0','handleWidth/2','handleHeight'),rect('-handleWidth/2+handleRail','handleRail','handleWidth/2-handleRail','handleHeight-handleRail')]),'handleT')
 feat(a,'AsaPiePad',sk(a,'AsaPiePerfil',[rect('-handleWidth/2','0','handleWidth/2','handleSeat')],'0'),'handleFootT')
 place=App.Placement(App.Vector(0,P['handleSeat'],0),App.Rotation(App.Vector(1,0,0),-90))
 feat(a,'AsaTaladrosPocket',sk(a,'AsaTaladrosPerfil',[],placement=place,circles=[(f'{sg}*handleCenter','-handleFootT/2','hole/2') for sg in [-1,1]]),'handleSeat',True)
 cuts=[rect('handleCenter-washerOD/2-0.2','handleSeat','handleWidth/2+0.2','handleHeight'),rect('-handleWidth/2-0.2','handleSeat','-handleCenter+washerOD/2+0.2','handleHeight')]
 feat(a,'AsaAccesoPocket',sk(a,'AsaAccesoPerfil',cuts,'handleFootT'),'handleFootT',True)
 a.Visibility=False;d.save()


def add_upper_guides(b):
 polys=[]
 for sg in [-1,1]:
  for side in range(4):
   poly=rect(str(sg)+'*20-3','-outer/2',str(sg)+'*20+3','-panelOffset-panelT-0.2')
   for k in range(side):poly=[('-('+y+')',x) for x,y in poly]
   polys.append(poly)
 feat(b,'MarcoGuiasPad',sk(b,'MarcoGuiasPerfil',polys,'upperHeight-seat-6'),'6')

def build_hardware():
 for L in [15,20,35]:
  b=body('M4x'+str(L),'Referencia comercial M4×'+str(L)+' — rosca omitida',(0.8,0.82,0.85),True)
  feat(b,b.Name+'VastagoPad',sk(b,b.Name+'VastagoPerfil',[],circles=[('0','0','boltD/2')]),str(L))
  poly=[('nutSW/sqrt(3)*'+str(math.cos(i*math.pi/3)),'nutSW/sqrt(3)*'+str(math.sin(i*math.pi/3))) for i in range(6)]
  feat(b,b.Name+'CabezaPad',sk(b,b.Name+'CabezaPerfil',[poly],str(L)),'headH');b.Visibility=False
 n=body('TuercaM4','Referencia 934N-4 — taladro de envolvente, rosca omitida',(0.85,0.86,0.88),True)
 poly=[('nutSW/sqrt(3)*'+str(math.cos(i*math.pi/3)),'nutSW/sqrt(3)*'+str(math.sin(i*math.pi/3))) for i in range(6)]
 feat(n,'TuercaPad',sk(n,'TuercaPerfil',[poly]),'nutH')
 feat(n,'TuercaRoscaPocket',sk(n,'TuercaRoscaPerfil',[],'nutH',circles=[('0','0','boltD/2+0.05')]),'nutH',True);n.Visibility=False
 w=body('ArandelaM4','Referencia 125N-4 de nylon',(0.85,0.86,0.88),True)
 feat(w,'ArandelaPad',sk(w,'ArandelaPerfil',[],circles=[('0','0','washerOD/2'),('0','0','washerID/2')]),'washerT');w.Visibility=False;d.save()

def link(parent,source,n,xyz,rotation=None):
 o=d.addObject('App::Link',n);o.setLink(source);parent.addObject(o)
 o.Placement=App.Placement(App.Vector(*[v(a) for a in xyz]),rotation or App.Rotation())
 for axis,a in zip('xyz',xyz):o.setExpression('Placement.Base.'+axis,ex(a))
 o.Visibility=True;return o

def xyrotate(x,y,side):
 for i in range(side):x,y='-('+y+')',x
 return x,y

def side_hardware(parent,side,z,suffix):
 rot=App.Rotation(App.Vector(0,0,1),side*90).multiply(App.Rotation(App.Vector(1,0,0),90))
 rad='panelOffset+panelT';head=rad+'+washerT';base='bossOuter-bossT'
 records=[('M4x15','('+head+')-15'),('ArandelaM4',rad),('ArandelaM4','('+base+')-washerT'),('TuercaM4','('+base+')-washerT-nutH')]
 for i,(n,r) in enumerate(records):
  x,y=xyrotate('0','-('+r+')',side);link(parent,d.getObject(n),'F'+suffix+str(i),(x,y,z),rot)

def vertical_hardware(parent,x,y,top,bottom,L,suffix):
 for i,(n,z) in enumerate([('M4x'+str(L),top+'+washerT-'+str(L)),('ArandelaM4',top),('ArandelaM4',bottom+'-washerT'),('TuercaM4',bottom+'-washerT-nutH')]):
  link(parent,d.getObject(n),'V'+suffix+str(i),(x,y,z))

def assemble():
 global printed_links,hardware_links
 printed_links=[]
 for i in [1,2]:
  parent=d.addObject('App::Part','Modulo'+str(i));parent.Label='Módulo idéntico '+str(i)
  for axis,a in [('x','centerX'),('y','0'),('z','baseZ+'+str(i-1)+'*module')]:parent.setExpression('Placement.Base.'+axis,ex(a))
  printed_links += [link(parent,d.Base,'Base'+str(i),('0','0','0')),link(parent,d.Marco,'Marco'+str(i),('0','0','module-upperHeight'))]
  for side in range(4):
   x,y=xyrotate('0','-panelOffset',side)
   rot=App.Rotation(App.Vector(0,0,1),side*90).multiply(App.Rotation(App.Vector(1,0,0),90))
   printed_links.append(link(parent,d.Panel,'Panel'+str(i)+str(side),(x,y,'seat'),rot))
   side_hardware(parent,side,'lowerBolt',str(i)+str(side)+'B');side_hardware(parent,side,'upperBolt',str(i)+str(side)+'T')
 union=d.addObject('App::Part','Apilamiento')
 for axis,a in [('x','centerX'),('y','0'),('z','baseZ')]:union.setExpression('Placement.Base.'+axis,ex(a))
 for a in [-1,1]:
  for c in [-1,1]:vertical_hardware(union,f'{a}*corner',f'{c}*corner','module+baseHeight','module-cornerCap',20,'S'+str(a).replace('-','N')+str(c).replace('-','N'))
 top=d.addObject('App::Part','Suspension')
 for axis,a in [('x','centerX'),('y','0'),('z','baseZ+2*module')]:top.setExpression('Placement.Base.'+axis,ex(a))
 printed_links.append(link(top,d.Tapa,'TapaMontada',('0','0','0')))
 for sg in [-1,1]:printed_links.append(link(top,d.Escuadra,'Escuadra'+str(sg).replace('-','N'),('0',f'{sg}*corner+hangerFootT/2','lidT'),App.Rotation(App.Vector(1,0,0),90)))
 printed_links.append(link(top,d.Asa,'AsaMontada',('-handleFootT/2','0','lidT+handleRise'),App.Rotation(App.Vector(1,1,1),120)))
 for a in [-1,1]:
  for c in [-1,1]:vertical_hardware(top,f'{a}*corner',f'{c}*corner','lidT+hangerBeam','-cornerCap',35,'T'+str(a).replace('-','N')+str(c).replace('-','N'))
 for sg in [-1,1]:handle_hardware(top,sg)
 hardware_links=[o for o in d.Objects if o.TypeId=='App::Link' and o.Name.startswith(('F','V'))]
 for o in d.Maestras.Group+d.TornilleriaReferencia.Group:o.Visibility=False
 for o in d.Objects:
  if o.TypeId=='Sketcher::SketchObject' or (o.TypeId=='PartDesign::Body' and o not in d.Maestras.Group+d.TornilleriaReferencia.Group):o.Visibility=False
 d.recompute();Gui.activeDocument().activeView().viewAxonometric();Gui.activeDocument().activeView().fitAll();d.save()
 print('Fabricación',len(printed_links),'piezas PETG; comercial',len(hardware_links),'referencias')

def restore_ball_references(src):
 bio=d.getObject('Body') or d.copyObject(src.Body,False)
 if bio.Tip is None:
  biosk=d.copyObject(src.Sketch,False);bio.addObject(biosk)
  biorev=d.copyObject(src.Revolution,False);bio.addObject(biorev);biorev.Profile=biosk;biorev.ReferenceAxis=(biosk,['V_Axis']);bio.Tip=biorev
 for n in ['Array','Array001']:
  a=d.getObject(n)
  for path,e in list(a.ExpressionEngine):a.setExpression(path,None)
  a.Base=bio;a.NumberX=2;a.NumberY=2;a.NumberZ=5
  a.IntervalX=App.Vector(P['pitch'],0,0);a.IntervalY=App.Vector(0,P['pitch'],0);a.IntervalZ=App.Vector(0,0,29)
  for path,e in [('IntervalX.x','pitch'),('IntervalY.y','pitch'),('Placement.Base.x','centerX-pitch/2'),('Placement.Base.y','-pitch/2'),('Placement.Base.z','baseZ+seat'+(' + module' if n=='Array001' else ''))]:a.setExpression(path,ex(e))
  a.touch()
 d.recompute();bio.Visibility=False
 for o in bio.Group:o.Visibility=False

def build_coupons():
 group=d.addObject('App::DocumentObjectGroup','Muestras');group.Label='Probetas de encaje y carga — no forman parte del conjunto'
 def cb(n,label):
  b=body(n,label,(0.8,0.25,0.6));d.Maestras.removeObject(b);group.addObject(b);return b
 b=cb('MuestraApoyo','Muestra de apoyo del panel, orientación equivalente a base')
 feat(b,'MuestraSueloPad',sk(b,'MuestraSueloPerfil',[rect('-15','0','15','12')]),'seat')
 feat(b,'MuestraBossPad',sk(b,'MuestraBossPerfil',[rect('-bossWidth/2','0','bossWidth/2','bossT')]),'bossHeight')
 place=App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(1,0,0),90))
 feat(b,'MuestraBossPocket',sk(b,'MuestraBossTaladro',[rect('-hole/2','lowerBolt-hole/2','hole/2','lowerBolt+hole/2')],placement=place),'bossT',True);b.Visibility=False
 p=cb('MuestraPanel','Lengüeta 2,4 mm — borde crítico superior a 4,8 mm del eje')
 feat(p,'MuestraPanelPad',sk(p,'MuestraPanelPerfil',[rect('-bossWidth/2','0','bossWidth/2','14.8')]),'panelT')
 feat(p,'MuestraPanelPocket',sk(p,'MuestraPanelTaladro',[],'panelT',circles=[('0','10','hole/2')]),'panelT',True);p.Visibility=False
 for n,H in [('MuestraEsquinaSuperior','cornerCap'),('MuestraEsquinaBase','baseHeight')]:
  b=cb(n,'Apilado — probeta de esquina de '+str(v(H))+' mm')
  feat(b,n+'Pad',sk(b,n+'Perfil',[rect('-10','-10','10','10')]),H)
  feat(b,n+'Pocket',sk(b,n+'Taladro',[],H,circles=[('0','0','hole/2')]),H,True);b.Visibility=False
 group.Visibility=False;d.save()


def handle_hardware(parent,sg):
 # Tornillo de abajo arriba: cabeza debajo de tapa, tuerca sobre pie del asa.
 for i,(n,z) in enumerate([('M4x20','20-washerT'),('ArandelaM4','lidT+handleSeat'),('ArandelaM4','-washerT'),('TuercaM4','lidT+handleSeat+washerT')]):
  link(parent,d.getObject(n),'VA'+str(sg).replace('-','N')+str(i),('0',str(sg)+'*handleCenter',z),App.Rotation(App.Vector(1,0,0),180) if i==0 else None)
