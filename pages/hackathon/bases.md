---
title: "Bases del Hackathon #Somos600M"
description: Todo lo que necesitas saber para presentar un buen proyecto al hackathon
lang: es
cover: https://somosnlp.github.io/assets/images/eventos/240301_hackathon_ext.jpg
---

Cada equipo participante generará un corpus de instrucciones, entrenará su LLM y creará una demo para compartir su gran trabajo con la comunidad. Este año el enfoque son proyectos que representen la riqueza del español y la diversidad de las personas hispanohablantes. Como siempre, os animamos a que los proyectos tengan impacto social y estén relacionados con alguno de los Objetivos de Desarrollo Sostenibles de la ONU. ¡Gracias por participar! ✨

<div class="flex justify-center">
<a href="https://hackathonsomosnlp2024.eventbrite.com/?aff=w" target="_blank">
    <img src="https://somosnlp.github.io/assets/images/eventos/240301_hackathon_ext.jpg"
        width="650" height="365" alt="Cartel del Hackathon 2024" />
</a>
</div>

<center><a href="https://hackathonsomosnlp2024.eventbrite.com/?aff=w" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">📝 ¡Inscripciones abiertas hasta el 22 de marzo!</a></center>

## 👀 Maneras de participar

Como sabes, la iniciativa #Somos600M tiene dos objetivos:

### ✅ Crear la primera leaderboard de LLMs

Ayúdanos a validar en comunidad las traducciones hechas por el Grupo de PLN de la Universidad de Oregon de las bases de datos utilizadas en la famosa [Open LLM Leaderboard de Hugging Face](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard).

Gracias al apoyo de Argilla y Hugging Face, en concreto de Álvaro Bartolomé, Ignacio Talavera, Daniel Vila y Omar Sanseviero, colaborar es muy sencillo:

1. Crea una cuenta en [Hugging Face](https://huggingface.co/join) y únete a la organización de SomosNLP con [esta invitación](https://huggingface.co/organizations/somosnlp/share/qgytUhPKvxVxsbZWTzVUAUSUnZmVXNPmjc)
2. Entra en el [entorno de validación](https://huggingface.co/spaces/somosnlp/benchmark-annotation-argilla)
3. Valida la traducción de un párrafo del inglés al español (la traducción ya está hecha, solo tienes que verificar que está bien y corregirla en caso necesario)
4. Repite el paso 3 cuantas veces quieras y mira cómo subes en el [ranking de colaboraciones](https://huggingface.co/spaces/somosnlp/benchmark-annotation-argilla-dashboard)
5. Tu nombre aparecerá como parte del equipo que creó las bases de datos de la futura leaderboard de LLMs en español 🙌

### 🌎 Crear el mayor corpus de instrucciones

Participar en nuestro hackathon y aplicar tus conocimientos a democratizar el PLN en español es muy sencillo, ¡anímate!

1. Únete a nuestra comunidad de [Discord](https://discord.com/invite/my8w7JUxZR). Auto-asígnate el rol "Hackathon24": en el servidor, vete al comienzo de la barra lateral izquierda, haz click en "Canales y roles", selecciona "Participar en el hackathon 2024".
2. Crea una cuenta en [Hugging Face](https://huggingface.co/join) y únete a la organización de [SomosNLP](https://huggingface.co/organizations/somosnlp/share/qgytUhPKvxVxsbZWTzVUAUSUnZmVXNPmjc).
3. Regístrate en [Eventbrite](https://hackathonsomosnlp2024.eventbrite.com/?aff=w).
4. Crea tu equipo o únete a uno (equipos de 1 a 5 personas). Hay que inscribir los equipos en el canal **#encuentra-equipo** (más info en el README del canal).
5. Crea tu corpus de instrucciones y súbelo a la org de hf.co/SomosNLP. Te recomendados utilizar la librería `distilabel` (ver recursos abajo).
6. Escribe la Dataset Card de tu dataset: describe el proceso de creación y curación (incluye el script/notebook), inspecciona el dataset, evalúa y mitiga sesgos.
7. Fine-tune un LLM (hasta 7B) para la tarea que hayas elegido y súbelo a la org de hf.co/SomosNLP. Recomendamos técnicas tipo QLoRA. Pondremos a vuestra disposición GPU VMs para el entrenamiento. 
8. Escribe la Model Card de tu modelo: describe el proceso de entrenamiento (incluye el script/notebook), evalúa su calidad, sesgos y huella de carbono.
9. Crea una demo para mostrar tu proyecto a la comunidad y súbela a la org de hf.co/SomosNLP. Puedes utilizar GPUs Nvidia T4 - small.
10. Entrega tu proyecto rellenando un formulario que publicaremos próximamente. Puedes seguir haciendo modificaciones hasta las 23h59 *Anywhere on Earth* del viernes 29 de marzo (revisaremos la hora de los commits 👀).
- Extra. Puedes presentar tu proyecto al Workshop de LatinX in AI @NAACL, descubre cómo [aquí](https://somosnlp.org/blog/latinx-in-ai-at-naacl-2024).
11. Presenta tu proyecto en 5 minutos ante el jurado y la comunidad.

Nota: Un proyecto completo consiste en corpus de instrucciones + modelo + demo. Igualmente dado el enfoque del hackathon en los datos aceptamos también proyectos que solo hayan creado corpus (más info sobre las evaluaciones a continuación).

A continuación también puedes encontrar una guía para desarrollar un buen proyecto, con requisitos, recomendaciones y recursos.

Si tienes cualquier duda sobre las bases estamos a tu disposición en el canal #pide-ayuda, escribe un título descriptivo y utiliza la etiqueta "hackathon".

¡Mucho éxito! 🚀

## 📝 Guía y recursos para desarrollar un buen proyecto

Recuerda que el objetivo del hackathon es representar la diversidad de las personas hispanohablantes, te animamos a crear corpus que reflejen la riqueza del español, en la medida de lo posible divídelo por países/regiones e incluye ejemplos de diferentes variedades del español.

### 📚 Corpus 

Los datos son lo más importante en el desarrollo de un modelo y también le daremos mayor importancia a la hora de evaluar los proyectos 👀

- En español o lenguas cooficiales.
- Corpus de instrucciones, i.e.: pregunta + respuesta.
- Sube el corpus a hf.co/somosnlp.
- Crea una Dataset Card.
- Sube al repo todos los scripts/notebooks utilizados y explica en la Dataset Card qué es qué.
- En la Dataset Card enlaza el dataset utilizado para el entrenamiento.
- Estructura el corpus como explicamos a continuación.

<details>
<summary>Recomendaciones</summary>

Notación:

- Si vas a crear primero un corpus para una tarea clásica y después lo vas a convertir en instrucciones, llámalos igual añadiendo el sufijo `it` al corpus de instrucciones.
- Si quieres ir un paso más allá y también vas a adaptar el corpus para DPO, sube el corpus de instrucciones con el sufijo `it` y el DPO con el sufijo `dpo`.

Recomendaciones:

- Para crear el corpus te recomendamos utilizar `distilabel`.
- Puedes utilizar los endpoints PRO de Hugging Face como se explica en el notebook de ejemplo (recuerda que tienes que pertenecer a hf.co/somosnlp).
- Si te animas a etiquetar un corpus te recomendamos utilizar `Argilla`.
- Sube el corpus directamente a hf.co/somosnlp e itera ahí.
- Cumplimenta bien la Dataset Card: detalla el proceso de creación y curación, describe el dataset, evalúa y mitiga sesgos. Tendremos en cuenta a la hora de evaluar los proyectos si la documentación está completa e incluye temas como una evaluación de los sesgos (e.g., se ha prestado atención a que las clases estén balanceadas).
- También recomendamos incluir la motivación del proyecto e impacto.

</details>

<details>
<summary>Estructura del corpus</summary>

Por ser corpus de instrucciones cada corpus contará con las siguientes columnas:
- `pregunta`
- `respuesta`

Además, dado el enfoque en las variedades de la lengua del hackathon, también incluiremos las siguientes columnas:

- `idioma` (variedad geográfica): código ISO del idioma ("catalán" = `ca`, "quechua" = `qu`), en caso de ser español hay que especificar la variedad geográfica ("español de México" = `es_mx`, "español de Ecuador" = `es_ec`).
- `registro` (variedad funcional): `coloquial`, `medio` o `culto`
- `periodo` (variedad histórica): si es un corpus en español elegir entre `actual`, `moderno` (ss. XVIII-XIX), `clásico` (ss. XVI-XVII) o `medieval`, si es en otro idioma rellenar si tenéis conocimiento.

Para completar la información de los ejemplos incluiremos también:
- `dominio`: `legal`, `salud` (clínico, biomédico, farmacia), `literatura` (poesía, música, teatro), `sociales` (historia, geografía, etc), `exactas` (física, mates, etc), `prensa`, `cocina`, `filosofia` (ética, lógica, etc), `seguros`, ..., `miscelaneo` (última opción). Si puedes, especifica el subdominio, e.g. `literatura_poesia`, `sociales_historia`.
- `tarea`: `pregunta`, `clasificacion`, `traduccion`, `resumen`, `similitud_semantica`. Si puedes, especifica también la subtarea, e.g. `pregunta_abierta`, `pregunta_opcion_multiple`.
- `país_origen`: país de origen de los datos.
- `país_referencia`: país al que hace referencia la pregunta, si procede.

Si tienes dudas, ¡#pide-ayuda! Si crees que nos hemos dejado alguna categoría avísanos para que la añadamos :)

Si tienes que añadir columnas puedes hacerlo automáticamente utilizando los mismos endpoints que para crear los datasets sintéticos. Acuérdate de revisar las anotaciones automáticas.

</details>

<details>
<summary>Recursos</summary>

- [Notebook: creación de datasets sintéticos con distilabel](https://github.com/somosnlp/recursos/blob/main/hackathon_2024/creacion_de_datasets_sinteticos_con_distilabel.ipynb), creado por Daniel Vila y Agustín Piqueres @Argilla.
- [Taller práctico: distilabel y Argilla, herramientas para crear modelos como Notus](https://www.youtube.com/watch?v=riM3pgV4m_I&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J) impartido por Gabriel Martín, MLE @Argilla (notebook disponible).
- [Notebook: Creación de datasets para SFT y DPO con distilabel y Argilla](https://github.com/somosnlp/recursos/blob/main/hackathon_2024/distilabel_y_argilla_creacion_datasets_para_sft_y_dpo.ipynb), notebook del taller de Gabriel.
- [Notebook: creación de un dataset sintético a partir del PDF del EU AI Act](https://distilabel.argilla.io/latest/tutorials/pipeline-notus-instructions-preferences-legal/), creado por el equipo de Argilla y con traducción WIP por Edison J. Bejarano.
- [Cómo anotar un corpus lingüísticos para entrenar LLMs](https://www.youtube.com/watch?v=d6vrflcIY-g&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J), impartida el miércoles 20 por Marta Guerrero @IIC, creadora de 3 de los corpus que formarán la leaderboard.
- [Taller práctico: Etiquetado de datos con Argilla](https://somosnlp.org/hackathon-2023/etiquetado-de-datos-con-argilla) impartido por Daniel Vila Suero, co-fundador y CEO @Argilla.
- [AMA de etiquetado de datos](https://somosnlp.org/hackathon-2023/ama-con-natalia-elvira) con Natalia Elvira, Project Manager @Argilla.

</details>

### ⚙️ Modelo

- En español o lenguas cooficiales.
- Haz fine-tuning de un modelo ya existente (no pre-entrenes uno desde cero), con las máquinas disponibles puedes ajustar un LLM de hasta 7B.
- Sube el modelo a hf.co/somosnlp.
- Crea la [Model Card](https://huggingface.co/spaces/huggingface/Model_Cards_Writing_Tool).
- Incluye en el repo todos los scripts/notebooks utilizados y explica en la Model Card qué es qué.
- En la Model Card enlaza el corpus utilizado.

<details>
<summary>Recomendaciones</summary>

- Os animamos a entrenar vuestros modelos directamente desde el hub de Hugging Face, ¡tenemos créditos patrocinados por HF! Podéis utilizar [autotrain](https://huggingface.co/docs/autotrain/llm_finetuning) y [jupyterlab](https://huggingface.co/docs/hub/spaces-sdks-docker-jupyter), con GPUs hasta *T4 medium*.
- Recuerda que es muy importante siempre hacer pruebas en máquinas humildes para verificar que el código es correcto y no encontrar bugs después de varias horas de entrenamiento.
- Sube el modelo directamente a hf.co/somosnlp e itera ahí.
- Cumplimenta bien la Model Card: detalla el proceso de entrenamiento, evalúa su calidad, sesgos y huella de carbono.
- También recomendamos incluir la motivación del proyecto e impacto.
- Este año la evaluación corre a nuestro cargo, ¡vuestros modelos inaugurarán la primera leaderboard abierta de LLMs en español!


</details>

<details>
<summary>Recursos</summary>

- [Taller práctico: Fine-tuning de grandes modelos de lenguaje](https://somosnlp.org/hackathon-2023/fine-tuning-llms) impartido por Manu Romero, creador de +500 modelos del Hub de Hugging Face.
- [Taller práctico: El impacto de la calidad de los datos en un FT de LLMs](https://www.youtube.com/watch?v=hPq5NG8kA8w&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J), impartido también por Manu Romero.
- [Taller + AMA sobre entrenamiento de LLMs](https://www.youtube.com/playlist?list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J) con Alejandro Vaca, fundador de LenguajeNaturalAI.
- [Docs: AutoTrain (inglés)](https://huggingface.co/docs/autotrain/llm_finetuning), os animamos a probar esta plataforma no-code de Hugging Face. Vamos a traducir esta sección de la documentación, avisadnos si necesitáis ayuda para comprenderla.
- [Tutorial: AutoTrain + spacerunner (inglés)](https://huggingface.co/blog/stefan-it/autotrain-flair-mobie), con esta combinación podéis correr scripts en AutoTrain. Vamos a traducir el tutorial, avisadnos si necesitáis ayuda para comprenderlo.
- [Docs: Jupyterlab en Spaces](https://huggingface.co/new-space?template=SpacesExamples/jupyterlab), donde podéis correr vuestros notebooks como siempre.
- Notebooks de `unsloth` para entrenar más rápido (en inglés, si necesitáis que los tenga me decís):
[Gemma FT en dataset de instrucciones estilo Alpaca](https://colab.research.google.com/drive/10NbwlsRChbma1v55m8LAPYG15uQv6HLo) y
[Hacer RLAIF via DPO sobre Zephir](https://colab.research.google.com/drive/15vttTpzzVXv_tJwEk-hIcQ0S9FcEWvwP).
- [Space: Model Card Creator](https://huggingface.co/spaces/huggingface/Model_Cards_Writing_Tool), Space que os guía en la creación de vuestra model card.
- [Detección y mitigación de sesgos en modelos de lenguaje](https://somosnlp.org/hackathon-2023/evaluacion-de-sesgos), charla impartida por María Grandury, fundadora de SomosNLP.
- Para evaluar la huella de carbono del entrenamiento de tu modelo puedes utilizar herramientas como [ML CO2 Impact](https://mlco2.github.io/impact) o [Code Carbon](https://codecarbon.io), integrada en 🤗 Transformers. Te recomendamos este [vídeo](https://www.youtube.com/watch?v=ftWlj4FBHTg) de motivación, este [artículo](https://huggingface.co/blog/carbon-emissions-on-the-hub) del blog de HF y la sección de la [documentación](https://huggingface.co/docs/hub/model-cards-co2) de 🤗 Transformers que trata este tema.
- [Ética ambiental en IA: construyendo narrativas sostenibles en español](https://www.youtube.com/watch?v=MJLdrXz6bSE&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J), charla impartida por Jorge Vallego, Project Lead @H4rmony. Os puede servir para darle un enfoque eco-consciente a vuestro dataset.

</details>

### 🖼️ Demo

Crea una demo para que todo el mundo pueda interactuar con tu nuevo modelo.

Recomendaciones: 

- Si es tu primera demo, te recomendamos utilizar Gradio ya que es más sencillo.
- Crea la demo directamente en hf.co/somosnlp e itera ahí.
- Puedes utilizar GPUs `Nvidia T4 - small` patrocinadas por Hugging Face.
- Qué incluir en la demo: motivación del proyecto, impacto, ideas futuras, número de ODS si procede, enlace al dataset y modelo utilizados, miembros del equipo, todo lo que consideres necesario para promocionar tu proyecto :)
- Crea una demo clara e intuitiva.

<details>
<summary>Recursos</summary>

- Docs: [Gradio docs](https://www.gradio.app/docs)
- Notebook: [Cómo crear una demo con Gradio](https://somosnlp.org/recursos/tutoriales/06_demos_con_gradio)
- Vídeo tutoriales: [Aquí](https://www.youtube.com/watch?v=Q0t1bNoa0tI&list=PLTA-KAy8nxaB-HA79tlOTRl496_XIlJta) tienes tutoriales para crear demos utilizando Gradio, Streamlit y Flask.

</details>

### 📝 Paper

- Si quieres presentar tu proyecto al Workshop de LatinX in AI @NAACL, descubre cómo [aquí](https://somosnlp.org/blog/latinx-in-ai-at-naacl-2024).
- Te recomendamos ver el taller ["Preparación de un proyecto de investigación de ML"](https://www.youtube.com/watch?v=QziYfITvGrA&list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG).
- Y también el taller del lunes donde Diana Galván, Chair del Workshop, compartió muchos consejos: ["Taller de escritura de abstracts, LatinX in NLP @NAACL 2024"](https://www.youtube.com/watch?v=0f-wLobIOps&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J)
- Diapositivas del taller disponibles en [github.com/somosnlp/recursos](https://github.com/somosnlp/recursos/blob/main/hackathon_2024/taller_escritura_abstracts_lxai_naacl.pdf)

### 📸 Presentación

- El día 3 de abril tendréis 5 minutos por equipo para presentar vuestro proyecto al jurado y a la comunidad.

### ✨ Visibilidad

- Te recomendamos que subas tus datasets, modelos y demos desde el principio a la org hf.co/somosnlp para que aparezcan en la nueva [❤️ leaderboard](https://huggingface.co/spaces/somosnlp/likes_leaderboard) y todo el mundo pueda verlo y darle likes. ¡Habrá una mención de honor para el proyecto con más ❤️!
- Puedes compartir tu proyecto en el canal #comparte-tu-proyecto.
- Si quieres compartir tu proyecto en redes utiliza el hashtag #Somos600M y menciona a SomosNLP, ¡será un placer darle más visibilidad!

## Evaluación y premios

### 🗓️ Fechas importantes

- 29 de marzo 23h59 *Anywhere On Earth*: Fecha límite para entregar los proyectos al Hackathon #Somos600M (formulario) y al workshop de LatinX in NLP @NAACL (web).
- 3 de abril: Presentación en directo de los proyectos, 5 mins por equipo.
- 10 de abril: Anuncio de los equipos ganadores y envío de los comentario del jurado.
- Próximamente: Presentación en directo de los proyectos ganadores, 30 mins por equipo.

### 🏆 Beneficios y premios

Todas las personas participantes:
- Acceso a los endpoints PRO en Hugging Face para la creación de corpus sintéticos.
- Acceso a GPUs de hasta 25GB de RAM en Hugging Face para el entrenamiento de modelos y la demo.
- Acceso a "persistent storage" en Hugging Face para la creación de espacios de anotación de Argilla.
- Apoyo para presentar tu proyecto al workshop LatinX in NLP @NAACL 2024, una de las conferencias internacionales más importantes de PLN.

Todas las personas que presenten un proyecto:
- Créditos de la MonsterAPI de Q Blocks para entrenamiento de LLMs.
- Descuento
- Descuento de ... para la WomenTech Global Conference 2024.
- Posibilidad de conseguir una nominación para unirse a Nova (comenta tu interés en el formulario de entrega de proyectos).
- Posibilidad de conseguir una entrada completamente gratis para asistir a la WomenTech Global Conference 2024 (comenta tu interés en el formulario de entrega de proyectos).
- Posibilidad de continuar desarrollando tu proyecto con nuestro apoyo, ¡contáctanos!

Equipo 3er puesto:
- 20k créditos de la MonsterAPI de Q Blocks para entrenamiento de LLMs (premio por persona).
- Beca completa para el curso 

Equipo 2o puesto:
- 30k créditos de la MonsterAPI de Q Blocks para entrenamiento de LLMs (premio por persona).
- Beca completa para el curso 

Equipo 1er puesto:
- 50k créditos de la MonsterAPI de Q Blocks para entrenamiento de LLMs (premio por persona).
- Beca completa para el curso 

<!-- Hey Gaurav! Instead of giving 10k credits to 100 participants, what do you think about dividing the 1000k among the winners? (e.g. 50k for the persons in the 1st team, 30k 2nd, ..., 10k for some mentions) -->

### ✅ Evaluación de los proyectos

Corpus (4 ptos):
- Enfoque en las variedades lingüísticas
- Correcta estructura del corpus
- Técnica de creación del corpus
- Claridad y reproducibilidad de los scripts
- Completitud de la Dataset Card
- Calidad del corpus

Modelo (3 ptos):
- Método de entrenamiento utilizado
- Claridad y reproducibilidad de los scripts
- Completitud de la Model Card
- Evaluación del modelo

Demo (1 pto):
- Claridad y UX de la demo

Proyecto y presentación (2 ptos):
- Motivación, originalidad e impacto social
- Claridad y calidad de la exposición

## ❓ Preguntas frecuentes

<details>
<summary>¿Por qué debería participar?</summary>

Al unirte a este hackathon tendrás la oportunidad de:

- ✅ Comprender cómo funcionan los grandes modelos del lenguaje (LLMs) y descubrir los retos de cada etapa de su desarrollo: creación del corpus, entrenamiento y evaluación
- ✅ Participar en la creación del mayor corpus de calidad y diverso que incluya las distintas variedades del español y lenguas cooficiales (top como experiencia y top para el CV)
- ✅ Ser parte del equipo que cree algunas de las bases de datos de la primera leaderboard pública de LLMs en español
- ✅ Resolver todas tus dudas sobre PLN durante sesiones de mentoría "Ask My Anything"
- ✅ Recibir apoyo para presentar tu trabajo en un paper
- ✅ Ganar premios para seguir creciendo como profesional y conseguir un certificado que poder compartir en LinkedIn
- ✅ Unirte a la mayor comunidad de hispanohablantes que estudian, trabajan e investigan en PLN

</details>

<details>
<summary>¿Cuál es el nivel necesario?</summary>

Desde el equipo de SomosNLP queremos animarte a participar independientemente de tus conocimientos actuales. En ediciones anteriores hemos contado con grupos de institutos de investigación y grupos de estudiantes de grado, ¡todos los proyectos suman!

- 📖 Impartiremos una serie de **talleres prácticos** mostrándote cómo desarrollar un proyecto para que tengas un ejemplo de referencia. Para calentar puedes visualizar los de la edición anterior:

  - [Fine-tuning LLMs (Manu Romero)](https://somosnlp.org/hackathon-2023/fine-tuning-llms)
  - [Etiquetado de datos con Argilla (Daniel Vila)](https://somosnlp.org/hackathon-2023/etiquetado-de-datos-con-argilla)

- ❓ Organizaremos **AMAs** (del inglés, Ask Me Anything) con expertas y mentores para que puedan solucionar tus dudas.

</details>

<details>
<summary>¿De qué depende la complejidad de los proyectos?</summary>

Proporcionaremos un ejemplo de cómo crear un dataset, entrenar un modelo y crear una demo. Depende de ti y tu equipo elegir cuánto investigar y trabajar para mejorar la versión base. La dificultad también depende del caso de uso, el origen de los datos, el tiempo que dediquéis a su curación, la técnica de entrenamiento, las iteraciones que hagáis y lo elaborada que queráis que sea vuestra demo. ¡Sois libres de elegir todo!

</details>

<details>
<summary>¿Cómo se elige la temática de las bases de datos/modelos?</summary>

La temática de los proyectos es siempre libre. Este año el enfoque es representar la riqueza del español, por lo que os animamos a crear proyectos relacionados con vuestro país (leyes, manera de hablar, cultura, ...). Además, como es habitual, os animamos a que los proyectos tengan impacto social y estén relacionados con alguno de los Objetivos de Desarrollo Sostenibles de la ONU. Si buscas inspiración, en el canal #encuentra-equipo de Discord puedes encontrar temas propuestos.

</details>

<details>
<summary>¿De verdad se necesitan 3 semanas?</summary>

No, depende de tu disponibilidad, puedes desarrollar un buen proyecto en una semana. Tenemos en cuenta que las personas estudian y trabajan, por lo que dejamos más tiempo del necesario para que todo el mundo pueda participar. También queremos daros tiempo extra para que disfrutéis la oportunidad de asistir en directo a las ponencias y mentorías celebradas durante el hackathon.

</details>

<details>
<summary>¿Hasta cuándo puedo crear un equipo?</summary>

Damos la bienvenida a nuevos equipos hasta el 22 de marzo.

</details>

<details>
<summary>¿Cómo me uno a un equipo?</summary>

Lee el README en el canal #encuentra-equipo de nuestro servidor de Discord :)

</details>

<details>
<summary>¿Puede haber equipos de 1 persona?</summary>

Sí, aceptamos equipos de 1 a 5 personas.

</details>

<details>
<summary>¿Cómo nos recomendáis organizarnos?</summary>

- Utilizar el canal de vuestro proyecto en Discord para comunicaros y organizaros.
- Dado que es un hackathon internacional recomendamos una comunicación asíncrona o que os repartáis el trabajo y hagáis reuniones de menos personas
- Fijar reuniones o hablar espontáneamente utilizando los nuevos canales de voz de la categoría "SALAS DE REUNIÓN" de Discord
- Fijar en el canal del proyecto los mensajes importantes, e.g.: repartición de tareas, día de la próxima reunión, ... Para fijar un mensaje haz click en los tres puntitos y selecciona "Fijar mensaje"
- Para mayor claridad también podéis crear un documento compartido con las personas del equipo en el que escribir el objetivo del proyecto, repartir tareas y demás (y fijar el enlace en el chat)

</details>

*Si te hemos dicho que en esta página hay info que no encuentras, borra las cookies y recarga la página.*

## 🙌 Otras maneras de apoyar la iniciativa #Somos600M

<details>
<summary>¿Cómo puedo colaborar?</summary>

- Comparte los posts de las cuentas de @SomosNLP ([LinkedIn](https://www.linkedin.com/company/somosnlp), [Twitter](https://twitter.com/somosnlp_)), ¡invita a tus colegas del trabajo, compañeros y compañeras de clase a crear un equipo!
<!-- - ¿Tienes 2 horitas para ayudarnos con la organización de este increíble evento? Te estamos esperando, [únete al equipo](https://forms.gle/radg18NMLRZMPu38A). -->
- ¿Estás en la uni? [Comparte esta info con tu profe](https://somosnlp.org/hackathon/universidades) o alguien del grupo de IA/informática para que tu universidad colabore con el evento.
- ¿Te gustaría compartir tu conocimiento con la comunidad? Propón una [ponencia](https://forms.gle/YpUvifDNLG6E56Cy9) o una [mentoría](https://forms.gle/7UmsVDnFmNo1pCrf9).
- ¿Formas parte de un grupo de investigación? Igual os interesa [colaborar donando un corpus](https://somosnlp.org/donatucorpus).
- ¿Quieres apoyar la iniciativa dando visibilidad, patrocinando vales o con una donación económica? ¡[Patrocina el hackathon](https://forms.gle/sEkxstwbJSRYpgDa8)!

</details>
