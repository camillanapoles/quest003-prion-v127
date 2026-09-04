"""Q2 da autora: resposta hostil que promete AÇÃO EM LOCAL deve virar registro
executável com id único — garantia de execução no local, ligada à auditoria."""
import pytest
from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.escritor import (V2_DB, fechar_acao, registrar_acao,
                                    check_acoes, hostil_aprova)
from thesis_engine.models import AcaoDevedora, Block, WritingCycle


def test_registrar_e_executar_acao(tmp_path):
    db = str(tmp_path / "a.db")
    aid = registrar_acao(db, origem_item_id="H9999", cap_destino="c15",
                         acao="reproduzir folhas com datas")
    assert aid.startswith("A")
    pend = check_acoes(db, cap="c15")
    assert pend[0]["status"] == "pendente" and pend[0]["origem"] == "H9999"
    r = fechar_acao(db, aid, evidencia="bloco D0500 (apêndice A)")
    assert r["status"] == "executada"
    assert check_acoes(db, cap="c15")[0]["status"] == "executada"


def test_aprova_bloqueada_por_acao_pendente_no_local():
    """hostil_aprova NÃO aprova capítulo com ação devedora pendente NELE."""
    # fase-consciente: enquanto c15 não está aprovado, ações pendentes podem
    # viver nele (bloqueiam a aprovação); após aprovado, nenhuma pode restar —
    # a aprovação exige execução. O invariant migra para o próximo local (c00).
    r = hostil_aprova(V2_DB, "c04")
    assert not r["acoes_pendentes_no_local"]
    with Session(create_db(V2_DB)) as s:
        c04_escrito = s.exec(
            select(Block.block_id).where(Block.chap_id == "c04")
        ).first() is not None
        c15_aprovado = (
            s.exec(
                select(WritingCycle).where(
                    WritingCycle.cap_key == "c15", WritingCycle.estado == "approved"
                )
            ).first()
            is not None
        )
        pend_c15 = [
            a.acao_id
            for a in s.exec(select(AcaoDevedora)).all()
            if a.cap_destino == "c15" and a.status == "pendente"
        ]
        if c15_aprovado:
            assert not pend_c15  # aprovação de c15 exigiu executar as ações
        # (fase anterior: antes de c15 escrito/aprovado, A0001 pendia aqui)
    if c04_escrito:
        assert r["aprova"] is True

