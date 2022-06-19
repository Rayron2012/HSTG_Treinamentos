'''

Set

Estrutura:
meu_set = {valor, valor, valor, valor,...}

Observações:
Não pode ter valores duplicados
Não tem ordem fixa

'''

set_produtos = {'arroz', 'feijao', 'macarrao', 'atum', 'azeite'}

print(set_produtos)

'''
Aplicação bem útil:

Quantos clientes tivemos na loja?'''

cpf_clientes = ['762.196.080-97', '263.027.380-67', '827.363.930-40', '925.413.640-91', '870.565.160-33', '892.080.930-50', '462.126.030-81', '393.462.330-10', '393.462.330-10', '393.462.330-10', '988.305.810-11', '596.125.830-05', '596.125.830-05', '990.236.770-48']

set_cpf_clientes = set(cpf_clientes)

# Transformar novamente em lista e aplicar todos os parametros possiveis
lista_set_cpf_clientes = list(set_cpf_clientes)


print(len(set_cpf_clientes))

# O set transforma valores duplicados em unique e alem disso printa valores de forma aleatoria