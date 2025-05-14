---
title: "Desafio #HackathonSomosNLP 2025: Exames INCLUDE"
description: Como participar neste desafio e ajudar a melhorar o conhecimento cultural dos modelos de linguagem
lang: pt
cover: https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg
---

Procure exames de múltipla escolha do seu país para avaliar o conhecimento dos LLMs. Priorize exames em idiomas diferentes do espanhol e/ou focados em temas culturais (por exemplo, história, literatura). Usaremos essas perguntas e respostas para estender o benchmark aberto INCLUDE.

*9 de abril - 31 de maio (PRORROGADO) | máx 1 ponto*

<center><a href="https://docs.google.com/spreadsheets/d/1QLPQ7gah9yzG3-1BPIw5Jp994Rz8L_yZT8obgWH8S2Y" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Participe agora!</a></center>

🌎 Você pode contribuir com exames de todos os países, independentemente do seu local de origem ou residência. Confira a aba "Prioridad países" na planilha.

✨ Incentivos (os números se referem a perguntas com suas respectivas respostas):
- Por equipe:
    - 100 perguntas no total = 0,5 pontos
    - 200 perguntas no total = 1 ponto
- Por pessoa:
    - Cada 100 perguntas = 50 USD em créditos GPU ou livros (à sua escolha)
    - 300 por pessoa = convite para o Slack do projeto global e coautoria no paper do INCLUDE v2 liderado pela EPFL
- ATENÇÃO: Os exames devem cumprir os requisitos!

Recursos:
- [Workshop de Alfonso Amayuelas](https://www.youtube.com/watch?v=Jk70bSw4tTo&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6&index=1)
- Repositório GitHub com o código do workshop: [amayuelas/corpus-automation](https://github.com/amayuelas/corpus-automation)
- Canal do Discord [#examenes-include](https://discord.com/channels/938134488670675055/1326890438782750852)

---

## Protocolo de coleta de exames multilíngues

A seguir, apresentamos o protocolo para participar do projeto INCLUDE focado na coleta de exames multilíngues.

### 1. Buscar exames

Verifique se o exame atende aos seguintes requisitos:
- **Não é proprietário.** Se a licença restringe o uso comercial mas permite sua redistribuição para fins de pesquisa, então podemos usar este exame. Se a licença for desconhecida, inclua o exame.
- **É um exame com formato de perguntas de múltipla escolha** e tem 4 opções por pergunta.
- **Contém as respostas** e há apenas uma resposta correta por pergunta.
- O tema do exame deve estar relacionado à **cultura** de um país (por exemplo, história, literatura) ou ser informação regional (por exemplo, carteira de motorista). Não são válidos os exames de ciências exatas ou naturais (por exemplo, matemática, física).
- Priorize buscar exames em **línguas** originárias da Brasil 

Ideias para encontrar exames:
- Exames de idiomas
- Exames de nacionalização
- Carteiras de motorista
- Exames de acesso à universidade ou da universidade
- Exames do ensino fundamental ou médio
- Exames habilitantes de profissões (direito, medicina, psicologia, etc.)
- Perguntas de programas estilo "Quem quer ser um milionário?"
- Perguntas de jogos tipo Trivial Pursuit
- Testes de autoavaliação em livros didáticos

Lembre-se: não precisa ser um exame digitalizado, você também pode digitalizar livros ou tirar fotos de documentos.

### 2. Adicionar exames à planilha

Quando encontrar um exame, guarde sua URL/nome/artigo/documentação de origem e adicione-o à [planilha](https://docs.google.com/spreadsheets/d/1QLPQ7gah9yzG3-1BPIw5Jp994Rz8L_yZT8obgWH8S2Y/edit?usp=sharing).

Inclua o seguinte:
- Seu nome
- Seu nome no Discord
- Nome do exame (o mais detalhado possível)
- Língua e país de origem do exame
- Domínio do exame (por exemplo, Literatura, Direito, Direção, etc.)
- Nível do exame
- Número de perguntas
- Origem do exame (URL se disponível online, nome do livro ou URL do documento PDF no seu Drive, etc.)
- Formato original (por exemplo, PDF, página web, livro didático, etc.)

### 3. Processar os exames

Depois de encontrar um exame:

- Extraia as perguntas e respostas e crie um arquivo final em formato **JSON** (exemplo a seguir).
    - Recomendamos o [workshop de Alfonso Amayuelas](https://www.youtube.com/watch?v=Jk70bSw4tTo&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6&index=1)
    - Repositório GitHub com o código do workshop: [amayuelas/corpus-automation](https://github.com/amayuelas/corpus-automation)
- Faça upload do arquivo final para um dataset **PRIVADO** em [huggingface.co/somosnlp-hackathon-2025](https://huggingface.co/somosnlp-hackathon-2025) com o nome do exame. Se você não faz parte da organização, junte-se com este [convite](https://huggingface.co/somosnlp-hackathon-2025).
- No canal do Discord [#examenes-include](https://discord.com/channels/938134488670675055/1326890438782750852), mencione @mariagrandury e compartilhe o link para o dataset criado.
- Verificaremos o conteúdo e informaremos se alguma alteração for necessária.

Exemplo JSON no formato esperado:

```json
{
  "language": "pt",
  "country": "Brasil",
  "exam_name": "Exame Final de História do Ensino Médio 2017",
  "source": "https://url-do-exame",
  "license": "CC-BY-SA",
  "level": "Acesso à Universidade",
  "category_en": "History",
  "category_original_lang": "História",
  "original_question_num": 1,
  "question": "Em qual dos seguintes anos começou a Proclamação da República?",
  "options": [ "1889", "1890", "1891", "1892" ],
  "answer": 0
}
```

## Equipe

Muito obrigado a:
- EPFL: Prêmios e organização da equipe global
- A equipe: María Grandury e Angelika Romanou 

<center style="margin-top:40px;"><a href="https://docs.google.com/spreadsheets/d/1QLPQ7gah9yzG3-1BPIw5Jp994Rz8L_yZT8obgWH8S2Y" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Participe agora!</a></center>

<center style="margin-top:40px;"><a href="https://somosnlp.org/pt/hackathon/retos" target="_blank" style="background-color:gray; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Voltar aos desafios</a></center>
