---
title: "Desafio #HackathonSomosNLP 2026: Preferências"
description: Como participar neste desafio e ajudar a alinhar modelos de linguagem com a tua cultura
lang: pt
cover: /images/eventos/260511_hackathon_eventbrite.png
---

Desenha prompts que avaliem a adequação cultural com o teu país e escolhe a melhor resposta numa LLM Arena. Os prompts e as respostas serão recolhidos e partilhados com todas as equipas participantes como dataset de preferências v0 para a fase de alinhamento. Para este desafio terás acesso a uma LLM Arena com 5 modelos de grande dimensão ou proprietários.

<!-- *14 de abril - 21 de maio (PRORROGADO) | máx 3 pontos* -->

1. **Lê o guia abaixo para aprender a desenhar prompts de qualidade.**

<div style="display: flex; justify-content: center; gap: 20px;">
  <a href="https://forms.gle/itbDvVxD2iG5nzsC6" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">2. Verifica que entendeste o guia</a>
  <a href="https://huggingface.co/spaces/somosnlp/validacion-preferencias" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">3. Valida prompts de outras equipas</a>
  <a href="https://fastchat-webui-908374066028.us-central1.run.app/gradio/" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">4. Envia os teus prompts à Arena</a>
</div>

🌎 Gera **apenas** prompts relacionados com o país ou países com os quais tenhas um vínculo forte o suficiente para conheceres a cultura local.

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

O objetivo deste desafio é criar, entre todas as equipas, um dataset que permita alinhar LLMs com a cultura dos países da América Latina e da Península Ibérica. Para tal, cada equipa tem de:

1. Desenhar prompts seguindo o guia a seguir
2. Enviar os seus prompts a uma LLM Arena e escolher a melhor resposta
3. Em simultâneo, ir validando os prompts e respostas de outras equipas
4. Vamos publicar o conjunto de prompts e respostas
<!-- 
: [somosnlp-hackathon/dataset-preferencias-dpo-v0](https://huggingface.co/datasets/somosnlp-hackathon/dataset-preferencias-dpo-v0)
5. Durante as 2 semanas seguintes cada equipe terá acesso a 500 USD em créditos da Cohere para processar, filtrar e estender o dataset inicial v0 (v0 = versão 0 = versão inicial) e a GPUs L40S da Hugging Face para alinhar um LLM de 7B de parâmetros.

Para acessar os créditos API e GPUs:
- A equipe deve contribuir no total com 100 prompts **de qualidade** ao dataset de preferências e 200 respostas ao dataset de avaliação ([BLEND](https://somosnlp.org/pt/hackathon/retos/blend))
- A(s) pessoa(s) que envie(m) os prompts à Arena tem que ter completado o [teste de compreensão do guia](https://forms.gle/itbDvVxD2iG5nzsC6)
- É necessário [registrar a equipe](https://forms.gle/mLKEURUXGiNhq31T9)
-->

🚨 **Lê com atenção os guias abaixo para saberes mais detalhes de cada passo.** Leva menos de 10 minutos e é imprescindível para garantir a qualidade e homogeneidade dos dados, muito importante para dar continuidade ao vosso projeto. Não serão considerados prompts e respostas de equipas que não tenham seguido as instruções.

## 🤗 Como criar equipas

<details>
<summary>Como criar equipas</summary>

- Podem ser homogéneas (todas as pessoas são do mesmo país) ou heterogéneas (de países de origem diferentes)
    - Equipas homogéneas
        - É mais provável que os prompts sejam mais ou menos padrão, já que vão estar a representar uma mesma cultura. Quanto às respostas, pode haver mais do que uma que se considere culturalmente adequada, consoante a região.
        - Podem reutilizar prompts e respondê-los tendo em conta a perspetiva de diferentes regiões.
    - Equipas heterogéneas
        - É provável que haja variedade tanto nos prompts como nas respostas consideradas culturalmente adequadas.
        - Podem reutilizar prompts e respondê-los tendo em conta a perspetiva de diferentes países.
- Não é necessário que os prompts que enviarem à LLM Arena estejam relacionados com o objetivo final com o qual querem alinhar o vosso LLM.

> 💡 Recomendação
>
> 1. Decidir se querem trabalhar numa equipa homogénea ou heterogénea. Recomendamos um meio-termo: equipas que incluam 2 ou 3 países.
> 2. Começar a desenhar prompts representando diferentes abordagens à cultura dos países representados.
> 3. Decidir o tema do projeto (relacionado com a adequação cultural!) para o ter em conta, se quiserem, no design de prompts. Vão na mesma ter créditos para estender o dataset comum com mais prompts especificamente criados para o vosso caso de uso.

</details>

## 👀 1. As definições

O principal objetivo do hackathon, e em particular deste desafio, é melhorar a "adequação cultural" dos LLMs — vejamos o que isso significa. Começamos com algumas definições:

<details>
<summary>Cultura</summary>

> *No seu sentido etnográfico amplo, a cultura é esse todo complexo que inclui o conhecimento, a crença, a arte, a moral, o direito, o costume e qualquer outra capacidade e hábito adquirido pelo homem como membro da sociedade. ([ref](https://books.google.co.uk/books/about/Through_the_Language_Glass.html?id=6NOjIzNZvosC&redir_esc=y))*
> 

> *Apenas podemos considerar elementos da cultura tradicional aqueles que a comunidade conserva e transmite. [...] Esta aceitação, e portanto a literariedade tradicional, popular ou folclórica, dependerá de se o texto se ajusta a uma linguagem determinada, a estruturas específicas, se coincide com determinados temas e se é criado a partir de uma estética coletiva. ([ref](https://books.google.co.uk/books/about/M%C3%A9xico_tradicional.html?id=kbowDQAAQBAJ&redir_esc=y))*
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

> Existência de várias culturas que convivem num mesmo espaço físico, geográfico ou social. Abrange todas as diferenças que se enquadram dentro da cultura, sejam religiosas, linguísticas, raciais, étnicas ou de género. ([ref](https://www.significados.com/multiculturalidad/))
> 

> Perante a comunidade reconhece-se a diversidade em todos os âmbitos e o respeito por ela mesma, promovendo direitos para cada uma das culturas incluídas.
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

- Algo é adequado em relação ao propósito do que se faz. No caso da linguagem, a adequação pode ser entendida como uma relação entre o **propósito comunicativo** (intenção ou motivação do remetente em relação ao destinatário ao comunicar) e os **meios linguísticos** escolhidos.
- O **propósito comunicativo** relaciona-se com o que e como queremos comunicar uma mensagem. Os **meios linguísticos** são as palavras e formas gramaticais que utilizamos. Por exemplo, as duas frases seguintes cumprem o propósito de pedir uma explicação:
    1. *Podias explicar-me, por favor?*
    2. *Explica-me.*
    
    A frase #1 transmite um pedido indireto e cortês por meio do uso do imperfeito do indicativo ("podias"). A inclusão da expressão "por favor" reforça a cortesia. A frase #2 transmite um pedido direto através do imperativo afirmativo do verbo "explicar". É menos cortês do que a frase #1.

</details>

<details>
<summary>Como é que a cultura influencia a escolha dos meios linguísticos?</summary>

- A cultura influencia as palavras (i.e. escolhas **léxicas**) e as **formas gramaticais** que utilizamos. Alguns exemplos:

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
| Carinho | Forma gramatical: Diminutivo | *Como estás, Edgarzinho?* |
| Minimizar | Forma gramatical: Diminutivo | *Naquela casinha.* |
| Afirmação | Escolha léxica: Bom | *Ah, bom;* *Bom... está bem* |
| Reorientação | Escolha léxica: Bom | *Bom... como estava a dizer* |
| Correção | Escolha léxica: Bom | *Bom, nós dizemos assim, não é?* |

</details>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    <img src="/images/infografias/adecuacion_cultural/pt/10.png" alt="Adequação Cultural 10" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/11.png" alt="Adequação Cultural 11" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/12.png" alt="Adequação Cultural 12" style="width: 100%;">
</div>

<details>
<summary>Como é que a cultura afeta a capacidade de um LLM de compreender uma língua?</summary>

- Na comunicação: os propósitos comunicativos são diretamente afetados pelas palavras e formas gramaticais usadas. Quanto mais palavras específicas de um país uma frase tiver (por exemplo, do Brasil), mais difícil pode ser compreendê-la para alguém (ou algo: um LLM) que não esteja familiarizado com essa cultura.
- Na perceção do mundo: códigos morais (i.e. o que é bom, o que é mau), atividades comuns (e.g. ir a uma tourada ou a um arraial), etc.

</details>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    <img src="/images/infografias/adecuacion_cultural/pt/13.png" alt="Adequação Cultural 13" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/14.png" alt="Adequação Cultural 14" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/15.png" alt="Adequação Cultural 15" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/16.png" alt="Adequação Cultural 16" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/17.png" alt="Adequação Cultural 17" style="width: 100%;">
    <img src="/images/infografias/adecuacion_cultural/pt/18.png" alt="Adequação Cultural 18" style="width: 100%;">
</div>

## 🎨 2. Como desenhar os prompts

### 2.1. Características gerais

Os prompts devem ser:

- **Não triviais**: evita perguntas factuais simples (e.g. "Qual é a capital do Brasil?").
- **Culturalmente situados**: abordam temas comuns numa região específica. **Usa papéis para contextualizar a tua pergunta**.
- **Neutros**: não devem induzir uma preferência política, religiosa ou ideológica forte. Estes temas podem ser tratados, mas sem incluir opiniões sobre qual é "melhor".

<details>
<summary>💡 O que é um papel?</summary>

É uma função que uma **pessoa** desempenha num lugar ou numa situação. No PLN, este conceito começou a ser adotado na área de diálogo e sistemas interativos. De facto, é comum encontrar o termo "persona" em vez de "papel", embora se refiram à mesma coisa.

*Porque é que é um conceito importante nos LLMs?*

A definição de papéis tornou-se crucial para adaptar os LLMs a contextos específicos. De acordo com [Tseng et al., 2024](https://aclanthology.org/2024.findings-emnlp.969/), há dois casos de uso:

1. **Interpretação de papéis**: os LLMs têm a tarefa de desempenhar os papéis atribuídos e agir de acordo com o feedback do ambiente, adaptando-se ao mesmo.
2. **Personalização**: os LLMs têm a tarefa de gerir as personalidades dos utilizadores (e.g. antecedentes, como o país de origem) para satisfazer necessidades individualizadas e adaptar-se a cada utilizador.

Um exemplo do caso #1 é querermos simular a interação entre pessoas de Portugal. A pessoa que desenha o prompt só tem de especificar as características do papel; não participa na interação (i.e. não há interação humana).

No caso #2, pelo contrário, pode haver interação humana. Tal como em #1, existe um designer que define o papel que o LLM deve desempenhar. O LLM interage com um humano, respondendo a partir da perspetiva do papel atribuído.

*Como definir um papel na LLM Arena?*

Inclui-o no "System prompt". Além do papel, recomendamos que explicites no System prompt que a resposta do LLM deve ser concisa e culturalmente adequada.

</details>

### 2.2. Exemplos de prompt (não exaustivos)

💡 Os prompts mostrados a seguir são apenas um guia

- Em relação aos papéis: cada equipa pode fazer a sua própria definição! Pode ser algo simples (e.g. só especificar o país de origem) ou algo mais elaborado (i.e. incluir género, idade, etc.)
- Em relação às perguntas: tirar perguntas de um dataset ou de um questionário é apenas uma opção. Também podem redigir as vossas próprias perguntas!


#### 1. **Definir um papel, mostrar uma situação com múltiplas reações possíveis** (como em [MultiTP](https://openreview.net/pdf?id=vrHErHkCNo))
    
<details>
<summary>Por exemplo...</summary>

Papel: Pessoa do Brasil

Situação: Uso de espaços exclusivos

```python
Imagina que estás no transporte público e observas que alguém 
se senta e/ou coloca as suas coisas num dos assentos reservados 
para gestantes, idosos e pessoas com deficiência.

Se entra uma pessoa que tem direito a usar esses 
assentos e não consegue utilizá-los, os restantes 
passageiros reagem... 
```

Resposta 1 (seguindo o papel pré-definido)

```python
Com agressividade, exigindo que a pessoa que está a fazer mau uso
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

- Papel (características): género, país de origem, educação, idade, classe social
- Pergunta: pergunta aberta
- Conjunto de respostas: há duas possibilidades:
    1. Todas as opções são culturalmente adequadas; o modelo teria de escolher a mais adequada ao papel e explicar porquê
    2. Apenas 1 das opções é culturalmente adequada
- Comportamento (a resposta do LLM): deve ser congruente com o papel

```python
Imagina que és uma pessoa {género} do {país}.
Tens {idade} anos e completaste o nível educativo {educação}.
Defines-te como parte de uma classe social {classe_social}. 

Responde à seguinte pergunta a partir desta perspetiva.
Considera que outras pessoas vão ler o que escolheres; o teu objetivo é
convencê-las de que a escolha foi feita a partir da perspetiva da
pessoa descrita acima.

Seleciona apenas uma opção e explica a tua escolha.

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

- Recomendamos guardar os teus prompts num ficheiro CSV
- Colunas:
    - obrigatórias: `prompt` e `pais`
    - opcional: adiciona as colunas que precisares, por exemplo se criaste um template com diferentes características sociais (e.g. `idade`) ou regiões, `origem` se as perguntas vierem de um dataset existente, etc.
- Vais ter de criar um dataset de prompts na organização do Hugging Face do hackathon: https://huggingface.co/somosnlp-hackathon (se ainda não te juntaste, utiliza este [convite](https://huggingface.co/organizations/somosnlp-hackathon/share/BMALwncoPyZLRdPuzwugnsDzXHsbLnjjGD))

### 2.4. Recursos

<details>
<summary>Datasets relacionados (podem usar as categorias para as perguntas)</summary>

- [BLEnD](https://arxiv.org/pdf/2406.09948): comida, desporto, família, educação, feriados/celebrações/lazer, vida profissional
- [CoScript](https://aclanthology.org/2023.acl-long.236.pdf): 19 categorias derivadas do wikiHow (Fig 8)
- [CVQA](https://arxiv.org/pdf/2406.05967): 10 categorias (Table 1)
- [FrameNet](https://framenet.icsi.berkeley.edu/frameIndex): base de dados extensa, vários frames (i.e. [marcos semânticos](https://www.aieti.eu/enti/frame_semantics_SPA/entrada.html))
    - Exemplo: ver os "lexical units" (em baixo) no frame "personal relationships"
- [HellaSwag](https://huggingface.co/datasets/Rowan/hellaswag): diversas atividades quotidianas retiradas do ActivityNet e wikiHow
    - Ver `activity_label` no dataset
- [World Values Survey (WVS)](https://www.worldvaluessurvey.org/WVSContents.jsp): 14 subsecções
    - Listadas na secção WVS wave 8 → Questionnaire and research topics

</details>

<details>
<summary>Ideias de categorias para perguntas abertas</summary>

- Normas culturais
    - *Como responderias educadamente a um desconhecido que furou a fila num banco no Brasil?*
    - *Como te diriges a um professor universitário em Portugal?*
- Provérbios e expressões
    - *O que significa o provérbio {provérbio} em {país}? Explica o significado e inclui um exemplo.*
- Contos e canções
    - *Qual é a moral do conto {conto} em {país}?*

</details>

<details>
<summary>Exemplos de prompts NÃO válidos</summary>

- Muito gerais ou universais: *"Explica a fotossíntese."*
- Demasiado subjetivos ou sem enquadramento cultural: *"Qual é o melhor valor humano?"*
- Perguntas conflituosas sem propósito contextual: *"Quem foi pior: Salazar ou Vargas?"*

</details>

## ✅ 3. Como escolher a melhor resposta na LLM Arena

- Depois de desenhares os prompts, utiliza a LLM Arena para gerar respostas com LLMs. Não precisas de guardar as respostas — guardamo-las automaticamente e disponibilizamo-las a todas as equipas no dia 21 de abril.
- Lê com atenção as duas respostas geradas pelo LLM. Depois, escolhe a opção que considerares **mais adequada** cultural e comunicativamente
- Para votar, tem em conta:
    - ✅ **Conhecimento cultural correto** — a informação objetiva tem de estar correta
    - ✅ **Adequação cultural** ao país e papel definidos
    - ✅ **Uso correto do português local** (formas locais, regionalismos, expressões idiomáticas, etc.) — a resposta gerada deveria usar a mesma variedade do português que a pergunta
        - Nota: não avalies por gramática perfeita ou estilo "neutro", mas sim pelo que soa natural e correto para a cultura do prompt.
- Seleciona:
    - **Resposta A / B**: se uma for claramente mais adequada do que a outra.
    - **Ambas boas**: se ambas forem corretas, naturais e culturalmente adequadas.
    - **Ambas más**: se ambas tiverem erros graves de tom, conteúdo ou adequação cultural.

## 🔍 4. Validar perguntas e respostas de outras equipas

- Abre o [espaço de validação](https://huggingface.co/spaces/somosnlp/validacion-preferencias) e seleciona o país para o qual consigas avaliar a adequação cultural
- No espaço vais poder ver o seguinte:
    - uma pergunta
    - as duas respostas geradas pelos LLMs
    - a resposta originalmente escolhida
- Vais ter de anotar:
    1. Se te parece que a pergunta está bem desenhada tendo em conta o guia anterior
    2. Se também escolherias essa resposta ou se mudarias
    3. Opcionalmente, podes editar e melhorar a resposta gerada que foi escolhida
- Considerações para a validação:
    - Evita vieses pessoais — avalia a partir da perspetiva do papel definido
    - Se o prompt não tem ancoragem cultural ou se nenhuma das respostas pode ser avaliada de forma razoável, marca-o como inválido
<!-- 
## 🌍 5. Mais desafios

- Na segunda-feira dia 21 publicaremos o conjunto de perguntas e respostas para que vocês possam utilizá-lo para alinhar seus LLMs. Também incluiremos os dados do mini desafio "[Validador de estereótipos](https://somosnlp.org/pt/hackathon/retos/estereotipos)".
- A partir da segunda-feira dia 21, daremos acesso aos créditos da Cohere e às GPUs da Hugging Face às equipes quando atingirem o mínimo de prompts, mencione @mariagrandury no tópico da sua equipe no canal #encuentra-equipo
- Lembre que você também pode participar dos mini desafios para conseguir mais pontos
    - [INCLUDE](https://somosnlp.org/pt/hackathon/retos/include) - Coleta de exames (até 30 de abril, haverá prêmios e paper)
    - [BLEND](https://somosnlp.org/pt/hackathon/retos/blend) - Perguntas de conhecimento cultural (até o final do hackathon, haverá paper)


<div style="display: flex; justify-content: center; gap: 20px;">
  <a href="https://forms.gle/itbDvVxD2iG5nzsC6" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Verifica que entendeste o guia</a>
  <a href="https://huggingface.co/spaces/somosnlp/validacion-preferencias" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Valida prompts de outras equipas</a>
  <a href="https://fastchat-webui-908374066028.us-central1.run.app/gradio/" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Envia os teus prompts à Arena</a>
</div>

<center style="margin-top:40px;"><a href="https://somosnlp.org/pt/hackathon/retos" target="_blank" style="background-color:gray; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Voltar aos desafios</a></center> -->

<div style="display: flex; justify-content: center; gap: 20px;">
  <a href="https://forms.gle/itbDvVxD2iG5nzsC6" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Verifica que entendeste o guia</a>
  <a href="https://huggingface.co/spaces/somosnlp/validacion-preferencias" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Valida prompts de outras equipas</a>
  <a href="https://fastchat-webui-908374066028.us-central1.run.app/gradio/" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Envia os teus prompts à Arena</a>
</div>
