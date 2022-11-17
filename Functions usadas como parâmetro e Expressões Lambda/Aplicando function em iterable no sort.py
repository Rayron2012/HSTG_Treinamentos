''''''

'''sort (ou sorted) com function

Descrição:
Até agora no programa, usamos várias vezes o .sort() para ordenar listas

Mas o método sort tem um parâmetro que nunca usamos e que agora sabemos usar.'''

produtos = ['apple tv', 'mac', 'IPhone x', 'IPhone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
#Quando não é valor inteiro o sorte ordena de acordo com a tabela ASCII
# https://web.fe.up.pt/~ee96100/projecto/Tabela%20ascii.htm

produtos.sort() # Ao usar o produtos2 = sorted(produtos), tem que declarar a nova lista
print(produtos)


# Como faríamos para ordenar corretamente?
# poderiamos padronizar tudo para minusculo com casefold

produtos.sort(key=str.casefold)
produtos.sort(k)
print(produtos)


# Outro exemplo: como ordenar um dicionário de acordo com o valor

vendas_produtos = {'vinho': 100, 'cafeiteira': 150, 'microondas': 300, 'iphone': 5500}


# Queremos listar da maior quantidade de vendas para a menor, para enviar como report para o diretor, por exemplo
# para ler um dicionario é necessario transformalo em uma lista de tuplas : venda_prod = list(vendas_produtos.items()), dessa maneira é possivél trabalhar com os produtos e valores

def segundo_item(tupla):
    return tupla[1]
lista_vendas = list(vendas_produtos.items())
lista_vendas.sort(key=segundo_item, reverse=True)
print(dict(lista_vendas))