valor = float(input("digite o valor monetário\n"))
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0

moedas1 = 0
moedas50 = 0
moedas25 = 0
moedas10 = 0
moedas005 = 0
moedas001 = 0

while (valor > 0):
    while (valor >= 100):
        valor -= 100
        print(valor)
        nota100 += 1
    while (valor >= 50):
        valor -= 50
        print(valor)
        nota50 += 1
    while (valor >= 20):
        valor -= 20
        print(valor)
        nota20 += 1
    while (valor >= 10):
        valor -= 10
        print(valor)
        nota10 += 1
    while (valor >= 5):
        valor -= 5
        print(valor)
        nota5 += 1
    while (valor >= 2):
        valor -= 2
        print(valor)
        nota2 += 1
    while (valor >= 1):
        valor -= 1
        print(valor)
        moedas1 += 1
    while (valor >= 0.5):
        valor -= 0.50
        print(valor)
        moedas50 += 1
    while (valor >= 0.25):
        valor -= 0.25
        print(valor)
        moedas25 += 1
    while (valor > 0.10):
        valor -= 0.10
        print(valor)
        moedas10 += 1

print("NOTAS:")
print(nota100)
print(nota50)
print(nota20)
print(nota10)
print(nota5)
print(nota2)
print("MOEDAS:")
print(moedas1)
print(moedas50)
print(moedas25)
print(moedas10)
print(moedas005)
print(moedas001)
