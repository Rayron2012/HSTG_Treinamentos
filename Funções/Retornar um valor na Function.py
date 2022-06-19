'''
Retornar um valor na Function Python

Estrutura Básica
Tipo de célula incompatível Clique duas vezes para inspecionar/editar o conteúdo
Exemplo: vamos criar uma função de cadastro de um Produto. Essa função deve garantir que o produto cadastrado está em letra minúscula.'''
'''
def nome_funcao():
    return valor final'''


def cadastrar_produto():
    produto = input('Digite o nome do produto que deseja cadastrar')
    produto = produto.casefold()
    produto = produto.strip() # retira espaços extras no inicio e fim da palavra caso o usuario tenha inserido ex:" rayron "
    return produto

produto = cadastrar_produto()

print(produto)