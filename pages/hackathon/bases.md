---
title: Bases del Hackathon #Somos600M
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

*Nota: Si te hemos dicho que aquí hay info que no encuentras, borra las cookies y recarga la página.*

## 👀 Maneras de participar

Como sabes, la iniciativa #Somos600M tiene dos objetivos:

### ✅ Crear la primera leaderboard de LLMs

Ayúdanos a validar en comunidad las traducciones hechas por el Grupo de PLN de la Universidad de Oregon de las bases de datos utilizadas en la famosa [Open LLM Leaderboard de Hugging Face](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard). Gracias al apoyo de Argilla y Hugging Face, en concreto de Álvaro Bartolomé, Daniel Vila y Omar Sanseviero, colaborar es muy sencillo:

1. Crea una cuenta en [Hugging Face](https://huggingface.co/join) y únete a la organización de [SomosNLP](https://huggingface.co/organizations/somosnlp/share/qgytUhPKvxVxsbZWTzVUAUSUnZmVXNPmjc)

2. Entra en …

3. Verifica la traducción de un párrafo del inglés al español

4. Repite el paso 3 cuantas veces quieras y ¡mira cómo subes en el ranking de colaboraciones!

5. Tu nombre aparecerá como parte del equipo que creó las bases de datos de la futura leaderboard de LLMs en español 🙌

### 🌎 Crear el mayor corpus de instrucciones

Participar en nuestro hackathon y aplicar tus conocimientos a democratizar el PLN en español es muy sencillo, ¡anímate!

1. Únete a nuestra comunidad de [Discord](https://discord.com/invite/my8w7JUxZR) (¡y preséntate en #intros!)

2. Crea una cuenta en [Hugging Face](https://huggingface.co/join) y únete a la organización de [SomosNLP](https://huggingface.co/organizations/somosnlp/share/qgytUhPKvxVxsbZWTzVUAUSUnZmVXNPmjc).

3. Regístrate en [Eventbrite](https://hackathonsomosnlp2024.eventbrite.com/?aff=w).

4. Crea tu equipo o únete a uno (equipos de de 1 a 5 personas). Hay que inscribir los equipos en el canal **#encuentra-equipo** (más info en el README del canal).

5. Crea tu corpus en la org de hf.co/SomosNLP, te animamos a crear un corpus de instrucciones originalmente en español. Te recomendados utilizar la librería `distilabel`. Próximamente el equipo de Argilla publicará un notebook de ejemplo.

6. Escribe la Dataset Card de tu dataset: inspecciona el dataset, evalúa y mitiga sesgos.

7. Fine-tuning de un LLM para la tarea que hayas elegido y *push to hub*. Pondremos a vuestra disposición GPU VMs 24GB, avísanos cuando tengas el dataset y esté todo listo para empezar el entrenamiento. Recuerda que es muy importante hacer pruebas en máquinas más humildes para verificar que el código es correcto y no encontrar errores después de varias horas de entrenamiento.

8. Escribe la Model Card de tu modelo: evalúa su calidad, sesgos y huella de carbono. Importante: enlaza el dataset utilizado para el entrenamiento.

9. Crea una demo para mostrar tu proyecto a la comunidad. Puedes utilizar GPUs Nvidia T4 - small. Importante: enlaza los dataset(s) y modelo(s) utilizados.

10. Entrega tu proyecto rellenando un formulario que publicaremos próximamente. Puedes seguir haciendo modificaciones hasta las 23h59 *Anywhere on Earth* del domingo 24 de marzo (revisaremos la hora de los commits 👀).

Si tienes cualquier duda estamos a tu disposición en el canal #pide-ayuda, escribe un título descriptivo y utiliza la etiqueta "hackathon".

¡Mucho éxito! 🚀

<!--

Al finalizar el hackathon, habremos creado el mayor corpus de instrucciones abierto originalmente en español y lenguas cooficiales.

### O... dona tu corpus

También puedes colaborar con ambos objetivos donando un corpus que hayas creado con tu grupo de investigación o empresa, [¡dona tu corpus!](https://somosnlp.org/donatucorpus) -->

## ❓ Preguntas frecuentes

<details>
<summary>¿Por qué debería participar?</summary>

Al unirte a este hackathon tendrás la oportunidad de:

- ✅ Comprender cómo funcionan los grandes modelos del lenguaje (LLMs) y descubrir los retos de cada etapa de su desarrollo: creación del corpus, entrenamiento y evaluación
- ✅ Participar en la creación de un corpus de calidad y diverso que incluya las distintas variedades del español y lenguas cooficiales (top como experiencia y top para el CV)
- ✅ Resolver todas tus dudas sobre PLN durante sesiones de mentoría "Ask My Anything"
- ✅ Recibir apoyo para presentar tu trabajo en un paper
- ✅ Ganar premios para seguir creciendo como profesional y conseguir un certificado
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

## 🙌 Mientras tanto... apoya la organización del evento

- Comparte los posts de las cuentas de @SomosNLP ([LinkedIn](https://www.linkedin.com/company/somosnlp), [Twitter](https://twitter.com/somosnlp_)), ¡invita a tus colegas del trabajo, compañeros y compañeras de clase a crear un equipo!
- ¿Tienes 2 horitas para ayudarnos con la organización de este increíble evento? Te estamos esperando, [únete al equipo](https://forms.gle/radg18NMLRZMPu38A).
- ¿Estás en la uni? [Comparte esta info con tu profe](https://somosnlp.org/hackathon/universidades) o alguien del grupo de IA/informática para que tu universidad colabore con el evento.
- ¿Te gustaría compartir tu conocimiento con la comunidad? Propón una [ponencia](https://forms.gle/YpUvifDNLG6E56Cy9) o una [mentoría](https://forms.gle/7UmsVDnFmNo1pCrf9).
- ¿Formas parte de un grupo de investigación? Igual os interesa [colaborar donando un corpus](https://somosnlp.org/donatucorpus).
- ¿Quieres apoyar la iniciativa dando visibilidad, patrocinando vales o con una donación económica? ¡[Patrocina el hackathon](https://forms.gle/sEkxstwbJSRYpgDa8)!

<!-- 
## 🏆 Evaluación y Premios

Para que todos los equipos comiencen el hackathon con las mismas oportunidades, las [bases](https://somosnlp.org/hackathon/bases) del hackathon junto con información detallada sobre la evaluación de los proyectos se publicarán en febrero.

Estamos hablando con todo el mundo para conseguir premios increíbles, ¡os mantendremos al corriente!
 -->
