'''Aplicação de Tupla - Lista de Tuplas
Estrutura:
Além de casos como o do enumerate, em que usamos uma função para transformar itens em tuplas porque isso ajuda o nosso
código, temos também listas de tuplas como algo comum dentro do Python.'''

vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]

# data, produto, cor, capacidade, unidade, valor_unitario = vendas[0]
#
# faturamento = unidade * valor_unitario
#
# print(faturamento)

# Qual foi o faturamento de IPhone no dia 20/08/2020?
# Qual foi o produto mais vendido (em unidades) no dia 21/08/2020?

faturamento = 0
for item in vendas:
    data, produto, cor, capacidade, unidade, valor_unitario = item
    if "iphone" in produto and "20/08/2020" in data:   #Seleciona funciona como um contem, se contem aphone no produto:
        faturamento += unidade * valor_unitario


print("O Faturamento de vendas de iphone x no dia 20/08/2020 foi de R${} ".format(faturamento))

produto_mais_vendido = ""
qtd_produto_mais_vendido = 0

for item in vendas:
    data, produto, cor, capacidade, unidade, valor_unitario = item #Nesses casos se vê necessario a criação de de variaveis auxiliares, para concluir a logica (produtos mais vendidos e qtd)
    if data == "21/08/2020":
        if unidade > qtd_produto_mais_vendido:
            qtd_produto_mais_vendido = unidade
            produto_mais_vendido = produto

print("O {} foi o produto mais vendido no dia 21/08/2020, com o total de {} unidades ".format(produto_mais_vendido, qtd_produto_mais_vendido))