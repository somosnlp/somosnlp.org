---
title: "Desafio Principal #HackathonSomosNLP 2026: Alinhamento de LLMs e VLLMs"
description: Como participar neste desafio e ajudar a melhorar o conhecimento cultural dos modelos de linguagem e visão-linguagem
lang: pt
cover: /images/eventos/260511_hackathon_eventbrite.png
---

## 🎯 Objetivo do desafio

- Escolhe uma das seguintes opções:
    - A. Alinha um **modelo de linguagem** (LLM) para gerar texto de forma culturalmente adequada
    - B. Adapta um **modelo multimodal visão-linguagem** (VLLM) para gerar descrições de imagens tendo em conta o contexto cultural
- Em espanhol, português ou qualquer língua da Península Ibérica ou da América Latina
- Adapta a partir de um modelo já existente (não pré-treines um do zero); recomendamos partir de modelos em torno dos 7B (e.g. [Salamandra](https://huggingface.co/BSC-LT/salamandra-7b-instruct), [Mistral](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) e [Gemma](https://huggingface.co/google/gemma-3-4b-it))
- Gera o dataset com a ajuda de 500 USD em créditos da API da Cohere! Recomendamos filtrar e estender o dataset de preferências v0 gerado em conjunto na Arena: [somosnlp-hackathon-2025/dataset-preferencias-dpo-v0](https://huggingface.co/datasets/somosnlp-hackathon-2025/dataset-preferencias-dpo-v0)
- Treina o teu modelo diretamente em JupyterLab no hub do Hugging Face — temos GPUs patrocinadas pelo 🤗!
- Faz upload do(s) modelo(s) juntamente com todos os notebooks utilizados para hf.co/somosnlp-hackathon-2026
- Escreve a [Model Card](https://huggingface.co/spaces/huggingface/Model_Cards_Writing_Tool); inclui ligações para o dataset e os notebooks utilizados (e.g. pré-processamento, treino)

---

## Guia

### ✅ Preparação

<details>
<summary>Requisitos por equipa</summary>

1. Contribuir com 100 prompts **de qualidade** para o dataset de [preferências](https://somosnlp.org/pt/hackathon/retos/preferencias)
2. Responder a 200 perguntas do dataset de avaliação ([BLEND](https://somosnlp.org/pt/hackathon/retos/blend))
3. Pedir os 500 USD de créditos da API da Cohere (depois de completar os pontos 1 e 2, mencionar @mariagrandury no canal da vossa equipa para receber instruções)
4. Criar na organização hf.co/somosnlp-hackathon-2026 um Space com o template de [jupyterlab](https://huggingface.co/docs/hub/spaces-sdks-docker-jupyter)
5. Preencher o [formulário de registo](https://forms.gle/mLKEURUXGiNhq31T9)

</details>

### 📚 Dataset

Os dados são o mais importante no desenvolvimento de um modelo, e também lhes vamos dar mais peso na altura de avaliar os projetos 👀

- Gera um dataset para o teu projeto:
    - Usa como versão inicial do teu dataset o que foi gerado em conjunto na Arena: [somosnlp-hackathon-2025/dataset-preferencias-dpo-v0](https://huggingface.co/datasets/somosnlp-hackathon-2025/dataset-preferencias-dpo-v0)
    - Aproveita os 500 USD de créditos da API da Cohere que cada equipa tem para o filtrar, melhorar e estender com mais prompts e respostas desenhados especificamente para o teu caso de uso
    - Tem em conta que, tratando-se de temas culturais, é muito importante que tudo o que seja gerado sinteticamente seja revisto por uma pessoa (podem usar [Argilla](https://huggingface.co/docs/hub/en/datasets-argilla))
- Faz upload do dataset para hf.co/somosnlp-hackathon-2026 e itera
- Faz upload para o repo do dataset de todos os notebooks e scripts utilizados para gerar e processar o dataset
    - Se preferires criar um repo no GitHub com todo o código, podes fazê-lo — só não te esqueças de incluir uma ligação na Dataset Card
- Preenche **bem** a Dataset Card
    - "Dataset Card" é o nome da documentação nos datasets do Hugging Face, é o README.md do repositório dos datasets
    - ATENÇÃO: É tido em conta na avaliação do projeto
    - Inclui na introdução a motivação do projeto e o seu impacto
    - Detalha o processo de geração e processamento, inclui as bibliotecas utilizadas e menciona os testes feitos, inclui as ligações para o código
    - Especifica a licença: de preferência `apache-2.0`, caso contrário, explica porquê
    - Avalia os enviesamentos do dataset, se está balanceado, que variedades da língua ou opiniões representa, etc.

Como nomear os datasets:
- O nome do dataset com os (mínimo 100) prompts que enviaram à LLM Arena deve conter `prompt`. Por exemplo: `normas_culturales_colombia_prompts`
- O nome dos datasets de preferências deve conter o nome do algoritmo principal para o qual podem ser utilizados (`dpo` ou `kto`). Por exemplo: `normas_culturales_colombia_dpo`
- Se o dataset for multimodal, deve conter `image`. Por exemplo: `utensilios_ecuador_images_kto`

### ⚙️ Modelo

1. Cria na organização hf.co/somosnlp-hackathon-2026 um Space com o template de [JupyterLab](https://huggingface.co/docs/hub/spaces-sdks-docker-jupyter)
2. A equipa do Hugging Face vai atribuir um grant de uma *L40S* ao Space
    - Configura o tempo de "auto-sleep" para 5 minutos para garantir um uso responsável 🌱
3. Desenha o notebook de treino
    - Guarda o modelo resultante diretamente em hf.co/somosnlp-hackathon-2026
    - Utiliza a biblioteca CodeCarbon para avaliar o impacto climático
4. Faz testes com modelos pequenos e subconjuntos do dataset para verificar que o código está correto e não encontrar bugs depois de várias horas de treino.
5. Lança o treino, revê os resultados e itera
    - Podes experimentar e.g. diferentes algoritmos ou modelos base
    - Não é preciso criar um repo diferente para cada modelo, se fizeres push para o mesmo repo, o modelo atualizado ficará guardado como um novo commit (ao qual podes ligar a partir da Model Card se quiseres)
6. **Descarrega os notebooks de processamento do dataset e de treino do modelo, faz upload deles para o repo do modelo** (MUITO IMPORTANTE) e elimina o Space de JupyterLab
7. Preenche **bem** a Model Card
    - "Model Card" é o nome da documentação nos modelos do Hugging Face, é o README.md do repositório dos modelos
    - ATENÇÃO: É tido em conta na avaliação do projeto
    - Recomendação: Vai descrevendo os testes à medida que os fazes, assim como o processo de melhoria do dataset e de treino do modelo
    - Inclui na introdução a motivação do projeto e o seu impacto
    - Detalha o processo de treino, inclui as bibliotecas utilizadas e menciona os testes feitos, inclui as ligações para o código
    - Especifica a licença: de preferência `apache-2.0`, caso contrário, explica porquê
    - Avalia os enviesamentos do modelo
    - Avalia o impacto ambiental

---

## Recursos

A seguir partilhamos imensos recursos para que possam desenvolver projetos de grande qualidade. Os recursos marcados com ⭐ correspondem a palestras e workshops dados durante o hackathon e pensados especificamente para vos ajudar nesta edição.

### 📚 Dataset

A API da Cohere:
- ⭐ [Workshop prático: Como utilizar a API da Cohere](https://www.youtube.com/watch?v=S_Wky6D9Nf0&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) dado por Alejandro Rodriguez, Research Engineer na Cohere. Utilizem os modelos da Cohere para limpar e estender o vosso dataset.

Criação de datasets:
- ⭐ [Red Teaming para modelos de linguagem](https://www.youtube.com/watch?v=pGOXE4rrO9M&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6), dado por Luis Vasquez, da equipa de Reinforcement Learning, Alignment & Red Teaming do Barcelona Supercomputing Center.
- ⭐ [MuSeD: Criação de um corpus multimodal em espanhol para a deteção de sexismo em vídeos de redes sociais](https://www.youtube.com/watch?v=w1ikWRaBQd0&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6), dado por Laura De Grazia da Universitat de Barcelona.
- [Como anotar corpora linguísticos para treinar LLMs](https://www.youtube.com/watch?v=d6vrflcIY-g&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J), dado por Marta Guerrero @IIC, co-criadora de 3 dos corpora que formam La Leaderboard.
- [Distilabel e Argilla, ferramentas para criar modelos como o Notus](https://www.youtube.com/watch?v=riM3pgV4m_I&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J) dado por Gabriel Martín, MLE @Argilla (notebook disponível).

Inspiração:
- ⭐ [Describing and interpreting interaction using cultural scripts](https://www.youtube.com/watch?v=jLh9Wyn7qcI&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) (palestra em inglês), dada por Lauren Sadow da Aarhus University.
- ⭐ [Expressando incerteza em tarefas multilingues](https://www.youtube.com/watch?v=TC9tOEyPqy8&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) dada por Selene Báez, investigadora pós-doutoral na University of Zurich.
- [Ética ambiental em IA: a construir narrativas sustentáveis em espanhol](https://www.youtube.com/watch?v=MJLdrXz6bSE&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J), palestra dada por Jorge Vallego, Project Lead @H4rmony. Pode servir-vos para dar uma abordagem eco-consciente ao vosso dataset.

### ⚙️ Modelo

Criação do Space de treino:
- [Docs: JupyterLab em Spaces](https://huggingface.co/docs/hub/en/spaces-sdks-docker-jupyter#jupyterlab-on-spaces), onde podem correr os vossos notebooks como sempre. ATENÇÃO a perder o armazenamento ao reiniciar o Space, guardem os notebooks!
<!--
- [Docs: AutoTrain (inglês)](https://huggingface.co/docs/autotrain/llm_finetuning), encorajamos-vos a experimentar esta plataforma no-code do Hugging Face. Vamos traduzir esta secção da documentação, avisem-nos se precisarem de ajuda para a compreender.
- [Tutorial: AutoTrain + spacerunner (inglês)](https://huggingface.co/blog/stefan-it/autotrain-flair-mobie), com esta combinação podem correr scripts no AutoTrain.
-->

Alinhamento de LLMs:
- ⭐ [Workshop prático: Alinhamento de LLMs usando Aprendizagem por Reforço](https://www.youtube.com/watch?v=wI6yjbed_1Q&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) dado por Luis Vasquez, da equipa de Reinforcement Learning, Alignment & Red Teaming do Barcelona Supercomputing Center.

Modelos multimodais:
- ⭐ [Palestra: Como fazer um Modelo Visão-Linguagem eficiente](https://www.youtube.com/watch?v=PjOXDCe_3kg&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) dada por Andrés Marafioti, ML Engineer no Hugging Face e criador do SmolVLM.
- ⭐ [Palestra: Instruction Tuning para Raciocínio Sequencial Multimodal](https://www.youtube.com/watch?v=xiAfa6rafRs&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) dada por Danae Sanchez, investigadora pós-doutoral na Universidade de Copenhaga.

Fine-tuning de LLMs:
- [Workshop prático: O impacto da qualidade dos dados num FT de LLMs](https://www.youtube.com/watch?v=hPq5NG8kA8w&list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J), dado também por Manu Romero, criador de mais de 500 modelos do Hub do Hugging Face.
- [Workshop prático: Fine-tuning de grandes modelos de linguagem](https://somosnlp.org/hackathon-2023/fine-tuning-llms) dado por Manu Romero, criador de mais de 500 modelos do Hub do Hugging Face.
- [Workshop + AMA sobre treino de LLMs](https://www.youtube.com/playlist?list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J) com Alejandro Vaca, fundador da LenguajeNaturalAI.
- Notebooks de `unsloth` para treinar mais depressa (em inglês, se precisarem que os traduzamos avisem-nos):
[Gemma FT em dataset de instruções estilo Alpaca](https://colab.research.google.com/drive/10NbwlsRChbma1v55m8LAPYG15uQv6HLo) e
[Fazer RLAIF via DPO sobre Zephir](https://colab.research.google.com/drive/15vttTpzzVXv_tJwEk-hIcQ0S9FcEWvwP).

Impacto climático:
- Para avaliar a pegada de carbono do treino do teu modelo podes utilizar ferramentas como o [Code Carbon](https://codecarbon.io) (melhor, integrado em 🤗 Transformers) ou o [ML CO2 Impact](https://mlco2.github.io/impact).
- Recomendamos-te este [vídeo](https://www.youtube.com/watch?v=ftWlj4FBHTg) de motivação, este [artigo](https://huggingface.co/blog/carbon-emissions-on-the-hub) do blog do HF e a secção da [documentação](https://huggingface.co/docs/hub/model-cards-co2) de 🤗 Transformers que aborda este tema.

### 📝 Documentação

- [Docs: como escrever uma boa Dataset Card](https://huggingface.co/docs/datasets/dataset_card): é a documentação oficial do Hugging Face, inclui um template e alguns bons exemplos.
- [Docs: como escrever uma Model Card](https://huggingface.co/docs/hub/model-cards): guia oficial do Hugging Face, inclui uma ligação para o Space para a criar automaticamente e uma explicação de cada secção.
- [Space: Model Card Creator](https://huggingface.co/spaces/huggingface/Model_Cards_Writing_Tool), Space que vos guia na criação da vossa model card.
- [Deteção e mitigação de enviesamentos em modelos de linguagem](https://somosnlp.org/hackathon-2023/evaluacion-de-sesgos), palestra dada por María Grandury, fundadora da SomosNLP.

<center style="margin-top:40px;"><a href="https://somosnlp.org/pt/hackathon/retos" target="_blank" style="background-color:gray; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Voltar aos desafios</a></center>
