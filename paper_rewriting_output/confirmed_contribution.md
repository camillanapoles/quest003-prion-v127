# Confirmed Contribution

*Nota de sequenciamento honesta: a motivação (M4-da-autora) e os blueprints precederam a escrita; este artefato destila a contribuição que a tese unificada já defende (fontes: confirmed_motivation.md · section_blueprints B0-B9 · tese_unificada.md Cap.1/6/9) — criado no fechamento do braço-B, não antes do drafting (desvio de ordem registrado; o conteúdo é pré-existente, não inventado agora).*

## Core Contribution

| Field | Content |
|---|---|
| Main contribution statement | A etrização computacional — método formal de continuidade de pesquisa (P0–P6) sobre dados reais publicados, com prognósticos travados antes da medição e auditoria hostil de máquina — demonstrado de ponta a ponta no caso V127, entregando o primeiro dimensionamento quantitativo de dose-e-entrega para doença priônica: limiar θ\*=0,333 (v1.0, travado), três regras de design, invariância multi-espécie do limiar (Cenário B, razão 1,20) e a primeira dose calculada do braço A6 em banda GUM (0,0–2,6 µg/depósito no degrau humano; largura ≈53× dominada pelo proxy de Kd — que o ensaio G0-A6 fecha). |
| Contribution type | new method (dominante; com new application e new empirical finding [SIM] embutidos) |
| One-sentence reviewer payoff | Um framework auditável que converte dado publicado em prognóstico de dose/posicionamento falseável — incluindo a quantificação honesta da própria incerteza (a banda É o achado até o ensaio fechá-la). |

## Why This Contribution Is Needed

| Field | Content |
|---|---|
| Field problem | Doenças priônicas: 100% fatais, sem terapia modificadora; seis candidatos clínicos fracassaram em quatro décadas sem modelo quantitativo de entrega. |
| Specific gap | Nenhum método formaliza **continuar pesquisa com rigor quando só há dado publicado** (a saúde salta de hipótese a experimento sem nomear o meio); e a cadeia dimensional κ→concentração→massa nunca foi fechada com incerteza propagada para esta classe de terapia. |
| Concrete challenge | Decidir dose/posicionamento exige amarrar cinética murina publicada → relógio organoide humano → transporte intersticial in-vivo → âncora κ↔µM (sem Kd do par real; só proxy) — cada el com fonte e incerteza própria, sem dado próprio medido. |
| Why prior work leaves it unresolved | Meta-análises resumem o medido (não derivam); in-silico trials simulam o ensaio (não travam prognóstico antes da medição nem rotulam tier); QSP/PBPK modelam sem a disciplina de pré-registro/anti-hindsight/auditoria recursiva; nenhum fechou a cadeia κ→massa com banda GUM declarando o que o ensaio fecha. |

## How This Paper Responds

| Field | Content |
|---|---|
| Design response | Pipeline P0–P6 com garantias por passo: registro E-verificado (58 fontes), motores auto-testados, critérios de aceitação pré-declarados, predições travadas por release, guardião R0–R3 + AST 9/9, e a cadeia de dose em banda GUM Tipo-B com critérios pré-registrados antes de computar. |
| Evidence required | (i) limiar quantitativo travado e não-retreinado; (ii) regras de design falseáveis; (iii) robustez a parâmetros não-medidos; (iv) transferibilidade entre espécies; (v) dose em massa com incerteza propagada; (vi) reprodutibilidade/auditabilidade de ponta a ponta. |
| Evidence available | (i) θ\*=0,333 v1.0 [C038]; (ii) regras 1–3 [C033-C035]; (iii) S1-S3 (C50 10×; só Kt move) [C051, F-43]; (iv) Cenário B 0,333–0,400 + titulação [C055-C057]; (v) banda A6 0,0–2,6 µg + largura ≈53× decomposta [C058-C060, E057/E058]; (vi) reprodução 2 ambientes (hash+valor), 60 claims/58 fontes/65 N-fatos, gates 0-BLOCKED. |
| Evidence missing | Dado [ORGANOID]+ medido (G0-wet não executado — especificado, F1–F10); Kd do par V127↔PrP^Sc (só proxy Aβ42 [E057]); discriminação da forma funcional do capping (pendente do A6). Por isso TODA a saída é tier [SIM]-planejamento e a dose é banda, não ponto. |

## Claim Boundary

| Field | Content |
|---|---|
| Strong claims allowed | Método formal replicável (P0–P6 com garantias); prognósticos falseáveis travados antes da medição; dose em banda com incerteza propagada e largura decomposta (14× Kd-proxy × 3,7× V-halo); ensaio que fecha cada banda especificado; auditoria de máquina reproduzível (AST 9/9). |
| Claims to soften or avoid | Eficácia clínica; aplicação humana; contenção medida em tecido; substituição do laboratório; precisão de ponto na dose (a banda é o achado — nunca "a dose é X µg"); seleção de parceiro executada (só o método é entregue). |
| Novelty risk | Revisor confundir etrização com in-silico trials/QSP — mitigado pela diferenciação estrutural (Cap. 1.2: prognóstico travado antes da medição; tiers; antecipação bancada; derivação vs resumo) e pelos quatro pontos de distinção citados com fonte. |
| Significance risk | "Sem dado wet-lab, é especulação" — mitigado pelo tier [SIM] em toda saída, pela quantificação do que falta (a banda ≈53× declara exatamente o que G0-A6 fecha) e pela entrega de desenho quantitativo que nenhum candidato anterior teve; remaining: a banca decide em grau superior (H1 documental). |
| Boundary conditions | Toda afirmação carrega tier [SIM] e binding [claim/evidence]; predições v1.0 comparadas-jamais-retreinadas; horizonte de θ\* declarado em toda citação (C056); uso humano só pela escada de gates [ORGANOID]→[MOUSE]→regulatório. |
