from Classes.Jogador import Jogador

class Tabuleiro:
    def __init__(self) -> None:
        self.tabuleiro = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
    
    def jogar_em(self, lin, col, jogador: Jogador) -> None:
        self.tabuleiro[lin][col] = jogador.get_jogador()
        
    def get_tab(self) -> list[list[str]]:
        return self.tabuleiro
    



if __name__ == "__main__":
    tabuleiro = Tabuleiro()
    while True:
        local = [input("linha:"), input("coluna: ")]
        tabuleiro.jogar_em(local[0], local[1], "x")