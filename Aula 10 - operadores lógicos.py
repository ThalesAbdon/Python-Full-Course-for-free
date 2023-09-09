# os operadores lógicos são usados para combinar duas ou mais expressões booleanas e
# produzir uma expressão booleana como resultado.

temperatura = float(input("qual a temperatura lá fora?"))

if temperatura >= 0 and temperatura <= 30:
    print("A temperatura está agradavel")
elif temperatura < 0 or temperatura > 30:
    print("A temperatura está ruim")

if not (temperatura >= 0 and temperatura <= 30):
    print("A temperatura está agradavel")
elif not (temperatura < 0 or temperatura > 30):
    print("A temperatura está ruim")
