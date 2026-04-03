---
title: Cómo contribuir 🚀
description: Ayúdanos a democratizar el PLN en español
date: 2021-07-03T16:00:00.000+00:00
lang: es
duration: 3min
cover: "/images/ilustraciones/undraw_remote_design_team_0hp4.svg"
author: María Grandury
bio: ML Research Engineer y fundadora de SomosNLP
website: https://mariagrandury.com
twitter: https://twitter.com/mariagrandury
linkedin: https://www.linkedin.com/in/mariagrandury
github: https://github.com/mariagrandury
tags: [comunidad]
---

<div class="flex justify-center">
    <img src="/images/ilustraciones/undraw_remote_design_team_0hp4.svg" />
</div>

Nuestra misión es crear y compartir recursos que posibiliten y aceleren el avance del PLN en español. Es un objetivo muy amplio que se puede traducir en:
- Ofrecer formación gratuita y open-source en español
- Promover el interés y el avance del PLN en español con hackathones y otros eventos
- Crear bases de datos o añadir las ya existentes a 🤗 Datasets para hacerlas más accesibles
- Entrenar/fine-tune modelos utilizando dichas bases de datos y añadirlos al 🤗 Model Hub
- Crear tutoriales explicando cómo hacer uso de estos recursos o traducir tutoriales ya existentes
- Dar visibilidad a los proyectos de nuestros miembros
- Organizar grupos de estudio para aprender en comunidad y grupos donde debatir el estado del arte del PLN
- Compartir eventos, artículos y proyectos interesantes para la comunidad

## Datasets
Ahora mismo hay [7 datasets monolingües en español](https://huggingface.co/datasets?filter=languages:es,multilinguality:monolingual).

Cómo contribuir a la librería 🤗 Datasets:
- Completar la documentación de las bases de datos ya existentes
- Añadir una base de datos a la librería
- Crear una nueva base de datos

#### Completar la documentación de las bases de datos ya existentes
El README de cada base de datos se llama Dataset Card y contiene información referente al uso, la estructura, la creación, la licencia y la citación de dicha base de datos.

Todas las Dataset Cards siguen una misma [plantilla](https://github.com/huggingface/datasets/blob/master/templates/README_guide.md) y cuanto más completas estén, mejor
(e.g. [Dataset Card for ELI5](https://github.com/huggingface/datasets/tree/master/datasets/eli5#dataset-card-for-eli5)). 
Si encuentras información que todavía no está incluida en la Dataset Card de cualquier base de datos, crea una Merge Request con tu aportación.

#### Añadir una base de datos a la librería
Si quieres añadir una base de datos a la librería de HF, solo tienes que:
1. Añadir una nueva fila a la hoja de cálculo* con la información de dicha base de datos y poner tu nombre en la columna "Contribuyente"
2. Seguir las instrucciones detalladas en [este documento](https://github.com/huggingface/datasets/blob/master/ADD_NEW_DATASET.md)

Si quieres sugerir la adición de una base de datos a la librería añade una nueva fila en la hoja de cálculo* y 
deja la columna "Contribuyente" en blanco para que otra persona pueda trabajar en ello.

*El enlace a la hoja de cálculo está en la descripción del canal #datasets de la comunidad de Discord.

#### Crear una nueva base de datos
Si tienes una idea para crear una nueva base de datos de PLN en español estás en el sitio adecuado:
1. Comparte tu idea en el canal #datasets de la comunidad de [Discord](https://discord.com/invite/my8w7JUxZR)
2. Reúne un equipo para hacerla realidad
3. Añádela a la librería de Hugging Face

## Modelos
Ahora mismo hay [321 modelos en español](https://huggingface.co/models?filter=es).

Cómo añadir tu modelo al 🤗 Model Hub:
1. Entrena/fine-tune tu modelo (echa un vistazo a los [datasets en español](https://huggingface.co/datasets?filter=languages:es,multilinguality:monolingual))
2. Sigue las instrucciones de [esta página](https://huggingface.co/transformers/model_sharing.html) para compartir tu modelo y subirlo al Hub

Recuerda detallar bien la Model Card, puedes utilizar [esta plantilla](https://github.com/huggingface/model_card).

Si tienes más dudas echa un vistazo a [Model Hub docs](https://huggingface.co/docs).


## Tutoriales
Tanto si quieres crear un tutorial desde cero como si quieres traducir uno:
1. Comparte tu idea en el canal #tutoriales de la comunidad de [Discord](https://discord.com/invite/my8w7JUxZR)
2. Reúne un equipo para hacerla realidad
3. Crea un repositorio con el nombre del nuevo tutorial
4. Crea un README.md con la información del tutorial
5. ¡Y a trabajar!
Al terminar, te animamos a abrir una [PR](https://github.com/somosnlp/somosnlp.org) para añadir el tutorial a nuestro blog.

## Eventos
Si te interesa dar una charla o taller relacionado con el PLN contáctanos, estaremos encantados de aprender de tu experiencia.

➡️ **[Call for talks](https://forms.gle/YpUvifDNLG6E56Cy9?typeform-source=localhost)**
