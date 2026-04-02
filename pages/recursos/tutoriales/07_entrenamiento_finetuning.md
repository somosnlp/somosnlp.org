---
title: Fine-tuning un modelo pre-entrenado
description: Cómo aplicar fine-tuning a un modelo pre-entrenado.
cover: /images/ilustraciones/undraw_education_edited.svg
author: Yhary Arias
bio: Estudiante de maestría en IA de la Universidad Politécnica de Valencia, España.
website: https://www.linkedin.com/in/yharyarias/
twitter: https://twitter.com/yharyarias5
github: https://github.com/yharyarias
---

Esta una traducción hecha de la [documentación de Transformers](https://huggingface.co/docs/transformers/training).

## Acerca de este tutorial

**Duración:** 20 a 40 minutos

**Objetivo**: Aprender a aplicar Fine-Tuning a un modelo pre-entrenado, desde la preparación del dataset hasta el proceso de evaluación de nuestro entrenamiento.

**Metas de aprendizaje:**

- Conocer las ventajas de usar modelos pre-entrenados.
- Aprender una de las formas más efecientes de preparar nuestro dataset.
- Aprender a configurar de manera optima y efectiva nuestros hiperparametro para el proceso de entrenamiento.
- Probar y experimentar diferentes configuraciones para los argumentos de nuestra función de entrenamiento.
- Evaluar el proceso de entrenamiento.

**Formato:** Laboratorio corto o para llevar a casa

**Público:** Estudiantes de diferentes niveles con interés en usar modelos existentes o compartir los suyos.

**Requisitos previos:**

- Comprensión de Machine Learning.
- (Opcional, pero recomendado) Experiencia con Git ([recurso](https://learngitbranching.js.org/)).


# Fine-tuning a un modelo pre-entrenado

El uso de un modelo pre-entrenado tiene importantes ventajas. Reduce los costos de computación, la huella de carbono, y te permite utilizar modelos de última generación sin tener que entrenar uno desde cero. 🤗 Transformers proporciona acceso a miles de modelos pre-entrenados en una amplia gama de tareas. Cuando utilizas un modelo pre-entrenado, lo entrenas con un dataset específico para tu tarea. Esto se conoce como fine-tuning, una técnica de entrenamiento increíblemente poderosa. En este tutorial haremos fine-tuning a un modelo pre-entrenado con un framework de Deep Learning de tu elección:

* Fine-tuning a un modelo pre-entrenado con 🤗 Transformers [Trainer](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/trainer#transformers.Trainer).
* Fine-tuning a un modelo pre-entrenado en TensorFlow con Keras.
* Fine-tuning a un modelo pre-entrenado en PyTorch nativo.


## Prepara un dataset


Antes de aplicar fine-tuning a un modelo pre-entrenado, descarga un dataset y prepáralo para el entrenamiento. El tutorial anterior nos enseñó cómo procesar los datos para el entrenamiento, y ahora es la oportunidad de poner a prueba estas habilidades.

Comienza cargando el dataset de [Yelp Reviews](https://huggingface.co/datasets/yelp_review_full):

```python
from datasets import load_dataset

dataset = load_dataset("yelp_review_full")
dataset[100]
{'label': 0,
 'text': 'My expectations for McDonalds are t rarely high. But for one to still fail so spectacularly...that takes something special!\\nThe cashier took my friends\'s order, then promptly ignored me. I had to force myself in front of a cashier who opened his register to wait on the person BEHIND me. I waited over five minutes for a gigantic order that included precisely one kid\'s meal. After watching two people who ordered after me be handed their food, I asked where mine was. The manager started yelling at the cashiers for \\"serving off their orders\\" when they didn\'t have their food. But neither cashier was anywhere near those controls, and the manager was the one serving food to customers and clearing the boards.\\nThe manager was rude when giving me my order. She didn\'t make sure that I had everything ON MY RECEIPT, and never even had the decency to apologize that I felt I was getting poor service.\\nI\'ve eaten at various McDonalds restaurants for over 30 years. I\'ve worked at more than one location. I expect bad days, bad moods, and the occasional mistake. But I have yet to have a decent experience at this store. It will remain a place I avoid unless someone in my party needs to avoid illness from low blood sugar. Perhaps I should go back to the racially biased service of Steak n Shake instead!'}
```

Como ya sabes, necesitas un tokenizador para procesar el texto e incluir una estrategia para el padding y el truncamiento, para manejar cualquier longitud de secuencia variable. Para procesar tu dataset en un solo paso, utiliza el método de 🤗 Datasets [map](https://huggingface.co/docs/datasets/process.html#map) para aplicar una función de preprocesamiento sobre todo el dataset:

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")


def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)


tokenized_datasets = dataset.map(tokenize_function, batched=True)
```

Si lo deseas, puedes crear un subconjunto más pequeño del dataset completo para aplicarle fine-tuning y así reducir el tiempo.

```python
small_train_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(1000))
small_eval_dataset = tokenized_datasets["test"].shuffle(seed=42).select(range(1000))
```


## Fine-tuning con `Trainer`


🤗 Transformers proporciona una clase [Trainer](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/trainer#transformers.Trainer) optimizada para el entrenamiento de modelos de 🤗 Transformers, haciendo más fácil el inicio del entrenamiento sin necesidad de escribir manualmente tu propio ciclo. La API del [Trainer](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/trainer#transformers.Trainer) soporta una amplia gama de opciones de entrenamiento y características como el logging, el gradient accumulation y el mixed precision.

Comienza cargando tu modelo y especifica el número de labels previstas. A partir del [Card Dataset](https://huggingface.co/datasets/yelp_review_full#data-fields) de Yelp Review, que como ya sabemos tiene 5 labels:

```python
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased", num_labels=5)
```

Tip: Verás una advertencia acerca de que algunos de los pesos pre-entrenados que no están siendo utilizados y que algunos pesos están siendo inicializados al azar. 
No te preocupes, esto es completamente normal. El head/cabezal pre-entrenado del modelo BERT se descarta y se sustituye por un head de clasificación inicializado aleatoriamente. Puedes aplicar fine-tuning a este nuevo head del modelo en tu tarea de clasificación de secuencias haciendo transfer learning del modelo pre-entrenado.

### Hiperparámetros de entrenamiento

A continuación, crea una clase [TrainingArguments](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/trainer#transformers.TrainingArguments) que contenga todos los hiperparámetros que puedes ajustar así como los indicadores para activar las diferentes opciones de entrenamiento. Para este tutorial puedes empezar con los [hiperparámetros](https://huggingface.co/docs/transformers/main_classes/trainer#transformers.TrainingArguments) de entrenamiento por defecto, pero siéntete libre de experimentar con ellos para encontrar tu configuración óptima.

Especifica dónde vas a guardar los checkpoints de tu entrenamiento:

```python
from transformers import TrainingArguments

training_args = TrainingArguments(output_dir="test_trainer")
```

### Métricas

El [Trainer](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/trainer#transformers.Trainer) no evalúa automáticamente el rendimiento del modelo durante el entrenamiento. Tendrás que pasarle a [Trainer](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/trainer#transformers.Trainer) una función para calcular y hacer un reporte de las métricas. La librería de 🤗 Datasets proporciona una función de [accuracy](https://huggingface.co/metrics/accuracy) simple que puedes cargar con la función `load_metric` (ver este [tutorial](https://huggingface.co/docs/datasets/metrics.html) para más información):

```python
import numpy as np
from datasets import load_metric

metric = load_metric("accuracy")
```

Define la función `compute` en `metric` para calcular el accuracy de tus predicciones. Antes de pasar tus predicciones a `compute`, necesitas convertir las predicciones a logits (recuerda que todos los modelos de 🤗 Transformers devuelven logits).

```python
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)
```

Si quieres controlar tus métricas de evaluación durante el fine-tuning, especifica el parámetro `evaluation_strategy` en tus argumentos de entrenamiento para que el modelo tenga en cuenta la métrica de evaluación al final de cada época:

```python
from transformers import TrainingArguments

training_args = TrainingArguments(output_dir="test_trainer", evaluation_strategy="epoch")
```

### Trainer

Crea un objeto [Trainer](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/trainer#transformers.Trainer) con tu modelo, argumentos de entrenamiento, conjuntos de datos de entrenamiento y de prueba, y tu función de evaluación:

```python
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=small_train_dataset,
    eval_dataset=small_eval_dataset,
    compute_metrics=compute_metrics,
)
```

A continuación, aplica fine-tuning a tu modelo llamando [~transformers.Trainer.train](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/trainer#transformers.Trainer.train):

```python
trainer.train()
```

## Fine-tuning con Keras


Los modelos de 🤗 Transformers también permite realizar el entrenamiento en TensorFlow con la API de Keras. Sólo es necesario hacer algunos cambios antes de hacer fine-tuning.

### Convierte el dataset al formato de TensorFlow

El [DefaultDataCollator](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/data_collator#transformers.DataCollatorWithPadding) junta los tensores en un batch para que el modelo se entrene en él. Asegúrate de especificar `return_tensors` para devolver los tensores de TensorFlow:

```python
from transformers import DefaultDataCollator

data_collator = DefaultDataCollator(return_tensors="tf")
```


Tip: [Trainer](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/trainer#transformers.Trainer) utiliza [DataCollatorWithPadding](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/data_collator#transformers.DataCollatorWithPadding) por defecto por lo que no es necesario especificar explícitamente un intercalador de datos (data collator, en inglés).


A continuación, convierte los datasets tokenizados en datasets de TensorFlow con el método [to_tf_dataset](https://huggingface.co/docs/datasets/package_reference/main_classes.html#datasets.Dataset.to_tf_dataset). Especifica tus entradas en `columns` y tu etiqueta en `label_cols`:

```python
tf_train_dataset = small_train_dataset.to_tf_dataset(
    columns=["attention_mask", "input_ids", "token_type_ids"],
    label_cols=["labels"],
    shuffle=True,
    collate_fn=data_collator,
    batch_size=8,
)

tf_validation_dataset = small_eval_dataset.to_tf_dataset(
    columns=["attention_mask", "input_ids", "token_type_ids"],
    label_cols=["labels"],
    shuffle=False,
    collate_fn=data_collator,
    batch_size=8,
)
```

### Compila y ajusta

Carguemos un modelo TensorFlow con el número esperado de labels:

```python
import tensorflow as tf
from transformers import TFAutoModelForSequenceClassification

model = TFAutoModelForSequenceClassification.from_pretrained("bert-base-cased", num_labels=5)
```

A continuación, compila y aplica fine-tuning a tu modelo con [fit](https://keras.io/api/models/model_training_apis/) como lo harías con cualquier otro modelo de Keras:

```python
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=5e-5),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=tf.metrics.SparseCategoricalAccuracy(),
)

model.fit(tf_train_dataset, validation_data=tf_validation_dataset, epochs=3)
```


## Fine-tune en PyTorch nativo


El [Trainer](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/trainer#transformers.Trainer) se encarga del ciclo de entrenamiento y permite aplicar fine-tuning a un modelo en una sola línea de código. Para los usuarios que prefieren escribir tu propio ciclo de entrenamiento, también puedes aplicar fine-tuning a un modelo de 🤗 Transformers en PyTorch nativo.

En este punto, es posible que necesites reiniciar tu notebook o ejecutar el siguiente código para liberar algo de memoria:

```python
del model
del pytorch_model
del trainer
torch.cuda.empty_cache()
```

A continuación, haremos un post-proceso manualmente al `tokenized_dataset` y así prepararlo para el entrenamiento.

1. Elimina la columna de `text` porque el modelo no acepta texto en crudo como entrada:

    ```python
    tokenized_datasets = tokenized_datasets.remove_columns(["text"])
    ```

2. Cambia el nombre de la columna de `label` a `labels` porque el modelo espera que el argumento se llame `labels`:

    ```python
    tokenized_datasets = tokenized_datasets.rename_column("label", "labels")
    ```

3. Establece el formato del dataset para devolver tensores PyTorch en lugar de listas:

    ```python
    tokenized_datasets.set_format("torch")
    ```

A continuación, crea un subconjunto más pequeño del dataset, como se ha mostrado anteriormente, para acelerar el fine-tuning:

```python
small_train_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(1000))
small_eval_dataset = tokenized_datasets["test"].shuffle(seed=42).select(range(1000))
```

### DataLoader

Crea un `DataLoader` para tus datasets de entrenamiento y de prueba para poder iterar sobre batches de datos:

```python
from torch.utils.data import DataLoader

train_dataloader = DataLoader(small_train_dataset, shuffle=True, batch_size=8)
eval_dataloader = DataLoader(small_eval_dataset, batch_size=8)
```

Carga tu modelo con el número de labels previstas:

```python
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased", num_labels=5)
```

### Optimiza y progrma el learning rate

Crea un optimizador y el learning rate para aplicar fine-tuning al modelo. Vamos a utilizar el optimizador [AdamW](https://pytorch.org/docs/stable/generated/torch.optim.AdamW.html) de PyTorch:

```python
from torch.optim import AdamW

optimizer = AdamW(model.parameters(), lr=5e-5)
```

Crea el learning rate desde el [Trainer](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/trainer#transformers.Trainer):

```python
from transformers import get_scheduler

num_epochs = 3
num_training_steps = num_epochs * len(train_dataloader)
lr_scheduler = get_scheduler(
    name="linear", optimizer=optimizer, num_warmup_steps=0, num_training_steps=num_training_steps
)
```

Por último, especifica el `device` o entorno de ejecución para utilizar una GPU si tienes acceso a una. De lo contrario, el entrenamiento en una CPU puede llevar varias horas en lugar de un par de minutos.

```python
import torch

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
model.to(device)
```


Tip: Consigue acceso gratuito a una GPU en la nube si es que no tienes este recurso de forma local con un notebook alojado en [Colaboratory](https://colab.research.google.com/) o [SageMaker StudioLab](https://studiolab.sagemaker.aws/).


Genial, ¡ahora estamos listos entrenar! 🥳

### Ciclo de entrenamiento

Para hacer un seguimiento al progreso del entrenamiento, utiliza la librería [tqdm](https://tqdm.github.io/) para añadir una barra de progreso sobre el número de pasos de entrenamiento:

```python
from tqdm.auto import tqdm

progress_bar = tqdm(range(num_training_steps))

model.train()
for epoch in range(num_epochs):
    for batch in train_dataloader:
        batch = {k: v.to(device) for k, v in batch.items()}
        outputs = model(**batch)
        loss = outputs.loss
        loss.backward()

        optimizer.step()
        lr_scheduler.step()
        optimizer.zero_grad()
        progress_bar.update(1)
```

### Métricas

De la misma manera que necesitas añadir una función de evaluación al [Trainer](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/trainer#transformers.Trainer), necesitas hacer lo mismo cuando escribas tu propio ciclo de entrenamiento. Pero en lugar de calcular y reportar la métrica al final de cada época, esta vez acumularás todos los batches con [add_batch](https://huggingface.co/docs/datasets/package_reference/main_classes.html?highlight=add_batch#datasets.Metric.add_batch) y calcularás la métrica al final.

```python
metric = load_metric("accuracy")
model.eval()
for batch in eval_dataloader:
    batch = {k: v.to(device) for k, v in batch.items()}
    with torch.no_grad():
        outputs = model(**batch)

    logits = outputs.logits
    predictions = torch.argmax(logits, dim=-1)
    metric.add_batch(predictions=predictions, references=batch["labels"])

metric.compute()
```

## Recursos adicionales

Para más ejemplos de fine-tuning consulta:

- [🤗 Transformers Examples](https://github.com/huggingface/transformers/tree/master/examples) incluye scripts 
  para entrenar tareas comunes de NLP en PyTorch y TensorFlow.

- [🤗 Transformers Notebooks](notebooks) contiene varios notebooks sobre cómo aplicar fine-tuning a un modelo para tareas específicas en PyTorch y TensorFlow.
