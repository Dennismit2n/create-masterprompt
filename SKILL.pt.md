# Create Masterprompt — versão portuguesa

> Tradução de `SKILL.md`. **O programa lê exclusivamente `SKILL.md`**, o
> ficheiro em inglês — esta versão existe para consulta humana. Se as duas se
> contradisserem, vale a inglesa. Corresponde à versão 1.7.0.
>
> Nomes de ficheiros, pastas e comandos de exemplo ficam propositadamente sem
> traduzir, porque é assim que se chamam no disco.
>
> Uma página para ver de relance em vez de ler de fio a pavio: [`docs/uebersicht-pt.png`](docs/uebersicht-pt.png)
> (versão inglesa: [`docs/uebersicht-en.png`](docs/uebersicht-en.png)).
>
> **Estado: publicação inicial.** O texto foi verificado várias vezes quanto à
> coerência interna e à conformidade com a especificação, mas o Skill em si
> ainda não correu em muitos projetos reais e distintos. Se algo no fluxo, na
> triagem de tamanho ou num dos templates não encaixar na tua forma de
> trabalhar, isso é um sinal útil — agradece-se que o reportes como Issue.

Um master prompt **não** é um prompt de persona. “És um engenheiro sénior, sê
minucioso” não acrescenta nada que um modelo competente já não faça. Um master
prompt é um **pacote de contexto**: os factos, decisões e limites duradouros de
um projeto, escritos de forma a que uma sessão sem qualquer histórico retome
exatamente onde a anterior parou.

Este Skill constrói esse pacote em seis fases e devolve três ficheiros.

## O que produzes

| Ficheiro | Para quê | Tempo de vida |
|---|---|---|
| `BRIEFING.md` | O master prompt. Contexto, decisões, anti-scope, armadilhas, estado atual. | O projeto inteiro |
| `DECISIONS.md` | Uma linha por questão resolvida, com o motivo. Só se acrescenta, nunca se reescreve. | O projeto inteiro |
| `HANDOFF_vNN.md` | Escrito antes do limite de contexto. O que uma sessão nova precisa *agora mesmo*. | Uma sessão |

Dá-lhes nomes na língua do utilizador. Mantém-nos junto do trabalho, não no
chat.

## Fase 0 — Triagem de tamanho (faz isto primeiro, em dez segundos)

Correr seis fases num script de renomear é a forma como as pessoas aprendem a
saltar o processo por completo. Classifica antes de começar:

- **S — uma sentada, reversível, sem incógnitas.** Passa diretamente ao
  trabalho. Oferece o percurso completo só se o projeto crescer.
- **M — algumas sessões, algumas incógnitas, uma ou duas bifurcações reais.**
  Fases 1–3 e 5, mais a 6 assim que o trabalho ultrapassar uma sessão.
  Ficheiro de briefing, mas curto. Sem documento de plano separado.
- **L — várias sessões, arquitetura a sério, decisões caras de desfazer.**
  As seis fases todas.

Diz numa frase que tamanho escolheste e porquê. Se o utilizador discordar, vai
dizê-lo — isso custa uma mensagem e poupa uma hora.

## Fase 1 — Pesquisa

Descobre o que já existe, onde está a lacuna, o que é tecnicamente viável e
que armadilhas já estão documentadas. **A pesquisa acontece só aqui.**
Pesquisar a meio da construção é a forma como uma construção se transforma num
poço sem fundo.

Entregável: um relatório com uma tabela comparativa, uma recomendação e fontes.

**Para de pesquisar quando as três condições se cumprirem** — não quando a
curiosidade se esgotar:
1. A tabela comparativa não tem células vazias para as opções pré-selecionadas.
2. Cada linha de armadilha tem uma fonte ou está marcada como pressuposto.
3. As duas últimas pesquisas não trouxeram nada de novo. Isso é saturação.

Se não conseguires chegar à saturação, di-lo e nomeia o que ficou em aberto.
Uma lacuna honesta vale mais do que um palpite confiante, e o utilizador pode
decidir se quer investir mais tempo.

## Fase 2 — Briefing

Comprime a pesquisa em `BRIEFING.md` usando `assets/template-briefing.md`.

O teste para este ficheiro: **entrega-o a uma sessão nova, sem histórico.
Consegue trabalhar com ele?** Se precisar de uma única pergunta de
esclarecimento sobre algo que tu já sabias, o briefing está incompleto. Relê-o
com olhos de adversário antes de o mostrar.

Secções obrigatórias — as duas primeiras são as que as pessoas saltam e depois
lamentam:

- **Anti-scope.** Não-objetivos explícitos, cada um com o seu motivo. “Sem
  encriptação na v1 — o cofre é só local, e a gestão de chaves duplicaria a
  construção.” O anti-scope é a defesa mais forte que existe contra o scope
  creep, porque transforma cada “não podíamos simplesmente…” numa decisão que
  tem de ser reaberta, em vez de um acrescento gratuito.
- **Registo de pressupostos.** Tudo o que decidiste sem perguntar. Uma linha
  por item, marcada para poder ser contestada mais tarde. Pressupostos não
  registados são invisíveis até se tornarem caros.
- Contexto, restrições, armadilhas conhecidas, estado atual.

## Fase 3 — Entrevista de decisões

Coloca as decisões em aberto **uma de cada vez**, esperando pela resposta
antes da seguinte. Perguntas em lote são lidas na diagonal, e uma decisão lida
na diagonal é um palpite com a assinatura do utilizador.

Por pergunta: 2–4 opções, uma recomendação clara e o motivo dela. Resolve as
dependências por ordem — decide a stack antes da biblioteca que corre sobre
ela.

**Vai tu mesmo à procura.** Se um facto pode ser descoberto em ficheiros,
ferramentas ou na web, descobre-o. Só as escolhas genuínas pertencem ao
utilizador.

**Não construas nada antes de esta fase fechar.** Se o utilizador disser
“começa lá” a meio da entrevista: nomeia as decisões concretas ainda em aberto,
oferece-te para as tomar tu como pressupostos registados, e continua só depois
de ele escolher. Começar com bifurcações em aberto significa retrabalho, e o
retrabalho custa mais do que custou a entrevista.

Fecha com um resumo numerado de todas as decisões. Acrescenta-o ao registo de
decisões, que segue `assets/template-decisions.md`.

## Fase 4 — Plano

Arquitetura, estrutura do repositório ou das pastas, ficheiro de convenções,
estratégia de testes, marcos, definição de concluído por marco e uma definição
de concluído para o projeto como um todo.

Os marcos são **fatias verticais**: cada um produz algo que o utilizador pode
de facto executar, ver ou usar. Cinco marcos que entregam cada um uma fatia
funcional valem mais do que três que entregam uma fundação que ninguém
consegue testar.

Mostra o plano para aprovação antes de construir.

## Fase 5 — Construção

Trabalha contra um objetivo declarado com uma **condição de paragem
verificável**. “Pronto quando `npm test` passa e a app abre a pasta do cofre” é
verificável. “Pronto quando funciona bem” não é.

- Teste antes da funcionalidade, onde um teste faz sentido.
- Commits pequenos, cada um revertível por si só.
- Linting como hook, não como lembrete.
- Sem pausas para pedir permissão. Pergunta só em bifurcações de design
  genuínas.

## Fase 6 — Handoff

Antes do limite de contexto — não depois — escreve o ficheiro de handoff
(`HANDOFF_vNN.md`, com nome na língua do utilizador) a partir de
`assets/template-handoff.md`, e depois inicia uma sessão nova. A compactação
sem fim perde precisamente os detalhes que foram caros de estabelecer.

Gatilhos: troços longos com uso intensivo de ferramentas, releitura repetida
dos mesmos ficheiros, ou o utilizador a pedir pela segunda vez algo que já foi
tratado.

## Ronda de melhoria

Em cada fronteira de fase, **antes** de mostrar o resultado, muda em silêncio
de escritor para revisor. Três perguntas:

1. **O que falta?** Que pergunta teria uma sessão nova de fazer que este
   ficheiro não responde?
2. **O que está afirmado em vez de comprovado?** Cada alegação sem fonte ou
   sem marca de pressuposto é candidata.
3. **O que é enchimento?** Qualquer frase que pudesse aparecer em qualquer
   outro projeto sai.

O utilizador vê o resultado revisto, não a crítica. Exceção: se a ronda
trouxer à tona algo que toca numa decisão, isso tem de lhe ser mostrado.

Produzir e avaliar são atividades diferentes. O escritor não consegue ver a
lacuna porque a peça em falta está na cabeça dele. Custa cerca de 30 % da fase
e rende mais do que qualquer outra coisa neste Skill.

Quando a forma da tarefa vai além de “escreve-me X”, carrega primeiro
`references/prompt-techniques.md` — traz a tabela de encaminhamento de forma de
tarefa para técnica e os sinais de alerta de over-prompting.

## Regra de retrocesso

As decisões são revistas. Isso é normal e barato, **se for bem tratado**:

1. Atualiza o registo de decisões — acrescenta a linha nova, marca a antiga
   como substituída, mantém as duas. A história explica por que razão o código
   tem o aspeto que tem.
2. Atualiza `BRIEFING.md`, porque é isso que uma sessão nova lê.
3. Nomeia o que a mudança invalida antes de tocar no código.

Mudar de rumo só no chat é o modo de falha: os ficheiros continuam a descrever
o projeto antigo, a sessão seguinte acredita neles, e a contradição vem ao de
cima três passos mais tarde.

## Regra de saída

Um projeto que não produziu nada em três sessões está encravado ou morto.
Di-lo sem rodeios e oferece três opções: encolher o âmbito, estacioná-lo com
um handoff escrito para poder ser retomado de forma limpa, ou abandoná-lo.
Ideias são baratas; projetos meio construídos têm custos de manutenção. Este é
o único sítio onde ser frontal é o serviço.

## Gotchas

Factos do ambiente que desafiam qualquer suposição razoável. Verifica-os antes
de contornar um sintoma.

- **O frontmatter de Skills da Anthropic aceita exatamente seis chaves**:
  `name`, `description`, `license`, `allowed-tools`, `metadata`,
  `compatibility`. Qualquer outra falha a validação ao fazer upload para o
  claude.ai, mesmo que o Claude Code a tolere. Os Skills funcionam localmente
  em silêncio e partem-se no upload.
- **O nome da pasta tem de ser igual ao campo `name`** após normalização NFKC.
  Renomear a pasta sem o frontmatter é a avaria mais comum.
- **`name`: só minúsculas, dígitos e hífens.** Sem underscores, sem hífens
  consecutivos, sem hífen no início nem no fim. Máximo 64 caracteres.
  `description` máximo 1024.
- **Dois pontos sem aspas em `description` partem o parse do YAML.** “Use
  when: …” falha. Põe entre aspas ou usa um escalar de bloco (`>-`).
- **No arranque da sessão só `name` + `description` são carregados.** O corpo
  carrega ao disparar. Por isso, toda a dica de “quando usar isto” pertence à
  descrição; uma condição de disparo enterrada no corpo nunca é lida a tempo de
  disparar.
- **Pedidos simples de um só passo não disparam Skills**, por melhor que seja
  a descrição, porque o modelo trata deles diretamente. Testa o disparo com
  pedidos substanciais, de vários passos.
- **Os Skills são instruções, não imposição.** `allowed-tools` dispensa os
  pedidos de permissão; não restringe nada.

## Ficheiros de referência

Carrega-os quando a fase os pedir, não à partida:

- `references/profile-questionnaire.md` — os campos que um utilizador preenche
  uma vez para tornar este Skill seu. Lê na primeira utilização, ou quando o
  utilizador quiser uma variante pessoal.
- `references/quality-gates.md` — a lista de verificação por fase. Lê antes de
  fechar qualquer fase.
- `references/anti-patterns.md` — modos de falha com as respetivas correções.
  Lê quando um projeto está a empancar, a andar em círculos ou a gerar
  retrabalho.
- `references/model-routing.md` — que classe de modelo se adequa a que fase.
  Lê quando o utilizador se importa com a escolha de modelo ou com o custo.
- `references/prompt-techniques.md` — encaminhamento de forma de tarefa para
  técnica, mais sinais de alerta de over-prompting. Lê quando uma fase não
  está a entregar, um artefacto parece magro ou a tarefa vai além de
  “escreve-me X”.

Os templates em `assets/` destinam-se a ser copiados e preenchidos, não
parafraseados. Estruturas são reproduzidas com mais fiabilidade do que
descrições em prosa de estruturas.

## Regras da casa

Estas moldam cada resposta enquanto o Skill está ativo:

- **Responde na língua do utilizador**, incluindo nos ficheiros gerados. Este
  Skill está escrito em inglês; o resultado não.
- **Uma pequena lição por resposta.** Duas a quatro frases sobre o *porquê*,
  não sobre o quê. A ideia é que o utilizador consiga conduzir o projeto
  seguinte sem ti.
- **Qualidade acima de poupança na escolha do modelo.** Nunca desças para um
  modelo mais barato quando o mais capaz dá um resultado melhor. Mais barato só
  está certo quando o resultado é equivalente. Na dúvida, fica no de cima e
  di-lo.
- **Nunca adivinhes onde um erro é caro.** Uma gralha numa resposta não custa
  nada. Uma gralha num nome de ficheiro, identificador, formato de dados ou
  commit custa uma tarde. Corrige em silêncio onde a versão certa é óbvia;
  pergunta onde não é.
- **Abreviaturas pouco claras: pergunta, não adivinhes.** Indica a expansão
  habitual, se existir. Um palpite errado aqui acumula — três passos mais tarde
  já sustenta peso e é caro de desfazer.
- **Declara os pressupostos em voz alta.** Se não tiveres a certeza de que o
  teu pressuposto se aguenta, di-lo em vez de o vender como facto.
- **Sem perguntas a pairar quando uma tarefa está concluída.** Nada de “mais
  alguma coisa?”, nada de menu de opções para fechar. Se o utilizador quiser
  mais, vai dizê-lo.
