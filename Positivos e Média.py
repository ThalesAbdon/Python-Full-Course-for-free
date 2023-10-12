valor = float(input("digite um valor: "))
aux = 0
qtd_valores_positivos = 0
soma = 0

for i in range(5):
    if (valor >= 0):
        soma += valor
        qtd_valores_positivos += 1
        aux += 1
    valor = float(input("digite um valor: "))

# while aux < 5:
#     if (valor >= 0):
#         soma += valor
#         qtd_valores_positivos += 1
#     aux += 1
#     valor = float(input("digite um valor: "))

print(qtd_valores_positivos, "valores positivos")
print(soma/qtd_valores_positivos)
