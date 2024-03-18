---
title: Creando Narrativas Sostenibles en Español
description: Utilizando H4rmony, un dataset de preferencia ecológica 
date: 2024-03-17T16:00:00.000+00:00
lang: es
duration: 5min
cover: https://github.com/Neovalle/H4rmony/blob/main/data/H4RMONY%20logo.png
author: Jorge Vallego
bio: Consultor en Ingenieria de Datos y AI - Investigador Independiente
HuggingFace: https://huggingface.co/datasets/neovalle/H4rmony
linkedin: linkedin.com/in/jorge-vallego-391838a6
---

Durante una de las [keynotes del Hackathon #Somos600M](https://www.youtube.com/watch?v=MJLdrXz6bSE&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J), hablamos de la importancia del lenguaje en nuestra relación con el medioambiente y de cómo podemos hacer que las narrativas y discursos de los grandes modelos de lenguaje mejoren en ese sentido.

Esto sería algo particularmente interesante de aplicar y desarrollar durante la creación del gran corpus en español, en todas las fases de entrenamiento de LLMs y por qué no, también creando una nueva métrica ecológica en el leaderboard en español. En términos de entrenamiento ofrecemos un punto de partida, que ya ha sido probado en inglés, el dataset [H4rmony](https://huggingface.co/datasets/neovalle/H4rmony).

Este dataset ha sido creado como parte del H4rmony project, cuyo objetivo es mejorar la eco-narrativa de los modelos de lenguaje promoviendo un discurso sostenible, impulsando el ecocentrismo sobre el antropocentrismo. Es un dataset de preferencias que hemos creado usando principios ecolingüísticos y usado exitosamente en pruebas de concepto que nos han permitido alinear modelos abiertos con valores ecológicos. Lo hemos probado en entrenamientos con diferentes metodologías, en fine-tuning por instrucción, y en aprendizaje reforzado, tanto a través de modelos de recompensa como por DPO, siendo este último el que nos resultó más eficiente considerando tiempo de GPU, simplicidad de código y resultados finales.

Acerca de los resultados obtenidos destacamos también una inicial evaluación en la que podemos observar transferencia interlingüística, esto es que, si bien ajustamos un modelo usando un dataset 100% en inglés, el modelo resultante no sólo alcanza una narrativa más sostenible en inglés, sino también en italiano, que fue el segundo idioma que evaluamos.

Teniendo en cuenta estas observaciones proponemos utilizar el dataset H4rmony con el fin de mejorar la narrativa ecológica de modelos en español, por ejemplo:

- En su estado actual, a través DPO, si el modelo base es multilingüe, dada la transferencia interlingüística mencionada.
- Traduciéndolo al español y aplicándolo al modelo base en español, lo cual lógicamente dará mejores resultados que el caso anterior.
- Extendiéndolo con nuevas entradas en español antes de aplicarlo por DPO.
- Combinando las dos anteriores, lo cual si bien es más trabajoso, dará los mejores resultados.
 
### Cómo ajustar un modelo con el dataset H4rmony

Como dicho anteriormente recomendamos usar DPO porque es lo que nos ha resultado mejor, pero eso no quita explorar otros métodos que han aparecido más recientemente como KTO y IPO. Compartimos un excelente [artículo](https://huggingface.co/blog/pref-tuning) del blog de Hugging Face acerca de los métodos de entrenamiento por dataset de preferencia.

Un ejemplo concreto de cómo hacer el fine-tuning usando H4rmony puede encontrarse en [este notebook](https://github.com/Neovalle/H4rmony/blob/main/Fine_tune_with_H4rmony_and_DPO.ipynb), recuerda que dependiendo del modelo base debes cambiar algunas constantes, las capas que van a ser ajustadas y posiblemente tengas que probar con diferentes hiperparámetros.

### Cómo traducir y extender el dataset H4rmony

El dataset H4rmony fue creado con tres respuestas por cada prompt, una mejor, otra ambivalente y una peor. Esas respuestas fueron puestas en pares, mejor/ambivalente, ambivalente/peor y mejor/peor. Esto se hace para lograr una mejor generalización durante el aprendizaje reforzado, pero esto significa que hay mucha redundancia de texto en el dataset que no necesitamos a la hora de traducir; si queremos eliminar esas redundancias para hacer más eficiente la traducción, lo ideal es volver el dataset a prompt únicos con sus tres respectivas respuestas.

En [este notebook](https://github.com/Neovalle/H4rmony/blob/main/Imploding_and_Exploding_H4rmony_dataset.ipynb) tienes el código para hacer esa implosión, y también el código para que una vez traducido volver a poner los prompts por pares.

También puedes usar sólo la segunda parte del notebook si quieres crear un dataset con nuevos prompts con tres respuestas cada uno, y luego poner las respuestas por pares.

En ambos casos te recomendamos agregar tantos metadatos en el dataset como puedas, ya que estos son muy importantes para mantener la calidad del dataset y poder subdividirlo, agregar, categorizar, balancear, etc. Si quieres algunos ejemplos de los metadatos que podrías incluir, mira el dataset card de [H4rmony](https://huggingface.co/datasets/neovalle/H4rmony) en Hugging Face.

En el caso que quieras agregar nuevos prompts y respuestas, y quieras aliviar el trabajo de anotación, puedes usar un modelo con roles adversarios para las respuestas de forma de ya saber por anticipado cuál de ellas será la respuesta preferida, y así la anotación se reduce simplemente a una verificación. También puedes ver en el dataset card de H4rmony más detalles sobre esta variación de RLHF que hemos utilizado en nuestro proyecto.

### ¿Podremos crear una métrica de evaluación ecológica?

Aquí dejamos una pregunta abierta ya que generar un score por similaridad semántica parece que no sería muy confiable en este caso ya que nos interesa saber que tan alineado ecológicamente es un modelo independientemente de las palabras y frases usadas en la repuesta. Lo que hemos pensado en los brainstormings del H4rmony project es que tal vez podríamos instruir un modelo para hacer la evaluación del grado de alineación ecológica y la sostenibilidad. Por ejemplo, presentarle a ese asistente instruido con principios ecolingüísticos las respuestas que dio un modelo X a los prompts del H4rmony dataset, y que las califique como buena, regular o mala, y luego cuantificar para darle un score total al modelo. 

¿Qué opinas? ¿Tienes alguna idea que quieras compartir? 
