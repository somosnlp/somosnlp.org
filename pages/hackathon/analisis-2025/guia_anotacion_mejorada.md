# Guía de Anotación Mejorada — Reto de Preferencias Culturales

## Cambios respecto a la guía 2025

Esta guía incorpora mejoras basadas en el análisis del dataset producido en la edición 2025 (2.136 registros, 9 países, 27 usuarios). Cada cambio está motivado por un hallazgo concreto.

---

### Cambio 1: Categoría cultural obligatoria (NUEVO)

**Problema detectado:** En 2025 no se pidió a los anotadores que clasificaran sus prompts. Al analizar el dataset resultante, el 42% quedó concentrado en una sola categoría (lenguaje y expresiones) y el 16% no encajó en ninguna categoría clara.

**Cambio:** Al enviar cada prompt, el anotador debe seleccionar una categoría de la siguiente taxonomía:

| Categoría | Descripción | Ejemplo |
|-----------|-------------|---------|
| Gastronomía y alimentación | Comidas, recetas, ingredientes, hábitos alimentarios locales | *¿Cómo se prepara un ajiaco en Colombia?* |
| Lenguaje y expresiones | Modismos, refranes, jerga, variaciones dialectales | *¿Qué significa "echar la foca" en Chile?* |
| Normas sociales y convivencia | Etiqueta, saludos, interacciones sociales, cortesía | *¿Cómo te diriges a un profesor universitario en Ecuador?* |
| Tradiciones y celebraciones | Fiestas, rituales, ceremonias, fechas clave | *¿Qué se hace durante la Diablada de Píllaro?* |
| Historia y política | Eventos históricos, instituciones, procesos políticos | *¿Qué significó la Revolución del Parque para los argentinos?* |
| Identidad y valores | Cosmovisión, religión, familia, identidad nacional | *¿Qué papel juega el compadrazgo en la vida social de Paraguay?* |
| Educación y trabajo | Sistema educativo, cultura laboral, economía informal | *¿Cómo funciona la minga como forma de trabajo comunitario en Ecuador?* |
| Geografía y medio ambiente | Paisajes, recursos, relación con el territorio | *¿Qué representa el páramo para las comunidades andinas?* |
| Arte y entretenimiento | Música, literatura, cine, deportes, ocio | *¿Por qué el béisbol es tan importante en Cuba?* |
| Vida cotidiana | Rutinas, transporte, compras, salud, seguridad | *¿Cómo es un día típico de compras en un mercado de Lima?* |

**Cuota mínima:** Cada equipo debe aportar prompts en al menos 4 categorías diferentes (de las 10 disponibles).

**Motivación:** Un dataset temáticamente diverso es más útil para alinear LLMs, ya que la adecuación cultural se manifiesta en todos los ámbitos, no solo en el léxico.

---

### Cambio 2: Anclaje cultural explícito obligatorio en el prompt (REFORZADO)

**Problema detectado:** El 33,8% de los prompts de 2025 carecía de mención cultural explícita en el user_message, dependiendo enteramente del system prompt para el contexto. Esto dificulta la reutilización de los datos fuera de la Arena y hace ambiguo el anclaje cultural.

**Cambio:** El user_message debe contener al menos una referencia explícita que lo sitúe culturalmente. Puede ser:
- Mención de un país, región o ciudad
- Referencia a una práctica, institución o elemento local específico
- Un refrán, expresión o término local (con indicación de origen)

**Ejemplo correcto:**
> *"¿Cómo celebran la Noche de San Juan en la costa gallega?"*

**Ejemplo incorrecto:**
> *"¿Cómo se celebra la noche de verano?"* (sin anclaje geográfico ni cultural)

**Motivación:** Un prompt sin anclaje cultural puede tener respuestas universalmente válidas, lo que anula su utilidad para entrenamiento en preferencias culturales.

---

### Cambio 3: System prompt estructurado (REFORZADO)

**Problema detectado:** Los system prompts variaron enormemente en formato y detalle (242 variantes distintas para 2.136 registros). Algunos eran tan genéricos como *"Una conversación entre un usuario y un modelo de lenguaje"*, mientras que otros eran muy detallados.

**Cambio:** El system prompt debe seguir esta estructura mínima:

```
Eres [rol] de [ciudad/región, país]. [Contexto adicional opcional: edad, ocupación, nivel educativo].
Responde de manera culturalmente adecuada, usando el español de [país/región].
Sé conciso y natural en tus respuestas.
```

**Campos obligatorios:** rol + país. **Campos recomendados:** región, ocupación, edad.

**Motivación:** La estandarización del system prompt permite análisis comparativos entre roles y países, y asegura que todos los registros tengan un mínimo de contexto.

---

### Cambio 4: Límite de contribuciones por usuario (NUEVO)

**Problema detectado:** En 2025, dos usuarios aportaron el 30% del dataset (636 registros de Cuba entre ambos). Esto introduce un sesgo de anotador severo: las preferencias individuales de 2 personas condicionan un tercio de los datos de entrenamiento.

**Cambio:**
- Máximo **150 prompts por persona** (100 obligatorios + 50 extra puntuables).
- Los equipos deben rotar entre sus miembros la tarea de envío de prompts.
- Cada equipo debe incluir contribuciones de al menos 2 personas diferentes.

**Motivación:** Diversificar las perspectivas de los anotadores es tan importante como diversificar los países representados. Un anotador individual tiene sesgos inconscientes que se amplifican con la repetición.

---

### Cambio 5: Longitud mínima y criterios de descarte (REFORZADO)

**Problema detectado:** Se encontraron prompts de 7 caracteres y respuestas de 6 caracteres. Aunque solo 1 prompt era trivial (saludo puro), varios eran demasiado breves para evaluar adecuación cultural.

**Cambio:**
- Longitud mínima del prompt: **50 caracteres**.
- Longitud mínima de las respuestas evaluadas: **100 caracteres** (si una respuesta es más corta, marcar como "ambas malas" o "no evaluable").
- Se rechazan automáticamente: saludos sin contenido, preguntas factuales simples (capitales, fechas), prompts en idiomas distintos al español.

**Motivación:** Los prompts muy cortos rara vez contienen suficiente información cultural para generar preferencias significativas.

---

### Cambio 6: Justificación obligatoria de la preferencia (NUEVO)

**Problema detectado:** El 27,6% de las evaluaciones resultaron en empate. No se puede saber si el anotador dudó genuinamente o si marcó empate por conveniencia. No hay forma de verificar si las preferencias se alinean con los criterios de evaluación.

**Cambio:** Al votar, el anotador debe proporcionar una breve justificación (1-2 oraciones, campo de texto libre) explicando el motivo de su elección. Categorías sugeridas:
- "Conocimiento cultural más preciso"
- "Uso más natural del español local"
- "Mejor adecuación al rol definido"
- "Respuesta más completa y útil"
- "Ambas equivalentes en calidad" (para empates)
- "Ninguna demuestra conocimiento cultural" (para ambas malas)

**Motivación:** La justificación permite filtrar votos arbitrarios, enriquecer el dataset con señales de calidad, e identificar los aspectos culturales más difíciles para los LLMs.

---

### Cambio 7: Criterios de evaluación ponderados (MODIFICADO)

**Problema detectado:** La guía 2025 listaba tres criterios (conocimiento cultural correcto, adecuación cultural, uso correcto del español local) sin indicar su peso relativo. Los anotadores no tenían claro qué priorizar cuando una respuesta era culturalmente adecuada pero lingüísticamente neutra, o viceversa.

**Cambio:** Establecer una jerarquía explícita:

1. **Corrección factual** (eliminatoria): Si una respuesta contiene errores objetivos sobre el país o la cultura, se descarta. No importa cuán bien escrita esté.
2. **Adecuación cultural** (peso alto): ¿La respuesta refleja la perspectiva, valores y prácticas del país/rol indicado?
3. **Variedad lingüística** (peso medio): ¿Usa el español del país/región? (voseo, léxico local, expresiones)
4. **Calidad comunicativa** (peso bajo): Claridad, estructura, utilidad de la respuesta.

**Motivación:** Sin jerarquía, los anotadores tienden a priorizar la calidad general de la respuesta por encima de la adecuación cultural, lo cual produce preferencias que no capturan la señal cultural deseada.

---

### Cambio 8: Validación cruzada obligatoria (REFORZADO)

**Problema detectado:** No se puede determinar del dataset 2025 cuántos registros pasaron por validación cruzada. La calidad depende enteramente de la autogestión de cada anotador.

**Cambio:**
- Todo prompt debe ser validado por al menos 1 persona que NO sea su autor.
- El validador debe ser de un país **diferente** al del prompt (para verificar que el anclaje cultural es comprensible) O del **mismo** país (para verificar la autenticidad cultural). Cada prompt recibe al menos una de estas dos validaciones.
- El validador puede marcar un prompt como: ✅ Válido / ⚠️ Necesita mejoras / ❌ Inválido (sin anclaje cultural, sesgado, trivial).

**Motivación:** La validación cruzada es el mecanismo más directo para asegurar calidad y detectar problemas antes de que los datos se usen para entrenamiento.

---

### Cambio 9: Diversidad geográfica mínima (NUEVO)

**Problema detectado:** 11+ países hispanohablantes no tienen representación en el dataset 2025. La muestra cubre solo 9 de los ~20 países donde el español es lengua oficial.

**Cambio:**
- Se establece un objetivo mínimo de **15 países** representados.
- Se incentiva especialmente la participación de países subrepresentados: Argentina, Venezuela, Bolivia, Uruguay, República Dominicana, Guatemala, Honduras, El Salvador, Costa Rica, Panamá.
- Equipos que aporten prompts de países no representados reciben puntos adicionales.

**Motivación:** Un dataset de adecuación cultural que no incluye las variedades rioplatense, venezolana o centroamericana tiene una utilidad limitada como recurso pan-hispánico.

---

### Cambio 10: Formato JSON extendido (MODIFICADO)

**Problema detectado:** El esquema 2025 no incluía campos para categoría, calidad, justificación ni metadatos del anotador.

**Cambio:** Nuevo esquema con campos adicionales:

```json
{
  "system_message": "Eres un pescador de Tumaco, Colombia...",
  "user_message": "¿Cómo se celebra la fiesta de la Virgen del Carmen en tu comunidad?",
  "accepted_response": "...",
  "accepted_model": "claude-3-5-sonnet@20240620",
  "rejected_response": "...",
  "rejected_model": "gpt-4o-mini",
  "username": "usuario@example.com",
  "tie": false,
  "both_bad": false,
  "categoria": "Tradiciones y celebraciones",
  "pais_prompt": "Colombia",
  "region_prompt": "Pacífico",
  "justificacion_preferencia": "La respuesta aceptada menciona la procesión marítima y el currulao, prácticas específicas del Pacífico colombiano.",
  "confianza_anotador": "alta"
}
```

**Campos nuevos:**
- `categoria` (obligatorio): una de las 10 categorías definidas.
- `pais_prompt` (obligatorio): país al que se refiere el prompt.
- `region_prompt` (opcional): región o ciudad específica.
- `justificacion_preferencia` (obligatorio): texto libre, 1-2 oraciones.
- `confianza_anotador` (obligatorio): "alta", "media" o "baja".

**Motivación:** Estos campos permiten filtrar, analizar y estratificar el dataset de forma mucho más granular, facilitando su uso para entrenamiento y evaluación.

---

## Resumen de cambios

| # | Cambio | Tipo | Problema que resuelve |
|---|--------|------|----------------------|
| 1 | Categoría cultural obligatoria | Nuevo | Desbalance temático (42% en una categoría) |
| 2 | Anclaje cultural explícito en prompt | Reforzado | 33,8% sin anclaje cultural |
| 3 | System prompt estructurado | Reforzado | 242 formatos diferentes, inconsistencia |
| 4 | Límite de contribuciones por usuario | Nuevo | 2 usuarios = 30% del dataset |
| 5 | Longitud mínima y criterios de descarte | Reforzado | Prompts de 7 chars, respuestas de 6 chars |
| 6 | Justificación de preferencia | Nuevo | 27,6% empates sin explicación |
| 7 | Criterios de evaluación ponderados | Modificado | Sin jerarquía clara entre criterios |
| 8 | Validación cruzada obligatoria | Reforzado | Sin control de calidad verificable |
| 9 | Diversidad geográfica mínima | Nuevo | Solo 9/20 países representados |
| 10 | Formato JSON extendido | Modificado | Sin campos para categoría ni justificación |

---

*Guía mejorada basada en el análisis del dataset 2025 — Hackathon SomosNLP 2026*
