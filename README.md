# SpiderGym 🕷️💪

**Datos que te hacen más fuerte.**

## 1. Descripción del proyecto

SpiderGym es un proyecto desarrollado para el ciclo de **Administración de Sistemas Informáticos en Red (ASIX)**, dentro del módulo de **Lenguajes de Marcas y Sistemas de Gestión de Información (LMSGI)**.

La idea es crear un sistema para gimnasios que permita relacionar las máquinas de entrenamiento con los usuarios y registrar su actividad física.

En el futuro, cada máquina podría identificarse mediante un código QR o NFC para asociar el entrenamiento al perfil correspondiente.

El objetivo es que los usuarios puedan consultar sus rutinas, registrar ejercicios y comprobar su evolución.

## 2. Objetivos

- Crear una web sencilla y fácil de utilizar.
- Mostrar un catálogo de máquinas de gimnasio.
- Ofrecer información detallada de cada máquina.
- Identificar individualmente las máquinas.
- Facilitar el registro y seguimiento de entrenamientos.
- Mejorar la accesibilidad y la organización de la información.
- Aprender HTML y aplicar los contenidos de LMSGI.

## 3. Estado actual del proyecto

**Versión:** Prototipo HTML — Quincena 3.

Actualmente SpiderGym es una web estática desarrollada con HTML5. No dispone todavía de una base de datos ni de conexiones reales con máquinas de gimnasio.

### Páginas implementadas

**Inicio — `index.html`**

Presenta el proyecto SpiderGym y permite acceder al catálogo.

**Máquinas — `maquinas.html`**

Contiene un catálogo básico y una tabla con información de ejemplo sobre máquinas, gimnasios y ubicaciones.

**Extensión de piernas — `maquina-extension-piernas.html`**

Muestra la ficha de una máquina con su imagen, identificación, gimnasio, ubicación, grupo muscular y funcionamiento previsto.

### Datos ficticios

Para demostrar cómo podría funcionar el sistema utilizamos estos ejemplos:

| Código | Gimnasio | Máquina | Ubicación |
|---|---|---|---|
| MAQ-DEMO-001 | Gimnasio Norte | Extensión de piernas | Zona A |
| MAQ-DEMO-002 | Gimnasio Sur | Extensión de piernas | Zona B |

Estos datos son ficticios y se utilizan únicamente para el prototipo.

## 4. Tecnologías utilizadas

- **HTML5:** estructura y contenido de las páginas.
- **Visual Studio Code:** edición del código.
- **Safari:** visualización y pruebas.
- **Git y GitHub:** control de versiones y almacenamiento del proyecto.
- **Markdown:** documentación.
- **ChatGPT:** apoyo al aprendizaje, explicación de conceptos y revisión de propuestas.

Por ahora no se ha incorporado CSS ni JavaScript.

## 5. Accesibilidad y mejoras de la Quincena 3

Durante esta quincena se han trabajado las siguientes mejoras:

- Uso de etiquetas semánticas como `header`, `nav`, `main`, `article` y `footer`.
- Declaración del idioma mediante `lang="es"`.
- Incorporación de metadatos `description` y `viewport`.
- Incorporación de metadatos Open Graph.
- Creación de una tabla con título y encabezados.
- Mejora del texto alternativo de la imagen.
- Identificación del menú principal mediante `aria-label`.
- Uso de `aria-current="page"` cuando corresponde.
- Incorporación de migas de pan en la ficha de Extensión de piernas.
- Comprobación manual de los enlaces principales.

También se ha probado con **VoiceOver** la lectura del texto alternativo de la imagen.

Quedan pendientes la validación completa de HTML y otras comprobaciones de accesibilidad.

## 6. Funcionamiento previsto de NFC y QR

La idea es que el usuario se identifique en una máquina mediante NFC o QR.

Es importante distinguir dos funciones:

- **Identificación:** NFC o QR permitirían identificar al usuario o la máquina.
- **Registro del entrenamiento:** para detectar automáticamente repeticiones, peso u otros datos serían necesarios sensores o sistemas compatibles.

Como alternativa, SpiderGym podría permitir introducir los datos manualmente.

**Estas funcionalidades todavía no están implementadas.** Forman parte de la propuesta futura del proyecto.

## 7. Funcionalidades futuras

La planificación de SpiderGym contempla:

- Rutinas personalizadas.
- Historial de entrenamientos.
- Estadísticas de progreso.
- Perfil personal.
- Comunidad de usuarios.
- Identificación mediante NFC o QR.
- Registro manual o automático de ejercicios.
- Posible incorporación de funciones de inteligencia artificial.

Estas funciones se desarrollarán progresivamente y no deben confundirse con las disponibles en el prototipo actual.

## 8. Estructura del proyecto

```text
SpiderGym/
├── index.html
├── maquinas.html
├── maquina-extension-piernas.html
├── README.md
├── img/
│   ├── logo-spidergym.jpg
│   └── extension-piernas.png
├── docs/
│   ├── auditoria-accesibilidad.md
│   ├── registro-errores.md
│   └── registro-ia.md
└── evidencias/
    ├── tabla-maquinas.png
    └── ficha-maquina.png
```

La carpeta `docs` contiene documentación del trabajo realizado y `evidencias` reúne capturas y pruebas del proyecto. Pueden añadirse otros documentos y subcarpetas conforme avance la entrega.

## 9. Cómo visualizar SpiderGym

Para consultar el prototipo:

1. Descargar o clonar el repositorio.
2. Abrir la carpeta SpiderGym.
3. Abrir `index.html` con un navegador.
4. Utilizar el menú para acceder a Máquinas.
5. Seleccionar «Ver detalle» en Extensión de piernas para consultar su ficha.

No es necesario instalar un servidor para visualizar las páginas HTML actuales.

## 10. Uso de inteligencia artificial

Durante el desarrollo se ha utilizado ChatGPT como herramienta de apoyo para:

- Resolver dudas sobre HTML.
- Comprender las etiquetas semánticas.
- Aprender conceptos de accesibilidad.
- Revisar la navegación.
- Proponer mejoras.
- Explicar el funcionamiento de NFC y QR.
- Preparar ejercicios y actividades de aprendizaje.

Las propuestas de IA se revisan antes de incorporarlas al proyecto.

El registro de IA recoge tanto actividades trabajadas como ejercicios preparados que todavía pueden requerir revisión o evidencias adicionales.

## 11. Documentación y evidencias

Se han preparado registros sobre accesibilidad, errores corregidos y utilización de IA.

También se han guardado capturas de la tabla de máquinas y de la ficha de Extensión de piernas.

Antes de la entrega final se revisarán la memoria descriptiva, las actividades de IA, sus evidencias y la documentación del repositorio.

## 12. Conclusión

SpiderGym es un proyecto en desarrollo que me permite aprender HTML y comprender cómo organizar una aplicación web.

Durante la tercera quincena he mejorado la estructura, navegación, accesibilidad y documentación de las páginas.

El objetivo es continuar ampliándolo poco a poco, entendiendo el código y utilizando la inteligencia artificial como herramienta de apoyo al aprendizaje.

---

**Proyecto SpiderGym — ASIX — LMSGI**

*Datos que te hacen más fuerte.*