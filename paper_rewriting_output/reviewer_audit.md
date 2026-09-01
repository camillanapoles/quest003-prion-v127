# Reviewer Audit — tese unificada (braço-B)

*Fontes do registro de objeções: as 3 personas (Methods/Reproducibility, Contribution, Clarity) mapeadas contra os achados hostis pré-existentes da casa — guardião R3 (interrogação epistêmica), `paper/hostile_review_v4.md`, Apêndice B.5 "Prejulgando objeções da banca" e o council-alfa. Nenhuma objeção inventada do nada: cada linha traça a um achado existente.*

## 1. Reviewer Value Map

| Critério | O que compra | Onde o manuscrito é forte | Onde é fraco (watch) |
|---|---|---|---|
| Novelty | o revisor precisa poder citar "o que isto acrescenta" | método nomeado com garantias (P0–P6); primeira dose calculada em banda GUM | risco de ler como "simulação a mais" se pular o Cap. 1.2 |
| Significance | por que importa ao campo | primeiro dimensionamento quantitativo de dose-e-entrega para doença 100% fatal com 6 falhas clínicas | significância plena depende do G0-wet (declarado) |
| Technical soundness | confiança no resultado | motores auto-testados (massa 100%; ℓ 0,5%); critérios pré-declarados; AST 9/9; reprod. 2 ambientes | Kd é proxy (Aβ42↔PrP) — forte só porque DECLARADO e quantificado na banda |
| Evidence sufficiency | evidência basta para o claim? | claims travadas v1.0; 60/58/65 registro; banda decomposta 14××3,7× | dado [ORGANOID]+ inexistente — coberto por tier e pelo ensaio especificado |
| Clarity | aceitar/rejeitar algo específico | θ\*=0,333; banda 0,0–2,6 µg — claims testáveis; siglas + openers clínicos | neologismo exige a nota-à-banca (chave-antes-da-porta) |
| Venue fit | aderência ao veículo | tese doctoral como documento primário (banca); recorte de artigo mapeado | submissão a periódico exige recorte fora do escopo do braço-B |

## 2. Reviewer Objection Register

| # | Persona | Objeção provável | Severity | Localização | Fix preventivo | Status |
|---|---|---|---|---|---|
| 1 | Methods | "Simulação sem validação wet-lab não é evidência" | CRITICAL | Cap. 8; Base de Validade §5.3 | tríade obrigatória + tier [SIM] em toda saída + G0-wet especificado (F1–F10) | CLOSED (declarado) |
| 2 | Methods | "Kd de Aβ42 não é Kd de V127↔PrP^Sc" | CRITICAL | §4.3; C060 | proxy DECLARADO; a banda ≈53× quantifica exatamente este limite; A6 fecha | CLOSED (quantificado) |
| 3 | Methods | "Parâmetros murinos não transferem" | MAJOR | Cap. 3; Cap. 2.3 | Cenário B (razão 1,20) + relógio humanizado + regra de titulação; refutação hamster reportada | CLOSED (sondado) |
| 4 | Methods | "Grade saturada infla critérios" | MAJOR | Ap. B/B.4 | escapes = limite inferior declarado; grade maior pré-declarada | CLOSED (declarado) |
| 5 | Methods | "Forma funcional do capping arbitrária" | MAJOR | §5.2; C051 | falseável pela dose-resposta do A6 — predição discriminadora travada | CLOSED (falseável) |
| 6 | Contribution | "Isto é só um in-silico trial renomeado" | CRITICAL | Cap. 1.2 | diferenciação estrutural 4 pontos (prognóstico travado; tiers; P6 bancado; P5 derivada) | CLOSED |
| 7 | Contribution | "Neologismo sem necessidade" | MAJOR | Cap. 1.1 | nenhum termo existente nomeia o estado ontológico; 5 critérios operacionalizam; precedente átomo/software | CLOSED |
| 8 | Contribution | "Cronologia: o desenho existia antes da 'validação'" | CRITICAL | Cap. 2.2 | cronologia honesta na abertura — precedência histórica exibida como força (anti-hindsight) | CLOSED |
| 9 | Contribution | "Sem seleção de parceiro, a continuidade é retórica" | MAJOR | §OE4 | método SLR-análogo documentado + piloto não-decisório executável | CLOSED (método entregue) |
| 10 | Clarity | "Símbolos θ/κ/Kt inacessíveis" | MINOR | Lista de Siglas; openers clínicos | camada clínica + rota-10min + "Em linguagem clínica" por capítulo técnico | CLOSED |
| 11 | Clarity | "Figuras não sustentam os claims" | MINOR | Figs. 4-5 | figuras auditáveis (scripts leem só JSONs; número nunca digitado) regeneráveis no CI | CLOSED |
| 12 | Clarity | "Banda de 2 ordens parece erro, não achado" | MINOR | §4.3; Fig. 5 | a largura é DECOMPOSTA (14××3,7×) e o ensaio que a fecha é nomeado (A6) | CLOSED |
| 13 | Methods | "Single-rater nos pesos de parceiro" | MINOR | Cap. 8.10 | co-rating pré-declarado como pendência no ledger | OPEN (tracked) |
| 14 | Methods | "Preprints não-verificados no banco" | MINOR | Referências complementares | marcados snippet-level; elevação a E só após abertura | OPEN (tracked) |
| 15 | Contribution | "Onde está o dado humano?" | MAJOR | Cap. 8.3 | inexistente e rotulado; rota compassiva E200K especificada, não prometida | CLOSED (declarado) |

## 3. Editorial Fit Map

| Questão do editor | Resposta |
|---|---|
| Venue fit | Tese doctoral (banca) como documento primário; derivados de método a periódicos de metodologia translacional (a própria tese mapeia: prion-like transfer >50M); a edição unificada é publication-grade single-column |
| Desk-reject risk | BAIXO para tese (documenta metodologia própria); para periódico: exige recorte (o achado da banda + Cenário B como artigo de método) |
| Por que enviar a revisão | Primeiro caso que cumpre um padrão auditável novo (5 critérios + gates de máquina) E entrega produto quantitativo novo (dose em banda com o ensaio que a fecha) |
| O que falta para submissão a periódico | ficha acadêmica (autora); recorte de artigo; checagem de venue específica (fora do escopo do braço-B) |
