# Validación real de SpiderGym · Práctica 3.2

Fecha: 2026-11-05. Carpeta comprobada: `/Users/alexolmos/SpiderGym`, abierta en VS Code. No es un informe de resultados esperados: describe ejecuciones efectuadas.

## Resultados

| Comprobación | Resultado observado | Evidencia |
| --- | --- | --- |
| Nu HTML Checker del W3C | 7 páginas, 0 errores y 0 advertencias en cada una | `evidencias/validacion/w3c-resumen.json` y respuestas `w3c-*.json` con hash de cada HTML enviado |
| Schema Markup Validator | ImageGallery con 9 ImageObject relacionados: 0 ERRORES y 0 ADVERTENCIAS | `schema_validacion.png`, `schema-resultado.txt`, `schema-fragmento-validado.html`, `schema-coincidencia.json` |
| Archivos y metadatos | Lectura de dimensiones reales, hashes, tamaños, proporción, origen, licencias, rutas, alt y coincidencia del JSON-LD | `comprobaciones-locales.json`; ejecutar `scripts/comprobar.py` para el número exacto actual |
| Navegador automatizado | 14/14 casos correctos; 7/7 páginas cargadas sin imágenes rotas ni errores de JavaScript | `navegador.json`; Chrome 155.0.8059.85 |
| DevTools visible | 375 px carga tres 480w; 768 px carga tres 768w; 1200 px carga tres 1920w, con pesos diferentes | `devtools-375.png`, `devtools-768.png`, `devtools-1200.png` y sus estados AX `.txt` |
| Imágenes bloqueadas | Tres JPEG bloqueados antes de cargar; permanecen los tres alt, los pies y las descripciones | `accesibilidad_sin_imagenes.png` y bloque withoutImages del informe de navegador |
| Teclado | Tab alcanza Saltar al contenido; Enter lleva el foco a main; Tab continúa por los enlaces del contenido | `teclado-salto-contenido.png` y registro keyboard de galeria.html |
| Licencias | Respuesta HTTP 200 de CC BY-SA 4.0 y CC BY 2.0; los originales coinciden con el SHA-1 de Commons | `evidencias/fuentes/comprobacion-url.json`, fichas API originales y comprobaciones locales |

## Selección adaptativa

Cada caso del navegador automatizado usa un contexto nuevo y respuestas sin caché. Se registra la URL realmente elegida en currentSrc, las peticiones de imagen y su estado HTTP, dimensiones intrínsecas y tamaño mostrado. Se probaron anchos 320, 375, 767, 768, 1199, 1200 y 1440 px, con DPR 1 y 2. No hubo desbordamiento horizontal en la galería en esos casos.

En DevTools se usó la copia real del proyecto mediante file://, vista Responsive y Disable cache. Las capturas se recortaron únicamente por arriba para excluir las pestañas personales y los marcadores; el área de página, ancho y panel Network se conservan. Las pruebas automatizadas independientes sí usaron HTTP en un servidor local aislado con puerto efímero. No se confunden las dos formas de prueba.

## Alcance exacto del validador de metadatos

Se envió al servicio oficial un fragmento con solo el bloque JSON-LD público. Se comparó su contenido JSON con data-galeria.jsonld y el bloque embebido: coinciden. El validador reúne el grafo bajo un ImageGallery; no son nueve galerías distintas.

El servicio asigna a las rutas relativas la base sintética `https://example-test.site/`. Esa base la introduce el validador: no se ha añadido al archivo ni se presenta como alojamiento de SpiderGym. El resultado comprueba el marcado y el vocabulario. La existencia y dimensiones de los archivos se comprobaron aparte, en el disco y por HTTP local. No hay una prueba de Google Rich Results ni una publicación pública del sitio.

## Límites de accesibilidad y compatibilidad

Se inspeccionaron visualmente las capturas de móvil y de imágenes bloqueadas y se probaron el foco y el salto por teclado. No se declara conformidad WCAG completa. No se ejecutó VoiceOver en esta sesión ni una auditoría con personas usuarias. Las pruebas previas de VoiceOver del proyecto no se presentan como pruebas nuevas de esta galería.

La adaptación se probó con Chrome, no en Safari/Firefox en esta sesión. Las páginas generales se cargaron a 1280 px; el barrido de 320-1440 px corresponde específicamente a la galería. La tabla anterior de 3.1 se conserva; este informe no afirma una auditoría responsive completa de esa tabla.

Los estilos predeterminados del navegador permiten leer esta entrega sin CSS de autor. No se afirma una auditoría numérica nueva de contraste. Los enlaces a resoluciones son descargas explícitas; la miniatura de 240 px sirve a una demostración HTML sin CSS. Elegir 1920w para ella en escritorio no representa la optimización óptima de una web de producción.

## Procedencia y reproducibilidad

Los originales se conservan sin modificar. Se aplica orientación EXIF, reducción Lanczos y JPEG progresivo calidad 85 con Pillow 13.0.0; se retiran EXIF/GPS en los derivados. Otra versión del codificador puede cambiar el hash, por lo que no se actualiza el manifiesto sin volver a comprobar los resultados.

Las licencias se atribuyen a las fichas consultadas: no se ha investigado independientemente su cadena de titularidad ni se garantizan derechos sobre personas/marcas. Los archivos históricos de licencia no acreditada no se borran del proyecto, pero no se usan en las páginas actualizadas ni se incluyen en el ZIP de la práctica.

## Repetir las comprobaciones

1. Desde la carpeta SpiderGym: `python3 scripts/comprobar.py` (requiere Pillow).
2. Opcionalmente regenerar imágenes: `python3 scripts/regenerar_imagenes.py`; comprobar otra vez el manifiesto. La web no necesita Python/Pillow para visualizarse.
3. Prueba de navegador: instalar Playwright en un entorno de pruebas y ejecutar `node scripts/navegador.cjs`. Si usa Chrome del sistema, indicar CHROME_PATH. El script levanta un servidor local solo mientras prueba y guarda las evidencias.
4. W3C: `python3 scripts/validar_html.py`. Este paso envía las siete páginas HTML especificadas al servicio oficial; no envía docs Markdown, evidencias, imágenes originales ni datos del usuario.
5. Schema.org: abrir validator.schema.org, Fragmento de código, pegar el JSON-LD dentro de su script application/ld+json y ejecutar. Guardar la nueva captura si se modifica el marcado.

## Lo que debe aportar Alex

Comprender el código y grabar/presentar el vídeo real de 10-12 minutos. El guion de apoyo está en `docs/guion-video.md`. No hay una grabación de defensa ya hecha ni se atribuye al alumno la ejecución manual de las pruebas automatizadas.
