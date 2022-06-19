# Estrutura while:
# Funcionamento:
# Usamos o while quando queremos repetir um código de forma indeterminada até uma condição se tornar verdadeira/falsa.

# A lógica é: enquanto a condição for verdadeira, o while executa o código. Assim que ela terminar de ser verdadeira, o código "sai" do while.

# while condicao:
#     repete esse código:

venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia: ')
vendas = []
#crie aqui o programa

while venda != '':
    vendas.append(venda)
    venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia: ')



print('Registro Finalizado. As vendas cadastradas foram: {}'.format(vendas))