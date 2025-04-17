---
title: "Reto #HackathonSomosNLP 2025: Exámenes INCLUDE"
description: Cómo participar en este reto y ayudar a mejorar el conocimiento cultural de los modelos de lenguaje
lang: es
cover: https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg
---

Busca exámenes de opción múltiple de tu país para evaluar el conocimiento de los LLMs. Prioriza exámenes en lenguas distintas al español y/o centrados en temas culturales (e.g. historia, literatura). Utilizaremos estas preguntas y respuestas para extender el benchmark abierto INCLUDE.

*9 de abril - 21 de abril | máx 1 pto*

<center><a href="https://docs.google.com/spreadsheets/d/1QLPQ7gah9yzG3-1BPIw5Jp994Rz8L_yZT8obgWH8S2Y" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">¡Participa ya!</a></center>

Incentivos (los números se refieren a preguntas con sus correspondientes respuestas):
- Por equipo:
    - 100 preguntas en total = 0.5 ptos
    - 200 preguntas en total = 1 pto
- Por persona:
    - Cada 100 preguntas = 50 USD en créditos GPU o libros
    - 300 por persona = invitación al Slack del proyecto global y co-autoría en el paper de INCLUDE v2
- OJO: ¡Los exámenes tienen que cumplir los requisitos!

Recursos:
- [Taller de Alfonso Amayuelas](https://www.youtube.com/watch?v=Jk70bSw4tTo&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6&index=1)
- Repo de GitHub con el código del taller: [amayuelas/corpus-automation](https://github.com/amayuelas/corpus-automation)

---

## Protocolo de recolección de exámenes multilingües

A continuación presentamos el protocolo para participar en el proyecto INCLUDE centrado en la recolección de exámenes multilingües.

### 1. Buscar exámenes

Verifica que el examen cumple con los siguientes requisitos:
- **No es propietario.** Si la licencia restringe el uso comercial pero permite su redistribución con fines de investigación, entonces sí podemos usar este examen. Si la licencia es desconocida, incluye el examen.
- **Es un examen con formato de preguntas de opción múltiple** y tiene 4 opciones por pregunta.
- **Contiene las respuestas** y hay solo una respuesta correcta por pregunta.
- El tema del examen debe estar relacionado con la **cultura** de un país (e.g., historia, literatura) o ser información regional (e.g. carnet de conducir). No son válidos los exámenes de ciencias exactas ni naturales (e.g. matemáticas, física).
- Prioriza buscar exámenes en **lenguas** originarias de LATAM o cooficiales de España. También son válidos los exámenes de estas regiones en español.
- A menos que sea un examen con un componente cultural muy importante, no buscamos más exámenes de España en español.

Ideas para encontrar exámenes:
- Exámenes de acceso a la universidad
- Exámenes del colegio o de instituto
- Exámenes habilitantes de profesiones (medicina, psicología, derecho, etc.)
- Exámenes de idiomas
- Exámenes de nacionalización
- Licencias de conducir
- Preguntas de concursos estilo "¿Quién quiere ser millonario?"
- Preguntas de juegos tipo Trivial Pursuit
- Tests de autoevaluación en libros de texto

Recuerda: no tiene por qué ser un examen digitalizado, también puedes escanear libros o hacer fotos de documentos.

### 2. Añadir exámenes a la hoja de cálculo

Cuando encuentres un examen, guarda su URL/nombre/artículo/documentación de origen y agrégalo a la [hoja de cálculo](https://docs.google.com/spreadsheets/d/1QLPQ7gah9yzG3-1BPIw5Jp994Rz8L_yZT8obgWH8S2Y/edit?usp=sharing).

Incluye lo siguiente:
- Tu nombre
- Tu nombre en Discord
- Nombre del examen (lo más detallado posible)
- Lengua y país de origen del examen
- Dominio del examen (e.g., Literatura, Derecho, Conducir, etc.)
- Nivel del examen
- Número de preguntas
- Origen del examen (URL si está disponible en línea, nombre del libro o URL al documento PDF en tu Drive, etc.)
- Formato original (e.g., PDF, página web, libro de texto, etc.)

### 3. Procesar los exámenes

Una vez que has encontrado un examen:

- Extrae las preguntas y respuestas y crea un archivo final en formato **JSON** (ejemplo a continuación).
    - Te recomendamos el [taller de Alfonso Amayuelas](https://www.youtube.com/watch?v=Jk70bSw4tTo&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6&index=1)
    - Repo de GitHub con el código del taller: [amayuelas/corpus-automation](https://github.com/amayuelas/corpus-automation)
- Sube el archivo final a un dataset **PRIVADO** en [huggingface.co/somosnlp-hackathon-2025](https://huggingface.co/somosnlp-hackathon-2025) con el nombre del examen. Si no formas parte de la organización, únete con esta [invitación](https://huggingface.co/somosnlp-hackathon-2025).
- En el canal de Discord [#examenes-include](https://discord.com/channels/938134488670675055/1326890438782750852), menciona a @mariagrandury y comparte el enlace al dataset creado.
- Verificaremos el contenido y te informaremos si se necesita hacer algún cambio.

Ejemplo JSON en el formato esperado:

```json
{
  "language": "es",
  "country": "España",
  "exam_name": "Examen final de Historia de España de Secundaria 2017",
  "source": "https://url-del-examen",
  "license": "CC-BY-SA",
  "level": "Acceso a la universidad",
  "category_en": "History",
  "category_original_lang": "Historia",
  "original_question_num": 1,
  "question": "¿En cuál de los siguientes años comenzó la Guerra Civil?",
  "options": [ "1936", "1937", "1938", "1939" ],
  "answer": 0
}
```

## Equipo

Muchísimas gracias a:
- EPFL: Premios y organización del equipo global
- El equipo: María Grandury y Angelika Romanou

<center style="margin-top:40px;"><a href="https://docs.google.com/spreadsheets/d/1QLPQ7gah9yzG3-1BPIw5Jp994Rz8L_yZT8obgWH8S2Y" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">¡Participa ya!</a></center>

<center style="margin-top:40px;"><a href="https://somosnlp.org/hackathon/retos" target="_blank" style="background-color:gray; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Volver a los retos</a></center>
