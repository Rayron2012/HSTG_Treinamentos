''''''
'''List Comprehensions com if para "filtrar" itens
Estrutura:'''

# Digamos que eu queira criar uma lista de produtos que bateram a meta.

meta = 1000
vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

produtos_acima_meta = []

'''Por for padrão'''
for i, produto in enumerate(produtos):
    if vendas_produtos[i] > meta:
        produtos_acima_meta.append(produto)

print(produtos_acima_meta)

'''Por list comprehensions'''
produtos_acima_meta = [produto for i, produto in enumerate(produtos) if vendas_produtos[i] > meta]
print(produtos_acima_meta)

'''lendo: produtos acima da meta vai receber, o produto da lista de produtos do mesmo indice se for um produto acima da meta'''