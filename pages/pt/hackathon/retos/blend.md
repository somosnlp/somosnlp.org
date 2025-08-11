---
title: "Desafio #HackathonSomosNLP 2025: BLEND"
description: Como participar neste desafio e ajudar a melhorar o conhecimento cultural dos modelos de linguagem
lang: pt
cover: https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg
---

Responda perguntas sobre seu país para avaliar o conhecimento cultural dos LLMs. Usaremos essas respostas para estender o benchmark aberto BLEND.

*14 de abril - 31 de maio (PRORROGADO) | máx 2 pontos*

<center><a href="https://somosnlp-blend-es.hf.space/" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Participe agora!</a></center>

🌎 Responda **apenas** perguntas do país ou países com os quais você tenha um vínculo forte o suficiente para conhecer a cultura local.

✨ Incentivos (os números se referem a perguntas respondidas validadas):
- Por equipe:
    - 200 por equipe = requisito para acessar os 500 USD da API Cohere para o desafio principal
    - Cada 50 perguntas por equipe = 0,5 pontos (máx 2 pontos)
- Por pessoa:
    - 100 por pessoa = coautoria no paper do BLEND-ES

🙌 Muito obrigado a:
- CENIA: Armazenamento dos dados nos espaços de anotação
- A equipe: Eugenio Herrera, Sebastián Cifuentes, Clemente, María Grandury, Luis Vasquez e Valle Ruiz

---

## O que é BLEND e por que estamos replicando?

<details>
<summary>O que é BLEND?</summary>

Neste desafio, buscamos adaptar a metodologia de [*BLEND: A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures and Languages*](https://arxiv.org/abs/2406.09948) para a criação de um novo benchmark cultural focado nas culturas de língua hispânica.

Em resumo, no paper original foram feitas 500 perguntas a participantes de 16 países/regiões de 13 línguas diferentes, com o objetivo de criar um benchmark cultural.

Um exemplo de pergunta é: "O que as pessoas de [Nome do país] geralmente comem de sobremesa?"

Com essa informação, os autores fizeram um cruzamento de respostas e assim geraram perguntas de múltipla escolha para avaliar o conhecimento cultural de diferentes LLMs.

</details>

<details>
<summary>Qual é nossa proposta?</summary>

Com sua ajuda, buscamos replicar esta metodologia no contexto de nossa diversa realidade cultural. Na figura a seguir, você pode ver o que buscamos:

![BLEND 1](https://somosnlp.github.io/assets/images/blog/retos_2025_blend_1.png)

Note que cada quadrado em verde implica sua participação, ou seja, você será uma peça-chave na construção deste novo benchmark!

</details>

## Como começar a responder perguntas?

Para participar da anotação colaborativa de dados, primeiro você deve acessar [huggingface.co/spaces/somosnlp/blend-es](https://huggingface.co/spaces/somosnlp/blend-es).

Você precisará de uma conta no HuggingFace para entrar. Se não tiver uma, você pode criar facilmente [aqui](https://huggingface.co/join).

Uma vez dentro, você verá a seguinte interface:

![BLEND 2](https://somosnlp.github.io/assets/images/blog/retos_2025_blend_2.png)

Como você notará, há uma lista de múltiplos *datasets*, nomeados de acordo com seu país, no seguinte formato:

- PAÍS - Código ISO - **Responder**
- PAÍS - Código ISO - **Validar**

Ou seja, cada país tem um espaço para responder perguntas e outro para validar as respostas dos demais participantes.

### Instruções para responder

Ao entrar no espaço correspondente ao seu país, você encontrará a seguinte interface:

![BLEND 3](https://somosnlp.github.io/assets/images/blog/retos_2025_blend_3.png)

Ao responder as perguntas, é importante seguir estas diretrizes:

- **Responda a partir do seu contexto cultural**: Forneça respostas que reflitam a realidade cultural do seu país. Não há respostas certas ou erradas, queremos capturar a diversidade cultural.
- **Responda em seu idioma nativo**: Use o português como você fala em seu país ou região.
- **Responda de maneira breve e concisa**: Use termos precisos, entidades específicas e referências temporais claras. Por exemplo, se perguntarem a que horas as pessoas saem do trabalho, respostas como "18:00" ou "19:00" são ideais.
- **Você pode dar múltiplas opções**: Se considerar necessário, você pode fornecer até três respostas diferentes se existirem várias práticas comuns em sua cultura.
- **Especifique a região se necessário**: Se sua resposta representa mais uma região específica do que todo o país, indique o nome desta região no formulário.
- **Não use IA nem buscadores**: Todas as respostas devem vir do seu conhecimento e experiência pessoal. Não é permitido consultar ChatGPT, Google, Bing ou outros serviços similares.

### Preenchendo o formulário passo a passo

Como você pode ver na imagem de exemplo, o formulário de anotação contém vários campos que você deve preencher:

1. **Pergunta**: Na parte esquerda você verá a pergunta cultural que deve responder. No exemplo, a pergunta é "Nos Jogos Olímpicos de Inverno, qual é o evento mais popular para assistir na Bolívia?".
2. **Adaptação da pergunta:** Se você entende a pergunta mas ela está formulada de uma maneira que não soa totalmente natural em seu país, reescreva a pergunta aqui de maneira correta. Use o menor número de mudanças possível (por exemplo, trocar uma palavra por um sinônimo).
3. **Resposta 1 (campo obrigatório)**: Aqui você deve inserir sua resposta principal. Lembre-se de responder de maneira breve e específica.
4. **Resposta 2 e Resposta 3 (campos opcionais)**: Se houver várias respostas válidas para a pergunta em seu contexto cultural, você pode incluí-las nestes campos. Por exemplo, se perguntarem sobre comidas típicas, você poderia incluir diferentes pratos em cada campo.
5. **Região específica (campo opcional)**: Se sua resposta é mais representativa de uma região específica do seu país do que de todo o território, escreva o nome dessa região neste campo.

**O que fazer se...**

1. **Você não sabe a resposta**: Quando você entende a pergunta e ela é relevante para sua cultura mas desconhece a resposta, passe para a próxima usando as setas no canto superior direito da pergunta.
2. **Não há resposta:** No final do formulário você encontrará opções específicas para indicar por que não pode responder. Você deve selecionar uma destas opções:
    - **Não há uma resposta específica para esta pergunta**: Quando em sua cultura não existe uma resposta clara ou consensual. Exceto:
        - Se a resposta depende da região, responda e utilize o campo "Região específica".
        - Se a resposta depende de outra característica que você possa especificar, utilize as três opções disponíveis e especifique a condição. Por exemplo, Resposta 1: "No Norte, ...", Resposta 2: "No Sul, ..." ou Resposta 1: "Menores de 35 anos, ...", Resposta 2: "Maiores de 35 anos, ..."
    - **Esta pergunta não se aplica à minha cultura**: Quando a pergunta faz referência a algo que não faz parte do seu contexto cultural.
    - Lembre-se que se você selecionar alguma dessas opções, deve escrever "Não há resposta" no campo "Resposta 1".

**Botões de ação**:
- Descartar: Para descartar sua resposta atual e começar de novo.
- Salvar como rascunho: Para salvar sua resposta como rascunho e continuá-la mais tarde.
- Enviar: Para enviar sua resposta e continuar com a próxima pergunta.
- Na parte superior da tela, você verá um contador que indica em qual pergunta você está (por exemplo, "1 of 500"), o que permitirá que você acompanhe seu progresso.

<center><a href="https://somosnlp-blend-es.hf.space/" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Participe agora!</a></center>

<center style="margin-top:40px;"><a href="https://somosnlp.org/pt/hackathon/retos" target="_blank" style="background-color:gray; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Voltar aos desafios</a></center>
