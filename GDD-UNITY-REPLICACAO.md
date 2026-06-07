# 🐴 Burrinho Royale — Documento de Mecânicas para Replicação em Unity

> **Objetivo:** descrever **todas as mecânicas e regras** do jogo com precisão suficiente para reimplementá-lo no Unity. Os números aqui refletem exatamente o balanceamento atual do protótipo.
>
> **Gênero:** Roguelike deckbuilder de dominó (estilo *Balatro*), single-player, com sabor alagoano.
> **Pitch:** Você joga dominó contra "A Lenda", encaixando pedras nas pontas da mesa para **bater uma meta de pontos** por fase. Cada pedra vale `Fichas × Mult`, e você acumula **Jokers** que distorcem essa conta.
> **Plataforma alvo:** WebGL/Browser.

---

## 1. Visão Geral do Loop de Jogo

```
NOVA RUN → FASE 1
   ↓
[ Dentro de uma fase ]
   Recebe mão de 7 pedras → joga pedras nas pontas → pontua (Fichas × Mult)
   • Esvaziou a mão? → mão nova GRÁTIS
   • Não encaixa? → "Gato por Lebre" (blefe arriscado) OU comprar do monte (−1 rodada)
   • pontos ≥ meta → VENCEU a fase
   • acabaram as rodadas + sem jogada, OU monte vazio + sem jogada → PERDEU a run
   ↓
RECOMPENSA: escolha 1 de 3 Jokers grátis (valem a run inteira)
   ↓
FASE seguinte (meta maior) → ... → repete
   ↓
PERDEU em qualquer fase → tela de fim → "Jogar de novo"
```

**Diferencial de design (a identidade do jogo):** o ciclo "esvaziou a mão → mão grátis". Vários jokers premiam isso — preserve a regra.

---

## 2. As Pedras (Dominó)

- O baralho é o **dominó duplo-6 padrão: 28 pedras únicas**. São todas as combinações de duas metades de 0 a 6, sem repetir o par: `[0,0], [0,1], … [0,6], [1,1], [1,2], … [6,6]`.
- Cada pedra tem **duas metades**, cada uma com um valor de **0 a 6**.
- **Nomes dos números** (usados na UI e nos jokers de tipo):

| Valor | Nome |
|------:|------|
| 0 | Branco |
| 1 | Piu |
| 2 | Duque |
| 3 | Terno |
| 4 | Quadra |
| 5 | Quina |
| 6 | Sena |

- **Carroça / dupla / "bomba":** pedra cujas duas metades são iguais (ex.: `[3,3]`).
- **"Tem o tipo N":** a pedra mostra o número N em **pelo menos uma** das metades (ex.: `[6,3]` tem o tipo 6 e o tipo 3).
- O baralho é **embaralhado** no início de cada fase (use um gerador aleatório com seed opcional para testes).

---

## 3. Progressão de Fases e Meta de Pontos

- Cada fase tem uma **meta de pontos**. Quando os pontos da fase atingem ou superam a meta, a fase é vencida na hora.
- **Meta por fase (escala automática):** `meta = arredondar(40 × 1,6^(número da fase − 1))`.
  - Fase 1 → **40** · Fase 2 → **64** · Fase 3 → **~102** · Fase 4 → **~164** · Fase 5 → **~262** · Fase 6 → **~419**.
  - A escala continua mesmo passando da fase 6 (a meta segue crescendo).
- **Rodadas (vidas) por fase:** **3** por padrão (o joker Jangada dá +1).
- **Nomes das fases** (estética, sabor alagoano):
  1. A Maré de Pajuçara
  2. O Sururu da Lagoa Mundaú
  3. A Jangada da Praia do Francês
  4. O Farol da Ponta Verde
  5. O Cânion do São Francisco
  6. A Feira de Maceió
- O indicador de fase na UI é uma **pilha de pontinhos** no canto inferior esquerdo: fase 1 = 1 pontinho, fase 2 = 2 pontinhos, e assim por diante.

> **Não há tela de vitória final** — a run sobe de fase indefinidamente (metas cada vez maiores) até o jogador perder. Os 6 nomes são apenas estéticos; passando do sexto, o nome fica no da última fase.

---

## 4. Início de Fase

Ao iniciar uma fase:
1. Embaralha as 28 pedras (formam o **monte**, a pilha de compra).
2. Tira as **7 primeiras** para a **mão** do jogador (elas saem do monte).
3. A **mesa** começa **vazia**, sem pedras.
4. Os pontos zeram; as rodadas voltam a 3 (+1 se tiver Jangada).
5. A meta da fase é calculada conforme a Seção 3.

---

## 5. Regras de Dominó (mesa reta de 2 pontas)

A mesa é uma **linha reta** com **duas pontas abertas** (esquerda e direita). Não há ramificações.

- **Ponta esquerda:** o número exposto na extremidade esquerda da fileira.
- **Ponta direita:** o número exposto na extremidade direita da fileira.
- **Onde pode jogar:**
  - **Mesa vazia:** qualquer pedra abre o jogo (vale para os dois lados).
  - **Mesa com pedras:** uma pedra pode ser jogada num lado se uma das suas metades for **igual ao número daquela ponta**.
- **Orientação ao encaixar:** a pedra é **girada** para que a metade que casa com a ponta fique encostada nela. (Importa para o visual e para recalcular qual número fica exposto na nova ponta.)
- **Escolha de lado:** se a pedra encaixa nas **duas** pontas, o jogo pergunta o lado (botões "◀ Esquerda" / "Direita ▶"). Se só encaixa num lado, joga direto nele.
- **Lá e Lô:** estado em que a mesa tem pedras **e** as duas pontas abertas mostram o **mesmo número**. É um gatilho para vários jokers (ver Seção 12.4).

---

## 6. Sistema de Pontuação (o coração do jogo)

> **Fórmula base:** `Pontos da jogada = Fichas × Mult` (+ bônus fixos de campo no fim). "Fichas" = a soma dos pontinhos da pedra, modificada por jokers. "Mult" = multiplicador.

Cada pedra jogada é pontuada na **ordem exata** abaixo (a ordem altera o resultado, então respeite-a):

### Passo A — Fichas
1. **Fichas = soma das duas metades** da pedra (ex.: `[6,3]` = 9).
2. **Filé da Rendeira** (se tiver o joker) e a pedra tem um 6 → **Fichas × 2**.
3. **Maré** (se tiver) → **Fichas + 1**.
4. Para cada joker **"+5 {Tipo}"** cujo tipo a pedra tenha → **Fichas + 5** (empilham; vários podem somar).

### Passo B — Mult
5. **Mult base = 1** + 2 (se tiver **Cachaça**) + bônus acumulado de **Mão Cheia** (ver Seção 8). *Este é o Mult exibido no HUD.*
6. **Carroça Dourada** (se tiver) e a pedra é dupla → **Mult + 3**.
7. **Bomba na Maré** (se tiver) e a pedra é dupla **e** a mesa já estava em lá e lô **antes** da jogada → **Mult + 5**.
8. Se a jogada veio de **Gato por Lebre** → jokers de blefe somam Mult (ex.: "Quem não arrisca não petisca" = **Mult + 2**).

### Passo C — Resultado final
9. **Ganho = Fichas × Mult**.
10. Para cada joker **"{Tipo} em Dobro"** cujo tipo a pedra tenha → **Ganho × 2** (empilham e são multiplicativos).
11. **Embalo do Lá e Lô** (se tiver) e a mesa já estava em lá e lô **antes** → **Ganho + 5** (fixo).
12. **Lá e Lô Premiado** (se tiver) e a jogada **deixou** a mesa em lá e lô (estado **depois**) → **Ganho + 10** (fixo).
13. **Mau-Olhado dos bosses:** se um boss de Mau-Olhado está ativo **e** esta é a **1ª pedra desta mão** → **Ganho = 0** (zera tudo, inclusive os bônus fixos).
14. Soma o Ganho aos pontos da fase.

> **Pontos de atenção:**
> - Jokers **"+5 Tipo"** somam **fichas** (passo 4); jokers **"{Tipo} em Dobro"** dobram o **resultado já multiplicado** (passo 10). São coisas diferentes.
> - Os bônus de lá e lô (+5 / +10) são **fixos no resultado final**, somados depois de `Fichas × Mult`.
> - O Mau-Olhado zera o ganho inteiro da 1ª pedra da mão, ignorando todos os bônus.
> - **Exemplos:** `[6,6]` sem jokers = 12 fichas × 1 = **12**. Com **Cachaça**: 12 × 3 = **36**. Numa `[6,3]` com **Filé**: (9 × 2) × mult. Com **+5 Sena** numa `[6,3]`: (9 + 5) × mult; com **Sena em Dobro** o resultado ainda dobra.

---

## 7. Jogar uma Pedra (fluxo)

1. O jogador clica numa pedra da mão.
2. Se a pedra estiver **bloqueada** (boss Duque) → nada acontece.
3. Se a pedra **não encaixa** em nenhuma ponta → abre a opção **Gato por Lebre** (se ainda disponível na fase).
4. Se encaixa nos **dois** lados → o jogo pergunta o lado; senão joga no único lado válido.
5. A pedra é encaixada (girada conforme a regra de orientação), some da mão e vai para a mesa.
6. A jogada é **pontuada** (Seção 6) e aparece a animação flutuante (ex.: `+36 (12 × 3)`; ou "Mau-olhado! 0" quando zerada).
7. **Vitória imediata:** se os pontos atingiram a meta → vence a fase (isto é checado **antes** da recompra de mão).
8. **Esvaziou a mão** → ver Seção 8.

---

## 8. Esvaziar a Mão (REGRA-CHAVE)

Sempre que a mão fica **vazia** após uma jogada (e a fase não terminou):
- O jogador **recompra 7 pedras do monte de graça** — **não custa rodada**.
- Anima "MÃO LIMPA! +mão grátis 🎉".
- Se tiver o joker **Mão Cheia**, cada esvaziada aumenta o Mult base em +1 (acumulado até o fim da fase).

> Este é o ciclo central do jogo. Manter as pedras fluindo e esvaziar a mão é a forma "limpa" de jogar; comprar do monte é a saída punida.

---

## 9. Gato por Lebre (blefe / jogar pedra que não encaixa)

Mecânica de risco para jogar uma pedra que **não encaixa** em nenhuma ponta.

- **Chance de sucesso:** **25%** de base. O joker **Mestre do Blefe** sobe para **50%** (limite de 100%).
- Ao escolher essa opção, o jogo mostra a pedra, a chance de "colar", o lado a colar (esquerda/direita) e avisa a penalidade da falha.
- **Sucesso:**
  - A pedra "cola" na ponta escolhida **mesmo sem encaixar** — e fica na **orientação original** (não é girada, diferente do encaixe normal).
  - A jogada é **pontuada** normalmente e os jokers de blefe entram (ex.: "Quem não arrisca não petisca" dá +2 Mult).
  - Anima "Colou! 🐱→🐇".
  - **Desbloqueia** o joker **Mestre do Blefe** (no 1º sucesso da sessão).
  - Pode vencer a fase ou esvaziar a mão como uma jogada normal.
- **Falha:**
  - **Perde METADE dos pontos da fase** (arredondando para baixo).
  - **Trava o Gato por Lebre pelo resto da fase** (não pode mais blefar até a próxima fase).
  - Anima "Pegou no flagra! −50% dos pontos 😿".
  - **Desbloqueia** o joker **Quem não arrisca não petisca** (na 1ª falha da sessão).

> **Desbloqueios persistem entre runs** (são progresso de sessão). Uma vez desbloqueados, os dois jokers de gato passam a poder aparecer no pool de recompensa pós-fase.

---

## 10. Comprar do Monte (punido)

- Disponível enquanto houver pedras no monte e rodadas restantes.
- **Custa 1 rodada** (vida): pega a próxima pedra do monte e adiciona à mão.
- Botão na UI: **"Comprar −1"** (o "−1" lembra o custo). Fica desabilitado quando não dá para comprar.

---

## 11. Travar, Vencer e Perder

### Sem jogada possível
Quando não há nenhuma pedra na mão que encaixe:
- Se ainda há monte **e** rodadas → mensagem orientando: "Sem encaixe! Compre do monte (−1 rodada) ou tente trocar gato por lebre (peça vermelha)." (o jogador precisa agir).
- Se acabaram as rodadas **ou** o monte está vazio → **derrota** ("Acabaram as rodadas!" ou "Monte vazio e sem encaixe!").

### Vitória de fase
- Disparada assim que os pontos atingem a meta (numa jogada normal ou num gato bem-sucedido).
- Mostra eventuais **desbloqueios** da fase e depois a **loja de recompensa** (Seção 14).

### Derrota / Fim da run
- Tela "🐴 Fim da run!" com o motivo e o quão longe chegou ("você chegou à fase X com Y/meta pontos") + botão **"Jogar de novo"**.

---

## 12. Jokers — LISTA COMPLETA (25)

Jokers são os modificadores que distorcem a pontuação. Cada um tem **nome**, **efeito** e a forma como entra na conta (ver a ordem na Seção 6). São **25** no total.

### 12.1 Jokers Globais (6) — recompensa pós-fase, valem a run inteira

| Nome | Efeito |
|---|---|
| **Cachaça** | +2 de Mult base. |
| **Carroça Dourada** | Jogar uma carroça (dupla) dá +3 Mult naquela jogada. |
| **Maré** | Cada pedra jogada vale +1 Ficha. |
| **Mão Cheia** | Toda vez que você esvazia a mão: +1 Mult na fase (acumulável). |
| **Filé da Rendeira** | Pedras com um 6 valem o dobro de Fichas. |
| **Jangada** | +1 rodada no início de cada fase. |

### 12.2 Jokers por Tipo de Pedra (14) — 2 para cada um dos 7 tipos
Aplicam-se quando a pedra **tem** aquele número em pelo menos uma metade.

| Tipo | Joker "+5" (soma Fichas) | Joker "em Dobro" (dobra o resultado) |
|---|---|---|
| Branco (0) | **+5 Branco** | **Branco em Dobro** |
| Piu (1) | **+5 Piu** | **Piu em Dobro** |
| Duque (2) | **+5 Duque** | **Duque em Dobro** |
| Terno (3) | **+5 Terno** | **Terno em Dobro** |
| Quadra (4) | **+5 Quadra** | **Quadra em Dobro** |
| Quina (5) | **+5 Quina** | **Quina em Dobro** |
| Sena (6) | **+5 Sena** | **Sena em Dobro** |

- **"+5 {Tipo}":** +5 Fichas se a pedra tem aquele número.
- **"{Tipo} em Dobro":** dobra o resultado (pontos) da jogada se a pedra tem aquele número.

### 12.3 Jokers do Gato por Lebre (2) — desbloqueáveis
Aparecem no pool de recompensa só **depois** de desbloqueados (ver Seção 9).

| Nome | Efeito |
|---|---|
| **Quem não arrisca não petisca** | Quando seu gato por lebre pontua: +2 de Mult naquela jogada. |
| **Mestre do Blefe** | Aumenta a chance do gato por lebre para 50%. |

### 12.4 Jokers de Efeito de Campo (3) — reagem ao estado das pontas

| Nome | Efeito | Quando |
|---|---|---|
| **Lá e Lô Premiado** | +10 pontos | a jogada **deixa** a mesa em lá e lô (estado **depois**). |
| **Bomba na Maré** | +5 de Mult | joga uma **bomba** (dupla) com a mesa **já** em lá e lô (estado **antes**). |
| **Embalo do Lá e Lô** | +5 pontos | joga **qualquer** peça com a mesa **já** em lá e lô (estado **antes**). |

### 12.5 Selos
A categoria **Selos** existe na UI (painel inferior direito), mas está **vazia** no protótipo atual (mostra "nenhum ainda"). É uma feature planejada — selos ficariam *na peça*, não no painel (ver `jokers.md`). **Para o MVP Unity, deixe a seção de selos como placeholder vazio.**

---

## 13. Limite de Jokers

- Há um **limite de 5 jokers** equipados ao mesmo tempo.
- Se você tenta adquirir um joker com o limite cheio, o jogo abre um aviso: você escolhe **remover um joker existente** para encaixar o novo, ou **descartar** a aquisição.

---

## 14. Recompensa Pós-Fase (sem dinheiro)

Ao vencer uma fase:
- **Não há economia/dinheiro.** Você escolhe **1 de 3 jokers grátis**.
- Os 3 são sorteados entre todos os jokers que você **ainda não possui** (incluindo os de gato, se já desbloqueados).
- Cada opção mostra nome + descrição + botão "Escolher". Há também um botão **"Pular ▶"** para seguir sem pegar nenhum.
- Se houver jokers **desbloqueados** durante a fase (via gato), aparece antes uma tela "🔓 Novo joker desbloqueado!" anunciando-os.
- Após escolher (ou pular), segue para a próxima fase.

---

## 15. Bosses (Chefes) — modificadores opcionais

Os bosses **não são fases fixas**; são **modificadores** que podem ser ligados (e combinados). Quando ativos, o painel do oponente troca de "A LENDA te observa…" para "👹 BOSS" listando os ativos.

| Boss | Efeito |
|---|---|
| **Caboclo d'Água** | **Mau-Olhado:** a **1ª pedra de cada mão não pontua** (ganho zerado). |
| **Comadre Florzinha** | **Mau-Olhado** (igual acima) **+** a meta da fase sobe **50%**. |
| **Duque Travado** | Pedras que têm um **Duque (2)** ficam **desabilitadas**: não podem ser jogadas nem contam como jogada possível (aparecem em cinza). |

> Caboclo e Florzinha compartilham o mesmo Mau-Olhado, então ativar os dois juntos não dobra o efeito de zerar — apenas zera a 1ª pedra da mão.


## 16. Resumo de Números-Chave (cola rápida)

| Mecânica | Valor |
|---|---|
| Pedras no baralho | 28 (duplo-6) |
| Tamanho da mão | 7 |
| Rodadas (vidas) por fase | 3 (+1 com Jangada) |
| Limite de jokers | 5 |
| Meta da fase i | arredondar(40 × 1,6^(i−1)) → 40, 64, 102, 164, 262, 419 |
| Meta com Comadre Florzinha | × 1,5 |
| Chance base do Gato por Lebre | 25% |
| Mestre do Blefe | sobe para 50% |
| Falha do gato | perde metade dos pontos + trava o gato na fase |
| Esvaziar a mão | recompra 7 pedras, sem custo de rodada |
| Comprar do monte | −1 rodada |
| Cachaça | +2 Mult base |
| Carroça Dourada | +3 Mult em carroça (dupla) |
| Bomba na Maré | +5 Mult (dupla + mesa já em lá e lô) |
| Quem não arrisca não petisca | +2 Mult na jogada de gato |
| Maré | +1 Ficha por pedra |
| Filé da Rendeira | ×2 Fichas se a pedra tem 6 |
| +5 {Tipo} | +5 Fichas se a pedra tem o tipo |
| {Tipo} em Dobro | ×2 no resultado se a pedra tem o tipo |
| Lá e Lô Premiado | +10 pontos (a jogada deixou em lá e lô) |
| Embalo do Lá e Lô | +5 pontos (mesa já estava em lá e lô) |
| Mão Cheia | +1 Mult base por mão esvaziada (na fase) |

---

*Documento de mecânicas do Burrinho Royale para replicação em Unity. Para jokers sugeridos/futuros e ideias de selos, ver `jokers.md`.*
</content>
