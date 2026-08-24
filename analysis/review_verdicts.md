# Auditoria de Vereditos — Quest 003 (núcleo analítico)

Legenda: ✅ positivo real · ❌ negativo (com ajuste incremental) · 🌑 cinza escuro (resultado provavelmente negativo por lógica/realidade) · 🌕 cinza claro (resultado provavelmente positivo pela estratégia lógica)

## ✅ POSITIVOS REAIS E VÁLIDOS (literatura atual)

1. **A molécula existe e funciona como descrito.** G127V sob seleção positiva na epidemia de kuru (Mead 2009) e resistência completa + inibição dominante-negativa dose-dependente em camundongos transgênicos (Asante 2015; Zheng 2018; revalidado por Gatdula 2026). Nenhuma alegação molecular central é ficção.
2. **A lógica estratégica de classe (negação de substrato) tem a melhor evidência da área.** Depleção de PrP reverte doença precoce (Mallucci 2003/2007); ASOs anti-PRNP estendem sobrevida 61-98% em camundongos (Raymond 2019; Minikel 2020) e já estão em first-in-human (ION717, desde 2023). O protocolo pertence à família terapêutica mais promissora conhecida para príons.
3. **A incompatibilidade cinética exponencial × linear é qualitativamente correta.** Fragmentação de fibrilas multiplica pontas ativas; migração celular é ~mm/dia. A intuição de "não perseguir a onda, mas mudar o terreno" é defesa pela literatura de PrP-lowering (efeito independente de perseguir focos).
4. **Precedente de terapia celular em príons existe.** hMSC prolongam sobrevida em camundongos infectados (Song 2009); NPCs humanas restauram eletrofisiologia de organoides com sCJD (Williams 2023) — o modelo de teste humano pré-clínico JÁ existe.
5. **A rota cirúrgica é tecnologia madura.** CED com cânula step-design anti-refluxo validada desde 2005 (Krauze), em ensaios clínicos ativos (Parvar 2025); DTI + neuronavegação robótica é padrão em neurocirurgia funcional.
6. **Diagnóstico precoce antemortem é real.** RT-QuIC em LCR/mucosa olfatória (Green 2018; Hermann 2021) — o requisito "aplicar cedo" tem instrumento.
7. **Segurança de NSC intracraniana em humanos tem registro de fase 1** (Mazzini 2015; Curtis 2018; PISCES).
8. **Infraestrutura GMP nacional é real** (HUG-CELL/USP, LaNCE) — alegação verificável.

## ❌ NEGATIVOS, GAPS E OBSTÁCULOS (com ajuste incremental)

1. **Erro de biologia do desenvolvimento no desenho:** NSCs neuroectodérmicas NÃO geram micróglia (linha germinal mesodérmica, saco vitelínico — Ginhoux 2010). O "quartel-general gerador de micróglias de vigilância" é impossível como escrito.
   → *Ajuste:* remover micróglia do claim; se vigilância imune for desejada, co-enxerto de micróglia-like de iPSC como produto separado.
2. **A "fábrica autossustentável" no SVZ humano é superestimada.** Neurogênese SVZ adulta humana é mínima (Sorrells 2018; consenso 2018) e o nicho é ele próprio reservatório de replicação priônica (Relaño-Ginés 2013).
   → *Ajuste:* reformular o depósito central como "depósito farmacológico de células produtoras de PrP-V127 de liberação lenta", não como fábrica regenerativa.
3. **Propagação não é frente sólida.** Disseminação sináptica/axonal + multifocal → linha de contenção anatômica não intercepta focos microscópicos além da margem. O próprio documento admite (30-40%) mas subestima a dimensão de rede.
   → *Ajuste:* mapear conectividade (tratografia DTI entre regiões afetadas) e injetar nos NÓS de rede, não em anéis; combinar com ASO sistêmico intratecal como "contenção química global" (ver Otimizações).
4. **DTI não resolve margem microscópica.** Resolução mm vs disseminação celular.
   → *Ajuste:* RT-QuIC/PMCA em amostras de LCR regional + biópsia de margem intraoperatória (imuno-histoquímica PrP-res rápida) para calibrar margens em tempo real.
5. **Aloenxerto off-the-shelf × rejeição.** Cérebro "privilegiado" perde privilégio na neuroinflamação priônica (BBB rompida). Imunossupressão em paciente DCJ = risco infeccioso grave.
   → *Ajuste:* banco HLA-matched + linhas hipoimunes (KO HLA + CD47↑), ou redefinir população-alvo (ver 6).
6. **Janela temporal da DCJ esporádica é brutal.** Sobrevida média 6-8 meses; atraso diagnóstico ~2-3 meses; produção autóloga impossível no tempo.
   → *Ajuste estrutural (maior do plano):* redirecionar a indicação inicial para **portadores pré-sintomáticos de DCJ genética (E200K, D178N, P102L)** — o Brasil tem agrupamentos E200K documentados. RT-QuIC+ presintomático = anos de janela, autóloga viável, QA completo, desenho de ensaio controlável. DCJ esporádica vira uso compassivo tardio.
7. **Tumorigenicidade iPSC.** Resíduo pluripotente → teratoma.
   → *Ajuste:* seleção negativa (SSEA-4/Tra-1-60), citometria de pureza, teste de expansão in vivo como gate de liberação.
8. **Biossegurança operacional subestimada.** A cânula atravessa tecido infectado até o SVZ: arrasto mecânico pode semear PrPSc no nicho e no trajeto; instrumentais precisam de protocolo de destruição/descontaminação (casos iatrogênicos documentados, Thomas 2013; CDC).
   → *Ajuste:* cânula de uso único com camisa externa (coaxial), fluxo retrógrado mínimo, sequenciamento de sala, protocolo WHO pós-procedimento.
9. **Custo/complexidade vs alternativa ASO.** ION717 já em clínica; células editadas + neurocirurgia robótica = ordens de magnitude mais caro e lento.
   → *Ajuste de posicionamento:* o valor único da célula é permanência + tropismo + entrega local; posicionar como camada sobre ASO (combinação), não competidor.

## 🌑 CINZA ESCURO (não documentado; lógica/realidade apontam negativo)

1. **Inibição dominante-negativa "em trans" na margem.** Toda evidência forte de DN é cis (V127 co-expresso NA MESMA célula). PrP é proteína GPI-ancorada de membrana — não satura espaço intercelular como "escudo difusível". A premissa do anel bombeiro ainda não foi demonstrada.
2. **Taxa de sobrevida funcional do enxerto ≥ necessário.** Tempestade de citocinas + microambiente citotóxico → apoptose precoce documentada em enxertos; lit. NSC: sobrevida típica 1-20%.
3. **Contenção COMPLETA em DCJ esporádica avançada** (focos invisíveis além da linha).
4. **Aprovação regulatória de célula基因组-editada em janela compassiva no Brasil** dentro do tempo de sobrevida do paciente (CTGT/ATMP via Anvisa + CONEP: 12-24 meses típico).
5. **"Regeneração" do parênquima morto** — nenhuma evidência de reconexão funcional de território espongiforme em humanos.

## 🌕 CINZA CLARO (não documentado; estratégia lógica aponta positivo)

1. **Resistência célula-autônoma das células editadas V127/V127** — extensão direta de Asante 2015; testável em organoide em ~90 dias (Williams 2023).
2. **PrP-V127 secretado/vesicular como DN trans.** Existem constructs de PrP solúvel dominante-negativo na lit. de desiagem molecular; nunca combinados com G127V. Se funcionar, CONVERTE o cinza escuro nº1 em claro. (Hipótese NOSSA — testável.)
3. **Combinação ASO-ponte + célula-contenção:** ASO derruba substrato global enquanto o enxerto estabelece — sinergia nunca testada, mas cada parte validada.
4. **Enxerto no nicho SVZ de portador E200K pré-sintomático:** ambiente ainda não-inflamado; a lacuna lit. é ausência de estudo, não contradição.
5. **Benefício funcional de NPCs mesmo sem conter príons** (Williams 2023: restauração eletrofisiológica) → desfecho secundário plausível (qualidade de vida) mesmo no fracasso da contenção.

## Impactos emergentes do estado da pesquisa

- **Corrida ASO:** se ION717 demonstrar desaceleração clínica, terapia celular precisa se justificar como complemento (permanência/focalidade) ou morre por custo-oportunidade.
- **Organoides cerebrais** encurtam o ciclo de iteração do desenho celular (meses, não anos) — acelerador infraestrutural do plano.
- **Precedente PRN100** (Mead 2022): anti-PrP em humanos foi seguro mas clinicamente pouco eficaz — alerta de que segurança pré-clínica ≠ eficácia nesta doença; calibrar expectativa de "congelamento".
- **Saúde pública:** paciente permanece infeccioso post-mortem independentemente do desfecho — protocolo de instrumentais/autópsia obrigatório no desenho.
