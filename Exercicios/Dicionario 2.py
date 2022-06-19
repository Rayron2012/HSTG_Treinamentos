
vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}


# Transformar dicionario em uma lista de tuplas:

items_dicionario = vendas_tecnologia.items()

print(items_dicionario)

print("-------------------")
# ou mostre acima de 5000 unidades:

# Dicionario:
for chave in vendas_tecnologia:
    valor = vendas_tecnologia[chave] # quando usamos dicionario a forma de obter o valor pode ser feita assim, pois extraimos o valor de um item e alocamos em uma variavel
    if valor >= 5000:
        print("O produto ({}) possui {} unidades.".format(chave, valor))

print("-------------------")

# .items
for item, qtd in vendas_tecnologia.items(): # Assim fica mais facil de desempacotar pois trasnformamos o dicionario em tuplas e abrimos a tupla de uma forma facil
    if qtd >= 5000:
        print('Produto {} e {} unidades'.format(item, qtd))

print("-------------------")


# Transformar chaves e valores em listas apartadas:

chaves = vendas_tecnologia.keys()
valores = vendas_tecnologia.values()
print(chaves)
print(valores)

print("-------------------")

# Utilizamos o metodo list para transformar em uma lista limpa
print(list(chaves))
print(list(valores))

print("-------------------")

# Colocar em uma variavel

lista_chaves = list(chaves)
lista_valores = list(valores)
lista_chaves.sort()


for chave in lista_chaves:
    print("O produto {}, tem {} unidades".format(chave, vendas_tecnologia[chave]))