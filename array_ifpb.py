class ErroTipo(Exception):
    pass




class Array:


    def __init__(self, tamanho, tipo):
        self.__tamanho = tamanho
        self.__tipo = tipo
        self.__dados = [None for x in range(tamanho)]


    def __len__(self):
        return self.__tamanho


    def __getitem__(self, item):
        return self.__dados[item]


    def __setitem__(self, item, value):
        if not isinstance(item, self.__tipo):
            raise ErroTipo("Tipo inválido")
        self.__dados[item] = value


    def __repr__(self):
        return repr(self.__dados)
