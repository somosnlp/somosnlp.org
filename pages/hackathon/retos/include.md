---
title: "Reto #HackathonSomosNLP 2025: Exámenes INCLUDE"
description: Cómo participar en este reto y ayudar a mejorar el conocimiento cultural de los modelos de lenguaje
lang: es
cover: https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg
---

## Protocolo de recolección de exámenes multilingües

A continuación presentamos el protocolo para participar en el proyecto INCLUDE centrado en la recolección de exámenes multilingües.

### 1. Buscar exámenes

Verifica que el examen cumple con los siguientes requisitos:
- **No es propietario.** Si la licencia restringe el uso comercial pero permite su redistribución con fines de investigación, entonces sí podemos usar este examen. Si la licencia es desconocida, incluye el examen.
- **Es un examen con formato de preguntas de opción múltiple** y tiene 4 opciones por pregunta.
- **Contiene las respuestas** y hay solo una respuesta correcta por pregunta.

Prioridades:
- El tema del examen debe estar relacionado con la **cultura** de un país: historia, literatura, etc. No son válidos los exámenes de ciencias exactas ni naturales (e.g. matemáticas, física).
- Prioriza buscar exámenes en lenguas originarias de LATAM o cooficiales de España. Son válidos los exámenes de idiomas y de nacionalización.

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
- Enlace del examen (si está disponible en línea, si no el nombre del libro o documento)
- Formato (e.g., PDF, página web, libro de texto, etc.)

### 3. Procesar los exámenes

Una vez que has encontrado un examen:

- Extrae las preguntas y respuestas y crea un archivo final en formato **JSON** (ejemplo a continuación).
- Sube el archivo final a un dataset en [huggingface.co/somosnlp-hackathon-2025](https://huggingface.co/somosnlp-hackathon-2025) con el nombre del examen. Si no formas parte de la organización, únete con esta [invitación](https://huggingface.co/somosnlp-hackathon-2025).
- En el canal de Discord [#examenes-include](https://discord.com/channels/938134488670675055/1326890438782750852), menciona a @mariagrandury y comparte el enlace al dataset creado.
- Verificaremos el contenido y te informaremos si se necesita hacer algún cambio.

Ejemplo JSON en el formato esperado:

```json
{
  "language": "es",
  "country": "España",
  "exam_name": "Examen Final de Física de Secundaria 2017",
  "source": "https://url-del-examen",
  "license": "Desconocida",
  "level": "Acceso a la Universidad",
  "category_en": "History",
  "category_original_lang": "Historia",
  "original_question_num": 1,
  "question": "¿En cuál de los siguientes años comenzó la Guerra Civil?",
  "options": [ "1936", "1937", "1938", "1939" ],
  "answer": 0
}
```
