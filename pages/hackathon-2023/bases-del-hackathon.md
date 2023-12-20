---
title: Bases del Hackathon
description: Todo lo que necesitas saber para presentar un buen proyecto al hackathon
lang: es
cover: https://somosnlp.github.io/assets/images/eventos/230320_hackathon_llms_fecha_extendida.jpg
---

<div class="flex justify-center">
<a href="https://hackathon_somos_nlp_2023.eventbrite.com/?aff=w" target="_blank">
    <img src="https://github.com/somosnlp/assets/raw/main/images/eventos/230320_hackathon_llms_fecha_extendida.jpg"
        width="650" height="365" alt="Cartel del Hackathon 2023" />
</a>
</div>

El objetivo del hackathon es crear recursos abiertos de PLN en español, a poder ser aprovechando el potencial de los grandes modelos del lenguaje para desarrollar un proyecto enfocado a alguno de los Objetivos de Desarrollo Sostenible.
  
Cada proyecto estará compuesto por un dataset, un modelo y una demo. Todo el proyecto deberá ser liberado.

## Pasos para participar

Participar en nuestro hackathon y aplicar tus conocimientos a una buena causa es muy sencillo, ¡anímate!

1. Únete a nuestra comunidad de
<a href="https://discord.com/invite/my8w7JUxZR" target="_blank">Discord</a>
y crea una cuenta en
<a href="https://huggingface.co/join" target="_blank">Hugging Face</a>.

2.  Regístrate en
<a href="https://www.eventbrite.com/e/registro-hackathon-somos-nlp-2023-los-llms-hablan-espanol-605939269667"
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

7. Fine-tuning de un LLM para la tarea que hayas elegido y *push to hub*. Pondremos a vuestra disposición GPU VMs 24GB, avísanos cuando tengas el dataset y esté todo listo para empezar el entrenamiento.

8. Escribe la Model Card de tu modelo: evalúa su calidad, sesgos y huella de carbono.

9. Crea una demo para mostrar tu proyecto a la comunidad. Puedes utilizar GPUs Nvidia T4 - small.

10. Entrega tu proyecto
<a href="https://forms.gle/nJEoNyuHBTGQrUjt9" target="_blank">rellenando este formulario</a>.
Puedes seguir haciendo modificaciones hasta las 23h59 *Anywhere on Earth* del domingo 9 de abril (revisaremos la hora de los commits 👀).


## Guía y recursos para desarrollar un buen proyecto

Define tu proyecto teniendo en cuenta que valoraremos el impacto social del mismo, que hay una mención de honor al mejor dataset etiquetado y otra al proyecto con más posibilidades de llegar al mercado.

### Dataset 

- En español o multilingüe.
- Te animamos a crear un dataset específicamente para tu proyecto aunque también puedes mejorar alguno ya existente o utilizarlo directamente (ojo a las licencias).
- Si te animas a etiquetar un dataset te recomendamos utilizar Argilla. El equipo ganador de la mención de honor al mejor dataset etiquetado obtendrá 200€ de crédito de computación en el hub de Hugging Face 🏆 *(Taller disponible)*
- Si quieres sumarte al reto colaborativo de limpiar, validar y extender nuestra traducción de **Clean Alpaca**, está todo explicado en la Dataset card de <a href="https://huggingface.co/datasets/somosnlp/somos-clean-alpaca-es" target="_blank">somos-clean-alpaca-es</a>. Si tienes dudas pregúntanos en el canal **#alpaca-es**. *(Vídeo explicativo disponible)*
- Cumplimenta bien la Dataset Card, tendremos en cuenta a la hora de evaluar los proyectos si está completa e incluye temas como una evaluación de los sesgos del dataset.

Recursos:
- <a href="https://somosnlp.org/hackathon-2023/etiquetado-de-datos-con-argilla" target="_blank">Taller práctico: Etiquetado de datos con Argilla</a> impartido por Daniel Vila Suero, co-fundador y CEO @Argilla. *(Grabación ya disponible)*
- <a href="https://somosnlp.org/hackathon-2023/ama-con-natalia-elvira" target="_blank">AMA de etiquetado de datos</a>, pregunta todas tus dudas a Natalia Elvira, Project Manager @Argilla. *(Grabación ya disponible)*
- Reto colaborativo Alpaca ES: <a href="https://www.youtube.com/watch?v=Q-2qsvOEgnA&list=PLTA-KAy8nxaCDc0IJpLac-3csiAepV546" target="_blank">Vídeo explicativo de Argilla (10 mins)</a>, <a href="https://platzi.com/blog/ayuda-a-mejorar-los-llm-en-espanol-en-7-sencillos-pasos/" target="_blank">Explicación en 7 pasos de Platzi</a>

  
### Modelo

- En español o multilingüe.
- Haz fine-tuning de un modelo ya existente (no pre-entrenes uno desde cero). En esta edición te animamos a que ajuste un gran modelo del lenguaje (LLM). *(Taller disponible)*
- Desde el lunes 3 al domingo 9 tendréis a vuestra disposición GPU VMs 24GB patrocinadas por Q Blocks para entrenar vuestro modelo final. *(Taller disponible)*
- Herramientas HF: Ahora se pueden ejecutar notebooks en el hub de HF. Si quieres, también puedes utilizar la herramienta experimental de HF fuego para entrenar tu modelo directamente desde Spaces.
- Evalúa tu modelo y haz públicos los resultados. Puedes utilizar la herramienta evaluate de HF o un script, ten en cuenta que tendrás que liberarlo.
- Cumplimenta bien la Model Card, a la hora de evaluar los proyectos daremos un punto extra si está completa y se incluyen temas como la evaluación de los sesgos del modelo y del impacto desde el punto de vista climático.
- Para tener más posibilidades de ganar una beca para el programa de incubación patrocinado por AgilMentor, puede incluir tu canvas de modelo de negocio, [Lucas te explica cómo](https://www.youtube.com/watch?v=oQnu5aE4_8M&list=PLTA-KAy8nxaCDc0IJpLac-3csiAepV546&t=1647s).

Recursos:
- <a href="https://somosnlp.org/hackathon-2023/fine-tuning-llms" target="_blank">Taller práctico: Fine-tuning de grandes modelos de lenguaje</a> impartido por Manu Romero, el mayor contribuidor del Hub de Hugging Face. *(Grabación ya disponible)*
- <a href="https://somosnlp.org/hackathon-2023/what-is-q-blocks" target="_blank">Taller: How to get started with Q Blocks</a> impartido por Gaurav Vij, Head of Product & Co-founder de Q Blocks.
- <a href="https://somosnlp.org/hackathon-2023/evaluacion-de-sesgos" target="_blank">Detección y mitigación de sesgos en modelos de lenguaje</a> impartido por María Grandury, ML Research Engineer en neurocat y fundadora de Somos NLP. *(Grabación ya disponible)*
- Para evaluar la huella de carbono del entrenamiento de tu modelo puedes utilizar herramientas como
<a href="https://mlco2.github.io/impact" target="_blank">ML CO2 Impact</a> o 
<a href="https://codecarbon.io" target="_blank">Code Carbon</a>,
integrada en 🤗 Transformers. Te recomendamos este
<a href="https://www.youtube.com/watch?v=ftWlj4FBHTg" target="_blank">vídeo</a>
de motivación, este
<a href="https://huggingface.co/blog/carbon-emissions-on-the-hub" target="_blank">artículo</a>
del blog de HF y la sección de la
<a href="https://huggingface.co/docs/hub/model-cards-co2" target="_blank">documentación</a>
 de 🤗 Transformers que trata este tema.


### Demo

- Por último, crea una demo de tu modelo en el hub de HF. Si es tu primera demo, te recomendamos utilizar Gradio ya que es más sencillo.
- Puedes utilizar GPUs Nvidia T4 - small patrocinadas por Hugging Face.
- Qué incluir en la demo: motivación, número de ODS si procede, enlace al dataset y modelo utilizados, miembros del equipo

Recursos:
- Notebook: <a href="https://somosnlp.org/recursos/tutoriales/06_demos_con_gradio" target="_blank">Cómo crear una demo con Gradio</a>
- Vídeo tutoriales: <a href="https://www.youtube.com/watch?v=Q0t1bNoa0tI&list=PLTA-KAy8nxaB-HA79tlOTRl496_XIlJta" target="_blank">Aquí</a>
tienes tutoriales para crear demos utilizando Gradio, Streamlit y Flask.

### Visibilidad

- Te recomendamos que subas tus datasets, modelos y demos desde el principio a la org
<a href="https://huggingface.co/organizations/hackathon-somos-nlp-2023" target="_blank">hackathon-somos-nlp-2023</a>
para que aparezcan en la
<a href="https://huggingface.co/spaces/hackathon-somos-nlp-2023/leaderboard"
target="_blank">leaderboard</a>
y todo el mundo pueda verlo y darle likes. Habrá una mención de honor al proyecto con más ❤️
- Puedes compartir tu proyecto en el canal #nuestros-proyectos.
- Si quieres compartir tu proyecto en redes utiliza el hashtag #HackathonSomosNLP y menciona a Somos NLP para que le demos más visibilidad.

## FAQ

### Inscribir un equipo

Todos los equipos tienen que inscribirse en el canal #equipos-hackathon. Una vez completo el equipo crearemos un canal en la sección HACKATHON-2023-EQUIPOS para que podáis organizaros y desarrollar vuestro proyecto.

Para ayudarte a definir tu proyecto, hemos propuesto algunas ideas en el primer mensaje del canal #equipos-hackathon. Si quieres ver ejemplos de proyectos, puedes echarle un vistazo a la organización del Hub de HF de la primera edición. También te animamos a ver los talleres en los que
<a href="https://www.youtube.com/watch?v=fOQLPuXewzE&list=PLTA-KAy8nxaAbyaBTYK68TZKQLv9V8L8M" target="_blank">equipos ganadores</a>
explican cómo implementaron sus proyectos.

### Liberar los proyectos  

IMPORTANTE: Todo el proyecto debe ser liberado en la organización
<a href="https://huggingface.co/organizations/hackathon-somos-nlp-2023"
target="_blank">hackathon-somos-nlp-2023</a>,
esto incluye el dataset, el modelo y la demo. Si no formas parte todavía haz click en "Request to join".

Los scripts de creación/limpieza del dataset y de entrenamiento/evaluación del modelo también deben ser liberados. Puedes esperar al 31 de marzo para evitar problemas de plagio. Incluye un enlace en la Dataset Card o Model Card a los notebooks o scripts utilizados en cada caso. Si los has creado específicamente para el proyecto, súbelos al repo correspondiente.

---

Para más info sobre talleres, AMAs, keynotes, premios y patrocinios, visita la 
<a href="https://somosnlp.org/hackathon" target="_blank">página del hackathon</a>.
