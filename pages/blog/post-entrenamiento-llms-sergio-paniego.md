---
title: Post-entrenamiento de LLMs
description: Resumen de la charla de Sergio Paniego en el #HackathonSomosNLP 2026
date: 2026-05-11T18:00:00.000+00:00
lang: es
duration: 4min
cover: /images/blog/Charla-Sergio-Paniego.JPG
author: Firdaous Boulahfa El Mourabit
bio: Lingüista Computacional & NLP Engineer
linkedin: https://www.linkedin.com/in/firdaous-boulahfa-el-mourabit-871b11343/
---
Cuando pensamos en entrenar un modelo de lenguaje, solemos imaginar el pre-entrenamiento: miles de horas de cómputo, terabytes de texto, grandes clústeres de GPUs. Pero eso solo es el principio. Un modelo que ha aprendido a predecir el siguiente token no sabe seguir instrucciones, no razona, no sabe cuándo está equivocado, y desde luego no actúa de forma segura.

Ahí es donde entra el **post-entrenamiento**: la fase que convierte un modelo base en algo realmente útil.

El pasado 11 de mayo, Sergio Paniego, ML Engineer en Hugging Face y PhD en IA por la URJC, impartió el primer taller del #HackathonSomosNLP 2026, dedicado precisamente a esto. En dos horas, cubrió el estado del arte del post-entrenamiento con herramientas de código abierto, ejemplos prácticos y notebooks que cualquiera puede ejecutar en Google Colab gratuito. Aquí van los puntos clave.

## **Las tres fases del entrenamiento de un LLM**

Antes de entrar en técnicas, conviene tener clara la estructura general:

- **Pre-entrenamiento**: el modelo aprende el lenguaje y el conocimiento del mundo a partir de texto crudo en grandes cantidades. Requiere cómputo industrial y no está al alcance de la mayoría.
- **Entrenamiento intermedio**: añade conocimiento de dominio específico (código, medicina, derecho...) con datos seleccionados cuidadosamente. Menos cómputo, más precisión.
- **Post-entrenamiento**: el modelo aprende a *comportarse*. A seguir instrucciones, razonar, ser seguro, actuar como agente. Requiere datos de muy alta calidad, pero el cómputo necesario es accesible.

El flujo en tres pasos: **encontrar el modelo → personalizarlo → desplegarlo**.

## **Técnicas:**

### **SFT: el punto de partida**

**Supervised Fine-Tuning (SFT)** es el método más usado para transformar un modelo base en un asistente conversacional. El modelo aprende de pares de ejemplos (instrucción → respuesta ideal), minimizando la log-likelihood negativa de secuencias de conversación con el chat template aplicado.

Es estable, eficiente y muy efectivo como primer paso. El SFTTrainer de TRL soporta dos formatos: estándar (modelado de lenguaje puro) y conversacional (instruction following), aplicando el chat template automáticamente. Todo esto en unas pocas líneas de código.

### **DPO: alinear con preferencias humanas**

El fine-tuning clásico enseña al modelo a imitar datos. Pero imitar no es lo mismo que preferir las respuestas correctas.

**Direct Preference Optimization (DPO)** permite alinear el modelo con preferencias humanas en términos de **utilidad**, **veracidad** y **seguridad**. Se alimenta de pares de respuestas para la misma pregunta: una elegida y una rechazada. El modelo aprende a preferir las que los humanos valorarían más, sin necesidad de entrenar un modelo de recompensa explícito.

### **GRPO: razonamiento y comportamiento agéntico**

**Group Relative Policy Optimization (GRPO)**, introducido en el artículo DeepSeekMath, lleva las cosas un paso más allá.

Es un método *online*: el modelo genera múltiples respuestas para cada prompt, cada una se evalúa con una función de recompensa, y los resultados se usan para actualizar los pesos. No necesita un modelo de valor separado, lo que lo hace más eficiente en memoria que PPO y más estable.

La función de recompensa la define el equipo: puede ser tan simple como verificar que la respuesta tenga el formato correcto, o tan compleja como evaluar si un agente evitó una colisión en un simulador de conducción.

## **TRL: la librería que lo une todo**

**TRL (Transformer Reinforcement Learning)** es la librería de Hugging Face que implementa todos estos métodos. Está construida sobre el Trainer de Transformers y ofrece trainers especializados listos para usar:

- SFTTrainer
- DPOTrainer
- GRPOTrainer

Sin necesidad de reimplementar nada desde cero. Es compatible con PEFT (LoRA, QLoRA), vLLM, Accelerate y tiene soporte multimodal para VLMs.

No hace falta un clúster de GPUs para empezar. Los trainers de TRL incluyen opciones de optimización integradas que permiten entrenar modelos de 7B en una T4 gratuita de Colab:

- **LoRA / QLoRA**: actualizan solo una fracción de los parámetros, reduciendo drásticamente el uso de memoria.
- **Unsloth**: reduce aún más el consumo de VRAM.
- **Gradient checkpointing y Liger kernels**: optimizaciones adicionales de memoria y velocidad.

Con todas las optimizaciones activadas, el uso de VRAM se reduce hasta **7 veces** respecto al entrenamiento naive en FP16.

## **OpenEnv: entrenar modelos que actúan en el mundo**

El siguiente paso en post-entrenamiento no son datasets estáticos, sino modelos que aprenden interactuando con entornos, como lo haría un agente.

**OpenEnv** es un framework de Meta/PyTorch que estandariza los entornos de aprendizaje por refuerzo para LLMs. Hasta ahora, cada entorno tenía su propia API, formato y lógica. OpenEnv resuelve eso: proporciona una interfaz simple (reset() + métodos públicos como herramientas), se puede ejecutar localmente, en Docker o en HF Spaces, y se integra nativamente con el GRPOTrainer de TRL.

El bucle de entrenamiento cambia así:

**Antes:** Prompt → <think>...</think> → Respuesta → Recompensa

**Ahora:** Estado → Acción → Entorno → Recompensa → Nuevo estado → ...

Sergio lo demostró con un ejemplo concreto usando **CARLA**, el simulador de conducción autónoma: un Qwen3-0.6B entrenado con GRPO aprendió a evitar colisiones con peatones en pocas decenas de pasos, pasando de chocar sistemáticamente a frenar y cambiar de carril con éxito.

## **Recursos**

Todo el material de la charla está disponible:

- 🎥 **Grabación completa**: https://www.youtube.com/live/dWk4Rq-2esA?si=fFrNfnuTSJBskrwe
- 📊 **Diapositivas**: https://github.com/sergiopaniego/talks
- 📚 **Material TRL**: https://huggingface.co/docs/trl/example_overview
- 🌐 **Material OpenEnv**: https://meta-pytorch.org/OpenEnv/tutorials/index.html
- 🍳 **Más recetas de HF**: https://huggingface.co/learn/cookbook/en/index

Puedes seguir a Sergio en LinkedIn y redes como **@sergiopaniego**.

*Este taller forma parte del #HackathonSomosNLP 2026, un hackathon comunitario centrado en la adecuación cultural de los LLMs para las comunidades hispanohablantes de Iberoamérica.*
