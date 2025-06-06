#list comprehension:
lista = [j for j in range(3)]

#sem list comprehension:
lista = []
for j in range(3):
    lista.append(j)

print([x for x in range(3)])

#pares verificando
pares = [x for x in range(10) if x % 2 == 0]

#quadrados:
quadrados = [x**2 for x in range(5)]


#duplicando strings:
palavras = ['oi', 'tchau', 'legal']
eco = [p * 2 for p in palavras]