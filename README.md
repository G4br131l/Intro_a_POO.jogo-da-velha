# Introdução a POO com jogo-da-velha

Essa é minha primeira aplicação dos conceitos de POO, então as classes devem estar meio estranhas os metodos e nomes também, haverão atualizações.

## Como funciona 

A *main.py* faz todo o gerenciamento do jogo, criando as instâcias e gerenciando as entradas e saídas, mas de uma forma bem mesquinha.

Quando executasse a main.py ele pedira a linha e em seguida a coluna para o primeiro jogador, depois para o segundo até o fim do jogo. aqui vai um exemplo:

> vez do jogador x  
 linha: 1  
 colona: 1  
 &nbsp; |&nbsp; |   
 \-----  
 &nbsp; |x|   
 \-----  
 &nbsp; |&nbsp; |   
 vez do jogador o  
 linha: 0  
 colona: 0  
 o|&nbsp; |&nbsp;   
 \-----  
 &nbsp; |x|   
 \-----  
 &nbsp; |&nbsp; |   

Se alguem ganhar ou der empate ele simplemente para, mas o método verifica se houve vitoria ou empate, e por falar em método.

## Classes

Existem 5 classes aqui, *Jogador, Tabuleiro, Interface, Regras* e *Jogo*

### Jogador 

Jogador te como função representar o jogador.

|Jogador|
|:---|
|**atributos**|
|`simbolo`|
|`qtd_de_jogadas`[^1]|
|**métodos**|
|`get_jogador()`|
|`get_qtd_de_jogadas()`|
|`jogou()`|

bem auto-explicativo
- `get_jogador() -> str` retorna o simbolo do jogador
- `get_qtd_de_jogadas() -> int` retorna a quantidade de jogadas
- `jogou() -> None` apenas acresenta 1 a `qtd_de_jogadas`

[^1]: esse atributo é inútil por enquanto, tenho planos futuros para ele.

### Tabuleiro

Função: representar um abstração do tabuleiro, sem regras ou alguma forma de apresentar ele ao usuário.

| Tabuleiro     |
|:--------------|
| **atributos** |
| `tabuleiro`   |
| **métodos**   |
| `jogar_em()`  |
| `get_tab()`   |

- `tabuleiro` é a abstração de tabuleiro que não precisa ser inicializada
- `jogar_em(linha: int, coluna: int, jogador: Jogador) -> None` coloca o jogador na posição linha e coluna passada
- `get_tab() -> list[list[str]]` retorna o tabuleiro

### Interface

Interface faz referência a parte "grafica" do jogo, controla a colocação e a sobreposição de "peças" e exibe o tabuleiro, sem nenhuma verificação de regra

| Interface         |
|-------------------|
| **atributos**     |
| `tabuleiro`       |
| **métodos**       |
| `exibir_jogo()`   |
| `jogar()`         |
| `jogada_valida()` |

- `Interface(tabuleiro: Tabuleiro) -> None` deve ser instaceada assim
- `exibir_jogo() -> None` sem parâmetros, apenas exibe o jogo
- `jogar(linha: int, coluna: int, jogador) -> bool` insere o simbolo do jogador no jogo, se possivel, retorna `True` se for possivel

### Regras

Regras abstrai as regras do jogo, é uma subclasse de Interface, ela verifica se o jogo chegou ao final ou não

Interface <- Regras
| Regras               |
|----------------------|
| **atributos**        |
| `jogador1`           |
| `jogador2`           |
| **métodos**          |
| `verificar_tab()`    |
| `linha_e_diagonal()` |

- `Regras(tabuleiro: Tabuleiro, jogador1: Jogador, jogador2: Jogador)` deve ser instanceada assim
- `verificar_tab()` varifica se algum jogador venceu a partida, retorna o jogador vencedor, se não houver, `False`
- `linha_e_diagonal()`[^2] é um método estatico e auxilia `verificar_tab()`

[^2]: eu queria que fosse um método privado, mas as outras classes não herdariam ele, então por praticidade ele não é.

### Jogo

É a abstração do jogo, é uma subclasse de Regras, ela controla quem joga, valida as jogadas e verifica se houve uma vitoria derrota ou empate.

Regras <- Jogo
| Jogo                |
|---------------------|
| **atributos**       |
| `numero_de_jogadas` |
| **métodos**         |
| `alguem_venceu()`   |
| `quem_joga()`       |
| `jogar()`           |

- `Jogo(tabuleiro: Tabuleiro, jogador1: Jogador, jogador2: Jogador) -> None` deve ser instanceada assim
- `numero_de_jogadas` conta todas as jogadas da partida
- `jogar(linha: int, colona: int, jogador: Jogador) -> bool` tem algumas alterações do `jogo()` da interface, mas no fim faz o mesmo com algumas verificações a mais
- `quem_joga() -> Jogador` diz de quem é a vez de jogar
- `alguem_venceu()` se não houver vencedor retorna `False`, se houver retorna o jogador vencedor ou `"empate"`