from Classes.Tabuleiro import Tabuleiro
from Classes.Jogador import Jogador
from Classes.Regras import Regras as RegrasDeTabuleiro

class Jogo(RegrasDeTabuleiro):
    def __init__(self, tabuleiro: Tabuleiro, jogador1: Jogador, jogador2: Jogador) -> None:
        super().__init__(tabuleiro, jogador1, jogador2)
        self.numero_de_jogadas = 0
    
    def alguem_venceu(self):
        if self.verificar_tab():
            return self.verificar_tab()
            
        if self.numero_de_jogadas == 9:
            return "empate"
        
        return False

    def quem_joga(self):
        if self.numero_de_jogadas % 2 == 0:
            return self.jogador1
        return self.jogador2
    
    def jogar(self, lin, col, jogador: Jogador):
        if not self.jogada_valida([lin, col]):
            return self.jogada_valida([lin, col])
        
        self.tabuleiro.jogar_em(lin, col, jogador)
        
        jogador.jogou()
        self.numero_de_jogadas += 1

        return True