# O for loop em Python é usado para iterar sobre uma sequência
# essa sequência pode ser uma lista, uma tupla, um dicionário, um conjunto ou uma string
# while loop = quando não temos limitação de loops.
# for loop = quando temos uma limitação do loop.

import time


for i in range(10):
    print(i+1)

for aux in range(50, 100, 2):
    print(aux)

for x in "Thales":
    print(x)

for segundos in range(10, 0, -1):
    print(segundos)
    time.sleep(1)
print("feliz Natal!")
