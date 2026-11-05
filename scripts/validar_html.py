"""Envía las páginas públicas del prototipo al Nu HTML Checker y guarda su respuesta."""
from pathlib import Path
from datetime import datetime,timezone
import urllib.request,urllib.error,json,sys,hashlib
root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
out=root/'evidencias/validacion';out.mkdir(parents=True,exist_ok=True)
records=[]
names=['index.html','maquinas.html','maquina-extension-piernas.html','galeria.html','galeria.htm','docs/licencias_recursos.html','docs/entrega-3-2.html']
# Lista explícita: no se envían documentos privados, evidencias, originales ni datos de entrenamiento.
# Estas siete páginas se inspeccionaron: solo prototipo académico, datos ficticios,
# descripciones de máquinas y atribuciones ya públicas en Wikimedia Commons.
pages=[root/name for name in names]
for p in pages:
    relative=str(p.relative_to(root));body=p.read_bytes()
    req=urllib.request.Request('https://validator.w3.org/nu/?out=json',data=body,headers={'Content-Type':'text/html; charset=utf-8','User-Agent':'SpiderGymAcademic/1.0'},method='POST')
    record={'file':relative,'sha256':hashlib.sha256(body).hexdigest(),'executedAt':datetime.now(timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(req,timeout=45) as r:raw=r.read();record['httpStatus']=r.status
        data=json.loads(raw);record.update(errors=sum(x['type']=='error' for x in data['messages']),warnings=sum(x['type']=='info' and x.get('subType')=='warning' for x in data['messages']),messages=data['messages'])
        (out/('w3c-'+p.name+'.json')).write_bytes(raw)
    except Exception as e:record['error']=str(e)
    records.append(record);print(relative,record.get('errors'),record.get('warnings'),record.get('error',''),flush=True)
(out/'w3c-resumen.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
sys.exit(any(r.get('error') or r.get('errors') for r in records))
