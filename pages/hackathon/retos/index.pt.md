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
    description: "Procura exames de múltipla escolha para avaliar o conhecimento dos LLMs sobre o teu país. Prioriza exames em línguas diferentes do espanhol e/ou focados em temas culturais (e.g. história, literatura).",
    dates: "9 de abril - 31 de maio",
    points: "1 ponto",
    requirements: "Saber pesquisar na internet",
    link: "https://somosnlp.org/pt/hackathon/retos/include",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "Perguntas culturais (BLEND)",
    description: "Responde a perguntas sobre o teu país para avaliar o conhecimento cultural dos LLMs. Vamos usar estas respostas para estender o benchmark aberto BLEND.",
    dates: "14 de abril - 31 de maio",
    points: "2 pontos",
    requirements: "Ter vivido em sociedade",
    link: "https://somosnlp.org/pt/hackathon/retos/blend",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  }
]

const mainChallenges = [
  {
    title: "1. Gera um dataset de preferências",
    description: "Desenha prompts que avaliem a adequação cultural com o teu país e escolhe a melhor resposta numa LLM Arena. Os prompts e as respostas vão ser recolhidos e partilhados com todas as equipas participantes como dataset de preferências v0 para a fase de alinhamento.",
    dates: "14 de abril - 21 de maio",
    points: "3 pontos",
    requirements: "Ter vivido em sociedade e querer compreender bem o conceito de adequação cultural",
    link: "https://somosnlp.org/pt/hackathon/retos/preferencias",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "2.A. Alinha um modelo textual (LLM)",
    description: "Processa, filtra e estende o dataset de preferências v0 adaptando-o ao teu caso de uso. Usa-o para alinhar um LLM com técnicas de treino otimizado e alinhamento como LoRA, quantização e otimização direta de preferências (DPO).",
    dates: "21 de abril - 31 de maio (Máx. 2 semanas)",
    points: "3 pontos",
    requirements: "Saber programar",
    link: "https://somosnlp.org/pt/hackathon/retos/alineamiento",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "2.B. Alinha um modelo multimodal",
    description: "Gera um dataset de imagens e descrições utilizando a API da Cohere. Usa-o para criar um modelo multimodal (VLLM) que gere descrições de imagens tendo em conta o contexto, usando as últimas técnicas de treino otimizado.",
    dates: "21 de abril - 31 de maio (Máx. 2 semanas)",
    points: "3 pontos",
    requirements: "Ter experiência em PLN",
    link: "https://somosnlp.org/pt/hackathon/retos/alineamiento",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  }
]

const finalChallenges = [
  {
    title: "3. Cria uma demo",
    description: "Cria uma demo do teu projeto num Space do Hugging Face para que toda a gente possa ver o teu trabalho.",
    dates: "Até 31 de maio",
    points: "0,5 pontos",
    requirements: "Ter completado um desafio principal",
    link: "https://somosnlp.org/pt/hackathon/retos/presentacion",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "4. Grava um vídeo",
    description: "Grava um vídeo de 5 minutos a apresentar o teu projeto ao júri e ao resto da comunidade.",
    dates: "Envio até 1 de junho",
    points: "0,5 pontos",
    requirements: "Ter completado um desafio principal",
    link: "https://somosnlp.org/pt/hackathon/retos/presentacion",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  },
  {
    title: "5. (Opcional) Escreve um paper",
    description: "Escreve um paper a descrever o teu projeto. Se tiveres interesse, podemos orientar-te e ajudar-te a submetê-lo a um workshop do LatinX in NLP.",
    dates: "A partir de junho",
    points: "0,5 pontos",
    requirements: "Ter completado um desafio principal",
    link: "https://somosnlp.org/pt/hackathon/retos/presentacion",
    cover: "/images/eventos/260511_hackathon_eventbrite.png"
  }
]
</script>

O hackathon deste ano foca-se na criação de recursos que permitam avaliar e alinhar modelos de linguagem com a cultura dos países da América Latina e da Península Ibérica. O hackathon foi prorrogado **até 31 DE MAIO**.

O hackathon é composto por um desafio principal e vários mini desafios, com os quais também podem acumular pontos para os prémios finais e ganhar prémios extra. A pontuação máxima total é de 10 pontos.

Nesta página vais encontrar informação sobre:
- Primeiros passos
- Incentivos e prémios
- Mini desafios
- Desafio principal
- Perguntas frequentes

Muito sucesso! 🚀

---

## 👣 Primeiros passos

Antes de começar, toda a gente tem de:
- ✅ Juntar-se ao [servidor de Discord da SomosNLP](https://discord.com/invite/my8w7JUxZR)
- ✅ Criar uma conta no [Hugging Face](https://huggingface.co/join)
- ✅ Preencher o [formulário de inscrição](https://hackathon-somosnlp-2026.eventbrite.com)
- ✅ Juntar-se à [organização do hackathon no Hugging Face](https://huggingface.co/organizations/somosnlp-hackathon/share/BMALwncoPyZLRdPuzwugnsDzXHsbLnjjGD), onde vão ser partilhados os datasets, modelos e demos

Para criar uma equipa:
- Podes inscrever-te com pessoas que já conheças (por exemplo, o teu grupo da turma ou do trabalho) ou conhecer pessoas da comunidade SomosNLP de outros países, universidades e empresas. Se quiseres conhecer pessoas novas, consulta o [canal #encuentra-equipo](https://discord.com/channels/938134488670675055/1082369575666073611)
- Depois de formarem a equipa, UMA pessoa tem de [registar a equipa](https://forms.gle/mLKEURUXGiNhq31T9)

---

## 👏 Incentivos e prémios

Ao participar terás a oportunidade de:
- ✨ Aprender com workshops e palestras em direto
- ✨ Aceder a 500 USD em créditos da API da Cohere
- ✨ Aceder a uma GPU L40S do Hugging Face
- ✨ Ganhar 1000 USD em créditos da API da Mistral
- ✨ Ganhar centenas de USD em créditos GPU e livros de IA e linguagem
- ✨ Ganhar acesso a um Mestrado online em IA
- ✨ Ganhar um bilhete para a conferência online da WomenTech Network
- ✨ Ganhar uma nomeação para a rede de talento Nova
- ✨ Ganhar mentorias com pessoas de referência da área do PLN
- ✨ Copublicar papers em conferências internacionais de PLN
- ✨ Conseguir um certificado de participação (ou de equipa vencedora) do hackathon

Mãos à obra! 🚀

---

## ✨ Mini desafios

Participa nestes mini desafios para ajudar a criar bases de dados que avaliem o conhecimento cultural e os estereótipos dos LLMs. Vais acumular pontos e podes ganhar prémios extra!

<ChallengesGrid :challenges="miniChallenges" />

---

## 🔥 Desafio principal

1. Gera um dataset de preferências
2. Alinha um modelo textual (opção A) ou multimodal (opção B) — à tua escolha
3. Cria uma demo do teu projeto
4. Apresenta o teu projeto num vídeo de 5 minutos
5. (Opcional) escreve um paper a apresentar o teu projeto

<ChallengesGrid :challenges="mainChallenges" />

<ChallengesGrid :challenges="finalChallenges" />

---

## ❓ Perguntas frequentes

<details>
<summary>Porque é que devo participar?</summary>

Ao juntares-te a este hackathon terás a oportunidade de:

- ✅ Compreender como funcionam os grandes modelos de linguagem, tanto textuais (LLMs) como multimodais (VLLMs), e descobrir os desafios de cada etapa do seu desenvolvimento: criação do corpus, treino, alinhamento e avaliação
- ✅ Participar na criação do primeiro corpus de preferências de qualidade e diverso para alinhar LLMs com a cultura dos países da América Latina e da Península Ibérica (excelente como experiência e ótimo para o CV)
- ✅ Fazer parte da equipa que cria algumas das bases de dados da primeira leaderboard aberta de LLMs em espanhol: La Leaderboard
- ✅ Esclarecer todas as tuas dúvidas sobre PLN durante sessões de mentoria "Ask Me Anything"
- ✅ Receber apoio para apresentar o teu trabalho num paper
- ✅ Ganhar prémios para continuares a crescer profissionalmente e um certificado para partilhar no LinkedIn
- ✅ Juntar-te à maior comunidade de pessoas lusófonas e hispanofalantes que estudam, trabalham e investigam em PLN

</details>

<details>
<summary>Qual é o nível necessário?</summary>

A equipa da SomosNLP quer encorajar-te a participar, independentemente dos teus conhecimentos atuais. Em edições anteriores contámos com grupos de institutos de investigação e grupos de estudantes de licenciatura — todos os projetos contam!

- 📖 Vamos dar uma série de **workshops práticos** a mostrar como desenvolver um projeto, para teres um exemplo de referência.

<!-- Para aquecer podes ver os da edição anterior:

  - [Fine-tuning LLMs (Manu Romero)](https://somosnlp.org/hackathon-2023/fine-tuning-llms)
  - [Etiquetagem de dados com Argilla (Daniel Vila)](https://somosnlp.org/hackathon-2023/etiquetado-de-datos-con-argilla) -->

- ❓ Vamos organizar **AMAs** (do inglês, Ask Me Anything) com especialistas e mentores para esclarecerem as tuas dúvidas.

</details>

<details>
<summary>De que depende a complexidade dos projetos?</summary>

Vamos disponibilizar um exemplo de como criar um dataset, treinar um modelo e criar uma demo. Cabe-te a ti e à tua equipa decidir quanto investigar e trabalhar para melhorar a versão base. A dificuldade depende também do caso de uso, da origem dos dados, do tempo dedicado à sua curadoria, da técnica de treino, das iterações que fizerem e de quão elaborada querem que seja a vossa demo. Têm liberdade para escolher tudo!

</details>

<details>
<summary>São mesmo necessárias 4 semanas?</summary>

Não, depende da tua disponibilidade — podes desenvolver um bom projeto numa semana. Sabemos que as pessoas estudam e trabalham, por isso damos mais tempo do que o estritamente necessário para que toda a gente possa participar. Também queremos dar-te tempo extra para aproveitares a oportunidade de assistir em direto às palestras e mentorias do hackathon.

</details>

<details>
<summary>Até quando posso criar uma equipa?</summary>

EDITADO: Aceitamos novas equipas até 23 de maio. O dia final para entregar projetos é 31 de maio.

</details>

<details>
<summary>Como me junto a uma equipa?</summary>

Lê a secção "Para criar uma equipa:" no início desta página e o README no canal #encuentra-equipo do nosso servidor de Discord :)

</details>

<details>
<summary>Pode haver equipas de 1 pessoa?</summary>

Sim, aceitamos equipas de 1 a 5 pessoas.

</details>

<details>
<summary>Como nos recomendam que nos organizemos?</summary>

- Usem o canal do vosso projeto no Discord para comunicarem e organizarem-se.
- Como é um hackathon internacional, recomendamos comunicação assíncrona ou que dividam o trabalho e façam reuniões com menos pessoas.
- Marquem reuniões ou conversem espontaneamente usando os novos canais de voz da categoria "SALAS DE REUNIÓN" do Discord.
- Fixem no canal do projeto as mensagens importantes — por exemplo: divisão de tarefas, dia da próxima reunião, etc. Para fixar uma mensagem, clica nos três pontinhos e seleciona "Fixar mensagem".
- Para maior clareza, podem também criar um documento partilhado entre os membros da equipa para escrever o objetivo do projeto, dividir tarefas e por aí fora (e fixem o link no chat).

</details>

<details>
<summary>Não percebo o Discord — quais são os canais mais importantes?</summary>

- Vê o canal [#anuncios](https://discord.com/channels/938134488670675055/944255490748207115); recomendamos ativar as notificações do canal — publicamos 2 a 3 vezes por semana.
- Faz as tuas perguntas no canal [#pide-ayuda](https://discord.com/channels/938134488670675055/1051997272356966430) do Discord para que toda a gente possa beneficiar da resposta.
- Anunciamos os eventos no canal [#eventos](https://discord.com/channels/938134488670675055/939934987581534228) e adicionamo-los ao [Google Calendar](https://calendar.google.com/calendar/u/0?cid=ZWM3MGZhODIzNmYyNzBlMTYwYzFiMjdhNDgzZWMyMjA1ZjQwYzUyN2E5N2MwZTJhZmY0OTcwZDZmZjBkYzQyMEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t).

</details>

<details>
<summary>Como posso ficar a saber dos eventos?</summary>

- Anunciamos os eventos no canal [#eventos](https://discord.com/channels/938134488670675055/939934987581534228)
- Adicionamo-los ao [Google Calendar](https://calendar.google.com/calendar/u/0?cid=ZWM3MGZhODIzNmYyNzBlMTYwYzFiMjdhNDgzZWMyMjA1ZjQwYzUyN2E5N2MwZTJhZmY0OTcwZDZmZjBkYzQyMEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t)
- Anunciamo-los nas redes sociais ([LinkedIn](https://www.linkedin.com/company/somosnlp), [X (Twitter)](https://x.com/somosnlp_))
- [Segue-nos no YouTube](https://www.youtube.com/c/somosnlp?sub_confirmation=1) e guarda a [playlist do hackathon 2026](https://www.youtube.com/playlist?list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6)

</details>

<details>
<summary>Como posso dar feedback sobre o evento?</summary>

- Podes dar-nos feedback para melhorar os guias dos desafios através deste [formulário](https://forms.gle/LjQBb8B3XGqPs8Ws9) (anónimo)
- Vamos também partilhar um formulário de feedback geral no final do evento

</details>


*Se te dissemos que existe nesta página informação que não consegues encontrar, apaga as cookies e recarrega a página.*

---

## 🙌 Outras formas de apoiar a adequação cultural dos LLMs

<details>
<summary>Como posso ajudar?</summary>

- Partilha as publicações das contas da @SomosNLP ([LinkedIn](https://www.linkedin.com/company/somosnlp), [X (Twitter)](https://x.com/somosnlp_)) e convida os teus colegas de trabalho e da turma a formar uma equipa!
<!-- - Tens 2 horinhas para nos ajudar a organizar este evento incrível? Estamos à tua espera, [junta-te à equipa](https://forms.gle/radg18NMLRZMPu38A). -->
- Estás na universidade? [Partilha esta informação com o(a) teu(tua) professor(a)](https://somosnlp.org/pt/hackathon/universidades) ou com alguém do grupo de IA/informática para que a tua universidade colabore com o evento.
<!-- - Gostarias de partilhar o teu conhecimento com a comunidade? Propõe uma [palestra](https://forms.gle/YpUvifDNLG6E56Cy9) ou uma [mentoria](https://forms.gle/7UmsVDnFmNo1pCrf9).
- Fazes parte de um grupo de investigação? Talvez vos interesse [colaborar doando um corpus](https://somosnlp.org/donatucorpus). -->
- Queres apoiar a iniciativa com visibilidade, patrocinando vouchers ou com uma doação financeira? [Patrocina o hackathon](https://forms.gle/sEkxstwbJSRYpgDa8)!

</details>
