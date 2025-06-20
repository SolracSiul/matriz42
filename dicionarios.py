**Códigos de Dicionários em Python (Consolidados)**

```python
# Exemplo 1: Criando um dicionário
pessoa = {
    "nome": "João",
    "idade": 15,
    "cidade": "Rio de Janeiro"
}
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cidade"])

# Exemplo 2: Atualizando dados
filme = {
    "título": "Matrix",
    "ano": 1999,
    "diretor": "Wachowski"
}
filme["nota"] = 9.5
filme["ano"] = 2000
print(filme)

# Exemplo 3: Cadastro de alunos
alunos = {
    "aluno1": {"nome": "Ana", "nota": 9},
    "aluno2": {"nome": "Carlos", "nota": 7},
    "aluno3": {"nome": "Beatriz", "nota": 8}
}
for aluno in alunos.values():
    print(f"{aluno['nome']} tirou nota {aluno['nota']}")

# Exemplo 4: Frequência de palavras
frase = "olá mundo olá"
contagem = {}
for palavra in frase.split():
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1
print(contagem)

# Exemplo 5: Todas as formas de iteração
pessoa = {"nome": "Maria", "idade": 30, "cidade": "São Paulo"}

# Chaves
for chave in pessoa:
    print(chave)

# Chaves (explicitamente)
for chave in pessoa.keys():
    print(chave)

# Valores
for valor in pessoa.values():
    print(valor)

# Chaves e valores
for chave, valor in pessoa.items():
    print(chave, ":", valor)

# Exemplo 6: Lista com dicionários
alunos = [
    {"nome": "João", "nota": 7},
    {"nome": "Ana", "nota": 9},
    {"nome": "Pedro", "nota": 6}
]

for aluno in alunos:
    print(f"{aluno['nome']} tirou nota {aluno['nota']}")

for aluno in alunos:
    for chave, valor in aluno.items():
        print(f"{chave}: {valor}")
    print("----")

# Exemplo 7: Dicionários aninhados

turma = [
    {"nome": "João", "disciplinas": {"matemática": 7, "português": 8}},
    {"nome": "Ana", "disciplinas": {"matemática": 10, "português": 9}}
]

for aluno in turma:
    print(f"Aluno: {aluno['nome']}")
    for materia, nota in aluno["disciplinas"].items():
        print(f"  {materia}: {nota}")

# Tarefa de casa resolvida
produto = {
    "nome": "Teclado",
    "preco": 150.0,
    "quantidade": 10
}

valor_total = produto["preco"] * produto["quantidade"]
print(f"O valor total em estoque do produto {produto['nome']} é R$ {valor_total:.2f}")

# array de produtos: 
produtos = [
    {"nome": "Teclado", "preco": 150.0, "quantidade": 10},
    {"nome": "Mouse", "preco": 80.0, "quantidade": 20},
    {"nome": "Monitor", "preco": 1200.0, "quantidade": 5}
]

valor_total_estoque = 0

for produto in produtos:
    total_item = produto["preco"] * produto["quantidade"]
    valor_total_estoque += total_item
    print(f"{produto['nome']}: R$ {total_item:.2f}")

print(f"\nValor total do estoque: R$ {valor_total_estoque:.2f}")

```
