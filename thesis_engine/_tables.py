
# gerado por guard.py — registro auto-descritivo do banco
_TABLES = [
    ("acaoedeedora", "setup", "Ações devedoras (semeadas + executadas)"),
    ("block", "execution", "Blocos de texto (escritos pelo ciclo)"),
    ("chapter", "setup", "17 capítulos (estrutura, read-only)"),
    ("claim", "setup", "Claims C001-C060 (sha256 imutável)"),
    ("environmentrule", "setup", "Guard de ambiente (repo/branch/forbidden)"),
    ("graphedge", "setup", "Grafo arestas (1145, read-only)"),
    ("graphnode", "setup", "Grafo 3-trees (884 nós, read-only)"),
    ("methodfact", "setup", "Métodos M001-M004"),
    ("nfact", "setup", "N-fatos N001-N065 (imutável)"),
    ("numbervalue", "setup", "308 números com lineage (read-only)"),
    ("planchapter", "setup", "Plano global por capítulo (read-only)"),
    ("resultfact", "setup", "Resultados R001-R005"),
    ("reviewquestion", "setup", "7 perguntas do revisor hostil (a-g)"),
    ("revisaohostil", "execution", "Fila do revisor hostil (perguntas/respostas)"),
    ("section", "execution", "Seções (criadas pelo escritor)"),
    ("source", "setup", "Fontes E001-E058 (imutável)"),
    ("stylerule", "setup", "37 regras de estilo (LLM-bans + PT-bans)"),
    ("tableregistry", "setup", "Esta meta-tabela (auto-descrição do banco)"),
    ("writingcycle", "execution", "FSM do ciclo por capítulo"),
]
