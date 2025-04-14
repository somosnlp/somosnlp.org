---
title: "Reto #HackathonSomosNLP 2025: BLEND"
description: Cómo participar en este reto y ayudar a mejorar el conocimiento cultural de los modelos de lenguaje
lang: es
cover: https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg
---

Responde preguntas sobre tu país para evaluar el conocimiento cultural de LLMs. Utilizaremos estas respuestas para extender el benchmark abierto BLEND.

*14 de abril - 7 de mayo | máx 2 ptos*

<center><a href="https://docs.google.com/spreadsheets/d/1QLPQ7gah9yzG3-1BPIw5Jp994Rz8L_yZT8obgWH8S2Y" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">¡Participa ya!</a></center>

Incentivos:
- 200 por equipo = acceso a los 500 USD de la API Cohere para el reto principal
- 50 por persona = co-autoría en el paper

Muchísimas gracias a:
- CENIA: Almacenamiento de los datos en los espacios de anotación
- El equipo: Eugenio Herrera, Sebastián Cifuentes, Clemente y María Grandury

---

## **¿Qué es BLEND y por qué estamos replicándolo?**

### **Background**

En este reto buscamos adaptar la metodología de [*BLEND: A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures and Languages*](https://arxiv.org/abs/2406.09948) para la creación de un nuevo benchmark cultural enfocado en las culturas de habla hispana.

A modo de resumen, en el paper original se realizaron 500 preguntas a participantes de 16 países/regiones de 13 lenguas distintas, con el fin de crear un benchmark cultural.

Un ejemplo de pregunta es: "¿Qué comen generalmente las personas de [Nombre del país] de postre?"

Con esta información, los autores realizaron un cruce de respuestas, y así generaron preguntas de alternativa múltiples para evaluar el conocimiento cultural de distintos LLMs.

### **Propuesta**

Con tu ayuda, buscamos replicar esta metodología en el contexto de nuestra diversa realidad cultural. En la siguiente figura puedes apreciar qué buscamos:

![BLEND 1](https://somosnlp.github.io/assets/images/blog/retos_2025_blend_1.png)


Notar que cada cuadrado en verde implica tu participación, es decir, ¡serás una pieza clave en la construcción de este nuevo benchmark!

## **¿Cómo comenzar a responder preguntas?**

Para participar en la anotación colaborativa de datos, primero debes ingresar a XXX dirección.

Necesitarás una cuenta en HuggingFace para ingresar. Si no tienes una, puedes crearte una de forma sencilla [aquí](https://huggingface.co/join).

Una vez dentro, verás la siguiente interfaz:

![BLEND 2](https://somosnlp.github.io/assets/images/blog/retos_2025_blend_2.png)

Como notarás, hay un listado de múltiples *datasets*, nombrados acorde a su país, bajo el siguiente formato:

- PAÍS - Código ISO - **Responder**
- PAÍS - Código ISO - **Validar**

Es decir, cada país tiene un espacio para responder preguntas, y otro para validar las respuestas del resto de los participantes.

### **Instrucciones para responder**

Al ingresar al espacio correspondiente a tu país, te encontrarás con la siguiente interfaz:

![BLEND 3](https://somosnlp.github.io/assets/images/blog/retos_2025_blend_3.png)

Al momento de responder las preguntas, es importante seguir estas pautas:

- **Contesta desde tu contexto cultural**: Proporciona respuestas que reflejen la realidad cultural de tu país. No hay respuestas correctas o incorrectas, queremos capturar la diversidad cultural.
- **Responde en tu idioma nativo**: Utiliza el español como lo hablas en tu país o región.
- **Responde de manera breve y concisa**: Usa términos precisos, entidades específicas y referencias temporales claras. Por ejemplo, si te preguntan a qué hora sale la gente del trabajo, respuestas como "18:00" o "19:00" son ideales.
- **Puedes dar múltiples opciones**: Si lo consideras necesario, puedes proporcionar hasta tres respuestas diferentes si existen varias prácticas comunes en tu cultura.
- **Especifica la región si es necesario**: Si tu respuesta representa más a una región específica que a todo el país, indica el nombre de esta región en el formulario.
- **No uses IA ni buscadores**: Todas las respuestas deben provenir de tu conocimiento y experiencia personal. No está permitido consultar ChatGPT, Google, Bing u otros servicios similares.

### **Completando el formulario paso a paso**

Como puedes ver en la imagen de ejemplo, el formulario de anotación contiene varios campos que debes completar:

1. **Pregunta**: En la parte izquierda verás la pregunta cultural que debes responder. En el ejemplo, la pregunta es "En los Juegos Olímpicos de Invierno, ¿cuál es el evento más popular para ver en Bolivia?".
2. **Adaptación pregunta:** Si entiendes la pregunta pero está formulada de una manera que no suena del todo natural en tu país, reescribe la pregunta aquí de manera correcta. Utiliza el menor número de cambios posibles (e.g. cambiar una palabra por un sinónimo).
3. **Respuesta 1 (campo obligatorio)**: Aquí debes ingresar tu respuesta principal. Recuerda responder de manera breve y específica. 
4. **Respuesta 2 y Respuesta 3 (campos opcionales)**: Si hay varias respuestas válidas para la pregunta en tu contexto cultural, puedes incluirlas en estos campos. Por ejemplo, si te preguntan por comidas típicas, podrías incluir diferentes platos en cada campo.
5. **Región específica (campo opcional)**: Si tu respuesta es más representativa de una región específica de tu país que de todo el territorio, escribe el nombre de esa región en este campo.

**Qué hacer si...**

1. **No sabes la respuesta**: Cuando entiendes la pregunta y es relevante para tu cultura pero desconoces la respuesta, pasa a la siguiente con las flechas en la esquina superior derecha de la pregunta.
2. **No hay respuesta:** Al final del formulario encontrarás opciones específicas para indicar por qué no puedes responder. Debes seleccionar una de estas opciones:
    - **No hay una respuesta específica a esta pregunta**: Cuando en tu cultura no existe una respuesta clara o consensuada. Excepto:
        - Si la respuesta depende de la región, responde y utiliza el campo “Región específica”.
        - Si la respuesta depende de otra característica que puedas especificar, utiliza las tres opciones disponibles y especifica la condición. Por ejemplo, Respuesta 1: “En el Norte, ….”, Respuesta 2: “En el Sur, …” ó Respuesta 1: “Menores de 35 años, …”, Respuesta 2: “Mayores de 35 años, …”
    - **Esta pregunta no aplica a mi cultura**: Cuando la pregunta hace referencia a algo que no es parte de tu contexto cultural.
    - Recuerda que si seleccionas alguna de estas opciones, debes escribir "No hay respuesta" en el campo “Respuesta 1”.

**Botones de acción**:
- Discard: Para descartar tu respuesta actual y comenzar de nuevo.
- Save as draft: Para guardar tu respuesta como borrador y continuarla más tarde.
- Submit: Para enviar tu respuesta y continuar con la siguiente pregunta.
- En la parte superior de la pantalla, verás un contador que indica en qué pregunta te encuentras (por ejemplo, "1 of 500"), lo que te permitirá hacer un seguimiento de tu progreso.