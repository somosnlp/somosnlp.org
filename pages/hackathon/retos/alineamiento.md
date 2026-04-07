---
title: "Reto Principal #HackathonSomosNLP 2026: Alineamiento de LLMs y VLLMs"
description: Cómo participar en este reto y ayudar a mejorar el conocimiento cultural de los modelos de lenguaje y visión-lenguaje
lang: es
cover: /images/eventos/250401_hackathon_sinfecha.jpg
---

## 🎯 Objetivo del reto

- Elige una de las siguientes opciones:
    - A. Alinea un **modelo de lenguaje** (LLM) para generar texto de manera culturalmente adecuada
    - B. Adapta un **modelo multimodal visión-lenguaje** (VLLM) para generar descripciones de imágenes teniendo en cuenta el contexto cultural
- En español, portugués o cualquier lengua de la Península Ibérica o LATAM
- Adapta de un modelo ya existente (no pre-entrenes uno desde cero), recomendamos tomar de base modelos en torno a 7B (e.g. [Salamandra](https://huggingface.co/BSC-LT/salamandra-7b-instruct), [Mistral](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) y [Gemma](https://huggingface.co/google/gemma-3-4b-it))
- ¡Genera el dataset con ayuda de 500 USD en créditos de la API de Cohere! Recomendamos filtrar y extender el dataset de preferencias v0 generado en común en la Arena: [somosnlp-hackathon/dataset-preferencias-dpo-v0](https://huggingface.co/datasets/somosnlp-hackathon/dataset-preferencias-dpo-v0)
- Entrena tu modelo directamente en JupyterLab en el hub de Hugging Face, ¡tenemos GPUs patrocinadas por 🤗! 
- Sube el modelo(s) junto con todos los notebooks utilizados a hf.co/somosnlp-hackathon
- Escribe la [Model Card](https://huggingface.co/spaces/huggingface/Model_Cards_Writing_Tool), incluye enlaces al dataset y los notebooks utilizados (e.g. preprocesamiento, entrenamiento)

---

## Guía

### ✅ Preparación

<details>
<summary>Requisitos por equipo</summary>

1. Contribuir 100 prompts **de calidad** al dataset de [preferencias](https://somosnlp.org/hackathon/retos/preferencias)
2. Responder 200 preguntas del dataset de evaluación ([BLEND](https://somosnlp.org/hackathon/retos/blend))
3. Pedir los 500 USD créditos de la API de Cohere (tras completar los puntos 1 y 2, mencionar a @mariagrandury en el canal de vuestro equipo para instrucciones)
4. Crear en la organización hf.co/somosnlp-hackathon un Space con la plantilla de [jupyterlab](https://huggingface.co/docs/hub/spaces-sdks-docker-jupyter)
5. Completar el [formulario de registro](https://forms.gle/mLKEURUXGiNhq31T9)

</details>

### 📚 Dataset

Los datos son lo más importante en el desarrollo de un modelo y también le daremos mayor importancia a la hora de evaluar los proyectos 👀

- Genera un dataset para tu proyecto:
    - Toma como versión inicial para tu dataset el generado en común en la Arena: [somosnlp-hackathon/dataset-preferencias-dpo-v0](https://huggingface.co/datasets/somosnlp-hackathon/dataset-preferencias-dpo-v0)
    - Aprovecha los 500 USD de créditos de la API de Cohere que tiene cada equipo para filtrarlo, mejorarlo y extenderlo con más prompts y respuestas específicamente diseñados para tu caso de uso
    - Ten en cuenta que tratándose de temas culturales, es muy importante que todo lo que se genere sintéticamente sea revisado por una persona (podéis utilizar [Argilla](https://huggingface.co/docs/hub/en/datasets-argilla))
- Sube el dataset a hf.co/somosnlp-hackathon e itera
- Sube al repo del dataset todos los notebooks y scripts utilizados para generar el dataset y procesarlo
    - Si prefieres crear un repo en GitHub con todo el código, puedes hacerlo, no olvides de incluir un enlace en la Dataset Card
- Cumplimenta **bien** la Dataset Card
    - "Dataset Card" es el nombre de la documentación en los datasets de Hugging Face, es el README.md del repositorio de los datasets
    - OJO: Se tiene en cuenta para la evaluación del proyecto
    - Incluye en la introducción la motivación del proyecto e impacto
    - Detalla el proceso de generación y procesamiento, incluye las librerías utilizadas y menciona las pruebas hechas, incluye los enlaces al código
    - Especifica la licencia: a poder ser `apache-2.0`, si no, explica por qué
    - Evalúa los sesgos del dataset, si está balanceado, qué variedades del lenguaje u opiniones representa, etc.

Cómo nombrar los datasets:
- El nombre del dataset con los (mínimo 100) prompts que enviasteis al LLM Arena debe contener `prompt`. Por ejemplo: `normas_culturales_colombia_prompts`
- El nombre de los datasets de preferencias deben contener el nombre del algoritmo principal para el que se pueden utilizar (`dpo` o `kto`). Por ejemplo: `normas_culturales_colombia_dpo`
- Si el dataset es multimodal, debe contener `image`. Por ejemplo: `utensilios_ecuador_images_kto`

### ⚙️ Modelo

1. Crear en la organización hf.co/somosnlp-hackathon un Space con la plantilla de [JupyterLab](https://huggingface.co/docs/hub/spaces-sdks-docker-jupyter)
2. El equipo de Hugging Face le asignará un grant de una *L40S* al Space
    - Configura el tiempo de "auto-sleep" a 5 minutos para asegurar un uso responsable 🌱 
3. Diseña el notebook de entrenamiento
    - Guarda el modelo resultante directamente en hf.co/somosnlp-hackathon
    - Utiliza la librería CodeCarbon para evaluar el impacto climático
4. Haz pruebas con modelos pequeños y subconjuntos del dataset para verificar que el código es correcto y no encontrar bugs después de varias horas de entrenamiento.
5. Lanza el entrenamiento, revisa los resultados e itera
    - Puedes probar e.g. diferentes algoritmos o modelos base
    - No hace falta que crees un repo diferente para cada modelo, si haces push a un mismo repo, el modelo actualizado se guardará como un nuevo commit (al que puedes enlazar desde la Model Card si quieres)
6. **Descarga los notebooks de procesamiento del dataset y entrenamiento del modelo, súbelos al repo del modelo** (MUY IMPORTANTE) y elimina el Space de JupyterLab
7. Cumplimenta **bien** la Model Card
    - "Model Card" es el nombre de la documentación en los modelos de Hugging Face, es el README.md del repositorio de los modelos
    - OJO: Se tiene en cuenta para la evaluación del proyecto
    - Recomendación: Vete describiendo las pruebas según las haces, así como el proceso de mejora del dataset y entrenamiento del modelos
    - Incluye en la introducción la motivación del proyecto e impacto
    - Detalla el proceso de entrenamiento, incluye las librerías utilizadas y menciona las pruebas hechas, incluye los enlaces al código
    - Especifica la licencia: a poder ser `apache-2.0`, si no, explica por qué
    - Evalúa los sesgos del modelo
    - Evalúa el impacto ambiental

---

## Recursos

A continuación compartimos un montón de recursos para que podáis desarrollar proyectos de gran calidad. Los recursos marcados con ⭐ corresponden a charlas y talleres impartidas durante el hackathon y pensados específicamente para ayudaros en esta edición.

### 📚 Dataset

La API de Cohere:
- ⭐ [Taller práctico: Cómo utilizar la API de Cohere](https://www.youtube.com/watch?v=S_Wky6D9Nf0&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) impartido por Alejandro Rodriguez, Research Engineer en Cohere. Utilizad los modelos de Cohere para limpiar y extender vuestro dataset.

Creación de datasets:
- ⭐ [Red Teaming para modelos de lenguaje](https://www.youtube.com/watch?v=pGOXE4rrO9M&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6), impartido por Luis Vasquez, del equipo de Reinforcement Learning, Alignment & Red Teaming del Barcelona Supercomputing Center.
- ⭐ [MuSeD: Creación de un corpus multimodal en español para la detección de sexismo en vídeos de redes sociales](https://www.youtube.com/watch?v=w1ikWRaBQd0&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6), impartida por Laura De Grazia de la Universitat de Barcelona.
- [Cómo anotar corpus lingüísticos para entrenar LLMs](https://www.youtube.com/watch?v=d6vrflcIY-g&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J), impartida por Marta Guerrero @IIC, co-creadora de 3 de los corpus que forman La Leaderboard.
- [Distilabel y Argilla, herramientas para crear modelos como Notus](https://www.youtube.com/watch?v=riM3pgV4m_I&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J) impartido por Gabriel Martín, MLE @Argilla (notebook disponible).

Inspiración:
- ⭐ [Describing and interpreting interaction using cultural scripts](https://www.youtube.com/watch?v=jLh9Wyn7qcI&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6), charla impartida en inglés por Lauren Sadow de la Aarhus University.
- ⭐ [Expresando incertidumbre en tareas multilingües](https://www.youtube.com/watch?v=TC9tOEyPqy8&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) impartida por Selene Báez, investigadora postdoctoral en la University of Zurich.
- [Ética ambiental en IA: construyendo narrativas sostenibles en español](https://www.youtube.com/watch?v=MJLdrXz6bSE&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J), charla impartida por Jorge Vallego, Project Lead @H4rmony. Os puede servir para darle un enfoque eco-consciente a vuestro dataset.

### ⚙️ Modelo

Creación del Space de entrenamiento:
- [Docs: Jupyterlab en Spaces](https://huggingface.co/docs/hub/en/spaces-sdks-docker-jupyter#jupyterlab-on-spaces), donde podéis correr vuestros notebooks como siempre. OJO a perder el almacenamiento al reiniciar el Space, ¡guardad los notebooks!
<!--
- [Docs: AutoTrain (inglés)](https://huggingface.co/docs/autotrain/llm_finetuning), os animamos a probar esta plataforma no-code de Hugging Face. Vamos a traducir esta sección de la documentación, avisadnos si necesitáis ayuda para comprenderla.
- [Tutorial: AutoTrain + spacerunner (inglés)](https://huggingface.co/blog/stefan-it/autotrain-flair-mobie), con esta combinación podéis correr scripts en AutoTrain.
-->

Alineamiento de LLMs:
- ⭐ [Taller práctico: Alineación de LLMs usando Aprendizaje por Refuerzo](https://www.youtube.com/watch?v=wI6yjbed_1Q&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) impartido por Luis Vasquez, del equipo de Reinforcement Learning, Alignment & Red Teaming del Barcelona Supercomputing Center.

Modelos multimodales:
- ⭐ [Charla: Cómo hacer un Modelo Visión-Lenguaje eficiente](https://www.youtube.com/watch?v=PjOXDCe_3kg&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) impartida por Andrés Marafioti, ML Engineer en Hugging Face y creador de SmolVLM.
- ⭐ [Charla: Instruction Tuning para Razonamiento Secuencial Multimodal](https://www.youtube.com/watch?v=xiAfa6rafRs&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) impartida por Danae Sanchez investigadora postdoctoral en la Universidad de Copenhagen.

Fine-tuning de LLMs:
- [Taller práctico: El impacto de la calidad de los datos en un FT de LLMs](https://www.youtube.com/watch?v=hPq5NG8kA8w&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J), impartido también por Manu Romero, creador de +500 modelos del Hub de Hugging Face.
- [Taller práctico: Fine-tuning de grandes modelos de lenguaje](https://somosnlp.org/hackathon-2023/fine-tuning-llms) impartido por Manu Romero, creador de +500 modelos del Hub de Hugging Face.
- [Taller + AMA sobre entrenamiento de LLMs](https://www.youtube.com/playlist?list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J) con Alejandro Vaca, fundador de LenguajeNaturalAI.
- Notebooks de `unsloth` para entrenar más rápido (en inglés, si necesitáis que los traduzcamos avisadnos):
[Gemma FT en dataset de instrucciones estilo Alpaca](https://colab.research.google.com/drive/10NbwlsRChbma1v55m8LAPYG15uQv6HLo) y
[Hacer RLAIF via DPO sobre Zephir](https://colab.research.google.com/drive/15vttTpzzVXv_tJwEk-hIcQ0S9FcEWvwP).

Impacto climático:
- Para evaluar la huella de carbono del entrenamiento de tu modelo puedes utilizar herramientas como [Code Carbon](https://codecarbon.io) (mejor, integrada en 🤗 Transformers) o [ML CO2 Impact](https://mlco2.github.io/impact).
- Te recomendamos este [vídeo](https://www.youtube.com/watch?v=ftWlj4FBHTg) de motivación, este [artículo](https://huggingface.co/blog/carbon-emissions-on-the-hub) del blog de HF y la sección de la [documentación](https://huggingface.co/docs/hub/model-cards-co2) de 🤗 Transformers que trata este tema.

### 📝 Documentación

- [Docs: cómo escribir una buena Dataset Card](https://huggingface.co/docs/datasets/dataset_card): es la documentación oficial de Hugging Face, incluye una plantilla y un par de buenos ejemplos.
- [Docs: cómo escribir una Model Card](https://huggingface.co/docs/hub/model-cards): guía oficial de Hugging Face, incluye un enlace al Space para crearla automáticamente y una explicación de cada sección.
- [Space: Model Card Creator](https://huggingface.co/spaces/huggingface/Model_Cards_Writing_Tool), Space que os guía en la creación de vuestra model card.
- [Detección y mitigación de sesgos en modelos de lenguaje](https://somosnlp.org/hackathon-2023/evaluacion-de-sesgos), charla impartida por María Grandury, fundadora de SomosNLP.

<center style="margin-top:40px;"><a href="https://somosnlp.org/hackathon/retos" target="_blank" style="background-color:gray; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Volver a los retos</a></center>
