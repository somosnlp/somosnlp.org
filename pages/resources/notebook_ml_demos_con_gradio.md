---
title: Demos con Gradio y Hugging Face
description: Creación y hosting de demos con Gradio y Hugging Face
cover: https://somosnlp.github.io/assets/images/undraw_education_edited.svg
author: Abubakar Abid
bio: Gradio Founder @Hugging Face
website:
twitter: https://twitter.com/abidlabs
linkedin:
github:
---


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/education-toolkit/blob/main/tutorials/ES/02_ml-demos-con-gradio.ipynb)




**Notebook original en inglés [aquí](https://colab.research.google.com/github/huggingface/education-toolkit/blob/main/tutorials/EN/02_ml-demos-with-gradio.ipynb).**



💡 **¡Hola!**



Hemos reunido un conjunto de herramientas que l@s profesor@s universitari@s pueden usar para preparar fácilmente laboratorios, tareas o clases. El contenido está diseñado de manera autónoma, de modo que se puede incorporar fácilmente al plan de estudios existente. Este contenido es gratuito y utiliza tecnologías Open Source ampliamente conocidas (`transformers`, `gradio`, etc).



Alternativamente, puede solicitar que alguien del equipo de Hugging Face ejecute los tutoriales para su clase a través de la iniciativa [Gira de demo.cratización de ML](https://www.notion.so/ML-Demo-cratization-tour-with-66847a294abd4e9785e85663f5239652)!



Además de los tutoriales, también compartimos otros recursos para profundizar en ML que pueden ayudar a diseñar el contenido del curso.




# Tutorial: Cree y aloje demos de Machine Learning con Gradio y Hugging Face 🤗



**Objetivos:**

1. Crear un demo rápido para su modelo de Machine Learning en Python usando la biblioteca `gradio`

2. Alojar los demos de forma gratuita con Hugging Face Spaces

3. Agregar el demo a su organización en Hugging Face para su clase o conferencia. Esto incluye:

* Un paso de configuración para instructor@s (u organizador@s de conferencias)

* Instrucciones de cómo subir los demos para l@s estudiantes (o participantes de conferencias)



**Duración**: 20-40 minutos



**Requisitos previos:** Conocimiento de Python y familiaridad básica del Machine Learning




**Autor**: [Abubakar Abid](https://twitter.com/abidlabs) (siéntase libre de enviarme un ping con cualquier pregunta sobre este tutorial)



¡Todos estos pasos se pueden hacer gratis! Todo lo que necesita es un navegador de Internet y un lugar donde pueda escribir Python 👩‍💻



## ¿Por qué demos?



Los **demos** de modelos de Machine Learning son una parte cada vez más importante de los _cursos_ y _conferencias_ de Machine Learning. Los demos permiten:

* que las personas que desarrollan modelos puedan **presentar** fácilmente su trabajo a una amplia audiencia

* aumentar la **reproducibilidad** de la investigación en Machine Learning

* que divers@s usuari@s puedan **identificar y depurar** más fácilmente los puntos de falla de los modelos




Como un ejemplo rápido de lo que nos gustaría construir, eche un vistazo a [Keras org en Hugging Face](https://huggingface.co/keras-io), que incluye una tarjeta de descripción y una colección de Modelos y Spaces construidos por la comunidad de Keras. Cualquier Space se puede abrir en su navegador y puede usar el modelo inmediatamente como se muestra aquí:



![](https://i.ibb.co/7y6DGjB/ezgif-5-cc52b7e590.gif)






## 1. Crear demos rápidos de ML en Python usando la biblioteca Gradio



`gradio` es una biblioteca de Python que le permite crear demos web simplemente especificando la lista de componentes de entrada y salida que espera su modelo de Machine Learning.



¿Qué quiero decir con componentes de entrada y salida? Gradio viene con un montón de componentes predefinidos para diferentes tipos de modelos de aprendizaje automático. Aquí hay unos ejemplos:



* Para un **clasificador de imágenes**, el tipo de entrada esperado es una `Image` y el tipo de salida es una `Label`.

* Para un **modelo de reconocimiento de voz**, el componente de entrada esperado es un `Microphone` (que permite a los usuarios grabar desde el navegador) o `Audio` (que permite a los usuarios arrastrar y soltar archivos de audio), mientras que el tipo de salida es `Text`.

* Para un **modelo de respuesta a preguntas**, esperamos **2 entradas**: [`Text`, `Text`], un cuadro de texto para el párrafo y otro para la pregunta, y el tipo de salida es un solo `Text` correspondiente a la respuesta.



Ya se va notando la idea... (para todos los componentes, [ver la documentación](https://gradio.app/docs/))



Además de los tipos de entrada y salida, Gradio espera un tercer parámetro, que es la propia función de predicción. Este parámetro puede ser ***cualquier* función normal de Python** que tome los parámetros correspondientes a los componentes de entrada y devuelva los valores correspondientes a los componentes de salida.


Basta de palabras. ¡Veamos algo de código!


```python
# Primero, instale Gradio
!pip install --quiet gradio
```

```python
# Definir una función simple "Hola mundo"
def  greet(name):
	return  "Hello " + name + "!!"
```


```python
# Escriba 2 líneas de Python para crear una GUI simple
import gradio as gr
gr.Interface(fn=greet, inputs="text", outputs="text").launch();
```

Ejecutar el código anterior debería producir una GUI simple dentro de este Notebook que le permita escribir entradas de ejemplo y ver el resultado devuelto por su función.



Note que definimos una 'Interface' usando los 3 ingredientes mencionados anteriormente:

* Una función

* Componente(s) de entrada

* Componente(s) de salida



Este es un ejemplo simple para texto, pero el mismo principio es válido para cualquier otro tipo de tipo de datos. Por ejemplo, aquí hay una interface que genera un tono musical cuando se le proporcionan algunos parámetros diferentes (el código específico dentro de `generate_tone()` no es importante para el propósito de este tutorial):




```python
import numpy as np
import gradio as gr

def  generate_tone(note, octave, duration):
	sampling_rate = 48000
	a4_freq, tones_from_a4 = 440, 12 * (octave - 4) + (note - 9)
	frequency = a4_freq * 2 ** (tones_from_a4 / 12)
	audio = np.linspace(0, int(duration), int(duration) * sampling_rate)
	audio = (20000 * np.sin(audio * (2 * np.pi * frequency))).astype(np.int16)
	return sampling_rate, audio

gr.Interface(
	generate_tone,
	[
		gr.inputs.Dropdown(["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"], type="index"),
		gr.inputs.Slider(4, 6, step=1),
		gr.inputs.Textbox(type="number", default=1, label="Duration in seconds"),
	],
	"audio",
	title="Generate a Musical Tone!"
).launch()
```













**Desafío #1**: cree un demo de Gradio que tome una imagen y aplique un *filtro sepia* en menos de 10 líneas de código Python. Puedes encontrar [este enlace útil](https://www.yabirgb.com/sepia_filter/).



Hay muchos más ejemplos que puede probar en la [página de inicio](https://gradio.app/getting_started/) de Gradio que cubren características adicionales tales como:

* Agregar entradas de ejemplo

* Agregar _estado_ (por ejemplo para chatbots)

* Compartir demos fácilmente usando un parámetro llamado `share` (<-- Esto está muy cool 😎)



Es especialmente fácil hacer un demo de modelos `transformers` desde el Hub de Hugging Face utilizando el método especial `gr.Interface.load`. Por ejemplo,

aquí está el código para construir un demo para [GPT-J](https://huggingface.co/EleutherAI/gpt-j-6B), un modelo de lenguaje grande, y agregar un par de ejemplos de entradas:


```python
import gradio as gr

examples = [["The Moon's orbit around Earth has"], ["There once was a pineapple"]]

gr.Interface.load("huggingface/EleutherAI/gpt-j-6B", examples=examples).launch();
```



**Desafío #2**: Vaya al [Model Hub de Hugging Face](https://huggingface.co/models), y elija un modelo que realice uno de las otros tasks admitidos en la biblioteca `transformers`(aparte de la generación de texto). Cree un demos de Gradio para ese modelo usando `gr.Interface.load`.



## 2. Aloje el demo (gratis) en los Spaces de Hugging Face



Una vez que haya realizado un demo de Gradio puede alojarlo de forma permanente en Hugging Spaces muy fácilmente:



Estos son los pasos (que se muestran en el GIF a continuación):



A. Cree una cuenta de Hugging Face, si aún no tiene una, visitando https://huggingface.co/ y haciendo clic en "Sign Up"



B. Una vez que haya iniciado sesión, haga clic en su foto de perfil y luego haga clic debajo en "New Space" para ir a esta página: https://huggingface.co/new-space



C. Dale a tu Space un nombre y una licencia. Selecciona "Gradio" como Space SDK y elija "Public" si está de acuerdo con que todos accedan a su Space y al código subyacente



D. Luego encontrará una página que le brinda instrucciones sobre cómo subir sus archivos en el repositorio de Git para ese Space. Es posible que también deba agregar un archivo `requirements.txt` para especificar las dependencias del paquete de Python



E. Una vez que haya enviado sus archivos, ¡eso es todo! Spaces creará automáticamente el demo de Gradio. Podrá compartirla con cualquier persona, en cualquier lugar!



![GIF](https://huggingface.co/blog/assets/28_gradio-spaces/spaces-demo-finalized.gif)







Incluso puede insertar su demo de Gradio en cualquier sitio web. En un blog, una pagina de portfolio, o incluso en un Colab notebook como el modelo de reconocimiento de bocetos de Pictionary a continuación:




```python
from IPython.display import IFrame

IFrame(src='https://hf.space/gradioiframe/abidlabs/Draw/+', width=1000, height=800)
```


**Desafío #3**: Suba su demo de Gradio a los Spaces de Hugging Face y obtenga un URL permanente para él. Comparta el URL permanente con alguien (la persona con la que colabora, un@ amig@, un@ usuari@, etc.). ¿Qué tipo de comentarios recibe sobre su modelo de Machine Learning?



## 3. Agregue su demo a la organización Hugging Face para su clase o conferencia



#### **Configuración** (Para instructor@s u organizador@s de conferencias)



A. Cree una cuenta de Hugging Face, si aún no tiene una, visitando https://huggingface.co/ y haciendo clic en "Sign Up"



B. Una vez que haya iniciado sesión, haga clic en su foto de perfil y luego haga clic en "Nueva organización" para ir a esta página: https://huggingface.co/organizations/new



C. Complete la información para su clase o conferencia. Recomendamos crear una organización separada cada vez que se imparte una clase (por ejemplo, "Stanford-CS236g-20222") y para cada año de la conferencia.



D. Se creará su organización y ahora l@s usuari@s podrán solicitar ser agregad@s a su organización visitando la página de la organización.



E. Opcionalmente, puede cambiar la configuración haciendo clic en el botón "Organization settings". Por lo general, para clases y conferencias, querrá navegar a `Settings > Members` y establezca el rol predeterminado para nuev@s miembr@s en "write", lo que les permite enviar Spaces pero no cambiar la configuración.


#### Para estudiantes o participantes de conferencias


A. Pída a a la persona que instruye el curso u organiza la conferencia el enlace a la página de la Organización si aún no lo tiene.

B. Visite la página de la Organización y haga clic en el botón "Request to join this org", si aún no es parte de la organización.

C. Una vez que haya sido aprobado para unirse a la organización, haya creado su demo de Gradio y lo haya subido a Spaces (ver las secciones 1 y 2), simplemente vaya a su Space y en `Settings > Rename or transfer this space` seleccione el nombre de la organización en `New owner`. Haga clic en el botón y el Space ahora se agregará a su clase o conferencia!