# Qué bien que quieras contribuir a nuestra página web 💛

Aquí te explicamos cómo:

- Publicar tu artículo o tutorial en nuestro blog
- Contribuir al desarrollo de la página web

## 💡 Publicar un artículo en el blog

Gracias por compartir con la comunidad tu conocimiento y experiencia, ¡contribuir a nuestro blog es muy fácil!

Si no tienes GitHub, mándanos el artículo por correo a <info@somosnlp.org>. Si tienes GitHub:

1. Escribe tu artículo o tutorial en un archivo markdown `.md`
2. Incluye los metadatos como el título o tu nombre en el YAML header (ejemplo a continuación)
3. Abre una PR para añadir tu artículo a `./pages/blog`

### Notebooks

Si tu artículo es aplicado y lo tienes en forma de notebook puedes utilizar la biblioteca `nbconvert` ([repo](https://github.com/jupyter/nbconvert)) para convertirlo en un archivo markdown:

```
jupyter nbconvert --to markdown <nombre_de_tu_notebook>.ipynb 
```

Para añadir el enlace al Colab puedes incluir al comienzo de tu artículo lo siguiente:

```
<a href="<colab_url>" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>
```

### YAML header

Para la vista previa de los artículos y para darte el reconocimiento merecido, hay que incluir los metadatos en un encabezamiento YAML.

Simplemente adapta el siguiente ejemplo y cópialo al principio de tu markdown (antes del enlace a Colab). Los campos sobre el autor o autora son opcionales.

```
---
title: ¡Hola, mundo! 🤗
description: Somos la red internacional de hispanohablantes acelerarando el avance del PLN en español.
date: 2021-07-01T16:00:00.000+00:00
lang: es
duration: 3min
cover: https://raw.githubusercontent.com/somosnlp/assets/main/logo.svg
author: María Grandury
bio: ML Research Engineer y fundadora de SomosNLP
website: https://mariagrandury.com
twitter: https://twitter.com/mariagrandury
linkedin: https://www.linkedin.com/in/mariagrandury
github: https://github.com/mariagrandury
---
```

### Abrir PR

Una vez tu artículo esté listo, solo tienes que abrir una PR para añadirlo a `./pages/blog`.

Para mayor claridad, te pedimos que el título de la PR empiece por "Blog:" y el mensaje del commit por "blog: " (e.g. `blog: añadir artículo '¡Hola, mundo!'`).
Muchas gracias :)

¡Estamos impacientes por leer lo que tienes que contarnos!

## 🚀 Contribuir al desarrollo de la página web

También puedes contribuir al diseño y mejora de la propia página web. Si estás buscando ideas, échale un vistazo a los [issues abiertos](https://github.com/somosnlp/somosnlp.org/issues).

Por favor, utiliza ["Semantic Commit Messages"](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716).

### "Development"

Primero asegúrate de que tienes `pnpm`. Después, instala las dependencias del repo
```bash
pnpm install
```

Cuando termine la instalación, ejecuta
```bash
pnpm dev
```

y visita <http://localhost:3333>.

### "Build"

Para construir la página web ejecuta

```bash
pnpm build
```

Esto generará todos los archivos necesarios en la carpeta `dist`.

### "Deploy on Netlify"

[Netlify](https://app.netlify.com/start) despliega automáticamente la página web cada vez que se hace push a `main`.
Al crear tu PR podrás previsualizar la página web haciendo click en el enlace `😎 Deploy Preview` del comentario hecho por el bot de Netlify.

¡Muchas gracias por tu contribución!
