idade = int(input("Quantos anos você tem?: "))
# if é uma construção que permite executar código apenas se uma certa condição for satisfeita.
if idade >= 18 and idade != 100:
    print("Você é maior de idade!")
elif idade == 100:
    print("Você é centenário")
elif idade < 0:
    print("Você nem é nascido ainda!")
else:
    print("Você é menor de idade")
