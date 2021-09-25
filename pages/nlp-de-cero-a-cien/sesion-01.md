---
title: "Sesión 1: Introducción al NLP y Word Embeddings"
date: 2021-07-13T16:00:00.000+00:00
lang: es
duration: 42min
---

<div>
    <CourseSummary
        description="Tras una introducción al Procesamiento de Lenguaje Natural, veremos cómo funcionan los Word Embeddings y Word2Vec, así como sus posibles usos y sesgos."
        video="https://www.youtube.com/embed/RunqyndjEbg"
        slides="https://github.com/nlp-en-es/nlp-de-cero-a-cien/blob/main/1_word_embeddings/presentacion.pdf"
        name="Omar Sanseviero"
        twitter="https://twitter.com/osanseviero"
        linkedin="https://www.linkedin.com/in/omarsanseviero/"
        github="https://github.com/osanseviero"
    />
</div>

---

En esta primera sesión el tema es Word Embeddings, un concepto fundamental del Procesamiento del Lenguaje Natural. Aquí les compartimos recursos adicionales así como publicaciones por si les interesa profundizar en el tema. Así mismo, hay un cuaderno de colab con ejercicios para que puedan entender mejor el concepto.

## Recursos adicionales

* https://jalammar.github.io/illustrated-Word2Vec/: guía ilustrada que explica de manera muy intuitiva los conceptos de Word2Vec.
* https://lena-voita.github.io/nlp_course/word_embeddings.html: explicación de Word Embeddings y contiene tanto publicaciones como preguntas para hacer reflexión adicional.
* [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/): capítulo 6, secciones 3-8.

## Papers

* [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781): paper original de Word2Vec.
* [Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings](https://papers.nips.cc/paper/2016/file/a486cd07e4ac3d270571622f4f316ec5-Paper.pdf): paper donde se discuten los sesgos que pueden existir en los embeddings.

## Ejercicios: Word2Vec con Gensim

<a href="https://colab.research.google.com/github/nlp-en-es/nlp-de-cero-a-cien/blob/main/1_word_embeddings/Word2Vec.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

En este cuaderno de Jupyter vas a utilizar la biblioteca [Gensim](https://radimrehurek.com/gensim/index.html) para experimentar con Word2Vec. Este cuaderno está enfocado en la intuición de los conceptos y no en los detalles de implementación. Este cuaderno está inspirado en esta [guía](https://radimrehurek.com/gensim/auto_examples/tutorials/run_Word2Vec.html).


### 1. Instalación y cargar el modelo


```python
!pip install --upgrade gensim
```


```python
import gensim.downloader as api

model = api.load('Word2Vec-google-news-300')
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

1. Usa el modelo Word2Vec para hacer un ranking de las siguientes 15 palabras según su similitud con las palabras "man" y "woman". Para cada par, imprime su similitud.


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

#### 3. Ahora completa las analogías usando un modelo Word2Vec

Aquí hay un ejemplo de cómo hacerlo. Puedes resolver analogías como "A es a B como C es a _" haciendo A + C - B.


```python
# man is to woman as king is to ___?
model.most_similar(positive=["king", "woman"], negative=["man"], topn=1)
```


```python
# us is to burger as italy is to ___?
model.most_similar(positive=["Mexico", "burger"], negative=["USA"], topn=1)
```

## Impartido por Omar Sanseviero

Omar es un Ingeniero de Machine Learning con 7 años de experiencia en la industria de la tecnología. Actualmente trabaja en Hugging Face en el equipo de open-source democratizando el uso de Machine Learning. Previamente, Omar trabajó como Ingeniero de Software en Google en Suiza en el equipo de Assistant. Omar es un apasionado de la educación y co-fundó AI Learners, una comunidad de personas que buscan aprender y discutir temas sobre Inteligencia Artificial y sus diferentes aplicaciones.
