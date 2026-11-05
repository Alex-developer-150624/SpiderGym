"""Regenera solo derivados desde originales; Python 3 y Pillow (probado: 13.0.0)."""
from pathlib import Path
from PIL import Image, ImageOps
import json, hashlib

root=Path(__file__).resolve().parents[1]
records=json.loads((root/'recursos.json').read_text())
for r in records:
    original=root/r['originalPath']
    assert hashlib.sha256(original.read_bytes()).hexdigest()==r['sha256']
    im=ImageOps.exif_transpose(Image.open(original)).convert('RGB')
    for v in r['variants']:
        assert v['width']<=im.width, 'El archivo original no permite este tamaño sin ampliación'
        assert v['height']==round(im.height*v['width']/im.width)
        dest=root/v['path']
        im.resize((v['width'],v['height']),Image.Resampling.LANCZOS).save(dest,'JPEG',quality=85,optimize=True,progressive=True)
        print(dest.relative_to(root),dest.stat().st_size,hashlib.sha256(dest.read_bytes()).hexdigest())
print('Regeneración terminada. Ejecuta comprobar.py para contrastar el manifiesto; otra versión de Pillow puede producir bytes diferentes.')
