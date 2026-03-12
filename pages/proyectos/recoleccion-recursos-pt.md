---
title: Recolha de recursos
description: 
date: 2026-04-01T18:00:00.000+00:00
lang: pt
duration: 
cover:
---

# Datasheets

3.1 Motivação
As perguntas desta secção têm como objetivo principal incentivar os criadores de datasets a articular claramente as suas razões para criar o dataset e a promover a transparência sobre os interesses de financiamento. Isto pode ser particularmente relevante para datasets criados para fins de investigação.
- Para que finalidade foi criado o dataset? Havia alguma tarefa específica em mente? Existia alguma lacuna específica que precisava de ser preenchida? Por favor, forneça uma descrição.
- Quem criou o dataset (p. ex., que equipa ou grupo de investigação) e em nome de que entidade (p. ex., empresa, instituição ou organização)?
- Quem financiou a criação do dataset? Se existir uma bolsa associada, indique o nome do financiador e o nome e número da bolsa.
- Algum outro comentário?

3.2 Composição
Os criadores de datasets devem ler estas perguntas antes de qualquer recolha de dados e, de seguida, fornecer respostas após a conclusão da recolha. A maioria das perguntas desta secção tem como objetivo fornecer aos consumidores de datasets as informações de que necessitam para tomar decisões informadas sobre a utilização do dataset para as tarefas escolhidas. Algumas perguntas são elaboradas para obter informações sobre a conformidade com o Regulamento Geral sobre a Proteção de Dados (RGPD) da UE ou regulamentos comparáveis noutras jurisdições. As perguntas que se aplicam apenas a datasets relacionados com pessoas são agrupadas no final da secção. Recomendamos adotar uma interpretação ampla sobre se um dataset está relacionado com pessoas. Por exemplo, qualquer dataset que contenha texto escrito por pessoas está relacionado com pessoas.
- O que representam as instâncias que compõem o dataset (p. ex., documentos, fotografias, pessoas, países)? Existem múltiplos tipos de instâncias (p. ex., filmes, utilizadores e avaliações; pessoas e interações entre elas; nós e arestas)? Por favor, forneça uma descrição.
- Quantas instâncias existem no total (de cada tipo, se aplicável)?
- O dataset contém todas as instâncias possíveis ou é uma amostra (não necessariamente aleatória) de instâncias de um conjunto maior? Se for uma amostra, qual é o conjunto maior? A amostra é representativa do conjunto maior (p. ex., cobertura geográfica)? Em caso afirmativo, descreva como essa representatividade foi validada/verificada. Se não for representativa do conjunto maior, descreva por que não (p. ex., para cobrir uma gama mais diversificada de instâncias, porque algumas instâncias foram retidas ou não estavam disponíveis).
- De que dados é composta cada instância? Dados "brutos" (p. ex., texto não processado ou imagens) ou características? Em ambos os casos, forneça uma descrição.
- Existe um rótulo ou variável alvo associado a cada instância? Em caso afirmativo, forneça uma descrição.
- Há alguma informação em falta em instâncias individuais? Em caso afirmativo, forneça uma descrição explicando por que essa informação está ausente (p. ex., porque não estava disponível). Isto não inclui informação removida intencionalmente, mas pode incluir, por exemplo, texto redigido.
- As relações entre instâncias individuais são tornadas explícitas (p. ex., avaliações de filmes por utilizadores, ligações de redes sociais)? Em caso afirmativo, descreva como essas relações são explicitadas.
- Existem data splits recomendados (p. ex., treino, desenvolvimento/validação, teste)? Em caso afirmativo, forneça uma descrição dessas divisões, explicando a justificação subjacente.
- Há erros, fontes de ruído ou redundâncias no dataset? Em caso afirmativo, forneça uma descrição.
- O dataset é autocontido ou está ligado a, ou de outra forma depende de, recursos externos (p. ex., sítios web, tweets, outros datasets)? Se estiver ligado a ou depender de recursos externos, a) existem garantias de que eles existirão e permanecerão constantes ao longo do tempo; b) existem versões de arquivo oficiais do dataset completo (ou seja, incluindo os recursos externos tal como existiam no momento da criação do dataset); c) existem restrições (p. ex., licenças, taxas) associadas a algum dos recursos externos que possam aplicar-se a um consumidor do dataset? Forneça descrições de todos os recursos externos e de quaisquer restrições associadas, bem como ligações ou outros pontos de acesso, conforme apropriado.
- O dataset contém dados que poderiam ser considerados confidenciais (p. ex., dados protegidos por privilégio legal ou sigilo médico-paciente, dados que incluem o conteúdo de comunicações não públicas de indivíduos)? Em caso afirmativo, forneça uma descrição.
- O dataset contém dados que, se visualizados diretamente, poderiam ser ofensivos, insultantes, ameaçadores ou que poderiam causar ansiedade? Em caso afirmativo, descreva por quê.

Se o dataset não estiver relacionado com pessoas, pode ignorar as perguntas restantes desta secção.
- O dataset identifica alguma subpopulação (p. ex., por idade, género)? Em caso afirmativo, descreva como essas subpopulações são identificadas e forneça uma descrição das suas respetivas distribuições dentro do dataset.
- É possível identificar indivíduos (ou seja, uma ou mais pessoas singulares), direta ou indiretamente (ou seja, em combinação com outros dados) a partir do dataset? Em caso afirmativo, descreva como.
- O dataset contém dados que poderiam ser considerados sensíveis de alguma forma (p. ex., dados que revelem raça ou origem étnica, orientação sexual, crenças religiosas, opiniões políticas ou filiação sindical, ou localizações; dados financeiros ou de saúde; dados biométricos ou genéticos; formas de identificação governamental, como números de segurança social; historial criminal)? Em caso afirmativo, forneça uma descrição.
- Algum outro comentário?

3.3 Processo de recolha
À semelhança das perguntas da secção anterior, os criadores de datasets devem ler estas perguntas antes de qualquer recolha de dados para identificar potenciais problemas e, de seguida, fornecer respostas após a conclusão da recolha. Para além dos objetivos descritos na secção anterior, as perguntas desta secção são elaboradas para obter informações que possam ajudar investigadores e profissionais a criar datasets alternativos com características semelhantes. Do mesmo modo, as perguntas que se aplicam apenas a datasets relacionados com pessoas são agrupadas no final da secção.

- Como foram adquiridos os dados associados a cada instância? Os dados eram diretamente observáveis (p. ex., texto bruto, avaliações de filmes), reportados por sujeitos (p. ex., respostas a inquéritos), ou inferidos/derivados indiretamente de outros dados (p. ex., marcações de partes do discurso, estimativas de idade ou idioma baseadas em modelos)? Se os dados foram reportados por sujeitos ou inferidos/derivados indiretamente de outros dados, foram validados/verificados? Em caso afirmativo, descreva como.
- Que mecanismos ou procedimentos foram utilizados para recolher os dados (p. ex., aparelhos de hardware ou sensores, curadoria humana manual, programas de software, APIs de software)? Como foram validados esses mecanismos ou procedimentos?
- Se o dataset é uma amostra de um conjunto maior, qual foi a estratégia de amostragem (p. ex., determinista, probabilista com probabilidades de amostragem específicas)?
- Quem esteve envolvido no processo de recolha de dados (p. ex., estudantes, trabalhadores de crowdsourcing, contratados) e como foram remunerados (p. ex., quanto foram pagos os trabalhadores de crowdsourcing)?
- Em que período de tempo foram recolhidos os dados? Este período corresponde ao período de criação dos dados associados às instâncias (p. ex., rastreamento recente de artigos de notícias antigos)? Caso contrário, descreva o período em que os dados associados às instâncias foram criados.
- Foram realizados processos de revisão ética (p. ex., por uma comissão de ética em investigação)? Em caso afirmativo, forneça uma descrição desses processos de revisão, incluindo os resultados, bem como uma ligação ou outro ponto de acesso a qualquer documentação de suporte.

Se o dataset não estiver relacionado com pessoas, pode ignorar as perguntas restantes desta secção

- Os dados foram recolhidos diretamente dos indivíduos em questão, ou obtidos por meio de terceiros ou outras fontes (p. ex., sítios web)?
- Os indivíduos em questão foram notificados sobre a recolha de dados? Em caso afirmativo, descreva (ou mostre com capturas de ecrã ou outras informações) como foi fornecida a notificação e forneça uma ligação ou outro ponto de acesso ao texto exato da notificação, ou reproduza-o.
- Os indivíduos em questão consentiram a recolha e utilização dos seus dados? Em caso afirmativo, descreva (ou mostre com capturas de ecrã ou outras informações) como o consentimento foi solicitado e fornecido, e forneça uma ligação ou outro ponto de acesso ao texto exato ao qual os indivíduos consentiram, ou reproduza-o.
- Se o consentimento foi obtido, foi fornecido aos indivíduos que consentiram um mecanismo para revogar o seu consentimento no futuro ou para determinadas utilizações? Em caso afirmativo, forneça uma descrição, bem como uma ligação ou outro ponto de acesso ao mecanismo (se aplicável).
- Foi realizada uma análise do impacto potencial do dataset e da sua utilização nos titulares de dados (p. ex., uma análise de impacto sobre a proteção de dados)? Em caso afirmativo, forneça uma descrição dessa análise, incluindo os resultados, bem como uma ligação ou outro ponto de acesso a qualquer documentação de suporte.
- Algum outro comentário?

3.4 Pré-processamento/limpeza/rotulagem
Os criadores de datasets devem ler estas perguntas antes de qualquer pré-processamento, limpeza ou rotulagem e, de seguida, fornecer respostas após a conclusão dessas tarefas. As perguntas desta secção têm como objetivo fornecer aos consumidores de datasets as informações de que necessitam para determinar se os dados "brutos" foram processados de formas compatíveis com as tarefas escolhidas. Por exemplo, o texto que foi convertido em "bag-of-words" não é adequado para tarefas que envolvam a ordem das palavras.
- Foi realizado algum pré-processamento/limpeza/rotulagem dos dados (p. ex., discretização ou agrupamento, tokenização, marcação de partes do discurso, extração de características SIFT, remoção de instâncias, processamento de valores em falta)? Em caso afirmativo, forneça uma descrição. Caso contrário, pode ignorar as perguntas restantes desta secção.
- Os dados "brutos" foram guardados em complemento aos dados pré-processados/limpos/rotulados (p. ex., para possíveis utilizações futuras não previstas)? Em caso afirmativo, forneça uma ligação ou outro ponto de acesso aos dados "brutos".
- O software utilizado para pré-processar/limpar/rotular os dados está disponível? Em caso afirmativo, forneça uma ligação ou outro ponto de acesso.
- Algum outro comentário?

3.5 Utilizações
As perguntas desta secção têm como objetivo incentivar os criadores de datasets a refletir sobre as tarefas para as quais o dataset deve e não deve ser utilizado. Ao destacar explicitamente essas tarefas, os criadores de datasets podem ajudar os consumidores a tomar decisões informadas, evitando assim possíveis riscos ou danos.
- O dataset já foi utilizado para alguma tarefa? Em caso afirmativo, forneça uma descrição.
- Existe algum repositório que estabeleça ligação a alguns ou todos os artigos ou sistemas que utilizam o dataset? Em caso afirmativo, forneça uma ligação ou outro ponto de acesso.
- Para que (outras) tarefas poderia ser utilizado o dataset?
- Há algo sobre a composição do dataset ou a forma como foi recolhido e pré-processado/limpo/rotulado que possa afetar utilizações futuras? Por exemplo, há algo que um consumidor do dataset precise de saber para evitar utilizações que possam resultar em tratamento injusto de indivíduos ou grupos (p. ex., estereótipos, problemas de qualidade do serviço) ou outros riscos ou danos (p. ex., riscos legais, danos financeiros)? Em caso afirmativo, forneça uma descrição. Existe algo que um consumidor do dataset pudesse fazer para mitigar esses riscos ou danos?
- Existem tarefas para as quais o dataset não deve ser utilizado? Em caso afirmativo, forneça uma descrição.
- Algum outro comentário?

3.6 Distribuição
Os criadores de datasets devem fornecer respostas a estas perguntas antes de distribuir o dataset, seja internamente dentro da entidade em nome da qual foi criado ou externamente a terceiros.
- O dataset será distribuído a terceiros fora da entidade (p. ex., empresa, instituição, organização) em nome da qual foi criado? Em caso afirmativo, forneça uma descrição.
- Como será distribuído o dataset (p. ex., tarball num sítio web, API, GitHub)? O dataset tem um identificador de objeto digital (DOI)?
- Quando será distribuído o dataset?
- O dataset será distribuído sob uma licença de direitos de autor ou outra licença de propriedade intelectual (PI), e/ou sob termos de utilização (TdU) aplicáveis? Em caso afirmativo, descreva essa licença e/ou os TdU, e forneça uma ligação ou outro ponto de acesso aos termos de licença ou TdU relevantes, ou reproduza-os, bem como quaisquer taxas associadas a essas restrições.
- Terceiros impuseram restrições baseadas em PI ou outras restrições sobre os dados associados às instâncias? Em caso afirmativo, descreva essas restrições e forneça uma ligação ou outro ponto de acesso aos termos de licença relevantes, ou reproduza-os, bem como quaisquer taxas associadas a essas restrições.
- Aplicam-se controlos de exportação ou outras restrições regulatórias ao dataset ou a instâncias individuais? Em caso afirmativo, descreva essas restrições e forneça uma ligação ou outro ponto de acesso à documentação de suporte, ou reproduza-a.
- Algum outro comentário?

3.7 Manutenção
À semelhança das perguntas da secção anterior, os criadores de datasets devem fornecer respostas a estas perguntas antes de distribuir o dataset. As perguntas desta secção têm como objetivo incentivar os criadores de datasets a planear a manutenção do dataset e a comunicar esse plano aos consumidores.

- Quem será responsável pelo suporte/alojamento/manutenção do dataset?
- Como pode ser contactado o proprietário/curador/gestor do dataset (p. ex., endereço de correio eletrónico)?
- Existe um erratum? Em caso afirmativo, forneça uma ligação ou outro ponto de acesso.
- O dataset será atualizado (p. ex., para corrigir erros de rotulagem, adicionar novas instâncias, eliminar instâncias)? Em caso afirmativo, descreva com que frequência, por quem e como as atualizações serão comunicadas aos consumidores do dataset (p. ex., lista de correio eletrónico, GitHub).
- Se o dataset estiver relacionado com pessoas, existem limites aplicáveis à retenção dos dados associados às instâncias (p. ex., foi informado aos indivíduos em questão que os seus dados seriam retidos durante um período de tempo fixo e depois eliminados)? Em caso afirmativo, descreva esses limites e explique como serão aplicados.
- Versões anteriores do dataset continuarão a ser suportadas/alojadas/mantidas? Em caso afirmativo, descreva como. Caso contrário, descreva como a sua obsolescência será comunicada aos consumidores do dataset.
- Se outros desejarem estender/ampliar/desenvolver/contribuir para o dataset, existe um mecanismo para o fazer? Em caso afirmativo, forneça uma descrição. Essas contribuições serão validadas/verificadas? Em caso afirmativo, descreva como. Caso contrário, porquê? Existe um processo para comunicar/distribuir essas contribuições aos consumidores do dataset? Em caso afirmativo, forneça uma descrição.
- Algum outro comentário?
