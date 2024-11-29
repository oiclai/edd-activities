from pilha import Pilha, PilhaVaziaException


def test_pilha():
    p = Pilha()
    assert p.estah_vazia is True
    assert p.tamanho == 0
    assert len(p) == 0
    assert str(p) == "[]"
    p.empilhar(70)
    assert p.tamanho == 1
    assert p.estah_vazia is False
    assert str(p) == "[70]"
    p.empilhar(99)
    assert str(p) == "[99, 70]"
    p.empilhar(200)
    assert len(p) == 3
    valor = p.desempilhar()
    assert valor == 200, f"{valor}"
    assert p.desempilhar() == 99
    assert p.desempilhar() == 70
    assert p.estah_vazia is True
    try:
        p.desempilhar()
        assert False, "Não levantou a exceção"
    except PilhaVaziaException:
        pass




if __name__ == "__main__":
    test_pilha()
