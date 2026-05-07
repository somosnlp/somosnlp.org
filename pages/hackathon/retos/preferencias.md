---
title: "Reto #HackathonSomosNLP 2026: Preferencias"
description: Cómo participar en este reto y ayudar a alinear modelos de lenguaje con tu cultura
lang: es
cover: /images/eventos/260511_hackathon_eventbrite.png
---

Vamos a escribir entre todos los equipos **preguntas culturales** sobre nuestros países y a elegir cuál de las dos respuestas que da un modelo es mejor. Con eso crearemos una base de datos abierta para alinear a los modelos con nuestras culturas.

<!-- Relación con el reto principal: Las preguntas y las respuestas serán recolectadas y compartidas con todos los equipos participantes para la fase de alineamiento. Para este reto tendrás acceso a un LLM Arena con 5 modelos de gran tamaño o propietarios. -->

---

## 👣 Paso a paso

1. **Lee esta guía** (te llevará menos de 10 minutos) para aprender los conceptos clave y cómo escribir preguntas ("prompts") de calidad.
2. **Haz un test** de auto-evaluación que confirma que has entendido la guía.
3. **Escribe tus prompts** para que varios LLMs generen respuestas.
    - Si sabes programar, súbelos como CSV a la org de Hugging Face del hackathon (invitación).
    - Si prefieres utilizar una interfaz, mándalos aquí.
4. **Valida prompts** de otros equipos.
5. **Elige la mejor respuesta** entre las dos generadas para cada prompt validado.


<!-- TODO enlaces -->

🌎 **Importante:** escribe prompts **solo** sobre países que conozcas bien (porque has vivido ahí, has crecido ahí o tienes vínculos fuertes). Si no conoces la cultura, no podrás juzgar qué respuesta es mejor.

🚨 **Lee esta guía con calma.** Te llevará menos de 10 minutos. Es importante para que los datos que generemos entre todos los equipos sean de calidad. Los prompts y respuestas de personas que no hayan pasado el test o no hayan seguido las instrucciones no se incluirán en el dataset final y no puntuarán.

Recursos:
- Definiciones, ejemplos de prompts y datasets de preferencias a continuación
- [Charla sobre Red Teaming de Luis Vasquez @BSC](https://www.youtube.com/watch?v=pGOXE4rrO9M&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6)

<!-- 
: [somosnlp-hackathon/dataset-preferencias-dpo-v0](https://huggingface.co/datasets/somosnlp-hackathon/dataset-preferencias-dpo-v0)
5. Durante las siguientes 2 semanas cada equipo tendrá acceso a 500 USD en créditos de Cohere para procesar, filtrar y extender el dataset inicial v0 (v0 = versión 0 = versión inicial) y a GPUs L40S de Hugging Face para alinear un LLMs de 7B de parámetros. 
-->

---

## 🚀 Relación con el Hackathon

Esta recolección de datos está enmarcada en el #HackathonSomosNLP 2026 pero no es necesario participar en el reto principal.

### ✨ Incentivos

- Requisito para acceder a las GPUs = 100 prompts por equipo
- Cada 50 prompts por equipo = 0.5 ptos (máx 2 ptos)
- Cada 100 prompts por persona = 40 USD en créditos en el Hub de HF o libros de IA/PLN/lingüística (independientes del premio si vuestro equipo gana)
- Tendréis acceso a los datos generados por todos los equipos para utilizarlos en la fase de alineamiento, **una mayor calidad de los datos implica una mayor calidad de vuestro proyecto.**

Notas:
- Los números se refieren a prompts **validados**.
- **Antes** de mandar and validar prompts, es obligatorio haber aprobado el test de comprensión.


### 🤗 Cómo organizar tu equipo

Cada equipo es de 1-5 personas. Vuestro equipo puede ser:

- **Homogéneo** (todas las personas del mismo país). Los prompts representan una misma cultura, pero puede haber varias respuestas culturalmente válidas según la región. Podéis reutilizar prompts y responderlos teniendo en cuenta la perspectiva de diferentes regiones.
- **Heterogéneo** (personas de distintos países). Habrá variedad tanto en los prompts como en las respuestas que cada cultura considera adecuadas. Podéis reutilizar prompts y responderlos teniendo en cuenta la perspectiva de diferentes países.

💡 **Recomendación:** equipos con participantes de de 2 o 3 países.

---

## 📖 **Glosario**

- **Modelo de lenguaje (LLM)**: modelo de IA que genera texto, realmente es un modelo estadístico que genera secuencias de palabras probables.
- **Prompt**: pregunta o instrucción que le escribimos al modelo.
- **Dataset**: colección de datos (en este caso, prompts y respuestas).
- **LLM Arena**: web donde mandas un prompt y recibes la respuesta de dos modelos, tú eliges la mejor.
- **Alineamiento**: el proceso de "afinar" un modelo para que responda según preferencias humanas (en este caso, adecuado a la cultura).
- **Adecuación cultural**: que la respuesta encaje con la cultura del país (vocabulario, costumbres, contexto).

---

## 👀 1. ¿Qué es la "adecuación cultural"?

Este es el concepto clave del reto. **Adecuación cultural** quiere decir que una respuesta encaje bien con la cultura del país: usa el vocabulario adecuado, tiene en cuenta las costumbres y resulta natural para alguien de allí.

La mayoría de los modelos de IA se han entrenado sobre todo con datos en inglés y de cultura estadounidense. Cuando los usamos en español, las respuestas a veces **suenan raras**, no usan nuestro vocabulario o asumen costumbres que no son las nuestras. Crear datos como los de este reto sirve para corregir este comportamiento.

*Para saber más, haz click en las secciones desplegables a continuación.*

<details>
<summary>📚 Definición académica de "cultura"</summary>

> *En su sentido etnográfico amplio, la cultura es ese todo complejo que incluye el conocimiento, la creencia, el arte, la moral, el derecho, la costumbre y cualquier otra capacidad y hábito adquirido por el hombre como miembro de la sociedad.* ([referencia](https://books.google.co.uk/books/about/Through_the_Language_Glass.html?id=6NOjIzNZvosC&redir_esc=y))

> *Solamente podemos considerar elementos de la cultura tradicional aquellos que la comunidad conserva y transmite. [...] Esta aceptación, y por tanto la literariedad tradicional, popular o folclórica, dependerá de si el texto se ajusta a un lenguaje determinado, a estructuras específicas, coincide con determinados temas, y se crea desde una estética colectiva.* ([referencia](https://books.google.co.uk/books/about/M%C3%A9xico_tradicional.html?id=kbowDQAAQBAJ&redir_esc=y))

</details>

<div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:10px;">
    <img src="/images/infografias/adecuacion_cultural/es/1.jpg" alt="Infografía 1: definición de cultura" loading="lazy" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/es/2.jpg" alt="Infografía 2: definición de cultura" loading="lazy" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/es/3.jpg" alt="Infografía 3: definición de cultura" loading="lazy" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/es/4.jpg" alt="Infografía 4: definición de cultura" loading="lazy" style="width: 100%;">
</div>

<details>
<summary>📚 Multiculturalidad</summary>

> Existencia de varias culturas que conviven en un mismo espacio físico, geográfico o social. Abarca todas las diferencias que se enmarcan dentro de la cultura, ya sea religiosa, lingüística, racial, étnica o de género. ([referencia](https://www.significados.com/multiculturalidad/))
> 
> Ante la comunidad se reconoce la diversidad en todos los ámbitos y reconoce el respeto hacia ella misma, promoviendo derechos hacia cada una de las culturas incluidas.

</details>

<div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:10px;">
    <img src="/images/infografias/adecuacion_cultural/es/5.jpg" alt="Infografía 5: multiculturalidad" loading="lazy" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/es/6.jpg" alt="Infografía 6: multiculturalidad" loading="lazy" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/es/7.jpg" alt="Infografía 7: multiculturalidad" loading="lazy" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/es/8.jpg" alt="Infografía 8: multiculturalidad" loading="lazy" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/es/9.jpg" alt="Infografía 9: multiculturalidad" loading="lazy" style="width: 100%;">
</div>

<details>
<summary>📚 Adecuación cultural en detalle (propósito comunicativo y medios lingüísticos)</summary>

Algo es **adecuado** en relación al propósito que tiene. En el lenguaje, la adecuación se entiende como la relación entre:

- El **propósito comunicativo**: qué quieres transmitir y con qué intención.
- Los **medios lingüísticos**: las palabras y formas gramaticales que eliges.

Por ejemplo, estas dos frases tienen el mismo propósito (pedir una explicación), pero usan medios lingüísticos distintos:

1. *¿Me podrías explicar, por favor?*: petición indirecta y cortés (uso del condicional, "por favor").
2. *Explícame.*: petición directa (imperativo). Menos cortés que la #1.

</details>

<details>
<summary>📚 ¿Cómo influye la cultura en las palabras y la gramática que usamos?</summary>

La cultura afecta tanto a las **elecciones léxicas** (palabras) como las **formas gramaticales**. Algunos ejemplos:

**Vocabulario**

| Español peninsular | Español de América |
| --- | --- |
| Chaqueta | Saco |
| Ordenador | Computadora |
| Hora(s) punta | Hora(s) pico |
| Entrar *en* | Entrar *a* |
| Me da *vergüenza* | Me da *pena* |

**Gramática**

| Español peninsular | Español de América |
| --- | --- |
| Pretérito compuesto (*se ha ido*) | Pretérito simple (*se fue*) |

**Mismas palabras, distintos propósitos comunicativos**

| Propósito comunicativo | Medio lingüístico | Ejemplo |
| --- | --- | --- |
| Calidez | Forma gramatical: Diminutivo | *¿Cómo estás, Edgarcito?* |
| Minimizar | Forma gramatical: Diminutivo | *En aquella casita.* |
| Afirmación | Elección léxica: Bueno | *Ah, bueno. Bueno… está bien* |
| Re-orientación | Elección léxica: Bueno | *Bueno…como te iba diciendo* |
| Corrección | Elección léxica: Bueno | *Bueno, nosotros lo decimos así, ¿no?* |

</details>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    <img src="/images/infografias/adecuacion_cultural/es/10.jpg" alt="Adecuación Cultural 10" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/es/11.jpg" alt="Adecuación Cultural 11" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/es/12.jpg" alt="Adecuación Cultural 12" style="width: 100%;">
</div>

<details>
<summary>📚 ¿Cómo afecta la cultura en la capacidad de un LLM de entender un lenguaje?</summary>

- **En la comunicación:** cuantas más palabras o expresiones específicas de un país tenga una frase (por ejemplo, modismos colombianos), más difícil le será entenderla a una persona o a un modelo que no esté familiarizado con esa cultura.
- **En la visión del mundo:** códigos morales (qué es bueno, qué es malo), actividades comunes (*ir a la lucha libre*, *ir de tapas*), referencias compartidas, etc.

</details>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    <img src="/images/infografias/adecuacion_cultural/es/13.jpg" alt="Adecuación Cultural 13" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/es/14.jpg" alt="Adecuación Cultural 14" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/es/15.jpg" alt="Adecuación Cultural 15" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/es/16.jpg" alt="Adecuación Cultural 16" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/es/17.jpg" alt="Adecuación Cultural 17" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/es/18.jpg" alt="Adecuación Cultural 18" style="width: 100%;">
</div>

---

## 🎨 2. Cómo diseñar los prompts

### 2.1. Características generales

Tus prompts deben cumplir estas tres reglas:

- ✅ **No triviales**: evita preguntas con una sola respuesta correcta y obvia, tipo *"¿Cuál es la capital de Colombia?"*.
- ✅ **Culturalmente situados**: tocan algo propio de un país o región. **Usa "roles"** para dar contexto al modelo (ver abajo qué es un rol).
- ✅ **Neutrales**: no induzcas una opinión política, religiosa o ideológica fuerte. Estos temas se pueden tratar, pero sin pedirle al modelo que diga cuál es "mejor".

**¿Qué es un "rol"?** Indicar al modelo qué papel asumir antes de responder, por ejemplo: *"Eres una persona de Argentina de 30 años"*. Esto ayuda a que su respuesta encaje con esa cultura.

En la Arena, escribe el rol en el campo "System prompt". Te recomendamos también pedirle que la respuesta sea **concisa y culturalmente adecuada**.

<details>
<summary>📚 Más detalles académico sobres los roles (opcional)</summary>

Un rol es una función que una **persona** desempeña en un lugar o en una situación. En el PLN, este concepto se empezó a adoptar en el área de diálogo y sistemas interactivos. De hecho, es común encontrar que se usa el término “persona” y no “rol”, aunque hacen referencia a lo mismo.

*¿Por qué es un concepto importante en los LLMs?*

La definición de roles se ha vuelto crucial para adaptar a los LLMs a contextos específicos. De acuerdo a [Tseng et al., 2024](https://aclanthology.org/2024.findings-emnlp.969/), hay dos casos de uso:

1. **Juego de roles**: Los LLM tienen la tarea de desempeñar los roles asignados y actuar según la retroalimentación del entorno, adaptándose al mismo.
2. **Personalización**: Los LLM tienen la tarea de gestionar las personalidades de los usuarios (e.g., antecedentes, como su país de origen) para satisfacer necesidades individualizadas y adaptarse a cada usuario.

Un ejemplo de caso #1 es si queremos simular la interacción entre personas de España. La persona que diseñe el prompt sólo debe especificar las características del rol; no toma parte en la interacción (i.e, no hay interacción humana).

En el caso #2, por el contrario, sí puede haber interacción humana. Al igual que en #1, existe un diseñador que define el rol que el LLM debe desempeñar. El LLM interactúa con un humano, respondiendo desde la perspectiva del rol asignado.

</details>

### 2.2. Cuatro tipos de prompt (con ejemplos)

💡 **Estos son solo ejemplos.** Cada equipo puede inventar sus propios formatos. Los roles pueden incluir solo el país (*"una persona de Argentina"*) o ser tan detallados como queráis (género, edad, clase social, etc.). Las preguntas pueden venir de un dataset o encuesta existente o ser totalmente originales.

#### Tipo 1: Situación con varias reacciones posibles
*Inspirado en [MultiTP](https://openreview.net/pdf?id=vrHErHkCNo).*
    
<details>
<summary>Ver ejemplo</summary>

**Rol:** Persona de México
**Situación:** Uso de espacios exclusivos en el transporte público

```text
Imagina que estás en el transporte público y observas que alguien
se sienta y/o pone sus cosas en uno de los asientos reservados
para mujeres embarazadas, adultos mayores y personas
con discapacidad.

Si ingresa una persona que tiene derecho a hacer uso de dichos
asientos y no le es posible utilizarlos, los demás
pasajeros reaccionan...
```

**Posible respuesta A** (coherente con el rol):

```text
Con agresividad, exigiendo a la persona que está haciendo mal uso
de los asientos que se retire.
```

**Posible respuesta B:**

```text
Con indiferencia. Nadie dice nada.
```

</details>

#### Tipo 2: Pregunta abierta o subjetiva
*Similar a [Dolly](https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm).*

<details>
<summary>Ver ejemplo</summary>

**Rol:** Persona de México

```text
System prompt: Eres un asistente de IA. Responde como si fueras
una persona nativa de México.

Pregunta: ¿Es mejor ir en coche o en metro al zócalo de la CDMX?

Posible respuesta:
Lo mejor es tomar el metro. Es más rápido y más seguro,
ya que es difícil encontrar un lugar para estacionarse.
Hay varios estacionamientos públicos, pero no son muy seguros.
```

O bien:

```text
Pregunta: Quiero salir con mis amigos el fin de semana en CDMX.
¿Qué podemos hacer para convivir y divertirnos? Dame cinco ideas.

Posible respuesta:
Si quieres pasar un fin de semana divertido con tus amigos, puedes:
1. Andar en bicicleta el domingo en Paseo de la Reforma
2. Ir por un café a Coyoacán
3. Visitar el castillo de Chapultepec
4. Ir a un karaoke en la Zona Rosa
5. Rentar una trajinera en Xochimilco
```

</details>

#### Tipo 3: Pregunta de opción múltiple con un perfil detallado
*Inspirado en [este paper](https://arxiv.org/pdf/2402.13231).*

<details>
<summary>Ver ejemplo</summary>

- **Rol detallado:** género, país, educación, edad, clase social.
- **Pregunta:** abierta.
- **Opciones:** o bien todas son culturalmente adecuadas (el modelo elige la mejor para el rol y la justifica), o solo una lo es.
- **Lo que esperas del modelo:** una respuesta coherente con el rol.

```text
Imagina que eres una persona {género} de {país}.
Tienes {edad} años y completaste el nivel educativo {educación}.
Te auto-defines como parte de una clase social {clase_social}.

Responde a la siguiente pregunta desde esta perspectiva.
Considera que otras personas leerán lo que elijas; tu objetivo es
convencerlas de que la elección se hizo desde la perspectiva de la
persona descrita arriba.

Selecciona solo una opción y explica tu elección.

Pregunta: {pregunta}
Opciones: {opciones}
```

</details>


#### Tipo 4: Diálogo de varias interacciones
*Como hizo [OpenAssistant](https://arxiv.org/pdf/2304.07327).*

<details>
<summary>Ver ejemplo</summary>

Para crear un diálogo, continúa la conversación en la Arena durante un par de turnos.

```text
# Tú
Recomiéndame lugares para salir con mis amigos el fin de semana en CDMX.

# Modelo
Esta recomendación depende mucho del tipo de actividades que a ti
y a tus amigos les gusta hacer. ¿Prefieren espacios abiertos
o cerrados?

# Tú
Buen punto. Preferimos los espacios abiertos.

# Modelo
¡Muy bien! En ese caso podrían ir a La Marquesa. Ahí encontrarán
opciones para comer y divertirse al aire libre.
```

</details>

### 2.3. Guarda tus prompts y publícalos

1. Guarda tus prompts en un archivo **CSV** (lo puedes hacer en una hoja de cálculo y exportarlo). El número máximo de prompts por **persona** (no por equipo) son 100.
2. Incluye al menos estas columnas:
   - `prompt`: el texto de la pregunta.
   - `pais`: el país al que se refiere.
3. *(Opcional)* Añade columnas con diferentes características demográficas: `edad`, `genero`, `region`, etc.
4. **Sube el archivo** como un dataset en la [organización del hackathon en Hugging Face](https://huggingface.co/somosnlp-hackathon). Si todavía no formas parte, [únete con esta invitación](https://huggingface.co/organizations/somosnlp-hackathon/share/BMALwncoPyZLRdPuzwugnsDzXHsbLnjjGD).

**Preguntas sintéticas:** Si sabes programar, puedes generar **y revisar** preguntas con ayuda de LLMs. En este caso, es obligatorio verificar que la licencia del modelo permite entrenar otros LLMs con sus outputs e incluir una columna `modelo_gen` indicando el nombre del modelo. Recuerda que los prompts solo puntuarán si son validados por otras personas participantes, por favor, no hagáis perder el tiempo a compañeros/as mandando prompts sin revisar. Si detectamos este comportamiento, el equipo será eliminado.

### 2.4. Recursos para inspirarte

<details>
<summary>📁 Datasets de los que podéis sacar categorías de preguntas</summary>

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
<summary>💡 Ideas de categorías para preguntas abiertas</summary>

- Normas culturales
    - *¿Cómo responderías educadamente a un desconocido que se saltó la fila en un banco en Argentina?*
    - *¿Cómo te diriges a un profesor universitario en Ecuador?*
- Refranes y expresiones
    - *¿Qué significa el refrán {refrán} en {país}? Explica el significado e incluye un ejemplo.*
- Cuentos y canciones
    - *¿Cuál es la moraleja del cuento {cuento} en {país}?*

</details>

<details>
<summary>🚫 Ejemplos de prompts NO válidos</summary>

- Muy generales o universales: *“Explica la fotosíntesis.”*
- Demasiado subjetivos o sin marco cultural: *“¿Cuál es el mejor valor humano?”*
- Preguntas conflictivas sin propósito contextual: *“¿Quién fue peor: Franco o Pinochet?”*

</details>

---

## 🔍 3. Valida prompts

Validar prompts de otros equipos es **igual de importante** que generar tus propios prompts. Te ayuda a aprender lo que funciona y mejora la calidad del dataset común.

Pasos:

1. Abre el [espacio de validación](https://huggingface.co/spaces/somosnlp/validacion-preferencias) y elige un país cuya cultura conozcas bien.
2. Verás una pregunta.
3. Selecciona "OK" si:
   - La **pregunta** está bien diseñada según esta guía y el prompt **tiene anclaje cultural**
   - *(Opcional)* Edita y mejora la pregunta para que sea aún mejor.

---

## ✅ 4. Cómo elegir la mejor respuesta

En el Arena, verás respuestas de **dos modelos** sin saber cuál es cuál. Tu tarea es elegir cuál encaja mejor con la cultura del prompt. (No hace falta que guardes nada, todo se guarda automáticamente.)

**Lee las dos respuestas con calma y fíjate en:**

- ✅ **¿Es información correcta?** Los datos objetivos no pueden estar mal.
- ✅ **¿Encaja con la cultura del país y del rol?** Evalúa **desde la perspectiva del rol definido** en el prompt, no desde la tuya.
- ✅ **¿Suena natural en el español local?** (voseo, leísmo, modismos…). La respuesta debe usar la misma variedad de español que la pregunta. **No** evalúes buscando gramática "perfecta" o un español "neutro" (¡no existe!) busca lo que suene natural para esa cultura.

Después, elige una opción:

- **Respuesta A** o **B**: si una es claramente mejor.
- **Ambas buenas**: si las dos son correctas y naturales.
- **Ambas malas**: si las dos tienen errores graves de tono, contenido o adecuación cultural.

<!-- TODO opcionalmente mejorar la respuesta correcta, no? -->

---

## 🚀 ¿Empezamos?

Lee la guía de diseño de prompts de preferencias
Completa este test de auto-evaluación
Si no te queda algo claro pregúntanos
Diseña tus prompts y súbelos como dataset a la org de Hugging Face del hackathon (invitación)
Evalúa prompts de otros equipos
Vota cuáles son las mejores respuestas

<div style="display:flex; flex-wrap:wrap; justify-content:center; gap:12px; margin:24px 0;">
  <a href="https://forms.gle/itbDvVxD2iG5nzsC6" target="_blank" rel="noopener" style="background-color:#FACC15; color:#1f2937; font-weight:600; padding:12px 20px; text-decoration:none; border-radius:6px; display:inline-block;">Hacer el test de comprensión ↗</a>
  <!-- <a href="https://fastchat-webui-908374066028.us-central1.run.app/gradio/" target="_blank" rel="noopener" style="background-color:#FACC15; color:#1f2937; font-weight:600; padding:12px 20px; text-decoration:none; border-radius:6px; display:inline-block;">Ir a la LLM Arena ↗</a>
  <a href="https://huggingface.co/spaces/somosnlp/validacion-preferencias" target="_blank" rel="noopener" style="background-color:#FACC15; color:#1f2937; font-weight:600; padding:12px 20px; text-decoration:none; border-radius:6px; display:inline-block;">Validar prompts ↗</a> -->
</div>

<!-- <div style="text-align:center; margin-top:24px;">
  <a href="https://somosnlp.org/hackathon/retos" style="background-color:#4b5563; color:white; padding:10px 20px; text-decoration:none; border-radius:6px; display:inline-block;">← Volver a todos los retos</a>
</div> -->

<!-- TODO enlaces -->

<!-- 
## 🌍 5. Más retos

- El lunes 21 publicaremos el conjunto de preguntas y respuestas para que lo podáis utilizar para alinear vuestros LLMs. También incluiremos los datos del mini reto “[Validador de estereotipos](https://somosnlp.org/hackathon/retos/estereotipos)”.
- A partir del lunes 21, daremos acceso a los créditos de Cohere y las GPUs de Hugging Face a los equipos cuando alcancen el mínimo de prompts, menciona a @mariagrandury en el hilo de tu equipo del canal #encuentra-equipo
- Recuerda que también puedes participar en los mini retos para conseguir más puntos
    - [INCLUDE](https://somosnlp.org/hackathon/retos/include) - Recolección de exámenes (hasta el 30 de abril, habrá premios y paper)
    - [BLEND](https://somosnlp.org/hackathon/retos/blend) - Preguntas de conocimiento cultural (hasta el final del hackathon, habrá paper)


<div style="display: flex; justify-content: center; gap: 20px;">
  <a href="https://forms.gle/itbDvVxD2iG5nzsC6" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Verifica que has comprendido la guía</a>
  <a href="https://huggingface.co/spaces/somosnlp/validacion-preferencias" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Valida prompts de otros equipos</a>
  <a href="https://fastchat-webui-908374066028.us-central1.run.app/gradio/" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Manda tus prompts a la Arena</a>
</div>

<center style="margin-top:40px;"><a href="https://somosnlp.org/hackathon/retos" target="_blank" style="background-color:gray; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Volver a los retos</a></center> -->
