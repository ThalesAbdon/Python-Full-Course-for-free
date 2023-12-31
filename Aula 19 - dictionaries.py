# É a coleção de todas as palavras que podem ser usadas na linguagem, como em uma língua falada

pokemons = {
    '001': {
        'Nome': 'Charmander',
        'Tipo': 'Fogo',
        'Evolução': 'Charmeleon',
        'Fraquezas': ['Água', 'Terra', 'Pedra'],
        'Ataques': ['Arranhão', 'Lança-chamas', 'Soco de Fogo'],
    },
    '004': {
        'Nome': 'Bulbassauro',
        'Tipo': ['Grama', 'Venenoso'],
        'Evolução': 'Ivysaur',
        'Fraquezas': ['Fogo', 'Psíquico', 'Voador', 'Gelo'],
        'Ataques': ['Investida', 'Chicote de Vinha', 'Semente Sanguessuga'],
    }
}

print(f"Número: 001")
print(f"Nome: {pokemons['001']['Nome']}")
print(f"Tipo: {pokemons['001']['Tipo']}")
print(f"Evolução: {pokemons['001']['Evolução']}")
print(f"Fraquezas: {', '.join(pokemons['001']['Fraquezas'])}")
print(f"Ataques: {', '.join(pokemons['001']['Ataques'])}")


print(f"Número: 004")
print(f"Nome: {pokemons['004']['Nome']}")
print(f"Tipo: {', '.join(pokemons['004']['Tipo'])}")
print(f"Evolução: {pokemons['004']['Evolução']}")
print(f"Fraquezas: {', '.join(pokemons['004']['Fraquezas'])}")
print(f"Ataques: {', '.join(pokemons['004']['Ataques'])}")

# for num, info in pokemons.items():
#     print(f"Número: {num}")
#     print(f"Nome: {info['Nome']}")
#     if isinstance(info['Tipo'], list):
#         print(f"Tipo: {', '.join(info['Tipo'])}")
#     else:
#         print(f"Tipo: {info['Tipo']}")
#     print(f"Evolução: {info['Evolução']}")
#     print(f"Fraquezas: {', '.join(info['Fraquezas'])}")
#     print(f"Ataques: {', '.join(info['Ataques'])}")
#     print()  # Linha em branco entre os Pokémon
