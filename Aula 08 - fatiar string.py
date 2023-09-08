nome = "Thales Abdon"
primeiro_nome = nome[0:6]
ultimo_nome = nome[7:12]
apelido = nome[0:len(nome):2]
nome_reverso = nome[::-1]
print(nome_reverso)
print(apelido)
print(primeiro_nome)
print(ultimo_nome)

site = "http://google.com"
corte = slice(7, -4)
print(site[corte])
