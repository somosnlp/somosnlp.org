---
title: "Bases del Hackathon #Somos600M"
description: Todo lo que necesitas saber para presentar un buen proyecto al hackathon
lang: es
cover: https://somosnlp.github.io/assets/images/eventos/240301_hackathon.jpg
---

Cada equipo participante generará un corpus de instrucciones, entrenará su LLM y creará una demo para compartir su gran trabajo con la comunidad. Este año el enfoque son proyectos que representen la riqueza del español y la diversidad de las personas hispanohablantes. Como siempre, os animamos a que los proyectos tengan impacto social y estén relacionados con alguno de los Objetivos de Desarrollo Sostenibles de la ONU. ¡Gracias por participar! ✨

<div class="flex justify-center">
<a href="https://hackathonsomosnlp2024.eventbrite.com/?aff=w" target="_blank">
    <img src="https://somosnlp.github.io/assets/images/eventos/240301_hackathon.jpg"
        width="650" height="365" alt="Cartel del Hackathon 2024" />
</a>
</div>

<center><a href="https://hackathonsomosnlp2024.eventbrite.com/?aff=w" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">📝 ¡Inscripciones abiertas hasta el 15 de marzo!</a></center>

## 👀 Maneras de participar

Como sabes, la iniciativa #Somos600M tiene dos objetivos:

### ✅ Crear la primera leaderboard de LLMs

Ayúdanos a validar en comunidad las traducciones hechas por el Grupo de PLN de la Universidad de Oregon de las bases de datos utilizadas en la famosa [Open LLM Leaderboard de Hugging Face](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard).

Gracias al apoyo de Argilla y Hugging Face, en concreto de Álvaro Bartolomé, Ignacio Talavera, Daniel Vila y Omar Sanseviero, colaborar es muy sencillo:

1. Crea una cuenta en [Hugging Face](https://huggingface.co/join) y únete a la organización de SomosNLP con [esta invitación](https://huggingface.co/organizations/somosnlp/share/qgytUhPKvxVxsbZWTzVUAUSUnZmVXNPmjc)
2. Entra en el [entorno de validación](https://huggingface.co/spaces/somosnlp/benchmark-annotation-argilla)
3. Valida la traducción de un párrafo del inglés al español
4. Repite el paso 3 cuantas veces quieras y mira cómo subes en el [ranking de colaboraciones](https://huggingface.co/spaces/somosnlp/benchmark-annotation-argilla-dashboard)
5. Tu nombre aparecerá como parte del equipo que creó las bases de datos de la futura leaderboard de LLMs en español 🙌

### 🌎 Crear el mayor corpus de instrucciones

Participar en nuestro hackathon y aplicar tus conocimientos a democratizar el PLN en español es muy sencillo, ¡anímate!

1. Únete a nuestra comunidad de [Discord](https://discord.com/invite/my8w7JUxZR). Auto-asígnate el rol "Hackathon24": en el servidor, vete al comienzo de la barra lateral izquierda, haz click en "Canales y roles", selecciona "Participar en el hackathon 2024".
2. Crea una cuenta en [Hugging Face](https://huggingface.co/join) y únete a la organización de [SomosNLP](https://huggingface.co/organizations/somosnlp/share/qgytUhPKvxVxsbZWTzVUAUSUnZmVXNPmjc).
3. Regístrate en [Eventbrite](https://hackathonsomosnlp2024.eventbrite.com/?aff=w).
4. Crea tu equipo o únete a uno (equipos de de 1 a 5 personas). Hay que inscribir los equipos en el canal **#encuentra-equipo** (más info en el README del canal).
5. Crea tu corpus de instrucciones y súbelo a la org de hf.co/SomosNLP. Te recomendados utilizar la librería `distilabel` (ver recursos abajo).
6. Escribe la Dataset Card de tu dataset: describe el proceso de creación y curación (link al notebook), inspecciona el dataset, evalúa y mitiga sesgos.
7. Fine-tuning de un LLM para la tarea que hayas elegido y súbelo a la org de hf.co/SomosNLP. Pondremos a vuestra disposición GPU VMs, avísanos cuando tengas el dataset y esté todo listo para empezar el entrenamiento. Recuerda que es muy importante hacer pruebas en máquinas más humildes para verificar que el código es correcto y no encontrar bugs después de varias horas de entrenamiento.
8. Escribe la Model Card de tu modelo: describe el proceso de entrenamiento (link al notebook), evalúa su calidad, sesgos y huella de carbono. Importante: enlaza el dataset utilizado para el entrenamiento.
9. Crea una demo para mostrar tu proyecto a la comunidad y súbela a la org de hf.co/SomosNLP. Puedes utilizar GPUs Nvidia T4 - small (gracias Hugging Face). Importante: enlaza los dataset(s) y modelo(s) utilizados.
10. Entrega tu proyecto rellenando un formulario que publicaremos próximamente. Puedes seguir haciendo modificaciones hasta las 23h59 *Anywhere on Earth* del martes 26 de marzo (revisaremos la hora de los commits 👀).

Si tienes cualquier duda sobre las bases estamos a tu disposición en el canal #pide-ayuda, escribe un título descriptivo y utiliza la etiqueta "hackathon".

¡Mucho éxito! 🚀

<!--

Al finalizar el hackathon, habremos creado el mayor corpus de instrucciones abierto originalmente en español y lenguas cooficiales.

Agradecemos mucho a Hugging Face la mejora de la org de SomosNLP a enterprise para poder utilizar la PRO API. Pedimos a todos los equipos responsabilidad y que esta API sea estrictamente usada para el desarrollo de proyectos del hackathon.

### O... dona tu corpus

También puedes colaborar con ambos objetivos donando un corpus que hayas creado con tu grupo de investigación o empresa, [¡dona tu corpus!](https://somosnlp.org/donatucorpus) -->

## 📝 Guía y recursos para desarrollar un buen proyecto

Recuerda que el objetivo del hackathon es representar la diversidad de las personas hispanohablantes, te animamos a crear corpus que reflejen la riqueza del español, en la medida de lo posible divídelo por países/regiones e incluye ejemplos de diferentes variedades del español.

### 📚 Corpus 

- En español o lenguas cooficiales.
- Corpus de instrucciones, i.e.: pregunta + (opcional: entrada/contexto) + respuesta.
- Si quieres ir un paso más allá también puedes adaptar el corpus para DPO. En este caso, sube el corpus de instrucciones con el sufijo `it` y el DPO con el sufijo `dpo`.
- Para crear el corpus te recomendamos utilizar `distilabel`.
- Puedes utilizar los endpoints PRO de Hugging Face como se explica el notebook de ejemplo (recuerda que tienes que pertenecer a hf.co/somosnlp).
- Si te animas a etiquetar un corpus te recomendamos utilizar `Argilla`.
- Sube el corpus directamente a hf.co/somosnlp e itera ahí.
- Escribe en la primera versión de la Dataset Card la motivación del proyecto y los miembros del equipo: "Corpus creado en el marco del [hackathon #Somos600M](https://somosnlp.org/hackathon) organizado por SomosNLP por el siguiente equipo: ... El objetivo del proyecto es ..."
- Cumplimenta bien la Dataset Card, tendremos en cuenta a la hora de evaluar los proyectos si está completa e incluye temas como una evaluación de los sesgos (e.g., se ha prestado atención a que las clases estén balanceadas).

<details>
<summary>Estructura del corpus</summary>

Por ser corpus de instrucciones cada corpus contará con las siguientes columnas:
- `pregunta`
- `entrada` (opcional: entrada o contexto)
- `respuesta`

Además, dado el enfoque en las variedades de la lengua del hackathon, también incluiremos las siguientes columnas:

- `idioma` (variedad geográfica): código ISO del idioma ("catalán" = `ca`, "quechua" = `qu`), en caso de ser español hay que especificar la variedad geográfica ("español de México" = `es_mx`, "español de Ecuador" = `es_ec`).
- `epoca` (variedad histórica): si es un corpus en español elegir entre `actual`, `moderno`, `clásico` (siglo de oro) o `medieval`, si es en otro idioma rellenar si tenéis conocimiento.
- `nivel` (variedad sociocultural): una de `culto`, `medio`, `vulgar`
- `registro` (variedad funcional): coloquial / formal, jerga (de profesión determinada) o argots (de un grupo social, e.g., argot juvenil)

Para completar la información de los ejemplos incluiremos también:
- `dominio`: `legal`. `salud` (clínico, biomédico, farma), `tecnico` (académico, técnico), `literatura` (poesía, música, teatro),  `noticias`, `cocina`, ..., `general` (última opción). Si puedes, especifica el subdominio, e.g. `literatura_poesia`.
- `tarea`: `pregunta`, `clasificacion`, `traduccion`, `resumen`, `similitud_semantica`. Si puedes, especifica también la subtarea, e.g. `pregunta_abierta`, `pregunta_opcion_multiple`.
- `país`: si procede, país al que hace referencia la pregunta (e.g. ley de un país, receta típica, pregunta de historia). ¡Ojo, no confundir país e idioma!

Si tienes dudas #pide-ayuda, hay lingüistas en la comunidad!

Si tienes que añadir columnas puedes hacerlo automáticamente utilizando los mismos endpoints que para crear los datasets sintéticos. Acuérdate de revisar después las anotaciones automáticas.

</details>

<details>
<summary>Recursos</summary>

- [Notebook: creación de datasets sintéticos con distilabel](https://github.com/somosnlp/recursos/blob/main/hackathon_2024/creacion_de_datasets_sinteticos_con_distilabel.ipynb), creado por Daniel Vila y Agustín Piqueres @Argilla.
- [Notebook: creación de un dataset sintético a partir del PDF del EU AI Act](https://distilabel.argilla.io/latest/tutorials/pipeline-notus-instructions-preferences-legal/), creado por el equipo de Argilla y con traducción WIP por Edison J. Bejarano.
- [Taller práctico: distilabel y Argilla, herramientas para crear modelos como Notus](https://www.youtube.com/watch?v=riM3pgV4m_I&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J) impartido por Gabriel Martín, MLE @Argilla, (presentó otro notebook diferente!)
- [Cómo anotar un corpus lingüísticos para entrenar LLMs](https://www.youtube.com/watch?v=d6vrflcIY-g&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J), impartida el miércoles 20 por Marta Guerrero @IIC, creadora de 3 de los corpus que formarán la leaderboard.
- [Taller práctico: Etiquetado de datos con Argilla](https://somosnlp.org/hackathon-2023/etiquetado-de-datos-con-argilla) impartido por Daniel Vila Suero, co-fundador y CEO @Argilla.
- [AMA de etiquetado de datos](https://somosnlp.org/hackathon-2023/ama-con-natalia-elvira), pregunta todas tus dudas a Natalia Elvira, Project Manager @Argilla.

</details>

### ⚙️ Modelo

- En español o lenguas cooficiales.
- Haz fine-tuning de un modelo ya existente (no pre-entrenes uno desde cero). En esta edición te animamos a que ajuste un gran modelo del lenguaje (LLM).
<!-- - Desde el lunes 3 al domingo 9 tendréis a vuestra disposición GPU VMs 24GB patrocinadas por Q Blocks para entrenar vuestro modelo final. -->
- Os animamos a utilizar [autotrain](https://huggingface.co/docs/autotrain/llm_finetuning) para entrenar vuestros modelos directamente desde el hub de Hugging Face, ¡tenemos créditos patrocinados por HF!
- Sube el modelo directamente a hf.co/somosnlp e itera ahí. Escribe en la primera versión de la Model Card la motivación del proyecto y los miembros del equipo.
- Este año la evaluación corre a nuestro cargo, ¡vuestros modelos inaugurarán la primera leaderboard abierta de LLMs en español!
- Cumplimenta bien la Model Card, a la hora de evaluar los proyectos daremos un punto extra si está completa y se incluyen temas como la evaluación de los sesgos del modelo y del impacto desde el punto de vista climático.

<details>
<summary>Recursos</summary>

- [Taller práctico: Fine-tuning de grandes modelos de lenguaje](https://somosnlp.org/hackathon-2023/fine-tuning-llms) impartido por Manu Romero, creador de +500 modelos del Hub de Hugging Face.
- [Taller práctico: El impacto de la calidad de los datos en un FT](https://www.youtube.com/watch?v=hPq5NG8kA8w&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J), impartido también por Manu Romero.
- [AMA (Ask Me Anything) sobre entrenamiento de LLMs](https://www.youtube.com/playlist?list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J) con Alejandro Vaca el lunes 18.
- [Docs: AutoTrain](https://huggingface.co/docs/autotrain/llm_finetuning), os animamos a probar esta herramienta y aprovechar los créditos patrocinados por Hugging Face!
<!-- - <a href="https://somosnlp.org/hackathon-2023/what-is-q-blocks" target="_blank">Taller: How to get started with Q Blocks</a> impartido por Gaurav Vij, Head of Product & Co-founder de Q Blocks. -->
- [Detección y mitigación de sesgos en modelos de lenguaje](https://somosnlp.org/hackathon-2023/evaluacion-de-sesgos), charla impartida por María Grandury, fundadora de SomosNLP.
- Para evaluar la huella de carbono del entrenamiento de tu modelo puedes utilizar herramientas como [ML CO2 Impact](https://mlco2.github.io/impact) o [Code Carbon](https://codecarbon.io), integrada en 🤗 Transformers. Te recomendamos este [vídeo](https://www.youtube.com/watch?v=ftWlj4FBHTg) de motivación, este [artículo](https://huggingface.co/blog/carbon-emissions-on-the-hub) del blog de HF y la sección de la [documentación](https://huggingface.co/docs/hub/model-cards-co2) de 🤗 Transformers que trata este tema.
- [Ética ambiental en IA: construyendo narrativas sostenibles en español](https://www.youtube.com/watch?v=MJLdrXz6bSE&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J), charla impartida por Jorge Vallego, Project Lead @H4rmony. Os puede servir para darle un enfoque eco-consciente a vuestro dataset.

</details>

### 🖼️ Demo

- Por último, crea una demo para que todo el mundo pueda interactuar con tu nuevo modelo. Si es tu primera demo, te recomendamos utilizar Gradio ya que es más sencillo.
- Crea la demo directamente en hf.co/somosnlp e itera ahí.
- Puedes utilizar GPUs `Nvidia T4 - small` patrocinadas por Hugging Face.
- Qué incluir en la demo: motivación del proyecto, impacto, ideas futuras, número de ODS si procede, enlace al dataset y modelo utilizados, miembros del equipo :)

<details>
<summary>Recursos</summary>

- Docs: [Gradio docs](https://www.gradio.app/docs)
- Notebook: [Cómo crear una demo con Gradio](https://somosnlp.org/recursos/tutoriales/06_demos_con_gradio)
- Vídeo tutoriales: [Aquí](https://www.youtube.com/watch?v=Q0t1bNoa0tI&list=PLTA-KAy8nxaB-HA79tlOTRl496_XIlJta) tienes tutoriales para crear demos utilizando Gradio, Streamlit y Flask.

</details>

### ✨ Visibilidad

- Te recomendamos que subas tus datasets, modelos y demos desde el principio a la org hf.co/somosnlp para que aparezcan en la nueva [❤️ leaderboard](https://huggingface.co/spaces/somosnlp/likes_leaderboard) y todo el mundo pueda verlo y darle likes. ¡Habrá una mención de honor para el proyecto con más ❤️!
- Puedes compartir tu proyecto en el canal #comparte-tu-proyecto.
- Si quieres compartir tu proyecto en redes utiliza el hashtag #Somos600M y menciona a SomosNLP, ¡será un placer darle más visibilidad!

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

Idealmente durante la primera semana del hackathon, hasta el 8 de marzo.

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

## 🙌 Mientras tanto... apoya la organización del evento

- Comparte los posts de las cuentas de @SomosNLP ([LinkedIn](https://www.linkedin.com/company/somosnlp), [Twitter](https://twitter.com/somosnlp_)), ¡invita a tus colegas del trabajo, compañeros y compañeras de clase a crear un equipo!
<!-- - ¿Tienes 2 horitas para ayudarnos con la organización de este increíble evento? Te estamos esperando, [únete al equipo](https://forms.gle/radg18NMLRZMPu38A). -->
- ¿Estás en la uni? [Comparte esta info con tu profe](https://somosnlp.org/hackathon/universidades) o alguien del grupo de IA/informática para que tu universidad colabore con el evento.
- ¿Te gustaría compartir tu conocimiento con la comunidad? Propón una [ponencia](https://forms.gle/YpUvifDNLG6E56Cy9) o una [mentoría](https://forms.gle/7UmsVDnFmNo1pCrf9).
- ¿Formas parte de un grupo de investigación? Igual os interesa [colaborar donando un corpus](https://somosnlp.org/donatucorpus).
- ¿Quieres apoyar la iniciativa dando visibilidad, patrocinando vales o con una donación económica? ¡[Patrocina el hackathon](https://forms.gle/sEkxstwbJSRYpgDa8)!

<!-- 
## 🏆 Evaluación y Premios

Para que todos los equipos comiencen el hackathon con las mismas oportunidades, las [bases](https://somosnlp.org/hackathon/bases) del hackathon junto con información detallada sobre la evaluación de los proyectos se publicarán en febrero.

Estamos hablando con todo el mundo para conseguir premios increíbles, ¡os mantendremos al corriente!

## 🏆 Beneficios y Premios

 - 
 -->
