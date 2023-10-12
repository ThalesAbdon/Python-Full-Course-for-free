import random
lista_de_numeros = [
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
]
print(lista_de_numeros)
maior_numero = lista_de_numeros[len(lista_de_numeros) - 1]

for i in lista_de_numeros:
    if (i >= maior_numero):
        maior_numero = i

print(maior_numero)
