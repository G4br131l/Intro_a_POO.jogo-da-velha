from Classes.Interface import Interface
from Classes.Tabuleiro import Tabuleiro
from Classes.Jogador import Jogador

class Regras(Interface):
    def __init__(self, tabuleiro: Tabuleiro, jogador1: Jogador, jogador2: Jogador) -> None:
        super().__init__(tabuleiro)
        self.jogador1 = jogador1
        self.jogador2 = jogador2


    def verificar_tab(self):
        jogadores = [self.jogador1.get_jogador(), self.jogador2.get_jogador()]
        tab = self.tabuleiro.get_tab()
 
        tab_inverso = [[' ' for _ in range(len(tab))] for _ in range(len(tab[0]))]
        for i in range(len(tab)):
            for j in range(len(tab[0])):
                tab_inverso[j][i] = tab[i][j]


        if self.linha_e_diagonal(jogadores, tab):
            return self.linha_e_diagonal(jogadores, tab)

        if self.linha_e_diagonal(jogadores, tab_inverso):
            return self.linha_e_diagonal(jogadores, tab_inverso)
            
        return False
    
    @staticmethod   
    def linha_e_diagonal(jogadores: list[str], tabuleiro: list[list[str]]) -> bool:
        for jogador in jogadores:
            if [jogador] * 3 in tabuleiro:
                return jogador
            
        diagonal = False  
        for jogador in jogadores:
            for i in range(3):
                if jogador == tabuleiro[i][i]:
                    diagonal = True
                else:
                    diagonal = False
                    break
            if diagonal:
                return jogador
            
        return False