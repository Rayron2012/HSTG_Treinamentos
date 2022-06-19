'''

Function Python
O que é?
As functions são blocos de código que servem 1 único propósito, fazem uma ação específica.

Estrutura Básica
'''

# def nome_função():
#     faça alguma coisa
#     faça outra coisa
#     return valor final

def cadastrar_produto():
    produto = input("Digite o nome do produto: ")
    produto = produto.casefold()
    print("produto {} cadastrado com sucesso".format(produto))

for i in range(3):
    cadastrar_produto()
