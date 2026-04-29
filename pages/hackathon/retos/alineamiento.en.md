---
title: "Main Challenge #HackathonSomosNLP 2026: LLM and VLLM Alignment"
description: How to participate in this challenge and help improve the cultural knowledge of language and vision-language models
lang: en
cover: /images/eventos/260511_hackathon_eventbrite.png
---

## 🎯 Challenge Objective

- Choose one of the following options:
    - A. Align a **language model** (LLM) to generate text in a culturally appropriate manner
    - B. Adapt a **multimodal vision-language model** (VLLM) to generate image descriptions taking into account the cultural context
- In Spanish, Portuguese, or any language of the Iberian Peninsula or LATAM
- Adapt from an existing model (do not pre-train one from scratch), we recommend using models around 7B as a base (e.g. [Salamandra](https://huggingface.co/BSC-LT/salamandra-7b-instruct), [Mistral](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) and [Gemma](https://huggingface.co/google/gemma-3-4b-it))
- Generate the dataset with the help of 500 USD in Cohere API credits! We recommend filtering and extending the v0 preferences dataset generated collectively in the Arena: [somosnlp-hackathon-2025/dataset-preferencias-dpo-v0](https://huggingface.co/datasets/somosnlp-hackathon-2025/dataset-preferencias-dpo-v0)
- Train your model directly in JupyterLab on the Hugging Face hub — we have GPUs sponsored by 🤗!
- Upload the model(s) along with all notebooks used to hf.co/somosnlp-hackathon-2026
- Write the [Model Card](https://huggingface.co/spaces/huggingface/Model_Cards_Writing_Tool), include links to the dataset and notebooks used (e.g. preprocessing, training)

---

## Guide

### ✅ Preparation

<details>
<summary>Requirements per team</summary>

1. Contribute 100 **quality** prompts to the [preferences](https://somosnlp.org/en/hackathon/retos/preferencias) dataset
2. Answer 200 questions from the evaluation dataset ([BLEND](https://somosnlp.org/en/hackathon/retos/blend))
3. Request the 500 USD Cohere API credits (after completing points 1 and 2, mention @mariagrandury in your team's channel for instructions)
4. Create a Space in the organization hf.co/somosnlp-hackathon-2026 with the [jupyterlab](https://huggingface.co/docs/hub/spaces-sdks-docker-jupyter) template
5. Complete the [registration form](https://forms.gle/mLKEURUXGiNhq31T9)

</details>

### 📚 Dataset

Data is the most important thing in model development, and we will also give it greater importance when evaluating projects 👀

- Generate a dataset for your project:
    - Use as the initial version for your dataset the one generated collectively in the Arena: [somosnlp-hackathon-2025/dataset-preferencias-dpo-v0](https://huggingface.co/datasets/somosnlp-hackathon-2025/dataset-preferencias-dpo-v0)
    - Take advantage of the 500 USD in Cohere API credits that each team has to filter, improve, and extend it with more prompts and responses specifically designed for your use case
    - Keep in mind that when dealing with cultural topics, it is very important that everything generated synthetically is reviewed by a person (you can use [Argilla](https://huggingface.co/docs/hub/en/datasets-argilla))
- Upload the dataset to hf.co/somosnlp-hackathon-2026 and iterate
- Upload all notebooks and scripts used to generate and process the dataset to the dataset repo
    - If you prefer to create a GitHub repo with all the code, you can do so — don't forget to include a link in the Dataset Card
- Fill out the Dataset Card **properly**
    - "Dataset Card" is the name of the documentation for Hugging Face datasets, it is the README.md of the dataset repository
    - NOTE: This is taken into account for project evaluation
    - Include in the introduction the project motivation and impact
    - Detail the generation and processing pipeline, include the libraries used and mention the tests done, include links to the code
    - Specify the license: preferably `apache-2.0`, if not, explain why
    - Evaluate the dataset biases, whether it is balanced, what language varieties or opinions it represents, etc.

How to name datasets:
- The name of the dataset with the (minimum 100) prompts you submitted to the LLM Arena must contain `prompt`. For example: `normas_culturales_colombia_prompts`
- The names of preference datasets must contain the name of the main algorithm they can be used for (`dpo` or `kto`). For example: `normas_culturales_colombia_dpo`
- If the dataset is multimodal, it must contain `image`. For example: `utensilios_ecuador_images_kto`

### ⚙️ Model

1. Create a Space in the organization hf.co/somosnlp-hackathon-2026 with the [JupyterLab](https://huggingface.co/docs/hub/spaces-sdks-docker-jupyter) template
2. The Hugging Face team will assign an *L40S* grant to the Space
    - Set the "auto-sleep" time to 5 minutes to ensure responsible use 🌱
3. Design the training notebook
    - Save the resulting model directly to hf.co/somosnlp-hackathon-2026
    - Use the CodeCarbon library to evaluate the climate impact
4. Run tests with small models and dataset subsets to verify the code is correct and avoid finding bugs after several hours of training.
5. Launch the training, review the results, and iterate
    - You can try e.g. different algorithms or base models
    - You don't need to create a different repo for each model; if you push to the same repo, the updated model will be saved as a new commit (which you can link from the Model Card if you want)
6. **Download the dataset processing and model training notebooks, upload them to the model repo** (VERY IMPORTANT) and delete the JupyterLab Space
7. Fill out the Model Card **properly**
    - "Model Card" is the name of the documentation for Hugging Face models, it is the README.md of the model repository
    - NOTE: This is taken into account for project evaluation
    - Recommendation: Describe the tests as you do them, as well as the dataset improvement and model training process
    - Include in the introduction the project motivation and impact
    - Detail the training process, include the libraries used and mention the tests done, include links to the code
    - Specify the license: preferably `apache-2.0`, if not, explain why
    - Evaluate the model biases
    - Evaluate the environmental impact

---

## Resources

Below we share plenty of resources so you can develop high-quality projects. Resources marked with ⭐ correspond to talks and workshops given during the hackathon and specifically designed to help you in this edition.

### 📚 Dataset

The Cohere API:
- ⭐ [Practical workshop: How to use the Cohere API](https://www.youtube.com/watch?v=S_Wky6D9Nf0&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) given by Alejandro Rodriguez, Research Engineer at Cohere. Use Cohere's models to clean and extend your dataset.

Dataset creation:
- ⭐ [Red Teaming for language models](https://www.youtube.com/watch?v=pGOXE4rrO9M&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6), given by Luis Vasquez, from the Reinforcement Learning, Alignment & Red Teaming team at the Barcelona Supercomputing Center.
- ⭐ [MuSeD: Creation of a multimodal corpus in Spanish for sexism detection in social media videos](https://www.youtube.com/watch?v=w1ikWRaBQd0&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6), given by Laura De Grazia from the Universitat de Barcelona.
- [How to annotate linguistic corpora to train LLMs](https://www.youtube.com/watch?v=d6vrflcIY-g&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J), given by Marta Guerrero @IIC, co-creator of 3 of the corpora that form La Leaderboard.
- [Distilabel and Argilla, tools for creating models like Notus](https://www.youtube.com/watch?v=riM3pgV4m_I&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J) given by Gabriel Martín, MLE @Argilla (notebook available).

Inspiration:
- ⭐ [Describing and interpreting interaction using cultural scripts](https://www.youtube.com/watch?v=jLh9Wyn7qcI&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6), talk given in English by Lauren Sadow from Aarhus University.
- ⭐ [Expressing uncertainty in multilingual tasks](https://www.youtube.com/watch?v=TC9tOEyPqy8&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) given by Selene Báez, postdoctoral researcher at the University of Zurich.
- [Environmental ethics in AI: building sustainable narratives in Spanish](https://www.youtube.com/watch?v=MJLdrXz6bSE&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J), talk given by Jorge Vallego, Project Lead @H4rmony. It can help you give an eco-conscious approach to your dataset.

### ⚙️ Model

Creating the training Space:
- [Docs: JupyterLab on Spaces](https://huggingface.co/docs/hub/en/spaces-sdks-docker-jupyter#jupyterlab-on-spaces), where you can run your notebooks as always. Be careful not to lose storage when restarting the Space — save your notebooks!
<!--
- [Docs: AutoTrain (English)](https://huggingface.co/docs/autotrain/llm_finetuning), we encourage you to try this no-code platform from Hugging Face. We are going to translate this section of the documentation, let us know if you need help understanding it.
- [Tutorial: AutoTrain + spacerunner (English)](https://huggingface.co/blog/stefan-it/autotrain-flair-mobie), with this combination you can run scripts on AutoTrain.
-->

LLM Alignment:
- ⭐ [Practical workshop: LLM Alignment using Reinforcement Learning](https://www.youtube.com/watch?v=wI6yjbed_1Q&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) given by Luis Vasquez, from the Reinforcement Learning, Alignment & Red Teaming team at the Barcelona Supercomputing Center.

Multimodal models:
- ⭐ [Talk: How to build an efficient Vision-Language Model](https://www.youtube.com/watch?v=PjOXDCe_3kg&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) given by Andrés Marafioti, ML Engineer at Hugging Face and creator of SmolVLM.
- ⭐ [Talk: Instruction Tuning for Sequential Multimodal Reasoning](https://www.youtube.com/watch?v=xiAfa6rafRs&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) given by Danae Sanchez, postdoctoral researcher at the University of Copenhagen.

LLM Fine-tuning:
- [Practical workshop: The impact of data quality on LLM fine-tuning](https://www.youtube.com/watch?v=hPq5NG8kA8w&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J), also given by Manu Romero, creator of 500+ models on the Hugging Face Hub.
- [Practical workshop: Fine-tuning large language models](https://somosnlp.org/hackathon-2023/fine-tuning-llms) given by Manu Romero, creator of 500+ models on the Hugging Face Hub.
- [Workshop + AMA on LLM training](https://www.youtube.com/playlist?list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J) with Alejandro Vaca, founder of LenguajeNaturalAI.
- `unsloth` notebooks for faster training (in English, let us know if you need them translated):
[Gemma FT on Alpaca-style instruction dataset](https://colab.research.google.com/drive/10NbwlsRChbma1v55m8LAPYG15uQv6HLo) and
[RLAIF via DPO on Zephyr](https://colab.research.google.com/drive/15vttTpzzVXv_tJwEk-hIcQ0S9FcEWvwP).

Climate impact:
- To evaluate the carbon footprint of your model training, you can use tools like [Code Carbon](https://codecarbon.io) (better, integrated into 🤗 Transformers) or [ML CO2 Impact](https://mlco2.github.io/impact).
- We recommend this [video](https://www.youtube.com/watch?v=ftWlj4FBHTg) for motivation, this [article](https://huggingface.co/blog/carbon-emissions-on-the-hub) from the HF blog, and the [documentation](https://huggingface.co/docs/hub/model-cards-co2) section of 🤗 Transformers that covers this topic.

### 📝 Documentation

- [Docs: how to write a good Dataset Card](https://huggingface.co/docs/datasets/dataset_card): this is the official Hugging Face documentation, includes a template and a couple of good examples.
- [Docs: how to write a Model Card](https://huggingface.co/docs/hub/model-cards): official Hugging Face guide, includes a link to the Space to create it automatically and an explanation of each section.
- [Space: Model Card Creator](https://huggingface.co/spaces/huggingface/Model_Cards_Writing_Tool), Space that guides you in creating your model card.
- [Bias detection and mitigation in language models](https://somosnlp.org/hackathon-2023/evaluacion-de-sesgos), talk given by María Grandury, founder of SomosNLP.

<center style="margin-top:40px;"><a href="https://somosnlp.org/en/hackathon/retos" target="_blank" style="background-color:gray; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Back to challenges</a></center>
