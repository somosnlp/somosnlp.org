---
title: Selección de artículos II (Dic 2024)
description: Selección de artículos relevantes para la comunidad hispanohablante.
date: 2024-12-3T12:00:00.000+00:00
lang: es
duration: 4min
cover: /images/blog/seleccion_articulos.png
author: Gonzalo Martínez, PhD
bio: Investigador de PLN @UC3M
scholar: https://scholar.google.com/citations?user=FF6Yw5QAAAAJ
---

¡Hola de nuevo, bienvenidos a la segunda edición de resúmenes de artículos de SomosNLP! 

Sabemos que es casi imposible mantenerse al día con todas las novedades en el mundo del NLP en español, así que aquí estamos para compartir contigo los papers más interesantes. Si tienes alguna sugerencia o quieres que comentemos tu trabajo, ¡escríbenos a info@somosnlp.com!

En esta edición nos hemos centrado en los artículos sobre español de la conferencia EMNLP, ¡una de las más importantes de NLP en todo el mundo!


<div class="flex justify-center">
    <img src="/images/blog/seleccion_articulos_laura_rdgz.png" alt="Selección de artículos" width="400">
</div>

## 🔍 Simplificación Léxica en Español y Catalán: Dos nuevos Corpus

*Lexical Complexity Prediction and Lexical Simplification for Catalan and Spanish: Resource Creation, Quality Assessment, and Ethical Considerationss*

Paper: https://aclanthology.org/2024.tsar-1.9/

Los autores presentan dos nuevos conjuntos de datos para la simplificación léxica y la predicción de complejidad léxica en español y catalán.  Esta tarea consiste en remplazar las más palabras complejas de un texto por otras más simples y fáciles de entender. Así personas con problemas cognitivos o que están aprendiendo el idioma, pueden acceder a él y disfrutarlo. Por desgracia, no existen muchos recursos en español ni en catalán, en comparación a los que existen en inglés. Gracias a estos autores se podrá avanzar en los estudios de esta área en nuestros idiomas.  El datasets en español consta de 625 palabras en 210 contextos distintos obtenidas de textos educativos sobre finanzas, mientras que el dataset en catalán tiene 475 palabras objetivo en 160 contextos de noticias educativas. 

## 💟 Más Allá de las Emociones Básicas: Identificación de Estados Afectivos

*MASIVE: Open-Ended Affective State Identification in English and Spanish*

Paper: https://aclanthology.org/2024.emnlp-main.1139/

El Análisis de sentimientos se ha centrado en emociones básicas como tristeza, alegría, etc. Sin embargo, en la vida real utilizamos emociones más específicas y hasta coloquiales: cagado, flipando, tusa. Para estudiarlo, los autores presentan MASSIVE, un corpus de estas emociones en inglés y Español. Este ha sido creado a partir de publicaciones de Reddit. El conjunto de datos en español tiene una gran variedad de etiquetas de estados afectivos, incluidos términos específicos de dialectos regionales del español, siendo un recurso muy valioso para estudiar variaciones dialectales en la expresión emocional.

## 📰 Traducción de Asturiano: Caltengamos les nueses llingües!

*Enhaced Apertium System: Translation into Low-Resource Languages of Spain Spanish–Asturian*

Paper: https://aclanthology.org/2024.wmt-1.84/ 

Este artículo trata sobre las nuevas mejoras a Eslema, un sistema de traducción máquina Español-Asturiano basada en reglas Apertium. Detallan las dificultades de trabajar con el asturiano, una lengua de bajos recursos que carece de reconocimiento oficial en España. Esta falta de reconocimiento se traduce en una financiación y recursos limitados para el desarrollo de tecnologías lingüísticas, creando barreras para la presencia digital del asturiano y los esfuerzos de preservación lingüística. El artículo también discute el problema de las métricas de evaluación para lenguas de bajos recursos como el asturiano. Los autores argumentan que métricas estándar como BLEU, que dependen de coincidencias literales palabra por palabra, no siempre son apropiadas para evaluar la calidad de las traducciones en lenguas con datos limitados.

## 🩺 Reconocimiento de Entidades Médicas

*Few-shot clinical entity recognition in English, French and Spanish: masked language models outperform generative model prompting*

Paper: https://aclanthology.org/2024.findings-emnlp.400/

Este artículo investiga el rendimiento de varios modelos de lenguaje en tareas de Reconocimiento de Entidades Nombradas (NER) en textos clínicos en inglés, francés y español. El NER implica identificar y clasificar entidades nombradas, como condiciones médicas, síntomas o tratamientos, dentro del texto. Esta tarea es crucial para construir sistemas de extracción de información clínica, permitiendo el análisis automatizado de registros de pacientes y apoyando la toma de decisiones clínicas.

## 🤖 Creatividad Artificial: Comparando LLMs con Escritores Humanos

*Pron vs Prompt: Can Large Language Models already Challenge a World-Class Fiction Author at Creative Text Writing?*

Paper: https://aclanthology.org/2024.emnlp-main.1096/

¿Podía ganar ChatGPT a un experimentado novelista? 🤔 Este artículo examina las capacidades de escritura creativa de los LLMs comparándolas con el reconocido novelista español Patricio Pron.  Se enfocan en una tarea específica de escritura creativa: generar sinopsis cortas para títulos de películas imaginarias. De este modo pudieron hacer una comparación controlada de la creatividad humana y la máquina, en elementos como originalidad, atractivo y estructura narrativa. Los resultados muestran que GPT-4, aunque es capaz de generar textos coherentes y gramaticalmente correctos, no alcanza las habilidades de escritura creativa de Pron.

## 📚 Corpus Español para Traducción Automática: Diversidad Dialectal en SEED

*Spanish Corpus and Provenance with Computer-Aided Translation for the WMT24 OLDI Shared Task*

Paper: https://aclanthology.org/2024.wmt-1.50/ 

Este artículo detalla la creación de un nuevo corpus en español para el conjunto de datos SEED, un masivo conjunto de datos multilingüe para entrenar modelos de traducción automática. Los autores se enfocan en las variedades de español latinoamericano para alinearse con la cobertura lingüística del benchmark FLORES+, un conjunto de datos clave para lenguas de bajos recursos. Este enfoque resalta la importancia de representar la diversidad dialectal en los recursos lingüísticos, alejándose de un enfoque único para el español.

¡Hasta la próxima!
