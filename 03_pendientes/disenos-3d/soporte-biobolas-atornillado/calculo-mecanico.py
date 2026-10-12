"""Demandas del prototipo. No certifica PETG, nylon, vidrio ni uniones."""
from pathlib import Path
import math,json
R=Path(__file__).resolve().parent
c=json.loads((R/'comprobacion-cad.json').read_text());p=c['parameters_mm'];W=2*9.81*2.5;F=W/2
E=600;budget=5
run=p['panelWidth']-p['rail'];rise=p['panelHeight']-p['rail'];L=math.hypot(run,rise);N=5/(run/L)
root=4-1.226869*0.7;A=math.pi*root**2/4;S=math.pi*root**3/32
# Cribado superior de excentricidad entre centros de apoyo en solape simple.
e=(p['bossT']+p['panelT'])/2+(p['panelOffset']-p['bossOuter']);M=F*e
seat_width=p['pitch']/2+p['rib']/2-17.15;arm=p['outer']/2-p['rim']-p['pitch']/2
sigma={
 'panel_net_tension':F/((p['bossWidth']-p['hole'])*p['panelT']),
 'panel_hole_bearing':F/(4*p['panelT']),
 'boss_hole_bearing':F/(4*p['bossT']),
 'upper_panel_end_tearout_shear':F/(2*p['panelT']*(p['panelHeight']-(p['upperBolt']-p['seat'])-p['hole']/2)),
 'diagonal_tension':N/(p['diag']*p['panelT']),
 'handle_top_bending':(W*(p['handleWidth']-2*p['handleRail'])/4)/(p['handleT']*p['handleRail']**2/6),
 'hook_wall_and_top_bending':(F*(p['glassInner']+p['glassThickness']/2))/(p['hangerT']*p['hookWall']**2/6),
 'hanger_foot_beam_screen':(F*2*p['corner']/4)/((p['hangerFootT']-p['hole'])*p['hangerBeam']**2/6),
 'lid_crossbar_net_bending_screen':(F*(p['outer']-2*p['rim'])/4)/((p['crossbar']-p['hole'])*p['lidT']**2/6),
 'base_rib_at_hotel':(.8*9.81*2.5*.3/2*arm)/(seat_width*p['seat']**2/6),
}
# Presupuesto solo hipotético de PETG. No aplicarlo como admisible del nylon.
r={'status':'cribado_no_aceptacion_mecanica','service_mass_kg':2,'wet_balls_hotels_user_kg':1.2,'petg_full_solid_g':c['mass_full_solid_g'],'hardware_mass_allowance_g_unmeasured':50,'retained_water_allowance_g_unmeasured':150,'design_force_N':W,'active_connections_assumption':2,'force_per_connection_N':F,'petg_assumed_budget_MPa':budget,'petg_assumed_E_MPa':E,'petg_nominal_stresses_MPa':sigma,'within_assumed_petg_budget':all(s<budget for s in sigma.values()),'diagonal_tension_only':{'length_mm':L,'force_N':N,'ideal_axial_extension_mm':N*L/(E*p['diag']*p['panelT']),'uniform_pinned_compression_critical_N':math.pi**2*E*(p['diag']*p['panelT']**3/12)/L**2,'compression_capacity_not_relied_on':True},'nylon_fastener_demands_not_qualified':{'root_diameter_mm_nominal':root,'single_shear_or_tension_nominal_MPa':F/A,'lap_eccentricity_mm':e,'lap_moment_upper_screen_Nmm':M,'lap_bending_nominal_MPa':M/S,'wet_material_allowable_unknown':True,'bending_screen_limitation':'El momento completo entre centros es un cribado conservador. Reparto de contacto, apriete, arandelas y flexión requieren ensayo o modelo de unión; no equivale a verificación.'},'thread_protrusion_mm':{'panel_M4x15':15-(p['bossT']+.2+p['panelT']+2*p['washerT']+p['nutH']),'stack_M4x20':20-(p['baseHeight']+p['cornerCap']+2*p['washerT']+p['nutH']),'suspension_M4x35':35-(p['cornerCap']+p['lidT']+p['hangerBeam']+2*p['washerT']+p['nutH']),'handle_M4x20':20-(p['lidT']+p['handleSeat']+2*p['washerT']+p['nutH'])},'limitations':['Materiales sin calificar con humedad, salinidad, lote y orientacion reales.','No se resuelven concentraciones, flexion de solapes, apriete ni relajacion a largo plazo.','No es FEM y no acredita rigidez del ensamblaje o carga de vidrio.','Se requieren pruebas de union con 2.5kg, conjunto 2kg/5kg, lateral10N e inmersion antes de aceptacion.']}
(R/'calculo-mecanico.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps(r,indent=2))
