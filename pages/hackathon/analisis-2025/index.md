---
title: "Análisis Dataset 2025"
description: 
lang: es
cover: 
---

## 1. Resumen

Se analizaron **2.136 registros** de interacciones del LLM Arena, generados por **27 usuarios** de **9 países** hispanohablantes, evaluados contra **5 modelos LLM**. Cada registro contiene un prompt cultural, las respuestas de dos modelos, y la preferencia del anotador (preferencia clara, empate o ambas malas).

El análisis revela un dataset con una cobertura geográfica desigual, una concentración temática dominante en lenguaje y expresiones, y una calidad de prompts generalmente alta pero con áreas claras de mejora. El 27,6% de los veredictos son empates y el 10,3% marcan ambas respuestas como malas, lo cual reduce sustancialmente los pares utilizables para DPO.

---

## 2. Distribución por país

| País       | Prompts | % del total |
|------------|---------|-------------|
| Cuba       | 636     | 29,8%       |
| España     | 513     | 24,0%       |
| Colombia   | 324     | 15,2%       |
| Paraguay   | 195     | 9,1%        |
| Ecuador    | 153     | 7,2%        |
| Chile      | 121     | 5,7%        |
| Perú       | 118     | 5,5%        |
| México     | 41      | 1,9%        |
| Nicaragua  | 35      | 1,6%        |

 Cuba y España concentran el 53,8% del dataset. México, a pesar de ser el país hispanohablante más poblado, aporta solo 41 prompts (1,9%). Nicaragua está subrepresentada con solo 35 entradas. Esta distribución limita la validez del dataset como recurso pan-hispánico.

**Países ausentes:** No hay datos de Argentina, Venezuela, Bolivia, Uruguay, República Dominicana, Guatemala, Honduras, El Salvador, Costa Rica ni Panamá, lo que deja sin representar variedades lingüísticas cruciales como el rioplatense, el venezolano o el centroamericano.

![Distribución por país](/images/analisis-2025/01_prompts_por_pais.png)

---

## 3. Análisis por modelo

Se utilizaron 5 modelos en la Arena. Cada prompt fue evaluado por 2 modelos seleccionados aleatoriamente.

| Modelo | Victorias | Derrotas | Win-rate |
|--------|-----------|----------|----------|
| Claude 3.5 Sonnet | 358 | 180 | 0,665 |
| Gemini 2.0 Flash | 298 | 236 | 0,558 |
| Mistral Large 2411 | 253 | 263 | 0,490 |
| GPT-4o Mini | 246 | 283 | 0,465 |
| Llama 3.2 90B | 173 | 366 | 0,321 |

 Claude 3.5 Sonnet domina con un win-rate del 66,5%, mientras que Llama 3.2 solo gana el 32,1% de sus enfrentamientos. Esto sugiere que los modelos propietarios más grandes generan respuestas percibidas como más adecuadas culturalmente. Sin embargo, esto podría indicar también un sesgo hacia respuestas más largas o formales, no necesariamente más culturalmente informadas.

![Win-rate por modelo](/images/analisis-2025/02_modelos_winrate.png)
![Win-rate](/images/analisis-2025/09_winrate.png)

---

## 4. Análisis por categoría cultural

Se asignó a cada prompt una categoría cultural basada en análisis léxico del contenido del user_message:

| Categoría | Prompts | % |
|-----------|---------|---|
| Lenguaje y expresiones | 902 | 42,2% |
| Otro / Sin categoría clara | 341 | 16,0% |
| Gastronomía y alimentación | 214 | 10,0% |
| Identidad y valores | 135 | 6,3% |
| Arte y entretenimiento | 101 | 4,7% |
| Normas sociales y convivencia | 97 | 4,5% |
| Geografía y medio ambiente | 94 | 4,4% |
| Historia y política | 80 | 3,7% |
| Tradiciones y celebraciones | 76 | 3,6% |
| Educación y trabajo | 55 | 2,6% |
| Vida cotidiana | 41 | 1,9% |

El 42% de los prompts se centra en lenguaje y expresiones (significados, modismos, refranes), lo cual es valioso para evaluar variación dialectal pero genera un dataset temáticamente desbalanceado. Categorías como "vida cotidiana" y "tradiciones" están subrepresentadas, pese a ser fundamentales para la adecuación cultural.

Categoría "Otro": El 16% de prompts (341) no encaja claramente en las categorías definidas. Muchos son refranes sin contexto explícito, preguntas ambiguas o prompts que tocan varios temas sin profundizar en ninguno.

![Categorías globales](/images/analisis-2025/04_categorias_global.png)
![Categorías por país](/images/analisis-2025/03_categorias_por_pais.png)

---

## 5. Análisis de empates y "ambas malas"

| Veredicto | N | % |
|-----------|---|---|
| Preferencia clara | 1.328 | 62,2% |
| Empate (tie) | 589 | 27,6% |
| Ambas malas | 219 | 10,3% |

Solo el **62,2% de los registros son directamente utilizables para DPO** (requiere un par claro accepted/rejected). El alto porcentaje de empates (27,6%) sugiere que los modelos frecuentemente producen respuestas de calidad similar, o que los anotadores tienen dificultad para discriminar diferencias sutiles de adecuación cultural.

El 10,3% de "ambas malas" indica que en una de cada diez interacciones, ningún modelo produjo una respuesta culturalmente satisfactoria, lo cual subraya la necesidad de mejorar estos modelos en este dominio.

![Veredictos por país](/images/analisis-2025/07_ties_bothbad.png)

---

## 6. Análisis de longitud

| Métrica | Prompts | Resp. aceptadas | Resp. rechazadas |
|---------|---------|-----------------|------------------|
| Media | 237 chars | 1.254 chars | 1.143 chars |
| Mediana | 135 chars | 1.185 chars | 1.107 chars |
| Mínimo | 7 chars | 6 chars | 7 chars |
| Máximo | 2.600 chars | 7.419 chars | 7.176 chars |

 Las respuestas aceptadas son en promedio un 9,7% más largas que las rechazadas (1.254 vs 1.143 chars). Esto podría indicar un "sesgo de longitud" en las preferencias: los anotadores tienden a preferir respuestas más extensas, lo cual no siempre correlaciona con mayor adecuación cultural. El prompt más corto tiene solo 7 caracteres, lo que sugiere entradas triviales que deberían filtrarse.

![Distribución de longitudes](/images/analisis-2025/06_longitudes.png)

---

## 7. Análisis por usuario

El dataset fue generado por 27 usuarios, con una distribución muy desigual:

| Usuario (anonimizado) | Prompts | País |
|-----------------------|---------|------|
| Top 1 | 430 | Cuba |
| Top 2 | 206 | Cuba |
| Top 3 | 153 | Ecuador |
| Top 4 | 133 | Colombia |
| Top 5 | 120 | Chile |

 Los 2 principales contribuidores son de Cuba y aportan el 29,8% del dataset entre ambos. Esto introduce un sesgo de anotador significativo: las preferencias de 2 personas moldean un tercio de los datos de entrenamiento. La concentración por usuario (top 5 aporta el 53,5%) compromete la diversidad de perspectivas culturales.

![Top usuarios](/images/analisis-2025/08_top_usuarios.png)

---

## 8. Evaluación de calidad

Se evaluó cada prompt con un score de 0 a 1 basado en: presencia de system prompt, mención de país/rol, no trivialidad, anclaje cultural explícito, formato de pregunta/instrucción, y neutralidad.

| Métrica | Valor |
|---------|-------|
| Score medio global | 0,889 |
| Prompts triviales | 1 (0,0%) |
| Sin anclaje cultural explícito | 721 (33,8%) |
| Sin system prompt | 37 (1,7%) |

**Score por país (ordenado):**
Cuba: 1,00 · México: 0,99 · Colombia: 0,91 · Chile: 0,90 · Ecuador: 0,89 · Paraguay: 0,87 · Perú: 0,86 · Nicaragua: 0,83 · España: 0,75

 El 33,8% de prompts carece de anclaje cultural explícito en el texto del prompt (aunque el system message puede proporcionarlo). España presenta el score más bajo (0,75), posiblemente porque muchos prompts de España son culturalmente implícitos (refranes sin explicitar que son españoles). Cuba tiene el score más alto, en parte porque sus system prompts son consistentemente detallados.

![Calidad por país](/images/analisis-2025/05_calidad_por_pais.png)

---

## 9. Adecuación a la guía de anotación

Se verificó el cumplimiento de los criterios de la guía de anotación original:

### Criterios bien cumplidos
- **Uso de system prompt:** El 98,3% de los registros incluye un system prompt, cumpliendo la recomendación de definir un rol.
- **No trivialidad:** Solo 1 prompt es claramente trivial (saludo sin contenido), lo que indica que los anotadores entendieron la instrucción.
- **Variedad temática:** Se cubren 10 categorías culturales diferentes.

### Criterios con cumplimiento parcial
- **Anclaje cultural explícito:** El 33,8% de los prompts no menciona explícitamente un país o contexto cultural en el user_message, delegando ese contexto al system prompt. Esto es aceptable pero dificulta la reutilización del prompt fuera de la Arena.
- **Roles elaborados:** Muchos system prompts son genéricos ("Eres una persona de Cuba") sin detallar edad, género, ocupación o región, perdiendo riqueza contextual.
- **Neutralidad:** Aunque pocos prompts contienen sesgos evidentes, algunos incluyen presupuestos culturales que podrían condicionar la respuesta.

### Criterios con cumplimiento bajo
- **Diversidad geográfica:** Solo 9 de ~20 países hispanohablantes están representados.
- **Balance temático:** El 42% de prompts está en una sola categoría.
- **Diversidad de anotadores:** 2 personas generan el 30% de los datos.

---

## 10. Conclusiones y recomendaciones

### Para el dataset
1. **Filtrar registros de baja calidad:** Eliminar prompts triviales y aquellos sin ningún anclaje cultural (ni en prompt ni en system message).
2. **Descartar empates y "ambas malas" para DPO:** Solo 1.328 de 2.136 registros (62%) son directamente utilizables.
3. **Rebalancear geográficamente:** Priorizar la recolección de datos de México, Argentina, Venezuela y Centroamérica.
4. **Diversificar categorías:** Establecer cuotas mínimas por categoría para evitar la dominancia de "lenguaje y expresiones".

### Para la guía de anotación
1. Hacer obligatorio el campo de categoría cultural.
2. Requerir anclaje cultural explícito en el user_message (no solo en el system prompt).
3. Establecer longitud mínima de prompts (50 caracteres).
4. Limitar la contribución máxima por usuario para evitar sesgo de anotador.
5. Incluir ejemplos negativos más claros y criterios de rechazo.
6. Definir un protocolo para documentar la justificación de la preferencia.

### Para la edición 2026
1. Usar este dataset como línea base para medir la mejora.
2. Implementar una fase de validación cruzada obligatoria.
3. Considerar incluir un campo de "confianza" del anotador en su elección.
4. Explorar la inclusión de variantes dialectales del portugués (Brasil, Portugal).
