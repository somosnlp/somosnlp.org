---
title: "Sesión 1: Word Embeddings"
date: 2021-07-13T16:00:00.000+00:00
lang: es
duration: 42min
cover: "https://nlp-en-es.github.io/assets/images/undraw_Online_learning_re_qw08.svg"
---

<iframe class="mx-auto my-8" width="560" height="315" src="https://www.youtube.com/embed/RunqyndjEbg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<div class="text-lg mb-8">
    Ponente:
    <a class="font-regular" href="https://twitter.com/osanseviero">@osanseviero</a>
</div>

# Recursos adicionales

## Word2vec con Gensim

<a href="https://colab.research.google.com/github/nlp-en-es/nlp-de-cero-a-cien/blob/main/1_word_embeddings/word2vec.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

En este cuaderno de Jupyter vas a utilizar la biblioteca [Gensim](https://radimrehurek.com/gensim/index.html) para experimentar con word2vec. Este cuaderno está enfocado en la intuición de los conceptos y no en los detalles de implementación. Este cuaderno está inspirado en esta [guía](https://radimrehurek.com/gensim/auto_examples/tutorials/run_word2vec.html).


### 1. Instalación y cargar el modelo


```python
!pip install --upgrade gensim
```


```python
import gensim.downloader as api

model = api.load('word2vec-google-news-300')
```

### 2. Similitud de palabras

En esta sección veremos cómo conseguir la similitud entre dos palabras utilizando un word embedding ya entrenado.


```python
model.similarity("king", "queen")
model.similarity("king", "man")
model.similarity("king", "potato")
model.similarity("king", "king")
```

Ahora veremos cómo encontrar las palabras con mayor similitud al conjunto de palabras especificado.


```python
model.most_similar(["king", "queen"], topn=5)
model.most_similar(["tomato", "carrot"], topn=5)
```

Pero incluso puedes hacer cosas interesantes como ver qué palabra no corresponde a una lista.


```python
model.doesnt_match(["summer", "fall", "spring", "air"])
```

### Ejercicios

1. Usa el modelo word2vec para hacer un ranking de las siguientes 15 palabras según su similitud con las palabras "man" y "woman". Para cada par, imprime su similitud.


```python
words = [
"wife",
"husband",
"child",
"queen",
"king",
"man",
"woman",
"birth",
"doctor",
"nurse",
"teacher",
"professor",
"engineer",
"scientist",
"president"]
```

#### 2. Completa las siguientes analogías por tu cuenta (sin usar el modelo)

1. king is to throne as judge is to _
1. giant is to dwarf as genius is to _
1. French is to France as Spaniard is to _
1. bad is to good as sad is to _
1. nurse is to hospital as teacher is to _
1. universe is to planet as house is to _

#### 3. Ahora completa las analogías usando un modelo word2vec

Aquí hay un ejemplo de cómo hacerlo. Puedes resolver analogías como "A es a B como C es a _" haciendo A + C - B.


```python
# man is to woman as king is to ___?
model.most_similar(positive=["king", "woman"], negative=["man"], topn=1)
```


```python
# us is to burger as italy is to ___?
model.most_similar(positive=["Mexico", "burger"], negative=["USA"], topn=1)
```
