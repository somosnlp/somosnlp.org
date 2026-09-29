---
title: Un modelo de lenguaje de 30.000 millones de parámetros en cuatro Raspberry Pi 5
description: Qué velocidad alcanza Qwen3-30B-A3B en cuatro placas, solo con la CPU, por qué genera más rápido que un modelo denso de 8.000 millones y dónde está hoy su límite
date: 2026-09-29T10:00:00.000+00:00
lang: es
duration: 6min
cover: /images/blog/qwen3-raspberry-pi-cluster.png
author: Isaac Correa
bio: Cofundador de Hellomatik
website: https://hellomatik.com
tags: [recursos, papers]
---

Este artículo resume dos estudios de Daniel Correa Villa ([danielcorrea-hellomatik](https://github.com/danielcorrea-hellomatik) en GitHub), cofundador de [Hellomatik](https://hellomatik.com). Todas las cifras salen de los estudios y de su repositorio, enlazados al final.

Repartido entre cuatro Raspberry Pi 5 de 16 GB, solo con la CPU y sin subir la frecuencia del procesador, Qwen3-30B-A3B, un modelo de lenguaje abierto de 30.000 millones de parámetros, genera 15,14 tokens por segundo. En las mismas placas genera más rápido que un modelo denso de 8.000 millones, y sirve para conversaciones cortas, pero todavía no para agentes con instrucciones largas.

## El clúster

Cuatro Raspberry Pi 5 de 16 GB, cada una con su disipador activo y un disco NVMe, conectadas por un conmutador Gigabit. El programa es distributed-llama, que reparte cada capa del modelo entre las cuatro placas, con los pesos cuantizados en Q40, unos 4,5 bits por peso. Cada optimización se ha validado comprobando que el SHA-256 de los tokens generados con los prompts de referencia coincide con el de la ejecución original: con esos prompts, ninguna cambió ni un token de la salida.

![Render del clúster: el nodo raíz y tres trabajadores conectados por un conmutador Gigabit](/images/blog/qwen3-raspberry-pi-cluster.png)

Cada token pasa por las cuatro placas: distributed-llama reparte cada capa entre ellas y las sincroniza varias veces por capa. La memoria que marca el dibujo, 12 GB en la raíz y 6,3 GB en cada trabajador, es la de la configuración con contexto largo (32.768 tokens); las mediciones de velocidad usan un contexto de 4.096 tokens, con unos 5,5 GB por placa.

## Por qué el modelo grande genera más rápido que el pequeño

| | Qwen3-30B-A3B | DeepSeek-R1-Distill-Llama-8B |
|---|---|---|
| Tipo de modelo | Mezcla de expertos | Denso |
| Parámetros que usa en cada token | Unos 3.000 millones de 30.000 | Los 8.000 millones |
| Generación, cada modelo en su configuración óptima, contexto corto | 15,14 tokens por segundo | 8,32 tokens por segundo |

En el modelo denso, lo que más pesa en el tiempo de cada token es la lectura de memoria: para generar cada token hay que leer todos sus pesos. Un modelo de mezcla de expertos activa, en cada capa y en cada token, 8 de sus 128 expertos, así que lee muchos menos datos que un modelo denso de 8.000 millones, que los lee todos. En hardware con poco ancho de banda de memoria, un modelo de mezcla de expertos grande genera más rápido que uno denso pequeño, siempre que todos sus pesos quepan en la memoria del conjunto. La comparación mide velocidad, no la calidad de las respuestas.

En el modelo de mezcla de expertos, la memoria ya no es lo único que pesa. El ajuste de firmware `SDRAM_BANKLOW=1`, que sube un 50 % el ancho de banda de lectura, de 8,3 a 12,5 GB/s por placa, sube su generación solo un 5,9 %: según el perfilado del estudio, casi la mitad del tiempo de cada token se va en coordinar las cuatro placas, esperar en las barreras de sincronización y atender llamadas al sistema.

## Qué aceleró el sistema

En las mismas placas, distributed-llama sin modificar genera 13,15 tokens por segundo con el modelo de 30.000 millones. Los cambios que llevaron a 15,14 fueron de dos tipos:

- **Cambios en el programa**: opciones de compilación que activan las instrucciones de producto escalar del Cortex-A76 y cambios en el código fuente, como fusionar dos operaciones de cada experto en un solo paso. Juntos aportan un 5,6 %.
- **Ajustes de sistema**: el mismo `SDRAM_BANKLOW=1` en la configuración del cargador de arranque (activo por defecto en las versiones publicadas desde diciembre de 2024; el estudio no dice qué versión tenían las placas antes); tres hilos de cálculo por placa con el cuarto núcleo dedicado a las interrupciones de red; y parar dos agentes de monitorización que competían por el ancho de banda de memoria, lo que por sí solo sube la generación un 5,2 %.

Cada mejora se midió por separado y en momentos distintos del trabajo, así que los porcentajes no se suman: el total, de 13,15 a 15,14, es un 15,1 %.

En el modelo denso de 8.000 millones, esos mismos cambios en el código no modifican la velocidad de generación con cuatro hilos por placa. Sí casi duplican el procesamiento del prompt (*prefill*), que pasa de 8,52 a 15,81 tokens por segundo, porque en esa fase cada dato leído de memoria alimenta mucho más cálculo.

## Dónde está el límite

**El procesamiento del prompt es lento.** Con el modelo de 30.000 millones, cuyos 15,14 tokens por segundo son también una cifra de contexto corto, el prompt se procesa a unos 15,7 tokens por segundo, casi la misma velocidad que la generación: un prompt de 2.000 tokens tarda unos dos minutos antes de la primera palabra de la respuesta. Para un prompt de 20.000 tokens, el tamaño de las instrucciones de sistema de un agente como Hermes Agent, el estudio proyecta más de veinte minutos. El clúster sirve para conversaciones cortas y todavía no para agentes con instrucciones largas.

**La generación se frena al crecer el contexto.** En el modelo de 8.000 millones, el tiempo de cada token crece en línea recta con la longitud del contexto, según t(L) = 116,73 + 0,0174 × L milisegundos (R² = 0,9993). Los 8,32 tokens por segundo de la tabla son la cifra de contexto corto; cerca de los 5.000 tokens la velocidad baja a unos 5, así que una respuesta de razonamiento larga se genera más despacio de lo que indica la tabla.

**Para modelos de 8.000 millones hay hardware más rápido.** El propio estudio lo indica: un Mac mini M4 da unos 25 tokens por segundo y una Jetson Orin Nano Super, 21,75. El valor del clúster está en mostrar qué se puede ejecutar en placas baratas y fáciles de conseguir y qué ajustes influyen realmente en la velocidad.

## Fuentes

- Estudio del modelo de 30.000 millones, con los datos de cada ejecución: [doi.org/10.5281/zenodo.20357376](https://doi.org/10.5281/zenodo.20357376)
- Estudio del modelo de 8.000 millones: [doi.org/10.5281/zenodo.20411979](https://doi.org/10.5281/zenodo.20411979)
- Código, licencia MIT: [hellomatik-org/distributed-llama](https://github.com/hellomatik-org/distributed-llama)

Este artículo se ha redactado con ayuda de inteligencia artificial y se ha comprobado contra los dos estudios y el repositorio antes de publicarlo.
