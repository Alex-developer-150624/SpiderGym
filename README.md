# SpiderGym · Práctica 3.2 terminada

Galería HTML sin CSS de extensión de piernas, press de pecho y jalón al pecho. Proyecto académico estático: NFC/QR y conexión de máquinas siguen siendo una propuesta.

## Abrir

Desde esta carpeta, ejecuta `python3 -m http.server 8000 --bind 127.0.0.1` y abre `http://127.0.0.1:8000/galeria.html`. Las páginas también abren como archivos locales; las pruebas de red se hacen por HTTP. No hacen falta Node ni librerías para ver la web.

## Archivos

- `galeria.html`: entrega principal con tres fotos y JSON-LD embebido.
- `assets/images/`: nueve JPEG reales de 480, 768 y 1920 píxeles; sin ampliación de originales.
- `assets/originales/`: originales sin cambios para reproducir el proceso.
- `recursos.json`: dimensiones, bytes, hashes, autoría, fuentes y licencias.
- `data-galeria.jsonld`: copia de los metadatos embebidos.
- `docs/entrega-3-2.html`: documentación para leer en navegador.
- `docs/galeria_decisiones.md`, `docs/requisitos.md`, `docs/licencias_recursos.md` y `docs/validacion-3-2.md`: decisiones, correspondencia y pruebas reales.
- `docs/guion-video.md`: apoyo para la presentación de 10-12 minutos.
- `evidencias/`: respuestas originales de fuentes, informes y capturas de pruebas.
- `scripts/`: regeneración y comprobaciones reproducibles.
- `drafts/galeria_v1.html`: borrador auténtico anterior, con sus limitaciones; no es la entrega final.

## Derechos y publicación

Fotografías de Aliva Sahoo, Tyler Read (PTPioneer) y SAgbley, según las fichas enlazadas. Se conservan atribución, licencia e indicación de cambios. Las licencias de las fotos no se aplican automáticamente al código ni a otros recursos históricos del proyecto. No hay una URL pública inventada ni resultados de validación supuestos. Lee el informe para ver el alcance de las pruebas.

Se ha trabajado sobre la copia local de VS Code y se ha conservado el trabajo previo de la práctica 3.1. No se ha hecho push ni publicación. Pendiente del alumno: comprender y defender el trabajo mediante el vídeo/presentación solicitado; el guion no sustituye su explicación.
