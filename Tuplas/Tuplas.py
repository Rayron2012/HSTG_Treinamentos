# Tuplas
'''
Estrutura:
tupla = (valor, valor, valor, ...)

Diferença
Parece uma lista, mas é imutável.

Vantagens:
Mais eficiente (em termos de performance)
Protege a base de dados (por ser imutável)
Muito usado para dados heterogêneos
Criando tuplas
'''

vendas = ('Ray', '10/06/2022', '13/09/1994', 8000, 'Programador JR')

# nome = vendas[0]
# data_contratacao = vendas[1]
# data_nascimento = vendas[2]
# salario = vendas[3]
# cargo = vendas[4]

# Ou outra forma mais intuitiva e facil, poré a ordem e a quantidade tem que seguir de acordo com a tupla :

nome, data_contratacao, data_nascimento, salario, cargo = vendas
print(nome, data_contratacao, data_nascimento, salario, cargo)