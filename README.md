# SpiderGym

Proyecto de Lenguajes de Marcas de primero de ASIX. SpiderGym es una propuesta de
gimnasio inteligente para registrar y consultar entrenamientos mediante máquinas
conectadas. Los usuarios podrán identificarse mediante NFC o QR y consultar
series, repeticiones, peso y descansos.

## Quincena 2 de LMSGI — Entrega 02

Primera versión navegable del proyecto utilizando HTML semántico, sin CSS ni
JavaScript. Esta entrega muestra la entidad **máquina** mediante un catálogo y
una página de detalle.

- `index.html`: presentación del proyecto.
- `maquinas.html`: catálogo de máquinas.
- `maquina-extension-piernas.html`: ficha de la máquina de extensión de piernas.

Se utilizan encabezados, párrafos, listas, enlaces con rutas relativas e imágenes
con texto alternativo. El contenido se organiza con `header`, `nav`, `main`,
`article` y `footer` según corresponde en cada página.

El registro de entrenamientos, NFC y QR son funciones previstas del proyecto;
esta entrega contiene páginas HTML estáticas.

## Estructura del repositorio

```text
SpiderGym/
├── index.html
├── maquinas.html
├── maquina-extension-piernas.html
├── README.md
├── img/
│   ├── logo-spidergym.jpg
│   └── extension-piernas.png
├── evidencias/
│   └── comprobacion-quincena-2.md
├── docs/                        # Actividades de la Quincena 1
└── Boceto app Spider Gym.jpeg    # Boceto inicial
```

Las páginas HTML están en la raíz del repositorio. Se conserva la documentación
de la Quincena 1.

## Cómo abrir y comprobar la entrega

1. Descargar el repositorio completo o clonarlo:
   `git clone https://github.com/Alex-developer-150624/SpiderGym.git`.
2. Abrir `index.html` en un navegador. No requiere instalación ni servidor.
3. Pulsar **Máquinas**, abrir **Ver detalle** en Extensión de piernas y volver al
   catálogo. Comprobar también el enlace **Inicio**.
4. Comprobar que aparecen el logotipo y la fotografía de la máquina.

La comprobación local de estructura, enlaces e imágenes está documentada en
[`evidencias/comprobacion-quincena-2.md`](evidencias/comprobacion-quincena-2.md).

## Decisiones técnicas

- Usar HTML semántico para que cada parte del contenido tenga una función clara.
- Mantener las tres páginas en la raíz y utilizar rutas relativas para poder
  abrir el sitio localmente y trasladarlo sin cambiar los enlaces.
- Guardar las imágenes en `img/` y añadir texto alternativo a cada una.

## Uso de IA en esta preparación

Se ha utilizado Codex para preparar la subida a GitHub, corregir la ubicación de
la cabecera de `index.html` dentro de `body`, ajustar los nombres de las imágenes a sus formatos reales, actualizar este README y comprobar
los enlaces, las imágenes y la estructura básica mediante Python. El resultado
de esa comprobación se guarda en `evidencias/`. No se han implementado las
funciones futuras de registro de entrenamientos.

## Estado del proyecto

Primera versión HTML navegable. El proyecto continuará ampliándose durante las
siguientes quincenas.
