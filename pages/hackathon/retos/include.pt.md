---
title: "Desafio #HackathonSomosNLP 2026: Exames INCLUDE"
description: Como participar deste desafio e ajudar a melhorar o conhecimento cultural dos modelos de linguagem
lang: pt
cover: /images/eventos/260511_hackathon_eventbrite.png
---

Procure exames de múltipla escolha do seu país para avaliar o conhecimento dos LLMs. Priorize exames em línguas diferentes do espanhol e/ou focados em temas culturais (e.g. história, literatura). Vamos usar essas perguntas e respostas para estender o benchmark aberto INCLUDE.

*9 de abril a 31 de maio (PRORROGADO) | máx 1 ponto*

<center><a href="https://docs.google.com/spreadsheets/d/1QLPQ7gah9yzG3-1BPIw5Jp994Rz8L_yZT8obgWH8S2Y" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Participe agora!</a></center>

🌎 Você pode contribuir com exames de qualquer país, independentemente da sua origem ou local de residência. Confira a aba "Prioridad países" da planilha.

✨ Incentivos (os números se referem a perguntas com as respectivas respostas):
* Por equipe:
    * 100 perguntas no total = 0,5 pontos
    * 200 perguntas no total = 1 ponto
    * 200 por equipe = também é requisito para acessar os 500 USD em créditos da API da Cohere para o desafio principal
* Por pessoa:
    * Cada 100 perguntas = 50 USD em créditos GPU ou livros (à sua escolha)
    * 300 por pessoa = convite para o Slack do projeto global e coautoria no paper do INCLUDE v2 liderado pela EPFL
* ATENÇÃO: Os exames precisam cumprir os requisitos!

Recursos:
* [Workshop de Alfonso Amayuelas](https://www.youtube.com/watch?v=Jk70bSw4tTo&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6&index=1)
* Repositório GitHub com o código do workshop: [amayuelas/corpus-automation](https://github.com/amayuelas/corpus-automation)
* Canal do Discord [#examenes-include](https://discord.com/channels/938134488670675055/1326890438782750852)

---

## Protocolo de coleta de exames multilíngues

A seguir apresentamos o protocolo para participar do projeto INCLUDE, focado na coleta de exames multilíngues.

### 1. Procurar exames

Verifique se o exame cumpre os seguintes requisitos:
* **Não é proprietário.** Se a licença restringe o uso comercial mas permite a redistribuição para fins de pesquisa, então podemos usar este exame. Se a licença for desconhecida, inclua o exame mesmo assim.
* **É um exame com formato de múltipla escolha** e tem 4 opções por pergunta.
* **Contém as respostas** e tem apenas uma resposta correta por pergunta.
* O tema do exame precisa estar relacionado com a **cultura** de um país (e.g. história, literatura) ou ser informação regional (e.g. carteira de motorista). Não são válidos os exames de ciências exatas ou naturais (e.g. matemática, física).
* Priorize exames em **línguas** originárias da América Latina ou cooficiais da Espanha.
* Também são válidos os exames em espanhol dos seguintes países:

    | PRIORIDADE            | NÃO*         |
    |-----------------------|--------------|
    | Porto Rico            | Espanha      |
    | República Dominicana  | Chile        |
    | Costa Rica            |              |
    | Panamá                |              |
    | Nicarágua             |              |
    | Guatemala             |              |
    | El Salvador           |              |
    | Guiné Equatorial      |              |
    | Honduras              |              |
    | Cuba                  |              |
    | Bolívia               |              |
    | Colômbia              |              |
    | Paraguai              |              |
    | Uruguai               |              |
    | Venezuela             |              |

*A não ser que se trate de um exame com componente cultural ou regional muito relevante. Nesse caso, pergunte primeiro no [Discord](https://discord.com/channels/938134488670675055/1326890438782750852). De qualquer forma, recomendamos procurar exames dos países prioritários.

Ideias para encontrar exames:
* Exames de idiomas
* Exames de naturalização
* Provas de carteira de motorista
* Exames de acesso à universidade ou da universidade
* Exames do ensino fundamental ou médio
* Exames habilitantes de profissões (direito, medicina, psicologia, etc.)
* Perguntas de programas estilo "Quem Quer Ser Milionário?"
* Perguntas de jogos tipo Trivial Pursuit
* Testes de autoavaliação em livros didáticos

Lembre que não precisa ser um exame digitalizado. Você também pode escanear livros ou tirar fotos de documentos.

### 2. Adicionar exames à planilha

Quando encontrar um exame, salve a URL/nome/artigo/documentação de origem e adicione na [planilha](https://docs.google.com/spreadsheets/d/1QLPQ7gah9yzG3-1BPIw5Jp994Rz8L_yZT8obgWH8S2Y/edit?usp=sharing).

Inclua o seguinte:
* Seu nome
* Seu nome no Discord
* Nome do exame (o mais detalhado possível)
* Língua e país de origem do exame
* Domínio do exame (e.g. Literatura, Direito, Direção, etc.)
* Nível do exame
* Número de perguntas
* Origem do exame (URL se estiver disponível online, nome do livro ou URL para o PDF no seu Drive, etc.)
* Formato original (e.g. PDF, página web, livro didático, etc.)

### 3. Processar os exames

Depois de encontrar um exame:

* Extraia as perguntas e respostas e crie um arquivo final em formato **JSON** (exemplo a seguir).
    * Recomendamos o [workshop de Alfonso Amayuelas](https://www.youtube.com/watch?v=Jk70bSw4tTo&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6&index=1)
    * Repositório GitHub com o código do workshop: [amayuelas/corpus-automation](https://github.com/amayuelas/corpus-automation)
* Faça upload do arquivo final para um dataset **PRIVADO** em [huggingface.co/somosnlp-hackathon](https://huggingface.co/somosnlp-hackathon) com o nome do exame. Se ainda não faz parte da organização, entre com este [convite](https://huggingface.co/somosnlp-hackathon).
* No canal do Discord [#examenes-include](https://discord.com/channels/938134488670675055/1326890438782750852), mencione @mariagrandury e compartilhe o link para o dataset criado.
* Vamos verificar o conteúdo e avisar se for necessária alguma alteração.

Exemplo JSON no formato esperado:

```json
{
  "language": "pt",
  "country": "Brasil",
  "exam_name": "Exame Final de História do Ensino Médio 2017",
  "source": "https://url-do-exame",
  "license": "CC-BY-SA",
  "level": "Acesso à universidade",
  "category_en": "History",
  "category_original_lang": "História",
  "original_question_num": 1,
  "question": "Em qual dos seguintes anos começou a Proclamação da República?",
  "options": [ "1889", "1890", "1891", "1892" ],
  "answer": 0
}
```

## Equipe

Muito obrigada a:
* EPFL: prêmios e organização da equipe global
* A equipe: María Grandury e Angelika Romanou

<center style="margin-top:40px;"><a href="https://docs.google.com/spreadsheets/d/1QLPQ7gah9yzG3-1BPIw5Jp994Rz8L_yZT8obgWH8S2Y" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Participe agora!</a></center>

<center style="margin-top:40px;"><a href="https://somosnlp.org/pt/hackathon/retos" target="_blank" style="background-color:gray; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Voltar aos desafios</a></center>
