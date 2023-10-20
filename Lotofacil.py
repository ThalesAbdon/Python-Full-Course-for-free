# Apenas um programa para auxiliar meu pai que faz aquela fézinha na lotofacil!
# Tem o objetivo de facilitar na hora de checkar o número de acerto!
sorteados_original = [1, 4, 7, 8, 9, 11, 12, 14, 15, 16, 17, 21, 22, 23, 24]
sorteados_ordenados = sorted(sorteados_original)

lista1 = [2, 3, 5, 9, 10, 11, 12, 13, 14, 19, 20, 21, 23, 24, 25]
lista2 = [1, 3, 4, 5, 6, 7, 8, 9, 11, 12, 16, 17, 18, 24, 25]
lista3 = [1, 2, 3, 5, 7, 10, 14, 15, 16, 17, 19, 20, 21, 22, 25]
lista4 = [1, 3, 8, 9, 10, 11, 12, 13, 15, 18, 20, 21, 23, 24, 25]
lista5 = [4, 5, 6, 7, 8, 9, 11, 13, 14, 17, 18, 19, 20, 21, 22]
listaT1 = [3, 4, 5, 7, 10, 11, 13, 14, 16, 18, 19, 21, 22, 24, 25]
listaT2 = [1, 2, 5, 6, 8, 9, 12, 14, 15, 17, 18, 20, 21, 23, 25]
listaT3 = [1, 4, 5, 6, 8, 9, 11, 12, 16, 19, 202, 21, 23, 24, 25]
numeros_iguais = 0

for numero in sorteados_ordenados:
    if numero in lista5:
        numeros_iguais += 1

print(f"Número de números iguais: {numeros_iguais}")
