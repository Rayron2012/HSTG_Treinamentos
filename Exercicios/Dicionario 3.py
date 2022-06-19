'''

Transformando Listas em Dicionários e Function zip

Estrutura:

Dicionário com valores padrões:
dicionario = dict.fromkeys(lista_chaves, valor_padrao)

Dicionário a partir de listas de tuplas:
dicionario = dict(lista_tuplas)

Dicionário a partir de 2 listas:
Passo 1: Transformar listas em lista de tuplas com o método zip
Passo 2: Transformar em dicionario

lista_tuplas = zip(lista1, lista2)
dicionario = dict(lista_tuplas)
'''

produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus']
vendas = [15000, 12000, 10000, 14300, 1720, 1000, 2500, 1000, 17000, 2450]


# dicionario = dict.fromkeys(produtos, 0) #transforma uma lista em tuplas porem com valor fixo ex: 0
# print(dicionario)

lista_tuplas = zip(produtos, vendas) # transforma em objeto
# é necessario usar for para exibir os itens dentro desse objeto

for item in lista_tuplas:
    print(item)

dicionario_vendas = dict(lista_tuplas) #Usado para transformar o objeto em dicionario
print(dicionario_vendas)


#fazendo por listas
indice = produtos.index('ipad')
print('Vendemos {} ipads'.format(vendas[indice]))

#fazendo por dicionario
print('Vendemos {} ipads'.format(dicionario_vendas['ipad']))
