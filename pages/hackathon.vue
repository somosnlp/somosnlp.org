<script setup lang="ts">
import { isDark } from "~/logic"
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
                Contruye al lado de mentores, expertas y hackers la siguiente generación de modelos
                de Procesamiento del Lenguaje Natural
            </p>
        </header>
        <hr class="mx-auto mt-8 mb-12 prose" />

        <article class="m-auto prose">
            ¡Únete al mayor hackathon de Procesamiento del Lenguaje Natural en español!
            <div class="flex justify-center">
                <img
                    src="https://github.com/somosnlp/assets/raw/main/images/hackathon_pln_es_3.png"
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

            <h2>Bases del hackathon</h2>
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
                    >aquí</a> 🚀.
                </li>
                <li>
                    Únete a nuestra comunidad de
                    <a
                        href="https://discord.gg/u2wWMHsc"
                        target="_blank"
                    >Discord</a>
                    y acepta la invitación que te mandemos para unirte a la organización
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
                    origen de los datos utilizados y el proceso de entrenamiento del modelo. Antes
                    del comienzo del hackathon publicaremos un ejemplo de referencia.
                </li>
                <li>
                    Crea una demo de el/los modelo/s utilizando la tecnología que prefieras
                    (e.g. FastAPI, Flask, Gradio, Streamlit).
                </li>
                <li>
                    Por último, rellena este
                    <a href="./hackathon_wip" target="_blank">formulario</a> para
                    presentar el proyecto.
                </li>
            </ol>
            <p>
                Un jurado formado por especialistas en PLN (por anunciar) elegirá los tres equipos
                ganadores. Además, se concederá una mención de honor al mejor proyecto enfocado a un
                Objetivo de Desarrollo Sostenible y otra al modelo con más ❤️ en el Hub de Hugging Face.
            </p>
            <p>¡Buena suerte!</p>

            <h2>Charlas y Talleres</h2>
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
            <HackathonList />

            <h2>Patrocinadores</h2>
            <p>
                Muchísimas gracias por vuestro tiempo y por apoyarnos para que nuestra iniciativa
                llegue más lejos. ¡Vamos a democratizar el PLN en español!
            </p>
            <h3>🥇 Platrocinadores de oro</h3>
            <div class="auto-rows-fr grid gap-x-16 place-items-center lg:grid-cols-3">
                <a href="https://www.paperspace.com/" target="_blank">
                    <img
                        v-if="!isDark"
                        class="w-screen"
                        src="https://somosnlp.github.io/assets/images/logo_paperspace_black.svg"
                        alt="Paperspace"
                    />
                    <img
                        v-if="isDark"
                        class="w-screen"
                        src="https://somosnlp.github.io/assets/images/logo_paperspace_white.svg"
                        alt="Paperspace"
                    />
                </a>
                <a href="https://huggingface.co/" target="_blank">
                    <img
                        class="w-screen"
                        src="https://somosnlp.github.io/assets/images/logo_HuggingFace.svg"
                        alt="Hugging Face"
                    />
                </a>
                <a href="https://www.spain-ai.com/" target="_blank">
                    <img
                        v-if="!isDark"
                        class="w-screen"
                        src="https://somosnlp.github.io/assets/images/logo_SpainAI_black.png"
                        alt="Spain AI"
                    />
                    <img
                        v-if="isDark"
                        class="w-screen"
                        src="https://somosnlp.github.io/assets/images/logo_SpainAI_white.png"
                        alt="Spain AI"
                    />
                </a>
            </div>
            <h3>🥈 Patrocinadores de plata</h3>
            <div class="auto-rows-fr grid gap-x-16 place-items-center lg:grid-cols-3">
                <a href="https://ibidat.es/" target="_blank">
                    <img
                        v-if="!isDark"
                        class="w-screen"
                        src="https://somosnlp.github.io/assets/images/logo_IBiDat.png"
                        alt="IBiDat"
                    />
                    <img
                        v-if="isDark"
                        class="w-screen"
                        src="https://somosnlp.github.io/assets/images/logo_IBiDat_neg.png"
                        alt="IBiDat"
                    />
                </a>
                <a href="https://www.narrativa.com/" target="_blank">
                    <img
                        v-if="!isDark"
                        class="w-screen"
                        src="https://somosnlp.github.io/assets/images/logo_Narrativa.png"
                        alt="UNL"
                    />
                    <img
                        v-if="isDark"
                        class="w-screen"
                        src="https://somosnlp.github.io/assets/images/logo_Narrativa_dark.png"
                        alt="UNL"
                    />
                </a>
                <a href="https://gplsi.dlsi.ua.es/pln/" target="_blank">
                    <img
                        class="w-screen"
                        src="https://somosnlp.github.io/assets/images/logo_PLNnet.svg"
                        alt="PLN.net"
                    />
                </a>
                <a href="https://saturdays.ai/" target="_blank">
                    <img
                        class="w-screen"
                        src="https://somosnlp.github.io/assets/images/logo_SaturdaysAI.png"
                        alt="Saturdays AI"
                    />
                </a>
                <a href="https://www.unam.mx/" target="_blank">
                    <img
                        v-if="!isDark"
                        class="w-screen"
                        src="https://somosnlp.github.io/assets/images/logo_UNAM_dark.png"
                        alt="UNAM"
                    />
                    <img
                        v-if="isDark"
                        class="w-screen"
                        src="https://somosnlp.github.io/assets/images/logo_UNAM_light.png"
                        alt="UNAM"
                    />
                </a>
                <a href="https://www.unl.edu.ec/" target="_blank">
                    <img
                        class="w-screen"
                        src="https://somosnlp.github.io/assets/images/logo_UNL_square.png"
                        alt="UNL"
                    />
                </a>
            </div>
        </article>
    </Container>
</template>