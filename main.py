from Classes.Jogo import Jogo, Tabuleiro, Jogador

if __name__ == "__main__":

    tabuleiro = Tabuleiro()
    jogador1 = Jogador("x")
    jogador2 = Jogador("o")
    jogo = Jogo(tabuleiro, jogador1, jogador2)

    while not jogo.alguem_venceu():
        print(f'vez do jogador {jogo.quem_joga().get_jogador()}')
        local = {
            "lin": int(input("linha: ")),
            'col': int(input('colona: ')) 
        }
        jogo.jogar(local["lin"], local["col"], jogo.quem_joga())

        jogo.exibir_jogo()