<script setup lang="ts">
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
</script>

<template>
    <Container class="my-12">

        <header class="m-auto text-center prose">
            <h1>{{ t('events.title') }}</h1>
            <p class="text-lg">
                {{ t('events.subtitle') }}
            </p>
        </header>

        <hr class="mx-auto mt-8 mb-12 prose" />

        <article class="m-auto prose">

            <!-- <div class="mx-auto my-8 text-center">
                <span class="font-medium text-xl tracking-wider text-accent-500 uppercase"
                    dark="text-accent-400">Próximos eventos</span>
                <a href="https://hackathonsomosnlp2024.eventbrite.com/?aff=w" target="_blank">
                    <div class="flex justify-center grid grid-cols-2 gap-5">
                    <div class="flex justify-center">
                        <img alt="Charla de Amanda Curry" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/240326_amanda_curry.jpg" />

                    </div>
                </a>
            </div> -->

            <div class="mt-10 grid gap-4 lg:grid-cols-2">
                <a href="https://somosnlp.org/eventos/calendario" target="_blank" class="button-accent">
                    <carbon:calendar />
                    {{ t('events.calendar.view') }}
                </a>
                <a href="https://calendar.google.com/calendar/u/0?cid=ZWM3MGZhODIzNmYyNzBlMTYwYzFiMjdhNDgzZWMyMjA1ZjQwYzUyN2E5N2MwZTJhZmY0OTcwZDZmZjBkYzQyMEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t"
                    target="_blank" class="button-gray">
                    <carbon:logo-google />
                    {{ t('events.calendar.join') }}
                </a>
            </div>

            <hr class="mx-auto mt-8 mb-12 prose" />
            <div class="text-center font-medium text-xl tracking-wider text-accent-500 uppercase" dark="text-accent-400">Únete
                al Hackathon #Somos600M</div>

            <div class="mt-10 grid gap-4 lg:grid-cols-1">
                
                <a href="/hackathon" target="_blank">
                    <img alt="Hackathon #Somos600M" width="650" height="365"
                        src="https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg" />
                </a>
                <!-- 
                <a href="/hackathon/ponencias" target="_blank">
                    <img alt="Hackathon #Somos600M" width="650" height="365"
                        src="https://somosnlp.github.io/assets/images/eventos/250401_hackathon_callfortalks.jpg" />
                </a> -->
            </div>

            <div class="m-12">
                <span class="font-medium text-xl tracking-wider text-accent-500 uppercase"
                    dark="text-accent-400">{{ t('events.sections.recordings') }}</span>
                <ul>
                    <li>
                        <a href="#hackathon-2024">{{ t('events.sections.hackathon-2024') }}</a>
                    </li>
                    <li>
                        <a href="#hackathon-2023">{{ t('events.sections.hackathon-2023') }}</a>
                    </li>
                    <li>
                        <a href="#hackathon-2022">{{ t('events.sections.hackathon-2022') }}</a>
                    </li>
                    <li>
                        <a href="#somos-mujeres-nlp">{{ t('events.sections.somos-mujeres-nlp') }}</a>
                    </li>
                    <li>
                        <a href="#proyectos-de-la-comunidad">{{ t('events.sections.community') }}</a>
                    </li>
                </ul>
            </div>

            <h3 id="hackathon-2025">{{ t('events.sections.hackathon-2025') }}</h3>
            <div class="mx-auto my-8 text-center">
            <div class="grid grid-cols-2 gap-8 my-1">
                <a href="https://www.youtube.com/playlist?list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6" target="_blank">
                    <img alt="Alfonso Amayuelas" width="650" height="365"
                        src="https://github.com/somosnlp/assets/raw/main/images/eventos/250415_alfonso_amayuelas.png" />
                </a>

                <a href="https://www.youtube.com/playlist?list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6" target="_blank">
                    <img alt="Selene Baez" width="650" height="365"
                        src="https://github.com/somosnlp/assets/raw/main/images/eventos/250410_selene_baez.png" />
                </a>

                <a href="https://www.youtube.com/playlist?list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6" target="_blank">
                    <img alt="Luis Vasquez" width="650" height="365"
                        src="https://github.com/somosnlp/assets/raw/main/images/eventos/250410_luis_vasquez.png" />
                </a>
            </div>
            </div>

            <h3 id="eventos-madrid">{{ t('events.sections.madrid') }}</h3>

            <div class="mx-auto my-8 text-center">
                <div class="grid grid-cols-2 gap-8 my-1">
                    <a href="/eventos/madrid/evaluacion-de-llms" target="_blank">
                        <img alt="Evaluación de LLMs" width="650" height="365"
                            src="https://github.com/somosnlp/assets/raw/main/images/eventos/20241217_evaluacion_llm_upm.png" />
                    </a>

                    <a href="/eventos/madrid/suenan-los-directivos-con-proyectos-de-ia" target="_blank">
                        <img alt="Sueñan los directivos con proyectos de IA" width="650" height="365"
                            src="https://github.com/somosnlp/assets/raw/main/images/eventos/20250115_entaina_directivos_ia.png" />
                    </a>
                </div>

                <p>¿Organizamos un evento presencial en tu ciudad?</p>
            </div>

            <h3 id="hackathon-2024">{{ t('events.sections.hackathon-2024') }}</h3>

            <div class="mx-auto my-8 text-center">
                <div class="grid grid-cols-2 gap-8 my-1">
                    <a href="/hackathon-2024/ia_y_lms_retos_y_oportunidades" target="_blank">
                        <img alt="Charla de Elena González-Blanco" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/240307_elena_gonzalez_blanco.png" />
                    </a>

                    <a href="/hackathon-2024/crear_datasets_de_calidad_con_argilla_y_distilabel" target="_blank">
                        <img alt="Charla de Gabriel Martín" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/240311_gabriel_martin_blazquez.jpg" />
                    </a>

                    <a href="/hackathon-2024/importancia_de_la_calidad_de_los_datos_al_entrenar" target="_blank">
                        <img alt="Charla de Manu Romero" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/240311_manu_romero.jpg" />
                    </a>

                    <a href="/hackathon-2024/diversidad_linguistica_en_ia" target="_blank">
                        <img alt="Charla de María Grandury" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/240313_maria_grandury.jpg" />
                    </a>

                    <a href="/hackathon-2024/deteccion_de_sesgos_en_medios_de_comunicacion" target="_blank">
                        <img alt="Charla de Fran Rodrigo" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/240313_francisco_javier_rodrigo.jpg" />
                    </a>

                    <a href="/hackathon-2024/combatiendo_el_discurso_de_odio_mediante_contranarrativas" target="_blank">
                        <img alt="Charla de Estrella Vallecillo" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/240313_estrella_vallecillo.jpg" />
                    </a>

                    <a href="/hackathon-2024/etica_ambiental_en_ia" target="_blank">
                        <img alt="Charla de Jorge Vallego" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/240313_jorge_vallego.jpg" />
                    </a>

                    <a href="/hackathon-2024/entrenamiento_de_llms" target="_blank">
                        <img alt="Charla de Alejandro Vaca" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/240318_alejandro_vaca.jpg" />
                    </a>

                    <a href="/hackathon-2024/prospectiva_estrategica_y_nlp" target="_blank">
                        <img alt="Charla de Cristina Vila" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/240319_cristina_vila.jpg" />
                    </a>

                    <a href="/hackathon-2024/estimacion_de_la_severidad_de_la_depresion_en_internet" target="_blank">
                        <img alt="Charla de Anxo Pérez" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/240319_anxo_perez.jpg" />
                    </a>

                    <a href="/hackathon-2024/como_anotar_corpus_linguisticos_para_entrenar_llms" target="_blank">
                        <img alt="Charla de Marta Guerrero" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/240320_marta_guerrero.jpg" />
                    </a>

                    <a href="/hackathon-2024/empatia_y_emociones_en_ia" target="_blank">
                        <img alt="Charla de Amanda Curry" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/240326_amanda_curry.jpg" />
                    </a>

                </div>
            </div>


            <h3 id="hackathon-2023">{{ t('events.sections.hackathon-2023') }}</h3>

            <div class="mx-auto my-8 text-center">
                <div class="grid grid-cols-2 gap-8 my-1">
                    <a href="/hackathon-2023/fine-tuning-llms" target="_blank">
                        <img alt="Fine-tuning de grandes modelos de lenguaje" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/230320_fine_tuning_llms.jpg" />
                    </a>

                    <a href="/hackathon-2023/etiquetado-de-datos-con-argilla" target="_blank">
                        <img alt="Introducción a Argilla" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/230321_etiquetado_de_datos_con_argilla.jpg" />
                    </a>

                    <a href="/hackathon-2023/ama-con-omar-sanseviero" target="_blank">
                        <img alt="AMA con Omar Sanseviero" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/230322_ama_con_omar_sanseviero.jpg" />
                    </a>

                    <a href="hackathon-2023/ama-con-natalia-elvira" target="_blank">
                        <img alt="AMA con Natalia Elvira" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/230323_ama_con_natalia_elvira.jpg" />
                    </a>

                    <a href="hackathon-2023/tecnologias-clave-de-chatgpt" target="_blank">
                        <img alt="Tecnologías clave de ChatGPT" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/230328_tecnologias_clave_de_chatgpt.jpg" />
                    </a>

                    <a href="/hackathon-2023/evaluacion-de-sesgos" target="_blank">
                        <img alt="Evaluación de sesgos" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/230328_evaluacion_de_sesgos.jpg" />
                    </a>

                    <a href="hackathon-2023/impacto-de-los-llms" target="_blank">
                        <img alt="Impacto de los LLMs" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/230328_impacto_de_los_llms.jpg" />
                    </a>

                    <a href="hackathon-2023/aymurai" target="_blank">
                        <img alt="AymurAI" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/230328_aymurai.jpg" />
                    </a>

                    <a href="/hackathon-2023/de-la-idea-a-la-startup" target="_blank">
                        <img alt="De la idea a la startup" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/230329_de_la_idea_a_la_startup.jpg" />
                    </a>

                    <a href="/hackathon-2023/ama-con-alejandro-vaca" target="_blank">
                        <img alt="AMA con Alejandro Vaca" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/230330_ama_con_alejandro_vaca.jpg" />
                    </a>

                    <a href="/hackathon-2023/proyecto-bertin" target="_blank">
                        <img alt="Proyecto BERTIN" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/230403_proyecto_bertin.jpg" />
                    </a>

                    <a href="/hackathon-2023/estrategias-de-simplificacion-para-llms" target="_blank">
                        <img alt="Estrategias de simplificación" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/230403_estrategias_de_simplificacion.jpg" />
                    </a>

                    <a href="/hackathon-2023/deteccion-del-lenguaje-ofensivo" target="_blank">
                        <img alt="Detección del lenguaje ofensivo" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/230404_deteccion_del_lenguaje_ofensivo.jpg" />
                    </a>

                    <a href="/hackathon-2023/evaluacion-con-desacuerdo" target="_blank">
                        <img alt="Evaluación con desacuerdo" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/230404_evaluacion_con_desacuerdo.jpg" />
                    </a>

                    <a href="/hackathon-2023/nlp-clinico" target="_blank">
                        <img alt="NLP Clínico" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/230404_nlp_clinico.png" />
                    </a>

                    <a href="/hackathon-2023/pln-en-el-sector-legal" target="_blank">
                        <img alt="PLN en el sector legal" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/230404_pln_en_el_sector_legal.png" />
                    </a>

                </div>
            </div>

            <hr class="mx-auto mt-8 mb-12 prose" />

            <h3 id="hackathon-2022">{{ t('events.sections.hackathon-2022') }}</h3>
            <p>
                {{ t('events.sections.hackathon-2022-description') }}
            </p>

            <div class="mx-auto my-8 text-center">
                <div class="grid grid-cols-2 gap-8 my-1">
                    <a href="https://www.youtube.com/watch?v=3OhArr1R2Lw&list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG"
                        target="_blank">
                        <img alt="RigoBERTa" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/evento_iic.png" />
                    </a>
                    <a href="https://www.youtube.com/watch?v=GX4l3WhOy4o&list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG"
                        target="_blank">
                        <img alt="IA y NLP, una apasionante encrucijada" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/evento_cristina.png" />
                    </a>
                    <a href="https://www.youtube.com/watch?v=UQwWTykNFW0&list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG"
                        target="_blank">
                        <img alt="Muestreo de datos BERTIN" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/evento_paulo.png" />
                    </a>
                    <a href="https://www.youtube.com/watch?v=aNR7UM-E6vA&list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG"
                        target="_blank">
                        <img alt="Lenguas Minorizadas - MX" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/evento_ximena.png" />
                    </a>
                    <a href="https://www.youtube.com/watch?v=_TbNgSodiPY&list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG"
                        target="_blank">
                        <img alt="El ecosistema de Hugging Face" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/evento_14_03_ecosistema_hf.png" />
                    </a>
                    <a href="https://www.youtube.com/watch?v=jvhEra9mdPw&list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG"
                        target="_blank">
                        <img alt="Análisis del error" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/evento_16_03_errores.png" />
                    </a>
                    <a href="https://www.youtube.com/watch?v=_f3eLbrFiCc&list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG"
                        target="_blank">
                        <img alt="AMA I" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/evento_17_03_ama.png" />
                    </a>
                    <a href="https://www.youtube.com/watch?v=UR6MHBbPA3g&list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG"
                        target="_blank">
                        <img alt="Etiquetado de datos" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/evento_29_03_anotacion.png" />
                    </a>
                    <a href="https://www.youtube.com/watch?v=j4qfRljYNYI&list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG"
                        target="_blank">
                        <img alt="Modelos del Lenguaje para RRSS" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/evento_22_03_cardiff.png" />
                    </a>
                    <a href="https://www.youtube.com/watch?v=RWIZj9puFX0&list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG"
                        target="_blank">
                        <img alt="AMA II" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/evento_ama_lewis.png" />
                    </a>
                    <a href="https://www.youtube.com/watch?v=U8fig2fqrl8&list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG"
                        target="_blank">
                        <img alt="Traducción Automática" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/evento_eva.png" />
                    </a>
                    <a href="https://www.youtube.com/watch?v=7ckg10QUHLw&list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG"
                        target="_blank">
                        <img alt="Topics con clustering no-supervisado" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/evento_31_03_topics.png" />
                    </a>
                    <a href="https://www.youtube.com/watch?v=QziYfITvGrA&list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG"
                        target="_blank">
                        <img alt="Taller de escritura de abstracts" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/evento_abstracts.png" />
                    </a>
                </div>
            </div>

            <hr class="mx-auto mt-8 mb-12 prose" />

            <h3 id="somos-mujeres-nlp">{{ t('events.sections.somos-mujeres-nlp') }}</h3>
            <p>
                {{ t('events.sections.somos-mujeres-nlp-description') }}
            </p>
            <div class="mx-auto my-8 text-center">
                <div class="grid grid-cols-2 gap-8 my-1">
                    <a href="https://www.youtube.com/watch?v=5fOiLWXQ78c&list=PLTA-KAy8nxaCGGYz5CWiLZNzc31ilPDyI"
                        target="_blank">
                        <img alt="Mesa Redonda 8M" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/230309_mesa_redonda_8m.jpg" />
                    </a>
                    <a href="https://www.youtube.com/watch?v=ZLd85RiLViQ&list=PLTA-KAy8nxaCGGYz5CWiLZNzc31ilPDyI"
                        target="_blank">
                        <img alt="Somos Mujeres NLP" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/230308_video_8m.jpg" />
                    </a>
                </div>
            </div>

            <hr class="mx-auto mt-8 mb-12 prose" />

            <h3 id="proyectos-de-la-comunidad">{{ t('events.sections.community') }}</h3>
            <p>
                {{ t('events.sections.community-description') }}
            </p>
            <p>
                {{ t('events.sections.community-description-2') }}
                <a
                    href="https://kq8ietkql1m.typeform.com/to/BYH9KG3f"
                    target="_blank">{{ t('events.sections.community-description-3') }}</a>💡
            </p>

            <div class="mx-auto my-8 text-center">
                <div class="grid grid-cols-2 gap-8 my-1">
                    <a href="https://www.youtube.com/watch?v=fOQLPuXewzE&list=PLTA-KAy8nxaAbyaBTYK68TZKQLv9V8L8M"
                        target="_blank">
                        <img alt="BiomedIA" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/230112_biomedia.jpg" />
                    </a>
                    <a href="https://www.youtube.com/watch?v=XOaQKNauySo&list=PLTA-KAy8nxaAbyaBTYK68TZKQLv9V8L8M"
                        target="_blank">
                        <img alt="Modelo Jurídico Mexicano" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/221213_neutralizacion_de_genero.jpg" />
                    </a>
                    <a href="https://www.youtube.com/watch?v=ZTYAsEHUhPs&list=PLTA-KAy8nxaAbyaBTYK68TZKQLv9V8L8M"
                        target="_blank">
                        <img alt="Neutralización de Género" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/221208_modelo_juridico_mexicano.jpg" />
                    </a>
                    <a href="https://www.youtube.com/watch?v=1LmH6lblxvg&list=PLTA-KAy8nxaAbyaBTYK68TZKQLv9V8L8M"
                        target="_blank">
                        <img alt="Detector de Sexismo" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/221212_detector_sexismo.jpg" />
                    </a>
                    <a href="https://www.youtube.com/watch?v=t86nV8Vfzbg&list=PLTA-KAy8nxaAbyaBTYK68TZKQLv9V8L8M"
                        target="_blank">
                        <img alt="Validador de Veracidad de Noticias" width="650" height="365"
                            src="https://somosnlp.github.io/assets/images/eventos/221129_news_veracity_validator.png" />
                    </a>
                </div>
            </div>

            <a href="https://www.youtube.com/c/somosnlp?sub_confirmation=1" target="_blank"
                class="button-accent max-w-100 mx-auto">
                <carbon:logo-youtube text="xl" />
                <span text="center">{{ t('events.all-events') }}</span>
            </a>
        </article>
    </Container>
</template>