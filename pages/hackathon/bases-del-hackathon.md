---
title: Bases del Hackathon
description: Todo lo que necesitas saber para presentar un buen proyecto al hackathon
lang: es
cover: https://somosnlp.github.io/assets/images/eventos/230320_hackathon_llms_fecha_ext.jpg
---

El objetivo del hackathon es crear recursos abiertos de PLN en español, a poder ser aprovechando el potencial de los grandes modelos del lenguaje para desarrollar un proyecto enfocado a alguno de los Objetivos de Desarrollo Sostenible.
  
Cada proyecto estará compuesto por un dataset, un modelo y una demo. Todo el proyecto deberá ser liberado.

## Pasos para participar

Participar en nuestro hackathon y aplicar tus conocimientos a una buena causa es muy sencillo, ¡anímate!

1. Únete a nuestra comunidad de
<a href="https://discord.com/invite/my8w7JUxZR" target="_blank">Discord</a>
y crea una cuenta en
<a href="https://huggingface.co/join" target="_blank">Hugging Face</a>.

2.  Regístrate en
<a href="https://www.eventbrite.com/e/registro-hackathon-somos-nlp-2023-los-llms-hablan-espanol-565283938477?aff=w"
target="_blank">Eventbrite</a>.

3. Únete a la organización
<a href="https://huggingface.co/organizations/hackathon-somos-nlp-2023/share/YPgLHyEfyVvfnHMYmPbisOqmWTOzQxSDYI"
target="_blank">hackathon-somos-nlp-2023</a>
del Hub de Hugging Face. Tienes que liberar en esta organización todos los datasets, modelos y demos. Te recomendamos que los crees directamente aquí para que aparezcan lo antes posible en la 
<a href="https://huggingface.co/spaces/hackathon-somos-nlp-2023/leaderboard"
target="_blank">leaderboard</a>.

4. Define tu proyecto y reúne tu equipo (de 1 a 5 personas). Hay que inscribir los equipos en el canal **#equipos-hackathon** (más info en el canal).

5. Crea tu dataset en la org del hackathon, te animamos a crear un dataset específicamente para el proyecto aunque también puedes reutilizar o mejorar uno ya existente. 

6. Escribe la Dataset Card de tu dataset: inspecciona el dataset y evalúa sesgos.

7. Fine-tuning de un LLM para la tarea que hayas elegido y *push to hub*. Pondremos a vuestra disposición GPU VMs, avísanos cuando tengas el dataset y esté todo listo para empezar el entrenamiento.

8. Escribe la Model Card de tu modelo: evalúa su calidad, sesgos y huella de carbono.

9. Crea una demo.


## Guía y recursos para desarrollar un buen proyecto

### Dataset 
  
- Te animamos a crear un dataset específicamente para tu proyecto aunque también puedes mejorar alguno ya existente o utilizarlo directamente (ojo a las licencias). Habrá una mención de honor al mejor dataset etiquetado 🏆
- En español o multilingüe.
- Si te animas a etiquetar un dataset te recomendamos utilizar Argilla.
- Martes 21: <a href="hackathon/etiquetado-de-datos-con-argilla" target="_blank">Taller práctico: Etiquetado de datos con Argilla</a> impartido por Daniel Vila Suero, co-fundador y CEO @Argilla. *(Grabación ya disponible)*
- Jueves 23: <a href="hackathon/ama-con-natalia-elvira" target="_blank">AMA de etiquetado de datos</a>, pregunta todas tus dudas a Natalia Elvira, Project Manager @Argilla
- Te recomendamos que subas el dataset desde el principio a la org <a href="https://huggingface.co/organizations/hackathon-somos-nlp-2023"
target="_blank">hackathon-somos-nlp-2023</a> para que aparezca en la leaderboard y todo el mundo pueda verla y darle likes. Habrá una mención de honor al dataset con más ❤️
- Puedes compartir tu dataset en el canal #nuestros-proyectos. Si quieres compartir tu dataset en redes utiliza el hashtag #HackathonSomosNLP y menciona a Somos NLP para que le demos más visibilidad.
- Cumplimenta bien la Dataset Card, tendremos en cuenta a la hora de evaluar los proyectos si está completa y si incluye temas como una evaluación de los sesgos del dataset.
  
### Modelo

- Haz fine-tuning de un modelo ya existente (no pre-entrenes uno desde cero). En esta edición te animamos a que ajuste un gran modelo del lenguaje (LLM), como BERTIN-GPT-J o BLOOM.
- Lunes 20: <a href="hackathon/fine-tuning-llms" target="_blank">Taller práctico: Fine-tuning de grandes modelos de lenguaje</a> impartido por Manu Romero, el mayor contribuidor del Hub de Hugging Face. *(Grabación ya disponible)*
- En español o multilingüe.
- Si quieres, puedes utilizar la herramienta experimental de HF fuego para entrenar tu modelo directamente desde Spaces.
- Te recomendamos que subas el modelo desde el principio a la org <a href="https://huggingface.co/organizations/hackathon-somos-nlp-2023"
target="_blank">hackathon-somos-nlp-2023</a> para que aparezca en la leaderboard y todo el mundo pueda verlo y darle likes. Habrá una mención de honor al modelo con más ❤️
- Puedes compartir tu modelo en el canal #nuestros-proyectos. S quieres compartir tu modelo en redes utiliza el hashtag #HackathonSomosNLP y menciona a Somos NLP para que le demos más visibilidad.
- Evalúa tu modelo y haz públicos los resultados. Puedes utilizar la herramienta evaluate de HF o un script, ten en cuenta que tendrás que liberarlo.
- Cumplimenta bien la Model Card, a la hora de evaluar los proyectos daremos un punto extra si está completa y se incluyen temas como la evaluación de los sesgos del modelo y del impacto desde el punto de vista climático.
- Para evaluar la huella de carbono del entrenamiento de tu modelo puedes utilizar herramientas como [ML CO2 Impact](https://mlco2.github.io/impact/) o [Code Carbon](https://codecarbon.io/), integrada en 🤗 Transformers. Te recomendamos este [vídeo](https://www.youtube.com/watch?v=ftWlj4FBHTg) de motivación, este [artículo](https://huggingface.co/blog/carbon-emissions-on-the-hub) del blog de HF y la sección de la [documentación](https://huggingface.co/docs/hub/model-cards-co2) de 🤗 Transformers que trata este tema.

### Demo

- Por último, crea una demo de tu modelo en el hub de HF. Si es tu primera demo, te recomendamos utilizar Gradio ya que es más sencillo.
- Notebook: <a href="https://somosnlp.org/recursos/tutoriales/06_demos_con_gradio" target="_blank">Cómo crear una demo con Gradio</a>
- Vídeo tutoriales: <a href="https://www.youtube.com/watch?v=Q0t1bNoa0tI&list=PLTA-KAy8nxaB-HA79tlOTRl496_XIlJta" target="_blank">Aquí</a>
tienes tutoriales para crear demos utilizando Gradio, Streamlit y Flask.
- En cuanto crees la demo en la org del hackathon aparecerá en la 
<a href="https://huggingface.co/spaces/hackathon-somos-nlp-2023/leaderboard"
target="_blank">leaderboard</a>, compártela en el canal #nuestros-proyectos y en redes para conseguir más likes. Habrá una mención de honor a la demo con más ❤️
- Si quieres compartir tu demo en redes utiliza el hashtag #HackathonSomosNLP y menciona a Somos NLP para que le demos más visibilidad.

## FAQ

### Inscribir un equipo

Todos los equipos tienen que inscribirse en el canal #equipos-hackathon. Una vez completo el equipo crearemos un canal en la sección HACKATHON-2023-EQUIPOS para que podáis organizaros y desarrollar vuestro proyecto.

Para ayudarte a definir tu proyecto, hemos propuesto algunas ideas en el primer mensaje del canal #equipos-hackathon. Si quieres ver ejemplos de proyectos, puedes echarle un vistazo a la organización del Hub de HF de la primera edición. También te animamos a ver los talleres en los que
<a href="https://www.youtube.com/watch?v=fOQLPuXewzE&list=PLTA-KAy8nxaAbyaBTYK68TZKQLv9V8L8M">equipos ganadores</a>
explican cómo implementaron sus proyectos.

### Liberar los proyectos  

IMPORTANTE: Todo el proyecto debe ser liberado en la organización
<a href="https://huggingface.co/organizations/hackathon-somos-nlp-2023"
target="_blank">hackathon-somos-nlp-2023</a>,
esto incluye el dataset, el modelo y la demo. Si no formas parte todavía haz click en "Request to join".

Los scripts de creación/limpieza del dataset y de entrenamiento/evaluación del modelo también deben ser liberados. Puedes esperar al 31 de marzo para evitar problemas de plagio. Incluye un enlace en la Dataset Card o Model Card a los notebooks o scripts utilizados en cada caso. Si los has creado específicamente para el proyecto, súbelos al repo correspondiente.

---

Para más info sobre talleres, AMAs, keynotes, premios y patrocinios, volver a la 
<a href="https://somosnlp.org/hackathon" target="_blank">página del hackathon</a>.
