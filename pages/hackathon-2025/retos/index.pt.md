---
title: "Desafios #HackathonSomosNLP 2025"
description: Vamos possibilitar a criação de LLMs alinhados com a cultura da LATAM e da Península Ibérica.
lang: pt
cover: /images/eventos/250401_hackathon_sinfecha.jpg
---

<script setup>
import ChallengesGrid from '../../../src/components/ChallengesGrid.vue'

const miniChallenges = [
  {
    title: "Exames (INCLUDE)",
    description: "Procure exames de múltipla escolha do seu país para avaliar o conhecimento dos LLMs. Priorize exames em idiomas diferentes do espanhol e/ou focados em temas culturais (por exemplo, história, literatura).",
    dates: "9 de abril - 31 de maio (PRORROGADO)",
    points: "1 ponto",
    requirements: "Saber pesquisar na internet",
    link: "https://somosnlp.org/pt/hackathon-2025-2025/retos/include",
    cover: "/images/eventos/250401_hackathon_sinfecha.jpg"
  },
  {
    title: "Estereótipos",
    description: "Compartilhe e avalie estereótipos para ajudar a mitigar vieses dos LLMs.",
    dates: "9 de abril - 15 de maio (PRORROGADO)",
    points: "1 ponto",
    requirements: "Ter vivido em sociedade",
    link: "https://somosnlp.org/pt/hackathon-2025-2025/retos/estereotipos",
    cover: "/images/eventos/250401_hackathon_sinfecha.jpg"
  },
  {
    title: "Perguntas Culturais (BLEND)",
    description: "Responda perguntas sobre seu país para avaliar o conhecimento cultural dos LLMs. Usaremos essas respostas para estender o benchmark aberto BLEND.",
    dates: "14 de abril - 31 de maio (PRORROGADO)",
    points: "2 pontos",
    requirements: "Ter vivido em sociedade",
    link: "https://somosnlp.org/pt/hackathon-2025-2025/retos/blend",
    cover: "/images/eventos/250401_hackathon_sinfecha.jpg"
  }
]

const mainChallenges = [
  {
    title: "1. Gere um Dataset de Preferências",
    description: "Projete prompts que avaliem a adequação cultural com seu país e escolha a melhor resposta em uma LLM Arena. Os prompts e as respostas serão coletados e compartilhados com todas as equipes participantes como dataset de preferências v0 para a fase de alinhamento.",
    dates: "14 de abril - 15 de maio (PRORROGADO)",
    points: "3 pontos",
    requirements: "Ter vivido em sociedade e querer entender bem o conceito de adequação cultural",
    link: "https://somosnlp.org/pt/hackathon-2025-2025/retos/preferencias",
    cover: "/images/eventos/250401_hackathon_sinfecha.jpg"
  },
  {
    title: "2.A. Alinhe um Modelo Textual (LLM)",
    description: "Processe, filtre e estenda o dataset de preferências v0 adaptando-o ao seu caso de uso. Use-o para alinhar um LLM usando técnicas de treinamento otimizado e alinhamento como LoRA, quantização e otimização direta de preferências (DPO).",
    dates: "21 de abril - 31 de maio (Máx. 2 semanas)",
    points: "3 pontos",
    requirements: "Saber programar",
    link: "https://somosnlp.org/pt/hackathon-2025-2025/retos/preferencias",
    cover: "/images/eventos/250401_hackathon_sinfecha.jpg"
  },
  {
    title: "2.B. Alinhe um Modelo Multimodal",
    description: "Gere um dataset de imagens e descrições usando a API da Cohere. Use-o para criar um modelo multimodal (VLLM) que gere descrições de imagens levando em conta o contexto usando as últimas técnicas de treinamento otimizado.",
    dates: "21 de abril - 31 de maio (Máx. 2 semanas)",
    points: "3 pontos",
    requirements: "Ter experiência em NLP",
    link: "https://somosnlp.org/pt/hackathon-2025-2025/retos/preferencias",
    cover: "/images/eventos/250401_hackathon_sinfecha.jpg"
  }
]

const finalChallenges = [
  {
    title: "3. Crie uma Demo",
    description: "Crie uma demo do seu projeto em um Space do Hugging Face para que todos possam ver seu trabalho.",
    dates: "Até 31 de maio (PRORROGADO)",
    points: "0,5 pontos",
    requirements: "Ter completado algum desafio principal",
    link: "https://somosnlp.org/pt/hackathon-2025-2025/retos/presentacion",
    cover: "/images/eventos/250401_hackathon_sinfecha.jpg"
  },
  {
    title: "4. Grave um Vídeo",
    description: "Grave um vídeo de 5 minutos apresentando seu projeto para o júri e o resto da comunidade.",
    dates: "Envio até 1 de junho (PRORROGADO)",
    points: "0,5 pontos",
    requirements: "Ter completado algum desafio principal",
    link: "https://somosnlp.org/pt/hackathon-2025-2025/retos/presentacion",
    cover: "/images/eventos/250401_hackathon_sinfecha.jpg"
  },
  {
    title: "5. (Opcional) Escreva um Paper",
    description: "Escreva um paper descrevendo seu projeto. Se você estiver interessado, podemos orientá-lo e ajudá-lo a enviá-lo para um workshop do LatinX in NLP.",
    dates: "A partir de junho",
    points: "0,5 pontos",
    requirements: "Ter completado algum desafio principal",
    link: "https://somosnlp.org/pt/hackathon-2025-2025/retos/presentacion",
    cover: "/images/eventos/250401_hackathon_sinfecha.jpg"
  }
]
</script>

O hackathon deste ano está focado na criação de recursos que permitam a avaliação e o alinhamento de modelos de linguagem com a cultura dos países da América Latina e da Península Ibérica. O hackathon foi prorrogado **até 31 DE MAIO**.

O hackathon consiste em um desafio principal e vários mini desafios com os quais você também pode acumular pontos para os prêmios finais e ganhar prêmios extras. A pontuação máxima total é de 10 pontos.

Antes de começar, todas as pessoas precisam:
- ✅ Juntar-se ao [servidor Discord da SomosNLP](https://discord.com/invite/my8w7JUxZR)
- ✅ Criar uma conta no [Hugging Face](https://huggingface.co/join)
- ✅ Preencher o [formulário de inscrição](https://forms.gle/bDaBC7XV3iu2trj59)
- ✅ Juntar-se à [organização Hugging Face do hackathon](https://huggingface.co/organizations/somosnlp-hackathon-2025/share/BMALwncoPyZLRdPuzwugnsDzXHsbLnjjGD), onde datasets, modelos e demos serão compartilhados

Para criar uma equipe:
- Você pode se inscrever com pessoas que já conhece (por exemplo, seu grupo de classe ou trabalho) ou conhecer pessoas da comunidade SomosNLP de outros países, universidades e empresas. Se quiser conhecer pessoas, confira o [canal #encuentra-equipo](https://discord.com/channels/938134488670675055/1082369575666073611)
- Depois de criar a equipe, UMA pessoa deve [registrar a equipe](https://forms.gle/mLKEURUXGiNhq31T9)

## 👏 Incentivos e prêmios

Ao participar, você terá a oportunidade de:
- ✨ Aprender com workshops e palestras ao vivo
- ✨ Obter acesso aos 500 USD da API da Cohere
- ✨ Obter acesso a GPUs L40S da Hugging Face
- ✨ Ganhar 1000 USD em créditos da API da Mistral
- ✨ Ganhar centenas de USD em créditos GPU e livros de IA e linguagem
- ✨ Ganhar acesso a um Mestrado online em IA
- ✨ Ganhar uma entrada para a conferência online da WomenTech Network
- ✨ Ganhar uma indicação para a rede de talentos Nova
- ✨ Ganhar mentorias com pessoas relevantes na área de NLP
- ✨ Co-publicar papers em conferências internacionais de NLP
- ✨ Obter um certificado de participação (ou equipe vencedora) do hackathon

Vamos nessa! 🚀


## ✨ Mini desafios

Participe destes mini desafios para contribuir com a criação de bancos de dados que avaliem o conhecimento cultural e estereótipos dos LLMs. Você poderá acumular pontos e ganhar prêmios extras!

<ChallengesGrid :challenges="miniChallenges" />

## 🔥 Desafio Principal

1. Gere um dataset de preferências
2. Alinhe um modelo textual (opção A) ou multimodal (opção B), à sua escolha
3. Crie uma demo do seu projeto
4. Apresente seu projeto em um vídeo de 5 mins
5. (Opcional) escreva um paper apresentando seu projeto

<ChallengesGrid :challenges="mainChallenges" />

<ChallengesGrid :challenges="finalChallenges" />

## ❓ Ajuda

Se você tiver alguma dúvida:
- Verifique o canal [#anuncios](https://discord.com/channels/938134488670675055/944255490748207115), recomendamos ativar as notificações do canal, publicamos no máximo 1 vez por dia
- Faça suas perguntas no canal [#pedir-ajuda](https://discord.com/channels/938134488670675055/1051997272356966430) do Discord para que todos possam se beneficiar da resposta
- Os eventos são anunciados no canal [#eventos](https://discord.com/channels/938134488670675055/939934987581534228) e adicionados ao [Google Calendar](https://calendar.google.com/calendar/u/0?cid=ZWM3MGZhODIzNmYyNzBlMTYwYzFiMjdhNDgzZWMyMjA1ZjQwYzUyN2E5N2MwZTJhZmY0OTcwZDZmZjBkYzQyMEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t)
- Você pode nos dar feedback para melhorar os guias dos desafios com este [formulário](https://forms.gle/LjQBb8B3XGqPs8Ws9) (anônimo)


## 🗓️ Eventos

#### Automatizando extração de corpus de PDFs | Alfonso Amayuelas, PhD @ Universidade da Califórnia, Santa Barbara

Como usar as últimas ferramentas em LLMs para criar datasets de QA? Neste evento, usaremos um modelo de OCR e LLMs para padronizar exames, questionários, etc.

[Gravação já disponível!](https://www.youtube.com/watch?v=Jk70bSw4tTo&list=PLTA-KAy8nxaCGGYz5CWiLZNzc31ilPDyI&index=3)

![alt text](/images/eventos/250415_alfonso_amayuelas.png)


#### Confidently wrong: expressando incerteza em tarefas multilíngues | Selene Baez, Postdoc @ Universidade de Zurique

Embora a fluência e a coerência dos Modelos de Linguagem (LLM) na geração de texto tenham melhorado significativamente, sua capacidade de gerar expressões adequadas de incerteza ainda é limitada. Por meio de uma tarefa de Q&A multilíngue de livro fechado e GPT-3.5, exploramos a precisão com que os LLMs se calibram e expressam certeza em uma variedade de idiomas, incluindo ambientes com poucos recursos.

[Gravação disponível!](https://www.youtube.com/watch?v=TC9tOEyPqy8&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6)

![alt text](/images/eventos/250410_selene_baez.png)

#### Red Teaming para Modelos de Linguagem | Luis Vasquez, Research Engineer @Barcelona Supercomputing Center

Breve introdução ao Red Teaming para Modelos de Linguagem: definição, estratégias comuns e recursos.

[Gravação disponível!](https://www.youtube.com/watch?v=pGOXE4rrO9M&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6)

![alt text](/images/eventos/250410_luis_vasquez.png)
