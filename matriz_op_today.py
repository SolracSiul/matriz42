matriz_list = [[j for j in range(3)] for i in range(3)]
matriz = []

for i in range(3):         
    linha = []
    for j in range(3):     
        linha.append(j)    
    matriz.append(linha)   

#soma na linha
""" soma na linha
linha = 1
soma = 0

for j in range(3): 
    soma += matriz[linha][j]

print("Soma da linha:", soma)

"""
#soma na coluna
"""
    coluna = 2
    soma = 0

    for i in range(3):  # percorre todas as linhas
        soma += matriz[i][coluna]

    print("Soma da coluna:", soma)
"""
#soma na diagonal:
"""
    soma = 0

    for i in range(3):
        soma += matriz[i][i]

    print("Soma da diagonal primária:", soma)
"""
#soma na diagonal secundária:
"""
    soma = 0

    for i in range(3):
        soma += matriz[i][2 - i]

    print("Soma da diagonal secundária:", soma)
"""
#explicação disso:
"""

| i (linha) | coluna = 2 - i | matriz\[i]\[2 - i] |

| 0         | 2 - 0 = 2      | matriz\[0]\[2]     |
| 1         | 2 - 1 = 1      | matriz\[1]\[1]     |
| 2         | 2 - 2 = 0      | matriz\[2]\[0]     |

"""