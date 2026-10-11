"""Export reproducible views of actual extrusion segments, not the CAD surfaces."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from mpl_toolkits.mplot3d.art3d import Line3DCollection
ROOT=Path(__file__).resolve().parent
COLORS={'Outer wall':'#126891','Inner wall':'#49a8ca','Brim':'#cc7623','Skirt':'#bcac80','Internal Bridge':'#dd4355','Sparse infill':'#86964f','Internal solid infill':'#657ca3','Top surface':'#9269a7','Bottom surface':'#526895'}
for item in json.loads((ROOT/'piezas.json').read_text()):
 slug=item['slug'];out=ROOT/'laminados'/slug
 data=json.loads((out/'trayectorias.json').read_text())
 data=[s for s in data if s[6]!='Custom']
 layers=sorted({s[7] for s in data if s[7] is not None})
 targets=[layers[0]]
 if slug=='estructura': targets += [min(layers,key=lambda z:abs(z-t)) for t in [35.04,39.84]]
 elif slug=='probeta-silicona':targets += [min(layers,key=lambda z:abs(z-t)) for t in [4.64,6.84]]
 else:targets += [layers[len(layers)//2],layers[-1]]
 fig=plt.figure(figsize=(15,10),layout='constrained')
 ax=fig.add_subplot(2,2,1,projection='3d')
 step=max(1,len(data)//18000);selected=data[::step]
 seg=np.array([[s[:3],s[3:6]] for s in selected])
 ax.add_collection3d(Line3DCollection(seg,colors=[COLORS.get(s[6],'#888888') for s in selected],linewidths=.55))
 allpoints=np.array([s[:6] for s in data]).reshape(-1,3)
 lo=allpoints.min(axis=0);hi=allpoints.max(axis=0)
 ax.set_xlim(lo[0]-1,hi[0]+1);ax.set_ylim(lo[1]-1,hi[1]+1);ax.set_zlim(0,hi[2]+1)
 ax.set_box_aspect(np.maximum(hi-lo,[1,1,1]));ax.view_init(20,-65)
 ax.set_title('Extrusión completa (vista global muestreada)')
 ax.set_xlabel('X, mm');ax.set_ylabel('Y, mm');ax.set_zlabel('Z, mm')
 for i,z in enumerate(targets,2):
  ax=fig.add_subplot(2,2,i)
  ds=[s for s in data if s[7]==z]
  seg=[[[s[0],s[1]],[s[3],s[4]]] for s in ds]
  ax.add_collection(LineCollection(seg,colors=[COLORS.get(s[6],'#888888') for s in ds],linewidths=.65))
  ax.autoscale();ax.set_aspect('equal');ax.set_title(f'Capa Z={z:.2f} mm — todos los segmentos')
  ax.set_xlabel('X, mm');ax.set_ylabel('Y, mm');ax.grid(alpha=.15)
 fig.suptitle('Veril — '+slug+' — trayectorias del G-code, sin soportes',fontsize=15)
 fig.savefig(out/'vista-previa.png',dpi=150)
 plt.close(fig)
 print(slug,'vista generada')
