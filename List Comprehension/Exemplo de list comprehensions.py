'''

Um exemplo prático de List Comprehension
O que faríamos se quisermos ordenar 2 listas "relacionadas"'''

vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

lista_aux = list(zip(vendas_produtos, produtos))
lista_aux.sort(reverse=True)
'''Sort esta ordenando'''

produtos = [produto for vendas, produto in lista_aux]
'''para cada vendas e produtos dentro da lista,  variavel produtos recebe os produto' da lista aux'''

print(produtos)

'''Podemos ler o caso acima da segundte forma

produto = []
for vendas_produtos, produtos in lista_aux:
    produto.append(produtos)
    print(produto)  '''