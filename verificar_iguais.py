import random

linhas = 3
colunas = 3

matriz_lc = [[random.randint(1, 9) for j in range(colunas)] for i in range(linhas)]

# Exibindo a matriz
for linha in matriz_lc:
    print(linha)


iguais = True
valor_referencia = matriz[0][0]  
#diagonal
for i in range(1, 3):  
    if matriz[i][i] != valor_referencia:
        iguais = False
        break  
if iguais:
    print("Todos os elementos da diagonal primária são iguais!")
else:
    print("Os elementos da diagonal primária são diferentes.")