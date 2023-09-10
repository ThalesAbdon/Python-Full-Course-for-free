from collections import Counter

# Defina os 4 arrays de 15 números cada
array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
array2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
array3 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
array4 = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 1, 2, 3, 4]

# Combine todos os números em uma única lista
todos_numeros = array1 + array2 + array3 + array4

# Conte a frequência de cada número
frequencia_numeros = Counter(todos_numeros)

# Ordene os números com base em suas frequências em ordem crescente
numeros_ordenados = sorted(
    frequencia_numeros, key=lambda x: frequencia_numeros[x])

# Selecione os 15 primeiros números da lista ordenada
quinze_menos_frequentes = numeros_ordenados[:15]

# Imprima os 15 números menos frequentes
print(sorted(quinze_menos_frequentes))
