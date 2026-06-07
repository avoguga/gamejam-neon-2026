# 🎓 Tutorial do Burrinho Royale — Guia Passo a Passo

> Guia **só do tutorial**: como ele funciona e como reproduzir exatamente o tutorial roteirizado que já existe no protótipo. O tutorial é uma **fase encenada** (mão fixa, baralho controlado, sucesso garantido) que ensina o básico do dominó e as 4 mecânicas-chave do jogo: **encaixar metades**, **comprar do monte**, **gato por lebre** e **esvaziar a mão**. Ao terminar, ele entrega o jogador na partida normal.

---

## 1. Como o tutorial entra e sai

- **Roda 1× ao abrir o jogo.** Ao iniciar, o tutorial assume o controle: substitui a mão, zera o baralho/mesa e mostra a primeira fala.
- **É uma fase fabricada, não a fase 1 real.** Nada do que acontece nele conta para a run de verdade (não desbloqueia jokers, não usa o baralho completo, não rola aleatoriedade).
- **No fim** abre a tela *"✅ Fase concluída!"* com dois botões:
  - **"Ir para o jogo ▶"** → encerra o tutorial e começa a **partida normal** (mão nova, baralho completo, regras reais).
  - **"Rever tutorial"** → reinicia o tutorial do passo 0.
- **Sucesso é garantido o tempo todo.** O jogador não tem como perder, falhar o gato ou ficar travado. O roteiro só destrava a próxima ação quando a atual é feita.

---

## 2. Estado inicial (montar antes do passo 0)

Ao começar o tutorial, prepare a cena exatamente assim:

| Item | Valor no tutorial |
|---|---|
| **Mão (5 pedras, nesta ordem)** | `3/3` · `3/5` · `5/4` · `0/0` · `1/0` |
| **Mesa (board)** | vazia |
| **Monte** | vazio (a única compra é forçada e entrega uma peça fixa) |
| **Rodadas (vidas)** | **1** |
| **Pontos** | 0 |
| **Meta** | 0 (só aparece no último passo) |
| **Jokers / bônus** | nenhum |

> A mão tem só 5 pedras (a partida normal usa 7). É de propósito: o roteiro depende dessas peças específicas.

---

## 3. Legenda visual das pedras (vale em todos os passos)

O tutorial pinta cada pedra para guiar o clique. Replique essas 4 aparências:

| Aparência | Significado | Estilo de referência |
|---|---|---|
| 🔵 **Contorno azul + brilho** | Pedra **jogável / recomendada** agora — clique para jogar | borda azul `#2196f3` com glow |
| 🔴 **Contorno vermelho** | Pedra de **gato por lebre** (não encaixa; joga blefando) | borda vermelha `#d34b45` |
| ⬜ **Esmaecida (40%)** | Pedra **travada** neste passo — clicar não faz nada (ou avisa "Bloqueado!") | opacidade reduzida |
| ▫️ **Normal** | Sem destaque especial | — |

A **fala do personagem** aparece no topo da mesa a cada passo. O botão **"Comprar 1"** fica **desabilitado** em todos os passos, exceto no passo da compra (passo 3).

---

## 4. Os 7 passos (com as peças corretas)

Cada passo tem: a **fala**, o que fica **destacado**, a **ação do jogador** e o que **acontece/avança**.

### Passo 0 — Jogue a primeira pedra
- **Fala:** *"Opa, ta familiarizado com dominó? Não? Eu em... Vamos lá. Primeiro jogue uma das pedras em sua mão, vamos começar com essa."*
- **Destaque:** só a **`3/5`** fica 🔵 azul. As outras 4 ficam ⬜ esmaecidas.
- **Ação:** clicar na **`3/5`**.
- **Resultado:** como a mesa está vazia, a pedra é colocada no centro. **Mesa: `[3|5]`** (pontas abertas = **3** e **5**). → avança para o passo 1.

### Passo 1 — Ligue metades correspondentes
- **Fala:** *"Certo! Note como cada pedra contem 2 numeros... Agora vamos ligar essas metades com outras pedras com metades correspondentes."*
- **Destaque:** ficam 🔵 azuis as **duas** que encaixam nas pontas: **`3/3`** (liga no 3) e **`5/4`** (liga no 5). `0/0` e `1/0` ficam ⬜ esmaecidas.
- **Ação:** clicar em **`3/3`** *ou* **`5/4`** (qualquer uma das duas).
- **Resultado:** a pedra encaixa na ponta certa. → avança para o passo 2.

### Passo 2 — Faça a próxima jogada (encaixe livre)
- **Fala:** *"Ok... Você ta pegando o jeito, agora faz a próxima jogada."*
- **Destaque:** qualquer pedra da mão que **encaixe** numa ponta fica 🔵 azul (a que sobrou entre `3/3`/`5/4`). As que não encaixam (`0/0`, `1/0`) ficam ⬜ esmaecidas.
- **Bloqueio:** se o jogador clicar numa pedra que não encaixa, mostra o aviso **"Bloqueado!"** e nada acontece.
- **Ação:** jogar a pedra azul que encaixa.
- **Resultado:** mão fica com **`0/0`** e **`1/0`**, que **não encaixam** em nenhuma ponta. → avança para o passo 3.

### Passo 3 — Compre do monte
- **Fala:** *"Oh... Veja, estamos sem opções, hm... Certo, vamos comprar do monte! Comprar do monte custa uma rodada, quando suas rodadas chegam a zero, caso você não tenha mais opções para jogar, você perde! Vamos ver o que vem..."*
- **Destaque:** todas as pedras da mão ficam ⬜ esmaecidas; o único controle ativo é o botão **"Comprar 1"** (habilitado só neste passo).
- **Ação:** clicar em **"Comprar 1"**.
- **Resultado:** entra a pedra **fixa `1/1`** na mão **e as rodadas caem de 1 → 0** (a compra custa 1 rodada). Mão agora: `0/0`, `1/0`, `1/1`. → avança para o passo 4.

> Detalhe importante de roteiro: a peça comprada é **sempre a `1/1`** (não é aleatória) e a rodada chega a 0 de propósito, para preparar o "tudo ou nada" do próximo passo.

### Passo 4 — Gato por Lebre (tudo ou nada)
- **Fala:** *"Ok, agora é tudo ou nada! Vamos tentar blefar, ou como meu voinho diria, trocar gato por lebre."*
- **Destaque:** as pedras de blefe **`0/0`** e **`1/1`** ficam 🔴 vermelhas (são as marcadas como gato). As demais ficam ⬜ esmaecidas/bloqueadas.
- **Ação:** clicar numa pedra 🔴 vermelha (`0/0` ou `1/1`) → abre o **modal do gato**, que pede para escolher a ponta (**◀ Esquerda** / **Direita ▶**). Escolher um lado.
- **Resultado:** no tutorial o gato **sempre cola** (sucesso garantido, sem rolar dado e sem desbloquear joker). A pedra "gruda" na ponta escolhida e aparece **"Colou! 🐱→🐇"**. → avança para o passo 5.

> No jogo normal o gato é arriscado (chance de falhar, perde metade dos pontos e trava). **No tutorial isso é desligado** — é só para ensinar o gesto.

### Passo 5 — Esvazie a mão (a mecânica-chave)
- **Fala:** *"UOU! ISSO FOI DO BARALHO! Agora vamos esvaziar nossa mão. Sempre que esvaziamos nossa mão, compramos do monte sem gastar rodadas!"*
- **Destaque:** as pedras que **encaixam** ficam 🔵 azuis; clicar em pedra que não encaixa mostra **"Bloqueado!"**.
- **Ação:** ir jogando as pedras que encaixam **até a mão ficar vazia** (o passo **não avança** enquanto sobrar pedra — cada jogada válida mantém você aqui).
- **Resultado:** quando a **última** pedra sai e a mão zera, aparece **"MÃO LIMPA! Compra grátis 🎉"**. → após um instante, avança para o passo 6.

> É aqui que se ensina a identidade do jogo: **esvaziar a mão dá uma mão nova de graça, sem custar rodada.**

### Passo 6 — A Meta (concluir a fase)
- **Preparação automática deste passo (setup):** a cena é reconfigurada para deixar a vitória a um clique:
  - **Meta = 27**, **Pontos = 26** (falta só 1 ponto).
  - A mão é **trocada** por três pedras: **`6/6`**, **`3/2`**, **`4/1`**.
- **Fala:** *"Ufa, limpamos a mão, mas opa! Notou aquela meta ali? Quando superamos a meta, a fase é concluida, vamos tentar completar ela com o que fizemos até agora!"*
- **Destaque:** pedras que **encaixam** numa ponta ficam 🔵 azuis; pedras que **não encaixam** ficam 🔴 vermelhas (dá para concluir tanto encaixando quanto blefando — qualquer caminho vence).
- **Ação:** clicar em **qualquer** pedra.
  - Se **encaixa** → é jogada normalmente.
  - Se **não encaixa** → abre o gato (sucesso garantido).
- **Resultado:** soma os pontos da jogada aos 26; se ainda faltar, o placar é **forçado** a bater a meta (a vitória é garantida). Aparece **"FASE CONCLUÍDA! 🎉"** e, depois de ~1s, abre a tela de fim.

---

## 5. Tela de fim do tutorial

Quando a fase encenada é concluída, abre o overlay:

- **Título:** *"✅ Fase concluída!"*
- **Texto:** *"Mandou bem — você já pegou o básico do dominó."*
- **Nota (itálico, menor):** *"A próxima parte do tutorial será sobre os Jokers."*
- **Botões:**
  - **"Ir para o jogo ▶"** → fecha o tutorial e inicia a **partida normal**.
  - **"Rever tutorial"** → reinicia tudo do passo 0.

---

## 6. Resumo das peças do tutorial (cola rápida)

| Passo | Mão / evento | Peça(s) certa(s) | Ação |
|---|---|---|---|
| **Início** | mão fixa | `3/3` `3/5` `5/4` `0/0` `1/0` | — |
| **0** | jogar a 1ª | 🔵 `3/5` | clica `3/5` |
| **1** | ligar metades | 🔵 `3/3` e 🔵 `5/4` | clica uma das duas |
| **2** | próxima jogada | 🔵 a que sobrou (`3/3`/`5/4`) | clica a azul |
| **3** | comprar | botão **Comprar 1** | compra → entra `1/1`, rodada 1→0 |
| **4** | gato por lebre | 🔴 `0/0` e 🔴 `1/1` | clica vermelha → escolhe ponta |
| **5** | esvaziar a mão | 🔵 as que encaixam | joga até zerar → "Compra grátis" |
| **6** | meta | mão vira `6/6` `3/2` `4/1` (meta 27 / pontos 26) | clica qualquer → "Fase concluída" |

---

## 7. Regras especiais que só valem no tutorial (não esquecer ao implementar)

1. **Baralho controlado:** a única compra entrega a peça fixa **`1/1`** (sem aleatoriedade).
2. **Gato sempre cola:** sem rolar chance, sem perda de pontos, sem trava, sem desbloqueio de joker.
3. **Vitória garantida no passo da meta:** se a jogada não bater os 27, o placar é forçado até a meta.
4. **Cliques são "trilho":** só a(s) peça(s) certa(s) do passo respondem; clique fora mostra "Bloqueado!" e o passo não avança.
5. **Comprar só no passo 3:** o botão de compra fica desabilitado em todos os outros passos.
6. **Sem jokers/bônus/chefes** durante o tutorial — é dominó puro mais as 4 mecânicas ensinadas.
