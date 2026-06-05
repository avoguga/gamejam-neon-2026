# 🎮 Relatório: Como Vencer Game Jams — Estilo, Mecânicas e Passo a Passo

> Pesquisa elaborada com base em recaps oficiais do GMTK (Mark Brown), dados de votação do Ludum Dare, resultados do Brackeys, Pirate Software Jam e guias da comunidade (2023–2026). Fontes citadas ao longo do documento.

---

## 📌 Resumo executivo — A fórmula vencedora

Um jogo que vence game jam quase sempre tem:

1. **UMA mecânica central** com uma tensão/twist interessante, **lapidada até ser gostosa de jogar** (juice: screenshake, partículas, hitstop, SFX, restart instantâneo, controles responsivos).
2. **Interpretação do tema esperta, mas legível** — um passo "lateral" da leitura óbvia, mas ainda reconhecível na hora (pra pontuar na categoria Tema).
3. **Visual 2D coeso com paleta limitada** (pixel art ou vetorial flat), escolhido para ser viável no tempo e **bonito em um GIF de capa**.
4. **Completo** — com estados reais de vitória/derrota — **e polido** ("absurdamente polido para 4 dias" é a régua).
5. **Sem fricção para acessar e avaliar** — **build no navegador (HTML5/WebGL)**, gameplay imediato, controles intuitivos, dificuldade que favorece o jogador.
6. Pontuando em **todos os eixos de avaliação** (Tema, Inovação, Diversão, Gráficos, **Áudio**), porque vencedores são decididos pela média entre categorias.

A frase-síntese do Mark Brown (GMTK): *"faça eles sorrirem, faça eles rirem, e faça seu jogo tão frenético que não dá nem tempo de pensar em parar."*

---

## 🧠 Como os vencedores são realmente escolhidos (isso explica tudo)

Entender a votação explica todos os padrões abaixo.

- **Ludum Dare** — avaliado pelos participantes em **9 categorias**: inovação, diversão, tema, gráficos, áudio, humor, mood, geral e comunidade. Nota = média de 1–5 ao longo de ~3 semanas.
- **Brackeys Game Jam** — em 2025.2 avaliou em **Overall, Enjoyment, Gameplay, Innovation, Theme, Visuals, Audio**. Teve **2.274 jogos e 42.431 avaliações**.
- **GMTK Game Jam** — votação da comunidade (grande demais para um juiz). **2024 ("Built to Scale")**: 7.600 jogos / 32.000 designers. **2025 ("Loop")**: 9.600+ jogos / 37.000+ participantes.

**Implicação-chave:** quem vota são **outros jammers jogando centenas de entradas rapidinho**. Por isso você precisa: (a) **encaixar no tema visivelmente**, (b) **causar boa primeira impressão rápido**, (c) **ser fácil de acessar e jogar**, (d) **pontuar em todo eixo** — um jogo sem áudio ou sem ligação com o tema já tem o teto de nota cortado.

---

## 🎨 1. Estilos de arte que vencem (e por quê)

**Padrão dominante: 2D estilizado — quase sempre pixel art ou minimalista/vetorial flat.** Uma análise de vencedores consecutivos do Ludum Dare concluiu que **"todos os jogos vencedores são 2D"** porque: é mais simples de fazer, **fica bonito com menos esforço**, há muitos frameworks prontos e existe um **bônus de nostalgia**.

**Por que a arte importa:**
1. **Primeira impressão = voto.** Antes de apertar "Play", o jogador já decidiu pela capa/GIF e primeiro frame.
2. **Coesão vence volume.** Orientação oficial do itch.io: *"pequenos toques pensados são muito melhores do que muitos assets variados de baixa qualidade."* Táticas práticas: limite a **8–16 cores de uma paleta pronta (Lospec)**, adicione **textura/grain** (2 minutos já elevam a qualidade percebida), use **regra dos terços** e faça um **GIF de capa animado (<3 MB)**.
3. **Minimalismo serve puzzle/estratégia; pixel art serve arcade/plataforma.** A arte deve **apoiar a mecânica**, não competir com ela.

**Conclusão:** você quase nunca vence com 3D low-poly ou realismo num fim de semana. Vence com um **visual 2D enxuto e coeso** que lê na hora e fica ótimo num GIF.

---

## ⚙️ 2. Mecânicas e loops que são recompensados

**Achado mais forte e repetido: foque em UMA mecânica e faça ela ser gostosa.**

- *"Todos os jogos citados concentram-se em uma única ideia"* — vencedores evitam feature creep.
- *"Projete o jogo em torno de uma mecânica e foque em fazê-la sentir bem; muitas features só deixam a base de código complexa e cheia de bugs."*

**Como os loops vencedores se parecem:**
- **Um "verbo" central com um twist.** Ex.: empacotar/girar itens, mas encolher deixa mais pesado; pegar gosma pra crescer e atirar gosma pra encolher (e usar o recuo pra pular).
- **Momentos "aha" de puzzle.** Níveis com sacadas inteligentes pontuam alto em Inovação/Diversão.
- **Loops arcade frenéticos.** "Faça tão frenético que não dá pra parar."
- **Resposta imediata.** Controles responsivos, transições rápidas, **restart instantâneo** (tira o atrito do loop).
- **Generosidade > justiça.** Dificuldade que favorece o jogador cria experiências melhores do que a justiça estrita.

**Arquétipos recorrentes (GMTK 2023–2025):**
- Puzzles de **crescer/encolher e escala** ("Built to Scale" 2024).
- Jogos de **time-loop / repetição** ("Loop" 2025 — a cada loop você aprende ou perde algo).
- **Inversão de papéis** ("Roles Reversed" 2023 — tower defense reverso, etc.).
- **Ritmo fundido com outro gênero** (Rave Cage Cyberfunk, Rhythmetric).

**Conclusão:** pegue **um verbo, dê um twist ligado ao tema e ajuste o feel até ficar instantaneamente satisfatório.**

---

## 🎯 3. Interpretação do tema — literal vs. lateral

**O ponto ideal é "esperto, mas legível"** — nem literal demais, nem tão abstrato que ninguém vê a ligação.

- *"Todos os vencedores ficam muito próximos do tema"* — um tema abraçado com força produz um jogo mais focado **e** pontua na categoria Tema.
- Mas literalidade pura é comum e esquecível. O GMTK 2024 teve ~20 puzzle-platformers de empurrar caixas no top 100 — a leitura óbvia é lotada.

**Regra prática:** *se alguém descobre o tema só depois de jogar, a ligação deve ser óbvia e parecer esperta — não arbitrária.* Mire **um passo lateral** da leitura óbvia, mas nunca tão longe que o avaliador não veja (senão você perde a nota de Tema de cara).

---

## ✂️ 4. Escopo — o que vencedores incluem vs. cortam

Disciplina de escopo é o **fator nº 1** de o jogo ficar jogável e polido.

**O que CORTAM:**
- Múltiplas mecânicas / feature creep → corte sem dó até uma só.
- Engines/ferramentas/linguagens novas → **use o que você já domina.**
- Muitos níveis/conteúdo → poucos níveis bem feitos com bons "aha".
- 3D e pipelines de arte complexos.

**O que INVESTEM (em ordem):**
1. **Loop central completo** com estado claro de vitória e derrota.
2. **Legibilidade do tema.**
3. **Juice/feel e áudio** nas horas finais.
4. **Onboarding sem fricção** — controles intuitivos ou tutorial rápido.

> **Dica estratégica:** para realmente *vencer*, considere **jams menores** — as gigantes (GMTK, Ludum Dare) atraem times de elite; jams menores são mais "venciveis" por hora investida.

**Fórmula de escopo vencedora:** *"uma mecânica polida, finalizada e legível no tema"* — não um protótipo ambicioso pela metade.

---

## ✨ 5. Juice, game feel, áudio e primeira impressão

É aqui que jogos "apenas finalizados" viram vencedores.

- **Polimento é traço quase universal.** *"Absurdamente polido para um jogo feito em 4 dias"* — essa é a régua.
- **Juice = satisfação segundo a segundo:** screenshake, partículas, hitstop, SFX em pular/atirar/acertar/morrer. Mantenha o screenshake **curto (50–300ms)** e com decaimento.
- **Áudio é uma categoria inteira** — sem som, você abre mão de uma nota. Mas **nenhuma mecânica deve depender de áudio** (salas de exibição e abas mudas matam isso).
- **Primeira impressão é decisiva** por causa da avaliação rápida: GIF de capa atraente, gameplay imediato (sem intro longa), restart instantâneo, abertura carismática/frenética.
- **Acessibilidade multiplica votos:** o maior alavanca é o **build no navegador (WebGL/HTML5)** — muita gente não baixa `.exe`.

---

## 🕹️ 6. Gêneros que tendem a vencer

- **Puzzle (com twist esperto)** — o mais recompensado quando bem executado (Inovação + Tema + "aha").
- **Arcade / score-chase** — recompensa juice e o loop "não consigo parar".
- **Narrativa curta / experiência** — recompensa Mood/atmosfera; humor é um atalho emocional fácil.
- **Ritmo / música** — padrão em alta em 2025; pontua Áudio, Diversão e Inovação ao mesmo tempo.
- **Sandbox de física / "feel"** — alto juice, diversão imediata.

> Validação: protótipos de jam viraram hits comerciais — **Surgeon Simulator** (GGJ 2013, 48h → 1,8M+ cópias), **Keep Talking and Nobody Explodes**, **Mini Metro**, **Titan Souls**.

---

# 🚀 PASSO A PASSO — Do início ao envio

> Verdade central repetida por todo jammer experiente: **um jogo pequeno, finalizado e polido vence um ambicioso e inacabado, sempre.** Os dois maiores assassinos são *overscoping* e *deixar o envio para a última hora*.

## Fase 0 — ANTES da jam (a semana anterior)

O trabalho feito antes do tema cair é o tempo mais barato que você gasta.

- **Use a engine que você já conhece** — jam não é hora de aprender ferramenta nova.
  - **Godot** (solo/2D, web export ótimo), **Unity** (times, ecossistema de assets), **GameMaker** (2D rapidíssimo).
- **Tenha um template reutilizável pronto** — menu principal, opções, pause, créditos, troca de cena, fades. (ex.: Maaack Godot Template, bitbrain/godot-gamejam com deploy automático pro itch.io).
- **Teste o pipeline de export inteiro num "hello world"** — builde, zipe, suba num itch.io privado e **rode no navegador** antes da jam.
- **Defina papéis do time (3–5 pessoas):** 1–2 programadores, 1–2 artistas, 1 de áudio e **1 diretor/lead designer** que decide. Empodere os leads para decidir no domínio deles.
- **Plano de sono e logística:** durma suas 7–8h (sono é feature). Num jam de 72h, conte ~**54h reais** de trabalho. Faça compras/louça/roupa antes.

## Fase 1 — HORA DO TEMA (primeiros ~60 min)

Não gaste metade do Dia 1 só pensando. Time-box de 1 hora:

1. **Brainstorm (15 min)** — escreva tudo, sem filtro. Tema pode ser literal, criativo, narrativo ou mecânico. Persiga a leitura **não-óbvia**.
2. **Scorecard das ideias (15 min)** — nota para: *Consigo terminar? A diversão é óbvia? Tenho a skill/assets? Dá pra julgar em 3 min?*
3. **Documento de escopo — MVP / Bom-ter / Cortar (15 min)** — escreva os três baldes antes de codar.
4. **Trave e comprometa (15 min)** — defina marcos com "soft deadlines".

**Regra da mecânica única:** resuma em uma frase — *"É um jogo onde você ___."* Se esse verbo não é interessante sozinho, features extras não salvam.

## Fase 2 — TIMELINE dia a dia

Sequência universal: **Prototipe a diversão → vertical slice → conteúdo → polish/juice → envie cedo.** Trabalhe em **sprints de 2h**. O sinal de um bom plano é um **buffer grande no fim.**

### Jam de 48h (Sex 18h → Dom 18h)
| Janela | Foco |
|---|---|
| **H0–4 (Sex noite)** | Tema + ideação. Protótipo do **core com placeholders cinza.** Pergunta única: *o loop é divertido?* Se não, pivote AGORA. |
| **Fim de Sex** | Pronto pra "produção". Depois **durma.** |
| **H4–12 (Sáb)** | **Vertical slice** — um loop completo jogável de ponta a ponta. |
| **H12–24 (Sáb)** | **Conteúdo + 1º playtest.** Build Alpha, teste com gente real, corrija bugs. |
| **Fim de Sáb** | Alpha funcionando. **Durma.** |
| **H24–34 (Dom)** | **Polish & juice**, assets finais, menu, onboarding básico. Beta de manhã. |
| **H34–46** | **Pare de adicionar features.** Só correção de bugs. |
| **~2h finais** | **Builde, suba e envie cedo.** Nunca deixe o build pros últimos 30 min. |

### Jam de 72h
- **Dia 1 (Sex noite):** ideação + protótipo "fun-first". Durma.
- **Dia 2 (Sáb):** grosso da produção — vertical slice + maior parte do conteúdo. Alpha no sábado à noite, playteste.
- **Dia 3 manhã (Dom):** finalize conteúdo, **trave o escopo (feature-freeze)**, comece o polish.
- **Dia 3 → Dia 4 manhã:** polish, juice, áudio, menus, tutorial. Beta playtest.
- **~3–4h finais:** build → upload → screenshots/GIF → página → **envie com buffer.**

> Regra de bolso: **os últimos 25–30% da jam são polish + envio, não features novas.**

### Jam de 1 semana
Mais tempo = mais tentação de overscope (o perigo é *maior*, não menor). Use os dias extras como **ciclos de iteração e playtest**, não como licença pra adicionar sistemas. Playteste com gente de fora até o fim do Dia 3; feature-freeze no Dia 6.

## Fase 3 — Gestão de ESCOPO (faz ou quebra)

- **Overscoping é a causa nº 1** de jogos de jam morrerem.
- **MVP:** defina a versão *mínima* que ainda é divertida e on-theme. Construa-a inteira antes de tudo.
- **Protótipo fun-first:** primeiro build é teste cinza do *verbo central*. Se o placeholder não é divertido, pivote enquanto é barato.
- **Termine o loop antes de história/UI/menus.**
- **Corte agressivamente.** A lista "Cortar" é uma feature, não um fracasso.

## Fase 4 — POLISH (onde as notas são ganhas)

**Checklist de juice:** screenshake curto · partículas (poeira/faíscas) · squash & stretch · hitstop · tweens/easing em UI.
**Áudio:** SFX em *toda* ação (inclusive cliques de menu) · varie pitch/volume levemente. Não dependa de som para mecânica.
**Menus & onboarding:** título + pause + créditos já passam "finalizado". **Ensine jogando**, controles na tela e na página do itch.

## Fase 5 — ENVIO (não perca a corrida na última hora)

**Gotchas de build/export — teste cedo:**
- Prefira **build jogável no navegador (HTML5/WebGL).**
- Web export é um **ZIP** com `index.html` + arquivos (Godot/Unity exportam multi-arquivo — zipe).
- Tela em branco? Quase sempre MIME-type/WASM — cheque o console.
- Builds multithread (Godot/Unity) precisam de **SharedArrayBuffer** → marque a opção no itch.io, ou exporte **single-thread.**
- Evite chamadas de rede externas (CORS bloqueia).

**Página do itch.io:**
- **GIF animado no topo é o item de maior impacto.** ~10s do melhor momento, <3 MB. Use o 1º frame como capa. (ScreenToGif / EZgif)
- 3–5 screenshots de gameplay real.
- Descrição: hook de uma linha + interpretação do tema + **controles** + créditos/atribuições.
- Tags e gênero corretos.

**Otimização das notas:**
- Coloque esforço visível em *toda* categoria julgada (Tema é categoria própria na maioria).
- **Avalie e comente outras entradas** — isso traz jammers de volta pra sua página e eles retribuem; é o jeito comprovado de juntar votos suficientes pra ranquear.

## ⚠️ Erros comuns que afundam jogos de jam
1. Overscoping. 2. Aprender engine/linguagem nova no meio. 3. Deixar build/upload pra última hora. 4. Polir história/UI antes do loop rodar. 5. Pular o sono. 6. Mecânica que depende de áudio. 7. Só ter download (sem web). 8. Sem onboarding/controles. 9. Sem GIF/screenshots. 10. Gastar metade do Dia 1 em brainstorm.

---

## 🧰 Ferramentas e assets gratuitos

**SFX:** [Bfxr](https://www.bfxr.net/) · [sfxr/jsfxr](https://sfxr.me/) · [ChipTone](https://sfbgames.itch.io/chiptone)
**Bibliotecas de SFX/música:** [Freesound](https://freesound.org) · [SONNISS GameAudioGDC](https://sonniss.com/gameaudiogdc) · [Kenney Audio](https://kenney.nl/assets/category:Audio) · [OpenGameArt](https://opengameart.org) · [Incompetech](https://incompetech.com)
**Criar música:** [Bosca Ceoil Blue](https://terrycavanagh.itch.io/bosca-ceoil-blue) · [BeepBox](https://www.beepbox.co)
**Arte/sprites:** [Kenney Assets](https://kenney.nl/assets) · [Piskel](https://www.piskelapp.com) · Krita · Inkscape · LibreSprite · MagicaVoxel · [Lospec (paletas)](https://lospec.com)
**Fontes:** [Google Fonts](https://fonts.google.com) (mais segura p/ uso comercial) · Font Squirrel · DaFont · 1001 Fonts
**Captura/GIF:** [ScreenToGif](https://www.screentogif.com) · [EZgif](https://ezgif.com)
**Templates:** [Maaack Godot Template](https://github.com/Maaack/Godot-Game-Template) · [bitbrain/godot-gamejam](https://github.com/bitbrain/godot-gamejam)

---

# 🏆 TOP 10 — Jogos vencedores de Game Jam (2024–2026)

> **Notas de verificação:** O GMTK rodou em 2024 ("Built to Scale") e 2025 ("Loop") e **volta em 2026** (10ª edição, 22–26 jul). Em 2025 o Mark Brown deixou de nomear um único vencedor (publica "20 favoritos" + rankings da comunidade); **2024 teve um #1 claro** no itch.io. O Global Game Jam **não é competitivo** (sem ranking oficial), por isso foi excluído em favor de entradas realmente ranqueadas.

### 🥇 #1 — *That Time I Got Reincarnated as a Panda...* — GMTK 2024, **#1 Geral**
- **Tema:** "Built to Scale" · **Nota 4.689** (a mais alta de ~14.000+ entradas)
- **Gameplay:** você constrói e **escala** plataformas para guiar um panda que rola sozinho. "Clique pra construir, scroll pra escalar, velocidade = pontos." Vira um brinquedo de momentum/score-attack.
- **Por que venceu:** leitura dupla genial do tema (você literalmente *escala* plataformas E persegue *escala* de pontuação no placar), design de uma tela legível na hora, e física de momentum extremamente satisfatória.
- **Ferramentas/Time/Tempo:** Clickteam Fusion 2.5, Aseprite, BFXR · **Solo** (Colisan) · ~43h.
- 🔗 [itch.io](https://colisan.itch.io/that-time-i-got-reincarnated-as-a-panda-a-h-t-c-c-b-r-a-o-b-t-s-p) · [Resultados GMTK 2024](https://itch.io/jam/gmtk-2024/results)

### 🥈 #2 — *Would you still love me if I was a worm?* — Ludum Dare 55, **#1 Geral (Jam)**
- **Tema:** "Summoning" (abr/2024) · **#1 Geral e #1 Diversão**
- **Gameplay:** jogo de ação onde você lança cartas para **invocar um exército de vermes** (verme laser, dragão...), cada habilidade destravada por um mini-game de skill, numa jornada de vingança.
- **Por que venceu:** premissa memorável (em cima de um meme viral), variedade mecânica real via mini-games, muito polish e humor.
- **Ferramentas/Time/Tempo:** **Godot** · time de 6 · 72h.
- 🔗 [itch.io](https://guyunger.itch.io/would-you-still-love-me-if-i-was-a-worm) · [ldjam](https://ldjam.com/events/ludum-dare/55/would-you-still-love-me-if-i-was-a-worm)

### 🥉 #3 — *Henry Super Brain* — Pirate Software Game Jam 15, **#1 Geral**
- **Tema:** "Shadows and Alchemy" (jul/2024) · #1 de 2.354 entradas
- **Gameplay:** puzzle dentro do cérebro de um furão, onde você experimenta combinações incomuns de input→ação, remapeando e encadeando controles como o próprio puzzle.
- **Por que venceu:** mecânica central genuinamente nova (mapear inputs *é* o puzzle), boa apresentação, leitura não-literal do tema — e foi o **primeiro jogo publicado** do criador.
- **Ferramentas/Tempo:** Unreal Engine, arte no Photoshop · janela de ~2 semanas.
- 🔗 [itch.io](https://devnix.itch.io/henry-super-brain) · [Anúncio dos vencedores](https://x.com/PirateSoftware/status/1824864291818017141)

### #4 — *Wrong File* — Brackeys Game Jam 2025.1, **#1 Geral**
- **Tema:** "Nothing can go wrong..." (fev/2025) · **4.350**
- **Gameplay:** você trabalha na "WF Company" e, durante a primeira semana de trabalho de escritório mundano, precisa secretamente repelir malwares invadindo o sistema — tudo que "não pode dar errado" dá.
- **Por que venceu:** ironia temática afiada, apresentação em camadas (simulação de desktop) e polish apertado (o 2º lugar ficou só 0.002 atrás).
- **Time/Tempo:** time de 5 · jam de ~1 semana.
- 🔗 [Resultados Brackeys 2025.1](https://itch.io/jam/brackeys-13/results)

### #5 — *Rhythmetric* — GMTK Game Jam 2025, **favorito do Mark Brown / top da comunidade**
- **Tema:** "Loop" (jul–ago/2025) · entre os "20 favoritos" (sem #1 único por escolha do organizador)
- **Gameplay:** um círculo luta contra formas pontudas com lasers, esquivas e escudos. Você posiciona movimentos ao longo de uma **trilha em loop**; conforme o indicador roda, cada movimento dispara no tempo — você *programa* seu combate como um loop rítmico.
- **Por que se destacou:** fusão inventiva de sequenciador rítmico + ação que acerta o tema "Loop" literal e mecanicamente.
- **Tempo:** 96h.
- 🔗 [Favoritos do Mark Brown](https://gmtk.substack.com/p/my-favourite-games-from-gmtk-game) · [Resultados GMTK 2025](https://itch.io/jam/gmtk-2025/results)

### #6 — *Varmint* — GMTK Game Jam 2024, **#2 Geral**
- **Tema:** "Built to Scale" · **4.583**
- **Gameplay:** entrada de ação/arcade polida que interpreta escala via combate e progressão baseados em tamanho (um "varmint" que cresce contra ameaças).
- **Por que se destacou:** polish e feel excepcionais — top 5 entre 14.000+ entradas.
- **Tempo:** 96h (DirtyOnion + time).
- 🔗 [Resultados GMTK 2024](https://itch.io/jam/gmtk-2024/results)

### #7 — *Pizzascaper* — GMTK Game Jam 2024, **#3 Geral**
- **Tema:** "Built to Scale" · **4.583 (empate)**
- **Gameplay:** plataforma de speedrun em primeira pessoa estilo *Neon White*, onde você **escala** blocos do cenário virando-os em trampolins, ganhando momentum para encadear níveis neon em alta velocidade.
- **Por que se destacou:** levou "scale" pro speedrunning cinético, arte neon e teto de skill alto.
- **Tempo:** 96h · time de 3.
- 🔗 [Best-of Mark Brown](https://gmtk.substack.com/p/the-best-games-from-gmtk-game-jam-500)

### #8 — *Shutterbug* — GMTK Game Jam 2024, **favorito top (browser)**
- **Tema:** "Built to Scale"
- **Gameplay:** jogo de navegador que usa a **própria janela do browser como visor de câmera** — você redimensiona e reposiciona a janela real para enquadrar e fotografar insetos atendendo requisitos de composição.
- **Por que se destacou:** uma das meta-mecânicas mais criativas da jam, transformando o "escalar a janela" na câmera — encaixe perfeito e inesperado no tema.
- **Tempo:** 96h (build web).
- 🔗 [Best-of Mark Brown](https://gmtk.substack.com/p/the-best-games-from-gmtk-game-jam-500)

### #9 — *Entrada da PUNKCAKE Délicieux ("Depths")* — Ludum Dare 57, **#1 Geral**
- **Tema:** "Depths" (abr/2025) · **#1 Geral, #1 Diversão, #2 Inovação** (1.566 entradas)
- **Gameplay:** arcade/roguelike apertado no estilo característico da PUNKCAKE — uma tela, denso de mecânica, com estratégia profunda (estúdio por trás de *Shotgun King*, vencedor da LD50).
- **Por que venceu:** campeões recorrentes do LD, conhecidos por mecânicas elegantes e instantaneamente compreensíveis; varreram Diversão e lideraram o Geral.
- **Time/Tempo:** trio do estúdio + compositor · 72h.
- 🔗 [PUNKCAKE itch.io](https://punkcake.itch.io/)
- *Obs.: o título exato do envio da LD57 não foi confirmável com clareza no índice público de resultados durante a pesquisa.*

### #10 — *Picture Perfect* — GMTK Game Jam 2024, **favorito top (narrativo)**
- **Tema:** "Built to Scale"
- **Gameplay:** jogo aconchegante de narrativa construído sobre **fotografia em perspectiva forçada**. Você manipula zoom, posição da câmera e poses para criar ilusões de escala, que aos poucos revelam uma história tocante de pai e filha numa viagem.
- **Por que se destacou:** narrativa emocional e uso gentil e esperto de escala/perspectiva como mecânica *e* dispositivo narrativo — contraponto tonal às entradas de ação no topo.
- **Tempo:** 96h.
- 🔗 [Best-of Mark Brown](https://gmtk.substack.com/p/the-best-games-from-gmtk-game-jam-500)

---

## 📊 Padrões do Top 10

- **#1 mais verificados:** GMTK 2024 (Panda), Ludum Dare 55 (Worm), Pirate Jam 15 (Henry Super Brain), Brackeys 2025.1 (Wrong File), Ludum Dare 57 (PUNKCAKE).
- **Recorrências:** 2D estilizado, **uma mecânica com twist**, tema "esperto-mas-legível", polish acima da média, e (quando possível) **jogável no navegador**.
- **Times pequenos vencem:** de **solo** (Panda) a **6 pessoas** (Worm) — o tamanho importa menos que o foco.
- **Engines:** Godot, Unity, Unreal, Clickteam Fusion — **a que você domina** é a certa.

---

### 📚 Fontes principais
- GMTK 2024 best-of — https://gmtk.substack.com/p/the-best-games-from-gmtk-game-jam-500
- GMTK 2025 favoritos — https://gmtk.substack.com/p/my-favourite-games-from-gmtk-game
- Rat King — "The winners of Ludum Dare" — https://ratking.de/blog/2014/01/31/the-winners-of-ludum-dare/
- Ludum Dare (Wikipedia) — https://en.wikipedia.org/wiki/Ludum_Dare
- Brackeys 2025.1 — https://itch.io/jam/brackeys-13/results · Brackeys 2025.2 — https://itch.io/jam/brackeys-14/results
- Pirate Jam 15 vencedores — https://x.com/PirateSoftware/status/1824864291818017141
- itch.io — dicas de arte — https://itch.io/blog/935472/4-tips-to-improve-your-game-jam-art-at-any-skill-level
- "Avoid these pitfalls" — https://devindetails.com/avoid-these-pitfalls-during-your-next-game-jam-as-i-wish-i-did/
- 19 Game Jam Tips — https://gamedevelopermarketing.com/game-jam-tips/
- itch.io — game jams docs — https://itch.io/docs/creators/game-jams
- Making a Game Feel "Juicy" — https://itch.io/blog/1059831/making-a-game-feel-juicy-with-simple-effects
