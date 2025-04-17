---
title: "Reto #HackathonSomosNLP 2025: Preferencias"
description: Cómo participar en este reto y ayudar a alinear modelos de lenguaje con tu cultura
lang: es
cover: https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg
---

Diseña prompts que evalúen la adecuación cultural con tu país y elige la mejor respuesta en un LLM Arena. Los prompts y las respuestas serán recolectados y compartidos con todos los equipos participantes como dataset de preferencias v0 para la fase de alineamiento. Para este reto tendrás acceso a un LLM Arena con 5 modelos de gran tamaño o propietarios.

*14 de abril - 21 de abril | máx 3 ptos*

<center><a href="https://fastchat-webui-908374066028.us-central1.run.app/gradio/" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">¡Participa ya!</a></center>

Incentivos (los números se refieren a prompts respondidos validados):
- 100 por equipo = requisito para acceder a los 500 USD de la API de Cohere para el reto principal
- Cada 50 prompts por equipo = 0.5 ptos

Muchísimas gracias a:
- CENIA: Créditos API para los LLMs de la Arena
- El equipo: Gonzalo Fuentes, Diana Galván, Eugenio Herrera, Sebastián Cifuentes, Clemente y María Grandury

---

## Objetivo

El objetivo de este reto es crear entre todos los equipos un dataset que permita alinear LLMs con la cultura de los países de LATAM y la Península Ibérica. Para ello, cada equipo tiene que:

1. Diseñar prompts siguiendo la guía a continuación
2. Mandar sus prompts a un LLM Arena y elegir la mejor respuesta
3. Simultáneamente, ir validando los prompts y respuestas de otros equipos
4. El día 21 de abril publicaremos el conjunto de prompts y respuestas, llamémoslo “dataset v0”
5. Durante las siguientes 2 semanas cada equipo tendrá acceso a 500 USD en créditos de Cohere para procesar, filtrar y extender v0 y a GPUs L40S de Hugging Face para alinear un LLMs de 7B de parámetros.

Nota: para acceder a los créditos y GPUs es necesario contribuir 200 prompts **de calidad** al dataset.

Lee con atención las guías a continuación para más detalles de cada paso. Toma menos de 10 minutos y es imprescindible para asegurar la calidad y homogeneidad de los datos, muy importante para continuar vuestro proyecto.

## **0. Cómo crear equipos**

- Pueden ser homogéneos (todas las personas son del mismo país) o heterogéneos (distintos países de origen)
    - Equipos homogéneos
        - Lo más probable es que los prompts sean más o menos estándares, ya que estarán representando a una misma cultura. Las respuestas, sin embargo, puede que haya más de una que se considere culturalmente adecuada dependiendo de la región.
        - Podéis reutilizar prompts y responderlos teniendo en cuenta la perspectiva de diferentes regiones.
    - Equipos heterogéneos
        - Es probable que haya variedad tanto en los prompts como en las respuestas que se consideran culturalmente adecuadas.
        - Podéis reutilizar prompts y responderlos teniendo en cuenta la perspectiva de diferentes países.
- No es necesario que los prompts que mandéis al LLM Arena estén relacionados con el objetivo final con el que queráis alinear vuestro LLM.

> 💡 Recomendación
>
> 1. Decidir si desean trabajar en un equipo homogéneo o heterogéneo. Recomendamos un punto medio: equipos que incluyan 2 o 3 países.
> 2. Empezar a diseñar prompts representando diferentes enfoques de la cultura de los países representados.
> 3. Decidir el tema del proyecto (¡relacionado con la adecuación cultural!) para tenerlo en cuenta, si queréis, en el diseño de prompts. Igualmente tendréis créditos para extender el dataset común con más prompts específicamente creados para vuestro caso de uso.

## 1. Las definiciones

El principal objetivo del hackathon, y en particular de este reto, es mejorar la “adecuación cultural” de los LLMs, veamos qué significa esto. Comenzamos con unas definiciones:

<details>
<summary>Cultura</summary>

> *En su sentido etnográfico amplio, la cultura es ese todo complejo que incluye el conocimiento, la creencia, el arte, la moral, el derecho, la costumbre y cualquier otra capacidad y hábito adquirido por el hombre como miembro de la sociedad. ([ref](https://books.google.co.uk/books/about/Through_the_Language_Glass.html?id=6NOjIzNZvosC&redir_esc=y))*
> 

> *Solamente podemos considerar elementos de la cultura tradicional, aquellos que la comunidad conserva y transmite. […] Esta aceptación, y por tanto, la literariedad tradicional, popular o folclórica, dependerá de si el texto se ajusta a un lenguaje determinado, a estructuras específicas, coincide con determinados temas, y se crea desde una estética colectiva. ([ref](https://books.google.co.uk/books/about/M%C3%A9xico_tradicional.html?id=kbowDQAAQBAJ&redir_esc=y))*
> 

</details>

<details>
<summary>Multiculturalidad</summary>

> Existencia de varias culturas que conviven en un mismo espacio físico, geográfico o social. Abarca todas las diferencias que se enmarcan dentro de la cultura, ya sea, religiosa, lingüística, racial, étnica o de género. ([ref](https://www.significados.com/multiculturalidad/))
> 

> Ante la comunidad se reconoce la diversidad en todos los ámbitos y reconoce el respeto hacia ella misma, promoviendo derechos hacia cada una de las culturas incluidas.
> 

</details>

<details>
<summary>Adecuación cultural</summary>

- Algo es adecuado en relación al propósito de lo que se hace. En el caso del lenguaje, la adecuación puede entenderse como una relación entre el **propósito comunicativo** (intención o motivación del remitente al destinatario al comunicarse) ****y los **medios lingüísticos** elegidos.
- El **propósito comunicativo** se relaciona con qué y cómo queremos comunicar un mensaje. Los **medios lingüísticos** son las palabras y formas gramaticales que utilizamos. Por ejemplo, las siguientes dos oraciones cumplen el propósito de solicitar una explicación:
    1. ¿*Me podrías explicar, por favor?*
    2. *Explícame.*
    
    La oración #1 transmite una petición indirecta y cortés por medio del uso condicional simple (”podrías”). La inclusión de la frase “por favor” refuerza la cortesía. La oración #2 transmite una petición directa por medio de la forma gramatical del imperativo afirmativo del verbo “explicar”. Es menos cortés que la oración #1.

</details>

<details>
<summary>¿Cómo influye la cultura en la elección de medios lingüísticos?</summary>

- La cultura influye en las palabras (i.e., elecciones **léxicas**) y las **formas gramaticales** que utilizamos. Algunos ejemplos:

Elecciones léxicas

| Español peninsular | Español de América |
| --- | --- |
| Chaqueta | Saco |
| Ordenador | Computadora |
| Hora(s) punta | Hora(s) pico |
| Entrar *en* | Entrar *a* |
| Me da *vergüenza* | Me da *pena* |

Formas gramaticales

| Español peninsular | Español de América |
| --- | --- |
| Pretérito compuesto (e.g., *se ha ido*) | Pretérito simple (e.g., *se fue*) |

Distintos propósitos comunicativos

| Propósito comunicativo | Medio lingüístico | Ejemplo |
| --- | --- | --- |
| Calidez | Forma gramatical: Diminutivo | *¿Cómo estás, Edgarcito?* |
| Minimizar | Forma gramatical: Diminutivo | *En aquella casita.* |
| Afirmación | Elección léxica: Bueno | *Ah, bueno;* *Bueno…está bien* |
| Re-orientación | Elección léxica: Bueno | *Bueno…como te iba diciendo* |
| Corrección | Elección léxica: Bueno | *Bueno, nosotros lo decimos así no?* |

</details>

<details>
<summary>¿Cómo afecta la cultura en la capacidad de un LLM de entender un lenguaje?</summary>
  - En la comunicación → Los propósitos comunicativos se ven directamente afectados por las palabras y formas gramaticales usadas. Mientras más palabras de un país específico tenga una oración (por ejemplo, de Colombia), más difícil puede ser entenderla para alguien (o algo: un LLM) que no esté familiarizado con esa cultura.
  - En la percepción del mundo → Códigos morales (i.e., qué es bueno, qué es malo), actividades comunes (e.g., ir a la lucha libre o ir a una corrida de toros), etc.

</details>


## **2. Cómo diseñar los prompts**

### 2.1. Características generales

Los prompts deben ser:

- **No triviales**: evitar preguntas factual simples (e.g. “¿Cuál es la capital de Colombia?”).
- **Culturalmente situados**: tocan temas comunes en una región específica. **Utiliza** **roles para contextualizar tu pregunta**.
- **Neutrales**: no deben inducir una preferencia política, religiosa, o ideológica fuerte. Estos temas sí se pueden tratar pero sin incluir opiniones sobre cuál es “mejor”.
- No incluyas estereotipos: para tratar este tema participa en el reto del [Validador de estereotipos](https://somosnlp.org/hackathon/retos/estereotipos).

<details>
<summary>💡 ¿Qué es un rol?</summary>

Es una función que una **persona** desempeña en un lugar o en una situación. En el PLN, este concepto se empezó a adoptar en el área de diálogo y sistemas interactivos. De hecho, es común encontrar que se usa el término “persona” y no “rol”, aunque hacen referencia a lo mismo.

*¿Por qué es un concepto importante en los LLMs?*

La definición de roles se ha vuelto crucial para adaptar a los LLMs a contextos específicos. De acuerdo a [Tseng et al., 2024](https://aclanthology.org/2024.findings-emnlp.969/), hay dos casos de uso:

1. **Juego de roles**: Los LLM tienen la tarea de desempeñar los roles asignados y actuar según la retroalimentación del entorno, adaptándose al mismo.
2. **Personalización**: Los LLM tienen la tarea de gestionar las personalidades de los usuarios (e.g., antecedentes, como su país de origen) para satisfacer necesidades individualizadas y adaptarse a cada usuario.

Un ejemplo de caso #1 es si queremos simular la interacción entre personas de España. La persona que diseñe el prompt sólo debe especificar las características del rol; no toma parte en la interacción (i.e, no hay interacción humana).

En el caso #2, por el contrario, sí puede haber interacción humana. Al igual que en #1, existe un diseñador que define el rol que el LLM debe desempeñar. El LLM interactúa con un humano, respondiendo desde la perspectiva del rol asignado.

*¿Cómo definir un rol en el LLM Arena?*

Inclúyelo en el “System prompt”. Además del rol, recomendamos explicitar en el System prompt que la respuesta del LLM sea concisa y culturalmente adecuada.

</details>

### **2.2. Ejemplos de prompt (no exhaustivos)**

💡 Los prompts que se muestran a continuación son sólo una guía

- Respecto a los roles: ¡Cada equipo puede hacer su propia definición! Puede ser algo simple (e.g., sólo especificar el país de origen) o algo más elaborado (i.e., incluir género, edad, etc)
- Respecto a las preguntas: Tomar preguntas de un dataset o una encuesta es sólo una opción. ¡También pueden redactar sus propias preguntas!


#### 1. **Definir un rol, mostrar una situación con múltiples reacciones posibles** (como en [MultiTP](https://openreview.net/pdf?id=vrHErHkCNo))
    
<details>
<summary>Por ejemplo…</summary>

Rol: Persona de México

Situación: Uso de espacios exclusivos

```python
Imagina que estás en el transporte público y observas que alguien 
se sienta y/o pone sus cosas en uno de los asientos reservados 
para mujeres embarazadas, adultos mayores y personas 
con discapacidad.

Si ingresa una persona que tiene derecho a hacer uso de dichos 
asientos y no le es posible utilizarlos, los demás 
pasajeros reaccionan... 
```

Respuesta 1 (siguiendo el rol pre-definido)

```python
Con agresividad, exigiendo a la persona que está haciendo mal uso
de los asientos que se retire.
```

Respuesta 2

```python
Con indiferencia. Nadie dice nada. 
```

</details>

#### 2. **Definir un rol y presentar una pregunta abierta/subjetiva** (similar a lo que hizo [Dolly](https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm)) 

<details>
<summary>Por ejemplo…</summary>

Pregunta: generada por alguien de México

Rol: país de origen

```python
System prompt: Eres un asistente de IA. Responde como si fueras 
una persona nativa de {pais_de_origen}.

Pregunta: ¿Es mejor ir en coche o en metro al zócalo de la CDMX?

Respuesta (ejemplo):
                    Lo mejor es tomar el metro. Es más rápido y más seguro,
                    ya que es difícil encontrar un lugar para estacionarse.
                    Hay varios estacionamientos públicos, pero no son muy
                    seguros.
```

ó

```python
Pregunta: Quiero salir con mis amigos el fin de semana en CDMX.
                    ¿Qué podemos hacer para convivir y divertirnos?
                    Dame cinco ideas.
                    
Respuesta (ejemplo):
Si quieres pasar un fin de semana divertido con tus amigos, puedes:
1. Andar en bicicleta el domingo en Paseo de la Reforma
2. Ir por un café a Coyoacán
3. Visitar el castillo de Chapultepec
4. Ir a un karaoke en la Zona Rosa
5. Rentar una trajinera en Xochimilco
```

</details>

#### 3. **Definir un rol, un comportamiento y presentar una pregunta de opción múltiple** (como en [este paper](https://arxiv.org/pdf/2402.13231))

<details>
<summary>💡 Por ejemplo…</summary>

- Rol (características): Género, país de origen, educación, edad, clase social
- Pregunta: Pregunta abierta
- Set de respuestas: Hay dos posibilidades:
    1. Todas las opciones son culturalmente adecuadas, el modelo tendría que elegir la más adecuada para el rol y explicar por qué
    2. Sólo 1 de las opciones es culturalmente adecuada
- Comportamiento (la respuesta del LLM): Debe ser congruente con el rol

```python
Imagina que eres una persona {género} de {país}.
Tienes {edad} años y completaste el nivel educativo {educación}.
Te auto-defines como parte de una clase social {clase_social}. 

Responde a la siguiente pregunta desde esta perspectiva.
Considera que otras personas leerán lo que elijas; tu objetivo es 
convencerlos de que la elección se hizo desde la perspectiva de la
persona descrita arriba.

Selecciona sólo una opción y explica tu elección.

Pregunta: {pregunta}
Opciones: {set de respuestas}
```

</details>


#### 4. **Diálogos** (como hizo [OpenAssistant](https://arxiv.org/pdf/2304.07327))

<details>
<summary>💡 Por ejemplo…</summary>

Para generar un diálogo, simplemente continúa la conversación en el LLM Arena un par de interacciones.

```python
# Prompt
Recomiéndame lugares para salir con mis amigos el fin de semana en CDMX

# Respuesta (assistant)
Esta recomendación depende mucho del tipo de actividades que a ti y a
tus amigos les gusta hacer. Necesito más información, como el si
prefieren espacios abiertos o espacios cerrados.

# Respuesta (prompter)
Buen punto. Preferimos los espacios abiertos.

# Respuesta (assistant)
¡Muy bien! En ese caso, podrían ir a La Marquesa. Ahí encontrarán 
opciones para comer y divertirse al aire libre. 
```

</details>

### 2.3. Crea tu dataset de prompts

- Recomendamos guardar tus prompts en un archivo CSV
- Columnas:
    - necesarias: `prompt` y `pais`
    - opcional: añade las columnas que necesites, por ejemplo si has creado una plantilla con diferentes características sociales (e.g. `edad`) o regiones, `origen` si las preguntas vienen de un dataset existente, etc.
- Tendrás que crear un dataset de prompts en la org de Hugging Face del hackathon: https://huggingface.co/somosnlp-hackathon-2025 (si todavía no te has unido, utiliza esta [invitación](https://huggingface.co/organizations/somosnlp-hackathon-2025/share/BMALwncoPyZLRdPuzwugnsDzXHsbLnjjGD))

### **2.4. Recursos**

<details>
<summary>Datasets relacionados (podéis tomar las categorías para las preguntas)</summary>

- [BLEnD](https://arxiv.org/pdf/2406.09948): comida, deportes, familia, educación, días festivos/celebraciones/ocio, vida laboral
- [CoScript](https://aclanthology.org/2023.acl-long.236.pdf): 19 categorías derivadas de wikiHow (Fig 8)
- [CVQA](https://arxiv.org/pdf/2406.05967): 10 categorías (Table 1)
- [FrameNet](https://framenet.icsi.berkeley.edu/frameIndex): Base de datos extensa, varios frames (i.e., [marcos semánticos](https://www.aieti.eu/enti/frame_semantics_SPA/entrada.html))
    - Ejemplo: Ver los “lexical units” (hasta abajo) en el frame “personal relationships”
- [HellaSwag](https://huggingface.co/datasets/Rowan/hellaswag): Diversas actividades cotidianas tomadas de ActivityNet y wikiHow
    - Ver `activity_label` en el dataset
- [World Values Survey (WVS)](https://www.worldvaluessurvey.org/WVSContents.jsp): 14 sub-secciones
    - Listadas bajo la sección WVS wave 8 → Questionnaire and research topics

</details>

<details>
<summary>Ideas de categorías para preguntas abiertas</summary>

- Normas culturales
    - *¿Cómo responderías educadamente a un desconocido que se saltó la fila en un banco en Argentina?*
    - *¿Cómo te diriges a un profesor universitario en Ecuador?*
- Refranes y expresiones
    - *¿Qué significa el refrán {refrán} en {país}? Explica el significado e incluye un ejemplo.*
- Cuentos y canciones
    - *¿Cuál es la moraleja del cuento {cuento} en {país}?*

</details>

<details>
<summary>Ejemplos de prompts NO válidos</summary>

- Muy generales o universales: *“Explica la fotosíntesis.”*
- Demasiado subjetivos o sin marco cultural: *“¿Cuál es el mejor valor humano?”*
- Preguntas conflictivas sin propósito contextual: *“¿Quién fue peor: Franco o Pinochet?”*

</details>

## 3. Cómo elegir la mejor respuesta en el LLM Arena

- Una vez diseñes los prompts, utiliza el LLM Arena para generar respuestas con LLMs. No hace falta que guardes las respuestas, las guardamos automáticamente y las liberaremos a todos los equipos el 21 de abril.
- Lee con atención las dos respuestas generadas por el LLM. Luego, elige la opción que consideres **más adecuada** cultural y comunicativamente
- Para votar, ten en cuenta:
    - ✅ **Conocimiento cultural correcto,** la información objetiva tiene que ser correcta
    - ✅ **Adecuación cultural** al país y rol definidos
    - ✅ **Uso correcto del español local** (voseo, leísmo, modismos, etc.), la respuesta generada debería utilizar la misma variedad del español que la pregunta
        - Nota: No evalúes por gramática perfecta o estilo “neutro”, sino por lo que suena natural y correcto para la cultura del prompt.
- Selecciona:
    - **Respuesta A / B**: Si una es claramente más adecuada que la otra.
    - **Ambas buenas**: Si ambas son correctas, naturales y culturalmente adecuadas.
    - **Ambas malas**: Si ambas tienen errores graves de tono, contenido o adecuación cultural.

## 4. Validar preguntas y respuestas de otros equipos

- El miércoles, cuando haya un mínimo número de preguntas y respuestas, publicaremos el espacio de validación
- En el espacio podrás ver lo siguiente:
    - una pregunta
    - las dos respuestas generadas por los LLMs
    - la respuesta elegida
- Tendrás que anotar:
    1. Si la pregunta te parece que está bien diseñada teniendo en cuenta la guía anterior
    2. Si también elegirías esa respuesta o cambiarías
    3. Opcionalmente, puedes editar y mejorar la respuesta generada elegida
- Consideraciones para la validación:
    - Evita sesgos personales, evalúa desde la perspectiva del rol definido
    - Si el prompt no tiene anclaje cultural o ambas respuestas no se pueden evaluar razonablemente, repórtalo como inválido

## 5. Más retos

- El lunes 21 publicaremos el conjunto de preguntas y respuestas para que lo podáis utilizar para alinear vuestros LLMs. También incluiremos los datos del mini reto “[Validador de estereotipos](https://somosnlp.org/hackathon/retos/estereotipos)”.
- A partir del lunes 21, daremos acceso a los créditos de Cohere y las GPUs de Hugging Face a los equipos cuando alcancen el mínimo de prompts
- Recuerda que también puedes participar en los mini retos para conseguir más puntos
    - [INCLUDE](https://somosnlp.org/hackathon/retos/include) - Recolección de exámenes (hasta el 23 de abril, habrá premios y paper)
    - [BLEND](https://somosnlp.org/hackathon/retos/blend) - Preguntas de conocimiento cultural (hasta el 7 de mayo, habrá paper)


<center style="margin-top:40px;"><a href="https://fastchat-webui-908374066028.us-central1.run.app/gradio/" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">¡Participa ya!</a></center>

<center style="margin-top:40px;"><a href="https://somosnlp.org/hackathon/retos" target="_blank" style="background-color:gray; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Volver a los retos</a></center>
