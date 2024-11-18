from enum import IntEnum;

class NumJogadoresInvalido(Exception):
    pass


class Naipe(IntEnum):
    PAUS = 1
    OUROS = 2
    COPAS = 3
    ESPADAS = 4


class Carta:
    AS = 1
    VALETE = 11
    DAMA = 12
    REI = 13


    def __init__(self, valor: int, naipe: Naipe):
        self.__valor: int = valor
        self.__naipe: Naipe = naipe


    def __eq__(self, outra:'Carta') -> bool:
        return self.valor == outra.valor


    def __gt__(self, outra:'Carta') -> bool:
        return self.valor > outra.valor


    def __repr__(self):
        return f'{self._get_valor_as_str()} de {self.__naipe.name.title()}'


    def _get_valor_as_str(self):
        if self.__valor == 1:
            return 'Às'
        elif 2 <= self.__valor <= 10:
            return str(self.__valor)
        elif self.__valor == 11:
            return 'Valete'
        elif self.__valor == 12:
            return 'Dama'
        elif self.__valor == 13:
            return 'Rei'
        else:
            raise ValueError("Valor de carta inválido")


    @property
    def valor(self):
        
        return self.__valor