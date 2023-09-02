"""
uma variável é um espaço na memória do computador reservado para armazenar um valor. 
As variáveis são usadas para armazenar dados que podem ser alterados durante a execução do programa.

As variáveis são definidas usando o operador igual (=). O lado esquerdo do operador de atribuição é 
o nome da variável, e o lado direito é o valor que será armazenado na variável.
"""

#TIPO STRING
#String: Representa uma sequência de caracteres.
#declarando uma variavel que recebe uma string.
nome = "Thales"
print(nome)
#printando olá mais a variavel nome
print("Olá " + nome)
#printando o tipo dessa varivel
print(type(nome))

first_name = "Thales"
last_name = "Abdon"
full_name = first_name + " " + last_name
print(full_name)

#TIPO INTEIRO
#Integer: Representa um número inteiro.
idade = 27
idade += 1
print(idade)
print(type(idade))
print("Sua idade é:",idade)

#TIPO FLOAT
#Float: Representa um número de ponto flutuante.
peso = 1.7
print(peso)
print(type(peso))

#TIPO BOOLEAN
#Boolean: Representa um valor booleano (verdadeiro ou falso).
animal = False
print("Você é um humano?",animal)
print(type(animal))