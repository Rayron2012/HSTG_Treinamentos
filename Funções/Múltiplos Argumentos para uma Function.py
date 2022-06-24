'''
Quantidade Indefinidas de Argumentos
Utilidade:
Quando você quer permitir uma quantidade indefinida de argumentos, usa o * para isso.

Estrutura:
Tipo de célula incompatível Clique duas vezes para inspecionar/editar o conteúdo
'''

def minha_soma(*numeros):
    print(numeros)
    soma = 0
    for numero in numeros:
        soma += numero
    return soma
print(minha_soma(10, 13, 1, 10, 90, 0, 9, 8))


def preco_final(preco, **adicionais):
    print(adicionais)
    if 'desconto' in adicionais:
        preco *= (1 - adicionais['desconto'])
    if 'garantia_extra' in adicionais:
        preco += adicionais['garantia_extra']
    if 'imposto' in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco

print(preco_final(1000, desconto=0.1, garantia_extra = 100, imposto=0.3))