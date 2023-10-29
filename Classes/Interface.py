from Classes.Tabuleiro import Tabuleiro

class Interface:
    def __init__(self, tabuleiro: Tabuleiro) -> None:
        self.tabuleiro = tabuleiro

    def exibir_jogo(self):
        tabuleiro = self.tabuleiro.get_tab()

        print('|'.join(tabuleiro[0]))
        print('-' * 5)
        print('|'.join(tabuleiro[1]))
        print('-' * 5)
        print('|'.join(tabuleiro[2]))

    def jogar(self, local: list):
        if not self.__jogada_valida(local):
            return False
        return True

    def jogada_valida(self, local):
        if self.tabuleiro.get_tab()[local[0]][local[1]] == ' ':
            return True
        return False
        




if __name__ == "__main__":
    from Classes.Jogador import Jogador
    
    def quem_joga(j1: Jogador, j2: Jogador):
        if j1.get_qtd_jogadas() == j2.get_qtd_jogadas():
            return j1.get_qtd_jogadas
        else:
            return j2.get_qtd_jogadas
    
    def acabou(j1: Jogador, j2: Jogador):
        if j1.get_qtd_jogadas() + j2.get_qtd_jogadas() == 9:
            return True
        return False

    tabuleiro = Tabuleiro()
    jogador1 = Jogador("x")
    jogador2 = Jogador("o")
    interface = Interface(tabuleiro, jogador1, jogador2)

    while not acabou(jogador1, jogador2):
        print(f'vez de {quem_joga(jogador1, jogador2).get_jogador()}')
        local = [int(input("linha: ")), int(input("coluna: "))]
        interface.jogar(local)

    print('acabou')    