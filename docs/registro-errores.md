
# Registro de errores y mejoras - SpiderGym

Fecha: 23/10/2026

## 1. Explicación del sistema NFC/QR

Problema:
La explicación inicial podía dar a entender que
el NFC o el QR registraban automáticamente los ejercicios.

Solución:
Se ha aclarado que NFC y QR identifican al usuario.
Para registrar datos automáticamente harían falta
sensores o un sistema compatible. También se contempla
la introducción manual de los datos.

## 2. Navegación y accesibilidad

Problema:
El menú no identificaba cuál era la página actual.

Solución:
Se han añadido aria-label y aria-current="page"
cuando corresponde.

## 3. Descripción de imágenes

Problema:
El texto alternativo de la imagen era poco descriptivo.

Solución:
Se ha ampliado el atributo alt de la imagen
de extensión de piernas.

## 4. Revisiones pendientes

- Validar el HTML completo.
- Comprobar posibles enlaces rotos.
