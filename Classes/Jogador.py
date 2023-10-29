class Jogador:
    def __init__(self, simbolo: str) -> None:
        self.simbolo = simbolo
        self.qtd_de_jogadas = 0

    def get_jogador(self) -> str:
        return self.simbolo
    
    def get_qtd_jogadas(self) -> int:
        return self.qtd_de_jogadas
    
    def jogou(self) -> None:
        self.qtd_de_jogadas += 1