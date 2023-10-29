class Jogador:
    def __init__(self, simbolo: str) -> None:
        self.simbolo = simbolo
        self.qtd_de_jogadas = 0

    def get_jogador(self):
        return self.simbolo
    
    def get_qtd_jogadas(self):
        return self.qtd_de_jogadas
    
    def jogou(self):
        self.qtd_de_jogadas += 1