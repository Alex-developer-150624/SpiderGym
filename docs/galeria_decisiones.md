# Decisiones de la práctica 3.2

Fecha de trabajo: 2026-11-05. Se usa la carpeta real abierta en VS Code: `/Users/alexolmos/SpiderGym`.

## Fuentes y alcance

Manual LMSGI aportado, tema 3, páginas PDF 42-44 (pies impresos 43-45): imágenes con dimensiones y alternativa, picture, metadatos, orden sin CSS y documentación del formato, tamaño y licencia.
Enunciado localizado en Descargas: `Prácticas con guiones de vídeos .html`, sección `tema3-2`. Pide galeria.html, 480w/768w/1920w, JSON-LD, ficha de licencias, borrador, decisiones, pruebas y vídeo de 10-12 minutos.
Se consultó GitHub `Alex-developer-150624/SpiderGym`, árbol `17cdbad06181e874dff4889fe5e19cc353208cbb`. La copia abierta en VS Code tiene cambios locales posteriores: se conservan, incluido el tercer registro y tfoot de la práctica 3.1. No se reinicia la rama ni se recuperan archivos que el usuario tenía eliminados.

## Imágenes y resolución

Se publican tres tipos ya presentes en el catálogo: extensión de piernas, press de pecho y jalón al pecho. Son fotos ilustrativas, no fotografías de los gimnasios ficticios. Los originales anteriores miden 520×506 y 480×467; su licencia no estaba acreditada y el HTML apuntaba a `extension-piernas-480w.png`, que no existía (el archivo se llamaba `extension-piernas480.png`). No se fabricó una versión de 1920 estirando esa foto.

Los nuevos originales permiten reducir a los tres anchos pedidos. Se aplica orientación EXIF antes de medir, Lanczos y JPEG progresivo calidad 85. Pillow 13.0.0. La proporción se conserva con redondeo de como máximo medio píxel. El manifiesto registra los tamaños reales de cada archivo; los sufijos no simulan dimensiones.

## HTML sin CSS

picture elige 1920w con viewport >=1200, 768w desde 768 hasta 1199, y el img de 480w por debajo de 768. Los source van del breakpoint mayor al menor. No se afirma que un móvil de alta densidad elija siempre el archivo más pequeño con cualquier configuración srcset: aquí hay una sola URL por condición media, elegida de forma explícita para la demostración del enunciado. Los números 480/768/1920 son anchos del archivo; no son todos breakpoints.

Se usa una vista previa de 240 píxeles de ancho mediante atributos HTML width/height, con proporción calculada, para que quepa sin CSS en el contenido de figure en móvil. Es una decisión didáctica: descargar 1920 para una miniatura no es una optimización ideal de producción. Una versión posterior con CSS podrá combinar tamaños fluidos, srcset y sizes ajustados al ancho real. Los enlaces permiten abrir cada resolución a tamaño completo.

Se añaden figure/figcaption, títulos, nav común, lang, viewport y salto al contenido con foco. El orden de lectura no depende de estilos. No hay JavaScript ejecutable en la galería; application/ld+json es un bloque de datos.

## Metadatos veraces

El tipo principal es ImageGallery con ImageObject para cada uno de los nueve archivos. Se elige ImageGallery porque es una colección de imágenes; no se simula un artículo ni un producto en venta. Cada ImageObject contiene creador real, URL local, formato, tamaño, dimensiones, SHA-256, procedencia y licencia. alt describe lo visible para quien no ve la foto; JSON-LD describe el recurso para sistemas que procesan datos. No sustituye al alt.

No se inventan fecha de publicación, precio, disponibilidad, reseñas, URL pública ni autoría de las fotos. Las rutas de contentUrl son relativas al documento y se verifican por HTTP local; al desplegar se resolverán en ese alojamiento. No hay etiqueta canonical inventada. El original de jalón necesita orientación EXIF: su matriz cruda es 3840×2160, y su visualización correcta es vertical, 2160×3840.

## Transferencia Article a Product

El enunciado pide demostrar el cambio en el vídeo. Se entregan ejemplos separados en `docs/transferencia-article.jsonld` y `docs/transferencia-product.jsonld`. Son ejemplos didácticos mínimos con nombre real del contenido, descripción e imagen existente. No se inyectan como metadatos de la galería. El ejemplo Product no incluye Offer, precio ni stock: no existe una oferta real. No basta cambiar @type: Article usa headline y Product usa name. Ninguno demuestra elegibilidad de resultados enriquecidos de Google.

## Derechos y límites

Se usa la declaración de licencia de cada ficha Commons y se conservan las evidencias. No se copia el ejemplo del enunciado que denomina CC0 a recursos de Unsplash/Pexels: esas etiquetas de ejemplo no acreditan una licencia. El enlace de PTPioneer solicitado por Tyler Read se mantiene. Las fotos anteriores y el logotipo quedan conservados en el proyecto, pero fuera de las páginas actualizadas y del paquete de esta práctica. No se atribuye a Alex la autoría fotográfica.

## IA y evidencias

Codex ayudó a localizar fuentes, generar versiones, escribir HTML/JSON-LD, documentación y ejecutar pruebas. Las imágenes no han sido generadas por IA. Los resultados observados están en el informe de validación; no se confunden pruebas automáticas con una auditoría WCAG completa o una sesión de VoiceOver. No se inventan actividades de Gemini/Copilot, experiencia personal ni una defensa ya grabada.
