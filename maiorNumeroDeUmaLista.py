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

for i in range(len(lista_de_numeros)):
    if (lista_de_numeros[i] >= maior_numero):
        maior_numero = lista_de_numeros[i]

print(maior_numero)
