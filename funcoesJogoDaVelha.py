import os
from ssl import VerifyFlags

def imprimirTabuleiro(lista):
    for y in range(len(lista)):
        for i in range(len(lista)):
            print(lista[y][i],end=" ")
        print("")

def validacao(lista):
    #variaveis usadas para validar
    diagonal1 = []
    diagonal2 = []
    vertical1 = []
    vertical2 = []
    vertical3 = []
    horizontal1 = []
    horizontal2 = []
    horizontal3 = []

    #loops para montar listas para verificar
    for a in range(len(lista)):
        diagonal1.append(lista[a][a])
    for b in range(len(lista)):
        x = 2
        diagonal2.append(lista[b][x-b])
    for c in range(len(lista)):
        vertical1.append(lista[c][0])
    for d in range(len(lista)):
        vertical2.append(lista[d][1])
    for e in range(len(lista)):
        vertical3.append(lista[e][2])
    for f in range(len(lista)):
        horizontal1.append(lista[0][f])
    for g in range(len(lista)):
        horizontal2.append(lista[1][g])
    for h in range(len(lista)):
        horizontal3.append(lista[2][h])

    
    #verificando listas montadas
    if diagonal1.count("x") == 3 or diagonal1.count("o") == 3:
        print(f"\nVencedor: jogador {diagonal1[0]}")
        return True
    elif diagonal2.count("x") == 3 or diagonal2.count("o") == 3:
        print(f"\nVencedor: jogador {diagonal2[0]}")
        return True
    elif vertical1.count("x") == 3 or vertical1.count("o") == 3:
        print(f"\nVencedor: jogador {vertical1[0]}")
        return True
    elif vertical2.count("x") == 3 or vertical2.count("o") == 3:
        print(f"\nVencedor: jogador {vertical2[0]}")
        return True
    elif vertical3.count("x") == 3 or vertical3.count("o") == 3:
        print(f"\nVencedor: jogador {vertical3[0]}")
        return True
    elif horizontal1.count("x") == 3 or horizontal1.count("o") == 3:
        print(f"\nVencedor: jogador {horizontal1[0]}")
        return True
    elif horizontal2.count("x") == 3 or horizontal2.count("o") == 3:
        print(f"\nVencedor: jogador {horizontal2[0]}")
        return True
    elif horizontal3.count("x") == 3 or horizontal3.count("o") == 3:
        print(f"\nVencedor: jogador {horizontal3[0]}")
        return True


def jogadorX(lista):
    imprimirTabuleiro(lista)

    vezJogador = list(input("\nJogador X , informe a linha e a coluna separado por uma virgula: "))
    try:
        while True:
            vezJogador.remove(',')
    except ValueError:
        pass
    
    linha = int(vezJogador[0])
    coluna = int(vezJogador[1])
    
    lista[linha-1][coluna-1] = "x"
    os.system("cls")

def jogadorO(lista):
    imprimirTabuleiro(lista)

    vezJogador = list(input("\nJogador O , informe a linha e a coluna separado por uma virgula: "))
    try:
        while True:
            vezJogador.remove(',')
    except ValueError:
        pass
    
    linha = int(vezJogador[0])
    coluna = int(vezJogador[1])
    
    lista[linha-1][coluna-1] = "o"
    os.system("cls")