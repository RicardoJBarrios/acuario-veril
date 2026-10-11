"""Slice each prepared project with embedded profiles and an isolated Orca datadir."""
from pathlib import Path
import json, subprocess, tempfile
ROOT = Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix='veril-rebosadero-orca-') as datadir:
    for item in json.loads((ROOT/'piezas.json').read_text()):
        slug=item['slug']
        out=ROOT/'laminados'/slug
        out.mkdir(parents=True,exist_ok=True)
        command=['/Applications/OrcaSlicer.app/Contents/MacOS/OrcaSlicer',
                 '--datadir',datadir,'--slice','0','--outputdir',str(out),
                 '--export-3mf',slug+'-laminado.3mf',str(ROOT/(slug+'--kp3-winkle-petg.3mf'))]
        with (out/'orca-cli.log').open('w') as log:
            subprocess.run(command,cwd=datadir,stdout=log,stderr=subprocess.STDOUT,check=True)
        (ROOT/item['gcode']).write_bytes((out/'plate_1.gcode').read_bytes())
        (out/'plate_1.gcode').unlink()
        print(slug,'generado',flush=True)
print('Regenerar el informe y las verificaciones después de cualquier cambio.',flush=True)
