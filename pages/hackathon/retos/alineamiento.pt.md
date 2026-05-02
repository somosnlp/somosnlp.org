---
title: "Desafio Principal #HackathonSomosNLP 2026: Alinhamento de LLMs e VLLMs"
description: Como participar deste desafio e ajudar a melhorar o conhecimento cultural dos modelos de linguagem e visão linguagem
lang: pt
cover: /images/eventos/260511_hackathon_eventbrite.png
---

## 🎯 Objetivo do desafio

* Escolha uma das opções a seguir:
    * A. Alinhe um **modelo de linguagem** (LLM) para gerar texto de forma culturalmente adequada
    * B. Adapte um **modelo multimodal visão linguagem** (VLLM) para gerar descrições de imagens levando em conta o contexto cultural
* Em espanhol, português ou qualquer língua da Península Ibérica ou da América Latina
* Adapte um modelo já existente (não pré treine um do zero). Recomendamos partir de modelos em torno de 7B (e.g. [Salamandra](https://huggingface.co/BSC-LT/salamandra-7b-instruct), [Mistral](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) e [Gemma](https://huggingface.co/google/gemma-3-4b-it))
* Gere o dataset com a ajuda de 500 USD em créditos da API da Cohere! Recomendamos filtrar e estender o dataset de preferências v0 gerado em conjunto na Arena: [somosnlp-hackathon-2025/dataset-preferencias-dpo-v0](https://huggingface.co/datasets/somosnlp-hackathon-2025/dataset-preferencias-dpo-v0)
* Treine seu modelo diretamente em JupyterLab no hub do Hugging Face. Temos GPUs patrocinadas pela 🤗!
* Faça upload do(s) modelo(s) junto com todos os notebooks utilizados para hf.co/somosnlp-hackathon-2026
* Escreva a [Model Card](https://huggingface.co/spaces/huggingface/Model_Cards_Writing_Tool). Inclua links para o dataset e para os notebooks utilizados (e.g. pré processamento, treinamento)

---

## Guia

### ✅ Preparação

<details>
<summary>Requisitos por equipe</summary>

1. Contribuir com 100 prompts **de qualidade** ao dataset de [preferências](https://somosnlp.org/pt/hackathon/retos/preferencias)
2. Responder 200 perguntas do dataset de avaliação ([BLEND](https://somosnlp.org/pt/hackathon/retos/blend))
3. Pedir os 500 USD em créditos da API da Cohere (depois de completar os pontos 1 e 2, mencione @mariagrandury no canal da equipe de vocês para receber instruções)
4. Criar na organização hf.co/somosnlp-hackathon-2026 um Space com o template de [jupyterlab](https://huggingface.co/docs/hub/spaces-sdks-docker-jupyter)
5. Preencher o [formulário de registro](https://forms.gle/mLKEURUXGiNhq31T9)

</details>

### 📚 Dataset

Os dados são o mais importante no desenvolvimento de um modelo, e também vamos dar mais peso a eles na hora de avaliar os projetos 👀

* Gere um dataset para o seu projeto:
    * Use como versão inicial do seu dataset o que foi gerado em conjunto na Arena: [somosnlp-hackathon-2025/dataset-preferencias-dpo-v0](https://huggingface.co/datasets/somosnlp-hackathon-2025/dataset-preferencias-dpo-v0)
    * Aproveite os 500 USD em créditos da API da Cohere que cada equipe tem para filtrar, melhorar e estender com mais prompts e respostas pensados especificamente para o seu caso de uso
    * Lembre que, tratando se de temas culturais, é muito importante que tudo o que for gerado sinteticamente seja revisado por uma pessoa (vocês podem usar [Argilla](https://huggingface.co/docs/hub/en/datasets-argilla))
* Faça upload do dataset para hf.co/somosnlp-hackathon-2026 e itere
* Faça upload para o repo do dataset de todos os notebooks e scripts usados para gerar e processar o dataset
    * Se preferir criar um repo no GitHub com todo o código, pode fazer isso. Só não esqueça de incluir um link na Dataset Card
* Preencha **bem** a Dataset Card
    * "Dataset Card" é o nome da documentação dos datasets do Hugging Face. É o README.md do repositório dos datasets
    * ATENÇÃO: É levado em conta na avaliação do projeto
    * Inclua na introdução a motivação do projeto e o seu impacto
    * Detalhe o processo de geração e processamento, inclua as bibliotecas usadas e mencione os testes feitos, inclua os links para o código
    * Especifique a licença: de preferência `apache-2.0`. Se não, explique por quê
    * Avalie os vieses do dataset, se está balanceado, que variedades da língua ou opiniões representa, etc.

Como nomear os datasets:
* O nome do dataset com os (mínimo 100) prompts que vocês enviaram para a LLM Arena precisa conter `prompt`. Por exemplo: `normas_culturales_colombia_prompts`
* O nome dos datasets de preferências precisa conter o nome do algoritmo principal para o qual podem ser usados (`dpo` ou `kto`). Por exemplo: `normas_culturales_colombia_dpo`
* Se o dataset for multimodal, precisa conter `image`. Por exemplo: `utensilios_ecuador_images_kto`

### ⚙️ Modelo

1. Crie na organização hf.co/somosnlp-hackathon-2026 um Space com o template de [JupyterLab](https://huggingface.co/docs/hub/spaces-sdks-docker-jupyter)
2. A equipe da Hugging Face vai atribuir um grant de uma *L40S* ao Space
    * Configure o tempo de "auto sleep" para 5 minutos para garantir um uso responsável 🌱
3. Desenhe o notebook de treinamento
    * Salve o modelo resultante diretamente em hf.co/somosnlp-hackathon-2026
    * Use a biblioteca CodeCarbon para avaliar o impacto climático
4. Faça testes com modelos pequenos e subconjuntos do dataset para verificar que o código está correto e não encontrar bugs depois de várias horas de treinamento.
5. Lance o treinamento, revise os resultados e itere
    * Você pode experimentar e.g. diferentes algoritmos ou modelos base
    * Não precisa criar um repo diferente para cada modelo. Se você fizer push para o mesmo repo, o modelo atualizado fica salvo como um novo commit (ao qual você pode linkar a partir da Model Card se quiser)
6. **Baixe os notebooks de processamento do dataset e de treinamento do modelo, faça upload deles para o repo do modelo** (MUITO IMPORTANTE) e elimine o Space de JupyterLab
7. Preencha **bem** a Model Card
    * "Model Card" é o nome da documentação dos modelos do Hugging Face. É o README.md do repositório dos modelos
    * ATENÇÃO: É levado em conta na avaliação do projeto
    * Recomendação: vá descrevendo os testes à medida que faz, assim como o processo de melhoria do dataset e de treinamento do modelo
    * Inclua na introdução a motivação do projeto e o seu impacto
    * Detalhe o processo de treinamento, inclua as bibliotecas usadas e mencione os testes feitos, inclua os links para o código
    * Especifique a licença: de preferência `apache-2.0`. Se não, explique por quê
    * Avalie os vieses do modelo
    * Avalie o impacto ambiental

---

## Recursos

A seguir compartilhamos vários recursos para que vocês possam desenvolver projetos de grande qualidade. Os recursos marcados com ⭐ correspondem a palestras e workshops dados durante o hackathon e pensados especificamente para ajudar nesta edição.

### 📚 Dataset

A API da Cohere:
* ⭐ [Workshop prático: Como usar a API da Cohere](https://www.youtube.com/watch?v=S_Wky6D9Nf0&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) dado por Alejandro Rodriguez, Research Engineer na Cohere. Usem os modelos da Cohere para limpar e estender o dataset de vocês.

Criação de datasets:
* ⭐ [Red Teaming para modelos de linguagem](https://www.youtube.com/watch?v=pGOXE4rrO9M&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6), dado por Luis Vasquez, da equipe de Reinforcement Learning, Alignment & Red Teaming do Barcelona Supercomputing Center.
* ⭐ [MuSeD: Criação de um corpus multimodal em espanhol para a detecção de sexismo em vídeos de redes sociais](https://www.youtube.com/watch?v=w1ikWRaBQd0&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6), dado por Laura De Grazia da Universitat de Barcelona.
* [Como anotar corpora linguísticos para treinar LLMs](https://www.youtube.com/watch?v=d6vrflcIY-g&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J), dado por Marta Guerrero @IIC, co criadora de 3 dos corpora que formam La Leaderboard.
* [Distilabel e Argilla, ferramentas para criar modelos como o Notus](https://www.youtube.com/watch?v=riM3pgV4m_I&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J) dado por Gabriel Martín, MLE @Argilla (notebook disponível).

Inspiração:
* ⭐ [Describing and interpreting interaction using cultural scripts](https://www.youtube.com/watch?v=jLh9Wyn7qcI&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) (palestra em inglês), dada por Lauren Sadow da Aarhus University.
* ⭐ [Expressando incerteza em tarefas multilíngues](https://www.youtube.com/watch?v=TC9tOEyPqy8&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6), dada por Selene Báez, pesquisadora pós doutoral na University of Zurich.
* [Ética ambiental em IA: construindo narrativas sustentáveis em espanhol](https://www.youtube.com/watch?v=MJLdrXz6bSE&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J), palestra dada por Jorge Vallego, Project Lead @H4rmony. Pode servir para dar uma abordagem eco consciente ao dataset de vocês.

### ⚙️ Modelo

Criação do Space de treinamento:
* [Docs: JupyterLab em Spaces](https://huggingface.co/docs/hub/en/spaces-sdks-docker-jupyter#jupyterlab-on-spaces), onde vocês podem rodar os notebooks como sempre. ATENÇÃO para não perder o armazenamento ao reiniciar o Space, salvem os notebooks!
<!--
* [Docs: AutoTrain (inglês)](https://huggingface.co/docs/autotrain/llm_finetuning), incentivamos vocês a experimentar essa plataforma no code da Hugging Face. Vamos traduzir essa seção da documentação, avisem se precisarem de ajuda para entender.
* [Tutorial: AutoTrain + spacerunner (inglês)](https://huggingface.co/blog/stefan-it/autotrain-flair-mobie), com essa combinação vocês podem rodar scripts no AutoTrain.
-->

Alinhamento de LLMs:
* ⭐ [Workshop prático: Alinhamento de LLMs usando Aprendizagem por Reforço](https://www.youtube.com/watch?v=wI6yjbed_1Q&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) dado por Luis Vasquez, da equipe de Reinforcement Learning, Alignment & Red Teaming do Barcelona Supercomputing Center.

Modelos multimodais:
* ⭐ [Palestra: Como fazer um Modelo Visão Linguagem eficiente](https://www.youtube.com/watch?v=PjOXDCe_3kg&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) dada por Andrés Marafioti, ML Engineer na Hugging Face e criador do SmolVLM.
* ⭐ [Palestra: Instruction Tuning para Raciocínio Sequencial Multimodal](https://www.youtube.com/watch?v=xiAfa6rafRs&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) dada por Danae Sanchez, pesquisadora pós doutoral na Universidade de Copenhague.

Fine tuning de LLMs:
* [Workshop prático: O impacto da qualidade dos dados em um FT de LLMs](https://www.youtube.com/watch?v=hPq5NG8kA8w&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J), dado também por Manu Romero, criador de mais de 500 modelos do Hub do Hugging Face.
* [Workshop prático: Fine tuning de grandes modelos de linguagem](https://somosnlp.org/hackathon-2023/fine-tuning-llms) dado por Manu Romero, criador de mais de 500 modelos do Hub do Hugging Face.
* [Workshop + AMA sobre treinamento de LLMs](https://www.youtube.com/playlist?list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J) com Alejandro Vaca, fundador da LenguajeNaturalAI.
* Notebooks de `unsloth` para treinar mais rápido (em inglês, se precisarem que a gente traduza, avisem):
[Gemma FT em dataset de instruções estilo Alpaca](https://colab.research.google.com/drive/10NbwlsRChbma1v55m8LAPYG15uQv6HLo) e
[Fazer RLAIF via DPO sobre Zephyr](https://colab.research.google.com/drive/15vttTpzzVXv_tJwEk-hIcQ0S9FcEWvwP).

Impacto climático:
* Para avaliar a pegada de carbono do treinamento do seu modelo, você pode usar ferramentas como o [Code Carbon](https://codecarbon.io) (melhor, integrado em 🤗 Transformers) ou o [ML CO2 Impact](https://mlco2.github.io/impact).
* Recomendamos este [vídeo](https://www.youtube.com/watch?v=ftWlj4FBHTg) de motivação, este [artigo](https://huggingface.co/blog/carbon-emissions-on-the-hub) do blog da HF e a seção da [documentação](https://huggingface.co/docs/hub/model-cards-co2) de 🤗 Transformers que aborda este tema.

### 📝 Documentação

* [Docs: como escrever uma boa Dataset Card](https://huggingface.co/docs/datasets/dataset_card): é a documentação oficial do Hugging Face, inclui um template e alguns bons exemplos.
* [Docs: como escrever uma Model Card](https://huggingface.co/docs/hub/model-cards): guia oficial do Hugging Face, inclui um link para o Space para criar automaticamente e uma explicação de cada seção.
* [Space: Model Card Creator](https://huggingface.co/spaces/huggingface/Model_Cards_Writing_Tool), Space que guia vocês na criação da model card de vocês.
* [Detecção e mitigação de vieses em modelos de linguagem](https://somosnlp.org/hackathon-2023/evaluacion-de-sesgos), palestra dada por María Grandury, fundadora da SomosNLP.

<center style="margin-top:40px;"><a href="https://somosnlp.org/pt/hackathon/retos" target="_blank" style="background-color:gray; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Voltar aos desafios</a></center>
