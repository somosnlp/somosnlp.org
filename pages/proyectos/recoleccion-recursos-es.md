---
title: Recolección de recursos
description: 
date: 2026-04-01T18:00:00.000+00:00
lang: es
duration: 
cover:
---

# Datasheets

3.1 Motivación
Las preguntas de esta sección tienen como objetivo principal alentar a los creadores de datasets a articular claramente sus razones para crear el dataset y promover la transparencia sobre los intereses de financiación. Esto último puede ser especialmente relevante para los datasets creados con fines de investigación.
- ¿Con qué propósito fue creado el dataset? ¿Se tenía en mente alguna tarea específica? ¿Existía alguna brecha específica que era necesario cubrir? Por favor, proporcione una descripción.
- ¿Quién creó el dataset (p. ej., qué equipo o grupo de investigación) y en nombre de qué entidad (p. ej., empresa, institución u organización)?
- ¿Quién financió la creación del dataset? Si existe una subvención asociada, proporcione el nombre del otorgante y el nombre y número de la subvención.
- ¿Algún otro comentario?

3.2 Composición
Los creadores de datasets deben leer estas preguntas antes de realizar cualquier recopilación de datos y luego proporcionar respuestas una vez que la recopilación esté completa. La mayoría de las preguntas de esta sección tienen como objetivo proporcionar a los consumidores de datasets la información que necesitan para tomar decisiones informadas sobre el uso del dataset para las tareas que han elegido. Algunas preguntas están diseñadas para obtener información sobre el cumplimiento del Reglamento General de Protección de Datos (RGPD) de la UE o regulaciones comparables en otras jurisdicciones. Las preguntas que se aplican únicamente a los datasets relacionados con personas se agrupan al final de la sección. Recomendamos adoptar una interpretación amplia sobre si un dataset está relacionado con personas. Por ejemplo, cualquier dataset que contenga texto escrito por personas está relacionado con personas.
- ¿Qué representan las instancias que componen el dataset (p. ej., documentos, fotos, personas, países)? ¿Existen múltiples tipos de instancias (p. ej., películas, usuarios y valoraciones; personas e interacciones entre ellas; nodos y aristas)? Por favor, proporcione una descripción.
- ¿Cuántas instancias hay en total (de cada tipo, si corresponde)?
- ¿El dataset contiene todas las instancias posibles o es una muestra (no necesariamente aleatoria) de instancias de un conjunto mayor? Si el dataset es una muestra, ¿cuál es el conjunto mayor? ¿Es la muestra representativa del conjunto mayor (p. ej., cobertura geográfica)? En caso afirmativo, describa cómo se validó/verificó esta representatividad. Si no es representativa del conjunto mayor, describa por qué no (p. ej., para cubrir una gama más diversa de instancias, porque se retuvieron o no estaban disponibles algunas instancias).
- ¿De qué datos consta cada instancia? ¿Datos "crudos" (p. ej., texto sin procesar o imágenes) o características? En cualquier caso, proporcione una descripción.
- ¿Existe una etiqueta o variable objetivo asociada a cada instancia? En caso afirmativo, proporcione una descripción.
- ¿Falta alguna información en instancias individuales? En caso afirmativo, proporcione una descripción que explique por qué falta esta información (p. ej., porque no estaba disponible). Esto no incluye información eliminada intencionalmente, pero podría incluir, por ejemplo, texto redactado.
- ¿Las relaciones entre instancias individuales están representadas explícitamente (p. ej., valoraciones de películas por usuarios, enlaces de redes sociales)? En caso afirmativo, describa cómo se hacen explícitas estas relaciones.
- ¿Existen data splits recomendados (p. ej., entrenamiento, desarrollo/validación, prueba)? En caso afirmativo, proporcione una descripción de estas particiones explicando la justificación que las sustenta.
- ¿Hay errores, fuentes de ruido o redundancias en el dataset? En caso afirmativo, proporcione una descripción.
- ¿El dataset es autocontenido o enlaza o depende de recursos externos (p. ej., sitios web, tuits, otros datasets)? Si enlaza o depende de recursos externos, a) ¿existen garantías de que existirán y permanecerán constantes a lo largo del tiempo?; b) ¿existen versiones de archivo oficiales del dataset completo (es decir, incluyendo los recursos externos tal como existían en el momento de la creación del dataset)?; c) ¿existen restricciones (p. ej., licencias, tarifas) asociadas a alguno de los recursos externos que puedan aplicarse a un consumidor del dataset? Proporcione descripciones de todos los recursos externos y de cualquier restricción asociada, así como enlaces u otros puntos de acceso, según corresponda.
- ¿El dataset contiene datos que podrían considerarse confidenciales (p. ej., datos protegidos por privilegio legal o por confidencialidad médico-paciente, datos que incluyen el contenido de comunicaciones no públicas de personas)? En caso afirmativo, proporcione una descripción.
- ¿El dataset contiene datos que, si se visualizan directamente, podrían resultar ofensivos, insultantes, amenazantes o que pudieran generar ansiedad? En caso afirmativo, describa por qué.

Si el dataset no está relacionado con personas, puede omitir las preguntas restantes de esta sección.
- ¿El dataset identifica alguna subpoblación (p. ej., por edad, género)? En caso afirmativo, describa cómo se identifican estas subpoblaciones y proporcione una descripción de sus respectivas distribuciones dentro del dataset.
- ¿Es posible identificar individuos (es decir, una o más personas físicas), de forma directa o indirecta (es decir, en combinación con otros datos) a partir del dataset? En caso afirmativo, describa cómo.
- ¿El dataset contiene datos que podrían considerarse sensibles de alguna manera (p. ej., datos que revelen origen étnico o racial, orientación sexual, creencias religiosas, opiniones políticas o afiliación sindical, o ubicaciones; datos financieros o de salud; datos biométricos o genéticos; formas de identificación gubernamental, como números de seguridad social; antecedentes penales)? En caso afirmativo, proporcione una descripción.
- ¿Algún otro comentario?

3.3 Proceso de recopilación
Al igual que con las preguntas de la sección anterior, los creadores de datasets deben leer estas preguntas antes de cualquier recopilación de datos para identificar posibles problemas y luego proporcionar respuestas una vez que la recopilación esté completa. Además de los objetivos descritos en la sección anterior, las preguntas de esta sección están diseñadas para obtener información que pueda ayudar a investigadores y profesionales a crear datasets alternativos con características similares. Del mismo modo, las preguntas que se aplican únicamente a los datasets relacionados con personas se agrupan al final de la sección.

- ¿Cómo se adquirieron los datos asociados a cada instancia? ¿Los datos eran directamente observables (p. ej., texto sin procesar, valoraciones de películas), reportados por sujetos (p. ej., respuestas a encuestas), o inferidos/derivados indirectamente de otros datos (p. ej., etiquetas de partes del discurso, estimaciones de edad o idioma basadas en modelos)? Si los datos fueron reportados por sujetos o inferidos/derivados indirectamente de otros datos, ¿se validaron/verificaron? En caso afirmativo, describa cómo.
- ¿Qué mecanismos o procedimientos se utilizaron para recopilar los datos (p. ej., aparatos de hardware o sensores, curación humana manual, programas de software, APIs de software)? ¿Cómo se validaron estos mecanismos o procedimientos?
- Si el dataset es una muestra de un conjunto mayor, ¿cuál fue la estrategia de muestreo (p. ej., determinista, probabilista con probabilidades de muestreo específicas)?
- ¿Quién participó en el proceso de recopilación de datos (p. ej., estudiantes, trabajadores de crowdsourcing, contratistas) y cómo fueron compensados (p. ej., cuánto se pagó a los trabajadores de crowdsourcing)?
- ¿En qué periodo de tiempo se recopilaron los datos? ¿Coincide este periodo con el de creación de los datos asociados a las instancias (p. ej., rastreo reciente de artículos de noticias antiguos)? En caso contrario, describa el periodo en el que se crearon los datos asociados a las instancias.
- ¿Se llevaron a cabo procesos de revisión ética (p. ej., por parte de un comité de revisión institucional)? En caso afirmativo, proporcione una descripción de estos procesos de revisión, incluidos los resultados, así como un enlace u otro punto de acceso a cualquier documentación de respaldo.

Si el dataset no está relacionado con personas, puede omitir las preguntas restantes de esta sección

- ¿Se recopilaron los datos de las personas en cuestión directamente, o se obtuvieron a través de terceros u otras fuentes (p. ej., sitios web)?
- ¿Fueron notificadas las personas en cuestión sobre la recopilación de datos? En caso afirmativo, describa (o muestre con capturas de pantalla u otra información) cómo se proporcionó el aviso y facilite un enlace u otro punto de acceso al texto exacto de la notificación, o reprodúzcalo.
- ¿Dieron su consentimiento las personas en cuestión para la recopilación y uso de sus datos? En caso afirmativo, describa (o muestre con capturas de pantalla u otra información) cómo se solicitó y proporcionó el consentimiento, y facilite un enlace u otro punto de acceso al texto exacto al que consintieron las personas, o reprodúzcalo.
- Si se obtuvo el consentimiento, ¿se proporcionó a las personas que consintieron un mecanismo para revocar su consentimiento en el futuro o para ciertos usos? En caso afirmativo, proporcione una descripción, así como un enlace u otro punto de acceso al mecanismo (si corresponde).
- ¿Se ha realizado un análisis del impacto potencial del dataset y su uso en los sujetos de los datos (p. ej., un análisis de impacto de protección de datos)? En caso afirmativo, proporcione una descripción de este análisis, incluidos los resultados, así como un enlace u otro punto de acceso a cualquier documentación de respaldo.
- ¿Algún otro comentario?

3.4 Preprocesamiento/limpieza/etiquetado
Los creadores de datasets deben leer estas preguntas antes de cualquier preprocesamiento, limpieza o etiquetado y luego proporcionar respuestas una vez que estas tareas estén completas. Las preguntas de esta sección tienen como objetivo proporcionar a los consumidores de datasets la información que necesitan para determinar si los datos "crudos" han sido procesados de maneras compatibles con las tareas que han elegido. Por ejemplo, el texto que ha sido convertido en "bag-of-words" no es adecuado para tareas que involucren el orden de las palabras.
- ¿Se realizó algún preprocesamiento/limpieza/etiquetado de los datos (p. ej., discretización o segmentación, tokenización, etiquetado de partes del discurso, extracción de características SIFT, eliminación de instancias, procesamiento de valores faltantes)? En caso afirmativo, proporcione una descripción. En caso contrario, puede omitir las preguntas restantes de esta sección.
- ¿Se guardaron los datos "crudos" además de los datos preprocesados/limpios/etiquetados (p. ej., para posibles usos futuros no previstos)? En caso afirmativo, proporcione un enlace u otro punto de acceso a los datos "crudos".
- ¿Está disponible el software utilizado para preprocesar/limpiar/etiquetar los datos? En caso afirmativo, proporcione un enlace u otro punto de acceso.
- ¿Algún otro comentario?

3.5 Usos
Las preguntas de esta sección tienen como objetivo alentar a los creadores de datasets a reflexionar sobre las tareas para las que el dataset debería y no debería utilizarse. Al destacar explícitamente estas tareas, los creadores de datasets pueden ayudar a los consumidores a tomar decisiones informadas, evitando así posibles riesgos o daños.
- ¿Ha sido utilizado el dataset para alguna tarea? En caso afirmativo, proporcione una descripción.
- ¿Existe algún repositorio que enlace con alguno o todos los artículos o sistemas que utilizan el dataset? En caso afirmativo, proporcione un enlace u otro punto de acceso.
- ¿Para qué (otras) tareas podría utilizarse el dataset?
- ¿Hay algo sobre la composición del dataset o la forma en que fue recopilado y preprocesado/limpiado/etiquetado que pudiera afectar los usos futuros? Por ejemplo, ¿hay algo que un consumidor del dataset deba saber para evitar usos que pudieran resultar en un trato injusto de individuos o grupos (p. ej., estereotipos, problemas de calidad del servicio) u otros riesgos o daños (p. ej., riesgos legales, daños financieros)? En caso afirmativo, proporcione una descripción. ¿Existe algo que un consumidor del dataset podría hacer para mitigar estos riesgos o daños?
- ¿Hay tareas para las que el dataset no debería utilizarse? En caso afirmativo, proporcione una descripción.
- ¿Algún otro comentario?

3.6 Distribución
Los creadores de datasets deben proporcionar respuestas a estas preguntas antes de distribuir el dataset, ya sea internamente dentro de la entidad en nombre de la cual fue creado o externamente a terceros.
- ¿Se distribuirá el dataset a terceros fuera de la entidad (p. ej., empresa, institución, organización) en nombre de la cual fue creado? En caso afirmativo, proporcione una descripción.
- ¿Cómo se distribuirá el dataset (p. ej., tarball en un sitio web, API, GitHub)? ¿Tiene el dataset un identificador de objeto digital (DOI)?
- ¿Cuándo se distribuirá el dataset?
- ¿Se distribuirá el dataset bajo una licencia de derechos de autor u otra licencia de propiedad intelectual (PI), y/o bajo términos de uso (TdU) aplicables? En caso afirmativo, describa esta licencia y/o los TdU, y proporcione un enlace u otro punto de acceso a los términos de licencia o TdU relevantes, o reprodúzcalos, así como cualquier tarifa asociada a estas restricciones.
- ¿Han impuesto terceros restricciones basadas en PI u otras restricciones sobre los datos asociados a las instancias? En caso afirmativo, describa estas restricciones y proporcione un enlace u otro punto de acceso a los términos de licencia relevantes, o reprodúzcalos, así como cualquier tarifa asociada a estas restricciones.
- ¿Se aplican controles de exportación u otras restricciones regulatorias al dataset o a instancias individuales? En caso afirmativo, describa estas restricciones y proporcione un enlace u otro punto de acceso a la documentación de respaldo, o reprodúzcala.
- ¿Algún otro comentario?

3.7 Mantenimiento
Al igual que con las preguntas de la sección anterior, los creadores de datasets deben proporcionar respuestas a estas preguntas antes de distribuir el dataset. Las preguntas de esta sección tienen como objetivo alentar a los creadores de datasets a planificar el mantenimiento del dataset y a comunicar este plan a los consumidores.

- ¿Quién se encargará del soporte/alojamiento/mantenimiento del dataset?
- ¿Cómo puede contactarse con el propietario/curador/gestor del dataset (p. ej., dirección de correo electrónico)?
- ¿Existe un erratum? En caso afirmativo, proporcione un enlace u otro punto de acceso.
- ¿Se actualizará el dataset (p. ej., para corregir errores de etiquetado, añadir nuevas instancias, eliminar instancias)? En caso afirmativo, describa con qué frecuencia, por quién y cómo se comunicarán las actualizaciones a los consumidores del dataset (p. ej., lista de correo, GitHub).
- Si el dataset está relacionado con personas, ¿existen límites aplicables a la retención de los datos asociados a las instancias (p. ej., ¿se informó a las personas en cuestión de que sus datos se retendrían durante un período de tiempo determinado y luego se eliminarían)? En caso afirmativo, describa estos límites y explique cómo se aplicarán.
- ¿Las versiones anteriores del dataset seguirán siendo soportadas/alojadas/mantenidas? En caso afirmativo, describa cómo. En caso contrario, describa cómo se comunicará a los consumidores del dataset su obsolescencia.
- Si otros desean extender/ampliar/desarrollar/contribuir al dataset, ¿existe un mecanismo para hacerlo? En caso afirmativo, proporcione una descripción. ¿Se validarán/verificarán estas contribuciones? En caso afirmativo, describa cómo. En caso contrario, ¿por qué no? ¿Existe un proceso para comunicar/distribuir estas contribuciones a los consumidores del dataset? En caso afirmativo, proporcione una descripción.
- ¿Algún otro comentario?
