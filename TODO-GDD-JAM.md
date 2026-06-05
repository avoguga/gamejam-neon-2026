# ✅ TODO List — GDD de Game Jam (One-Page Design Doc)

> **Filosofia:** num jam, o GDD é uma **bússola, não uma bíblia**. Escreva em **30–45 min** logo depois do tema cair, em **1 página**. Se algo não cabe numa página, está fora de escopo. Ele existe pra alinhar o time e te impedir de adicionar coisa no meio do caminho.

**Regra de ouro:** preencha de cima pra baixo. Se travar em qualquer item por mais de 5 min, escolha a opção mais simples e siga.

---

## 🎯 Bloco 1 — Conceito (o coração) — *10 min*
- [ ] **Pitch em 1 frase** — *"É um jogo onde você ___."* (o verbo central tem que ser interessante sozinho)
- [ ] **Como conecta com o TEMA** — 1 linha. (Teste: se contam o tema depois de jogar, a ligação é óbvia e esperta?)
- [ ] **Gênero** — puzzle / arcade / plataforma / narrativa / ritmo / etc.
- [ ] **Fantasia/emoção central** — o que o jogador deve *sentir*? (esperto, poderoso, tenso, encantado…)
- [ ] **Referência rápida** — "é tipo X com uma pitada de Y"

## ⚙️ Bloco 2 — Mecânica central (UMA só) — *10 min*
- [ ] **O verbo principal** — a ação que o jogador repete (pular, atirar, encolher, conectar…)
- [ ] **O twist** — a tensão/reviravolta que torna o verbo interessante
- [ ] **Core loop** — o ciclo de 10–30s: *ação → consequência → recompensa → repete*
- [ ] **Condição de vitória** — como se ganha/avança
- [ ] **Condição de derrota** — como se perde (ou "não tem derrota, é score-attack")
- [ ] **Controles** — mapeados em 1 linha (ex.: WASD mover, mouse mirar, espaço pular)

## 📐 Bloco 3 — Escopo: MVP / Bom-ter / CORTADO — *10 min*
> O bloco mais importante. Seja honesto e brutal.
- [ ] **MVP (obrigatório)** — a menor versão que é divertida E on-theme. Lista de 3–6 itens.
- [ ] **Bom-ter (se sobrar tempo)** — o que entra só depois do MVP funcionar
- [ ] **CORTADO (não faça)** — escreva o que você está *deliberadamente* deixando de fora (multiplayer, save, mais fases, história longa…)
- [ ] **Quantidade de conteúdo** — quantas fases/inimigos/níveis no mínimo? (poucos e bem feitos)

## 🎨 Bloco 4 — Direção de arte e áudio — *5 min*
- [ ] **Estilo visual** — pixel art / vetorial flat / minimalista (algo coeso e viável no tempo)
- [ ] **Paleta** — link de uma paleta pronta (ex.: Lospec, 8–16 cores)
- [ ] **Lista mínima de assets** — só o essencial pra jogar (player, 1–2 inimigos, tileset, UI)
- [ ] **Áudio** — música (1 faixa loop) + SFX das ações-chave (pular/atirar/acertar/UI). Fonte: Bfxr/Freesound.
- [ ] **Juice planejado** — screenshake? partículas? hitstop? squash & stretch? (escolha 2–3)

## 👥 Bloco 5 — Time, ferramentas e logística — *5 min*
- [ ] **Engine** — a que o time domina (Godot/Unity/GameMaker)
- [ ] **Papéis** — quem faz código / arte / áudio / design / lead (quem decide)
- [ ] **Ferramentas e repositório** — Git/itch, ferramentas de arte/áudio definidas
- [ ] **Plataforma de export** — **build no navegador (HTML5/WebGL)** como alvo principal
- [ ] **Pipeline de build testado** — confirme que exporta e roda no browser ANTES de produzir conteúdo

## 📅 Bloco 6 — Cronograma e marcos — *5 min*
- [ ] **Marco 1 — Protótipo "fun-first"** (core jogável com placeholders) — *data/hora*
- [ ] **Checkpoint:** *o loop é divertido?* Se não → **pivote agora**
- [ ] **Marco 2 — Vertical slice** (um loop completo de ponta a ponta) — *data/hora*
- [ ] **Marco 3 — Alpha + 1º playtest** (conteúdo dentro, testado com gente) — *data/hora*
- [ ] **Marco 4 — FEATURE FREEZE** (para de adicionar; só polish/bug) — *data/hora* (deixe ~25–30% do tempo aqui)
- [ ] **Marco 5 — Build final + envio** com buffer de 2–4h — *data/hora*

## 📤 Bloco 7 — Checklist de envio (preencher no fim) — *referência*
- [ ] Build web zipado e **testado no itch.io** (não só localmente)
- [ ] **GIF de capa** animado (~10s, <3 MB) + 1º frame como thumbnail
- [ ] 3–5 screenshots de gameplay real
- [ ] Descrição: hook + interpretação do tema + **controles** + créditos/atribuições
- [ ] Tags e gênero corretos
- [ ] Enviado **antes** do prazo (com folga)
- [ ] Avaliar/comentar outras entradas (pra ganhar votos de volta)

---

## 🧩 Template em branco (copie e preencha)

```
# [NOME DO JOGO] — GDD de Jam
Jam/Tema: ______________________  |  Prazo: ______

PITCH (1 frase): _________________________________________
Conexão com o tema: ______________________________________
Gênero: ________  |  Emoção central: ________  |  Tipo "X com Y": ________

MECÂNICA CENTRAL
- Verbo: ________________   Twist: ________________
- Core loop (10–30s): _____________________________
- Vitória: ____________   Derrota: ____________
- Controles: __________________________________

ESCOPO
- MVP: 1)____ 2)____ 3)____ 4)____
- Bom-ter: ________________________
- CORTADO (não fazer): ____________________________
- Conteúdo mínimo: ____ fases / ____ inimigos

ARTE & ÁUDIO
- Estilo: ________  Paleta(link): ________
- Assets mínimos: ________________________________
- Música: ____  SFX: ____  Juice: ________________

TIME & FERRAMENTAS
- Engine: ______  Export: Web/HTML5
- Papéis: Código:____ Arte:____ Áudio:____ Lead:____

CRONOGRAMA
- Protótipo fun: ____  Vertical slice: ____
- Alpha+playtest: ____  FEATURE FREEZE: ____  Envio: ____
```

---

### ⏱️ Resumo do tempo de preenchimento
| Bloco | Tempo |
|---|---|
| 1. Conceito | 10 min |
| 2. Mecânica | 10 min |
| 3. Escopo | 10 min |
| 4. Arte/Áudio | 5 min |
| 5. Time/Ferramentas | 5 min |
| 6. Cronograma | 5 min |
| **Total** | **~45 min** |

> Depois de preencher: **cole numa parede/Discord pinado**, e a cada decisão pergunte *"isso está no MVP ou no CORTADO?"*. Esse doc é seu escudo contra o overscoping — o assassino nº 1 de jogos de jam.
