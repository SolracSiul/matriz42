# === AULA DE MATRIZ EM PYTHON - PARTE TEÓRICA ===

# 1. O que é uma matriz?
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2. Como criar uma matriz?

# a) Manualmente
matriz_manual = [
    [1, 2, 3],
    [4, 5, 6]
]

# b) Usando for e range
linhas = 3
colunas = 4
matriz_for = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(0)
    matriz_for.append(linha)

print("Matriz criada com for e range:")
print(matriz_for)

# c) Usando list comprehension
matriz_lc = [[0 for j in range(colunas)] for i in range(linhas)]
print("Matriz criada com list comprehension:")
print(matriz_lc)

# d) Com números aleatórios
import random
matriz_random = [[random.randint(1, 10) for j in range(colunas)] for i in range(linhas)]
print("Matriz criada com números aleatórios:")
for linha in matriz_random:
    print(linha)

# 3. Como percorrer uma matriz
print("Percorrendo matriz_random:")
for i in range(len(matriz_random)):
    for j in range(len(matriz_random[0])):
        print(f"Elemento na posição [{i}][{j}]: {matriz_random[i][j]}")

# Alternativa simplificada
for linha in matriz_random:
    for elemento in linha:
        print(elemento)

# 4. Como inserir um elemento
matriz_random[1][2] = 99  # Substitui o elemento na linha 1, coluna 2
print("Matriz após inserção:")
print(matriz_random)

# Adicionar uma nova linha
nova_linha = [10, 11, 12]
matriz_random.append(nova_linha)
print("Matriz após adicionar nova linha:")
print(matriz_random)

# Adicionar um elemento no final de uma linha
matriz_random[0].append(13)
print("Matriz após adicionar elemento na primeira linha:")
print(matriz_random)

# 5. Como deletar elementos
# Remover elemento específico
del matriz_random[1][2]
print("Matriz após deletar elemento [1][2]:")
print(matriz_random)

# Remover uma linha inteira
del matriz_random[1]
print("Matriz após deletar linha 1:")
print(matriz_random)

# Limpar a matriz
matriz_random.clear()
print("Matriz após limpar tudo:")
print(matriz_random)

# 6. Operações importantes

# Criar matriz para operar
matriz_op = [[random.randint(1, 10) for j in range(3)] for i in range(3)]

# a) Somar todos os elementos
soma = 0
for linha in matriz_op:
    for elemento in linha:
        soma += elemento
print("Matriz de operação:")
for linha in matriz_op:
    print(linha)
print(f"Soma dos elementos: {soma}")

# b) Maior e menor elemento
maior = matriz_op[0][0]
menor = matriz_op[0][0]
for linha in matriz_op:
    for elemento in linha:
        if elemento > maior:
            maior = elemento
        if elemento < menor:
            menor = elemento
print(f"Maior elemento: {maior}, Menor elemento: {menor}")

# c) Contar elementos
cont = 0
for linha in matriz_op:
    cont += len(linha)
print(f"Total de elementos: {cont}")