---
title: "Desafio #HackathonSomosNLP 2025: Preferências"
description: Como participar neste desafio e ajudar a alinhar modelos de linguagem com sua cultura
lang: pt
cover: https://somosnlp.github.io/assets/images/eventos/250401_hackathon_sinfecha.jpg
---

Projete prompts que avaliem a adequação cultural com seu país e escolha a melhor resposta em uma LLM Arena. Os prompts e as respostas serão coletados e compartilhados com todas as equipes participantes como dataset de preferências v0 para a fase de alinhamento. Para este desafio, você terá acesso a uma LLM Arena com 5 modelos grandes ou proprietários.

*14 de abril - 21 de maio (PRORROGADO) | máx 3 pontos*

1. **Leia o guia a seguir para aprender a projetar prompts de qualidade.**

<div style="display: flex; justify-content: center; gap: 20px;">
  <a href="https://forms.gle/itbDvVxD2iG5nzsC6" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">2. Verifique que você entendeu o guia</a>
  <a href="https://huggingface.co/spaces/somosnlp/validacion-preferencias" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">3. Valide prompts de outras equipes</a>
  <a href="https://fastchat-webui-908374066028.us-central1.run.app/gradio/" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">4. Envie seus prompts à Arena</a>
</div>

🌎 Gere **apenas** prompts relacionados com o país ou países com os quais você tenha um vínculo forte o suficiente para conhecer a cultura local.

✨ Incentivos (os números se referem a prompts respondidos validados):
- 100 por equipe = requisito para acessar os 500 USD da API da Cohere para o desafio principal
- Cada 50 prompts por equipe = 0,5 pontos (máx 2 pontos, o outro ponto é obtido de avaliar como vocês utilizarem a API da Cohere para melhorar o dataset)
- Vocês terão acesso aos dados gerados por todas as equipes para tomá-los como base para seu alinhamento, **uma maior qualidade dos dados implica uma maior qualidade do seu projeto**

🙌 Muito obrigado a:
- CENIA: Créditos API para os LLMs da Arena
- A equipe: Gonzalo Fuentes, Diana Galván, Eugenio Herrera, Sebastián Cifuentes, Clemente, María Grandury, Luis Vasquez e Valle Ruiz

Recursos:
- Definições, exemplos de prompts e datasets de preferências a seguir
- [Palestra sobre Red Teaming de Luis Vasquez](https://www.youtube.com/watch?v=pGOXE4rrO9M&list=PLTA-KAy8nxaDHyJyPlrDMCkwTsJZpMNK6)

## Objetivo

O objetivo deste desafio é criar entre todas as equipes um dataset que permita alinhar LLMs com a cultura dos países da LATAM e da Península Ibérica. Para isso, cada equipe tem que:

1. Projetar prompts seguindo o guia a seguir
2. Enviar seus prompts para uma LLM Arena e escolher a melhor resposta
3. Simultaneamente, ir validando os prompts e respostas de outras equipes
4. No dia 21 de abril publicaremos o conjunto de prompts e respostas, chamemos de "dataset v0"
5. Durante as 2 semanas seguintes cada equipe terá acesso a 500 USD em créditos da Cohere para processar, filtrar e estender v0 e a GPUs L40S da Hugging Face para alinhar um LLM de 7B de parâmetros.

Nota: para acessar os créditos e GPUs é necessário contribuir com 200 prompts **de qualidade** ao dataset.

Leia com atenção os guias a seguir para mais detalhes de cada passo. Leva menos de 10 minutos e é imprescindível para assegurar a qualidade e homogeneidade dos dados, muito importante para continuar seu projeto.

## **0. Como criar equipes**

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

## 1. As definições

O principal objetivo do hackathon, e em particular deste desafio, é melhorar a "adequação cultural" dos LLMs, vejamos o que isso significa. Começamos com algumas definições:

<details>
<summary>Cultura</summary>

> *Em seu sentido etnográfico amplo, a cultura é esse todo complexo que inclui o conhecimento, a crença, a arte, a moral, o direito, o costume e qualquer outra capacidade e hábito adquirido pelo homem como membro da sociedade. ([ref](https://books.google.co.uk/books/about/Through_the_Language_Glass.html?id=6NOjIzNZvosC&redir_esc=y))*
> 

> *Somente podemos considerar elementos da cultura tradicional, aqueles que a comunidade conserva e transmite. [...] Esta aceitação, e portanto, a literariedade tradicional, popular ou folclórica, dependerá se o texto se ajusta a uma linguagem determinada, a estruturas específicas, coincide com determinados temas, e se cria a partir de uma estética coletiva. ([ref](https://books.google.co.uk/books/about/M%C3%A9xico_tradicional.html?id=kbowDQAAQBAJ&redir_esc=y))*
> 

</details>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    <img src="https://somosnlp.github.io/assets/images/infografias/adecuacion_cultural/pt/1.png" alt="Adequação Cultural 1" style="width: 100%;">
    <img src="https://somosnlp.github.io/assets/images/infografias/adecuacion_cultural/pt/2.png" alt="Adequação Cultural 2" style="width: 100%;">
    <img src="https://somosnlp.github.io/assets/images/infografias/adecuacion_cultural/pt/3.png" alt="Adequação Cultural 3" style="width: 100%;">
    <img src="https://somosnlp.github.io/assets/images/infografias/adecuacion_cultural/pt/4.png" alt="Adequação Cultural 4" style="width: 100%;">
</div>

<details>
<summary>Multiculturalidade</summary>

> Existência de várias culturas que convivem em um mesmo espaço físico, geográfico ou social. Abrange todas as diferenças que se enquadram dentro da cultura, seja religiosa, linguística, racial, étnica ou de gênero. ([ref](https://www.significados.com/multiculturalidad/))
> 

> Perante a comunidade se reconhece a diversidade em todos os âmbitos e reconhece o respeito em relação a ela mesma, promovendo direitos para cada uma das culturas incluídas.
> 

</details>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    <img src="https://somosnlp.github.io/assets/images/infografias/adecuacion_cultural/pt/5.png" alt="Adequação Cultural 5" style="width: 100%;">
    <img src="https://somosnlp.github.io/assets/images/infografias/adecuacion_cultural/pt/6.png" alt="Adequação Cultural 6" style="width: 100%;">
    <img src="https://somosnlp.github.io/assets/images/infografias/adecuacion_cultural/pt/7.png" alt="Adequação Cultural 7" style="width: 100%;">
    <img src="https://somosnlp.github.io/assets/images/infografias/adecuacion_cultural/pt/8.png" alt="Adequação Cultural 8" style="width: 100%;">
    <img src="https://somosnlp.github.io/assets/images/infografias/adecuacion_cultural/pt/9.png" alt="Adequação Cultural 9" style="width: 100%;">
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
    <img src="https://somosnlp.github.io/assets/images/infografias/adecuacion_cultural/pt/10.png" alt="Adequação Cultural 10" style="width: 100%;">
    <img src="https://somosnlp.github.io/assets/images/infografias/adecuacion_cultural/pt/11.png" alt="Adequação Cultural 11" style="width: 100%;">
    <img src="https://somosnlp.github.io/assets/images/infografias/adecuacion_cultural/pt/12.png" alt="Adequação Cultural 12" style="width: 100%;">
</div>

<details>
<summary>Como a cultura afeta a capacidade de um LLM de entender uma linguagem?</summary>
  - Na comunicação → Os propósitos comunicativos são diretamente afetados pelas palavras e formas gramaticais usadas. Quanto mais palavras de um país específico uma oração tiver (por exemplo, do Brasil), mais difícil pode ser entendê-la para alguém (ou algo: um LLM) que não esteja familiarizado com essa cultura.
  - Na percepção do mundo → Códigos morais (i.e., o que é bom, o que é mau), atividades comuns (por exemplo, ir a uma luta livre ou ir a uma tourada), etc.

</details>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    <img src="https://somosnlp.github.io/assets/images/infografias/adecuacion_cultural/pt/13.png" alt="Adequação Cultural 13" style="width: 100%;">
    <img src="https://somosnlp.github.io/assets/images/infografias/adecuacion_cultural/pt/14.png" alt="Adequação Cultural 14" style="width: 100%;">
    <img src="https://somosnlp.github.io/assets/images/infografias/adecuacion_cultural/pt/15.png" alt="Adequação Cultural 15" style="width: 100%;">
    <img src="https://somosnlp.github.io/assets/images/infografias/adecuacion_cultural/pt/16.png" alt="Adequação Cultural 16" style="width: 100%;">
    <img src="https://somosnlp.github.io/assets/images/infografias/adecuacion_cultural/pt/17.png" alt="Adequação Cultural 17" style="width: 100%;">
    <img src="https://somosnlp.github.io/assets/images/infografias/adecuacion_cultural/pt/18.png" alt="Adequação Cultural 18" style="width: 100%;">
</div>


## **2. Como projetar os prompts**

### 2.1. Características gerais

Os prompts devem ser:

- **Não triviais**: evitar perguntas factuais simples (por exemplo, "Qual é a capital do Brasil?").
- **Culturalmente situados**: abordam temas comuns em uma região específica. **Utilize papéis para contextualizar sua pergunta**.
- **Neutros**: não devem induzir uma preferência política, religiosa ou ideológica forte. Estes temas podem ser tratados mas sem incluir opiniões sobre qual é "melhor".
- Não inclua estereótipos: para tratar este tema participe do desafio do [Validador de estereótipos](https://somosnlp.org/pt/hackathon/retos/estereotipos).

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

### **2.2. Exemplos de prompt (não exaustivos)**

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
</details> 

<center style="margin-top:40px;"><a href="https://fastchat-webui-908374066028.us-central1.run.app/gradio/" target="_blank" style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Participe agora!</a></center>

<center style="margin-top:40px;"><a href="https://somosnlp.org/pt/hackathon/retos" target="_blank" style="background-color:gray; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">Voltar aos desafios</a></center>
