---
title: "Desafios #HackathonSomosNLP 2026"
description: Vamos impulsionar a criação de modelos de linguagem alinhados com a cultura dos países da América Latina e da Península Ibérica.
lang: pt
cover: /images/eventos/260511_hackathon_eventbrite.png
---

<script setup>
import ChallengesGrid from '../../../src/components/ChallengesGrid.vue'

const miniChallenges = [
  {
    title: "Exames (INCLUDE)",
    description: "Procure exames de múltipla escolha para avaliar o quanto os LLMs sabem sobre o seu país. Priorize exames em línguas diferentes do espanhol e/ou focados em temas culturais (e.g. história, literatura).",
    dates: "9 de abril a 31 de maio",
    points: "1 ponto",
    requirements: "Saber pesquisar na internet",
    link: "https://somosnlp.org/pt/hackathon/retos/include",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "Perguntas culturais (BLEND)",
    description: "Responda perguntas sobre o seu país para avaliar o conhecimento cultural dos LLMs. Vamos usar essas respostas para estender o benchmark aberto BLEND.",
    dates: "14 de abril a 31 de maio",
    points: "2 pontos",
    requirements: "Ter vivido em sociedade",
    link: "https://somosnlp.org/pt/hackathon/retos/blend",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  }
]

const mainChallenges = [
  {
    title: "1. Gere um dataset de preferências",
    description: "Crie prompts que avaliem a adequação cultural com o seu país e escolha a melhor resposta numa LLM Arena. Os prompts e as respostas serão coletados e compartilhados com todas as equipes participantes como dataset de preferências v0 para a fase de alinhamento.",
    dates: "14 de abril a 21 de maio",
    points: "3 pontos",
    requirements: "Ter vivido em sociedade e querer entender bem o conceito de adequação cultural",
    link: "https://somosnlp.org/pt/hackathon/retos/preferencias",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "2.A. Alinhe um modelo textual (LLM)",
    description: "Processe, filtre e estenda o dataset de preferências v0 adaptando para o seu caso de uso. Use o dataset para alinhar um LLM com técnicas de treinamento otimizado e alinhamento como LoRA, quantização e otimização direta de preferências (DPO).",
    dates: "21 de abril a 31 de maio (Máx. 2 semanas)",
    points: "3 pontos",
    requirements: "Saber programar",
    link: "https://somosnlp.org/pt/hackathon/retos/alineamiento",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "2.B. Alinhe um modelo multimodal",
    description: "Gere um dataset de imagens e descrições usando a API da Cohere. Use o dataset para criar um modelo multimodal (VLLM) que gere descrições de imagens levando em conta o contexto, com as últimas técnicas de treinamento otimizado.",
    dates: "21 de abril a 31 de maio (Máx. 2 semanas)",
    points: "3 pontos",
    requirements: "Ter experiência em PLN",
    link: "https://somosnlp.org/pt/hackathon/retos/alineamiento",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  }
]

const finalChallenges = [
  {
    title: "3. Crie uma demo",
    description: "Crie uma demo do seu projeto num Space do Hugging Face para que todo mundo possa ver o seu trabalho.",
    dates: "Até 31 de maio",
    points: "0,5 pontos",
    requirements: "Ter completado um desafio principal",
    link: "https://somosnlp.org/pt/hackathon/retos/presentacion",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "4. Grave um vídeo",
    description: "Grave um vídeo de 5 minutos apresentando seu projeto para o júri e para o resto da comunidade.",
    dates: "Envio até 1 de junho",
    points: "0,5 pontos",
    requirements: "Ter completado um desafio principal",
    link: "https://somosnlp.org/pt/hackathon/retos/presentacion",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "5. (Opcional) Escreva um paper",
    description: "Escreva um paper descrevendo o seu projeto. Se tiver interesse, podemos te orientar e ajudar a submeter para um workshop do LatinX in NLP.",
    dates: "A partir de junho",
    points: "0,5 pontos",
    requirements: "Ter completado um desafio principal",
    link: "https://somosnlp.org/pt/hackathon/retos/presentacion",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  }
]
</script>

O hackathon deste ano foca na criação de recursos que permitam avaliar e alinhar modelos de linguagem com a cultura dos países da América Latina e da Península Ibérica. O hackathon foi prorrogado **até 31 DE MAIO**.

O hackathon é composto por um desafio principal e por vários mini desafios, com os quais vocês também podem acumular pontos para os prêmios finais e ganhar prêmios extras. A pontuação máxima total é de 10 pontos.

Nesta página você vai encontrar informação sobre:
* Primeiros passos
* Incentivos e prêmios
* Mini desafios
* Desafio principal
* Perguntas frequentes

Boa sorte! 🚀

---

## 👣 Primeiros passos

Antes de começar, todo mundo precisa:
* ✅ Entrar no [servidor do Discord da SomosNLP](https://discord.com/invite/my8w7JUxZR)
* ✅ Criar uma conta no [Hugging Face](https://huggingface.co/join)
* ✅ Preencher o [formulário de inscrição](https://hackathon-somosnlp-2026.eventbrite.com)
* ✅ Entrar na [organização do hackathon no Hugging Face](https://huggingface.co/organizations/somosnlp-hackathon/share/BMALwncoPyZLRdPuzwugnsDzXHsbLnjjGD), onde os datasets, modelos e demos vão ser compartilhados

Para criar uma equipe:
* Você pode se inscrever com pessoas que já conhece (por exemplo, a galera da turma ou do trabalho) ou conhecer pessoas da comunidade SomosNLP de outros países, universidades e empresas. Se quiser conhecer pessoas novas, dá uma olhada no [canal #encuentra-equipo](https://discord.com/channels/938134488670675055/1082369575666073611)
* Depois de formar a equipe, UMA pessoa precisa [registrar a equipe](https://forms.gle/mLKEURUXGiNhq31T9)

---

## 👏 Incentivos e prêmios

Ao participar você terá a oportunidade de:
* ✨ Aprender com workshops e palestras ao vivo
* ✨ Ganhar acesso a 500 USD em créditos da API da Cohere
* ✨ Ganhar acesso a uma GPU L40S do Hugging Face
* ✨ Ganhar 1000 USD em créditos da API da Mistral
* ✨ Ganhar centenas de USD em créditos GPU e livros de IA e linguagem
* ✨ Ganhar acesso a um Mestrado online de IA
* ✨ Ganhar um ingresso para a conferência online da WomenTech Network
* ✨ Ganhar uma indicação para a rede de talentos Nova
* ✨ Ganhar mentorias com pessoas de referência da área de PLN
* ✨ Copublicar papers em conferências internacionais de PLN
* ✨ Conseguir um certificado de participação (ou de equipe vencedora) do hackathon

Mãos à obra! 🚀

---

## ✨ Mini desafios

Participe destes mini desafios para ajudar a criar bases de dados que avaliem o conhecimento cultural e os estereótipos dos LLMs. Você vai acumular pontos e pode ganhar prêmios extras!

<ChallengesGrid :challenges="miniChallenges" />

---

## 🔥 Desafio principal

1. Gere um dataset de preferências
2. Alinhe um modelo textual (opção A) ou multimodal (opção B), à sua escolha
3. Crie uma demo do seu projeto
4. Apresente seu projeto num vídeo de 5 minutos
5. (Opcional) escreva um paper apresentando o seu projeto

<ChallengesGrid :challenges="mainChallenges" />

<ChallengesGrid :challenges="finalChallenges" />

---

## ❓ Perguntas frequentes

<details>
<summary>Por que eu deveria participar?</summary>

Ao entrar neste hackathon, você terá a oportunidade de:

* ✅ Entender como funcionam os grandes modelos de linguagem, tanto textuais (LLMs) quanto multimodais (VLLMs), e descobrir os desafios de cada etapa do desenvolvimento: criação do corpus, treinamento, alinhamento e avaliação
* ✅ Participar da criação do primeiro corpus de preferências de qualidade e diverso para alinhar LLMs com a cultura dos países da América Latina e da Península Ibérica (excelente como experiência e ótimo para o currículo)
* ✅ Fazer parte da equipe que cria algumas das bases de dados da primeira leaderboard aberta de LLMs em espanhol: La Leaderboard
* ✅ Tirar todas as suas dúvidas sobre PLN durante sessões de mentoria "Ask Me Anything"
* ✅ Receber apoio para apresentar seu trabalho em um paper
* ✅ Ganhar prêmios para continuar crescendo profissionalmente e um certificado para compartilhar no LinkedIn
* ✅ Entrar na maior comunidade de pessoas lusófonas e hispanofalantes que estudam, trabalham e pesquisam em PLN

</details>

<details>
<summary>Qual é o nível necessário?</summary>

A equipe da SomosNLP quer incentivar você a participar, independentemente dos seus conhecimentos atuais. Em edições anteriores contamos com grupos de institutos de pesquisa e grupos de estudantes de graduação. Todos os projetos contam!

* 📖 Vamos dar uma série de **workshops práticos** mostrando como desenvolver um projeto, para você ter um exemplo de referência.

<!-- Para esquentar, você pode assistir aos da edição anterior:

  * [Fine tuning LLMs (Manu Romero)](https://somosnlp.org/hackathon-2023/fine-tuning-llms)
  * [Etiquetagem de dados com Argilla (Daniel Vila)](https://somosnlp.org/hackathon-2023/etiquetado-de-datos-con-argilla) -->

* ❓ Vamos organizar **AMAs** (do inglês, Ask Me Anything) com especialistas e mentores para tirar suas dúvidas.

</details>

<details>
<summary>De que depende a complexidade dos projetos?</summary>

Vamos disponibilizar um exemplo de como criar um dataset, treinar um modelo e criar uma demo. Cabe a você e à sua equipe decidir o quanto pesquisar e trabalhar para melhorar a versão base. A dificuldade também depende do caso de uso, da origem dos dados, do tempo dedicado à curadoria, da técnica de treinamento, das iterações que fizerem e do quão elaborada quiserem que seja a demo. Vocês têm liberdade para escolher tudo!

</details>

<details>
<summary>São mesmo necessárias 4 semanas?</summary>

Não, depende da sua disponibilidade. Você pode desenvolver um bom projeto em uma semana. Sabemos que as pessoas estudam e trabalham, por isso damos mais tempo do que o necessário para que todo mundo possa participar. Também queremos te dar tempo extra para aproveitar a oportunidade de assistir ao vivo às palestras e mentorias do hackathon.

</details>

<details>
<summary>Até quando posso criar uma equipe?</summary>

EDITADO: Damos as boas vindas a novas equipes até 23 de maio. O dia final para a entrega de projetos é 31 de maio.

</details>

<details>
<summary>Como entro em uma equipe?</summary>

Leia a seção "Para criar uma equipe:" no início desta página e o README no canal #encuentra-equipo do nosso servidor do Discord :)

</details>

<details>
<summary>Pode haver equipes de 1 pessoa?</summary>

Sim, aceitamos equipes de 1 a 5 pessoas.

</details>

<details>
<summary>Como vocês recomendam que a gente se organize?</summary>

* Usem o canal do projeto de vocês no Discord para se comunicar e se organizar.
* Como é um hackathon internacional, recomendamos comunicação assíncrona ou que vocês dividam o trabalho e façam reuniões com menos pessoas.
* Marquem reuniões ou conversem espontaneamente usando os novos canais de voz da categoria "SALAS DE REUNIÓN" do Discord.
* Fixem no canal do projeto as mensagens importantes. Por exemplo: divisão de tarefas, dia da próxima reunião, etc. Para fixar uma mensagem, clique nos três pontinhos e selecione "Fixar mensagem".
* Para maior clareza, vocês também podem criar um documento compartilhado entre os membros da equipe para anotar o objetivo do projeto, dividir tarefas e por aí vai (e fixem o link no chat).

</details>

<details>
<summary>Não entendo o Discord. Quais são os canais mais importantes?</summary>

* Confira o canal [#anuncios](https://discord.com/channels/938134488670675055/944255490748207115). Recomendamos ativar as notificações do canal, publicamos 2 a 3 vezes por semana.
* Tire suas dúvidas no canal [#pide-ayuda](https://discord.com/channels/938134488670675055/1051997272356966430) do Discord para que todo mundo possa se beneficiar da resposta.
* Anunciamos os eventos no canal [#eventos](https://discord.com/channels/938134488670675055/939934987581534228) e adicionamos ao [Google Calendar](https://calendar.google.com/calendar/u/0?cid=ZWM3MGZhODIzNmYyNzBlMTYwYzFiMjdhNDgzZWMyMjA1ZjQwYzUyN2E5N2MwZTJhZmY0OTcwZDZmZjBkYzQyMEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t).

</details>

<details>
<summary>Como posso ficar sabendo dos eventos?</summary>

* Anunciamos os eventos no canal [#eventos](https://discord.com/channels/938134488670675055/939934987581534228)
* Os adicionamos ao [Google Calendar](https://calendar.google.com/calendar/u/0?cid=ZWM3MGZhODIzNmYyNzBlMTYwYzFiMjdhNDgzZWMyMjA1ZjQwYzUyN2E5N2MwZTJhZmY0OTcwZDZmZjBkYzQyMEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t)
* Divulgamos nas redes sociais ([LinkedIn](https://www.linkedin.com/company/somosnlp), [X (Twitter)](https://x.com/somosnlp_))
* [Siga a gente no YouTube](https://www.youtube.com/c/somosnlp?sub_confirmation=1) e salve a [playlist do hackathon 2026](https://www.youtube.com/playlist?list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6)

</details>

<details>
<summary>Como posso dar feedback sobre o evento?</summary>

* Você pode dar feedback para a gente melhorar os guias dos desafios neste [formulário](https://forms.gle/LjQBb8B3XGqPs8Ws9) (anônimo)
* Vamos compartilhar um formulário de feedback geral no final do evento

</details>


*Se a gente disse que tem alguma informação nesta página que você não está achando, apague os cookies e recarregue a página.*

---

## 🙌 Outras formas de apoiar a adequação cultural dos LLMs

<details>
<summary>Como posso colaborar?</summary>

* Compartilhe as publicações das contas da @SomosNLP ([LinkedIn](https://www.linkedin.com/company/somosnlp), [X (Twitter)](https://x.com/somosnlp_)) e convide seus colegas de trabalho e da turma a formar uma equipe!
<!-- * Tem 2 horinhas para ajudar a gente a organizar este evento incrível? Estamos esperando, [entre na equipe](https://forms.gle/radg18NMLRZMPu38A). -->
* Está na universidade? [Compartilhe esta informação com o seu professor(a)](https://somosnlp.org/pt/hackathon/universidades) ou com alguém do grupo de IA/informática para que sua universidade colabore com o evento.
<!-- * Gostaria de compartilhar seu conhecimento com a comunidade? Proponha uma [palestra](https://forms.gle/YpUvifDNLG6E56Cy9) ou uma [mentoria](https://forms.gle/7UmsVDnFmNo1pCrf9).
* Faz parte de um grupo de pesquisa? Talvez vocês queiram [colaborar doando um corpus](https://somosnlp.org/donatucorpus). -->
* Quer apoiar a iniciativa com visibilidade, vouchers patrocinados ou uma doação financeira? [Patrocine o hackathon](https://forms.gle/sEkxstwbJSRYpgDa8)!

</details>
