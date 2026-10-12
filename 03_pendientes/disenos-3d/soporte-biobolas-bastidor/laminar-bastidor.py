"""Lamina las placas con directorio Orca aislado; no inicia impresiones."""
from pathlib import Path
import json
import subprocess
import tempfile
import hashlib
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parent/'impresion'
ORCA='/Applications/OrcaSlicer.app/Contents/MacOS/OrcaSlicer'
manifest=json.loads((ROOT/'piezas.json').read_text())
outputs=[]
for job in manifest['jobs']:
    project=ROOT/job['project']
    assert hashlib.sha256(project.read_bytes()).hexdigest()==job['project_sha256']
    target=ROOT/'laminados'/job['slug'];target.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='veril-bastidor-orca-') as datadir:
        args=[ORCA,'--datadir',datadir,'--slice','0','--outputdir',str(target),
              '--export-3mf',job['slug']+'-laminado.3mf',str(project)]
        with (target/'orca-cli.log').open('w') as log:
            result=subprocess.run(args,cwd=datadir,stdout=log,stderr=subprocess.STDOUT)
        if result.returncode:
            raise RuntimeError('Orca falla en '+job['slug']+'; consultar su log, exit='+str(result.returncode))
    gcode=ROOT/'gcode'/job['gcode'];gcode.parent.mkdir(exist_ok=True)
    gcode.write_bytes((target/'plate_1.gcode').read_bytes())
    (target/'plate_1.gcode').unlink()
    outputs.append({'slug':job['slug'],'gcode':gcode.name,'bytes':gcode.stat().st_size,
                    'sha256':hashlib.sha256(gcode.read_bytes()).hexdigest(),
                    'generated_utc':datetime.now(timezone.utc).isoformat(),
                    'method':'OrcaSlicer 2.4.2 CLI --datadir aislado',
                    'project_sha256':job['project_sha256']})
    (ROOT/'generacion.json').write_text(json.dumps(outputs,indent=2)+'\n')
    print('LAMINADO',job['slug'],gcode.name,flush=True)
