# vendas = [
#     ["maça", 5],
#     ["banana", 15],
#     ["azeite", 1],
#     ["vinho", 3],
# ]

vendas = []

produto = input("Digite o produto que você deseja comprar: ")
quantidade = input("Digite a quandidade desejada: ")
vendas.append([produto, quantidade])

while produto != "":
    if quantidade == "":

        break
    produto = input("Digite o produto que você deseja comprar: ")
    quantidade = input("Digite a quandidade desejada: ")
    vendas.append([produto, quantidade])

vendas.pop(-1)
print(vendas)



