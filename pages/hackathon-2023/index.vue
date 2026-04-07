<script setup lang="ts" >
import { useHead } from '@unhead/vue'
import { localePath } from '~/composables/useLanguage'

useHead({
    title: 'Hackathon SomosNLP 2023: Los LLMs hablan Español',
    meta: [
        { name: 'twitter:card', content: 'summary_large_image' },
        { name: 'twitter:site', content: '@somosnlp_' },
        { name: 'twitter:creator', content: '@somosnlp_' },
        { name: 'twitter:title', content: 'Hackathon SomosNLP 2023: Los LLMs hablan Español' },
        { name: 'twitter:description', content: '¡Únete a la segunda edición del mayor hackathon open-source de Procesamiento del Lenguaje Natural en español!' },
        { name: 'twitter:image', content: '/images/eventos/230320_hackathon_llms_fecha_extendida.jpg' },
        { name: 'twitter:image:alt', content: 'Cartel del Hackathon de SomosNLP' }
    ]
})

</script>

<template>
    <Container class="my-12">
        <header class="m-auto text-center prose">
            <h1>Hackathon SomosNLP 2023: Los LLMs hablan Español</h1>
            <p class="text-lg">
                Construye al lado de profesionales, expertas y mentores la siguiente generación de modelos de PLN en tu
                idioma
            </p>

            <div class="mt-10 grid gap-4 lg:grid-cols-2">
                <div class="button-gray max-w-70 border-2 border-accent-400 rounded">
                    <IconButtonLink
                        :url='`https://twitter.com/intent/tweet?text=Proyectos ganadores del %23HackathonSomosNLP @SomosNLP_ \n\n https://twitter.com/SomosNLP_/status/1648752306978971666`'>
                        <carbon:logo-twitter class="inline align-middle mr-2 text-lg" />
                        <span class="font-medium text-sm">Proyectos Ganadores #HackathonSomosNLP</span>
                    </IconButtonLink>
                </div>
                <div class="button-gray max-w-70 border-2 border-accent-400 rounded">
                    <IconButtonLink
                        :url='`https://www.linkedin.com/posts/somosnlp_hackathonsomosnlp-pln-opensource-activity-7054865464488861696-gS2E/`'>
                        <carbon:logo-linkedin class="inline align-middle mr-2 text-lg" />
                        <span class="font-medium text-sm">Proyectos Ganadores #HackathonSomosNLP</span>
                    </IconButtonLink>
                </div>
            </div>
        </header>
        <hr class="mx-auto mt-8 mb-12 prose" />

        <div class="m-auto text-center prose">
            <p>
                La segunda edición de nuestro hackathon ya ha finalizado, te animamos a echar un vistazo
                a los
                <a href="https://hf.co/hackathon-somos-nlp-2023" target="_blank">proyectos</a>
                de los equipos participantes y visualizar las grabaciones de las
                <a href="https://www.youtube.com/playlist?list=PLTA-KAy8nxaCDc0IJpLac-3csiAepV546" target="_blank">
                    charlas y talleres
                </a>impartidas por especialistas en el campo del PLN.
            </p>

            <p>
                <a :href="localePath('/eventos')">
                    ¡Únete a nuestros próximos eventos!
                </a>
            </p>
        </div>
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
                <a href="" target="_blank">
                    <img src="/images/eventos/230320_hackathon_llms_fecha_extendida.jpg"
                        width="650" height="365" alt="Cartel del Hackathon 2023" />
                </a>
            </div>

            <p>
                La democratización del PLN en español es el objetivo principal
                de SomosNLP y creemos que una de las mejores maneras de avanzar
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
                    Consultar tus dudas sobre PLN con mentores y mentoras en sesiones "Ask My Anything"
                </li>
                <li>
                    Recibir apoyo para presentar tu proyecto como paper a una conferencia o para desarrollar tu idea y
                    llevarla al mercado
                </li>
            </ul>
            ¡Regístrate ya!

            <hr class="mx-auto mt-8 mb-12 prose" />

            <h2 id="por-que-participar">📝 Índice</h2>
            <div class="m-12">
                <ul>
                    <li>
                        <a :href="localePath('/hackathon-2023/bases-del-hackathon')">Bases del Hackathon</a>
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
                personas, independientemente de si participan en el hackathon.
                <a href="https://www.youtube.com/playlist?list=PLTA-KAy8nxaCDc0IJpLac-3csiAepV546" target="_blank">¡Ya están
                    las grabaciones disponibles!</a>
            </p>
            <ul>
                Martes 28 de marzo: Día de Keynotes
                <li>
                    "Tecnologías clave de ChatGPT: Reinforcement Learning from Human Feedback", con Alejandro Vaca, Data
                    Scientist @IIC y ganador de la primera edición del hackathon
                </li>
                <li>
                    "Detección y mitigación de sesgos en modelos de lenguaje", con María Grandury, ML Research Engineer
                    @neurocat y Fundadora @SomosNLP
                </li>
                <li>
                    "Impacto de los LLM en el mundo actual", con Carlos Alarcón, Director de la escuela de datos & IA
                    @Platzi
                </li>
                <li>
                    "Inteligencia Artificial y los feminismos en América Latina: la experiencia del proyecto AymurAI", con
                    Ivana Feldfeber, Directora
                    Ejecutiva @DataGénero
                </li>
                Miércoles 29 de marzo: Taller de Emprendimiento
                <li>
                    "De la idea a la startup", con Lucas Fernández, Ingeniero Industrial y Fundador @AgilMentor
                </li>
                Lunes 3 de abril: BERTIN Monday
                <li>
                    "Estrategias de simplificación para modelos grandes de lenguaje", con Paulo Villegas, Experto
                    tecnológico en Telefónica Chief Digital Office
                </li>
                <li>
                    "Proyecto BERTIN: Entrenando modelos de lenguaje en Español de manera abierta", con Javier de la Rosa,
                    NLP Research Scientist @Nasjonalbibl AI-Lab y Álvaro Pérez, Investigador @linhd
                </li>
                Martes 4 de abril: Día de Keynotes
                <li>
                    "Detección del lenguaje ofensivo en la era digital: retos y avance", con Flor PLaza, Postdoc @MilaNLP
                    Uni Bocconi
                </li>
                <li>
                    "Evaluación con desacuerdo en tareas subjetivas: caso del sexismo en redes sociales", con Julio Gonzalo,
                    Director del grupo de investigación nlp.uned.es
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
                    <a href="https://calendar.google.com/calendar/u/0?cid=ZWM3MGZhODIzNmYyNzBlMTYwYzFiMjdhNDgzZWMyMjA1ZjQwYzUyN2E5N2MwZTJhZmY0OTcwZDZmZjBkYzQyMEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t"
                        target="_blank">calendario de Google</a>
                </li>
            </ul>
            </p>

            <hr class="mx-auto my-12 prose" />

            <h2 id="bases-del-hackathon">💻 Bases del Hackathon</h2>
            <a :href="localePath('/hackathon-2023/bases-del-hackathon')" target="_blank">
                Todo lo que necesitas saber para desarrollar un
                buen proyecto para el hackathon está aquí.
            </a>

            <h2 id="recursos">📖 Talleres y AMAs</h2>
            <p>
                Desde el equipo de SomosNLP queremos animarte a participar
                independientemente de tus conocimientos actuales.
            </p>
            <ul>
                <li>
                    Durante los primeros días del hackathon daremos una serie de <b>talleres prácticos</b> mostrándote cómo
                    hacer fine-tuning de un LLM y cómo etiquetar tu base de datos para que tengas un ejemplo de referencia.
                </li>
                <div class="mx-auto my-8 text-center">
                    <div class="grid grid-cols-2 gap-8 my-1">
                        <a :href="localePath('/hackathon-2023/fine-tuning-llms')" target="_blank">
                            <img alt="Fine-tuning LLMs" width="650" height="365"
                                src="/images/eventos/230320_fine_tuning_llms.jpg" />
                        </a>

                        <a href="hackathon-2023/etiquetado-de-datos-con-argilla" target="_blank">
                            <img alt="Etiquetado de datos con Argilla" width="650" height="365"
                                src="/images/eventos/230321_etiquetado_de_datos_con_argilla.jpg" />
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
                        <a :href="localePath('/hackathon-2023/ama-con-omar-sanseviero')" target="_blank">
                            <img alt="AMA con Omar Sanseviero" width="650" height="365"
                                src="/images/eventos/230322_ama_con_omar_sanseviero.jpg" />
                        </a>

                        <a href="hackathon-2023/ama-con-natalia-elvira" target="_blank">
                            <img alt="AMA con Natalia Elvira" width="650" height="365"
                                src="/images/eventos/230323_ama_con_natalia_elvira.jpg" />
                        </a>

                        <a href="" target="_blank">
                            <img alt="AMA con Manuel Romero" width="650" height="365"
                                src="/images/eventos/230327_ama_con_manuel_romero.jpg" />
                        </a>

                        <a :href="localePath('/hackathon-2023/ama-con-alejandro-vaca')" target="_blank">
                            <img alt="AMA con Alejandro Vaca" width="650" height="365"
                                src="/images/eventos/230330_ama_con_alejandro_vaca.jpg" />
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
                <a :href="localePath('/hackathon-2023/bases-del-hackathon')" target="_blank">Más detalles aquí.</a>
            </p>
            <ul>
                TODAS las personas que entreguen un proyecto completo conseguiréis:
                <li>
                    ⚙️ GPU VMs para entrenar vuestros modelos
                </li>
                <li>
                    ⚙️ GPU grants durante el evento para que tengáis NVIDIA T4s en vuestros Spaces
                </li>
                <li>
                    🤗 Swag de Hugging Face exclusivo del evento
                </li>
                <li>
                    💜 Descuento de 20% en tickets para asistir a la WomenTech Network Global Conference 2023 y la opción de
                    ganar 3 tickets completamente gratis
                </li>
                <li>
                    🚀 Descuento de 20% para participar en el programa de incubación de cuatro meses y medio de AgilMentor y
                    crear un MVP a partir de vuestro proyecto
                </li>
                <li>
                    📜 Certificado de participación o de equipo ganador del "Hackathon SomosNLP 2023: Los LLMs hablan
                    Español"
                    (verificado en nuestra web)
                </li>
            </ul>
            <ul>
                Además de los tres proyectos ganadores elegidos por el jurado, habrá varias menciones de honor:
                <li>
                    🤗 Proyecto con más likes en el Hub de Hugging Face (<a
                        href="https://huggingface.co/spaces/hackathon-somos-nlp-2023/leaderboard"
                        target="_blank">leaderboard</a>)
                </li>
                <li>
                    💛 Proyecto con mayor impacto social: Beca del 50% de descuento para participar en el programa de
                    incubación de cuatro meses y medio de AgilMentor y crear un MVP a partir de tu proyecto
                </li>
                <li>
                    ✍️ Mejor dataset etiquetado: 200€ de crédito en el Hub de Hugging Face patrocinado por Argilla
                </li>
                <li>
                    🚀 Proyecto con más opciones de llegar al mercado: Beca del 75% de descuento para participar en el
                    programa de incubación de cuatro meses y medio de AgilMentor y crear
                    un MVP a partir de tu proyecto
                </li>
            </ul>
            <p>Premios para el tercer puesto:</p>
            <ul>
                <li>
                    ✨ Nominaciones para entrar en la red global de talento Nova y la oportunidad de participar en su curso
                    de Personal Branding (persona elegida por el equipo de Nova)
                </li>
                <li>
                    🚀 Beca del 50% de descuento para participar en el programa de incubación de cuatro meses y medio de
                    AgilMentor y crear
                    un MVP a partir de tu proyecto
                </li>
                <li>
                    👀 Certificado, reconocimiento en la página web y redes sociales y rol honorífico en el servidor de
                    Discord "🏆Hackathon23"
                </li>
            </ul>
            <p>Premios para el segundo puesto:</p>
            <ul>
                <li>
                    ✨ Nominaciones para entrar en la red global de talento Nova y la oportunidad de participar en su curso
                    de Personal Branding (persona elegida por el equipo de Nova)
                </li>
                <li>
                    🚀 Beca del 50% de descuento para participar en el programa de incubación de cuatro meses y medio de
                    AgilMentor y crear
                    un MVP a partir de tu proyecto
                </li>
                <li>
                    👀 Certificado, reconocimiento en la página web y redes sociales y rol honorífico en el servidor de
                    Discord "🏆Hackathon23"
                </li>
            </ul>
            <p>Premios para el primer puesto:</p>
            <ul>
                <li>
                    ✨ Nominaciones para entrar en la red global de talento Nova y la oportunidad de participar en su curso
                    de Personal Branding (persona elegida por el equipo de Nova)
                </li>
                <li>
                    🚀 Beca del 50% de descuento para participar en el programa de incubación de cuatro meses y medio de
                    AgilMentor y crear un MVP a partir de tu proyecto
                </li>
                <li>
                    📚 Libros patrocinados por Argilla a elegir entre "NLP with Transformers", "Human-in-the-loop Machine
                    Learning" and "Designing Machine Learning Systems"
                </li>
                <li>
                    👀 Certificado, reconocimiento en la página web y redes sociales y rol honorífico en el servidor de
                    Discord "🏆Hackathon23"
                </li>
            </ul>
            <a :href="localePath('/blog/anuncio-patrocinios-2023')" target="_blank">
                ¡Más detalles sobre los patrocinios de oro aquí!
            </a>

            <hr class="mx-auto my-12 prose" />

            <h2 id="patrocinios">👏 Patrocinios</h2>
            <p>
                Muchísimas gracias por vuestro tiempo y por apoyarnos para que nuestra iniciativa llegue más lejos.
                ¡Vamos a democratizar el PLN en español!
            </p>

            <h3>🥇 Patrocinadores de oro</h3>
            <div class="auto-rows-fr grid gap-x-16 place-items-center lg:grid-cols-3">

                <SponsorInfo sponsor="Argilla" url="http://somosnlp.org/blog/anuncio-patrocinios-2023"
                    logo="/images/patrocinios/Argilla.svg"
                    logo_dark="/images/patrocinios/Argilla.svg" />

                <SponsorInfo sponsor="Q Blocks" url="https://qblocks.cloud/"
                    logo="/images/patrocinios/QBlocks.png"
                    logo_dark="/images/patrocinios/QBlocks_dark.png" />

                <SponsorInfo sponsor="Hugging Face" url="http://somosnlp.org/blog/anuncio-patrocinios-2023"
                    logo="/images/patrocinios/HuggingFace.svg"
                    logo_dark="/images/patrocinios/HuggingFace.svg" />

                <SponsorInfo sponsor="Instituto Milenio Fundamentos de los Datos"
                    url="http://somosnlp.org/blog/anuncio-patrocinios-2023"
                    logo="/images/patrocinios/IMFD.png"
                    logo_dark="/images/patrocinios/IMFD_dark.png" />

                <SponsorInfo sponsor="Nova" url="http://somosnlp.org/blog/anuncio-patrocinios-2023"
                    logo="/images/patrocinios/Nova.png"
                    logo_dark="/images/patrocinios/Nova_dark.png" />

                <SponsorInfo sponsor="AgilMentor" url="http://somosnlp.org/blog/anuncio-patrocinios-2023"
                    logo="/images/patrocinios/AgilMentor.png"
                    logo_dark="/images/patrocinios/AgilMentor.png" />

                <SponsorInfo sponsor="Women Tech Global Conference" url="http://somosnlp.org/blog/anuncio-patrocinios-2023"
                    logo="/images/patrocinios/WomenTechNetwork.png"
                    logo_dark="/images/patrocinios/WomenTechNetwork.png" />
            </div>

            <h3>🥈 Patrocinadores de plata</h3>
            <div class="auto-rows-fr grid gap-x-16 place-items-center lg:grid-cols-3">
                <SponsorInfo sponsor="Spain AI" url="https://www.spain-ai.com/"
                    logo="/images/patrocinios/SpainAI.png"
                    logo_dark="/images/patrocinios/SpainAI_dark.png" />

                <SponsorInfo sponsor="Narrativa" url="https://www.narrativa.com/"
                    logo="/images/patrocinios/Narrativa.png"
                    logo_dark="/images/patrocinios/Narrativa_dark.png" />

                <SponsorInfo sponsor="DataGénero" url="https://www.datagenero.org"
                    logo="/images/patrocinios/DataGenero.png"
                    logo_dark="/images/patrocinios/DataGenero.png" />

                <SponsorInfo sponsor="Instituto de Ingeniería del Conocimiento" url="https://www.iic.uam.es"
                    logo="/images/patrocinios/iic.bmp"
                    logo_dark="/images/patrocinios/iic_dark.bmp" />

                <SponsorInfo sponsor="UNED Research Group in NLP & IR" url="https://sites.google.com/view/nlp-uned/home"
                    logo="/images/patrocinios/UNEDNLP.png"
                    logo_dark="/images/patrocinios/UNEDNLP.png" />

                <SponsorInfo sponsor="Meaning Cloud" url="https://www.meaningcloud.com/"
                    logo="/images/patrocinios/MeaningCloud.png"
                    logo_dark="/images/patrocinios/MeaningCloud.png" />
            </div>

            <h3>🥉 Patrocinadores de bronce</h3>
            <div class="auto-rows-fr grid gap-x-16 place-items-center lg:grid-cols-3">
                <SponsorInfo sponsor="AI The New Sexy" url="https://linktr.ee/aithenewsexy"
                    logo="/images/patrocinios/AiTheNewSexy.PNG"
                    logo_dark="/images/patrocinios/AiTheNewSexy.PNG" />

                <SponsorInfo sponsor="Big Onion" url="https://datakondo.io/"
                    logo="/images/patrocinios/BigOnion.jpg"
                    logo_dark="/images/patrocinios/BigOnion.jpg" />

                <SponsorInfo sponsor="Capítulo Estudiantil AAAIMX" url="https://www.aaaimx.org/"
                    logo="/images/patrocinios/AAAIMX.png"
                    logo_dark="/images/patrocinios/AAAIMX_dark.png" />

                <SponsorInfo sponsor="DiverTLes" url="https://gplsi.dlsi.ua.es/pln/divertles"
                    logo="/images/patrocinios/DiverTLes.png"
                    logo_dark="/images/patrocinios/DiverTLes_dark.png" />

                <SponsorInfo sponsor="Grupo de Ingeniería Lingüística de la UNAM"
                    url="https://www.facebook.com/ingenieriaLinguistica"
                    logo="/images/patrocinios/GIL_UNAM.jpeg"
                    logo_dark="/images/patrocinios/GIL_UNAM.jpeg" />

                <SponsorInfo sponsor="IBiDat" url="https://ibidat.es/"
                    logo="/images/patrocinios/IBiDat.png"
                    logo_dark="/images/patrocinios/IBiDat_dark.png" />

                <SponsorInfo sponsor="MCD UNISON" url="https://mcd.unison.mx"
                    logo="/images/patrocinios/MCDUnisonMX.png"
                    logo_dark="/images/patrocinios/MCDUnisonMX.png" />

                <SponsorInfo sponsor="Mujeres Tech" url="https://www.mujerestech.com/"
                    logo="/images/patrocinios/MujeresTech.png"
                    logo_dark="/images/patrocinios/MujeresTech.png" />

                <SponsorInfo sponsor="NLP Spain" url="https://nlpspain.blogspot.com/"
                    logo="/images/patrocinios/NLPSpain.jpg"
                    logo_dark="/images/patrocinios/NLPSpain.jpg" />

                <SponsorInfo sponsor="NLP Webinar MX" url="http://www.nlpwebinarmx.org/"
                    logo="/images/patrocinios/NLPmx.png"
                    logo_dark="/images/patrocinios/NLPmx.png" />

                <SponsorInfo sponsor="Saturdays AI" url="https://saturdays.ai/"
                    logo="/images/patrocinios/SaturdaysAI.png"
                    logo_dark="/images/patrocinios/SaturdaysAI.png" />

                <SponsorInfo sponsor="Software Themis" url="https://www.themis.es/"
                    logo="/images/patrocinios/SoftwareThemis.png"
                    logo_dark="/images/patrocinios/SoftwareThemis_dark.png" />

                <SponsorInfo sponsor="Universidad Nacional de Loja" url="https://unl.edu.ec"
                    logo="/images/patrocinios/UNL.png"
                    logo_dark="/images/patrocinios/UNL_dark.png" />
            </div>
        </article>
    </Container>
</template>
