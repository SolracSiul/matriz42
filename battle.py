#simple battle 

import random

tabuleiro = [["~" for j in range(3)] for i in range(3)]
for linha in tabuleiro:
    print(linha)
lugares_corretos = []
while len(lugares_corretos) < 3:
    linha_gerada = random.randint(0,2)
    coluna_gerada = random.randint(0,2)
    tuplinha = (linha_gerada, coluna_gerada)
    if tuplinha not in lugares_corretos:
        lugares_corretos.append(tuplinha)

print("meus lugares corretos são: ", lugares_corretos)

def mostrarTabela():
    for linha in tabuleiro:
        print(" | ".join(linha))
acertos = 0
palpites = 0
mostrarTabela()
while acertos < 3 and palpites < 6:
    print("Vamos jogar: ")
    print("Digite a coordenada onde vc acha que está as bombas")
    alvo_linha = int(input("Informe a linha que deseja acertar: "))
    alvo_coluna = int(input("informe a coluna que deseja acertar: "))
    minha_tuplinha = (alvo_linha, alvo_coluna)
    if minha_tuplinha in lugares_corretos:
        tabuleiro[minha_tuplinha[0]][minha_tuplinha[1]] = 'N'
        acertos +=1
    else:
        tabuleiro[minha_tuplinha[0]][minha_tuplinha[1]] = 'X'
    palpites+=1
    mostrarTabela()
print("tabuleiro depois da lapada seca")
