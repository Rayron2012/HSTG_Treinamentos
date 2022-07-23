''''''

'''
Lambda Expressions para gerar funções

Descrição
Uma das aplicações de lambda expressions, além da vista na aula passada, é criar um "gerador de funções". Nesse caso, usaremos a lambda expressions dentro da definição de uma outra função
Exemplo:
Vamos criar uma função que me permita calcular o valor acrescido do imposto de diferentes categorias (produto, serviço, royalties, etc.)'''

def calcular_imposto(imposto):
    return lambda preco: preco * (1 + imposto)

# produto 0.1
#serviço 0.15
#royalties 0.25


'''Agora vamos definir as funções que calculam o imposto das 3 categorias (produto, serviço, royalties)'''
calcular_preco_produto = calcular_imposto(0.1)
calcular_preco_servico = calcular_imposto(0.15)
calcular_preco_royalties = calcular_imposto(0.25)

'''Agora vamos aplicar com um valor de nota fiscal de 100 para ver o resultado'''

print(int(calcular_preco_produto(100)))
print(int(calcular_preco_servico(100)))
print(calcular_preco_royalties(100))

# É menos usado do que a forma anterior que vimos, mas pode ser útil caso queira criar funções que possam ser adaptadas como vimos aqui


def calcular_preco_p(preco):
    return preco * 0.1
def calcular_servico(servico):
    return servico * 0.15


# Quando a função retorna lambda ela é um criador de função

