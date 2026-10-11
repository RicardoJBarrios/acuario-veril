"""Open a sliced project in isolated macOS Orca and record its window."""
from pathlib import Path
import json, subprocess, tempfile, sys, time
ROOT=Path(__file__).resolve().parent
slug=sys.argv[1]
project=ROOT/'laminados'/slug/(slug+'-laminado.3mf')
data=Path(tempfile.mkdtemp(prefix='veril-rebosadero-orca-gui-inicializado-'))
(data/'OrcaSlicer.conf').write_text(json.dumps({'header':'OrcaSlicer 2.4.2','app':{'version':'2.4.2','single_instance':False,'show_home_page':False,'show_daily_tips':False},'models':[{'model':'Kingroon KP3 (KP3-3DP180)','nozzle_diameter':'0.4','vendor':'Kingroon'}]},indent=2))
subprocess.run(['open','-n','-a','/Applications/OrcaSlicer.app','--args','--datadir',str(data),str(project)],check=True)
pid=None
for i in range(12):
    result=subprocess.run(['ps','-axo','pid=,command='],capture_output=True,text=True,check=True)
    matches=[line.strip().split(maxsplit=1)[0] for line in result.stdout.splitlines() if '/Contents/MacOS/OrcaSlicer' in line and str(data) in line]
    if matches:
        pid=int(matches[0]);break
    time.sleep(.5)
assert pid is not None
w=subprocess.run(['osascript','-e',f'tell application "System Events" to tell (first application process whose unix id is {pid}) to get name of every window'],capture_output=True,text=True)
windows=w.stdout.strip()
rec={'project':str(project.relative_to(ROOT)),'datadir':str(data),'pid':pid,'windows':windows,'opened':w.returncode==0 and slug+'-laminado' in windows}
records=json.loads((ROOT/'apertura-orca.json').read_text());records.append(rec);(ROOT/'apertura-orca.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(rec))
assert rec['opened'],rec
