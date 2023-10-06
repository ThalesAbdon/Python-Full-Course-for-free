# lista = é usado para armazenar múltiplos itens em uma única variavél

foods = ["kkkkk", "Pizza", "Esfiha", "Torta de Limão", "Ervilha"]

foods[0] = "Sushi"

foods.append("Sorvete")
foods.remove('Ervilha')
foods.pop()
foods.insert(0, "Bolo de Ninho")
foods.sort()
# foods.clear()

for i in foods:
    print(i)
