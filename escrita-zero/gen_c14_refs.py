#!/usr/bin/env python
"""Gera c14 (REFERÊNCIAS) determinicamente do registro probatório.

Regras (zero digitação — tudo sai do source_manifest.json):
  - Autoria: sobrenome MAIÚSCULO + iniciais, como ABNT NBR 6023;
    4+ autores (ou elipse "..." no registro) → 1º autor + " et al.";
    autores institucionais com parênteses → nome pleno + sigla;
    consórcio ("&") → nome pleno sem vírgula; sem autor → entrada por título.
  - Ano ausente → [s.d.]. Localizador: DOI > URL > PMID > PMCID.
  - Ordenação alfabética por (autor|título, título, evidence_id).
  - Cada entrada termina com [evidence:Exxx] — a etiqueta devolve ao registro.
Saída: escrita-zero/rascunhos/c14_referencias.md
"""
import json
import re
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
MANIFEST = REPO / "paper" / "evidence_workspace" / "source_manifest.json"
OUT = REPO / "escrita-zero" / "rascunhos" / "c14_referencias.md"

MESES = {
    "01": "jan.", "02": "fev.", "03": "mar.", "04": "abr.", "05": "maio",
    "06": "jun.", "07": "jul.", "08": "ago.", "09": "set.", "10": "out.",
    "11": "nov.", "12": "dez.",
}

SEM_AUTOR = "(autores nao retornados)"


def _iniciais(resto: str) -> str:
    out: list[str] = []
    for t in resto.replace(",", " ").split():
        t = t.strip(".")
        if not t:
            continue
        if t.upper() == t and len(t) <= 3:  # sigla de iniciais: DF -> D. F.
            out.extend(letra + "." for letra in t)
        else:  # nome completo: Simon -> S.
            out.append(t[0].upper() + ".")
    return " ".join(out)


def fmt_autor(a: str) -> tuple[str | None, bool]:
    """→ (autor formatado, tinha 'et al.' no registro)."""
    a = a.replace("【", "").replace("】", "").strip()
    etal = bool(re.search(r"\s+et\s+al\.?\s*$", a))
    a = re.sub(r"\s+et\s+al\.?\s*$", "", a)  # 'Nishimura Y et al.' -> 'Nishimura Y'
    if a == SEM_AUTOR or not a:
        return None, etal
    if "&" in a:  # consórcio: nome pleno, sem vírgula
        return re.sub(r"\s+", " ", a.replace(",", " ")).strip().upper(), etal
    m = re.match(r"^(\S+)\s*\((.+)\)\s*$", a)  # institucional: SIGLA (Nome, Pleno)
    if m:
        pleno = re.sub(r"\s+", " ", m.group(2).replace(",", " ")).strip().upper()
        return f"{pleno} ({m.group(1).upper()})", etal
    if "," in a:
        sobrenome, resto = a.split(",", 1)
        return f"{sobrenome.strip().upper()}, {_iniciais(resto.strip())}", etal
    partes = a.split(" ", 1)
    sobrenome = partes[0].upper()
    resto = partes[1] if len(partes) > 1 else ""
    if not resto:
        return sobrenome, etal
    return f"{sobrenome}, {_iniciais(resto)}", etal


def autoria(authors: list[str]) -> str | None:
    pares = [fmt_autor(a) for a in authors]
    autores = [a for a, _ in pares if a]
    if not autores:
        return None
    tem_elipse = any("..." in a or "…" in a for a in authors)
    tinha_etal = any(etal for _, etal in pares)
    if tem_elipse or tinha_etal or len(autores) > 3:
        return autores[0].rstrip(".") + ". et al."
    bloco = "; ".join(autores)
    return bloco if bloco.endswith(".") else bloco + "."


def _data(iso: str) -> str:
    ano, mes, _dia = iso.split("-")
    return f"{_dia} {MESES[mes]} {ano}" if False else f"{int(_dia)} {MESES[mes]} {ano}"


def localizador(x: dict) -> str:
    ids = x.get("identifiers", {})
    verificado = x.get("verification", {}).get("verified_on", "")
    if doi := ids.get("doi"):
        return f"DOI: https://doi.org/{doi}."
    if url := ids.get("url"):
        return f"Disponível em: {url}. Acesso em: {_data(verificado)}."
    if pmid := ids.get("pmid"):
        return f"Disponível em: https://pubmed.ncbi.nlm.nih.gov/{pmid}/. Acesso em: {_data(verificado)}."
    if pmcid := ids.get("pmcid"):
        return f"Disponível em: https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/. Acesso em: {_data(verificado)}."
    raise ValueError(f"{x['evidence_id']}: sem identificador persistente no registro")


def entrada(x: dict) -> str:
    aut = autoria(x.get("authors", []))
    titulo = x["title"].rstrip(". ")
    if not titulo.endswith(("?", "!")):
        titulo += "."
    ano = str(x["year"]) if x.get("year") else "[s.d.]"
    loc = localizador(x)
    corpo = f"{titulo} {ano}. {loc}"
    if aut:
        return f"{aut} {corpo} [evidence:{x['evidence_id']}]\n"
    return f"{titulo.upper()} {ano}. {loc} [evidence:{x['evidence_id']}]\n"


ARTIGOS_INICIAIS = {"a", "an", "the", "o", "os", "as", "um", "uma"}


def chave(x: dict) -> tuple[str, str, str]:
    aut = autoria(x.get("authors", [])) or ""
    norm = lambda s: unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    prim = (aut.split(";")[0] or x["title"]).rstrip(".,")
    if not aut:  # sem autoria: ordena pelo 1º termo significativo (ignora artigo)
        palavras = prim.split()
        idx = next((i for i, p in enumerate(palavras) if p.lower().strip(".,") not in ARTIGOS_INICIAIS), 0)
        prim = " ".join(palavras[idx:])
    return norm(prim), norm(x["title"]), x["evidence_id"]


def main() -> None:
    fontes = json.load(open(MANIFEST, encoding="utf-8"))["sources"]
    entradas = [entrada(x) for x in sorted(fontes, key=chave)]
    intro = (
        "# REFERÊNCIAS\n\n"
        "A lista abaixo foi gerada do registro probatório da tese, sem digitação "
        "manual: cada entrada reproduz os elementos que o registro guarda — "
        "autoria, título, ano e identificador persistente — com ordenação "
        "alfabética pelo primeiro autor e, quando não há autoria declarada, pelo "
        "título, como manda a norma brasileira de referências. O que o registro "
        "não guarda, a entrada não inventa: sem nome de periódico, volume ou "
        "paginação, o identificador persistente — DOI ou endereço resolvido — é o "
        "caminho do leitor até a fonte integral. As fontes que sustentam as claims "
        "da tese aparecem junto às complementares — base bibliográfica de "
        "reposicionamento de fármacos, farmacologia quantitativa e sistemas, "
        "estruturas por criomicroscopia; cada entrada fecha com a etiqueta de "
        "evidência que a devolve ao registro de origem, o mesmo mecanismo de "
        "rastreabilidade usado no corpo do texto.\n\n"
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(intro + "".join(entradas), encoding="utf-8")
    print(f"geradas {len(entradas)} entradas → {OUT}")


if __name__ == "__main__":
    main()
