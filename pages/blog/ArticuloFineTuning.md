---
title: Cómo afinar y alinear nuestro modelos
description: Discusion, instrucciones y código ejemplo de DPO, PEFT y Cuantización
date: 2025-05-04T122:00:00.000+00:00
lang: es
cover: https://github.com/Neovalle/H4rmony/blob/main/fine%20tuning.jpg
author: Jorge Vallego
bio: AI Engineering Consultant - H4rmony Project Leader
website: https://TheH4rmonyProject.org
linkedin: linkedin.com/in/jorge-vallego-391838a6
---


# Cómo afinar y alinear nuestros modelos

## Introducción

Comencemos analizando de una forma intuitiva de qué queremos lograr y qué es lo que hace un ajuste de un modelo.
Fine-tuning o ajuste es el proceso de adaptar un modelo preentrenado a una tarea específica utilizando nuevos ejemplos. En el contexto del reto de alineamiento del hackathon, esto significa enseñar al modelo a responder de manera más adecuada a la cultura, lengua y formas de comunicación propias de tu región.

Pero antes, conviene preguntarse: ¿qué es un modelo preentrenado y qué partes nos interesa modificar o “alinear”? En líneas generales, un modelo consta de un embedding (representación numérica de palabras o tokens) y una red neuronal que ha sido entrenada para predecir el siguiente token de una secuencia. Este tipo de modelos se conocen como *autoregresivos*: generan una palabra (o token) a la vez, y usan lo generado hasta el momento como contexto para predecir el siguiente.

El comportamiento del modelo está determinado por miles de millones de parámetros, que son los pesos de las conexiones entre las capas de la red neuronal. Durante el fine-tuning, lo que buscamos es ajustar esos pesos (o algunos de ellos) para que el modelo se comporte de manera más alineada con nuestros valores, objetivos o comunidad.

### Estrategias de ajuste

- **Fine-tuning completo**: se actualizan todos los parámetros del modelo. Requiere muchos recursos (GPUs potentes y mucho tiempo) y no suele ser necesario para tareas de adaptación de conocimientos o  preferencias.
- **Fine-tuning parcial**: se actualizan solo algunas capas (por ejemplo, las últimas capas del transformador o la capa de salida). Útil si ya tienes una base buena y solo quieres especializar.
- **LoRA / QLoRA (Low-Rank Adaptation)**: técnica eficiente que congela el modelo original y entrena pequeños adaptadores insertados en puntos clave. Es lo más recomendable cuando trabajamos con recursos limitados.

Cuando el objetivo no es simplemente enseñar respuestas correctas, sino enseñar al modelo a preferir una respuesta culturalmente más adecuada frente a otra, es prefirible utilizar técnicas de aprendizaje reforzado como **DPO (Direct Preference Optimization)**.

DPO permite incorporar preferencias humanas directamente durante el entrenamiento, utilizando un dataset con tres atributos principales  `prompt`, `chosen`, y `rejected`. Esto es ideal cuando:

- Se busca alinear el modelo con estilos lingüísticos o valores humanos específicos.
- Se dispone de respuestas alternativas, y se puede determinar cuál es la preferible.
- Se quiere mantener el conocimiento base del modelo pero ajustar su comportamiento.

#### Comparación con otras técnicas

A diferencia de SFT (Supervised Fine Tuning), que puede sobrescribir lo que el modelo sabe con nuevas muestras (a veces generando el problema de "catastrophic forgetting"), DPO es menos intrusivo: no le dice al modelo “esto es lo correcto”, sino “esto es mejor que esto otro”. Esta señal relativa permite afinar sin borrar del todo las habilidades generales del modelo.

Además de DPO, han surgido técnicas similares que siguen esta filosofía de preferencia directa. Por ejemplo:

- **ORPO** (Odds Ratio Preference Optimization)
- **KTO** (Kahneman-Tversky Optimization)
- **GRPO** (Group Relative Policy Optimization)

Estas técnicas también buscan optimizar el modelo a partir de comparaciones humanas, pero difieren en sus funciones de optimización y regularización. DPO se destaca actualmente por su simplicidad, estabilidad y eficacia en tareas de alineamiento lingüístico.


#### Ajuste por DPO

Para aplicar DPO en la práctica, lo primero que necesitamos es un conjunto de datos en el formato adecuado: una colección de ejemplos donde, para cada `prompt`, existan al menos dos respuestas candidatas —una preferida (`chosen`) y otra menos adecuada (`rejected`).
Como veremos en este artículo, en general, DPO suele acompañarse de otras técnicas complementarias como PEFT y cuantización. PEFT (Parameter-Efficient Fine-Tuning) es el marco general que agrupa técnicas como LoRA, QLoRA o Prompt Tuning. La librería `peft` de Hugging Face facilita su uso. También, cuantización, que es una técnica de reducción de precisión utilizada en modelos de aprendizaje profundo para disminuir el consumo de memoria y acelerar el procesamiento, se incluye en las implementaciones de ajuste por DPO.

Para entrar gradualmente en estas técnicas, empecemos con el mínimo código posible para demostrar un ajuste por DPO:


```python
# Instalación de las librerías necesarias
!pip install -qq trl transformers datasets

# Importaciones de módulos para carga de datos y entrenamiento
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import DPOConfig, DPOTrainer

# Nombre del modelo base
model_name = "HuggingFaceTB/SmolLM2-135M-Instruct"

# Carga del tokenizador asociado al modelo
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Carga del modelo en memoria 
model = AutoModelForCausalLM.from_pretrained(model_name)

# Carga del dataset de preferencias (formato con prompt, chosen, rejected)
train_dataset = load_dataset("neovalle/H4rmony_dpo", split="train")

# Configuración básica del entrenamiento con DPO
training_args = DPOConfig(
    output_dir="harmony-SmolLM2-135M-dpo",  # Carpeta donde se guardarán los resultados
    logging_steps=10,                       # Frecuencia con la que se muestran métricas
    report_to="none"                        # Desactiva integración con Weights & Biases
)

# Inicialización del entrenador DPO
trainer = DPOTrainer(
    model=model,                  # Modelo base
    args=training_args,           # Configuración del entrenamiento
    processing_class=tokenizer,   # Tokeniza y preparara los datos de entrada
    train_dataset=train_dataset,  # Dataset de entrenamiento

)

# Ejecución del proceso de entrenamiento
trainer.train()

```


Este código, si bien sirve para "romper el hielo" y que tomemos más confianza, necesita mucho trabajo antes que podamos ajustar modelos más grandes, y  encontremos los valores ideales de los hiper parámetros. Sigamos entonces por discutir técnicas que hagan nuestro ajuste más eficaz y eficiente.

## Ajuste usando LoRA

El ajuste fino tradicional de modelos de lenguaje implica modificar todos sus parámetros, lo que puede significar ajustar miles de millones de valores. Esto requiere mucha memoria, entrenamiento prolongado y puede sobrescribir el conocimiento general previamente adquirido por el modelo.

LoRA (Low-Rank Adaptation) es una técnica de fine-tuning eficiente (PEFT) que evita estos problemas insertando pequeñas matrices entrenables de bajo rango en puntos estratégicos del modelo, como las proyecciones de atención (q_proj, v_proj). Durante el entrenamiento, solo estas matrices son ajustadas, mientras que el resto del modelo permanece congelado.

Esto tiene tres ventajas clave:

    -Eficiencia computacional: se reducen los requisitos de memoria y tiempo.

    -Preservación del conocimiento: el modelo mantiene lo que ya sabía y solo aprende lo nuevo.

    -Modularidad: los adaptadores LoRA se pueden guardar por separado y aplicar a distintos modelos base.

LoRA pertenece al conjunto de técnicas llamadas PEFT (Parameter-Efficient Fine-Tuning), que buscan precisamente esto: adaptar modelos de forma eficiente y segura.

Pasemos a modificar el código anterior para incluir LoRA.


```python


## Como ves hemos agregado la biblioteca peft, y la accelerate (que puede no ser necesaria, pero es buena costumbre incluirla)

!pip install -qq trl transformers datasets peft accelerate 

from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model # nuevos módulos
from trl import DPOTrainer, DPOConfig 
import torch # necesario para el trabajo con tensores en 

# Nombre del modelo base
model_name = "HuggingFaceTB/SmolLM2-135M-Instruct"

# Carga del tokenizador
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Carga del modelo 
model = AutoModelForCausalLM.from_pretrained(
    model_name,
)

# Definimos la configuración LoRA, incluyendo las capas que vamos a ajustar
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)
model = get_peft_model(model, lora_config) # aplicamos la config al modelo  

# Carga del dataset de preferencias
train_dataset = load_dataset("neovalle/H4rmony_dpo", split="train")

# Configuración del entrenamiento
training_args = DPOConfig(
    output_dir="harmony-SmolLM2-135M-dpo",
    logging_steps=10,
    report_to="none"
)

# Entrenador DPO con LoRA
trainer = DPOTrainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    processing_class=tokenizer  
)
# Entrenamiento del modelo
trainer.train()

```

Estos cambios al código como decíamos, son fundamentales para un entrenamiento adecuado, dirigiendo los cambios a las capas que queremos. Entiendo que 
acá surgen varias preguntas ¿por qué rango 8?¿por qué definimos dropout?¿cómo sabemos qué capas entrenar? Entender estos y muchos otros hiper parámetros que estamos aceptando por defecto, tanto en la configuración de LoRA como en el entrenador es de suma importancia en el momento de determinar que es mejor para lograr nuestro modelo final. Más adelante nos concentraremos en entender cada uno de esos hiper parámetros y como sincronizarlos efectivamente. Pero pasemos a hacer nuestro entrenamiento más rápido y eficiente en el uso de memoria con otra técnica PEFT, la variación de LoRA llamada QLoRA (Quantized Low-Rank adaptation)

## Ajuste usando QLoRA

QLoRA (Quantized Low-Rank Adaptation) combina dos técnicas para permitir el ajuste eficiente de modelos grandes incluso en entornos con poca memoria. Por un lado, LoRA entrena solo una pequeña parte del modelo (adaptadores de bajo rango), y por otro, la cuantización en 4 bits reduce drásticamente el tamaño del modelo base al representar sus pesos con menor precisión. Esto permite cargar modelos de varios miles de millones de parámetros en una sola GPU sin perder demasiada precisión. La combinación es poderosa: se entrena poco, se guarda poco y se usa menos memoria, todo sin necesidad de modificar el modelo original. 

```python

# bitsandbytes es requerido para usar modelos cuantizados en 4-bit
!pip install -qq trl transformers datasets peft accelerate bitsandbytes

# Importaciones
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model
from trl import DPOTrainer, DPOConfig
import torch

# Nombre del modelo base
model_name = "HuggingFaceTB/SmolLM2-135M-Instruct"

# Carga del tokenizador
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Carga del modelo en 4-bit con soporte para cuantización usando bitsandbytes
from transformers import BitsAndBytesConfig
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,  # Activa la cuantización en 4 bits
    bnb_4bit_compute_dtype=torch.float16,  # Usa precisión media para los cálculos
    bnb_4bit_use_double_quant=True,  # Aplica cuantización secundaria para reducir aún más el tamaño
    bnb_4bit_quant_type="nf4"  # 'nf4' (NormalFloat4) mantiene más precisión que otros esquemas como int4
)

# Aplicaa cuantización
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,
    device_map="auto"
)

# Preparación del modelo para entrenamiento eficiente con LoRA y cuantización
from peft import prepare_model_for_kbit_training

model = prepare_model_for_kbit_training(model)  # LoRA sobre modelos 4-bit

# Ahora configuramos lora
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)
model = get_peft_model(model, lora_config) # Aplicamos lora al model cuantizado

# Carga del dataset de preferencias
train_dataset = load_dataset("neovalle/H4rmony_dpo", split="train")

# Configuración del entrenamiento
training_args = DPOConfig(
    output_dir="harmony-SmolLM2-135M-dpo",
    logging_steps=10,
    report_to="none"
)

# Entrenador DPO con LoRA
trainer = DPOTrainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    processing_class=tokenizer  
)

# Entrenamiento del modelo
trainer.train()

```

Muy bien!, hemos logrado usar DPO con PEFT y cuantización (QLoRA). Ahora el tema es qué tanto aprendió nuestro modelo con este ajuste. Al ejecutar estos programas habrás visto, que cuando entrena nos va dando un valor cada 10 pasos, loss o pérdida. Esto nos da una pauta de que si la pérdida baja consistentemente el model esta aprendiendo de las preferencias de nuestro dataset, cuando esto ocurre se dice que el modelo "converge". Hay muchos indicadores que nos pueden hablar de que tan buena o no es la convergencia. La librería Weights and Biases nos ayuda a visualizar todos estos indicadores, es muy recomendable utilizarla, solo se necesita una cuanta gratuita en https://wandb.ai donde se puede obtener una clave de API. Weights and Biases es por defecto el sistema de reporte de la librería trl, tanto es así que habrás visto que en el código he usado report_to="none" , esto es para evitar que generara reporte e hiciera el código más complicado. Ahora que ya hemos entendido DPO, PEFT y cuantización, incluyamos el reporte wandb. Sólamente haz una cuenta, obtiene to clave API y utilízala como se muestra en el código que verás más abajo. En este caso es en Google Colab.

## Generar reporte usando Weights and Biases.


```python

# agregamos la instalación weights and biases 
!pip install -qq trl transformers datasets peft accelerate bitsandbytes wandb

# Importaciones
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model
from trl import DPOTrainer, DPOConfig
import torch
import wandb # importamos weights and biases

# Extraemos la clabve de wandB del secreto de colab 
from google.colab import userdata
wandb_key = userdata.get('wandb')

wandb.login(key=wandb_key) # hacemos el login a W&B
wandb.init(project="H4rmony-DPO", name="SmolLM2-QLoRA") # iniciamos sesión

# Nombre del modelo base
model_name = "HuggingFaceTB/SmolLM2-135M-Instruct"

# Carga del tokenizador
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Carga del modelo en 4-bit con soporte para cuantización usando bitsandbytes
from transformers import BitsAndBytesConfig
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,  # Activa la cuantización en 4 bits
    bnb_4bit_compute_dtype=torch.float16,  # Usa precisión media para los cálculos
    bnb_4bit_use_double_quant=True,  # Aplica cuantización secundaria para reducir aún más el tamaño
    bnb_4bit_quant_type="nf4"  # 'nf4' (NormalFloat4) mantiene más precisión que otros esquemas como int4
)

# Aplicaa cuantización
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,
    device_map="auto"
)

# Preparación del modelo para entrenamiento eficiente con LoRA y cuantización
from peft import prepare_model_for_kbit_training

model = prepare_model_for_kbit_training(model)  # LoRA sobre modelos 4-bit

# Ahora configuramos lora
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)
model = get_peft_model(model, lora_config) # Aplicamos lora al model cuantizado

# Carga del dataset de preferencias
train_dataset = load_dataset("neovalle/H4rmony_dpo", split="train")

# Configuración del entrenamiento
training_args = DPOConfig(
    output_dir="harmony-SmolLM2-135M-dpo",
    logging_steps=10,
    report_to="wandb" # esta linea podría omitirse, wandb es el default
)

# Entrenador DPO con LoRA
trainer = DPOTrainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    processing_class=tokenizer
)

# Entrenamiento del modelo
trainer.train()


```

Ahora veamos qué nos muestra W and B:

![image](https://github.com/user-attachments/assets/84e4a4f5-7a9c-4ccc-a2b3-41a1e8868958)


En un primer vistazo vemos que está convergiendo, pero lejos de aproximarse a 0, y también se ven algunos saltos que pueden ser problemáticos. Esto significa que  hay cosas para trabajar y mejorar en este entrenamiento.


Sabemos que tenemos un código que funciona correctamente con DPO, PEFT y cuantización, nos queda trabajar en la parte más interesante que es asegurarnos que tenemos un buen dataset, entender el modelo base que nos conviene usar y más que nada entender cómo ajustar los hiper parámetros para lograr el mejor fine-tunining posible. Sobre estos temas profundizaremos en la próxima entrega. 







