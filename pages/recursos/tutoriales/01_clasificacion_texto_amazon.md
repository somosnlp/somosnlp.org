---
title: Clasificación de texto
description: Cómo afinar un modelo de RoBERTa en español para clasificar las reseñas de Amazon.
cover: https://somosnlp.github.io/assets/images/undraw_education_edited.svg
author: Lewis Tunstall
bio: Ingeniero de Machine Learning @HuggingFace 
twitter: https://twitter.com/_lewtun
linkedin: https://www.linkedin.com/in/lewis-tunstall
github: https://github.com/lewtun
---

<a href="https://colab.research.google.com/drive/17630ohLuzpQ3jJRp1YSb-05fcbi8STql
" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## Configuración

Si está ejecutando este notebook en Google Colab, ejecute la siguiente celda para instalar las bibliotecas que necesitamos:


```python
!pip install transformers datasets
```

Para compartir tu modelo con la comunidad, primero crea una cuenta en el [Hugging Face Hub](https://huggingface.co/join). A continuación, ejecute la siguiente celda y proporcione su nombre de usuario y contraseña para generar un token de autenticación:


```python
# Esto sólo funciona en Google Colab! Para los notebooks normales, es necesario ejecutar esto en el terminal
!huggingface-cli login
```

Si no tienes instalado [Git LFS](https://git-lfs.github.com), puedes hacerlo descomentando y ejecutando la celda de abajo:


```python
# !apt install git-lfs
# !git config --global user.email "you@example.com"
# !git config --global user.name "Your Name"
```

## Cargar y explorar los datos

Utilizaremos 🤗 Datasets para cargar y procesar nuestro conjunto de datos. Si no está familiarizado con 🤗 Datasets, vea el siguiente vídeo :)


```python
from IPython.display import YouTubeVideo

YouTubeVideo("_BZearw7f0w", width=600, height=400)
```


```python
from datasets import load_dataset

dataset = load_dataset("amazon_reviews_multi", "es")
dataset
```


```python
import random
import pandas as pd
from datasets import ClassLabel
from IPython.display import display, HTML

def show_random_elements(dataset, num_examples=10):
    "Taken from https://github.com/huggingface/notebooks/blob/master/examples/text_classification.ipynb"
    
    assert num_examples <= len(dataset), "Can't pick more elements than there are in the dataset."
    picks = []
    for _ in range(num_examples):
        pick = random.randint(0, len(dataset)-1)
        while pick in picks:
            pick = random.randint(0, len(dataset)-1)
        picks.append(pick)
    
    df = pd.DataFrame(dataset[picks])
    for column, typ in dataset.features.items():
        if isinstance(typ, ClassLabel):
            df[column] = df[column].transform(lambda i: typ.names[i])
    display(HTML(df.to_html()))

show_random_elements(dataset["train"])
```


```python
dataset.set_format("pandas")
df = dataset["train"][:]
df.head()
```


```python
df["product_category"].value_counts()
```


```python
df["stars"].value_counts()
```


```python
dataset.reset_format()
```

## Fusionar las clasificaciones por estrellas


```python
dataset = dataset.filter(lambda x : x["stars"] != 3)
```


```python
def merge_star_ratings(examples):
    if examples["stars"] <= 2:
        label = 0
    else:
        label = 1
    return {"labels": label}
```


```python
dataset = dataset.map(merge_star_ratings)
```


```python
show_random_elements(dataset["train"], num_examples=3)
```

## Tokenizar las reseñas


```python
from transformers import AutoTokenizer

model_checkpoint = "BSC-TeMU/roberta-base-bne"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
```

## Tokenización de las reseñas

Para entender la siguiente sección, vea este breve vídeo sobre la tokenización:


```python
YouTubeVideo("Yffk5aydLzg", width=600, height=400)
```


```python
tokenizer.vocab_size
```


```python
text = "¡hola, me llamo lewis!"
tokenized_text = tokenizer.encode(text)

for token in tokenized_text:
    print(token, tokenizer.decode([token]))
```


```python
encoded_text = tokenizer(text, return_tensors="pt")
encoded_text
```


```python
def tokenize_reviews(examples):
    return tokenizer(examples["review_body"], truncation=True)
```


```python
columns = dataset["train"].column_names
columns.remove("labels")
encoded_dataset = dataset.map(tokenize_reviews, batched=True, remove_columns=columns)
encoded_dataset
```


```python
encoded_dataset["train"][0]
```

## Cargar el modelo preentrenado


```python
from transformers import AutoModelForSequenceClassification

num_labels = 2
model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint, num_labels=num_labels)
```

### De las input IDs a los hidden states


```python
outputs = model(**encoded_text)
outputs
```

## Definir las métricas de rendimiento


```python
from datasets import load_metric 

metric = load_metric("accuracy")
metric
```


```python
import numpy as np

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    return metric.compute(predictions=predictions, references=labels)
```

## Afinar el modelo preentrenado

Si quiere entender más profundamente cómo funciona el Entrenador, vea el siguiente vídeo:


```python
YouTubeVideo("nvBXf7s7vTI", width=600, height=400)
```


```python
from transformers import TrainingArguments

model_name = model_checkpoint.split("/")[-1]

batch_size = 16
num_train_epochs=2
num_train_samples = 20_000
train_dataset = encoded_dataset["train"].shuffle(seed=42).select(range(num_train_samples))
logging_steps = len(train_dataset) // (2 * batch_size * num_train_epochs)

training_args = TrainingArguments(
    output_dir="results",
    num_train_epochs=num_train_epochs,     
    learning_rate=2e-5,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    weight_decay=0.01,
    evaluation_strategy="epoch",
    save_strategy="epoch", 
    logging_steps=logging_steps,
    push_to_hub=True,
    push_to_hub_model_id=f"{model_name}-finetuned-amazon_reviews_multi"
)
```


```python
from transformers import Trainer

trainer = Trainer(
    model=model, 
    args=training_args, 
    compute_metrics=compute_metrics,
    train_dataset=train_dataset,
    eval_dataset=encoded_dataset["validation"],
    tokenizer=tokenizer
)
```


```python
trainer.train()
```

## Empuje hacia el Hugging Face Hub

Para más detalles sobre el envío de modelos al Hub, vea el siguiente vídeo:


```python
YouTubeVideo("A5IWIxsHLUw", width=600, height=400)
```


```python
trainer.push_to_hub()
```

## Descargue el modelo desde el Hub


```python
from transformers import pipeline

model_checkpoint = "lewtun/roberta-base-bne-finetuned-amazon_reviews_multi"
pipe = pipeline("sentiment-analysis", model=model_checkpoint)
```


```python
pipe("¡me encanta el ipad!")
```

---

Este notebook forma parte del curso de NLP de 0 a 100. Puedes encontrar el curso completo [aquí](https://somosnlp.org/nlp-de-cero-a-cien).
