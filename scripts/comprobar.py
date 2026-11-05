"""Comprueba contenido y archivos reales. No equivale a W3C ni a Schema Validator."""
from pathlib import Path
from PIL import Image,ImageOps
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
from datetime import datetime,timezone
import hashlib,json,sys

root=Path(__file__).resolve().parents[1]
results=[]
def check(condition,detail):
    results.append({'pass':bool(condition),'detail':detail})
class Parser(HTMLParser):
    def __init__(self):super().__init__();self.tags=[];self.ld=[];self.in_ld=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs); self.tags.append((tag,a))
        if tag=='script' and a.get('type')=='application/ld+json':self.in_ld=True
    def handle_endtag(self,tag):
        if tag=='script':self.in_ld=False
    def handle_data(self,s):
        if self.in_ld:self.ld.append(s)
records=json.loads((root/'recursos.json').read_text())
ld=json.loads((root/'data-galeria.jsonld').read_text())
objects={o['contentUrl']:o for o in ld['@graph'] if o['@type']=='ImageObject'}
check(len(records)==3 and len(objects)==9,'Tres imágenes y nueve ImageObject')
for r in records:
    p=root/r['originalPath']; im=ImageOps.exif_transpose(Image.open(p))
    check(hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'],f"Original sin cambios: {p.name}")
    meta=json.loads((root/f"evidencias/fuentes/{r['id']}-commons.json").read_text())
    info=next(iter(meta['query']['pages'].values()))['imageinfo'][0]
    check(hashlib.sha1(p.read_bytes()).hexdigest()==info['sha1'],f"SHA-1 coincide con Commons: {p.name}")
    check(r['license'].rstrip('/')==info['extmetadata']['LicenseUrl']['value'].rstrip('/'),f"Licencia trazada a ficha Commons: {r['id']}")
    check((im.width,im.height)==(r['orientedWidth'],r['orientedHeight']),f"Orientación y medida: {r['id']}")
    check([v['width'] for v in r['variants']]==[480,768,1920],f"Tres anchos solicitados: {r['id']}")
    for v in r['variants']:
        p=root/v['path']; x=Image.open(p); o=objects[v['path']]
        digest=hashlib.sha256(p.read_bytes()).hexdigest()
        check(x.size==(v['width'],v['height']),f"Dimensiones reales: {p.name}")
        check(x.width<=im.width and x.height==round(im.height*x.width/im.width),f"Sin ampliación ni deformación: {p.name}")
        check(digest==v['sha256']==o['sha256'],f"Hash JSON-LD/manifiesto/archivo: {p.name}")
        check(p.stat().st_size==v['bytes'] and o['contentSize']==str(v['bytes'])+' bytes',f"Bytes JSON-LD/manifiesto/archivo: {p.name}")
        check(o['width']['value']==x.width and o['height']['value']==x.height,f"Dimensiones en JSON-LD: {p.name}")
        check(o['creator']['name']==r['creator'] and o['license']==r['license'] and o['isBasedOn']==r['source'],f"Autoría/licencia/procedencia JSON-LD: {p.name}")
        check(not x.getexif(),f"Derivado sin EXIF/GPS: {p.name}")
pages=[*root.glob('*.html'),*root.glob('*.htm'),*root.glob('docs/*.html')]
for p in pages:
    parser=Parser();text=p.read_text();parser.feed(text)
    check(text.lstrip().lower().startswith('<!doctype html>'),f"Doctype: {p.name}")
    check(any(t=='html' and a.get('lang')=='es' for t,a in parser.tags),f"Idioma: {p.name}")
    check(not any(t=='style' or 'style' in a or (t=='link' and a.get('rel')=='stylesheet') for t,a in parser.tags),f"Sin CSS: {p.name}")
    for t,a in parser.tags:
        for key in ['href','src','srcset']:
            if key not in a:continue
            for u in (a[key].split(',') if key=='srcset' else [a[key]]):
                u=u.strip().split()[0];parsed=urlparse(u)
                if parsed.scheme or parsed.netloc:continue
                dest=(p.parent/unquote(parsed.path)).resolve() if parsed.path else p
                check(dest.exists(),f"Ruta local existente: {p.name} → {u}")
                if parsed.fragment and dest.suffix in ['.html','.htm']:
                    check(f'id="{parsed.fragment}"' in dest.read_text(),f"Ancla existente: {u}")
        if t=='img':check(bool(a.get('alt')) and 'width' in a and 'height' in a,f"Alternativa y espacio reservado: {p.name}")
    if p.name=='galeria.html':
        check(json.loads(''.join(parser.ld))==ld,'JSON-LD embebido idéntico al entregado')
        check(sum(t=='picture' for t,a in parser.tags)==3,'Tres picture en galería')
        check(not any(t=='script' and a.get('type')!='application/ld+json' for t,a in parser.tags),'Sin JavaScript ejecutable en galería')
        for r in records:
            check(r['alt'] in text and r['creator'] in text and r['license'] in text,f"Metadatos coherentes con texto visible: {r['id']}")
check('MAQ-DEMO-003' in (root/'maquinas.html').read_text() and '<tfoot>' in (root/'maquinas.html').read_text(),'Se conserva fila y pie de práctica 3.1')
report={'executedAt':datetime.now(timezone.utc).isoformat(),'scope':'Comprobaciones propias de archivos y coherencia; no es certificación W3C/WCAG ni Schema Validator','checks':len(results),'passed':sum(r['pass'] for r in results),'failures':[r for r in results if not r['pass']],'results':results}
out=root/'evidencias/validacion/comprobaciones-locales.json';out.write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(f"{report['passed']}/{report['checks']} comprobaciones correctas")
for fail in report['failures']:print(fail['detail'])
sys.exit(bool(report['failures']))
