# 🃏 Jokers do Burrinho Royale — Lista atual + Sugestões

> Documento de referência. **Parte 1** lista tudo que já existe no jogo hoje (`mocks_v2_layout-mesa.html`). **Parte 2** traz sugestões de novos jokers, baseadas em jogos parecidos (Balatro, Dominoir, Dominova) adaptadas pro nosso dominó com tempero alagoano.
>
> Lembrete do sistema de pontuação atual: **Pontos = Fichas (soma dos pontinhos da peça) × Mult**. "Fichas" = chips. Jokers podem mexer em **fichas (+flat)**, **mult (+aditivo)** ou **multiplicar o resultado (×)**.

---

## PARTE 1 — Jokers que já existem

### 1.1 Jokers de Efeito Global (recompensa pós-fase)
Antes eram "Poderes da Loja". **Não existe mais dinheiro:** ao fim de cada fase você escolhe **1 de 3 jokers grátis**. Ficam a run inteira. Definidos em `ALL_POWERS` (todos com `kind:"power"` — agora contam como jokers).

| Nome | Efeito | Tipo de efeito |
|---|---|---|
| **Cachaça** | +2 de Mult base | +Mult (permanente) |
| **Carroça Dourada** | Jogar uma carroça (dupla) dá +3 Mult naquela jogada | +Mult condicional |
| **Maré** | Cada pedra jogada vale +1 Ficha | +Fichas |
| **Mão Cheia** | Toda vez que você esvazia a mão: +1 Mult na fase | +Mult escalável |
| **Filé da Rendeira** | Pedras com um 6 valem o dobro de Fichas | ×Fichas condicional |
| **Jangada** | +1 rodada no início de cada fase | Utilidade (vidas) |

### 1.2 Jokers por Tipo de Pedra (adicionados via debug — tecla **F**)
14 jokers, 2 para cada tipo. Aplicam se a peça **tiver** aquele número em **pelo menos uma** das metades. Definidos em `TIPO_JOKERS` (gerados a partir do array `TIPOS`).

Tipos: **Branco (0) · Piu (1) · Duque (2) · Terno (3) · Quadra (4) · Quina (5) · Sena (6)**

| Tipo | Joker "+5" (kind: add) | Joker "Dobro" (kind: mult) |
|---|---|---|
| Branco (0) | **+5 Branco** — +5 fichas se a peça tiver 0 (branco) | **Branco em Dobro** — dobra os pontos se a peça tiver 0 (branco) |
| Piu (1) | **+5 Piu** — +5 fichas se a peça tiver 1 | **Piu em Dobro** — dobra os pontos se a peça tiver 1 |
| Duque (2) | **+5 Duque** | **Duque em Dobro** |
| Terno (3) | **+5 Terno** | **Terno em Dobro** |
| Quadra (4) | **+5 Quadra** | **Quadra em Dobro** |
| Quina (5) | **+5 Quina** | **Quina em Dobro** |
| Sena (6) | **+5 Sena** | **Sena em Dobro** |

### 1.3 Jokers do Gato por Lebre (desbloqueados no 1º resultado de gato)
2 jokers especiais ligados à mecânica de "gato por lebre" (jogar peça que não encaixa). Desbloqueiam quando você tem o primeiro resultado de gato. Definidos em `GATO_JOKERS`.

| Nome | Efeito | Tipo de efeito |
|---|---|---|
| **Quem não arrisca não petisca** | Quando seu gato por lebre pontua: +2 de Mult naquela jogada | +Mult condicional (`gatoMult`) |
| **Mestre do Blefe** | Aumenta a chance do gato por lebre para 50% | Utilidade (`gatoBonus`) |

### 1.4 Jokers de Efeito de Campo (reagem ao estado da mesa)
Reagem ao estado das **pontas abertas** no momento da jogada. Definidos em `CAMPO_JOKERS`.

- **lá e lô** = as duas pontas abertas têm o **mesmo número** (`isLaELo()` → `pontaEsq() === pontaDir()`).
- **bomba** = carroça / peça dupla (`isDouble()`).

| Nome | Efeito | Quando | Tipo de efeito |
|---|---|---|---|
| **Lá e Lô Premiado** | +10 pontos | A jogada **deixa** a mesa em lá e lô (estado *depois*) | +Pontos (flat) |
| **Bomba na Maré** | +5 de Mult | Joga uma **bomba** com a mesa **já** em lá e lô (estado *antes*) | +Mult condicional |
| **Embalo do Lá e Lô** | +5 pontos | Joga **qualquer** peça com a mesa **já** em lá e lô (estado *antes*) | +Pontos (flat) |

> Nota: "pontos" aqui é bônus **flat no resultado final** da jogada (somado depois de `fichas × mult`). O Mau-Olhado dos chefes zera a jogada inteira, inclusive esses bônus.

> Total atual: **6 jokers globais + 14 jokers de tipo + 3 jokers de campo + 2 jokers do gato = 25 jokers**. Todos aparecem no modal de debug (tecla **F**) e no pool de recompensa pós-fase.
>
> **Selos:** a categoria de Selos está **vazia** por enquanto — selos ficam *na peça*, não no array de jokers (ver seção 2.8). O painel "Selos" do jogo aparece sem itens.

---

## PARTE 2 — Sugestões de novos jokers

Pesquisa de base: **Balatro** (categorias de joker: +Chips, +Mult, ×Mult, *retrigger*, economia, condicionais) e **Dominoir / Dominova** (Balatro com dominó — usam Score = Pips × Mult, modificadores por peça tipo *Polychrome/Steel/Gold*, artefatos com sinergias, e consumíveis que alteram peças). As ideias abaixo traduzem esses padrões pro nosso jogo.

> Convenção sugerida pra balancear: **×Mult** é o efeito mais forte (deixar raro/caro), **+Mult** médio, **+Fichas** o mais comum/barato. *Retrigger* é poderoso porque reativa todos os outros efeitos.

### 2.1 ×Mult — os "carros-chefe" (raros e caros)
O tipo mais forte: multiplicam o Mult, então escalam exponencialmente.

- **Caboclo d'Água** — ×Mult cresce conforme o nº de peças já na mesa (ex: a cada 5 peças jogadas, +0,5× no Mult).
- **Sururu Premiado** — a cada mão esvaziada na fase, ganha +0,2× permanente nesta fase (sinergia com a regra-chave de esvaziar a mão).
- **Lampião** — ×3 Mult, mas −1 rodada no início da fase (alto risco/recompensa, à la Buckshot).
- **Pôr do Sol da Ponta Verde** — ×Mult igual ao nº de rodadas que você ainda tem (jogue seguro = score alto).

### 2.2 +Mult condicional (médios)
- **Coco de Roda** — peças com pontinhos iguais nas duas metades que NÃO sejam carroça… (ou: +2 Mult se a peça encaixar na ponta esquerda).
- **Frevo** — +1 Mult por peça jogada em sequência sem comprar (zera se comprar do monte).
- **Mestre Sala** — +4 Mult na primeira peça de cada mão (anti-sinergia com o chefe Mau-Olhado, vira escolha).
- **Maré Cheia** — +Mult igual à quantidade de peças na sua mão (premia segurar peças).

### 2.3 +Fichas (comuns/baratos)
- **Pescaria** — +3 fichas por peça que contenha um 0 (branco/"pé").
- **Tapioca** — +10 fichas na última peça da mão (a que esvazia).
- **Caranguejo** — peças que encaixam na ponta direita dão +4 fichas.
- **Feira de Maceió** — +1 ficha por $ que você tem (escala com economia).

### 2.4 Retrigger (reativam efeitos — poderosos)
- **Eco da Lagoa** — a primeira carroça (dupla) de cada mão pontua duas vezes.
- **Comadre Florzinha** — a cada 3 peças jogadas, a próxima pontua duas vezes.
- **Berra-Boi** — peças com Sena (6) são pontuadas duas vezes (combo absurdo com os jokers de Sena).

### 2.5 Economia (geram $ pra loja)
- **Rendeira de Filé** — ganha $1 cada vez que esvazia a mão.
- **Cofre de Búzios** — no fim da fase, ganha $1 a cada 2 rodadas que sobraram.
- **Cambista** — peças carroça dão +$1 quando jogadas (máx. por fase).

### 2.6 Utilidade / quebra de regra (mudam como você joga)
- **Bússola do Jangadeiro** — uma vez por mão, comprar do monte NÃO custa rodada.
- **Vento Sul** — você pode jogar em qualquer ponta ignorando o encaixe 1×/fase (peça "coringa").
- **Rede de Pesca** — aumenta a mão inicial de 7 para 8 peças.
- **Lua Cheia** — vê o topo do monte (próxima peça a ser comprada).
- **Cordel da Sorte** — no início da fase, transforma 1 peça aleatória da mão numa carroça.

### 2.7 Sinergia com a regra-chave (esvaziar a mão)
Nosso diferencial é o ciclo "esvaziou a mão → mão grátis". Jokers que premiam isso dão identidade:
- **Mão de Vento** — esvaziar a mão dá +5 fichas base permanentes na fase.
- **Ciranda** — cada esvaziada seguida (sem perder rodada no meio) aumenta o bônus: +1×, +2×, +3×…
- **Quebra-Mar** — se esvaziar a mão 3× na mesma fase, ×2 Mult até o fim da fase.

### 2.8 Ideias para "Selos" (a seção de baixo do painel, ainda vazia)
Selos ficam **na peça**, não na mesa (modelo Balatro/Dominoir *Gold/Steel/Polychrome*). Ficam pra fase 2 do projeto, mas registrando:
- **Selo de Ouro** — esta peça dá +4 fichas quando jogada.
- **Selo de Sururu** — ao jogar, devolve uma peça aleatória pro monte e compra outra.
- **Selo Vermelho** — esta peça pontua duas vezes (retrigger local).
- **Selo de Maré** — vale dobro se for a última da mão.

---

## Notas de balanceamento (pra jam)
- Comece com **poucos jokers fortes** e muitos fracos — Balatro funciona porque ×Mult é raro.
- Cuidado com loops infinitos: jokers de **economia + esvaziar mão** podem disparar combos sem teto. Teste com o botão **F**.
- Os **jokers de tipo** (Parte 1.2) já cobrem a base "+Fichas / ×Pontos". As sugestões da Parte 2 adicionam as outras categorias do Balatro (retrigger, economia, utilidade, escala) que hoje faltam.

---

## Fontes pesquisadas
- [Jokers — Balatro Wiki (Fandom)](https://balatrogame.fandom.com/wiki/Jokers)
- [Jokers — Balatro Wiki (balatrowiki.org)](https://balatrowiki.org/w/Jokers)
- [Guide: Activation Sequence — Balatro Wiki](https://balatrogame.fandom.com/wiki/Guide:_Activation_Sequence)
- [Dominoir (Balatro com dominó) — itch.io](https://kawakubo.itch.io/dominoir)
- [I tried every Balatro-like game in Next Fest (cita Dominova)](https://nosmallgames.com/2025/06/i-tried-every-balatro-like-game-i-could-find-in-steam-next-fest-again/)
