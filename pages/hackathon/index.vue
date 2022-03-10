<script setup lang="ts">
import { useHead } from '@vueuse/head'

useHead({
    meta: [
        { property: 'og:title', content: 'Hackathon de NLP en Español' },
        { property: 'og:description', content: '¡Únete al mayor hackathon de Procesamiento del Lenguaje Natural en español!' },
        { property: 'og:image', content: 'https://github.com/somosnlp/assets/raw/main/images/hackathon_pln_es_3.png' },
        { name: 'twitter:card', content: 'Hackathon de NLP en Español' },
        { name: 'twitter:creator', content: '@somosnlp_' },
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

        <article class="m-auto prose">
            ¡Únete al mayor hackathon de Procesamiento del Lenguaje Natural en español!
            <div class="flex justify-center">
                <img
                    src="https://github.com/somosnlp/assets/raw/main/images/hackathon_pln_es_3.png"
                    width="650"
                    height="365"
                />
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

            <h2>🚀 Evento</h2>
            <p>Al unirte a este evento tendrás la oportunidad de:</p>
            <ul>
                <li>Ayudar al avance y la democratización del PLN en español</li>
                <li>Asistir a charlas y talleres impartidas por profesionales trabajando e investigando en el mundo del PLN</li>
                <li>Consultar tus dudas sobre PLN con mentores y expertas</li>
                <li>Conseguir acceso gratis a GPUs patrocinadas por Paperspace</li>
                <li>Participar en un sorteo de copias del libro "Natural Language Processing with Transformers" de Lewis Tunstall, Leandro von Werra y Thomas Wolf</li>
                <li>Conseguir acceso gratis a las plataformas de e-learning de Platzi y O'Reilly</li>
                <li>Canjear bonos por swag de Hugging Face especialmente diseñado para el evento</li>
            </ul>
            <a
                href="https://hackathon-pln-es.eventbrite.com/?aff=website"
                target="_blank"
            >¡Regístrate ya!</a>
            <h2>💻 Bases del hackathon</h2>
            <p>
                Participar en nuestro hackathon y aplicar tus conocimientos a una buena causa es muy
                sencillo, ¡anímate!
            </p>
            <ol>
                <li>
                    Crea una cuenta en
                    <a href="https://huggingface.co/join">Hugging Face</a> si
                    todavía no tienes una y regístrate
                    <a
                        href="https://hackathon-pln-es.eventbrite.com/?aff=website"
                        target="_blank"
                    >aquí</a>.
                </li>
                <li>
                    Únete a nuestra comunidad de
                    <a
                        href="https://discord.com/invite/my8w7JUxZR"
                        target="_blank"
                    >Discord</a>
                    y haz click en "request to join this org" en la organización
                    <a
                        href="https://huggingface.co/hackathon-pln-es"
                        target="_blank"
                    >hackathon-pln-es</a> de Hugging Face.
                </li>
                <li>
                    Echa un vistazo a los diferentes canales de Discord, sobre todo a los de la
                    sección "HACKATHON", ya que iremos anunciando talleres y material con el que
                    preparar el hackathon y también resolveremos las dudas que te puedan surgir
                    durante el evento.
                </li>
                <li>
                    Reúne tu equipo (de 1 a 5 personas). Si todavía no tienes equipo puedes utilizar
                    el canal #encuentra-equipo para crear uno nuevo o unirte a uno existente.
                </li>
                <li>
                    Junto con tu equipo, entrena y sube al
                    <a
                        href="https://huggingface.co/models"
                        target="_blank"
                    >Hub</a> uno o varios modelos. Desde la comunidad queremos animar a todos los
                    equipos a entrenar modelos que sirvan para abordar alguno de los
                    <a
                        href="https://www.un.org/sustainabledevelopment/es/objetivos-de-desarrollo-sostenible/"
                        target="_blank"
                    >Objetivos de Desarrollo Sostenible de la ONU</a>".
                </li>
                <li>
                    Asegúrate de incluir una "Model Card" explicando, entre otras cosas, el
                    origen de los datos utilizados y el proceso de entrenamiento del modelo.
                </li>
                <li>
                    Crea una demo de el/los modelo/s utilizando la tecnología que prefieras
                    (e.g. FastAPI, Flask, Gradio, Streamlit).
                </li>
                <li>
                    Por último, rellena este
                    <a href="./wip" target="_blank">formulario</a> para
                    presentar el proyecto.
                </li>
            </ol>
            <p>
                Un jurado formado por especialistas en PLN (por anunciar) elegirá los tres equipos
                ganadores. Además, se concederá una mención de honor al mejor proyecto enfocado a un
                Objetivo de Desarrollo Sostenible y otra al modelo con más ❤️ en el Hub de Hugging Face.
            </p>
            <p>¡Buena suerte!</p>

            <h2>📖 Recursos</h2>
            <p>
                Desde el equipo de Somos NLP queremos animarte a participar independientemente de
                tus conocimientos actuales.
            </p>
            <ul>
                <li>
                    Hemos creando listas de
                    <b>datasets y modelos open-source</b>
                    que puedes utilizar para hacer fine-tuning como te explicamos en nuestros
                    <b>tutoriales</b>
                    <a href="recursos">(somosnlp.org/recursos)</a>.
                </li>
                <li>
                    También daremos un
                    <b>taller práctico</b> el primer día del hackathon en el cual
                    crearemos una base de datos, entrenaremos un modelo y desarrollaremos una demo
                    para que tengas un ejemplo de proyecto de referencia.
                </li>
                <li>
                    Además, durante las dos semanas que dura el hackathon estaremos a tu disposición
                    en
                    <b>Discord</b> para guiarte y ayudarte a desarrollar tu proyecto.
                </li>
            </ul>

            <h2>💡 Charlas y Talleres</h2>
            <p>
                Durante el hackathon tendrán lugar diversas charlas y talleres impartidas por
                profesionales del mundo del Procesamiento del Lenguaje Natural. Iremos anunciando
                los eventos uno a uno así que atención a
                <a
                    href="https://twitter.com/somosnlp_"
                    target="_blank"
                >Twitter</a> y
                <a href="https://www.linkedin.com/company/somosnlp" target="_blank">LinkedIn</a>🔥
            </p>
            <EventHackathonList />

            <h2>👏 Patrocinadores</h2>
            <p>
                Muchísimas gracias por vuestro tiempo y por apoyarnos para que nuestra iniciativa
                llegue más lejos. ¡Vamos a democratizar el PLN en español!
            </p>
            <h3>🥇 Platrocinadores de oro</h3>
            <div class="auto-rows-fr grid gap-x-16 place-items-center lg:grid-cols-3">
                <SponsorInfo
                    sponsor="Paperspace"
                    url="https://www.paperspace.com/"
                    logo="https://somosnlp.github.io/assets/images/logo_paperspace.svg"
                    logo_dark="https://somosnlp.github.io/assets/images/logo_paperspace_dark.svg"
                />
                <SponsorInfo
                    sponsor="Platzi"
                    url="https://platzi.com/"
                    logo="https://somosnlp.github.io/assets/images/logo_platzi.png"
                    logo_dark="https://somosnlp.github.io/assets/images/logo_platzi_dark.png"
                />
                <SponsorInfo
                    sponsor="Hugging Face"
                    url="https://huggingface.co/"
                    logo="https://somosnlp.github.io/assets/images/logo_HuggingFace.svg"
                    logo_dark="https://somosnlp.github.io/assets/images/logo_HuggingFace.svg"
                />
            </div>
            <h3>🥈 Patrocinadores de plata</h3>
            <div class="auto-rows-fr grid gap-x-16 place-items-center lg:grid-cols-3">
                <SponsorInfo
                    sponsor="BSC"
                    url="https://www.bsc.es/"
                    logo="https://somosnlp.github.io/assets/images/logo_BSC.png"
                    logo_dark="https://somosnlp.github.io/assets/images/logo_BSC_dark.png"
                />
                <SponsorInfo
                    sponsor="DiverTLes"
                    url="https://gplsi.dlsi.ua.es/pln/divertles"
                    logo="https://somosnlp.github.io/assets/images/logo_DiverTLes.png"
                    logo_dark="https://somosnlp.github.io/assets/images/logo_DiverTLes_dark.png"
                />
                <SponsorInfo
                    sponsor="IBiDat"
                    url="https://ibidat.es/"
                    logo="https://somosnlp.github.io/assets/images/logo_IBiDat.png"
                    logo_dark="https://somosnlp.github.io/assets/images/logo_IBiDat_dark.png"
                />
                <SponsorInfo
                    sponsor="Narrativa"
                    url="https://www.narrativa.com/"
                    logo="https://somosnlp.github.io/assets/images/logo_Narrativa.png"
                    logo_dark="https://somosnlp.github.io/assets/images/logo_Narrativa_dark.png"
                />
                <SponsorInfo
                    sponsor="Plan TL"
                    url="https://plantl.mineco.gob.es/"
                    logo="https://somosnlp.github.io/assets/images/logo_PlanTL.png"
                    logo_dark="https://somosnlp.github.io/assets/images/logo_PlanTL_dark.png"
                />
                <SponsorInfo
                    sponsor="PLNnet"
                    url="https://gplsi.dlsi.ua.es/pln/"
                    logo="https://somosnlp.github.io/assets/images/logo_PLNnet.svg"
                    logo_dark="https://somosnlp.github.io/assets/images/logo_PLNnet.svg"
                />
                <SponsorInfo
                    sponsor="Saturdays AI"
                    url="https://saturdays.ai/"
                    logo="https://somosnlp.github.io/assets/images/logo_SaturdaysAI.png"
                    logo_dark="https://somosnlp.github.io/assets/images/logo_SaturdaysAI.png"
                />
                <SponsorInfo
                    sponsor="Spain AI"
                    url="https://www.spain-ai.com/"
                    logo="https://somosnlp.github.io/assets/images/logo_SpainAI.png"
                    logo_dark="https://somosnlp.github.io/assets/images/logo_SpainAI_dark.png"
                />
                <SponsorInfo
                    sponsor="UNAM"
                    url="https://www.unam.mx/"
                    logo="https://somosnlp.github.io/assets/images/logo_UNAM.png"
                    logo_dark="https://somosnlp.github.io/assets/images/logo_UNAM_dark.png"
                />
                <SponsorInfo
                    sponsor="UNL"
                    url="https://www.unl.edu.ec/"
                    logo="https://somosnlp.github.io/assets/images/logo_UNL_square.png"
                    logo_dark="https://somosnlp.github.io/assets/images/logo_UNL_square.png"
                />
            </div>
        </article>
    </Container>
</template>
