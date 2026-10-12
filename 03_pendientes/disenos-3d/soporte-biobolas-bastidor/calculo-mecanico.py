"""Cribado analítico reproducible; no certifica PETG ni representa FEM 3D.

N, mm, MPa. E=600 MPa y presupuesto de tensión=5 MPa son hipótesis elegidas,
no propiedades medidas de la bobina. Hace falta ensayar el conjunto impreso.
"""
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def lu_decompose(matrix):
    a=[row[:] for row in matrix];n=len(a)
    # Matriz simétrica definida positiva; eliminación sin pivoteo.
    for k in range(n):
        if a[k][k]<=0:raise ValueError('Rigidez no positiva')
        for i in range(k+1,n):
            a[i][k]/=a[k][k]
            for j in range(k+1,n):a[i][j]-=a[i][k]*a[k][j]
    return a


def solve_lu(a,b):
    n=len(a);x=b[:]
    for i in range(n):x[i]-=sum(a[i][j]*x[j] for j in range(i))
    for i in range(n-1,-1,-1):
        x[i]=(x[i]-sum(a[i][j]*x[j] for j in range(i+1,n)))/a[i][i]
    return x


def multiply(a,x):return [sum(v*w for v,w in zip(row,x)) for row in a]


def dot(a,b):return sum(x*y for x,y in zip(a,b))


def stepped_buckling(segments,length,E,width,thin,thick):
    """Diferencias finitas: extremos articulados, centro 70% reforzado.

    Se omite el arriostramiento que pudiera proporcionar la diagonal cruzada.
    No modela raíces, agujeros, alabeo ni delaminación. La segunda derivada
    discretiza la energía de flexión; la primera, la rigidez geométrica.
    """
    h=length/segments;n=segments-1
    kb=[[0.0]*n for _ in range(n)];kg=[[0.0]*n for _ in range(n)]
    for node in range(1,segments):
        t=thick if 0.15<=node/segments<=0.85 else thin
        I=width*t**3/12
        coeff={j-1:c/h**2 for j,c in [(node-1,1),(node,-2),(node+1,1)] if 0<j<segments}
        for i,ci in coeff.items():
            for j,cj in coeff.items():kb[i][j]+=E*I*h*ci*cj
    for left in range(segments):
        coeff={j-1:c/h for j,c in [(left,-1),(left+1,1)] if 0<j<segments}
        for i,ci in coeff.items():
            for j,cj in coeff.items():kg[i][j]+=h*ci*cj
    lu=lu_decompose(kb);v=[math.sin(math.pi*(i+1)/segments) for i in range(n)]
    previous=None
    for iteration in range(100):
        v=solve_lu(lu,multiply(kg,v));norm=math.sqrt(dot(v,v));v=[x/norm for x in v]
        eig=dot(v,multiply(kb,v))/dot(v,multiply(kg,v))
        if previous and abs(eig-previous)<1e-9*eig:break
        previous=eig
    return {'segments':segments,'critical_N':eig,'iterations':iteration+1}


def calculate():
    cad=json.loads((ROOT/'comprobacion-cad-funcional.json').read_text())
    p=cad['parameters_mm'];mass_solid_g=cad['assembled_volume_mm3']*1.23/1000
    total=1.2+mass_solid_g/1000+0.15
    service=math.ceil(total/0.5)*0.5
    W=service*9.81*2.5;F=W/2
    budget=5.0;E=600.0
    run=p['panelWidth']-p['railWidth'];rise=p['panelHeight']-p['railWidth']
    L=math.hypot(run,rise)
    eig=[stepped_buckling(n,L,E,p['diagonalWidth'],p['panelThickness'],
                           p['panelThickness']+p['braceExtra']) for n in [20,40,80]]
    # Apoyos en centros de las orejetas remanentes y carga en centro de panel.
    outer_center=-(p['outerWidth']/2-p['panelHeadHeight']+p['outerLeafInner'])/2
    inner_center=-(p['innerLeafOuter']+p['innerLeafInner'])/2
    panel_center=-(p['panelOffset']+p['panelThickness']/2)
    a=panel_center-outer_center;b=inner_center-panel_center
    M=F*a*b/(a+b)
    pin_S=p['panelKeyWidth']**3/6
    outer_t=p['outerWidth']/2-p['outerLeafInner']-p['panelHeadHeight']
    stress={
      'panel_key_bending':M/pin_S,
      'panel_key_double_shear':F/(2*p['panelKeyWidth']**2),
      'outer_fork_bearing':F*b/(a+b)/(outer_t*p['panelKeyWidth']),
      'outer_fork_end_tearout':F*b/(a+b)/(2*outer_t*(p['forkHeight']-p['pinCenterB']-p['panelHole']/2)),
      'panel_net_section':F/((p['railWidth']-p['panelHole'])*p['panelThickness']),
      'vertical_key_net_tension':F/(p['stackKeyWidth']*(p['stackKeyThickness']-3.2)),
      'structural_keeper_bending':(F*(p['stackHoleWidth']+p['keeperLength'])/8)/(p['keeperThickness']*p['keeperWidth']**2/6),
      'structural_keeper_double_shear':F/(2*p['keeperThickness']*p['keeperWidth']),
      'handle_top_bending':(W*(p['handleWidth']-2*p['handleRail'])/4)/(p['handleThickness']*p['handleRail']**2/6),
    }
    # Cada base recibe sus 20 bolas/hotel, no el módulo colgado debajo: esa
    # carga llega por el perímetro y las esquinas. Masa de asiento candidata
    # 0,8 kg/módulo, columna más cargada 30% y dos nervios ortogonales.
    module_seat_mass=0.8
    force_column=module_seat_mass*9.81*2.5*0.30
    local_rib_width=p['columnPitch']/2+p['ribWidth']/2-17.15
    arm=p['outerWidth']/2-p['frameWidth']-p['columnPitch']/2
    stress['base_rib_bending_at_hotel_relief']=(force_column/2*arm)/(local_rib_width*p['seatHeight']**2/6)
    e=p['glassInner']+p['glassThickness']/2
    moment=W*e/2
    stress['hook_outer_wall_bending']=moment/(p['hangerThickness']*p['hookWall']**2/6)
    stress['hook_top_bending_screen']=moment/(p['hangerThickness']*p['hookTop']**2/6)
    net_hanger_t=p['hangerThickness']-p['stackHoleThickness']
    stress['hanger_base_beam_at_handle_slot']=(F*(2*p['stackCenter'])/4)/(net_hanger_t*p['hangerBaseHeight']**2/6)
    stress['lid_handle_crossbar_at_key_slot']=(F*(p['outerWidth']-2*p['frameWidth'])/4)/((p['handleCrossbarWidth']-p['stackHoleThickness'])*p['lidHeight']**2/6)
    transverse=10.0;axial=(transverse/2)/(run/L)
    # La base y el aro conservan nervios de 3 mm, pero el aro lleva la carga
    # alrededor de los cuatro mástiles. La distribución real exige ensayo.
    result={
      'evidence':'analytical_screening_only_not_mechanical_acceptance',
      'user_wet_balls_and_hotels_kg':1.2,
      'full_solid_petg_upper_mass_g':mass_solid_g,
      'extra_retained_water_allowance_kg':0.15,
      'estimated_combined_kg':total,'rounded_service_mass_kg':service,
      'dynamic_multiplier':2.5,'vertical_design_force_N':W,
      'assumed_active_connections':2,'force_per_active_connection_N':F,
      'unmeasured_stress_budget_MPa':budget,'unmeasured_modulus_MPa':E,
      'nominal_stresses_MPa':stress,
      'stress_checks_within_assumed_budget':all(s<=budget for s in stress.values()),
      'diagonal_unbraced_length_mm':L,'lateral_screen_force_N':transverse,
      'diagonal_axial_demand_N':axial,'buckling_convergence':eig,
      'buckling_margin_under_assumptions':min(x['critical_N'] for x in eig)/axial,
      'hook_moment_each_Nmm':moment,
      'hook_horizontal_reaction_each_N':moment/p['hookDrop'],
      'module_seat_mass_assumption_kg':module_seat_mass,
      'most_loaded_column_fraction':0.30,
      'rib_width_remaining_at_hotel_mm':local_rib_width,
      'limitations':[
        'E y presupuesto de tensión sin medición local ni calificación húmeda.',
        'No se incluyen concentraciones, fluencia, fatiga, adhesión real de capas ni contacto no lineal.',
        'La viga de pandeo es un modelo unidimensional idealizado; no es FEM del conjunto.',
        'Las chavetas requieren ensayo específico de migración, giro y extracción en húmedo.',
        'Mástiles, nervios de asiento, marcos, raíces y vidrio requieren ensayo del conjunto.',
        'Dos uniones activas es una hipótesis de reparto, no un reparto comprobado.',
      ],
    }
    (ROOT/'calculo-mecanico.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':calculate()
