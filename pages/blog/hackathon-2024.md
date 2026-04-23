---
title: Finaliza nuestro hackathon 2024
description: Descubre los proyectos finales y las charlas impartidas
date: 2024-05-03T18:00:00.000+00:00
lang: es
duration: 6min
cover: /images/eventos/240301_hackathon.jpg
author: María Grandury
bio: Fundadora de SomosNLP
website: https://mariagrandury.com
twitter: https://twitter.com/mariagrandury
linkedin: https://www.linkedin.com/in/mariagrandury
huggingface: https://huggingface.co/mariagrandury
tags: [hackathon]
---

Ha finalizado la tercera edición del [hackathon de SomosNLP](https://somosnlp.org/hackathon), ¡vaya experiencia!

<div class="flex justify-center">
    <img src="/images/eventos/240301_hackathon.jpg" alt="Cartel Hackathon 2024" width="560" height="315"/>
</div>

Es todo un placer haber organizado un evento que haya conseguido reunir una vez más a más de 500 participantes de 30 países.

<div class="flex justify-center">
    <img src="/images/asistentes_hackathon_mapa.png" alt="Mapa de participantes 2024" width="560" height="315"/>
</div> <!--TOOD actualizar mapa-->

## Proyectos

¿Tienes curiosidad por ver los proyectos que se han desarrollado durante el Hackathon #Somos600M? ¡Aquí están!

👏 Un total de 19 proyectos de PLN en español enfocados en modelos de lenguaje que siguen instrucciones, ¡enhorabuena a todos los equipos!

🎦 Los vídeos de las presentaciones están disponibles en [esta playlist de YouTube](https://youtube.com/playlist?list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J&si=labN1RndCXO-W2PE) junto a los talleres y charlas de especialistas celebrados durante el hackathon.

🤗 Todos los recursos están disponibles en el Hub de Hugging Face: hf.co/somosnlp

Esperamos que os gusten y que surjan muchas aplicaciones utilizando estos nuevos recursos abiertos 💛

<div class="flex justify-center">
<a href="https://www.youtube.com/playlist?list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J" target="_blank">
    <img src="/images/eventos/240411_presentaciones.jpg"
        width="650" height="365" alt="Proyectos del Hackathon 2024" />
</a>
</div>

---

Y... 🥁🥁🥁

Los tres proyectos ganadores son:
- 🥇 NoticIA: Resumen de Noticias Clickbait
- 🥈 AsistenciaRefugiados: Asistencia legal para refugiados
- 🥉 TraductorInclusivo: Reescritura de textos utilizando lenguaje inclusivo

Y el proyecto más querido por la comunidad es:
- 💛 AviaciónInteligente: Navegación del Reglamento Aeronáutico Colombiano

Mención especial a los proyectos:
- 👏 ThinkParaguayo: Conoce la cultura guaraní
- 👏 LenguajeClaro: Simplificación de lenguaje administrativo
- 👏 BERTIN-ClimID: BERTIN-Base Climate-related text Identification

Y a los corpus:
- 📚 SMC: Spanish Medical Corpus
- 📚 RecetasDeLaAbuel@: Corpus de recetas de países hispanoamericanos
- 📚 LingComp_QA: Un corpus educativo de lingüística computacional en español
- 📚 KUNTUR: Constitución política de Perú de 1993
- 📚 Identificación de provincias y resúmenes del Corpus Oral y Sonoro del Español Rural

¡Enhorabuena a tooodos los equipos!

---

### 🥇 NoticIA: Resumen de Noticias Clickbait

Un dataset para el resumen de artículos clickbait en español. 

La práctica del Clickbait erosiona la confianza del público en las fuentes de noticias digitales y perjudica los ingresos publicitarios de los productores de contenido legítimo, que pueden experimentar una disminución en su tráfico web como resultado. Para abordar este desafío, hemos creado un corpus con 850 artículos de noticias clickbait en español. Cada artículo está acompañado de un resumen generativo de alta calidad y concisión, redactado por expertos humanos.

**ODS:** 8. Trabajo decente y crecimiento económico

**Proyecto:**
- [Corpus: NoticIA-IT](https://huggingface.co/datasets/somosnlp/NoticIA-it)
- [Modelo: NoticIA-7B](https://huggingface.co/somosnlp/NoticIA-7B)
- [Demo](https://huggingface.co/spaces/somosnlp/NoticIA-demo)
- [Presentación](https://www.youtube.com/watch?v=xc60K_NzUgk&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J&index=17)

¡Enhorabuena equipo!
- Iker García-Ferrero
- Begoña Altuna

---

### 🥈 AsistenciaRefugiados: Asistencia legal para refugiados

Asistente legal para personas en situación de refugio o asilo político.

España es el tercer país con mayor número de solicitudes de asilo, recibiendo cada año aproximadamente más de 100.000 solicitudes, y el tercero con menor número de aprobaciones dentro de la UE.

El objetivo principal de este proyecto es facilitar las tareas de las ONG de este ámbito y de otras instituciones y ayudarles a obtener respuestas a preguntas (QA) relacionadas con la legislación sobre refugiados en español. Con su refinada comprensión de los matices y complejidades de este campo legal.

**ODS:** 10. Reducción de las desigualdades 16. Paz, justicia e instituciones sólidas

**Proyecto:**
- [Corpus: AsistenciaRefugiados](https://huggingface.co/datasets/somosnlp/instruct-legal-refugiados-es)
- [Modelo: AsistenciaRefugiados 7B](https://huggingface.co/somosnlp/gemma-7b-it-legal-refugee-v0.1.1)
- [Demo](https://huggingface.co/spaces/somosnlp/QA-legal-refugiados)
- [Presentación](https://www.youtube.com/watch?v=1OqHDE5LKMI&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J&index=28)

¡Enhorabuena equipo!
- Eduardo Muñoz Sala
- Álvaro Hidalgo
- Teresa Martín

---

### 🥉 Traductor-Inclusivo: Reescritura de textos en español utilizando lenguaje inclusivo

Herramienta que permite reescribir textos en español utilizando lenguaje inclusivo.

El lenguaje o palabras que utilizamos muchas veces pueden imponer sesgos, ideologías o marginar a determinados grupos. "Traductor-Inclusivo" es una herramienta que permite reescribir textos utilizando lenguaje inclusivo ofreciendo una opción para evitar dichos sesgos.

**ODS:** 5. Igualdad de género

**Proyecto:**
- [Corpus: Traductor-Inclusivo](https://huggingface.co/datasets/somosnlp/es-inclusive-language)
- [Modelo: Traductor-Inclusivo](https://huggingface.co/somosnlp/es-inclusivo-translator)
- [Demo](https://huggingface.co/spaces/somosnlp/es-inclusive-language-demo)
- [Presentación](https://www.youtube.com/watch?v=7rrNGJIXEHU&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J&index=20)

¡Enhorabuena equipo!
- Andrés Martínez Fernández-Salguero
- Gaia Quintana Fleitas
- Miguel López Pérez
- Imanuel Rozenberg
- Josué Sauca

---

### 💛 AviaciónInteligente: Uso de LLMs para Facilitar la Navegación del Reglamento Aeronáutico Colombiano

Investigación que utiliza modelos de lenguaje de última generación para mejorar la comprensión y navegación del Reglamento Aeronáutico Colombiano (RAC), con el objetivo de facilitar el acceso a la información y mejorar la seguridad en la aviación civil.

El proyecto "Aviación Inteligente: LLMs para Navegar el RAC" está revolucionando el acceso al Reglamento Aeronáutico Colombiano a través de tecnologías avanzadas de Modelos de Lenguaje. Con la colaboración de la Fundación Universitaria Los Libertadores y un equipo de expertos anotadores, hemos creado y etiquetado 24,000 entradas curadas en nuestro dataset. Además, hemos realizado un afinamiento (finetuning) del modelo GEMMA 2B IT ColombiaRAC, optimizado específicamente para navegar eficazmente a través de las regulaciones aeronáuticas. Este enfoque no solo facilita las consultas normativas sino que también democratiza el conocimiento en la industria, haciendo la información aeronáutica accesible a un público más amplio y reduciendo las barreras de entrada en el campo. Este proyecto es un paso hacia un futuro donde el acceso y comprensión de las regulaciones aeronáuticas son más simples y abiertos para todos.

**ODS:** 4. Educación de calidad, 9. Industria, innovación e infraestructura

**Proyecto:**
- [Corpus: Base de Datos del Reglamento Aeronáutico Colombiano](https://huggingface.co/datasets/somosnlp/ColombiaRAC_FullyCurated)
- [Modelo: AviacionInteligente](https://huggingface.co/somosnlp/AviacionInteligente_gemma-2b-it-bnb-4bit)
- [Demo](https://huggingface.co/spaces/somosnlp/AviacionInteligente_Demo)
- [Presentación](https://www.youtube.com/watch?v=IGKU1qUur2c&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J&index=25)

¡Enhorabuena equipo!
- Edison Jair Bejarano Sepulveda
- Alec Mauricio Rosales Cabezas
- Santiago Pineda Montoya
- Nicolai Potes

---

### ThinkParaguayo: Conoce la cultura guaraní

Tenemos la misión de expandir la cultura guaraní mediante la IA.

La cultura guaraní tiene una riqueza increíble, que merece ser preservada y contada a las nuevas generaciones. Think Paraguayo es un proyecto destinado a promover y difundir la cultura guaraní utilizando la inteligencia artificial como herramienta principal. El objetivo es crear conciencia sobre la riqueza cultural del Paraguay y preservar la lengua y las tradiciones guaraníes. 

**ODS:** 4. Educación de calidad

**Proyecto:**
- [Corpus: Cultura Guaraní](https://huggingface.co/datasets/somosnlp/dataset-cultura-guarani_corpus-it)
- [Modelo: ThinkParaguayo](https://huggingface.co/somosnlp/gua-a)
- [Demo](https://huggingface.co/spaces/somosnlp/think-paraguayo)
- [Presentación](https://www.youtube.com/watch?v=1AV_37FJSzk&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J&index=25)

¡Enhorabuena equipo!
- Enrique Paiva
- Daniel Cabrera
- Leticia Bogado
- Alberto Benítez
- Emmanuel

---

### LenguajeClaro: Simplificación de lenguaje administrativo

Este modelo es el primer paso hacia un modelo de lenguaje que pueda usarse para reescribir textos de carácter administrativo con el objetivo de hacerlos más asequibles para todo el mundo.

**ODS:** 9. Industria, innovación e infraestructura, 10. Reducción de las desigualdades

**Proyecto:**
- [Corpus: LenguajeClaroQA](https://huggingface.co/datasets/somosnlp/lenguaje-claro-dataset)
- [Modelo: LenguajeClaro](https://huggingface.co/somosnlp/Phi-2-LenguajeClaro)
- [Demo](https://huggingface.co/spaces/somosnlp/lenguaje-claro-demo)
- [Presentación](https://www.youtube.com/watch?v=zv7vQVHP6gE&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J&index=22)

¡Enhorabuena equipo!
- Sergio Chicón Repiso
- Rubén Rodríguez de la Fuente
- Marta Fernández Gómez

---

### BERTIN-ClimID: BERTIN-Base Climate-related text Identification

Identificación de textos sobre sustentabilidad y cambio climático

Motivados por la idea de crear una repositorio en español sobre información o recursos en temas como cambio climático, sustentabilidad, calentamiento global, energía, etc.  La idea es dar visibilidad a soluciones, ejemplos de buenas prácticas ambientales o noticias que nos ayuden a combatir los efectos del cambio climático.

**ODS:** 13. Acción por el clima

**Proyecto:**
- [Corpus: ClimateDetection](https://huggingface.co/datasets/somosnlp/spa_climate_detection)
- [Modelo: BERTIN-ClimID](https://huggingface.co/somosnlp/bertin_base_climate_detection_spa_v2)
- [Demo](https://huggingface.co/spaces/somosnlp/Identificacion_de_textos_sobre_sustentabilidad_cambio_climatico)
- [Presentación](https://www.youtube.com/watch?v=sfXLUP9Ei-o&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J&index=23)

¡Enhorabuena equipo!
- Gabriela Zuñiga
- Gerardo Huerta

---

### SpanishMedicaLLM & SMC: Spanish Medical Corpus

Creación de un LLM  para dar soluciones y servicios de información de salud en LATAM.

El objetivo de este proyecto es crear un gran modelo de lenguaje (LLM; siglas en inglés) para el contexto médico en español permitiendo crear soluciones y servicios de información de salud en LATAM. El modelo contará con información de medicinas convencionales, naturales y tradicionales. Un resultado del proyecto es un conjunto de datos público del dominio médico que agrupa recursos de otras fuentes que permite crear o ajustar LLM . Los resultados del desempeño del LLM se comparan con  otros modelos del state-of-the-art como BioMistral, Meditron, MedPalm.

**ODS:** 3. Salud y bienestar

**Proyecto:**
- [Corpus: SMC (SpanishMedicalCorpus)](https://huggingface.co/datasets/somosnlp/spanish_medica_llm)
- [Modelo: SpanishMedicaLLM](https://huggingface.co/somosnlp/spanish_medica_llm)
- [Demo](https://huggingface.co/spaces/somosnlp/SpanishMedicaLLM)
- [Presentación](https://www.youtube.com/watch?v=tVe_MC7Da6k&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J&index=18)

¡Enhorabuena equipo!
- Dr. Dionis López Ramos
- Alvaro García Barragan
- Dariel Cabrebra
- Dylan Montoya
- Daniel Bermúdez

<!-- - Dr. Dionis López Ramos (Cuba)
- Alvaro García Barragan (España)
- Dariel Cabrebra (Cuba)
- Dylan Montoya (Colombia)
- Daniel Bermúdez (México) -->

---

### RecetasDeLaAbuel@: Corpus de recetas de países hispanoamericanos

El corpus 'RecetasDeLaAbuel@' es un homenaje a todas nuestr@s abuel@s que nos han enseñado a cocinar. Se trata de la mayor y más completa colección de recetas en español de países hispanoamericanos.

Nuestra misión es la creación de una IA en español que agrupe recetas de países hispanoamericanos y permita mejorar nuestra relación con la preparación y el cocinado de los alimentos. El objetivo final es la construcción de un asistente de cocina inteligente específico del idioma español.

**ODS:** 3. Salud y bienestar

**Proyecto:**
- [Corpus: RecetasDeLaAbuel@](https://huggingface.co/datasets/somosnlp/RecetasDeLaAbuela)
- [Modelo: RecetasDeLaAbuel@ 7B](https://huggingface.co/somosnlp/RecetasDeLaAbuela_gemma-2b-it-bnb-4bit)
- [Demo](https://huggingface.co/spaces/somosnlp/RecetasDeLaAbuela_Demo)
- [Presentación](https://www.youtube.com/watch?v=WK-1F1TX5d4&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J&index=19)

¡Enhorabuena equipo!
- roverico 
- Óscar
- Gabriel
- Sara
- Fredy

---

### ComeBien: Asistente de nutrición inteligente

ComeBien es un asistente de nutrición inteligente específico del idioma español que permite ayudarnos a comer de una manera saludable.

Nuestra misión es la creación de una IA en español que complemente recetas de países hispanoamericanos con su valor nutricional y permita mejorar nuestra relación con la comida. El objetivo final es la construcción de un asistente de nutrición inteligente específico del idioma español.

**ODS:** 3. Salud y bienestar

**Proyecto:**
- [Corpus: RecetasDeLaAbuel@](https://huggingface.co/datasets/somosnlp/RecetasDeLaAbuela)
- [Modelo: ComeBien 2B](https://huggingface.co/somosnlp/ComeBien_gemma-2b-it-bnb-4bit)
- [Demo](https://huggingface.co/spaces/somosnlp/ComeBien_Demo)
- [Presentación](https://www.youtube.com/watch?v=WK-1F1TX5d4&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J&index=19)

¡Enhorabuena equipo!
- roverico
- Andrea

---

### LingComp_QA: Un corpus educativo de lingüística computacional en español

LingComp_QA es un primer acercamiento que hemos hecho a la recolección de información sobre lingüística computacional, ya que consideramos que no hay suficientes recursos educativos en torno a este tema. Tenemos intención de ampliarlo y crear un modelo para alumnos de Lingüística y otros interesados en ponerse al día en PLN. 

**ODS:** 4. Educación de calidad, 9. Industria, innovación e infraestructura

**Proyecto:**
- [Corpus: LingComp_QA](https://huggingface.co/datasets/somosnlp/Lingcomp_QA)
- [Modelo: LingComp_QA Gemma 2B IT](https://huggingface.co/somosnlp/Lingcomp_QA_gemma-2b-it-bnb-4bit)
- [Demo](https://huggingface.co/spaces/somosnlp/Lingcomp_QA_Demo)

¡Enhorabuena equipo!
- Jorge Zamora Rey
- Mario Crespo Miguel
- Isabel Moyano Moreno

<!-- Equipo del Laboratorio de Lingüística computacional y digital del Instituto de Lingüística Aplicada de la Universidad de Cádiz -->

---

### KUNTUR: LLM de asistencia legal en textos jurídicos de Perú

El proyecto KUNTUR busca abordar la brecha de acceso a la información legal en Perú, especialmente para comunidades rurales y personas sin experiencia en derecho. Su objetivo es desarrollar un modelo de lenguaje especializado que haga que la ley sea más comprensible y accesible para todos, capacitando a individuos con conocimientos legales para tomar decisiones informadas y proteger sus derechos.

**ODS:** 16. Paz, justicia e instituciones sólidas

**Proyecto:**
- [Corpus: Constitución de Perú 1993 QA](https://huggingface.co/datasets/somosnlp/constitucion-politica-del-peru-1993-qa)
- [Modelo: KUNTUR Gemma 2B](https://huggingface.co/somosnlp/kuntur-peru-legal-es-gemma-2b-it-merged)
- [Demo](https://huggingface.co/spaces/somosnlp/KUNTUR/)
- [Presentación](https://www.youtube.com/watch?v=7Og2c8yyZqs&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J&index=27)

¡Enhorabuena!
- David Alonso Quispe Castillo

---

### Identificación de provincias y resúmenes con el COSER

En este proyecto se han generado dos corpus de instrucciones para la identificación de provincias de hablantes y resumen de las entrevistas basándose en el Corpus Oral y Sonoro del Español Rural.

**ODS:** 4. Educación de calidad, 10. Reducción de las desigualdades

**Proyecto:**
- [Corpus: COSER Resúmenes](https://huggingface.co/datasets/somosnlp/coser_resumenes)
- [Corpus: COSER Identifiación provincias](https://huggingface.co/datasets/somosnlp/coser_identificacion_provincias)

¡Enhorabuena equipo!
- Clara Adsuar
- Álvaro Bueno
- Benito
- Alberto Hernández
- Manuel Otero

---

### ChaterapIA

Dar acceso a ayuda psicológica a personas en necesidad. No importan tus recursos, la hora o el sitio, si necesitas ayuda siempre tendría que ser posible tener acceso a ella.

**ODS:** 3. Salud y bienestar, 10. Reducción de las desigualdades

**Proyecto:**
- [Corpus: ConversacionesTerapeuticas](https://huggingface.co/datasets/somosnlp/Conversaciones_terapeuticas_espanol)
- [Modelo: ChaterapIA](https://huggingface.co/somosnlp/chaterapia_model)
- [Demo](https://huggingface.co/spaces/somosnlp/chaterapia_demo)

¡Enhorabuena equipo!
- Julio 
- Nicho
- Joana
- Dyana
- Pablo

<!--

### SAM Doctor

Proyecto:
- [Corpus](https://huggingface.co/somosnlp/Sam_Diagnostic)
- [Modelo](https://huggingface.co/spaces/somosnlp/Sam_Diagnostic)

### WikiHow

Proyecto:
- [Corpus](https://huggingface.co/datasets/somosnlp/wikihow_es_80train_20test)

-->

---

¡Enhorabuena de nuevo a todo el mundo, muchísimas gracias por participar en esta maravillosa tercera edición del Hackathon SomosNLP! 👏🤩

---

## Charlas y talleres

<div class="mx-auto my-8 text-center">
    <div class="grid grid-cols-2 gap-8 my-1">
        <a href="/hackathon-2024/ia_y_lms_retos_y_oportunidades" target="_blank">
            <img alt="Charla de Elena González-Blanco" width="650" height="365"
                src="/images/eventos/240307_elena_gonzalez_blanco.png" />
        </a>
        <a href="/hackathon-2024/crear_datasets_de_calidad_con_argilla_y_distilabel" target="_blank">
            <img alt="Charla de Gabriel Martín" width="650" height="365"
                src="/images/eventos/240311_gabriel_martin_blazquez.jpg" />
        </a>
        <a href="/hackathon-2024/importancia_de_la_calidad_de_los_datos_al_entrenar" target="_blank">
            <img alt="Charla de Manu Romero" width="650" height="365"
                src="/images/eventos/240311_manu_romero.jpg" />
        </a>
        <a href="/hackathon-2024/diversidad_linguistica_en_ia" target="_blank">
            <img alt="Charla de María Grandury" width="650" height="365"
                src="/images/eventos/240313_maria_grandury.jpg" />
        </a>
        <a href="/hackathon-2024/deteccion_de_sesgos_en_medios_de_comunicacion" target="_blank">
            <img alt="Charla de Fran Rodrigo" width="650" height="365"
                src="/images/eventos/240313_francisco_javier_rodrigo.jpg" />
        </a>
        <a href="/hackathon-2024/combatiendo_el_discurso_de_odio_mediante_contranarrativas" target="_blank">
            <img alt="Charla de Estrella Vallecillo" width="650" height="365"
                src="/images/eventos/240313_estrella_vallecillo.jpg" />
        </a>
        <a href="/hackathon-2024/etica_ambiental_en_ia" target="_blank">
            <img alt="Charla de Jorge Vallego" width="650" height="365"
                src="/images/eventos/240313_jorge_vallego.jpg" />
        </a>
        <a href="/hackathon-2024/entrenamiento_de_llms" target="_blank">
            <img alt="Charla de Alejandro Vaca" width="650" height="365"
                src="/images/eventos/240318_alejandro_vaca.jpg" />
        </a>
        <a href="/hackathon-2024/prospectiva_estrategica_y_nlp" target="_blank">
            <img alt="Charla de Cristina Vila" width="650" height="365"
                src="/images/eventos/240319_cristina_vila.jpg" />
        </a>
        <a href="/hackathon-2024/estimacion_de_la_severidad_de_la_depresion_en_internet" target="_blank">
            <img alt="Charla de Anxo Pérez" width="650" height="365"
                src="/images/eventos/240319_anxo_perez.jpg" />
        </a>
        <a href="/hackathon-2024/como_anotar_corpus_linguisticos_para_entrenar_llms" target="_blank">
            <img alt="Charla de Marta Guerrero" width="650" height="365"
                src="/images/eventos/240320_marta_guerrero.jpg" />
        </a>
        <a href="/hackathon-2024/empatia_y_emociones_en_ia" target="_blank">
            <img alt="Charla de Amanda Curry" width="650" height="365"
                src="/images/eventos/240326_amanda_curry.jpg" />
        </a>
    </div>
</div>
