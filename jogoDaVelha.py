import funcoesJogoDaVelha

vencedor = False
tabuleiro =[
            ["-","-","-"],
            ["-","-","-"],
            ["-","-","-"],
            ]  


while vencedor == False:
    funcoesJogoDaVelha.jogadorX(tabuleiro)
    if funcoesJogoDaVelha.validacao(tabuleiro) == True:
        funcoesJogoDaVelha.imprimirTabuleiro(tabuleiro)
        break
    funcoesJogoDaVelha.jogadorO(tabuleiro)
    if funcoesJogoDaVelha.validacao(tabuleiro) == True:
        funcoesJogoDaVelha.imprimirTabuleiro(tabuleiro)
        break