<script setup lang="ts" >
import { useHead } from '@vueuse/head'

useHead({
    title: 'Hackathon Somos NLP 2023: Los LLMs hablan Español',
    meta: [
        { name: 'twitter:card', content: 'summary_large_image' },
        { name: 'twitter:site', content: '@somosnlp_' },
        { name: 'twitter:creator', content: '@somosnlp_' },
        { name: 'twitter:title', content: 'Hackathon Somos NLP 2023: Los LLMs hablan Español' },
        { name: 'twitter:description', content: '¡Únete a la segunda edición del mayor hackathon open-source de Procesamiento del Lenguaje Natural en español!' },
        { name: 'twitter:image', content: 'https://somosnlp.github.io/assets/images/eventos/230320_hackathon_llms_fecha_ext_anuncio.jpg' },
        { name: 'twitter:image:alt', content: 'Cartel del Hackathon de Somos NLP' }
    ]
})

</script>

<template>
    <Container class="my-12">
        <header class="m-auto text-center prose">
            <h1>Hackathon Somos NLP 2023: Los LLMs hablan Español</h1>
            <p class="text-lg">
                Construye al lado de profesionales, expertas y mentores la siguiente generación de modelos de PLN en tu
                idioma
            </p>

            <div class="mt-10 grid gap-4 lg:grid-cols-2">
                <a href="https://hackathon_somos_nlp_2023.eventbrite.com/?aff=w" target="_blank" class="button-accent">
                    <carbon:user-multiple />
                    Aún puedes registrarte
                </a>
                <div class="button-gray max-w-70 border-2 border-accent-400 rounded">
                    <IconButtonLink
                        :url='`https://twitter.com/intent/tweet?text=Voy a participar en el hackathon @SomosNLP_ 2023 "Los LLMs hablan Español" ¿te apuntas? \n\n https://twitter.com/SomosNLP_/status/1635311564051070982`'>
                        <carbon:logo-twitter class="inline align-middle mr-2 text-lg" />
                        <span class="font-medium text-sm">#HackathonSomosNLP</span>
                    </IconButtonLink>
                </div>
            </div>
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
                <img src="https://github.com/somosnlp/assets/raw/main/images/eventos/230320_hackathon_llms_fecha_ext_anuncio.jpg"
                    width="650" height="365" alt="Cartel del Hackathon 2023" />
            </div>

            <p>
                La democratización del PLN en español es el objetivo principal
                de Somos NLP y creemos que una de las mejores maneras de avanzar
                hacia este objetivo es creando más recursos abiertos de PLN en
                nuestro idioma.
            </p>
            <p>
                Con este hackathon te animamos a unirte a nuestro esfuerzo y
                <b>
                    crear datasets y modelos que apliquen el potencial de los grandes modelos del lenguaje (LLMs) a una
                    buena causa.
                </b>
            </p>
            <p>
                Los equipos que desarrollen un proyecto enfocado a uno de los <a
                    href="https://www.un.org/sustainabledevelopment/es/objetivos-de-desarrollo-sostenible/"
                    target="_blank">Objetivos de Desarrollo Sostenible </a>
                tendrán un punto extra 💛
            </p>

            <hr class="mx-auto my-12 prose" />

            <h2 id="por-que-participar">🚀 Por qué participar</h2>
            <p>Al unirte a este evento, además de ayudarnos a crear recursos abiertos y democratizar el PLN en tu idioma,
                tendrás la oportunidad de:</p>
            <ul>
                <li>
                    Asistir a charlas y talleres impartidas por profesionales del mundo del PLN, independientemente de si
                    participas en el hackathon
                </li>
                <li>
                    Comprender cómo funcionan los grandes modelos del lenguaje (LLMs) y aprender a aprovechar su potencial
                </li>
                <li>
                    Unirte a la mayor comunidad de hispanohablantes que estudian, trabajan e investigan en PLN
                </li>
                <li>
                    Consultar tus dudas sobre PLN con mentores y expertas en AMAs (del inglés, Ask Me Anything)
                </li>
                <li>
                    Recibir apoyo para presentar tu proyecto como paper a una conferencia o para desarrollar tu idea y
                    llevarla al mercado
                </li>
            </ul>
            <a href="https://www.eventbrite.com/e/registro-hackathon-somos-nlp-2023-los-llms-hablan-espanol-565283938477?aff=w"
                target="_blank">
                ¡Regístrate ya!
            </a>

            <hr class="mx-auto mt-8 mb-12 prose" />

            <h2 id="por-que-participar">📝 Índice</h2>
            <div class="m-12">
                <ul>
                    <li>
                        <a href="#bases-del-hackathon">Bases del Hackathon</a>
                    </li>
                    <li>
                        <a href="#talleres-y-amas">Talleres y AMAs</a>
                    </li>
                    <li>
                        <a href="#evaluacion-y-premios">Evaluación y Premios</a>
                    </li>
                    <li>
                        <a href="#keynotes">Keynotes de especialistas</a>
                    </li>
                    <li>
                        <a href="#patrocinios">Patrocinios</a>
                    </li>
                </ul>
            </div>

            <hr class="mx-auto my-12 prose" />

            <h2 id="keynotes">💡 Keynotes de especialistas</h2>
            <p>
                Durante dos días del hackathon (martes 28 de marzo y 4 de abril), tendrán lugar diversas keynotes impartidas
                por profesionales del mundo del Procesamiento del
                Lenguaje Natural. Estos eventos están abiertos a todas las
                personas, independientemente de si participan en el hackathon,
                <a href="https://www.eventbrite.com/e/registro-hackathon-somos-nlp-2023-los-llms-hablan-espanol-565283938477?aff=w"
                    target="_blank">¡apúntate!</a>
            </p>
            <ul>
                Contaremos con grandes especialistas como:
                <li>
                    Flor PLaza, Postdoc @MilaNLP Uni Bocconi
                </li>
                <li>
                    Alejandro Vaca, Data Scientist @IIC y ganador de la primera edición del hackathon
                </li>
                <li>
                    Carlos Alarcón, Director de la escuela de datos & IA @Platzi
                </li>
                <li>
                    Frida Ruh, Fundadora @AiTheNewSexy y Value Based Bidding Specialist for SPLA @Google
                </li>
                <li>
                    Salvador Lima, Lingüista Computacional @BSC & Biomedical TeMU
                </li>
                <li>
                    Javier de la Rosa, NLP Research Scientist @Nasjonalbibl AI-Lab
                </li>
            </ul>
            <p>
                Para estar al día de los eventos:
            <ul>
                <li>
                    Síguenos en
                    <a href="https://twitter.com/somosnlp_" target="_blank">Twitter</a> y
                    <a href="https://www.linkedin.com/company/somosnlp" target="_blank">LinkedIn</a>
                </li>
                <li>
                    Suscríbete a nuestro canal de
                    <a href="https://www.youtube.com/c/somosnlp?sub_confirmation=1" target="_blank">YouTube</a>
                </li>
                <li>Únete al
                    <a href="https://www.eventbrite.com/x/565283938477/" target="_blank">calendario de Google</a>
                    (primero regístrate en Eventbrite)
                </li>
            </ul>
            </p>

            <hr class="mx-auto my-12 prose" />

            <h2 id="bases-del-hackathon">💻 Bases del Hackathon</h2>
            <a href="https://somosnlp.org/hackathon/bases-del-hackathon" target="_blank">
                Todo lo que necesitas saber para desarrollar un
                buen proyecto para el hackathon está aquí.
            </a>

            <h2 id="recursos">📖 Talleres y AMAs</h2>
            <p>
                Desde el equipo de Somos NLP queremos animarte a participar
                independientemente de tus conocimientos actuales.
            </p>
            <ul>
                <li>
                    Durante los primeros días del hackathon daremos una serie de <b>talleres prácticos</b> mostrándote entre
                    otros cómo
                    hacer fine-tuning de un LLM y cómo etiquetar tu base de datos para que tengas un ejemplo de referencia.
                </li>
                <div class="mx-auto my-8 text-center">
                    <div class="grid grid-cols-2 gap-8 my-1">
                        <a href="/hackathon/fine-tuning-llms" target="_blank">
                            <img alt="Fine-tuning LLMs" width="650" height="365"
                                src="https://somosnlp.github.io/assets/images/eventos/230320_fine_tuning_llms.jpg" />
                        </a>
                        <a href="hackathon/etiquetado-de-datos-con-argilla" target="_blank">
                            <img alt="Etiquetado de datos con Argilla" width="650" height="365"
                                src="https://somosnlp.github.io/assets/images/eventos/230321_etiquetado_de_datos_con_argilla.jpg" />
                        </a>
                        <a href="/hackathon/evaluacion-de-sesgos" target="_blank">
                            <img alt="Evaluación de sesgos" width="650" height="365"
                                src="https://somosnlp.github.io/assets/images/eventos/230322_evaluacion_de_sesgos.jpg" />
                        </a>
                        <a href="/hackathon/deteccion-del-lenguaje-ofensivo" target="_blank">
                            <img alt="Detección del lenguaje ofensivo" width="650" height="365"
                                src="https://somosnlp.github.io/assets/images/eventos/230404_deteccion_del_lenguaje_ofensivo.jpg" />
                        </a>
                    </div>
                </div>
                <li>
                    Organizaremos
                    <b>AMAs</b> (del inglés, Ask Me Anything) con expertas y
                    mentores para que puedan solucionar tus dudas.
                </li>
                <div class="mx-auto my-8 text-center">
                    <div class="grid grid-cols-2 gap-8 my-1">
                        <a href="/hackathon/ama-con-omar-sanseviero" target="_blank">
                            <img alt="AMA con Omar Sanseviero" width="650" height="365"
                                src="https://somosnlp.github.io/assets/images/eventos/230322_ama_con_omar_sanseviero.jpg" />
                        </a>

                        <a href="hackathon/ama-con-natalia-elvira" target="_blank">
                            <img alt="AMA con Natalia Elvira" width="650" height="365"
                                src="https://somosnlp.github.io/assets/images/eventos/230323_ama_con_natalia_elvira.jpg" />
                        </a>

                        <a href="/hackathon/ama-con-alejandro-vaca" target="_blank">
                            <img alt="AMA con Alejandro Vaca" width="650" height="365"
                                src="https://somosnlp.github.io/assets/images/eventos/230327_ama_con_alejandro_vaca.jpg" />
                        </a>
                    </div>
                </div>
            </ul>

            <h2 id="evaluacion-y-premios">🏆 Evaluación y Premios</h2>
            <p>
                A la hora de evaluar los proyectos, dado que cada equipo
                utilizará un dataset diferente y entrenará su modelo para
                resolver una tarea diferente, además de tener en cuenta el
                valor de las métricas, los criterios de evaluación incluirán el
                impacto social del proyecto, la originalidad de la idea y la
                dificultad técnica.
                <a href="https://somosnlp.org/hackathon/bases-del-hackathon" target="_blank">Más detalles aquí.</a>
            </p>
            <ul>
                Además de los tres proyectos ganadores elegidos por el jurado, habrá varias menciones de honor:
                <li>
                    🤗 Proyecto con más likes en el Hub de Hugging Face
                </li>
                <li>
                    💛 Proyecto con mayor impacto social
                </li>
                <li>
                    ✍️ Mejor dataset etiquetado: patrocinado por Argilla
                </li>
                <li>
                    💸 Proyecto con más opciones de llegar al mercado: patrocinado por AgilMentor
                </li>
            </ul>
            <p>Los premios incluirán:</p>
            <ul>
                <li>GPU grants durante el evento para que tengáis NVIDIA T4's en vuestros Spaces</li>
                <li>Swag de Hugging Face exclusivo para todas las personas que entreguen un proyecto completo</li>
                <li>La posibilidad de entrar en la red global de talento Nova</li>
                <li>Tickets para asistir a la WomenTech Network Global Conference 2023</li>
                <li>Descuentos para participar en un programa de incubación de ideas y crear un MVP a partir de tu proyecto
                </li>
                <li>Certificado de participación o de equipo ganador del "Hackathon Somos NLP 2023: Los LLMs hablan
                    Español"
                    (verificado en nuestra web)</li>
                <li>Rol honorífico en el servidor de Discord, e.g.: "🏆Hackathon23"</li>
                <li>... y mucho más por anunciar</li>
            </ul>
            <a href="blog/anuncio-patrocinios" target="_blank">
                ¡Más detalles sobre los patrocinios de oro aquí!
            </a>
            <p>
                Estamos hablando con las empresas patrocinadoras,
                mantendremos esta sección actualizada 😉
            </p>

            <hr class="mx-auto my-12 prose" />

            <h2 id="patrocinios">👏 Patrocinios</h2>
            <p>
                Muchísimas gracias por vuestro tiempo y por apoyarnos para que nuestra iniciativa llegue más lejos.
                ¡Vamos a democratizar el PLN en español!
            </p>
            <h3>🥇 Patrocinadores de oro</h3>
            <div class="auto-rows-fr grid gap-x-16 place-items-center lg:grid-cols-3">
                <SponsorInfo sponsor="Hugging Face" url="http://somosnlp.org/blog/anuncio-patrocinios"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/HuggingFace.svg"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/HuggingFace.svg" />

                <SponsorInfo sponsor="Nova" url="http://somosnlp.org/blog/anuncio-patrocinios"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/Nova.png"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/Nova_dark.png" />

                <SponsorInfo sponsor="Argilla" url="http://somosnlp.org/blog/anuncio-patrocinios"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/Argilla.svg"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/Argilla.svg" />

                <SponsorInfo sponsor="Women Tech Global Conference" url="http://somosnlp.org/blog/anuncio-patrocinios"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/WomenTechNetwork.png"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/WomenTechNetwork.png" />

                <SponsorInfo sponsor="AgilMentor" url="http://somosnlp.org/blog/anuncio-patrocinios"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/AgilMentor.png"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/AgilMentor.png" />
            </div>
            <h3>🥈 Patrocinadores de plata</h3>
            <div class="auto-rows-fr grid gap-x-16 place-items-center lg:grid-cols-3">
                <SponsorInfo sponsor="Spain AI" url="https://www.spain-ai.com/"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/SpainAI.png"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/SpainAI_dark.png" />


                <SponsorInfo sponsor="Narrativa" url="https://www.narrativa.com/"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/Narrativa.png"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/Narrativa_dark.png" />

                <SponsorInfo sponsor="DataGénero" url="https://www.datagenero.org"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/DataGenero.png"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/DataGenero.png" />

                <SponsorInfo sponsor="Instituto de Ingeniería del Conocimiento" url="https://www.iic.uam.es"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/iic.bmp"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/iic_dark.bmp" />

                <SponsorInfo sponsor="AI The New Sexy" url="https://linktr.ee/aithenewsexy"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/AiTheNewSexy.PNG"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/AiTheNewSexy.PNG" />
            </div>
            <h3>🥉 Patrocinadores de bronce</h3>
            <div class="auto-rows-fr grid gap-x-16 place-items-center lg:grid-cols-3">
                <SponsorInfo sponsor="Saturdays AI" url="https://saturdays.ai/"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/SaturdaysAI.png"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/SaturdaysAI.png" />

                <SponsorInfo sponsor="DiverTLes" url="https://gplsi.dlsi.ua.es/pln/divertles"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/DiverTLes.png"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/DiverTLes_dark.png" />

                <SponsorInfo sponsor="Mujeres Tech" url="https://www.mujerestech.com/"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/MujeresTech.png"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/MujeresTech.png" />

                <SponsorInfo sponsor="IBiDat" url="https://ibidat.es/"
                    logo="https://somosnlp.github.io/assets/images/logo_IBiDat.png"
                    logo_dark="https://somosnlp.github.io/assets/images/logo_IBiDat_dark.png" />

                <SponsorInfo sponsor="NLP Spain" url="https://nlpspain.blogspot.com/"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/NLPSpain.jpg"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/NLPSpain.jpg" />

                <SponsorInfo sponsor="Capítulo Estudiantil AAAIMX" url="https://www.aaaimx.org/"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/AAAIMX.png"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/AAAIMX_dark.png" />

                <SponsorInfo sponsor="Big Onion" url="https://datakondo.io/"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/BigOnion.jpg"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/BigOnion.jpg" />

                <SponsorInfo sponsor="NLP Webinar MX" url="http://www.nlpwebinarmx.org/"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/NLPmx.png"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/NLPmx.png" />

                <SponsorInfo sponsor="MCD UNISON" url="https://mcd.unison.mx"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/MCDUnisonMX.png"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/MCDUnisonMX.png" />

                <SponsorInfo sponsor="Universidad Nacional de Loja" url="https://unl.edu.ec"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/UNL.png"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/UNL_dark.png" />

                <SponsorInfo sponsor="Grupo de Ingeniería Lingüística de la UNAM"
                    url="https://www.facebook.com/ingenieriaLinguistica"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/GIL_UNAM.jpeg"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/GIL_UNAM.jpeg" />
            </div>
        </article>
    </Container>
</template>
