def calcular_juros_composto():

    valor_inicial = float(input("Insira o valor inicial do investimento: R$"))
    taxa = float(input("Insira a taxa de juros anual (em decimal): "))
    periodos = int(input("Insira o número de períodos de investimento: "))

    valor_futuro = valor_inicial * (1 + taxa) ** periodos
    return valor_futuro


def calcular_raiz_quadrada(numero):
    if numero < 0:
        return "Erro: Não é possível calcular a raiz quadrada de um número negativo."
    else:
        raiz_quadrada = numero ** 0.5
        return raiz_quadrada


def calcular_raiz_cubica(numero):
    raiz_cubica = numero ** (1. / 3)
    return raiz_cubica


print(calcular_raiz_quadrada(36))
print(calcular_raiz_cubica(27))
