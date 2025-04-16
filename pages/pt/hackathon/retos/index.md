---
title: "Desafios #HackathonSomosNLP 2025"
description: Vamos possibilitar a criação de LLMs alinhados com a cultura da LATAM e da Península Ibérica.
lang: pt
cover: https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg
---

O hackathon deste ano está focado na criação de recursos que permitam a avaliação e o alinhamento de modelos de linguagem com a cultura dos países da América Latina e da Península Ibérica.

O hackathon consiste em um desafio principal e vários mini desafios com os quais você também pode acumular pontos para os prêmios finais e ganhar prêmios extras. A pontuação máxima total é de 10 pontos.

Antes de começar:
- ✅ Junte-se ao [servidor Discord da SomosNLP](https://discord.com/invite/my8w7JUxZR)
- ✅ Crie uma conta no [Hugging Face](https://huggingface.co/join)
- ✅ Preencha o [formulário de inscrição](https://forms.gle/bDaBC7XV3iu2trj59)
- ✅ Junte-se à [organização Hugging Face](https://huggingface.co/organizations/somosnlp-hackathon-2025/share/BMALwncoPyZLRdPuzwugnsDzXHsbLnjjGD) do hackathon, onde datasets, modelos e demos serão compartilhados
- ✅ [Crie ou junte-se a uma equipe](https://discord.com/channels/938134488670675055/1082369575666073611), criar um tópico no canal #encuentra-equipo é a maneira de registrar sua equipe para o hackathon

Se você tiver alguma dúvida:
- Verifique o canal [#anuncios](https://discord.com/channels/938134488670675055/944255490748207115), recomendamos ativar as notificações do canal, publicamos no máximo 1 vez por dia
- Faça suas perguntas no canal [#pedir-ajuda](https://discord.com/channels/938134488670675055/1051997272356966430) do Discord para que todos possam se beneficiar da resposta
- Os eventos são anunciados no canal [#eventos](https://discord.com/channels/938134488670675055/939934987581534228) e adicionados ao [Google Calendar](https://calendar.google.com/calendar/u/0?cid=ZWM3MGZhODIzNmYyNzBlMTYwYzFiMjdhNDgzZWMyMjA1ZjQwYzUyN2E5N2MwZTJhZmY0OTcwZDZmZjBkYzQyMEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t)
- Você pode nos dar feedback para melhorar os guias dos desafios com este [formulário](https://forms.gle/LjQBb8B3XGqPs8Ws9) (anônimo)

Vamos nessa! 🚀


## ✨ Mini desafios

### ✅ Exames (INCLUDE)

Procure exames de múltipla escolha do seu país para avaliar o conhecimento dos LLMs. Priorize exames em idiomas diferentes do espanhol e/ou focados em temas culturais (por exemplo, história, literatura). Usaremos essas perguntas e respostas para estender o benchmark aberto INCLUDE.

*9 de abril - 21 de abril | máx 1 ponto*

Requisitos: Saber pesquisar na internet

- [Participe agora!](https://docs.google.com/spreadsheets/d/1QLPQ7gah9yzG3-1BPIw5Jp994Rz8L_yZT8obgWH8S2Y)
- [Guias, material de apoio e incentivos](https://somosnlp.org/pt/hackathon/retos/include)

Recursos:
- GitHub repo: [amayuelas/corpus-automation](https://github.com/amayuelas/corpus-automation)

### 👀 Estereótipos

Compartilhe e avalie estereótipos para ajudar a mitigar vieses dos LLMs.

*9 de abril - 7 de maio | máx 1 ponto*

Requisitos: Ter vivido em sociedade

- [Participe agora!](https://ediadev.ngrok.app/)
- [Guias, material de apoio e incentivos](https://somosnlp.org/pt/hackathon/retos/estereotipos)


### ❓ Perguntas Culturais (BLEND)

Responda perguntas sobre seu país para avaliar o conhecimento cultural dos LLMs. Usaremos essas respostas para estender o benchmark aberto BLEND.

*14 de abril - 7 de maio | máx 2 pontos*

Requisitos: Ter vivido em sociedade

- [Participe agora!](https://somosnlp-blend-es.hf.space/)
- [Guias, material de apoio e incentivos](https://somosnlp.org/pt/hackathon/retos/blend)

## 🔥 Desafio Principal

### 📚 Dataset de Preferências (LLM Arena)

Projete prompts que avaliem a adequação cultural com seu país e escolha a melhor resposta em uma LLM Arena. Os prompts e as respostas serão coletados e compartilhados com todas as equipes participantes como dataset de preferências v0 para a fase de alinhamento. Para este desafio, você terá acesso a uma LLM Arena com 5 modelos grandes ou proprietários.

*14 de abril - 21 de abril | máx 3 pontos*

Requisitos: Ter vivido em sociedade e querer entender bem o conceito de adequação cultural

- [Participe agora!](https://fastchat-webui-908374066028.us-central1.run.app/gradio/)
- [Guias, material de apoio e incentivos](https://somosnlp.org/pt/hackathon/retos/preferencias)

### ⚙️ Opção A: Alinhamento de LLMs

Processe, filtre e estenda o dataset de preferências v0 adaptando-o ao seu caso de uso. Use-o para alinhar um LLM usando técnicas de treinamento otimizado e alinhamento como LoRA, quantização e otimização direta de preferências (DPO). Para este desafio, cada equipe terá acesso a 500 USD da API da Cohere e uma GPU L40S da Hugging Face.

*21 de abril - 5 de maio | máx 3 pontos*

Requisitos: Saber programar

<details>
<summary>Mais informações</summary>

Guias e material de apoio:
- Notebook de exemplo para alinhar um LLM com DPO

Incentivos:
- Soma até 3 pontos à pontuação total da sua equipe

Muito obrigado a:
- Cohere: Créditos API no valor de 500 USD para cada equipe
- Hugging Face: GPUs L40S para cada equipe (L40S = 8 vCPU, 62 GB RAM, 48 GB VRAM)

</details>

### 🎨 Opção B: Projeto Multimodal Cultural

Crie um modelo multimodal que gere descrições de imagens levando em conta o contexto. Para este desafio, cada equipe terá acesso a 500 USD da API da Cohere e uma GPU L40S da Hugging Face.

*21 de abril - 5 de maio | máx 3 pontos*

Requisitos: Ter experiência em NLP, haverá menos material de apoio para este desafio do que para a opção A

<details>
<summary>Mais informações</summary>

Guias e material de apoio:
- Notebook de exemplo para treinar um modelo de geração de descrições de imagens

Incentivos:
- Soma até 3 pontos à pontuação total da sua equipe

Muito obrigado a:
- Cohere: Créditos API no valor de 500 USD para cada equipe
- Hugging Face: GPUs L40S para cada equipe (L40S = 8 vCPU, 62 GB RAM, 48 GB VRAM)

</details>

### 🎥 Criação de uma Demo

Crie uma demo do seu projeto em um Space do Hugging Face para que todos possam ver seu trabalho.

*21 de abril - 5 de maio | máx 0,5 pontos*

<details>
<summary>Mais informações</summary>

Diretrizes e material de apoio:
- Código de exemplo para criar uma demo no Hugging Face

Incentivos:
- Adicione até 0,5 pontos à pontuação total da sua equipe
- 2 ou 3 melhores demos = extensão de tempo ZeroGPU
- Necessário para considerar o projeto concluído e ser elegível para prêmios

Muito obrigado a:
- Hugging Face: ZeroGPU para demos

</details>

### 🎥 Vídeo de 5' Apresentando o Projeto

Grave um vídeo de 5 minutos apresentando seu projeto.

*7 de maio | máx 0,5 pontos*

<details>
<summary>Mais informações</summary>

Diretrizes e material de apoio:
- Recomendações para criar uma apresentação

Incentivos:
- Adicione até 0,5 pontos à pontuação total da sua equipe
- Necessário pela Mistral para dar créditos à equipe vencedora
- Necessário para considerar o projeto concluído e ser elegível para prêmios

</details>

### 📝 Opcional: Escrita de um Paper

Com a ajuda de doutorandos e professores, escreva um paper apresentando seu projeto e envie-o para o workshop LatinX in NLP da NeurIPS, uma das conferências mais importantes da área.

<details>
<summary>Mais informações</summary>

Incentivos:
- Ganhe experiência em pesquisa
- Se seu paper for aceito, você terá a oportunidade de viajar para Vancouver para apresentá-lo!

Muito obrigado a:
- LatinX in AI: Mentorias para escrever papers

</details>
