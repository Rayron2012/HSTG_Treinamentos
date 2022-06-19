vendas = [1000, 2000, 3000, 4000, 5000]
funcionarios = ["Rayron", "Léia", "Guilherme", "Bea", "Frank"]

for i, venda in enumerate(vendas):
    print("{} bate a meta com {} vendas". format(funcionarios[i], venda))

# o enumerate tranfarmo a informaçõo em tuplas e utilizando o i, venda estamos fazendo o unpack dessa tupla


