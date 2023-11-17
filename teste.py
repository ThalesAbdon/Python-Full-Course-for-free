valor = float(input(""))
nota_100 = nota_50 = nota_20 = nota_10 = nota_5 = nota_2 = 0
moeda_1 = moeda_050 = moeda_025 = moeda_010 = moeda_005 = moeda_001 = 0
while valor >= 0:
    if valor >= 100:
        valor -= 100
        nota_100 += 1
    elif valor >= 50:
        valor -= 50
        nota_50 += 1
    elif valor >= 20:
        valor -= 20
        nota_20 += 1
    elif valor >= 10:
        valor -= 10
        nota_10 += 1
    elif valor >= 5:
        valor -= 5
        nota_5 += 1
    elif valor >= 2:
        valor -= 2
        nota_2 += 1
    elif valor >= 1:
        valor -= 1
        moeda_1 += 1
    elif valor >= 0.50:
        valor -= 0.50
        moeda_050 += 1
    elif valor >= 0.25:
        valor -= 0.25
        moeda_025 += 1
    elif valor >= 0.10:
        valor -= 0.10
        moeda_010 += 1
    elif valor >= 0.05:
        valor -= 0.05
        moeda_005 += 1
    elif valor >= 0.02:
        valor -= 0.02
        moeda_001 += 1

print("NOTAS:")
print(nota_100, "nota(s) de R$ 100.00")
print(nota_50, "nota(s) de R$ 50.00")
print(nota_20, "nota(s) de R$ 20.00")
print(nota_10, "nota(s) de R$ 10.00")
print(nota_5, "nota(s) de R$ 5.00")
print(nota_2, "nota(s) de R$ 2.00")
print("MOEDAS:")
print(moeda_1, "moeda(s) de R$ 1.00")
print(moeda_050, "moeda(s) de R$ 0.50")
print(moeda_025, "moeda(s) de R$ 0.25")
print(moeda_010, "moeda(s) de R$ 0.10")
print(moeda_005, "moeda(s) de R$ 0.05")
print(moeda_001, "moeda(s) de R$ 0.01")
