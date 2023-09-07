"""
Funções matemáticas são funções que realizam operações matemáticas. 
Em Python, as funções matemáticas são definidas no módulo math
"""
import math

pi = 3.14159265

# Arredonda um número para um número específico de dígitos.
print(round(pi, 4))
# retorna o menor inteiro maior ou igual a um número
print(math.ceil(pi))
# retorna o maior inteiro menor ou igual a um número
print(math.floor(pi))
# retorna o valor absoluto de um número
print(abs(pi))
# eleva um número a uma potência
print(pow(pi, 2))
# retorna a raiz quadrada de um número
print(math.sqrt(400))

x = int(input("digite o valor de x: "))
y = int(input("digite o valor de y: "))
z = int(input("digite o valor de z: "))


def max_num(x, y, z):
    if ((x > y) and (x > z)):
        print(x)
    elif ((y > x) and (y > z)):
        print(y)
    else:
        print(z)


max_num(x, y, z)
# retorna o maior valor de um conjunto de valores
print(max(x, y, z))
# retorna o menor valor de um conjunto de valores
print(min(x, y, z))
