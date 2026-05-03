---
title: "Retos #HackathonSomosNLP 2026"
description: Vamos a impulsar la creación de modelos de lenguaje alineados con la cultura de los países de LATAM y la Península Ibérica.
lang: es
cover: /images/eventos/260511_hackathon_eventbrite.png
---

<script setup>
import ChallengesGrid from '../../../src/components/ChallengesGrid.vue'

const miniChallenges = [
  {
    title: "Exámenes (INCLUDE)",
    description: "Busca exámenes tipo test (de opción múltiple) de tu país. Servirán para comprobar cuánto saben los modelos de lenguaje sobre la historia, la literatura o la cultura de tu país.",
    dates: "4 de mayo - 31 de mayo",
    points: "1 pto",
    requirements: "Saber buscar en internet",
    link: "https://somosnlp.org/hackathon/retos/include",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "Preguntas culturales (BLEND)",
    description: "Responde preguntas sencillas sobre la cultura de tu país (comida, tradiciones, refranes…). Tus respuestas servirán para crear un examen abierto que mida cuánto saben los modelos sobre cada cultura.",
    dates: "11 de mayo - 31 de mayo",
    points: "2 ptos",
    requirements: "Haber vivido bastante tiempo en un país",
    link: "https://somosnlp.org/hackathon/retos/blend",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  }
]

const mainChallenges = [
  {
    title: "1. Crea un dataset de preferencias",
    description: "Escribe preguntas culturales (prompts) sobre tu país y, en una web tipo \"arena\", elige cuál de las dos respuestas que da el modelo es mejor. Lo que recopilemos entre todas las personas participantes servirá para enseñar a los modelos a responder de manera más alineada con las preferencias humanas.",
    dates: "4 de mayo - 21 de mayo",
    points: "3 ptos",
    requirements: "Haber vivido en un país y tener ganas de aprender qué es la \"adecuación cultural\"",
    link: "https://somosnlp.org/hackathon/retos/preferencias",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "2.A. Alinea un modelo de texto (LLM)",
    description: "Usa datasets (incluyendo, si quieres, el del paso 1) para post-entrenar un modelo de lenguaje que genere respuestas de mejor calidad (razonamiento correcto, seguras, adecuadas al contexto cultural). Utiliza técnicas y algoritmos como LoRA, cuantización, DPO, RLVR o test-time learning, ¡explora lo que quieras!",
    dates: "21 de abril - 31 de mayo (Máx. 2 semanas)",
    points: "3 ptos",
    requirements: "Saber programar en Python",
    link: "https://somosnlp.org/hackathon/retos/alineamiento",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "2.B. Mejora un modelo multimodal (texto + imagen)",
    description: "Crea un dataset de imágenes con descripciones y entrena un modelo que sepa describir imágenes teniendo en cuenta el contexto cultural.",
    dates: "21 de abril - 31 de mayo (Máx. 2 semanas)",
    points: "3 ptos",
    requirements: "Tener experiencia previa con modelos de lenguaje",
    link: "https://somosnlp.org/hackathon/retos/alineamiento",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  }
]

const finalChallenges = [
  {
    title: "3. Crea una demo",
    description: "Crea una demo de tu proyecto en un Space de HuggingFace para que todo el mundo pueda ver tu trabajo.",
    dates: "Hasta el 3 de junio",
    points: "0.5 ptos",
    requirements: "Haber completado algún reto principal",
    link: "https://somosnlp.org/hackathon/retos/presentacion",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "4. Graba un vídeo",
    description: "Graba un vídeo de 5 minutos presentando tu proyecto al jurado y a la comunidad.",
    dates: "Envío hasta el 3 de junio",
    points: "0.5 ptos",
    requirements: "Haber completado algún reto principal",
    link: "https://somosnlp.org/hackathon/retos/presentacion",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "5. (Opcional) Escribe un paper",
    description: "Escribe un artículo científico (paper) sobre tu proyecto. Si te interesa, te ayudamos para enviarlo a un workshop de una conferencia de PLN.",
    dates: "A partir de junio",
    points: "0.5 ptos",
    requirements: "Haber completado algún reto principal",
    link: "https://somosnlp.org/hackathon/retos/presentacion",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  }
]
</script>

El hackathon de este año se centra en la última fase de entrenamiento de modelos de lenguaje, aquella en la que se mejora su capacidad de razonamiento y se alinean las respuestas con las preferencias humanas. **El objetivo es que los modelos generen texto correcto, seguro y adecuado al contexto cultural en nuestro idioma.** Además, como siempre, ponemos el foco en la creación de recursos que permitan la evaluación y el alineamiento de modelos de lenguaje con la cultura de los países de LATAM y la Península Ibérica.

**No hace falta saber de inteligencia artificial para participar.** Hay retos para todos los niveles, desde buscar exámenes en internet hasta post-entrenar tu propio modelo. En cada reto explicamos los conceptos y pasos. También tendrás acceso a talleres y a una comunidad para preguntar tus dudas.

En esta página encontrarás:
- 👣 Primeros pasos
- 🧭 ¿Por dónde empiezo?
- 👏 Incentivos y premios
- ✨ Mini retos
- 🔥 Reto principal
- ❓ Preguntas frecuentes

¡Mucho éxito! 🚀

---

## 👣 Primeros pasos

Antes de empezar, haz estas 4 cosas (te llevará menos de 10 minutos):

1. ✅ Únete a nuestro [Discord](https://discord.com/invite/my8w7JUxZR) (es donde nos comunicamos durante el hackathon)
2. ✅ Crea una cuenta gratuita en [Hugging Face](https://huggingface.co/join) (la plataforma donde se publican los datos y modelos)
3. ✅ Rellena el [formulario de registro](https://hackathon-somosnlp-2026.eventbrite.com)
4. ✅ Únete a la [organización del hackathon en Hugging Face](https://huggingface.co/organizations/somosnlp-hackathon/share/BMALwncoPyZLRdPuzwugnsDzXHsbLnjjGD)

Después, **forma un equipo (de 1 a 5 personas):**

- Puedes apuntarte con gente que ya conozcas (compañeros/as de clase, del trabajo…) o conocer a otra gente de la comunidad en el canal [#encuentra-equipo](https://discord.com/channels/938134488670675055/1082369575666073611) de Discord.
- Cuando tengáis el equipo formado, **una persona** debe [registrar el equipo en este formulario](https://forms.gle/mLKEURUXGiNhq31T9).

<!-- TODO formulario -->

---

## 🧭 ¿Por dónde empiezo?

Elige el camino que mejor se adapte a ti. **No tienes que hacer todos los retos**, puedes hacer solo los que te apetezcan y sumar puntos.

- 🟢 **Es mi primera vez con IA / no sé programar** → empieza por los **mini retos**. Solo tienes que buscar información o evaluar el conocimiento cultural de modelos de lenguaje.
- 🟡 **Sé algo de programación y quiero aprender** → empieza por los mini retos, haz el **reto principal opción A** (modelo de texto) y no te pierdas el taller inaugural.
- 🔴 **Tengo experiencia con modelos de lenguaje** → utiliza técnicas tan avanzadas como quieras para el reto principal (A o B). Si ya controlas SFT y DPO, explora test-time learning!

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

<!-- TODO premios -->

---

## ✨ Puntuación

💡 Puedes conseguir hasta **10 puntos en total**: 3 por los mini retos, 6 por el reto principal y 1 por la presentación final.

---

## ✨ Mini retos

Tareas cortas que puedes hacer sin programar. Ayudan a crear bases de datos para evaluar y mejorar cuánto saben los modelos de lenguaje sobre nuestra cultura. **Acumulan puntos y dan acceso a premios extra.**

<ChallengesGrid :challenges="miniChallenges" />

---

## 🔥 Reto principal

Un proyecto completo en 5 pasos. Te guiaremos con talleres y mentorías:

1. **Crea un dataset de preferencias**, diseña preguntas culturales y elige las mejores respuestas
2. **Mejora un modelo de IA** para que responda de manera precisa, segura y contextualizada
3. **Crea una demo** de tu proyecto
4. **Graba un vídeo** de 5 minutos presentando tu trabajo
5. *(Opcional)* **Escribe un paper** científico

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
- ✅ Resolver tus dudas sobre PLN durante sesiones de mentoría "Ask My Anything"
- ✅ Recibir apoyo para presentar tu trabajo en un paper
- ✅ Ganar premios para seguir creciendo como profesional y conseguir un certificado que poder compartir en LinkedIn
- ✅ Unirte a la mayor comunidad open-source iberoamericana de PLN

</details>

<details>
<summary>¿Qué nivel necesito tener?</summary>

**Cualquier nivel.** En ediciones anteriores han participado desde grupos de investigación con doctorado hasta estudiantes de grado. Si nunca has hecho un proyecto de IA, los **mini retos** son un buen punto de partida.

Para acompañarte tendrás:

- 📖 **Talleres prácticos** que te enseñan paso a paso cómo desarrollar el proyecto y notebooks de ejemplo.
- ❓ **Sesiones AMA** ("Ask Me Anything", o sea "pregúntame lo que quieras") con personas expertas que resolverán tus dudas.

</details>

<details>
<summary>¿Cómo de difícil es el reto principal?</summary>

Tú decides. Os daremos un **ejemplo base** que muestra paso a paso cómo crear un dataset, entrenar un modelo y publicar una demo. A partir de ahí, cada equipo decide cuánto quiere profundizar: el tema, de dónde sacar los datos, qué técnica de entrenamiento usar, lo elaborada que sea la demo… ¡Tenéis libertad total!

</details>

<!-- <details>
<summary>¿Cómo se elige la temática de las bases de datos/modelos?</summary>

La temática de los proyectos es siempre libre. Este año el enfoque es representar la riqueza del español, por lo que os animamos a crear proyectos relacionados con vuestro país (leyes, manera de hablar, cultura, ...). Además, como es habitual, os animamos a que los proyectos tengan impacto social y estén relacionados con alguno de los Objetivos de Desarrollo Sostenibles de la ONU. Si buscas inspiración, en el canal #encuentra-equipo de Discord puedes encontrar temas propuestos.

</details> -->

<details>
<summary>¿Necesito de verdad 4 semanas para hacerlo?</summary>

No. Dependiendo de tu disponibilidad se puede sacar un buen proyecto en **una semana**. Damos un plazo amplio porque sabemos que la mayoría de la gente estudia o trabaja, por lo que dejamos más tiempo del necesario para que todo el mundo pueda participar.

</details>

<details>
<summary>¿Hasta cuándo puedo crear un equipo?</summary>

Puedes crear un equipo nuevo **hasta el 15 de mayo**. La fecha límite para entregar los proyectos es el **31 de mayo**.

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
<summary>¿Cómo nos recomendáis organizarnos en equipo?</summary>

- Usad el canal de vuestro proyecto en Discord para comunicaros y organizaros.
- Como es un hackathon internacional, recomendamos **comunicación asíncrona** (mensajes que cada persona contesta cuando puede) o reuniones pequeñas, ya que la gente está en zonas horarias distintas.
- Para hablar en directo, podéis usar las **salas de voz** de Discord (categoría "SALAS DE REUNIÓN").
- **Fijad los mensajes importantes** (reparto de tareas, próxima reunión…) en el canal del equipo: pulsad los tres puntos sobre el mensaje y elegid "Fijar mensaje".
- Os puede ayudar tener un **documento compartido** (Google Docs, Notion…) con el objetivo del proyecto y el reparto de tareas. Fijad el enlace en el chat.

</details>

<details>
<summary>Es mi primera vez en Discord, ¿qué canales miro?</summary>

- 📣 [**#anuncios**](https://discord.com/channels/938134488670675055/944255490748207115): publicamos aprox 2 veces por semana. Te recomendamos **activar las notificaciones** de este canal.
- 🆘 [**#pide-ayuda**](https://discord.com/channels/938134488670675055/1051997272356966430): pregunta aquí tus dudas. Si una persona tiene tu duda, seguramente otras también la tengan, así la respuesta sirve para todo el mundo.
- 📅 [**#eventos**](https://discord.com/channels/938134488670675055/939934987581534228): anunciamos talleres y mentorías. También puedes [añadir nuestro calendario de Google](https://calendar.google.com/calendar/u/0?cid=ZWM3MGZhODIzNmYyNzBlMTYwYzFiMjdhNDgzZWMyMjA1ZjQwYzUyN2E5N2MwZTJhZmY0OTcwZDZmZjBkYzQyMEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t) al tuyo.

</details>

<details>
<summary>¿Cómo me puedo enterar de los eventos?</summary>

- Anunciamos los eventos en el canal [#eventos](https://discord.com/channels/938134488670675055/939934987581534228)
- Los añadimos al [calendario de Google](https://calendar.google.com/calendar/u/0?cid=ZWM3MGZhODIzNmYyNzBlMTYwYzFiMjdhNDgzZWMyMjA1ZjQwYzUyN2E5N2MwZTJhZmY0OTcwZDZmZjBkYzQyMEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t)
- Los anunciamos en redes sociales ([LinkedIn](https://www.linkedin.com/company/somosnlp), [X (Twitter)](https://x.com/somosnlp_))
- [Síguenos en YouTube](https://www.youtube.com/c/somosnlp?sub_confirmation=1) y guarda la [playlist del hackathon 2026](https://www.youtube.com/playlist?list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6)

</details>

<details>
<summary>¿Cómo puedo dar feedback del evento?</summary>

- Nos puedes dar feedback para mejorar las guías de los retos con este [formulario](https://forms.gle/LjQBb8B3XGqPs8Ws9) (anónimo)
- Compartiremos también un formulario de feedback general al final del evento

</details>


---

## 🙌 Otras maneras de apoyar la adecuación cultural de los LLMs

<details>
<summary>¿Cómo puedo colaborar?</summary>

- Comparte las publicaciones de @SomosNLP ([LinkedIn](https://www.linkedin.com/company/somosnlp), [X (Twitter)](https://x.com/somosnlp_)) e invita a colegas y compañeros/as de clase a formar un equipo.
<!-- - ¿Tienes 2 horitas para ayudarnos con la organización de este increíble evento? Te estamos esperando, [únete al equipo](https://forms.gle/radg18NMLRZMPu38A). -->
- ¿Estás en la uni? [Comparte esta info con tu profe](https://somosnlp.org/hackathon/universidades) o alguien del grupo de IA/informática para que tu universidad colabore con el evento.
<!-- - ¿Te gustaría compartir tu conocimiento con la comunidad? Propón una [ponencia](https://forms.gle/YpUvifDNLG6E56Cy9) o una [mentoría](https://forms.gle/7UmsVDnFmNo1pCrf9). 
- ¿Formas parte de un grupo de investigación? Igual os interesa [colaborar donando un corpus](https://somosnlp.org/donatucorpus).-->
- ¿Quieres apoyar la iniciativa dando visibilidad, patrocinando vales o con una donación económica? ¡[Patrocina el hackathon](https://forms.gle/sEkxstwbJSRYpgDa8)!

</details>



<!-- ## 🗓️ Eventos

#### Automatizando extracción de corpus desde PDFs | Alfonso Amayuelas, PhD @ Universidad de California, Santa Barbara

¿Cómo usar las últimas herramientas en LLMs para crear QA datasets? En este evento usaremos un modelo de OCR y LLMs para estandarizar exámenes, cuestionarios, etc. 

[¡Grabación ya disponible!](https://www.youtube.com/watch?v=Jk70bSw4tTo&list=PLTA-KAy8nxaCGGYz5CWiLZNzc31ilPDyI&index=3)

![alt text](/images/eventos/250415_alfonso_amayuelas.png)


#### Confidently wrong: expresando incertidumbre en tareas multilinguales | Selene Baez, Postdoc @ University of Zurich

Si bien la fluidez y la coherencia de los Modelos de Lenguaje (LLM) en la generación de texto han mejorado significativamente, su capacidad para generar expresiones adecuadas de incertidumbre sigue siendo limitada. Mediante una tarea de Q&A multilingüe a libro cerrado y GPT-3.5, exploramos la precisión con la que los LLM se calibran y expresan certeza en una variedad de idiomas, incluyendo entornos con bajos recursos.

[¡Grabación disponible!](https://www.youtube.com/watch?v=TC9tOEyPqy8&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6)

![alt text](/images/eventos/250410_selene_baez.png)

#### Red Teaming para Modelos de Lenguaje | Luis Vasquez, Research Engineer @Barcelona Supercomputing Center

Breve introducción al Red Teaming para Modelos de Lenguaje: definición, estrategias comunes y recursos.

[¡Grabación disponible!](https://www.youtube.com/watch?v=pGOXE4rrO9M&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6)

![alt text](/images/eventos/250410_luis_vasquez.png) -->
