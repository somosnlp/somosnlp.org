---
title: Traducción de Texto
description: Cómo afinar un modelo de T5 en español para traduccir frases del español al portugués
cover: /images/ilustraciones/undraw_education_edited.svg
author: Oscar Cumbicus
bio: Profesor @UNL e Investigador @IxaGroup
twitter: https://twitter.com/OscarCumbicus
linkedin: https://www.linkedin.com/in/oscar-cumbicus-47095443/
github: https://github.com/oskrmiguel
---

<a href="https://colab.research.google.com/github/oskrmiguel/Traductor_T5_Spanish_to_Portuguese/blob/main/T5_Espa%C3%B1ol_a_Portugues.ipynb
" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## Configuración
Este cuaderno es una adaptación de [How to fine-tune a model on
translation](https://colab.research.google.com/github/huggingface/notebooks/blob/master/examples/translation.ipynb)



Si vas a abrir este cuaderno en colab, probablemente necesitarás
instalar 🤗 Transformers y 🤗 Datasets. Descomenta la siguiente celda y
ejecútala.



``` {.python}
! pip install datasets transformers[sentencepiece] sacrebleu
```



Si estás abriendo este cuaderno localmente, asegúrate de que tu entorno
tiene una instalación de la última versión de esas bibliotecas.

Para poder compartir tu modelo con la comunidad y generar resultados
como el que se muestra en la imagen de abajo a través de la API de
inferencia, hay que seguir algunos pasos más.

Primero tienes que almacenar tu token de autenticación del sitio web de
Hugging Face (¡regístrate [aquí](https://huggingface.co/join) si aún no
lo has hecho!) y luego ejecutar la siguiente celda e introducir tu
nombre de usuario y contraseña:



``` {.python}
from huggingface_hub import notebook_login

notebook_login()
```



A continuación, debe instalar Git-LFS. Descomente las siguientes
instrucciones:



``` {.python}
!apt install git-lfs
```



Asegúrate de que tu versión de Transformers es al menos la 4.11.0 ya que
la funcionalidad se introdujo en esa versión:



``` {.python}
import transformers

print(transformers.__version__)
```


    4.17.0




# Fine-tuning de un modelo en una tarea de traducción



En este cuaderno, veremos cómo afinar uno de los modelos [🤗
Transformers](https://github.com/huggingface/transformers) para una
tarea de traducción. Utilizaremos el [tatoeba
dataset](https://huggingface.co/datasets/tatoeba), es una colección de frases y traducciones.


Veremos cómo cargar fácilmente el conjunto de datos para esta tarea
utilizando 🤗 Datasets y cómo afinar un modelo sobre él utilizando la API
`Trainer`.



## Cargar la base de datos



Utilizaremos la biblioteca [🤗
Datasets](https://github.com/huggingface/datasets) para descargar los
datos y obtener la métrica que necesitamos utilizar para la evaluación
(para comparar nuestro modelo con el benchmark). Esto se puede hacer
fácilmente con las funciones `load_dataset` y `load_metric`. Aquí
utilizamos la parte español/portugués del conjunto de datos tatoeba.



```python
from datasets import load_dataset, load_metric,DatasetDict

raw_datasets = load_dataset("tatoeba", "es-pt")
metric = load_metric("sacrebleu")
```


El objeto `dataset` es
[`DatasetDict`](https://huggingface.co/docs/datasets/package_reference/main_classes.html#datasetdict),
que contiene una clave para el conjunto de entrenamiento



```python
raw_datasets
```


    DatasetDict({
        train: Dataset({
            features: ['id', 'translation'],
            num_rows: 67782
        })
    })




Para acceder a un elemento real, primero hay que seleccionar una
división y luego dar un índice:



```python
raw_datasets["train"][0]
```


    {'id': '0',
     'translation': {'es': '¡Intentemos algo!',
      'pt': 'Vamos tentar alguma coisa!'}}




Nosotros dividiremos este conjunto de datos en entrenamiento, validación
y pruebas



```python
train_devtest = raw_datasets['train'].train_test_split(shuffle = True, seed = 200, test_size=0.1)
posts_dev_test = train_devtest['test'].train_test_split(shuffle = True, seed = 200, test_size=0.50)
raw_datasets = DatasetDict({
    'train': train_devtest['train'],
    'validation': posts_dev_test['test'],
    'test': posts_dev_test['train']})
```



```python
raw_datasets
```


    DatasetDict({
        train: Dataset({
            features: ['id', 'translation'],
            num_rows: 61003
        })
        validation: Dataset({
            features: ['id', 'translation'],
            num_rows: 3390
        })
        test: Dataset({
            features: ['id', 'translation'],
            num_rows: 3389
        })
    })




## Preprocesar los datos



Antes de que podamos introducir esos textos en nuestro modelo, tenemos
que preprocesarlos. Esto lo hace un `Tokenizer` de Transformers 🤗 que
(como su nombre indica) tokenizará las entradas (incluyendo la
conversión de los tokens a sus correspondientes IDs en el vocabulario
preentrenado) y las pondrá en un formato que el modelo espera, así como
generará las otras entradas que el modelo requiere.

Para hacer todo esto, instanciamos nuestro tokenizador con el método
`AutoTokenizer.from_pretrained`, que asegurará

-   obtenemos un tokenizador que corresponde a la arquitectura del
    modelo que queremos utilizar,
-   descargamos el vocabulario utilizado al preentrenar este punto de
    control específico.

Ese vocabulario se almacenará en la caché, para que no se descargue de
nuevo la próxima vez que ejecutemos la célula.



```python
from transformers import AutoTokenizer
model_checkpoint='t5-small'
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
```
Si está utilizando uno de los cinco puntos de control T5 que requieren
un prefijo especial para poner antes de las entradas, debe adaptar la
siguiente celda

```python
if model_checkpoint in ["t5-small", "t5-base", "t5-larg", "t5-3b", "t5-11b"]:
    prefix = "translate Spanish to Portuguese: "
else:
    prefix = ""
```

Podemos entonces escribir la función que preprocesará nuestras muestras.
Simplemente las alimentamos al `tokenizer` con el argumento
`truncation=True`. Esto asegurará que una entrada más larga de lo que el
modelo seleccionado puede manejar se truncará a la longitud máxima
aceptada por el modelo. El relleno se tratará más tarde (en un
recopilador de datos), de modo que rellenamos los ejemplos hasta la
longitud más larga del lote y no todo el conjunto de datos.



```python
max_input_length = 128
max_target_length = 128
source_lang = "es"
target_lang = "pt"

def preprocess_function(examples):
    inputs = [prefix + ex[source_lang] for ex in examples["translation"]]
    targets = [ex[target_lang] for ex in examples["translation"]]
    model_inputs = tokenizer(inputs, max_length=max_input_length, truncation=True)

    # Setup the tokenizer for targets
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(targets, max_length=max_target_length, truncation=True)

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs
```



Esta función funciona con uno o varios ejemplos. En el caso de varios
ejemplos, el tokenizador devolverá una lista de listas para cada clave:



```python
preprocess_function(raw_datasets['train'][:2])
```


    {'input_ids': [[13959, 5093, 12, 21076, 10, 1174, 15, 6626, 2561, 23, 32, 3, 9, 1313, 15, 3, 9, 3151, 35, 355, 7, 20, 1413, 15785, 9, 7, 12, 26, 32, 7, 10381, 3, 26, 2, 9, 7, 5, 1], [13959, 5093, 12, 21076, 10, 1626, 75, 154, 6899, 238, 285, 1498, 7, 975, 3, 154, 40, 5, 1]], 'attention_mask': [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]], 'labels': [[465, 7, 7, 32, 353, 44, 7253, 3151, 35, 9, 7, 20, 1413, 15785, 9, 7, 12, 26, 32, 7, 3, 32, 7, 1227, 9, 7, 5, 1], [1699, 11666, 3, 32, 238, 285, 7, 49, 3, 287, 3, 400, 5, 1]]}




Para aplicar esta función en todos los pares de frases de nuestro
conjunto de datos, sólo tenemos que utilizar el método `map` de nuestro
objeto `dataset` que hemos creado anteriormente. Esto aplicará la
función en todos los elementos de todas las divisiones en `dataset`, por
lo que nuestros datos de entrenamiento, validación y prueba serán
preprocesados en un solo comando.



```python
tokenized_datasets = raw_datasets.map(preprocess_function, batched=True)
```

Incluso mejor, los resultados son automáticamente almacenados en caché
por la biblioteca 🤗 Datasets para evitar perder tiempo en este paso la
próxima vez que ejecutes tu cuaderno. La biblioteca 🤗 Datasets es
normalmente lo suficientemente inteligente como para detectar cuando la
función que pasas a map ha cambiado (y por lo tanto requiere no utilizar
los datos de la caché). Por ejemplo, detectará correctamente si cambias
la tarea en la primera celda y vuelves a ejecutar el cuaderno. 🤗
Datasets te avisa cuando utiliza archivos en caché, puedes pasar
`load_from_cache_file=False` en la llamada a `map` para no utilizar los
archivos en caché y forzar que se aplique de nuevo el preprocesamiento.

Tenga en cuenta que pasamos `batched=True` para codificar los textos por
lotes juntos. Esto es para aprovechar todas las ventajas del tokenizador
rápido que cargamos antes, que utilizará el multithreading para tratar
los textos de un lote de forma concurrente.



## Fine-tune el modelo



Ahora que nuestros datos están listos, podemos descargar el modelo
preentrenado y ajustarlo. Como nuestra tarea es del tipo secuencia a
secuencia, utilizamos la clase `AutoModelForSeq2SeqLM`. Al igual que con
el tokenizador, el método `from_pretrained` descargará y almacenará en
caché el modelo por nosotros.



```python
from transformers import AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq, Seq2SeqTrainingArguments, Seq2SeqTrainer

model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)
```



Para instanciar un `Seq2SeqTrainer`, necesitaremos definir tres cosas
más. La más importante es el
[`Seq2SeqTrainingArguments`](https://huggingface.co/transformers/main_classes/trainer.html#transformers.Seq2SeqTrainingArguments),
que es una clase que contiene todos los atributos para personalizar el
entrenamiento. Requiere un nombre de carpeta, que se utilizará para
guardar los puntos de control del modelo, y todos los demás argumentos
son opcionales:



```python
batch_size = 32
model_name = model_checkpoint.split("/")[-1]
args = Seq2SeqTrainingArguments(
    f"{model_name}-finetuned-{source_lang}-to-{target_lang}",
    evaluation_strategy = "epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    weight_decay=0.01,
    save_total_limit=1,
    num_train_epochs=3,
    predict_with_generate=True,
    fp16=True,
    push_to_hub=True,
)
```



Aquí configuramos la evaluación para que se realice al final de cada
época, ajustamos la tasa de aprendizaje, utilizamos el `tamaño_del_lote`
definido en la parte superior de la celda y personalizamos el
decaimiento del peso. Como el `Seq2SeqTrainer` guardará el modelo
regularmente y nuestro conjunto de datos es bastante grande, le decimos
que haga tres guardados como máximo. Por último, utilizamos la opción
`predict_with_generate` (para generar correctamente los resúmenes) y
activamos el entrenamiento de precisión mixta (para ir un poco más
rápido).

El último argumento para configurar todo para que podamos empujar el
modelo al [Hub](https://huggingface.co/models) regularmente durante el
entrenamiento. Elimínalo si no has seguido los pasos de instalación en
la parte superior del cuaderno. Si quieres guardar tu modelo localmente
con un nombre diferente al del repositorio al que será empujado, o si
quieres empujar tu modelo bajo una organización y no tu espacio de
nombres, utiliza el argumento `hub_model_id` para establecer el nombre
del repositorio (tiene que ser el nombre completo, incluyendo tu espacio
de nombres: por ejemplo `"sgugger/marian-finetuned-en-to-ro"` o
`"huggingface/marian-finetuned-en-to-ro"`).

A continuación, necesitamos un tipo especial de recopilador de datos,
que no sólo rellenará las entradas hasta la longitud máxima en el lote,
sino también las etiquetas:



```python
data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)
```



Lo último que hay que definir para nuestro `Seq2SeqTrainer` es cómo
calcular las métricas a partir de las predicciones. Tenemos que definir
una función para esto, que sólo utilizará la \"métrica\" que cargamos
antes, y tenemos que hacer un poco de pre-procesamiento para decodificar
las predicciones en los textos:



```python
import numpy as np

def postprocess_text(preds, labels):
    preds = [pred.strip() for pred in preds]
    labels = [[label.strip()] for label in labels]

    return preds, labels

def compute_metrics(eval_preds):
    preds, labels = eval_preds
    if isinstance(preds, tuple):
        preds = preds[0]
    decoded_preds = tokenizer.batch_decode(preds, skip_special_tokens=True)

    # Replace -100 in the labels as we can't decode them.
    labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)

    # Some simple post-processing
    decoded_preds, decoded_labels = postprocess_text(decoded_preds, decoded_labels)

    result = metric.compute(predictions=decoded_preds, references=decoded_labels)
    result = {"bleu": result["score"]}

    prediction_lens = [np.count_nonzero(pred != tokenizer.pad_token_id) for pred in preds]
    result["gen_len"] = np.mean(prediction_lens)
    result = {k: round(v, 4) for k, v in result.items()}
    return result
```



A continuación, sólo tenemos que pasar todo esto junto con nuestros
conjuntos de datos al `Seq2SeqTrainer`:



```python
trainer = Seq2SeqTrainer(
    model,
    args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    data_collator=data_collator,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics
)
```




Ahora podemos afinar nuestro modelo simplemente llamando al método
`train`:



```python
trainer.train()
```

Ahora puedes subir el resultado del entrenamiento al Hub, sólo tienes
que ejecutar esta instrucción:



```python
trainer.push_to_hub()
```



## Pruebas del Modelo



Ahora probaremos nuestro modelo en la traducción con el conjunto de
test.

Primero descargaremos nuestro modelo subido al hub o si lo tienes
localmente utiliza la ruta donde guardaste el modelo recién entrenado.



```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
model = AutoModelForSeq2SeqLM.from_pretrained("oskrmiguel/t5-small-finetuned-es-to-pt")
tokenizer = AutoTokenizer.from_pretrained("oskrmiguel/t5-small-finetuned-es-to-pt")
```



Ahora utilizamos la división \'test\' que hicimos de nuestro DataSet
principal.

Como ejemplo traduciremos las 10 primeras frases del test.



```python
for indice in range(10):
  inputs = tokenizer(
      "{} {}".format("translate Spanish to Portuguese: ",raw_datasets['test'][indice]['translation']['es']),
      return_tensors="pt"
      )
  outputs = model.generate(inputs["input_ids"], max_length=40, num_beams=4, early_stopping=True)
  print("{} {}".format(raw_datasets['test'][indice]['translation']['es'],tokenizer.decode(outputs[0])))
```


    Lo que queda es recuerdo y amargura en el corazón. <pad> O que queda é recuerdo e amargura no coraz<unk>o.</s>
    La prostaglandina es una sustancia que protege las paredes del aparato digestivo. <pad> A prostaglandina é uma sustancia que protege as paredes do aparato digestivo.</s>
    Naoki y Kaori tienen la misma edad. <pad> Naoki e Kaori tem a misma edade.</s>
    ¿Tenés un papelito para anotar el número? <pad> Você tenho um papelito para anotar o n<unk>mero?</s>
    La esperanza muere al final. <pad> A esperanza muito final.</s>
    Este es un tipo de madera difícil de serrar. <pad> Este é um tipo de madera dif<unk>cil de serrar.</s>
    Este personaje sólo viste de rosa. <pad> Este personaje só viste de rosa.</s>
    Él vive solito. <pad> Ele vive solito.</s>
    Qué suerte que haga tan buen tiempo. <pad> Qué suerte que haga t<unk>o buen tempo.</s>
    María no sabe que es portadora del gen del albinismo. <pad> Mar<unk>a n<unk>o sabe que é portadora do gen do albinismo.</s>




**NOTA**: Puedes entrenar el modelo por más épocas para que obtengas
mejores resultados en tu traducción

