<script setup lang="ts" >
import { useHead } from '@vueuse/head'

useHead({
    title: 'Hackathon SomosNLP 2022 - Democratizando el NLP en español',
    meta: [
        { name: 'twitter:card', content: 'summary_large_image' },
        { name: 'twitter:site', content: '@somosnlp_' },
        { name: 'twitter:creator', content: '@somosnlp_' },
        { name: 'twitter:title', content: 'Hackathon SomosNLP 2022' },
        { name: 'twitter:description', content: '¡Únete al mayor hackathon open-source de Procesamiento del Lenguaje Natural en español!' },
        { name: 'twitter:image', content: '/images/eventos/220314_hackathon_pln_es_3.png' },
        { name: 'twitter:image:alt', content: 'Cartel del Hackathon de SomosNLP' }
    ]
})
</script>

<template>
    <Container class="my-12">
        <header class="m-auto text-center prose">
            <h1>Hackathon 2022 de PLN en Español</h1>
            <p class="text-lg">
                Construye al lado de mentores, expertas y hackers la siguiente generación de modelos
                de Procesamiento del Lenguaje Natural
            </p>
        </header>
        <hr class="mx-auto mt-8 mb-12 prose" />

        <div class="m-auto text-center prose">
            <p>
                La primera edición de nuestro hackathon ya ha finalizado, te animamos a echar un vistazo
                a los
                <a href="https://hf.co/hackathon-pln-es" target="_blank">proyectos</a>
                de los equipos participantes y visualizar las grabaciones de las
                <a href="https://www.youtube.com/playlist?list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG" target="_blank">
                    charlas y talleres
                </a>impartidas por especialistas en el campo del PLN.
            </p>
            <p>
                <a href="https://somosnlp.org/hackathon">
                    ¡Únete a la nueva edición!
                </a>
            </p>
        </div>
        <hr class="mx-auto mt-8 mb-12 prose" />

        <article class="m-auto prose">
            ¡Únete al mayor hackathon open-source de Procesamiento del Lenguaje Natural en español!
            <div class="flex justify-center">
                <img src="/images/eventos/220314_hackathon_pln_es_3.png" width="650"
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
                <li>Conseguir acceso gratis a GPUs patrocinadas por Paperspace</li>
                <li>Participar en un sorteo de copias del libro "Natural Language Processing with Transformers" de Lewis
                    Tunstall, Leandro von Werra y Thomas Wolf</li>
                <li>Conseguir acceso gratis a las plataformas de e-learning de Platzi y O'Reilly</li>
                <li>Canjear bonos por swag de Hugging Face especialmente diseñado para el evento</li>
            </ul>
            <a href="https://hackathon-pln-es.eventbrite.com/?aff=website" target="_blank">¡Regístrate ya!</a>
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
                    <a href="https://huggingface.co/hackathon-pln-es" target="_blank">hackathon-pln-es</a> de Hugging
                    Face.
                </li>
                <li>
                    Echa un vistazo a los diferentes canales de Discord, sobre todo a los de la
                    sección "HACKATHON", ya que iremos anunciando talleres y material con el que
                    preparar el hackathon y también resolveremos las dudas que te puedan surgir
                    durante el evento.
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
                    crear desde cero y subirla
                    a
                    <a href="https://hf.co/hackathon-pln-es" target="_blank">hackathon-pln-es</a>.
                </li>
                <li>
                    Junto con tu equipo, entrena y sube a
                    <a href="https://hf.co/hackathon-pln-es" target="_blank">hackathon-pln-es</a> uno o varios modelos.
                    Desde la comunidad
                    queremos animar a todos los equipos a entrenar modelos que sirvan para abordar
                    alguno de los
                    <a href="https://www.un.org/sustainabledevelopment/es/objetivos-de-desarrollo-sostenible/"
                        target="_blank">Objetivos de Desarrollo Sostenible de la ONU</a>.
                </li>
                <li>
                    Asegúrate de incluir una "Model Card" explicando, entre otras cosas, el
                    origen de los datos utilizados y el proceso de entrenamiento del modelo.
                </li>
                <li>
                    Crea una demo de el/los modelo/s utilizando la tecnología que prefieras
                    (e.g. Gradio, Streamlit, Flask, FastAPI). Puedes utilizar Spaces de Hugging Face
                    para crear tu demo en
                    <a href="https://hf.co/hackathon-pln-es" target="_blank">hackathon-pln-es</a>.
                </li>
                <li>
                    Por último, rellena este
                    <a href="https://kq8ietkql1m.typeform.com/to/BS6HBfy7" target="_blank">formulario</a> para
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
                A la hora de evaluar los proyectos, dado que cada equipo utilizará un dataset
                diferente y entrenará su modelo para resolver una tarea diferente, además de tener
                en cuanta el valor de las métricas, los criterios de evaluación incluirán el impacto
                social del proyecto, la originalidad de la idea y la dificultad técnica.
            </p>
            <p>
                Gracias al patrocinio de Platzi, todas las personas que presenten un proyecto
                ganarán una beca en su plataforma de e-learning:
            </p>
            <ul>
                <li>Participación: Beca de 3 meses</li>
                <li>Segundo y tercer puesto: Beca de 6 meses</li>
                <li>Equipo ganador: Beca Expert de 1 año</li>
            </ul>
            <p>El resto de premios incluirán:</p>
            <ul>
                <li>Certificado de participación/equipo ganador del Hackathon 2022 de PLN en Español</li>
                <li>Rol honorífico en el servidor de Discord, e.g.: "Hackathon 🥇"</li>
                <li>Swag de Hugging Face diseñado especialmente para el hackathon</li>
                <li>Tiempo de computación en GPUs patrocinadas por Paperspace</li>
                <li>Copias del libro "NLP with Transformers"</li>
            </ul>
            <p>
                Además de estos premios, podrás conseguir un mes de acceso gratis a la plataforma de
                e-learning de O'Reilly y participar en el sorteo de copias del libro
                <a href="https://transformersbook.com/" target="_blank">"Natural Language Processing with Transformers"
                    de Lewis Tunstall, Leandro von Werra y Thomas Wolf</a>
                al asistir a uno de nuestros eventos 🎁
            </p>

            <h2 id="recursos">📖 Recursos</h2>
            <p>
                Desde el equipo de SomosNLP queremos animarte a participar independientemente de
                tus conocimientos actuales.
            </p>
            <ul>
                <li>
                    Hemos creando una nueva sección "Recursos"
                    <a href="recursos">(somosnlp.org/recursos)</a> con listas de
                    <b>datasets y modelos open-source</b>
                    que puedes utilizar para hacer fine-tuning como te explicamos en nuestros
                    <b>tutoriales</b>.
                </li>
                <li>
                    También daremos un
                    <b>
                        <a href="https://www.youtube.com/watch?v=_TbNgSodiPY&list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG"
                            target="_blank">taller
                            práctico</a>
                    </b> el primer día del hackathon en el cual
                    crearemos una base de datos, entrenaremos un modelo y desarrollaremos una demo
                    para que tengas un ejemplo de proyecto de referencia.
                </li>
                <li>
                    Organizaremos dos
                    <b>AMAs</b> (del inglés, Ask Me Anything) con dos expertos en NLP
                    para que puedan solucionar tus dudas.
                </li>
                <li>
                    Hemos creado vídeo tutoriales explicando cómo utilizar las GPUs patrocinadas por
                    Paperspace y cómo crear demos en Spaces: echa un vistazo a la lista de YouTube
                    <a href="https://www.youtube.com/playlist?list=PLTA-KAy8nxaB-HA79tlOTRl496_XIlJta"
                        target="_blank">"Tutoriales".</a>
                </li>
                <li>
                    Además, durante las dos semanas que dura el hackathon estaremos a tu disposición
                    en
                    <b>Discord</b> para guiarte y ayudarte a desarrollar tu proyecto.
                </li>
            </ul>

            <h2 id="charlas-y-talleres">💡 Charlas y Talleres</h2>
            <p>
                Durante el hackathon tendrán lugar diversas charlas y talleres impartidas por
                profesionales del mundo del Procesamiento del Lenguaje Natural. Estos eventos están
                abiertos a todas las personas, independientemente de si participan en el hackathon,
                <a href="https://hackathon-pln-es.eventbrite.com/?aff=website" target="_blank">¡apúntate!</a>
            </p>
            <p>
                Iremos anunciando los eventos uno a uno así que atención a
                <a href="https://twitter.com/somosnlp_" target="_blank">Twitter</a> y
                <a href="https://www.linkedin.com/company/somosnlp" target="_blank">LinkedIn</a>🔥
            </p>
            <p>
                ➡️ Subimos las grabaciones de todas las charlas y talleres a la lista de YouTube
                <a href="https://www.youtube.com/playlist?list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG" target="_blank">Hackathon
                    de PLN en Español</a>
                para que las puedas ver cuando te venga bien.
            </p>
            <EventHackathon2022List />

            <h2 id="patrocinadores">👏 Patrocinadores</h2>
            <p>
                Muchísimas gracias por vuestro tiempo y por apoyarnos para que nuestra iniciativa
                llegue más lejos. ¡Vamos a democratizar el PLN en español!
            </p>
            <h3>🥇 Patrocinadores de oro</h3>
            <div class="auto-rows-fr grid gap-x-16 place-items-center lg:grid-cols-3">
                <SponsorInfo sponsor="Paperspace" url="https://www.paperspace.com/"
                    logo="/images/patrocinios/paperspace.svg"
                    logo_dark="/images/patrocinios/paperspace_dark.svg" />
                <SponsorInfo sponsor="Platzi" url="https://platzi.com/"
                    logo="/images/patrocinios/platzi.png"
                    logo_dark="/images/patrocinios/platzi_dark.png" />
                <SponsorInfo sponsor="Hugging Face" url="https://huggingface.co/"
                    logo="/images/patrocinios/HuggingFace.svg"
                    logo_dark="/images/patrocinios/HuggingFace.svg" />
            </div>
            <h3>🥈 Patrocinadores de plata</h3>
            <div class="auto-rows-fr grid gap-x-16 place-items-center lg:grid-cols-3">
                <SponsorInfo sponsor="BSC" url="https://www.bsc.es/"
                    logo="/images/patrocinios/BSC.png"
                    logo_dark="/images/patrocinios/BSC_dark.png" />
                <SponsorInfo sponsor="DiverTLes" url="https://gplsi.dlsi.ua.es/pln/divertles"
                    logo="/images/patrocinios/DiverTLes.png"
                    logo_dark="/images/patrocinios/DiverTLes_dark.png" />
                <SponsorInfo sponsor="IBiDat" url="https://ibidat.es/"
                    logo="/images/patrocinios/IBiDat.png"
                    logo_dark="/images/patrocinios/IBiDat_dark.png" />
                <SponsorInfo sponsor="Narrativa" url="https://www.narrativa.com/"
                    logo="/images/patrocinios/Narrativa.png"
                    logo_dark="/images/patrocinios/Narrativa_dark.png" />
                <SponsorInfo sponsor="Plan TL" url="https://plantl.mineco.gob.es/"
                    logo="/images/patrocinios/PlanTL.png"
                    logo_dark="/images/patrocinios/PlanTL_dark.png" />
                <SponsorInfo sponsor="PLNnet" url="https://gplsi.dlsi.ua.es/pln/"
                    logo="/images/patrocinios/PLNnet.svg"
                    logo_dark="/images/patrocinios/PLNnet.svg" />
                <SponsorInfo sponsor="Saturdays AI" url="https://saturdays.ai/"
                    logo="/images/patrocinios/SaturdaysAI.png"
                    logo_dark="/images/patrocinios/SaturdaysAI.png" />
                <SponsorInfo sponsor="Spain AI" url="https://www.spain-ai.com/"
                    logo="/images/patrocinios/SpainAI.png"
                    logo_dark="/images/patrocinios/SpainAI_dark.png" />
                <SponsorInfo sponsor="UNAM" url="https://www.unam.mx/"
                    logo="/images/patrocinios/UNAM.png"
                    logo_dark="/images/patrocinios/UNAM_dark.png" />
                <SponsorInfo sponsor="UNL" url="https://www.unl.edu.ec/"
                    logo="/images/patrocinios/UNL_square.png"
                    logo_dark="/images/patrocinios/UNL_square.png" />
            </div>
        </article>
    </Container>
</template>
