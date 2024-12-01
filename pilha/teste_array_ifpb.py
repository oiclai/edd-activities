from pilha.array_ifpb import Array


def test_array():
    array = Array(10, int)
    assert len(array) == 10
    assert array[0] is None
    array[1] = 100
    assert array[1] == 100
    array = Array(2, int)
    array[1] = 70
    assert str(array) == "[None, 70]"




if __name__ == "__main__":
    test_array()
