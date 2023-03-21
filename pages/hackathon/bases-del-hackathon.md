---
title: Bases del Hackathon
lang: es
cover: https://somosnlp.github.io/assets/images/eventos/2303.jpg
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
del Hub de Hugging Face. Habrá que liberar en esta organización todos los datasets, modelos y demos.

4. Define tu proyecto y reúne tu equipo (de 1 a 5 personas). Hay que inscribir los equipos en el canal **#equipos-hackathon** (más info en el canal).

5. Crea tu dataset, te animamos a crear un dataset específicamente para el proyecto aunque también puedes reutilizar o mejorar uno ya existente.

6. Escribe la Dataset Card de tu dataset: inspecciona el dataset y evalúa sesgos.

7. Fine-tuning de un LLM para la tarea que hayas elegido. Pondremos a vuestra disposición GPU VMs, avísanos cuando tengas el dataset listo y tokenizado y esté todo listo para empezar el entrenamiento.

8. Escribe la Model Card de tu modelo: evalúa su calidad, sesgos y huella de carbono.

9. Crea una demo.


## Guía para desarrollar un buen proyecto

### Dataset 
  
- Te animamos a crear un dataset específicamente para tu proyecto aunque también puedes mejorar alguno ya existente o utilizarlo directamente (ojo a las licencias).
- En español o multilingüe.
- Si te animas a etiquetar un dataset te recomendamos utilizar Argilla. El martes 21 haremos un taller donde el CEO te enseñará a utilizar la herramienta y el jueves 23 organizaremos un AMA con una persona del equipo que resolverá tus dudas. Además, el equipo estará atento a Discord para ayudarte.
- Cumplimenta bien la Dataset Card, tendremos en cuenta a la hora de evaluar los proyectos si está si está completa y si incluye temas como una evaluación de los sesgos del dataset.
  
### Modelo

- Haz fine-tuning de un modelo ya existente (no pre-entrenes uno desde cero). En esta edición te animamos a que ajuste un gran modelo del lenguaje (LLM), como BERTIN-GPT-J o BLOOM. El lunes 20 Manu Romero, el mayor contribuidor del Hub de Hugging Face, dará un taller en el que te explicaremos cómo realizar esto.
- En español o multilingüe.
- Si quieres, puedes utilizar la herramienta experimental de HF fuego para entrenar tu modelo directamente desde Spaces.
- Evalúa tu modelo y haz públicos los resultados. Puedes utilizar la herramienta evaluate de HF o un script, ten en cuenta que tendrás que liberarlo.
- Cumplimenta bien la Model Card, a la hora de evaluar los proyectos daremos un punto extra si está completa y se incluyen temas como la evaluación de los sesgos del modelo y del impacto desde el punto de vista climático.

### Demo

- Por último, crea una demo de tu modelo en el hub de HF.
<a
href="https://www.youtube.com/watch?v=Q0t1bNoa0tI&list=PLTA-KAy8nxaB-HA79tlOTRl496_XIlJta"
target="_blank">Aquí</a>
tienes tutoriales para crear demos utilizando gradio, streamlit y flask.
  
### Liberar los proyectos  

IMPORTANTE: Todo el proyecto debe ser liberado en la organización
<a href="https://huggingface.co/organizations/hackathon-somos-nlp-2023/share/YPgLHyEfyVvfnHMYmPbisOqmWTOzQxSDYI"
target="_blank">hackathon-somos-nlp-2023</a>,
esto incluye el dataset, el modelo y la demo.
  

Los scripts de creación/limpieza del dataset y de entrenamiento/evaluación del modelo también deben ser liberados. Puedes esperar al 31 de marzo para evitar problemas de plagio. Incluye un enlace en la Dataset Card o Model Card a los notebooks o scripts utilizados en cada caso. Si los has creado específicamente para el proyecto, súbelos al repo correspondiente.


## 📖 Recursos

Desde el equipo de Somos NLP queremos animarte a participar independientemente de tus conocimientos actuales.
  
Durante los primeros días del hackathon daremos una serie de <b>talleres prácticos</b> mostrándote entre otros cómo hacer fine-tuning de un LLM y cómo etiquetar tu base de datos para que tengas un ejemplo de referencia.
  
<div class="mx-auto my-8 text-center">
<div class="grid grid-cols-2 gap-8 my-1">
<a href="/hackathon/fine-tuning-llms" target="_blank">
<img alt="Fine-tuning LLMs" width="650" height="365"
src="https://somosnlp.github.io/assets/images/eventos/230320_fine_tuning_llms.jpg" />
</a>
<a href="hackathon/etiquetado-de-datos-con-argilla" target="_blank">
<img alt="Etiquetado de datos con Argilla" width="650" height="365"
src="https://somosnlp.github.io/assets/images/eventos/230321_etiquetado_de_datos_con_argilla.jpg" />
</a>
<a href="/hackathon/evaluacion-de-sesgos" target="_blank">
<img alt="Evaluación de sesgos" width="650" height="365"
src="https://somosnlp.github.io/assets/images/eventos/230322_evaluacion_de_sesgos.jpg" />
</a>
</div>
</div>
  
  
  
Organizaremos **AMAs** (del inglés, Ask Me Anything) con expertas y mentores para que puedan solucionar tus dudas.
  
<div class="mx-auto my-8 text-center">
<div class="grid grid-cols-2 gap-8 my-1">
<a href="hackathon/ama-con-natalia-elvira" target="_blank">
<img alt="AMA con Natalia Elvira" width="650" height="365"
src="https://somosnlp.github.io/assets/images/eventos/230323_ama_con_natalia_elvira.jpg" />
</a>
<a href="/hackathon/ama-con-omar-sanseviero" target="_blank">
<img alt="AMA con Omar Sanseviero" width="650" height="365"
src="https://somosnlp.github.io/assets/images/eventos/230327_ama_con_omar_sanseviero.jpg" />
</a>
<a href="/hackathon/ama-con-alejandro-vaca" target="_blank">
<img alt="AMA con Alejandro Vaca" width="650" height="365"
src="https://somosnlp.github.io/assets/images/eventos/230329_ama_con_alejandro_vaca.jpg" />
</a>
</div>
</div>
  
  
  
Además, durante el hackathon estaremos a tu disposición en el canal **#pide-ayuda** de Discord para guiarte y ayudarte a desarrollar tu proyecto.
  
  
Para ayudarte a definir tu proyecto, hemos propuesto algunas ideas en el primer mensaje del canal **#equipos-hackathon**. Además, en nuestra sección de "Recursos" [(somosnlp.org/recursos)](https://somosnlp.org/recursos) puedes encontrar listas de **datasets y modelos open-source**.
  
  
Si quieres ver ejemplos de proyectos, puedes echarle un vistazo a la organización del Hub de HF de la primera edición.

También te animamos a ver los talleres en los que 
<a href="https://www.youtube.com/watch?v=fOQLPuXewzE&list=PLTA-KAy8nxaAbyaBTYK68TZKQLv9V8L8M">equipos ganadores</a>
explican cómo implementaron sus proyectos.
  