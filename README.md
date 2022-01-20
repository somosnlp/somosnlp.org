[![Netlify Status](https://api.netlify.com/api/v1/badges/a1a287d2-c2b8-4a1f-991d-0c1c73d2aa72/deploy-status)](https://app.netlify.com/sites/nlp-en-es/deploys)

# NLP en ES

<p align='center'>
  <img src='https://raw.githubusercontent.com/nlp-en-es/design/main/logo.svg' />
</p>

## Contribuye al blog

Contribuir a nuestro blog es muy fácil y te invitamos a compartir con la comunidad tu conocimiento y experiencia.

Solo tienes que
1. escribir tu artículo en un archivo markdown `.md`
2. incluir los metadatos como el título o tu nombre en el encabezamiento (ejemplo a continuación)
3. abrir una PR para añadir tu artículo a `./pages/blog`

¡Anímate!

### Notebooks

Si tu artículo es aplicado y lo tienes en forma de notebook puedes utilizar la biblioteca `nbconvert` ([repo](https://github.com/jupyter/nbconvert)) para convertirlo en un archivo markdown:
```
jupyter nbconvert --to markdown <nombre_de_tu_notebook>.ipynb 
```

Para añadir el enlace al Colab puedes incluir al comienzo de tu artículo lo siguiente:
```
<a href="<colab_url>" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>
```

### YAML header

Para la vista previa de los artículos y para darte el reconocimiento merecido, hay que incluir los metadatos en un encabezamiento YAML.

Simplemente adapta el siguiente ejemplo y cópialo al principio de tu markdown (antes del enlace a Colab). Los campos sobre el autor o autora son opcionales.
```
---
title: ¡Hola, mundo! 🤗
description: Somos la red internacional de hispanohablantes acelerarando el avance del NLP en español.
date: 2021-07-01T16:00:00.000+00:00
lang: es
duration: 3min
cover: https://nlp-en-es.github.io/assets/logo.svg
author: María Grandury
bio: ML Research Engineer y fundadora de NLP en ES
website: https://mariagrandury.com
twitter: https://twitter.com/mariagrandury
linkedin: https://www.linkedin.com/in/mariagrandury
github: https://github.com/mariagrandury
---
```

### Abrir PR

Una vez tu artículo esté listo, solo tienes que abrir una PR para añadirlo a `./pages/blog`.

Para mayor claridad, te pedimos que la rama empiece por "blog/" (e.g. `blog/hola_mundo`) y el mensaje del commit por "blog: " (e.g. `blog: añadir artículo '¡Hola, mundo!'`). Muchas gracias :)

¡Estamos impacientes por leer lo que tienes que contarnos!


## Desarrollo

### Development

First, install the dependencies with
```bash
pnpm install
```

Then just run
```bash
pnpm dev
```
and visit http://localhost:3333.

### Build

To build the website run
```bash
pnpm build
```
This will generate files in `dist` that are ready to be served.

### Deploy on Netlify

The page is automatically deployed by [Netlify](https://app.netlify.com/start) everytime you push to the `main` branch. All other branches will be depoyed to a preview URL (the link is visible in the corresponding Pull Request).

## Licencia
[MIT License](https://github.com/nlp-en-es/pagina-web/blob/main/LICENSE)
