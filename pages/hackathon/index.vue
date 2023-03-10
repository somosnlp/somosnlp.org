<script setup lang="ts" >
import { useHead } from '@vueuse/head'

useHead({
    title: 'Hackathon Somos NLP 2023 - Democratizando el NLP en español',
    meta: [
        { name: 'twitter:card', content: 'summary_large_image' },
        { name: 'twitter:site', content: '@somosnlp_' },
        { name: 'twitter:creator', content: '@somosnlp_' },
        { name: 'twitter:title', content: 'Hackathon Somos NLP 2023' },
        { name: 'twitter:description', content: '¡Únete a la segunda edición del mayor hackathon open-source de Procesamiento del Lenguaje Natural en español!' },
        { name: 'twitter:image', content: 'https://somosnlp.github.io/assets/images/eventos/230320_hackathon.png' },
        { name: 'twitter:image:alt', content: 'Cartel del Hackathon de Somos NLP' }
    ]
})
</script>

<template>
    <Container class="my-12">
        <header class="m-auto text-center prose">
            <h1>Hackathon 2023 de PLN en Español</h1>
            <p class="text-lg">
                Construye al lado de profesionales, expertas y mentores la siguiente generación de modelos de Procesamiento
                del Lenguaje Natural
            </p>
        </header>
        <hr class="mx-auto mt-8 mb-12 prose" />

        <article class="m-auto prose">
            <p>
                Después de una primera edición en la que contamos con más de 500 participantes de 29 países distintos,
                superamos las 5.000 visualizaciones de nuestros eventos, aprendimos de 11 ponentes, finalizamos 22 proyectos
                y publicamos 3 papers.... ¡Volvemos a por eso y mucho más!
            </p>
            <p>
                ¡Únete a la segunda edición del mayor hackathon open-source de Procesamiento del Lenguaje Natural en
                español!
            </p>
            <div class="flex justify-center">
                <img src="https://github.com/somosnlp/assets/raw/main/images/eventos/230320_hackathon.jpg" width="650"
                    height="365" alt="Cartel del Hackathon 2023" />
            </div>

            <p>
                La democratización del PLN en español es el objetivo principal
                de nuestra comunidad y una de las mejores maneras de avanzar
                hacia este objetivo es creando más recursos abiertos de PLN en
                nuestro idioma.
            </p>
            <p>
                Con este hackathon te animamos a unirte a nuestro esfuerzo 🚀
            </p>

            <hr class="mx-auto my-12 prose" />
            <p>
                ➡️ Las charlas y talleres están abiertas a todo el mundo,
                independientemente de si participas en el hackathon.
                <a href="https://www.eventbrite.com/e/registro-ii-hackathon-somos-nlp-565283938477?aff=w" target="_blank">
                    ¡Regístrate ya!
                </a>
            </p>
            <hr class="mx-auto mt-8 mb-12 prose" />

            <div class="m-12">
                <ul>
                    <li>
                        <a href="#motivación">Motivación</a>
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
                        <a href="#equipo">Equipo</a>
                    </li>
                    <li>
                        <a href="#patrocinios">Patrocinios</a>
                    </li>
                </ul>
            </div>
            <hr class="mx-auto my-12 prose" />

            <h2 id="motivación">🚀 Motivación</h2>
            <p>Al unirte a este evento tendrás la oportunidad de:</p>
            <ul>
                <li>Ayudar al avance y la democratización del PLN en español</li>
                <li>
                    Asistir a charlas y talleres impartidas por profesionales trabajando e investigando en el mundo del PLN
                </li>
                <li>Consultar tus dudas sobre PLN con mentores y expertas</li>
                <li>Recibir apoyo para presentar un paper a una conferencia</li>
                <li>... y mucho más por anunciar</li>
            </ul>
            <a href="https://www.eventbrite.com/e/registro-ii-hackathon-somos-nlp-565283938477?aff=w" target="_blank">
                ¡Regístrate ya!
            </a>
            <h2 id="bases-del-hackathon">💻 Bases del Hackathon</h2>
            <p>
                Participar en nuestro hackathon y aplicar tus conocimientos a una buena causa es muy sencillo, ¡anímate!
            </p>
            <ol>
                <li>
                    Únete a nuestra comunidad de
                    <a href="https://discord.com/invite/my8w7JUxZR" target="_blank">Discord</a> y
                    crea una cuenta en el Hub de
                    <a href="https://huggingface.co/join" target="_blank">Hugging Face</a> si
                    todavía no tienes una.
                </li>
                <li>Regístrate en
                    <a href="https://www.eventbrite.com/e/registro-ii-hackathon-somos-nlp-565283938477?aff=w"
                        target="_blank">Eventbrite</a>.
                </li>
                <li>
                    Únete a la organización
                    <a href="https://huggingface.co/organizations/hackathon-somos-nlp-2023/share/YPgLHyEfyVvfnHMYmPbisOqmWTOzQxSDYI"
                        target="_blank">hackathon-somos-nlp-2023</a>
                    del Hub de Hugging Face.
                </li>
                <li>
                    Reúne tu equipo (de 1 a 5 personas). Si todavía no tienes
                    equipo puedes utilizar el canal #encuentra-equipo para
                    crear uno nuevo o unirte a uno existente.
                </li>
            </ol>
            <p>
                ¡Todo listo para poder empezar! Daremos más información sobre
                el tema del hackathon una semana antes de su comienzo.
            </p>

            <h2 id="evaluacion-y-premios">🏆 Evaluación y Premios</h2>
            <p>
                A la hora de evaluar los proyectos, dado que cada equipo
                utilizará un dataset diferente y entrenará su modelo para
                resolver una tarea diferente, además de tener en cuenta el
                valor de las métricas, los criterios de evaluación incluirán el
                impacto social del proyecto, la originalidad de la idea y la
                dificultad técnica. Los publicaremos próximamente.
            </p>
            <p>
                Estamos hablando con nuestros patrocinadores,
                mantendremos esta sección actualizada 😉
            </p>

            <h2 id="recursos">📖 Recursos</h2>
            <p>
                Desde el equipo de Somos NLP queremos animarte a participar
                independientemente de tus conocimientos actuales.
            </p>
            <ul>
                <li>
                    En nuestra sección "Recursos"
                    <a href="recursos">(somosnlp.org/recursos)</a>
                    puedes encontrar tanto listas de
                    <b>datasets y modelos open-source</b> como
                    <b>tutoriales</b> explicando cómo hacer fine-tuning
                    para desarrollar tu proyecto.
                </li>
                <li>
                    También daremos un <b>taller práctico</b> el primer día del
                    hackathon en el cual crearemos una base de datos,
                    entrenaremos un modelo y desarrollaremos una demo para que
                    tengas un ejemplo de proyecto de referencia.
                </li>
                <li>
                    Organizaremos
                    <b>AMAs</b> (del inglés, Ask Me Anything) con expertas y
                    mentores para que puedan solucionar tus dudas.
                </li>
                <li>
                    Además, durante la celebración del hackathon estaremos a tu
                    disposición en el canal <b>#pide-ayuda</b> de Discord para
                    guiarte y ayudarte a desarrollar tu proyecto.
                </li>
            </ul>

            <h2 id="charlas-y-talleres">💡 Charlas y Talleres</h2>
            <p>
                Durante el hackathon tendrán lugar diversas charlas y talleres
                impartidas por profesionales del mundo del Procesamiento del
                Lenguaje Natural. Estos eventos están abiertos a todas las
                personas, independientemente de si participan en el hackathon,
                <a href="https://www.eventbrite.com/e/registro-ii-hackathon-somos-nlp-565283938477?aff=w"
                    target="_blank">¡apúntate!</a>
            </p>
            <p>
                Iremos anunciando los eventos uno a uno así que atención a
                <a href="https://twitter.com/somosnlp_" target="_blank">Twitter</a> y
                <a href="https://www.linkedin.com/company/somosnlp" target="_blank">LinkedIn</a>🔥
            </p>
            <p>
                ¿No puedes esperar hasta el 20 de marzo? Visualiza las grabaciones de las
                <a href="https://www.youtube.com/playlist?list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG" target="_blank">
                    charlas y talleres del Hackathon 2022
                </a>.
            </p>

            <h2 id="equipo">👏 Equipo</h2>
            <p>
                ¿Quieres ayudarnos a organizar este hackathon?
                Crea, diseña, escribe... apóyanos haciendo lo que mejor se te dé. Háblanos por Discord o mándanos un correo
                a
                <a href="mailto:info@somosnlp.org" target="_blank">info@somosnlp.org</a>,
                ¡estamos esperándote!
            </p>

            <h2 id="patrocinios">👏 Patrocinios</h2>
            <p>
                ¿Quieres patrocinar este hackathon y ayudarnos a democratizar el PLN en español? Mándanos un correo a
                <a href="mailto:info@somosnlp.org" target="_blank">info@somosnlp.org</a>,
                ¡será un placer contar con tu apoyo!
            </p>

        </article>
    </Container>
</template>
