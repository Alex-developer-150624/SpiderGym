# Comprobación local — Quincena 2 de LMSGI

Fecha: 7 de octubre de 2026.

Resultado: las tres páginas superan las comprobaciones locales descritas abajo.
Se han utilizado Python 3 (`html.parser`, `pathlib` y `hashlib`) y las herramientas
`file` y `sips` sobre los archivos reales de la entrega. La comprobación cubre
la estructura básica y las rutas; no equivale a una validación completa con el
validador HTML de W3C ni a una prueba visual en el navegador.

## Resultados por página

| Archivo | Título de la pestaña | Enlaces locales | Imágenes | Resultado |
| --- | --- | ---: | ---: | --- |
| `index.html` | SpiderGym | 2 | 1 | Correcto |
| `maquinas.html` | SpiderGym - Máquinas | 3 | 0 | Correcto |
| `maquina-extension-piernas.html` | SpiderGym - Extensión de piernas | 3 | 1 | Correcto |

## Comprobaciones realizadas

- Los tres archivos se leen correctamente como UTF-8.
- Cada documento incluye `<!DOCTYPE html>`, `lang="es"`, declaración de UTF-8
  y un título no vacío.
- Cada página contiene un `html`, `head`, `body`, `title`, `main`, `h1`, `nav`
  y `footer`.
- Las etiquetas tienen un anidamiento y cierre coherentes; los elementos visibles
  están dentro de `body`.
- Los 8 enlaces internos usan rutas relativas y apuntan a archivos existentes.
- Las 2 referencias a imágenes existen y tienen texto alternativo.
- Los nombres en las rutas coinciden exactamente con los nombres de los archivos,
  incluidas mayúsculas y minúsculas.
- El formato real de cada imagen coincide con su extensión: logotipo JPEG de
  1254 × 1254 píxeles y fotografía PNG de 549 × 534 píxeles.

## Correcciones aplicadas

La cabecera con el logotipo y el encabezado principal de `index.html` estaba
antes de la apertura de `body`. Se ha situado dentro de `body` y se ha integrado
con el lema en una única cabecera.

Las extensiones de las imágenes no coincidían con sus formatos reales. Se ha
renombrado `logo-spidergym.png` a `logo-spidergym.jpg` y `extension-piernas.jpg`
a `extension-piernas.png`, y se han actualizado las referencias del HTML.
El contenido de las imágenes se conserva.

## Comprobación manual reproducible

1. Abrir `index.html` en un navegador y comprobar el logotipo.
2. Pulsar **Máquinas** y comprobar el catálogo.
3. Pulsar **Ver detalle** en Extensión de piernas y comprobar la fotografía.
4. Pulsar **Volver al catálogo** y después **Inicio**.

Estos pasos quedan documentados para repetir la prueba visual. No se adjuntan
capturas ni se afirma haber realizado esa prueba visual durante esta preparación.

## Identificación de la versión comprobada

SHA-256 de las páginas:

```text
89c2b1f5ba031f541715b240e21e679ebf31fdf6a616a247b95c5341929bf54e  index.html
2447738681dc51ac58f2a76c6b13e0296bceb9f346cab17d629008f73d0393db  maquinas.html
3e045835bcd8da6c7614d3f80fe69a8c43b540de0df4ab3726a9d2579d489d13  maquina-extension-piernas.html
```
