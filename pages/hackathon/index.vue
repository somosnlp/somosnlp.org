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
        { name: 'twitter:image', content: 'https://somosnlp.github.io/assets/images/eventos/230320_hackathon_llms.jpg' },
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
                    Registrarme
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
                <img src="https://github.com/somosnlp/assets/raw/main/images/eventos/230320_hackathon_llms.jpg" width="650"
                    height="365" alt="Cartel del Hackathon 2023" />
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
            <p>Al unirte a este evento tendrás la oportunidad de:</p>
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
                    Ayudar a crear recursos abiertos y democratizar el PLN en español
                </li>
                <li>Consultar tus dudas sobre PLN con mentores y expertas</li>
                <li>
                    Recibir apoyo para presentar tu proyecto como paper a una conferencia o para desarrollar tu idea y
                    llevarla al mercado
                </li>
                <li>... y mucho más por anunciar</li>
            </ul>
            <a href="https://www.eventbrite.com/e/registro-hackathon-somos-nlp-2023-los-llms-hablan-espanol-565283938477?aff=w"
                target="_blank">
                ¡Regístrate ya!
            </a>

            <hr class="mx-auto mt-8 mb-12 prose" />

            <h2 id="por-que-participar">📝 Índice</h2>
            <div class="m-12">
                <ul>
                    <p>Todo lo que necesitas saber del hackathon</p>
                    <ul>
                        <li>
                            <a href="#bases-del-hackathon">Bases del Hackathon</a>
                        </li>
                        <li>
                            <a href="#recursos">Recursos</a>
                        </li>
                        <li>
                            <a href="#evaluacion-y-premios">Evaluación y Premios</a>
                        </li>
                    </ul>
                    <p>Mejora tus conocimientos de PLN</p>
                    <ul>
                        <li>
                            <a href="#charlas-y-talleres">Charlas y Talleres</a>
                        </li>
                    </ul>
                    <p>Agradecimientos</p>
                    <ul>
                        <li>
                            <a href="#equipo">Equipo</a>
                        </li>
                        <li>
                            <a href="#patrocinios">Patrocinios</a>
                        </li>
                    </ul>
                </ul>
            </div>

            <hr class="mx-auto my-12 prose" />

            <h2 id="charlas-y-talleres">💡 Charlas y Talleres</h2>
            <p>
                Durante el hackathon tendrán lugar diversas charlas y talleres
                impartidas por profesionales del mundo del Procesamiento del
                Lenguaje Natural. Estos eventos están abiertos a todas las
                personas, independientemente de si participan en el hackathon,
                <a href="https://www.eventbrite.com/e/registro-hackathon-somos-nlp-2023-los-llms-hablan-espanol-565283938477?aff=w"
                    target="_blank">¡apúntate!</a>
            </p>
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

            <ul>
                <li>
                    El objetivo del hackathon es crear recursos abiertos de PLN en español, a poder ser aprovechando el
                    potencial de los grandes modelos del lenguaje para desarrollar un proyecto enfocado a alguno de los
                    Objetivos de Desarrollo Sostenible.
                </li>
                <li>
                    Dataset:
                    <ul>
                        <li>
                            Te animamos a crear un dataset específicamente para tu proyecto aunque también puedes mejorar
                            alguno ya existente o utilizarlo directamente (ojo a las licencias).
                        </li>
                        <li>
                            En español o multilingüe.
                        </li>
                        <li>
                            Si te animas a etiquetar un dataset te recomendamos utilizar Argilla. El martes 21 haremos un
                            taller donde el CEO te enseñará a utilizar la herramienta y el jueves 23 organizaremos un AMA
                            con una
                            persona del equipo
                            que resolverá tus dudas. Además, el equipo estará atento a Discord para ayudarte.
                        </li>
                        <li>
                            Cumplimenta bien la Dataset Card, tendremos en cuenta a la hora de evaluar los proyectos si está
                            si está completa y si incluye temas como una evaluación de los sesgos del dataset.
                        </li>

                    </ul>
                </li>
                <li>
                    Modelo:
                    <ul>
                        <li>
                            Haz fine-tuning de un modelo ya existente (no pre-entrenes uno desde cero). En esta edición te
                            animamos a que ajuste un
                            gran
                            modelo del
                            lenguaje (LLM), como BERTIN-GPT-J o BLOOM. El lunes 20 Manu Romero, el mayor contribuidor del
                            Hub de Hugging Face, dará un taller en el que te
                            explicaremos
                            cómo
                            realizar esto.
                        </li>
                        <li>
                            En español o multilingüe.
                        </li>
                        <li>
                            Si quieres, puedes utilizar la herramienta experimental de
                            HF
                            fuego para entrenar tu modelo directamente desde Spaces.
                        </li>
                        <li>
                            Evalúa tu modelo y haz públicos
                            los resultados. Puedes utilizar la herramienta evaluate de HF o un script, ten en cuenta que
                            tendrás
                            que
                            liberarlo.
                        </li>
                        <li>
                            Cumplimenta bien la Model Card, a la hora de evaluar los proyectos daremos un punto extra si
                            está completa y se incluyen temas como la
                            evaluación de los sesgos del modelo y del impacto desde el punto de vista climático.
                        </li>
                    </ul>
                </li>
                <li>
                    Demo:
                    Por último, crea una demo de tu modelo en el hub de HF. <a
                        href="https://www.youtube.com/watch?v=Q0t1bNoa0tI&list=PLTA-KAy8nxaB-HA79tlOTRl496_XIlJta"
                        target="_blank">Aquí</a> tienes tutoriales para
                    crear demos utilizando gradio,
                    streamlit y flask.
                </li>
                <li>
                    IMPORTANTE: Todo el proyecto debe ser liberado en la organización
                    <a href="https://huggingface.co/organizations/hackathon-somos-nlp-2023/share/YPgLHyEfyVvfnHMYmPbisOqmWTOzQxSDYI"
                        target="_blank">hackathon-somos-nlp-2023</a>,
                    esto incluye el dataset, el modelo y la demo.
                </li>
                <li>
                    Los scripts de creación/limpieza del dataset y de entrenamiento/evaluación del modelo también deben ser
                    liberados. Puedes esperar al 31 de marzo para evitar problemas de plagio. Incluye un enlace en la
                    Dataset Card o Model Card a los notebooks o scripts utilizados en cada caso. Si los has creado
                    específicamente para el proyecto, súbelos al repo correspondiente.
                </li>
            </ul>

            <p>
                Participar en nuestro hackathon y aplicar tus conocimientos a una buena causa es muy sencillo, ¡anímate!
            </p>
            <ol>
                <li>
                    Únete a nuestra comunidad de
                    <a href="https://discord.com/invite/my8w7JUxZR" target="_blank">Discord</a> y
                    crea una cuenta en
                    <a href="https://huggingface.co/join" target="_blank">Hugging Face</a>.
                </li>
                <li>Regístrate en
                    <a href="https://www.eventbrite.com/e/registro-hackathon-somos-nlp-2023-los-llms-hablan-espanol-565283938477?aff=w"
                        target="_blank">Eventbrite</a>.
                </li>
                <li>
                    Únete a la organización
                    <a href="https://huggingface.co/organizations/hackathon-somos-nlp-2023/share/YPgLHyEfyVvfnHMYmPbisOqmWTOzQxSDYI"
                        target="_blank">hackathon-somos-nlp-2023</a>
                    del Hub de Hugging Face. Habrá que liberar en esta organización todos los datasets, modelos y demos.
                </li>
                <li>
                    Reúne tu equipo (de 1 a 5 personas). Si todavía no tienes
                    equipo puedes utilizar el canal #equipos-hackathon para
                    crear uno nuevo o unirte a uno existente (más info en el canal). Te animamos a desarrollar un
                    proyecto
                    enfocado a alguno de los Objetivos de Desarrollo Sostenible de la ONU.
                </li>
            </ol>
            <p>
                ¡Todo listo para poder empezar!
            </p>

            <h2 id="recursos">📖 Recursos</h2>
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
                                src="https://somosnlp.github.io/assets/images/eventos/230320_fine_tuning_llm.jpg" />
                        </a>
                        <a href="hackathon/etiquetado-de-datos-con-argilla" target="_blank">
                            <img alt="Etiquetado de datos con Argilla" width="650" height="365"
                                src="https://somosnlp.github.io/assets/images/eventos/230321_etiquetado_de_datos_con_argilla.jpg" />
                        </a>
                        <a href="/hackathon/evaluacion-de-sesgos" target="_blank">
                            <img alt="Evaluación de sesgos" width="650" height="365"
                                src="https://somosnlp.github.io/assets/images/eventos/230322_evaluacion_de_sesgos.jpg" />
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
                        <a href="hackathon/ama-con-natalia-elvira" target="_blank">
                            <img alt="AMA con Natalia Elvira" width="650" height="365"
                                src="https://somosnlp.github.io/assets/images/eventos/230323_ama_con_natalia_elvira.jpg" />
                        </a>
                        <a href="/hackathon/ama-con-omar-sanseviero" target="_blank">
                            <img alt="AMA con Omar Sanseviero" width="650" height="365"
                                src="https://somosnlp.github.io/assets/images/eventos/230327_ama_con_omar_sanseviero.jpg" />
                        </a>
                        <a href="/hackathon/ama-con-alejandro-vaca" target="_blank">
                            <img alt="AMA con Alejandro Vaca" width="650" height="365"
                                src="https://somosnlp.github.io/assets/images/eventos/230329_ama_con_alejandro_vaca.jpg" />
                        </a>
                    </div>
                </div>
                <li>
                    Además, durante el hackathon estaremos a tu
                    disposición en el canal <b>#pide-ayuda</b> de Discord para
                    guiarte y ayudarte a desarrollar tu proyecto.
                </li>
                <li>
                    Para ayudarte a definir tu proyecto, hemos propuesto algunas ideas en el primer mensaje del canal
                    #equipos-hackathon. Además, en nuestra sección de "Recursos"
                    <a href="recursos">(somosnlp.org/recursos)</a>
                    puedes encontrar listas de
                    <b>datasets y modelos open-source</b>.
                </li>
                <li>
                    Si quieres ver ejemplos de proyectos, puedes echarle un vistazo a la organización del Hub de HF de la
                    primera edición.
                    También te animamos a ver los talleres en los que
                    <a href="https://www.youtube.com/watch?v=fOQLPuXewzE&list=PLTA-KAy8nxaAbyaBTYK68TZKQLv9V8L8M">equipos
                        ganadores</a>
                    explican cómo implementaron sus proyectos.
                </li>
            </ul>

            <h2 id="evaluacion-y-premios">🏆 Evaluación y Premios</h2>
            <p>
                A la hora de evaluar los proyectos, dado que cada equipo
                utilizará un dataset diferente y entrenará su modelo para
                resolver una tarea diferente, además de tener en cuenta el
                valor de las métricas, los criterios de evaluación incluirán el
                impacto social del proyecto, la originalidad de la idea y la
                dificultad técnica.
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

            <h2 id="equipo">👏 Equipo</h2>
            <p>
                ¿Quieres ayudarnos a organizar este hackathon?
                Crea, diseña, escribe... apóyanos haciendo lo que mejor se te dé. Háblanos por Discord o mándanos un
                correo
                a
                <a href="mailto:info@somosnlp.org" target="_blank">info@somosnlp.org</a>,
                ¡estamos esperándote!
            </p>

            <h2 id="patrocinios">👏 Patrocinios</h2>
            <p>
                Muchísimas gracias por vuestro tiempo y por apoyarnos para que nuestra iniciativa llegue más lejos.
                ¡Vamos a democratizar el PLN en español!
            </p>
            <h3>🥇 Patrocinadores de oro</h3>
            <div class="auto-rows-fr grid gap-x-16 place-items-center lg:grid-cols-3">
                <SponsorInfo sponsor="Hugging Face" url="https://huggingface.co/"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/HuggingFace.svg"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/HuggingFace.svg" />

                <SponsorInfo sponsor="Nova" url="https://www.novatalent.com/"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/Nova.png"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/Nova_dark.png" />

                <SponsorInfo sponsor="Argilla" url="https://www.argilla.io/"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/Argilla.svg"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/Argilla.svg" />

                <SponsorInfo sponsor="Women Tech Global Conference" url="https://www.womentech.net/women-tech-conference"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/WomenTechNetwork.png"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/WomenTechNetwork.png" />

                <SponsorInfo sponsor="AgilMentor" url="https://agilmentor.com/programa/incubacion-tech/"
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

                <SponsorInfo sponsor="DataGénero" url="https://www.datagenero.org"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/DataGenero.png"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/DataGenero.png" />

                <SponsorInfo sponsor="AI The New Sexy" url="https://linktr.ee/aithenewsexy"
                    logo="https://somosnlp.github.io/assets/images/patrocinios/AiTheNewSexy.PNG"
                    logo_dark="https://somosnlp.github.io/assets/images/patrocinios/AiTheNewSexy.PNG" />
            </div>
            <p>

                Seguiremos anunciando más patrocinios 🔥
            </p>
            <p>
                ¿Quieres patrocinar este hackathon y ayudarnos a democratizar el PLN en español? Mándanos un correo a
                <a href="mailto:info@somosnlp.org" target="_blank">info@somosnlp.org</a>,
                ¡será un placer contar con tu apoyo!
            </p>

        </article>
    </Container>
</template>
