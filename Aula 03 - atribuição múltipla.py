"""
 atribuição múltipla é uma operação que atribui o mesmo valor a várias variáveis. 
 Em Python, a atribuição múltipla é feita usando o operador de atribuição (=). 
"""

#ATRIBUIÇÃO SIMPLES
nome = "Thales"
idade = 27
estudante = True

print(nome)
print(idade)
print(estudante)

#ATRIBUIÇÃO MÚLTIPLA

name, age, student = "Thales", 27, True
print(name)
print(age)
print(student)

#Variaveis com o mesmo valor
idade_thales = idade_fulano = idade_ciclano = 27
print(idade_thales)
print(idade_fulano)
print(idade_ciclano)