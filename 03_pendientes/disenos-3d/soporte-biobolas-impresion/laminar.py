from pathlib import Path
import json,subprocess,tempfile
root=Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix="veril-biobolas-orca-") as datadir:
 for item in json.loads((root/"piezas.json").read_text()):
  slug=item["slug"];out=root/"laminados"/slug;out.mkdir(parents=True,exist_ok=True)
  command=["/Applications/OrcaSlicer.app/Contents/MacOS/OrcaSlicer","--datadir",datadir,"--slice","0","--outputdir",str(out),"--export-3mf",slug+"-laminado.3mf",str(root/(slug+"--kp3-winkle-petg.3mf"))]
  with (out/"orca-cli.log").open("w") as log:subprocess.run(command,cwd=datadir,stdout=log,stderr=subprocess.STDOUT,check=True)
  (root/item["gcode"]).write_bytes((out/"plate_1.gcode").read_bytes())
  (out/"plate_1.gcode").unlink()
  print(slug, "generado")
print("Actualizar comprobaciones, sumas e informe después de regenerar.")
