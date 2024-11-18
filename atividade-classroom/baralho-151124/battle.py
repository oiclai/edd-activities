from players import Jogador; from createDeckOfCards import Baralho; from predefCard import Carta
class Jogo:


    def __init__(self, numero_jogadores: int, n_max_rodadas: int = 100):
        self.__baralho: Baralho = Baralho()
        self.__numero_jogadores = numero_jogadores
        self.__jogador_a: Jogador = Jogador(input(f"Informe o nome do jogador 1: "))
        self.__jogador_b: Jogador = Jogador(input(f"Informe o nome do jogador 2: "))
        self.__baralho.embaralhar()
        self.__baralho.distribuir([self.__jogador_a, self.__jogador_b])
        self.__pilha: list[Carta] = []
        self.__n_max_rodadas:int = n_max_rodadas
        self._n_rodada:int = 1


    def rodada(self) -> Jogador|None:
        print("#" * 20)
        self.exibir_total_cartas()
        vencedor = None
        carta_a = self.__jogador_a.remover_carta()
        print(f"{self.__jogador_a} tirou a carta {carta_a}")
        carta_b = self.__jogador_b.remover_carta()
        print(f"{self.__jogador_b} tirou a carta {carta_b}")
        if carta_a > carta_b:
            vencedor = self.__jogador_a
        elif carta_b > carta_a:
            vencedor = self.__jogador_b
        else:
            self.__pilha.append(carta_a)
            self.__pilha.append(carta_b)


        if vencedor:
            vencedor.add_carta_na_base(carta_a)
            vencedor.add_carta_na_base(carta_b)
            for carta in self.__pilha:
                vencedor.add_carta_na_base(carta)
            self.__pilha = []
        return vencedor


    def run(self):


        while not self.__eh_hora_parar():
            self._n_rodada += 1
            vencedor = self.rodada()
            if vencedor:
                print(f"O vencedor da rodada #{self._n_rodada} é {vencedor}")
            else:
                print("A rodada deu empate")


        vencedor_jogo = None
        if self.__jogador_a.total_cartas > self.__jogador_b.total_cartas:
            vencedor_jogo = self.__jogador_a
        elif self.__jogador_a.total_cartas < self.__jogador_b.total_cartas:
            vencedor_jogo = self.__jogador_b


        if vencedor_jogo:
            print(f"O vencedor do jogo é {vencedor_jogo}")
            self.exibir_total_cartas()
        else:
            print("O jogo deu empatado")


    def __eh_hora_parar(self) -> bool:
        if not self.__jogador_a.possui_cartas:
            return True
        if not self.__jogador_b.possui_cartas:
            return True
        if self._n_rodada >= self.__n_max_rodadas:
            return True
        return False


    def exibir_total_cartas(self):
        print(f"{self.__jogador_a}: {self.__jogador_a.total_cartas} cartas")
        print(f"{self.__jogador_b}: {self.__jogador_b.total_cartas} cartas")




if __name__ == "__main__":
    jogo = Jogo(numero_jogadores=2, n_max_rodadas=2000)
    jogo.run()
