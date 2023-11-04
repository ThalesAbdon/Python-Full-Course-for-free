# Sets são coleções não-ordenadas de itens ÚNICOS, embora um Set possa ser modificado,
# os elementos contidos dentro do Set devem ser imutáveis.
# Sets são definidos por valores separados por vírgula dentro de chaves {}.

cores = {"azul", "vermelho", "verde", "rosa", "azul"}
cores_primarias = {"azul", "vermelho", "verde"}
print(cores)

cores.add("laranja")
print(cores)

for x in cores:
    print(x)

print(cores.intersection(cores_primarias))
print(cores.difference(cores_primarias))
