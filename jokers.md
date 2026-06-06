# 🃏 Jokers do Burrinho Royale — Lista atual + Sugestões

> Documento de referência. **Parte 1** lista tudo que já existe no jogo hoje (`mocks_v2_layout-mesa.html`). **Parte 2** traz sugestões de novos jokers, baseadas em jogos parecidos (Balatro, Dominoir, Dominova) adaptadas pro nosso dominó com tempero alagoano.
>
> Lembrete do sistema de pontuação atual: **Pontos = Fichas (soma dos pontinhos da peça) × Mult**. "Fichas" = chips. Jokers podem mexer em **fichas (+flat)**, **mult (+aditivo)** ou **multiplicar o resultado (×)**.

---

## PARTE 1 — Jokers que já existem

### 1.1 Poderes da Loja (aparecem depois da fase, na tela de loja)
Ficam a run inteira (máx. 5). Definidos em `ALL_POWERS`.

| Nome | Efeito | Preço | Tipo de efeito |
|---|---|---|---|
| **Cachaça** | +2 de Mult base | $5 | +Mult (permanente) |
| **Carroça Dourada** | Jogar uma carroça (dupla) dá +3 Mult naquela jogada | $5 | +Mult condicional |
| **Maré** | Cada pedra jogada vale +1 Ficha | $4 | +Fichas |
| **Mão Cheia** | Toda vez que você esvazia a mão: +1 Mult na fase | $6 | +Mult escalável |
| **Filé da Rendeira** | Pedras com um 6 valem o dobro de Fichas | $6 | ×Fichas condicional |
| **Jangada** | +1 rodada no início de cada fase | $5 | Utilidade (vidas) |

### 1.2 Jokers por Tipo de Pedra (adicionados via debug — tecla **F**)
12 jokers, 2 para cada tipo. Aplicam se a peça **tiver** aquele número em **pelo menos uma** das metades. Definidos em `TIPO_JOKERS`.

Tipos: **Piu (1) · Duque (2) · Terno (3) · Quadra (4) · Quina (5) · Sena (6)**

| Tipo | Joker "+5" (kind: add) | Joker "Dobro" (kind: mult) |
|---|---|---|
| Piu (1) | **+5 Piu** — +5 fichas se a peça tiver 1 | **Piu em Dobro** — dobra os pontos se a peça tiver 1 |
| Duque (2) | **+5 Duque** | **Duque em Dobro** |
| Terno (3) | **+5 Terno** | **Terno em Dobro** |
| Quadra (4) | **+5 Quadra** | **Quadra em Dobro** |
| Quina (5) | **+5 Quina** | **Quina em Dobro** |
| Sena (6) | **+5 Sena** | **Sena em Dobro** |

> Total atual: **6 poderes de loja + 12 jokers de tipo = 18 jokers**.

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
