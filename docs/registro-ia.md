# SpiderGym — Actividades de IA 1 a 10
**Quincena 3 · LMSGI · ASIX**
## IA-1. HTML semántico

**Prompt:** Actúa como profesor de Lenguajes de Marcas para un principiante de ASIX. Explícame qué es HTML semántico y hazme tres preguntas para comprobar que lo entiendo.

**Explicación de la IA:** HTML semántico consiste en utilizar etiquetas que indican qué función tiene cada parte de una página. Por ejemplo, `<nav>` identifica la navegación, `<main>` el contenido principal y `<footer>` el pie de página. A diferencia de `<div>`, estas etiquetas tienen significado propio y ayudan a organizar el documento y a las tecnologías de accesibilidad.

**Preguntas y respuestas modelo:**

**1. ¿Para qué sirve `<nav>`?**  
Para indicar al navegador que esa sección contiene enlaces de navegación.

**2. ¿Qué diferencia hay entre `<main>` y `<footer>`?**  
`<main>` contiene la información principal de la página y `<footer>` suele contener información complementaria, como autoría o enlaces secundarios.

**3. ¿Por qué no utilizar siempre `<div>`?**  
Porque `<div>` no explica qué función tiene cada sección y las etiquetas semánticas facilitan comprender la estructura.

**Corrección de referencia:** Las tres respuestas son correctas.

**Reflexión propuesta:** He aprendido que HTML no consiste solamente en mostrar texto e imágenes. También sirve para explicar cómo se organiza la información.

## IA-2. Entrevista sobre mi proyecto

**Prompt:** Actúa como un consultor web. Hazme diez preguntas para encontrar aspectos poco claros de SpiderGym.

**Entrevista simulada, con respuestas modelo:**

**1. ¿Qué problema resuelve SpiderGym?**  
Permitir que los usuarios registren sus entrenamientos y consulten su progreso sin depender de apuntarlo todo en papel.

**2. ¿Quién utilizaría la web?**  
Personas que entrenan en gimnasios, tanto principiantes como usuarios experimentados.

**3. ¿Cómo se identificarían los usuarios?**  
La idea es utilizar una tarjeta NFC o un código QR.

**4. ¿El NFC registra las repeticiones?**  
No. El NFC identifica al usuario; para registrar automáticamente el ejercicio harían falta sensores o integración con las máquinas.

**5. ¿Qué sucedería si una máquina no tuviera sensores?**  
El usuario podría introducir manualmente el peso, las series y las repeticiones.

**6. ¿Se podría utilizar desde el móvil?**  
Sí, porque la intención es consultarlo mientras se entrena.

**7. ¿Qué información mostraría cada máquina?**  
Su nombre, código, gimnasio, ubicación, músculos trabajados y datos de entrenamiento.

**8. ¿Todas las funciones estarán disponibles desde el principio?**  
No. Primero desarrollaré un prototipo HTML y después añadiré las funcionalidades progresivamente.

**9. ¿Qué ocurriría con la privacidad de los entrenamientos?**  
En una versión futura debería haber controles para decidir qué datos son privados y cuáles se comparten.

**10. ¿Qué diferencia a SpiderGym de una aplicación de rutinas?**  
La intención de relacionar los entrenamientos con máquinas físicas identificadas individualmente.

**Tres mejoras propuestas para la memoria:**

- Distinguir claramente la identificación NFC/QR del registro automático mediante sensores.
- Explicar que existe una alternativa de registro manual.
- Separar las funcionalidades futuras de las que realmente están implementadas.

**Reflexión propuesta:** Esta entrevista me ha servido para definir mejor el alcance del proyecto y evitar prometer funcionalidades que todavía no puedo desarrollar.

## IA-3. Crítica del menú de navegación

**Prompt:** Analiza la navegación de SpiderGym desde la usabilidad y la accesibilidad y propón hasta tres mejoras.

**Menú previsto en la memoria:**

Inicio | Máquinas | Rutinas | Mi progreso | Comunidad | Mi perfil | Contacto

**Menú implementado actualmente:**

Inicio | Máquinas

El resto de secciones están planificadas para próximas fases.

| Sugerencia de IA | Decisión propuesta | Motivo |
|---|---|---|
| Añadir migas de pan | Aceptada y aplicada | Permiten saber dónde estamos dentro de la estructura de la web. |
| Añadir «Saltar al contenido» | Aceptada, pendiente de implementar | Ayudaría a navegar más rápido mediante teclado. |
| Crear varios menús desplegables | Rechazada por ahora | Añadirían complejidad innecesaria a un prototipo con pocas páginas. |

**Cambio realizado:** En la ficha de Extensión de piernas he añadido la ruta Inicio → Máquinas → Extensión de piernas.

**Reflexión:** Las migas de pan son la mejora que más me ha gustado porque ayudan a orientarse sin llenar el menú principal de enlaces.

## IA-4. Comprender el HTML con ayuda de IA

**Prompt:** Soy principiante de ASIX. Explícame las etiquetas de mi página de SpiderGym y los conceptos `lang`, `alt` y `viewport`.

**Resumen de la explicación:**

El documento empieza con `<!DOCTYPE html>` para indicar que utiliza HTML5. Después, `<html>` contiene toda la página. Dentro de `<head>` están los metadatos y el título del navegador. En `<body>` está el contenido visible.

**Mini glosario de cinco términos:**

| Término | Explicación con palabras sencillas |
|---|---|
| `lang` | Indica el idioma de la página. |
| `alt` | Describe una imagen para quien no puede verla. |
| `viewport` | Ayuda a adaptar la página a pantallas de distintos tamaños. |
| `<nav>` | Identifica una zona destinada a navegar por la web. |
| `<main>` | Contiene la parte principal de la página. |

**Reflexión propuesta:** Ahora entiendo mejor la diferencia entre el contenido que aparece en la página y la información que dejamos en el código para el navegador.

## IA-5. Generación de un menú accesible

**Prompt:** Genera un menú HTML semántico para SpiderGym con `aria-label`, `aria-current` y un enlace para saltar al contenido. Explica para qué sirve cada elemento.

**Propuesta generada por ChatGPT:**

```html
<a href="#contenido">Saltar al contenido</a>

<header>
    <h1>SpiderGym</h1>

    <nav aria-label="Navegación principal">
        <a href="index.html" aria-current="page">Inicio</a>
        <a href="maquinas.html">Máquinas</a>
    </nav>
</header>

<main id="contenido">
    <h2>Bienvenido a SpiderGym</h2>
    <p>Datos que te hacen más fuerte.</p>
</main>
```

**Explicación:**

- El primer enlace permite ir directamente al contenido.
- `<header>` contiene la cabecera.
- `<h1>` identifica el título principal.
- `<nav>` contiene la navegación.
- `aria-label` identifica el menú.
- `aria-current="page"` señala que estamos en Inicio.
- `id="contenido"` permite que funcione el enlace «Saltar al contenido».

**Decisión:** Mantener el menú sencillo mientras no existan las demás páginas. Añadir el enlace de salto como próxima mejora.

**Verificación pendiente:** Ejecutar un validador HTML y guardar el informe. Este fragmento todavía no se ha añadido íntegramente al proyecto.

## IA-6. Encontrar errores HTML

**Prompt:** Genera una página de SpiderGym con cinco errores intencionados de estructura o accesibilidad.

**Ejemplo generado para practicar:**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>SpiderGym</title>
</head>
<body>
    <h1>SpiderGym</h1>
    <h3>Máquinas</h3>

    <img src="img/extension-piernas.png">

    <a href="maquinas.html">Haz clic aquí</a>

    <table>
        <tr>
            <td>Gimnasio</td>
            <td>Máquina</td>
        </tr>
        <tr>
            <td>Norte</td>
            <td>Extensión de piernas</td>
        </tr>
    </table>
</body>
</html>
```

**Cinco errores que hay que detectar:**

| Error | Corrección propuesta |
|---|---|
| Falta el idioma en `<html>` | Añadir `lang="es"`. |
| Se salta de `<h1>` a `<h3>` | Utilizar `<h2>` para el siguiente nivel. |
| La imagen no tiene `alt` | Añadir un texto alternativo descriptivo. |
| El enlace dice «Haz clic aquí» | Utilizar «Ver catálogo de máquinas». |
| La tabla usa `<td>` para los encabezados | Utilizar `<th scope="col">` y añadir un `<caption>` descriptivo. |

**Resultado de referencia:** Hay cinco problemas identificables. **Puntuación personal pendiente**, porque esta es una solución modelo y no una prueba individual realizada sin conocer las respuestas.

**Reflexión propuesta:** Algunos errores no impiden ver una página, pero sí dificultan que sea comprensible y accesible.

## IA-7. Tabla accesible y ficha detallada

**Prompt:** Explícame cómo hacer una tabla accesible de máquinas de gimnasio y simula qué información podría recibir un lector de pantalla.

**Propuesta de la IA:** Utilizar `<caption>` para identificar la tabla, `<thead>` para agrupar los encabezados y `<th scope="col">` para relacionar cada columna con sus datos.

**Aplicación en SpiderGym:** Hemos creado una tabla con los gimnasios ficticios Norte y Sur, las máquinas `MAQ-DEMO-001` y `MAQ-DEMO-002`, sus grupos musculares y ubicaciones. También ampliamos la ficha de Extensión de piernas.

**Simulación textual, no prueba real:** Un lector de pantalla podría identificar el título de la tabla, sus columnas y después los datos correspondientes a cada fila.

**Comprobación real realizada:** Probé VoiceOver con la imagen de Extensión de piernas y escuché cómo leía su descripción alternativa. La revisión detallada de la tabla con VoiceOver quedó pendiente.

**Reflexión:** He aprendido que una tabla accesible no es simplemente colocar datos en filas. También hay que identificar las cabeceras para que su contenido tenga sentido.

## IA-8. Explicar tres conceptos de manera sencilla

**Prompt:** Explícame las rutas relativas, los metadatos Open Graph y JSON mediante analogías sencillas, un ejemplo mínimo y un error habitual.

### Concepto 1. Ruta relativa

**Analogía:** Es como dar indicaciones dentro de un edificio: «sal de esta habitación y entra en la de al lado».

**Ejemplo en SpiderGym:**

```html
<a href="maquinas.html">Máquinas</a>
```

**Error habitual:** Escribir una ruta que no corresponde a la ubicación real del archivo.

**Lo que he entendido:** Sirve para enlazar archivos del proyecto sin escribir su dirección completa en el ordenador.

### Concepto 2. Open Graph

**Analogía:** Es como preparar la tarjeta de presentación de una página web para compartirla.

**Ejemplo:**

```html
<meta property="og:title" content="SpiderGym">
```

**Error habitual:** Pensar que estos metadatos aparecen directamente en el contenido visible de la web.

**Lo que he entendido:** Sirven para describir cómo queremos presentar la página al compartirla. Algunas vistas previas requieren además una URL pública y una imagen.

### Concepto 3. JSON

**Analogía:** Es como una ficha ordenada con campos y valores para guardar información.

**Ejemplo futuro de SpiderGym:**

```json
{
  "codigo": "MAQ-DEMO-001",
  "nombre": "Extensión de piernas",
  "gimnasio": "Gimnasio Norte"
}
```

**Error habitual:** Olvidar comillas o añadir una coma después del último campo.

**Lo que he entendido:** JSON permite almacenar datos de forma estructurada para que una aplicación pueda utilizarlos.

## IA-9. Mini test sobre HTML

**Prompt:** Prepárame diez preguntas tipo test, con cuatro opciones, sobre HTML semántico, accesibilidad y navegación.

**Test de práctica:**

**1. ¿Qué etiqueta identifica una zona de navegación?**  
A) `<main>` · B) `<nav>` · C) `<span>` · D) `<p>`

**2. ¿Qué etiqueta contiene el contenido principal?**  
A) `<main>` · B) `<footer>` · C) `<a>` · D) `<img>`

**3. ¿Para qué sirve `alt`?**  
A) Cambiar el color · B) Crear un título · C) Describir una imagen · D) Ajustar su anchura

**4. ¿Qué indica `aria-current="page"`?**  
A) El color · B) El idioma · C) El tamaño · D) La página actual

**5. ¿Qué etiqueta da título a una tabla?**  
A) `<caption>` · B) `<main>` · C) `<ul>` · D) `<header>`

**6. ¿Qué se utiliza para identificar una cabecera de columna?**  
A) `<td>` · B) `<th scope="col">` · C) `<tr>` · D) `<p>`

**7. ¿Qué significa `lang="es"`?**  
A) Número de enlaces · B) Tipo de imagen · C) Idioma español · D) Nombre del archivo

**8. ¿Para qué sirve el metadato `viewport`?**  
A) Adaptación a pantallas · B) Cambiar la fuente · C) Crear rutas · D) Leer QR

**9. ¿Qué indican las migas de pan?**  
A) El pie de página · B) Todos los clics realizados · C) Las pestañas abiertas · D) La posición dentro de la estructura web

**10. ¿Dónde se colocan normalmente los metadatos?**  
A) `<head>` · B) `<main>` · C) `<footer>` · D) `<nav>`

**Respuestas modelo para practicar:**  
1-B, 2-A, 3-C, 4-D, 5-A, 6-B, 7-C, 8-A, 9-B, 10-A.

**Corrección de la simulación:** 9/10. La respuesta 9 sería incorrecta: las migas de pan muestran la estructura de la web, no el historial exacto de clics. La correcta es D.

**Plan de repaso propuesto:** Repasar la diferencia entre el menú principal, los enlaces a fichas y las migas de pan, especialmente el uso de `aria-current`.

**Importante:** Ese 9/10 es un ejemplo de corrección, no una nota que haya obtenido personalmente en un test real.

## IA-10. Revisar críticamente una respuesta de IA

**Situación real analizada:** Durante nuestra conversación sobre `aria-current`, la explicación inicial de ChatGPT resultó confusa y podía dar a entender que el atributo no debía utilizarse en determinadas subpáginas.

**Pregunta que provocó la revisión:** Si estoy en una subpágina de una máquina, ¿por qué no sigo utilizando `aria-current="page"`?

**Corrección:** El atributo no depende de que una página tenga más subpáginas. Se utiliza para identificar el elemento actual dentro de un conjunto de navegación. En una ruta de migas de pan puede marcar la página final. Si ese último elemento no es un enlace, el atributo es opcional.

**Fuente contrastada:**

- MDN: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-current
- W3C: https://www.w3.org/WAI/ARIA/apg/patterns/breadcrumb/

**Reflexión:** Esta conversación me ha enseñado que la IA también puede explicar algo de manera confusa. Al preguntar varias veces conseguí entender que una cosa es el menú principal y otra la ruta que indica nuestra ubicación dentro de la web.

## Registro resumido del uso de IA

| Fecha | Herramienta | Actividad | Qué se ha trabajado | Verificación o modificación |
|---|---|---|---|---|
| 23/10/2026 | ChatGPT | IA-1 | HTML semántico | Preguntas modelo; corrección personal pendiente |
| 23/10/2026 | ChatGPT | IA-2 | Definición de SpiderGym | Entrevista simulada; revisar memoria |
| 23/10/2026 | ChatGPT | IA-3 | Menú accesible | Migas de pan implementadas |
| 23/10/2026 | ChatGPT | IA-4 | Etiquetas y atributos | Glosario preparado |
| 23/10/2026 | ChatGPT | IA-5 | Menú con salto al contenido | Código propuesto; validación pendiente |
| 23/10/2026 | ChatGPT | IA-6 | Errores HTML | Soluciones modelo; prueba personal pendiente |
| 23/10/2026 | ChatGPT | IA-7 | Tabla y ficha | HTML y capturas; simulación preparada |
| 23/10/2026 | ChatGPT | IA-8 | Rutas, Open Graph y JSON | Tres fichas preparadas |
| 23/10/2026 | ChatGPT | IA-9 | Test de diez preguntas | Simulación corregida; test personal pendiente |
| 23/10/2026 | ChatGPT | IA-10 | Revisión crítica de IA | Explicación de `aria-current` contrastada con MDN y W3C |

**Nota final:** Las respuestas modelo y simulaciones deben revisarse antes de entregar. Las capturas, las pruebas de validación y las puntuaciones personales tienen que corresponder a actividades realmente realizadas.