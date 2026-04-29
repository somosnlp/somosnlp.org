---
title: "Desafio #HackathonSomosNLP 2026: Preferências"
description: Como participar neste desafio e ajudar a alinhar modelos de linguagem com sua cultura
lang: pt
cover: /images/eventos/260511_hackathon_eventbrite.png
---

Projete prompts que avaliem a adequação cultural com seu país e escolha a melhor resposta em uma LLM Arena. Os prompts e as respostas serão coletados e compartilhados com todas as equipes participantes como dataset de preferências v0 para a fase de alinhamento. Para este desafio, você terá acesso a uma LLM Arena com 5 modelos grandes ou proprietários.

<!-- *14 de abril - 21 de maio (PRORROGADO) | máx 3 pontos* -->

1. **Leia o guia a seguir para aprender a projetar prompts de qualidade.**

<div style="display: flex; justify-content: center; gap: 20px;">
  <a href="https://forms.gle/itbDvVxD2iG5nzsC6" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">2. Verifique que você entendeu o guia</a>
  <a href="https://huggingface.co/spaces/somosnlp/validacion-preferencias" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">3. Valide prompts de outras equipes</a>
  <a href="https://fastchat-webui-908374066028.us-central1.run.app/gradio/" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">4. Envie seus prompts à Arena</a>
</div>

🌎 Gere **apenas** prompts relacionados com o país ou países com os quais você tenha um vínculo forte o suficiente para conhecer a cultura local.

<!-- ✨ Incentivos (os números se referem a prompts respondidos validados):
- 100 por equipe = requisito para acessar os 500 USD da API da Cohere para o desafio principal
- Cada 50 prompts por equipe = 0,5 pontos (máx 2 pontos, o outro ponto é obtido de avaliar como vocês utilizarem a API da Cohere para melhorar o dataset)
- Vocês terão acesso aos dados gerados por todas as equipes para tomá-los como base para seu alinhamento, **uma maior qualidade dos dados implica uma maior qualidade do seu projeto**

🙌 Muito obrigado a:
- CENIA: Créditos API para os LLMs da Arena
- A equipe: Gonzalo Fuentes, Diana Galván, Eugenio Herrera, Sebastián Cifuentes, Clemente, María Grandury, Luis Vasquez e Valle Ruiz

Recursos:
- Definições, exemplos de prompts e datasets de preferências a seguir
- [Palestra sobre Red Teaming de Luis Vasquez](https://www.youtube.com/watch?v=pGOXE4rrO9M&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6) -->

---

## 🎯 Objetivo

O objetivo deste desafio é criar entre todas as equipes um dataset que permita alinhar LLMs com a cultura dos países da LATAM e da Península Ibérica. Para isso, cada equipe tem que:

1. Projetar prompts seguindo o guia a seguir
2. Enviar seus prompts para uma LLM Arena e escolher a melhor resposta
3. Simultaneamente, ir validando os prompts e respostas de outras equipes
4. Publicaremos o conjunto de prompts e respostas
<!-- 
: [somosnlp-hackathon/dataset-preferencias-dpo-v0](https://huggingface.co/datasets/somosnlp-hackathon/dataset-preferencias-dpo-v0)
5. Durante as 2 semanas seguintes cada equipe terá acesso a 500 USD em créditos da Cohere para processar, filtrar e estender o dataset inicial v0 (v0 = versão 0 = versão inicial) e a GPUs L40S da Hugging Face para alinhar um LLM de 7B de parâmetros.

Para acessar os créditos API e GPUs:
- A equipe deve contribuir no total com 100 prompts **de qualidade** ao dataset de preferências e 200 respostas ao dataset de avaliação ([BLEND](https://somosnlp.org/pt/hackathon/retos/blend))
- A(s) pessoa(s) que envie(m) os prompts à Arena tem que ter completado o [teste de compreensão do guia](https://forms.gle/itbDvVxD2iG5nzsC6)
- É necessário [registrar a equipe](https://forms.gle/mLKEURUXGiNhq31T9)
-->

🚨 **Leia com atenção os guias a seguir para mais detalhes de cada passo.** Leva menos de 10 minutos e é imprescindível para assegurar a qualidade e homogeneidade dos dados, muito importante para continuar seu projeto. Não serão considerados prompts e respostas de equipes que não tenham seguido as instruções.

## 🤗 Como criar equipes

<details>
<summary>Como criar equipes</summary>

- Podem ser homogêneas (todas as pessoas são do mesmo país) ou heterogêneas (diferentes países de origem)
    - Equipes homogêneas
        - É mais provável que os prompts sejam mais ou menos padrão, já que estarão representando uma mesma cultura. As respostas, no entanto, pode haver mais de uma que se considere culturalmente adequada dependendo da região.
        - Vocês podem reutilizar prompts e respondê-los levando em conta a perspectiva de diferentes regiões.
    - Equipes heterogêneas
        - É provável que haja variedade tanto nos prompts quanto nas respostas que se consideram culturalmente adequadas.
        - Vocês podem reutilizar prompts e respondê-los levando em conta a perspectiva de diferentes países.
- Não é necessário que os prompts que você enviar à LLM Arena estejam relacionados com o objetivo final com o qual você quer alinhar seu LLM.

> 💡 Recomendação
>
> 1. Decidir se desejam trabalhar em uma equipe homogênea ou heterogênea. Recomendamos um meio termo: equipes que incluam 2 ou 3 países.
> 2. Começar a projetar prompts representando diferentes abordagens da cultura dos países representados.
> 3. Decidir o tema do projeto (relacionado com a adequação cultural!) para levá-lo em conta, se quiserem, no design de prompts. Igualmente terão créditos para estender o dataset comum com mais prompts especificamente criados para seu caso de uso.

</details>

## 👀 1. As definições

O principal objetivo do hackathon, e em particular deste desafio, é melhorar a "adequação cultural" dos LLMs, vejamos o que isso significa. Começamos com algumas definições:

<details>
<summary>Cultura</summary>

> *Em seu sentido etnográfico amplo, a cultura é esse todo complexo que inclui o conhecimento, a crença, a arte, a moral, o direito, o costume e qualquer outra capacidade e hábito adquirido pelo homem como membro da sociedade. ([ref](https://books.google.co.uk/books/about/Through_the_Language_Glass.html?id=6NOjIzNZvosC&redir_esc=y))*
> 

> *Somente podemos considerar elementos da cultura tradicional, aqueles que a comunidade conserva e transmite. [...] Esta aceitação, e portanto, a literariedade tradicional, popular ou folclórica, dependerá se o texto se ajusta a uma linguagem determinada, a estruturas específicas, coincide com determinados temas, e se cria a partir de uma estética coletiva. ([ref](https://books.google.co.uk/books/about/M%C3%A9xico_tradicional.html?id=kbowDQAAQBAJ&redir_esc=y))*
> 

</details>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    <img src="/images/infografias/adecuacion_cultural/pt/1.png" alt="Adequação Cultural 1" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/2.png" alt="Adequação Cultural 2" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/3.png" alt="Adequação Cultural 3" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/4.png" alt="Adequação Cultural 4" style="width: 100%;">
</div>

<details>
<summary>Multiculturalidade</summary>

> Existência de várias culturas que convivem em um mesmo espaço físico, geográfico ou social. Abrange todas as diferenças que se enquadram dentro da cultura, seja religiosa, linguística, racial, étnica ou de gênero. ([ref](https://www.significados.com/multiculturalidad/))
> 

> Perante a comunidade se reconhece a diversidade em todos os âmbitos e reconhece o respeito em relação a ela mesma, promovendo direitos para cada uma das culturas incluídas.
> 

</details>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    <img src="/images/infografias/adecuacion_cultural/pt/5.png" alt="Adequação Cultural 5" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/6.png" alt="Adequação Cultural 6" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/7.png" alt="Adequação Cultural 7" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/8.png" alt="Adequação Cultural 8" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/9.png" alt="Adequação Cultural 9" style="width: 100%;">
</div>


<details>
<summary>Adequação cultural</summary>

- Algo é adequado em relação ao propósito do que se faz. No caso da linguagem, a adequação pode ser entendida como uma relação entre o **propósito comunicativo** (intenção ou motivação do remetente ao destinatário ao se comunicar) e os **meios linguísticos** escolhidos.
- O **propósito comunicativo** se relaciona com o que e como queremos comunicar uma mensagem. Os **meios linguísticos** são as palavras e formas gramaticais que utilizamos. Por exemplo, as seguintes duas orações cumprem o propósito de solicitar uma explicação:
    1. *Você poderia me explicar, por favor?*
    2. *Me explique.*
    
    A oração #1 transmite um pedido indireto e cortês por meio do uso condicional simples ("poderia"). A inclusão da frase "por favor" reforça a cortesia. A oração #2 transmite um pedido direto por meio da forma gramatical do imperativo afirmativo do verbo "explicar". É menos cortês que a oração #1.

</details>

<details>
<summary>Como a cultura influencia na escolha dos meios linguísticos?</summary>

- A cultura influencia nas palavras (i.e., escolhas **léxicas**) e nas **formas gramaticais** que utilizamos. Alguns exemplos:

Escolhas léxicas

| Português de Portugal | Português do Brasil |
| --- | --- |
| Casaco | Jaqueta |
| Computador | Computador |
| Hora(s) de ponta | Hora(s) do rush |
| Entrar *em* | Entrar *em* |
| Tenho *vergonha* | Tenho *vergonha* |

Formas gramaticais

| Português de Portugal | Português do Brasil |
| --- | --- |
| Pretérito perfeito composto (e.g., *tem ido*) | Pretérito perfeito simples (e.g., *foi*) |

Diferentes propósitos comunicativos

| Propósito comunicativo | Meio linguístico | Exemplo |
| --- | --- | --- |
| Carinho | Forma gramatical: Diminutivo | *Como você está, Edgarzinho?* |
| Minimizar | Forma gramatical: Diminutivo | *Naquela casinha.* |
| Afirmação | Escolha léxica: Bom | *Ah, bom;* *Bom... tá bem* |
| Reorientação | Escolha léxica: Bom | *Bom... como eu estava dizendo* |
| Correção | Escolha léxica: Bom | *Bom, nós dizemos assim, né?* |

</details>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    <img src="/images/infografias/adecuacion_cultural/pt/10.png" alt="Adequação Cultural 10" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/11.png" alt="Adequação Cultural 11" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/12.png" alt="Adequação Cultural 12" style="width: 100%;">
</div>

<details>
<summary>Como a cultura afeta a capacidade de um LLM de entender uma linguagem?</summary>

- Na comunicação: Os propósitos comunicativos são diretamente afetados pelas palavras e formas gramaticais usadas. Quanto mais palavras de um país específico uma oração tiver (por exemplo, do Brasil), mais difícil pode ser entendê-la para alguém (ou algo: um LLM) que não esteja familiarizado com essa cultura.
- Na percepção do mundo: Códigos morais (i.e., o que é bom, o que é mau), atividades comuns (por exemplo, ir a uma luta livre ou ir a uma tourada), etc.

</details>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    <img src="/images/infografias/adecuacion_cultural/pt/13.png" alt="Adequação Cultural 13" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/14.png" alt="Adequação Cultural 14" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/15.png" alt="Adequação Cultural 15" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/16.png" alt="Adequação Cultural 16" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/17.png" alt="Adequação Cultural 17" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/18.png" alt="Adequação Cultural 18" style="width: 100%;">
</div>

## 🎨 2. Como projetar os prompts

### 2.1. Características gerais

Os prompts devem ser:

- **Não triviais**: evitar perguntas factuais simples (por exemplo, "Qual é a capital do Brasil?").
- **Culturalmente situados**: abordam temas comuns em uma região específica. **Utilize papéis para contextualizar sua pergunta**.
- **Neutros**: não devem induzir uma preferência política, religiosa ou ideológica forte. Estes temas podem ser tratados mas sem incluir opiniões sobre qual é "melhor".

<details>
<summary>💡 O que é um papel?</summary>

É uma função que uma **pessoa** desempenha em um lugar ou em uma situação. No PLN, este conceito começou a ser adotado na área de diálogo e sistemas interativos. De fato, é comum encontrar que se usa o termo "persona" e não "papel", embora façam referência à mesma coisa.

*Por que é um conceito importante nos LLMs?*

A definição de papéis tornou-se crucial para adaptar os LLMs a contextos específicos. De acordo com [Tseng et al., 2024](https://aclanthology.org/2024.findings-emnlp.969/), há dois casos de uso:

1. **Interpretação de papéis**: Os LLM têm a tarefa de desempenhar os papéis atribuídos e agir de acordo com o feedback do ambiente, adaptando-se ao mesmo.
2. **Personalização**: Os LLM têm a tarefa de gerenciar as personalidades dos usuários (por exemplo, antecedentes, como seu país de origem) para satisfazer necessidades individualizadas e adaptar-se a cada usuário.

Um exemplo do caso #1 é se queremos simular a interação entre pessoas de Portugal. A pessoa que projeta o prompt só deve especificar as características do papel; não toma parte na interação (i.e, não há interação humana).

No caso #2, pelo contrário, pode haver interação humana. Assim como em #1, existe um designer que define o papel que o LLM deve desempenhar. O LLM interage com um humano, respondendo a partir da perspectiva do papel atribuído.

*Como definir um papel na LLM Arena?*

Inclua-o no "System prompt". Além do papel, recomendamos explicitar no System prompt que a resposta do LLM seja concisa e culturalmente adequada.

</details>

### 2.2. Exemplos de prompt (não exaustivos)

💡 Os prompts que se mostram a seguir são apenas um guia

- Em relação aos papéis: Cada equipe pode fazer sua própria definição! Pode ser algo simples (por exemplo, só especificar o país de origem) ou algo mais elaborado (i.e., incluir gênero, idade, etc)
- Em relação às perguntas: Pegar perguntas de um dataset ou uma pesquisa é apenas uma opção. Vocês também podem redigir suas próprias perguntas!


#### 1. **Definir um papel, mostrar uma situação com múltiplas reações possíveis** (como em [MultiTP](https://openreview.net/pdf?id=vrHErHkCNo))
    
<details>
<summary>Por exemplo...</summary>

Papel: Pessoa do Brasil

Situação: Uso de espaços exclusivos

```python
Imagine que você está no transporte público e observa que alguém 
se senta e/ou coloca suas coisas em um dos assentos reservados 
para gestantes, idosos e pessoas com deficiência.

Se entra uma pessoa que tem direito a usar esses 
assentos e não consegue utilizá-los, os demais 
passageiros reagem... 
```

Resposta 1 (seguindo o papel pré-definido)

```python
Com agressividade, exigindo que a pessoa que está fazendo mau uso
dos assentos se retire.
```

Resposta 2

```python
Com indiferença. Ninguém diz nada. 
```

</details>

#### 2. **Definir um papel e apresentar uma pergunta aberta/subjetiva** (semelhante ao que fez [Dolly](https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm))

<details>
<summary>Por exemplo...</summary>

Pergunta: gerada por alguém do Brasil

Papel: país de origem

```python
System prompt: Você é um assistente de IA. Responda como se fosse 
uma pessoa nativa de {pais_de_origem}.

Pergunta: É melhor ir de carro ou de metrô ao centro de São Paulo?

Resposta (exemplo):
                    O melhor é pegar o metrô. É mais rápido e mais seguro,
                    já que é difícil encontrar lugar para estacionar.
                    Há vários estacionamentos públicos, mas não são muito
                    seguros.
```

ou

```python
Pergunta: Quero sair com meus amigos no fim de semana em São Paulo.
                    O que podemos fazer para nos divertir?
                    Me dê cinco ideias.
                    
Resposta (exemplo):
Se você quer passar um fim de semana divertido com seus amigos, pode:
1. Andar de bicicleta no domingo na Avenida Paulista
2. Ir tomar um café em Pinheiros
3. Visitar o Parque Ibirapuera
4. Ir a um karaokê na Liberdade
5. Fazer um passeio de barco na Represa de Guarapiranga
```

</details>

#### 3. **Definir um papel, um comportamento e apresentar uma pergunta de múltipla escolha** (como neste [paper](https://arxiv.org/pdf/2402.13231))

<details>
<summary>💡 Por exemplo...</summary>

- Papel (características): Gênero, país de origem, educação, idade, classe social
- Pergunta: Pergunta aberta
- Conjunto de respostas: Há duas possibilidades:
    1. Todas as opções são culturalmente adequadas, o modelo teria que escolher a mais adequada para o papel e explicar por quê
    2. Apenas 1 das opções é culturalmente adequada
- Comportamento (a resposta do LLM): Deve ser congruente com o papel

```python
Imagine que você é uma pessoa {gênero} do {país}.
Você tem {idade} anos e completou o nível educativo {educação}.
Você se autodefine como parte de uma classe social {classe_social}. 

Responda à seguinte pergunta a partir desta perspectiva.
Considere que outras pessoas vão ler o que você escolher; seu objetivo é
convencê-las de que a escolha foi feita a partir da perspectiva da
pessoa descrita acima.

Selecione apenas uma opção e explique sua escolha.

Pergunta: {pergunta}
Opções: {conjunto de respostas}
```

</details>


#### 4. **Diálogos** (como fez [OpenAssistant](https://arxiv.org/pdf/2304.07327))

<details>
<summary>💡 Por exemplo...</summary>

Para gerar um diálogo, simplesmente continue a conversa na LLM Arena por mais algumas interações.

```python
# Prompt
Me recomende lugares para sair com meus amigos no fim de semana em São Paulo

# Resposta (assistant)
Esta recomendação depende muito do tipo de atividades que você e
seus amigos gostam de fazer. Preciso de mais informações, como se
preferem espaços abertos ou espaços fechados.

# Resposta (prompter)
Bom ponto. Preferimos espaços abertos.

# Resposta (assistant)
Muito bem! Nesse caso, vocês poderiam ir ao Parque Ibirapuera. Lá vocês 
vão encontrar opções para comer e se divertir ao ar livre. 
```

</details>

### 2.3. Cria o teu dataset de prompts

- Recomendamos guardar seus prompts em um arquivo CSV
- Colunas:
    - necessárias: `prompt` e `pais`
    - opcional: adicione as colunas que precisar, por exemplo se você criou um template com diferentes características sociais (e.g. `idade`) ou regiões, `origem` se as perguntas vêm de um dataset existente, etc.
- Você terá que criar um dataset de prompts na org de Hugging Face do hackathon: https://huggingface.co/somosnlp-hackathon (se você ainda não se uniu, utilize este [convite](https://huggingface.co/organizations/somosnlp-hackathon/share/BMALwncoPyZLRdPuzwugnsDzXHsbLnjjGD))

### 2.4. Recursos

<details>
<summary>Datasets relacionados (vocês podem pegar as categorias para as perguntas)</summary>

- [BLEnD](https://arxiv.org/pdf/2406.09948): comida, esportes, família, educação, dias festivos/celebrações/lazer, vida profissional
- [CoScript](https://aclanthology.org/2023.acl-long.236.pdf): 19 categorias derivadas do wikiHow (Fig 8)
- [CVQA](https://arxiv.org/pdf/2406.05967): 10 categorias (Table 1)
- [FrameNet](https://framenet.icsi.berkeley.edu/frameIndex): Base de dados extensa, vários frames (i.e., [marcos semânticos](https://www.aieti.eu/enti/frame_semantics_SPA/entrada.html))
    - Exemplo: Ver os "lexical units" (lá embaixo) no frame "personal relationships"
- [HellaSwag](https://huggingface.co/datasets/Rowan/hellaswag): Diversas atividades cotidianas tomadas do ActivityNet e wikiHow
    - Ver `activity_label` no dataset
- [World Values Survey (WVS)](https://www.worldvaluessurvey.org/WVSContents.jsp): 14 subseções
    - Listadas sob a seção WVS wave 8 → Questionnaire and research topics

</details>

<details>
<summary>Ideias de categorias para perguntas abertas</summary>

- Normas culturais
    - *Como você responderia educadamente a um desconhecido que furou a fila num banco no Brasil?*
    - *Como você se dirige a um professor universitário em Portugal?*
- Provérbios e expressões
    - *O que significa o provérbio {provérbio} em {país}? Explique o significado e inclua um exemplo.*
- Contos e canções
    - *Qual é a moral do conto {conto} em {país}?*

</details>

<details>
<summary>Exemplos de prompts NÃO válidos</summary>

- Muito gerais ou universais: *"Explique a fotossíntese."*
- Demasiado subjetivos ou sem referencial cultural: *"Qual é o melhor valor humano?"*
- Perguntas conflituosas sem propósito contextual: *"Quem foi pior: Salazar ou Vargas?"*

</details>

## ✅ 3. Como escolher a melhor resposta na LLM Arena

- Uma vez que você projete os prompts, utilize a LLM Arena para gerar respostas com LLMs. Não é necessário que você guarde as respostas, nós as guardamos automaticamente e as liberaremos para todas as equipes no dia 21 de abril.
- Leia com atenção as duas respostas geradas pelo LLM. Depois, escolha a opção que considerar **mais adequada** cultural e comunicativamente
- Para votar, leve em conta:
    - ✅ **Conhecimento cultural correto,** a informação objetiva tem que estar correta
    - ✅ **Adequação cultural** ao país e papel definidos
    - ✅ **Uso correto do português local** (formas locais, regionalismos, expressões idiomáticas, etc.), a resposta gerada deveria utilizar a mesma variedade do português que a pergunta
        - Nota: Não avalie por gramática perfeita ou estilo "neutro", mas sim pelo que soa natural e correto para a cultura do prompt.
- Selecione:
    - **Resposta A / B**: Se uma é claramente mais adequada que a outra.
    - **Ambas boas**: Se ambas são corretas, naturais e culturalmente adequadas.
    - **Ambas ruins**: Se ambas têm erros graves de tom, conteúdo ou adequação cultural.

## 🔍 4. Validar perguntas e respostas de outras equipes

- Abra o [espaço de validação](https://huggingface.co/spaces/somosnlp/validacion-preferencias) e selecione o país para o qual você possa avaliar a adequação cultural
- No espaço você poderá ver o seguinte:
    - uma pergunta
    - as duas respostas geradas pelos LLMs
    - a resposta escolhida originalmente
- Você terá que anotar:
    1. Se a pergunta lhe parece estar bem projetada levando em conta o guia anterior
    2. Se você também escolheria essa resposta ou mudaria
    3. Opcionalmente, você pode editar e melhorar a resposta gerada escolhida
- Considerações para a validação:
    - Evite vieses pessoais, avalie a partir da perspectiva do papel definido
    - Se o prompt não tem ancoragem cultural ou ambas as respostas não podem ser avaliadas razoavelmente, reporte como inválido
<!-- 
## 🌍 5. Mais desafios

- Na segunda-feira dia 21 publicaremos o conjunto de perguntas e respostas para que vocês possam utilizá-lo para alinhar seus LLMs. Também incluiremos os dados do mini desafio "[Validador de estereótipos](https://somosnlp.org/pt/hackathon/retos/estereotipos)".
- A partir da segunda-feira dia 21, daremos acesso aos créditos da Cohere e às GPUs da Hugging Face às equipes quando atingirem o mínimo de prompts, mencione @mariagrandury no tópico da sua equipe no canal #encuentra-equipo
- Lembre que você também pode participar dos mini desafios para conseguir mais pontos
    - [INCLUDE](https://somosnlp.org/pt/hackathon/retos/include) - Coleta de exames (até 30 de abril, haverá prêmios e paper)
    - [BLEND](https://somosnlp.org/pt/hackathon/retos/blend) - Perguntas de conhecimento cultural (até o final do hackathon, haverá paper)


<div style="display: flex; justify-content: center; gap: 20px;">
  <a href="https://forms.gle/itbDvVxD2iG5nzsC6" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Verifique que você entendeu o guia</a>
  <a href="https://huggingface.co/spaces/somosnlp/validacion-preferencias" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Valide prompts de outras equipes</a>
  <a href="https://fastchat-webui-908374066028.us-central1.run.app/gradio/" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Envie seus prompts à Arena</a>
</div>

<center style="margin-top:40px;"><a href="https://somosnlp.org/pt/hackathon/retos" target="_blank" style="background-color:gray; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Voltar aos desafios</a></center> -->

<div style="display: flex; justify-content: center; gap: 20px;">
  <a href="https://forms.gle/itbDvVxD2iG5nzsC6" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Verifique que você entendeu o guia</a>
  <a href="https://huggingface.co/spaces/somosnlp/validacion-preferencias" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Valide prompts de outras equipes</a>
  <a href="https://fastchat-webui-908374066028.us-central1.run.app/gradio/" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Envie seus prompts à Arena</a>
</div>
