---
title: Evalúa la recuperación de páginas de un PDF con IDs de origen
description: Recorta un PDF ficticio, conserva la referencia a cada página original y verifica con Python qué página recupera cada pregunta.
date: 2026-11-21T00:00:00.000+00:00
lang: es
duration: 6min
author: Zen
github: https://github.com/zenoven
---

Si extraes las páginas 2 y 4 de un PDF, pasan a ocupar las posiciones 1 y 2 en el archivo resultante. Al evaluar la recuperación de información, una referencia a la «página 2» puede terminar señalando dos fragmentos distintos. Un identificador que combine el documento y su página física de origen permite comprobar si el buscador devolvió la evidencia correcta y volver al documento inicial para revisar el error.

En este ejercicio crearemos el manual ficticio de una biblioteca con cinco páginas. Las páginas 2 y 4 contienen las reglas de préstamo y devolución. La página 5 contiene una clave creada para el ejercicio. Si se incluye en el índice, una consulta podría recuperar esa clave en lugar de la regla que debería citar. Dejaremos la clave fuera del PDF recortado y guardaremos las respuestas esperadas aparte del corpus.

## Prepara el corpus y su manifiesto

Usa Python 3.10 o posterior. Para instalar las dos dependencias en un entorno virtual, ejecuta `python -m pip install pypdf==6.12.2 reportlab==5.1.0`. Guarda el siguiente script como `demo.py` y ejecútalo con `python demo.py` en una carpeta vacía. Genera las entradas y las salidas en esa carpeta.

```python
import json
import re
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

origen = Path("biblioteca-ficticia.pdf")
subset = Path("biblioteca-corpus.pdf")
paginas = [
    "Portada: manual ficticio de la biblioteca.",
    "El préstamo de una tableta dura siete días.",
    "El club de lectura se reúne los jueves.",
    "La devolución se realiza en el mostrador de la planta baja.",
    "Clave de evaluación: siete días y mostrador de la planta baja.",
]
pdf = canvas.Canvas(str(origen), invariant=1)
for texto in paginas:
    pdf.drawString(50, 750, texto)
    pdf.showPage()
pdf.save()

seleccion = [2, 4]
lector = PdfReader(origen)
escritor = PdfWriter()
for numero in seleccion:
    escritor.add_page(lector.pages[numero - 1])
escritor.write(subset)

filas = [
    {
        "id": f"biblioteca-ficticia:p{numero}",
        "pagina_pdf_origen": numero,
        "pagina_pdf_recorte": posicion,
        "texto": pagina.extract_text().strip(),
    }
    for posicion, (numero, pagina) in enumerate(
        zip(seleccion, PdfReader(subset).pages, strict=True), start=1
    )
]
assert [fila["texto"] for fila in filas] == [paginas[1], paginas[3]]
Path("corpus.jsonl").write_text(
    "".join(json.dumps(fila, ensure_ascii=False) + "\n" for fila in filas),
    encoding="utf-8",
)

def terminos(texto):
    return set(re.findall(r"[^\W\d_]+", texto.casefold()))

consultas = [
    ("¿Cuánto dura el préstamo de una tableta?", "biblioteca-ficticia:p2"),
    ("¿Dónde se realiza la devolución?", "biblioteca-ficticia:p4"),
]
aciertos = 0
for pregunta, esperada in consultas:
    buscados = terminos(pregunta)
    candidata = max(filas, key=lambda fila: len(buscados & terminos(fila["texto"])))
    aciertos += candidata["id"] == esperada
    print(f'{esperada} -> {candidata["id"]}')
print(f"Recall@1 del ejemplo: {aciertos}/{len(consultas)}")
assert aciertos == len(consultas)
```

```text
biblioteca-ficticia:p2 -> biblioteca-ficticia:p2
biblioteca-ficticia:p4 -> biblioteca-ficticia:p4
Recall@1 del ejemplo: 2/2
```

Cada línea de `corpus.jsonl` registra tanto la página de origen como su posición en el recorte. Por ejemplo, la segunda fila tiene `pagina_pdf_origen: 4` y `pagina_pdf_recorte: 2`. `PdfReader.pages` usa índices desde cero, así que el código resta uno al pasar el número físico a [pypdf](https://pypdf.readthedocs.io/en/stable/user/merging-pdfs.html). El número físico puede diferir del impreso si hay una portada o páginas preliminares con numeración romana.

Como comprobación visual opcional, abre el PDF original y revisa la portada y la página de devoluciones. También puedes abrir el archivo ficticio en la herramienta [Extraer páginas de PDF de PDF Fan](https://pdf.fan/es/extraer-paginas-pdf/), seleccionar las páginas 2 y 4 y comparar el orden con el manifiesto. Para reproducir el ejercicio, basta con el script. La extracción de páginas por sí sola tampoco certifica que se hayan eliminado metadatos o anexos.

## Comprueba qué mide la prueba

En el ejemplo hay una página esperada por pregunta. Contamos un acierto cuando el ID del primer resultado coincide con esa página. El solapamiento de palabras sirve como línea base y el orden de las filas desempata. Los dos aciertos confirman el recorrido de los IDs en esta prueba pequeña. Para ver el límite de la búsqueda, añade la consulta «¿Cuántas jornadas puedo quedarme con el dispositivo?» con la página 2 como referencia. El único término compartido con ambas páginas es «el». Invierte el orden de las filas antes de la búsqueda y verás que la página que queda primero se lleva el empate.

Para una prueba de trabajo, incorpora consultas que usen paráfrasis y páginas difíciles de distinguir. Etiqueta todas las evidencias válidas si varias páginas contienen la respuesta y conserva esa decisión junto a cada pregunta. Si las preguntas requieren dos páginas a la vez, añade una comprobación que exija recuperar ambas. Mantén las preguntas y etiquetas fuera del índice, usa IDs que incluyan la versión del documento y divide el conjunto por documento o familia documental si tienes versiones casi idénticas. Con PDFs escaneados, revisa la salida de OCR antes de interpretar los fallos de recuperación.

La iniciativa [Dona tu corpus](https://somosnlp.org/donatucorpus) presenta formas de colaborar con datos para la comunidad. Para compartir un corpus real, revisa primero que cuentas con los permisos y que el contenido se puede publicar.

*Transparencia: colaboro con PDF Fan. Usé asistencia de IA al preparar el borrador y ejecuté el ejemplo para verificar su resultado.*
