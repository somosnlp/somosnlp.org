---
title: "Retos #HackathonSomosNLP 2025"
description: Vamos a impulsar la creación de modelos de lenguaje alineados con la cultura de los países de LATAM y la Península Ibérica.
lang: es
cover: https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg
---

<script setup>
import ChallengesGrid from '../../../src/components/ChallengesGrid.vue'

const miniChallenges = [
  {
    title: "Exámenes (INCLUDE)",
    description: "Busca exámenes de opción múltiple para evaluar el conocimiento de los LLMs sobre tu país. Prioriza exámenes en lenguas distintas al español y/o centrados en temas culturales (e.g. historia, literatura).",
    dates: "9 de abril - 31 de mayo ",
    points: "1 pto",
    requirements: "Saber buscar en internet",
    link: "https://somosnlp.org/hackathon/retos/include",
    cover: "https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg"
  },
  {
    title: "Estereotipos",
    description: "Comparte y evalúa estereotipos para ayudar a mitigar sesgos de los LLMs.",
    dates: "9 de abril - 21 de mayo ",
    points: "1 pto",
    requirements: "Haber vivido en sociedad",
    link: "https://somosnlp.org/hackathon/retos/estereotipos",
    cover: "https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg"
  },
  {
    title: "Preguntas culturales (BLEND)",
    description: "Responde preguntas sobre tu país para evaluar el conocimiento cultural de LLMs. Utilizaremos estas respuestas para extender el benchmark abierto BLEND.",
    dates: "14 de abril - 31 de mayo ",
    points: "2 ptos",
    requirements: "Haber vivido en sociedad",
    link: "https://somosnlp.org/hackathon/retos/blend",
    cover: "https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg"
  }
]

const mainChallenges = [
  {
    title: "1. Genera un dataset de preferencias",
    description: "Diseña prompts que evalúen la adecuación cultural con tu país y elige la mejor respuesta en un LLM Arena. Los prompts y las respuestas serán recolectados y compartidos con todos los equipos participantes como dataset de preferencias v0 para la fase de alineamiento.",
    dates: "14 de abril - 21 de mayo ",
    points: "3 ptos",
    requirements: "Haber vivido en sociedad y querer comprender bien el concepto de adecuación cultural",
    link: "https://somosnlp.org/hackathon/retos/preferencias",
    cover: "https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg"
  },
  {
    title: "2.A. Alinea un modelo textual (LLM)",
    description: "Procesa, filtra y extiende el dataset de preferencias v0 adaptándolo a tu caso de uso. Utilízalo para alinear un LLM usando técnicas de entrenamiento optimizado y alineamiento como LoRA, cuantización y optimización directa de preferencias (DPO).",
    dates: "21 de abril - 31 de mayo (Máx. 2 semanas)",
    points: "3 ptos",
    requirements: "Saber programar",
    link: "https://somosnlp.org/hackathon/retos/alineamiento",
    cover: "https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg"
  },
  {
    title: "2.B. Alinea un modelo multimodal",
    description: "Genera un dataset de imágenes y descripciones utilizando la API de Cohere. Utilízalo para crear un modelo multimodal (VLLM) que genere descripciones de imágenes teniendo en cuenta el contexto usando las últimas técnicas de entrenamiento optimizado.",
    dates: "21 de abril - 31 de mayo (Máx. 2 semanas)",
    points: "3 ptos",
    requirements: "Tener experiencia en PLN",
    link: "https://somosnlp.org/hackathon/retos/alineamiento",
    cover: "https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg"
  }
]

const finalChallenges = [
  {
    title: "3. Crea de una demo",
    description: "Crea una demo de tu proyecto en un Space de HuggingFace para que todo el mundo pueda ver tu trabajo.",
    dates: "Hasta el 31 de mayo ",
    points: "0.5 ptos",
    requirements: "Haber completado algún reto principal",
    link: "https://somosnlp.org/hackathon/retos/presentacion",
    cover: "https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg"
  },
  {
    title: "4. Graba un vídeo",
    description: "Graba un vídeo 5 minutos presentando tu proyecto para el jurado y el resto de la comunidad.",
    dates: "Envío hasta el 1 de junio ",
    points: "0.5 ptos",
    requirements: "Haber completado algún reto principal",
    link: "https://somosnlp.org/hackathon/retos/presentacion",
    cover: "https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg"
  },
  {
    title: "5. (Opcional) Escribe un paper",
    description: "Escribe un paper describiendo tu proyecto. Si te interesa, te podemos mentorizar y ayudar a mandarlo a un workshop de LatinX in NLP.",
    dates: "A partir de junio",
    points: "0.5 ptos",
    requirements: "Haber completado algún reto principal",
    link: "https://somosnlp.org/hackathon/retos/presentacion",
    cover: "https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg"
  }
]
</script>

El hackathon de este año se centra en la creación de recursos que permitan la evaluación y el alineamiento de modelos de lenguaje con la cultura de los países de LATAM y la Península Ibérica. El hackathon se ha extendido **hasta el 31 DE MAYO**.

El hackathon consta de un reto principal y varios mini retos con los que también podéis acumular puntos para los premios finales y ganar premios extra. La puntuación máxima total es de 10 puntos.

En esta página encontrarás información sobre:
- Primeros pasos
- Incentivos y premios
- Mini retos
- Reto principal
- Preguntas frecuentes

¡Mucho éxito! 🚀

---

## 👣 Primeros pasos

Antes de comenzar, todas las personas tienen que:
- ✅ Unirse al servidor de [Discord de SomosNLP](https://discord.com/invite/my8w7JUxZR)
- ✅ Crear una cuenta en [Hugging Face](https://huggingface.co/join)
- ✅ Rellenar el [formulario de registro](https://forms.gle/bDaBC7XV3iu2trj59)
- ✅ Unirse a la [organización de Hugging Face del hackathon](https://huggingface.co/organizations/somosnlp-hackathon-2025/share/BMALwncoPyZLRdPuzwugnsDzXHsbLnjjGD), donde se compartirán los datasets, modelos y demos

Para crear un equipo:
- Puedes apuntarte con gente que ya conozcas (por ejemplo, tu grupo de clase o del trabajo) o conocer a gente de la comunidad de SomosNLP de otros países, universidades y empresas. Si quieres conocer a gente, revisa el [canal #encuentra-equipo](https://discord.com/channels/938134488670675055/1082369575666073611)
- Una vez que hayáis creado el equipo, UNA persona tiene que [registrar el equipo](https://forms.gle/mLKEURUXGiNhq31T9)

---

## 👏 Incentivos y premios

Al participar tendrás la oportunidad de:
- ✨ Aprender con talleres y charlas en directo
- ✨ Conseguir acceso a 500 USD de la API de Cohere
- ✨ Conseguir acceso a una GPU L40S de Hugging Face
- ✨ Ganar 1000 USD en créditos de la API de Mistral
- ✨ Ganar cientos de USD en créditos GPU y libros de IA y lenguaje
- ✨ Ganar acceso a un Máster online de IA
- ✨ Ganar una entrada para la conferencia online de WomenTech Network
- ✨ Ganar una nominación a la red de talento Nova
- ✨ Ganar mentorías con personas relevantes en el campo del PLN
- ✨ Co-publicar papers en conferencias de PLN internacionales
- ✨ Conseguir un certificado de participación (o equipo ganador) del hackathon

¡A por ello! 🚀

---

## ✨ Mini retos

Participa en estos mini retos para contribuir a la creación de bases de datos que evalúen el conocimiento cultural y estereotipos de los LLMs. ¡Podrás acumular puntos y ganar premios extra!

<ChallengesGrid :challenges="miniChallenges" />

---

## 🔥 Reto principal

1. Genera un dataset de preferencias
2. Alinea un modelo textual (opción A) o multimodal (opción B), a elegir
3. Crea una demo de tu proyecto
4. Presenta tu proyecto en un vídeo de 5 mins
5. (Opcional) escribe un paper presentando tu proyecto

<ChallengesGrid :challenges="mainChallenges" />

<ChallengesGrid :challenges="finalChallenges" />

---

## ❓ Preguntas frecuentes

<details>
<summary>¿Por qué debería participar?</summary>

Al unirte a este hackathon tendrás la oportunidad de:

- ✅ Comprender cómo funcionan los grandes modelos del lenguaje, tanto textuales (LLMs) como multimodales (VLLMs) y descubrir los retos de cada etapa de su desarrollo: creación del corpus, entrenamiento, alineamiento y evaluación
- ✅ Participar en la creación del primer corpus de preferencias de calidad y diverso para alinear LLMs con la cultura de los países de LATAM y la Península Ibérica (top como experiencia y top para el CV)
- ✅ Ser parte del equipo que cree algunas de las bases de datos de la primera leaderboard abierta de LLMs en español: La Leaderboard
- ✅ Resolver todas tus dudas sobre PLN durante sesiones de mentoría "Ask My Anything"
- ✅ Recibir apoyo para presentar tu trabajo en un paper
- ✅ Ganar premios para seguir creciendo como profesional y conseguir un certificado que poder compartir en LinkedIn
- ✅ Unirte a la mayor comunidad de hispanohablantes que estudian, trabajan e investigan en PLN

</details>

<details>
<summary>¿Cuál es el nivel necesario?</summary>

Desde el equipo de SomosNLP queremos animarte a participar independientemente de tus conocimientos actuales. En ediciones anteriores hemos contado con grupos de institutos de investigación y grupos de estudiantes de grado, ¡todos los proyectos suman!

- 📖 Impartiremos una serie de **talleres prácticos** mostrándote cómo desarrollar un proyecto para que tengas un ejemplo de referencia.

<!-- Para calentar puedes visualizar los de la edición anterior:

  - [Fine-tuning LLMs (Manu Romero)](https://somosnlp.org/hackathon-2023/fine-tuning-llms)
  - [Etiquetado de datos con Argilla (Daniel Vila)](https://somosnlp.org/hackathon-2023/etiquetado-de-datos-con-argilla) -->

- ❓ Organizaremos **AMAs** (del inglés, Ask Me Anything) con expertas y mentores para que puedan solucionar tus dudas.

</details>

<details>
<summary>¿De qué depende la complejidad de los proyectos?</summary>

Proporcionaremos un ejemplo de cómo crear un dataset, entrenar un modelo y crear una demo. Depende de ti y tu equipo elegir cuánto investigar y trabajar para mejorar la versión base. La dificultad también depende del caso de uso, el origen de los datos, el tiempo que dediquéis a su curación, la técnica de entrenamiento, las iteraciones que hagáis y lo elaborada que queráis que sea vuestra demo. ¡Sois libres de elegir todo!

</details>

<!-- <details>
<summary>¿Cómo se elige la temática de las bases de datos/modelos?</summary>

La temática de los proyectos es siempre libre. Este año el enfoque es representar la riqueza del español, por lo que os animamos a crear proyectos relacionados con vuestro país (leyes, manera de hablar, cultura, ...). Además, como es habitual, os animamos a que los proyectos tengan impacto social y estén relacionados con alguno de los Objetivos de Desarrollo Sostenibles de la ONU. Si buscas inspiración, en el canal #encuentra-equipo de Discord puedes encontrar temas propuestos.

</details> -->

<details>
<summary>¿De verdad se necesitan 4 semanas?</summary>

No, depende de tu disponibilidad, puedes desarrollar un buen proyecto en una semana. Tenemos en cuenta que las personas estudian y trabajan, por lo que dejamos más tiempo del necesario para que todo el mundo pueda participar. También queremos daros tiempo extra para que disfrutéis la oportunidad de asistir en directo a las ponencias y mentorías celebradas durante el hackathon.

</details>

<details>
<summary>¿Hasta cuándo puedo crear un equipo?</summary>

EDITADO: Damos la bienvenida a nuevos equipos hasta el 23 de mayo. El día final para entregar proyectos es el 31 de mayo.

</details>

<details>
<summary>¿Cómo me uno a un equipo?</summary>

Lee la sección "Para crear un equipo:" al comienzo de esta página y el README en el canal #encuentra-equipo de nuestro servidor de Discord :)

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

<details>
<summary>No entiendo Discord, ¿cuáles son los canales más importantes?</summary>

- Revisa el canal [#anuncios](https://discord.com/channels/938134488670675055/944255490748207115), recomendamos activar las notificaciones del canal, publicamos 2/3 veces a la semana
- Pregunta tus dudas en el canal [#pide-ayuda](https://discord.com/channels/938134488670675055/1051997272356966430) de Discord para que todo el mundo pueda beneficiarse de la respuesta
- Los eventos los anunciamos en el canal [#eventos](https://discord.com/channels/938134488670675055/939934987581534228) y los añadimos al [calendario de Google](https://calendar.google.com/calendar/u/0?cid=ZWM3MGZhODIzNmYyNzBlMTYwYzFiMjdhNDgzZWMyMjA1ZjQwYzUyN2E5N2MwZTJhZmY0OTcwZDZmZjBkYzQyMEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t)

</details>

<details>
<summary>¿Cómo me puedo enterar de los eventos?</summary>

- Anunciamos los eventos en el canal [#eventos](https://discord.com/channels/938134488670675055/939934987581534228)
- Los añadimos al [calendario de Google](https://calendar.google.com/calendar/u/0?cid=ZWM3MGZhODIzNmYyNzBlMTYwYzFiMjdhNDgzZWMyMjA1ZjQwYzUyN2E5N2MwZTJhZmY0OTcwZDZmZjBkYzQyMEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t)
- Los anunciamos en redes sociales ([LinkedIn](https://www.linkedin.com/company/somosnlp), [X (Twitter)](https://x.com/somosnlp_))
- [Síguenos en YouTube](https://www.youtube.com/c/somosnlp?sub_confirmation=1) y guarda la [playlist del hackathon 2025](https://www.youtube.com/playlist?list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6)

</details>

<details>
<summary>¿Cómo puedo dar feedback del evento?</summary>

- Nos puedes dar feedback para mejorar las guías de los retos con este [formulario](https://forms.gle/LjQBb8B3XGqPs8Ws9) (anónimo)
- Compartiremos también un formulario de feedback general al final del evento

</details>


*Si te hemos dicho que en esta página hay info que no encuentras, borra las cookies y recarga la página.*

---

## 🙌 Otras maneras de apoyar la adecuación cultural de los LLMs

<details>
<summary>¿Cómo puedo colaborar?</summary>

- Comparte los posts de las cuentas de @SomosNLP ([LinkedIn](https://www.linkedin.com/company/somosnlp), [X (Twitter)](https://x.com/somosnlp_)), ¡invita a tus colegas del trabajo, compañeros y compañeras de clase a crear un equipo!
<!-- - ¿Tienes 2 horitas para ayudarnos con la organización de este increíble evento? Te estamos esperando, [únete al equipo](https://forms.gle/radg18NMLRZMPu38A). -->
- ¿Estás en la uni? [Comparte esta info con tu profe](https://somosnlp.org/hackathon-2025/universidades) o alguien del grupo de IA/informática para que tu universidad colabore con el evento.
<!-- - ¿Te gustaría compartir tu conocimiento con la comunidad? Propón una [ponencia](https://forms.gle/YpUvifDNLG6E56Cy9) o una [mentoría](https://forms.gle/7UmsVDnFmNo1pCrf9). 
- ¿Formas parte de un grupo de investigación? Igual os interesa [colaborar donando un corpus](https://somosnlp.org/donatucorpus).-->
- ¿Quieres apoyar la iniciativa dando visibilidad, patrocinando vales o con una donación económica? ¡[Patrocina el hackathon](https://forms.gle/sEkxstwbJSRYpgDa8)!

</details>



<!-- ## 🗓️ Eventos

#### Automatizando extracción de corpus desde PDFs | Alfonso Amayuelas, PhD @ Universidad de California, Santa Barbara

¿Cómo usar las últimas herramientas en LLMs para crear QA datasets? En este evento usaremos un modelo de OCR y LLMs para estandarizar exámenes, cuestionarios, etc. 

[¡Grabación ya disponible!](https://www.youtube.com/watch?v=Jk70bSw4tTo&list=PLTA-KAy8nxaCGGYz5CWiLZNzc31ilPDyI&index=3)

![alt text](https://somosnlp.github.io/assets/images/eventos/250415_alfonso_amayuelas.png)


#### Confidently wrong: expresando incertidumbre en tareas multilinguales | Selene Baez, Postdoc @ University of Zurich

Si bien la fluidez y la coherencia de los Modelos de Lenguaje (LLM) en la generación de texto han mejorado significativamente, su capacidad para generar expresiones adecuadas de incertidumbre sigue siendo limitada. Mediante una tarea de Q&A multilingüe a libro cerrado y GPT-3.5, exploramos la precisión con la que los LLM se calibran y expresan certeza en una variedad de idiomas, incluyendo entornos con bajos recursos.

[¡Grabación disponible!](https://www.youtube.com/watch?v=TC9tOEyPqy8&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6)

![alt text](https://somosnlp.github.io/assets/images/eventos/250410_selene_baez.png)

#### Red Teaming para Modelos de Lenguaje | Luis Vasquez, Research Engineer @Barcelona Supercomputing Center

Breve introducción al Red Teaming para Modelos de Lenguaje: definición, estrategias comunes y recursos.

[¡Grabación disponible!](https://www.youtube.com/watch?v=pGOXE4rrO9M&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6)

![alt text](https://somosnlp.github.io/assets/images/eventos/250410_luis_vasquez.png) -->
