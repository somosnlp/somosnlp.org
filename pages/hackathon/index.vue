<script setup lang="ts" >
import { useHead } from '@vueuse/head'

useHead({
    title: 'Hackathon Somos NLP 2023 - Democratizando el NLP en español',
    meta: [
        { name: 'twitter:card', content: 'summary' },
        { name: 'twitter:site', content: '@somosnlp_' },
        { name: 'twitter:creator', content: '@somosnlp_' },
        { name: 'twitter:title', content: 'Hackathon Somos NLP 2023' },
        { name: 'twitter:description', content: '¡Únete al mayor hackathon open-source de Procesamiento del Lenguaje Natural en español!' },
        { name: 'twitter:image', content: 'https://somosnlp.github.io/assets/images/hackathon_pln_es_3.png' },
        { name: 'twitter:image:alt', content: 'Cartel del Hackathon de Somos NLP' }
    ]
})
</script>

<template>
    <Container class="my-12">
        <header class="m-auto text-center prose">
            <h1>Hackathon 2023 de PLN en Español</h1>
            <p class="text-lg">
                Construye al lado de mentores, expertas y hackers la siguiente generación de modelos
                de Procesamiento del Lenguaje Natural
            </p>
        </header>
        <hr class="mx-auto mt-8 mb-12 prose" />

        <div class="m-auto text-center prose">
            EVENTO FINALIZADO: El hackathon 2022 ya ha finalizado, puedes ver los
            <a href="https://hf.co/hackathon-pln-es" target="_blank">proyectos</a>
            de los equipos participantes y las grabaciones de
            <a href="https://www.youtube.com/c/somosnlp?sub_confirmation=1" target="_blank">todas las charlas y
                talleres</a>.
            ¡Únete a la comunidad en Discord y síguenos en RRSS para participar en futuros eventos!
        </div>
        <hr class="mx-auto mt-8 mb-12 prose" />

        <article class="m-auto prose">
            ¡Únete al mayor hackathon open-source de Procesamiento del Lenguaje Natural en español!
            <div class="flex justify-center">
                <img src="https://github.com/somosnlp/assets/raw/main/images/hackathon_pln_es_3.png" width="650"
                    height="365" alt="Cartel del hackathon" />
            </div>

            <p>
                La democratización del PLN en español es el objetivo principal de nuestra comunidad
                y una de las mejores maneras de avanzar hacia este objetivo es creando más recursos
                de PLN en nuestro idioma.
            </p>
            <p>
                Con este hackathon te animamos a unirte a nuestro esfuerzo. Te invitamos a entrenar
                y poner en producción un modelo de PLN en español.
            </p>

            <hr class="mx-auto my-12 prose" />
            <div class="m-12">
                <ul>
                    <li>
                        <a href="#evento">Evento</a>
                    </li>
                    <li>
                        <a href="#bases-del-hackathon">Bases del Hackathon</a>
                    </li>
                    <li>
                        <a href="#evaluacion-y-premios">Evaluación y Premios</a>
                    </li>
                    <li>
                        <a href="#recursos">Recursos</a>
                    </li>
                    <li>
                        <a href="#charlas-y-talleres">Charlas y Talleres</a>
                    </li>
                    <li>
                        <a href="#patrocinadores">Patrocinadores</a>
                    </li>
                </ul>
            </div>
            <hr class="mx-auto my-12 prose" />

            <h2 id="evento">🚀 Evento</h2>
            <p>Al unirte a este evento tendrás la oportunidad de:</p>
            <ul>
                <li>Ayudar al avance y la democratización del PLN en español</li>
                <li>Asistir a charlas y talleres impartidas por profesionales trabajando e investigando en el mundo del
                    PLN</li>
                <li>Consultar tus dudas sobre PLN con mentores y expertas</li>
                <li>Mucho más por anunciar</li>
            </ul>
            <a href="wip" target="_blank">¡Regístrate ya!</a>
            <h2 id="bases-del-hackathon">💻 Bases del Hackathon</h2>
            <p>
                Participar en nuestro hackathon y aplicar tus conocimientos a una buena causa es muy
                sencillo, ¡anímate!
            </p>
            <ol>
                <li>
                    Crea una cuenta en
                    <a href="https://huggingface.co/join" target="_blank">Hugging Face</a> si
                    todavía no tienes una y regístrate
                    <a href="https://hackathon-pln-es.eventbrite.com/?aff=website" target="_blank">aquí</a>.
                </li>
                <li>
                    Únete a nuestra comunidad de
                    <a href="https://discord.com/invite/my8w7JUxZR" target="_blank">Discord</a>
                    y haz click en "request to join this org" en la organización
                    <a href="wip" target="_blank">hackathon-somos-nlp-2023</a> de Hugging
                    Face.
                </li>
                <li>
                    Echa un vistazo a los diferentes canales de Discord, sobre
                    todo a los de la sección "HACKATHON", ya que iremos
                    anunciando talleres y material con el que preparar el
                    hackathon y también resolveremos las dudas que te puedan
                    surgir durante el evento.
                </li>
                <li>
                    Reúne tu equipo (de 1 a 5 personas). Si todavía no tienes equipo puedes utilizar
                    el canal #encuentra-equipo para crear uno nuevo o unirte a uno existente. Apunta
                    tu proyecto y los handles de HF de los miembros del equipo en la hoja de cálculo
                    que está en la descripción del canal #encuentra-equipo, os mandaremos por correo
                    el código de vuestra GPU de Paperspace.
                </li>
                <li>
                    Busca una base de datos para entrenar tu modelo. Puede estar en
                    <a href="https://hf.co/datasets" target="_blank">datasets</a>, en otra plataforma online o la puedes
                    crear desde cero y subirla a
                    <a href="wip" target="_blank">hackathon-somos-nlp-2023</a>.
                </li>
                <li>
                    Junto con tu equipo, entrena y sube a
                    <a href="wip" target="_blank">hackathon-somos-nlp-2023</a>
                    uno o varios modelos. Desde la comunidad queremos animar a
                    todos los equipos a entrenar modelos que sirvan para abordar
                    alguno de los
                    <a href="https://www.un.org/sustainabledevelopment/es/objetivos-de-desarrollo-sostenible/"
                        target="_blank">Objetivos de Desarrollo Sostenible de la ONU</a>.
                </li>
                <li>
                    Asegúrate de incluir una "Model Card" explicando, entre otras cosas, el
                    origen de los datos utilizados y el proceso de entrenamiento del modelo.
                </li>
                <li>
                    Crea una demo de el/los modelo/s utilizando la tecnología
                    que prefieras (e.g. Gradio, Streamlit, Flask, FastAPI).
                    Puedes utilizar Spaces de Hugging Face para crear tu demo en
                    <a href="wip" target="_blank">hackathon-somos-nlp-2023</a>.
                </li>
                <li>
                    Por último, rellena este
                    <a href="wip" target="_blank">formulario</a> para
                    presentar el proyecto.
                </li>
            </ol>
            <p>
                Un jurado formado por especialistas en PLN (por anunciar) elegirá los tres equipos
                ganadores. Además, se concederá una mención de honor al mejor proyecto enfocado a un
                Objetivo de Desarrollo Sostenible y otra al que consiga más ❤️ en el Hub de Hugging Face.
            </p>
            <p>¡Buena suerte!</p>

            <h2 id="evaluacion-y-premios">🏆 Evaluación y Premios</h2>
            <p>
                A la hora de evaluar los proyectos, dado que cada equipo
                utilizará un dataset diferente y entrenará su modelo para
                resolver una tarea diferente, además de tener en cuanta el
                valor de las métricas, los criterios de evaluación incluirán el
                impacto social del proyecto, la originalidad de la idea y la
                dificultad técnica.
            </p>
            <p>
                Nota: Seguimos hablando con nuestros patrocinadores, mantendremos esta
                sección actualizada.
            </p>

            <h2 id="recursos">📖 Recursos</h2>
            <p>
                Desde el equipo de Somos NLP queremos animarte a participar
                independientemente de tus conocimientos actuales.
            </p>
            <ul>
                <li>
                    En nuestra sección "Recursos"
                    <a href="recursos">(somosnlp.org/recursos)</a> puedes
                    encontrar tanto listas de
                    <b>datasets y modelos open-source</b>
                    como <b>tutoriales</b> explicando cómo hacer fine-tuning
                    para desarrollar tu proyecto.
                </li>
                <li>
                    También daremos un
                    <b>
                        taller práctico
                    </b> el primer día del hackathon en el cual crearemos una
                    base de datos, entrenaremos un modelo y desarrollaremos una
                    demo para que tengas un ejemplo de proyecto de referencia.
                </li>
                <li>
                    Organizaremos
                    <b>AMAs</b> (del inglés, Ask Me Anything) con expertas y
                    mentoras en NLP para que puedan solucionar tus dudas.
                </li>
                <li>
                    Además, durante la celebración del hackathon estaremos a tu
                    disposición en <b>Discord</b> para guiarte y ayudarte a
                    desarrollar tu proyecto.
                </li>
            </ul>

            <h2 id="charlas-y-talleres">💡 Charlas y Talleres</h2>
            <p>
                Durante el hackathon tendrán lugar diversas charlas y talleres
                impartidas por profesionales del mundo del Procesamiento del
                Lenguaje Natural. Estos eventos están abiertos a todas las
                personas, independientemente de si participan en el hackathon,
                <a href="wip" target="_blank">¡apúntate!</a>
            </p>
            <p>
                Iremos anunciando los eventos uno a uno así que atención a
                <a href="https://twitter.com/somosnlp_" target="_blank">Twitter</a> y
                <a href="https://www.linkedin.com/company/somosnlp" target="_blank">LinkedIn</a>🔥
            </p>
            <p>
                ➡️ Subiremos las grabaciones de todas las charlas y talleres a
                <a href="https://www.youtube.com/c/somosnlp?sub_confirmation=1" target="_blank">YouTube</a>
                para que las puedas ver cuando te venga bien.
            </p>

        </article>
    </Container>
</template>
