'''
break -> interrompe e finaliza o for
continue -> interrompe e vai para o próximo item do for
'''

vendas = [100, 150, 1500, 2000, 120]
todas_vendas = 0
# Caso 1: Se todas as vendas forem acima da meta, a loja ganha bônus
meta = 110

'''


for venda in vendas:
    if venda > meta:
        todas_vendas += 1
        if todas_vendas == len(vendas):
            print("A loja ganhou bonus")
    else:
        vagabundos = 0
        vagabundos += 1
        print("Infelizmente apenas {} não bateu a meta".format(vagabundos))'''


# Caso 2: Exiba quem bateu a meta
vendedores = ['João', 'Julia', 'Ana', 'José', 'Maria']

meta = 130

bateu = []

for i, venda in enumerate(vendas):
    if venda > meta:
        bateu.append(vendedores[i])
        print("{} Bateu a meta".format(vendedores[i]))

# Acima minhas resoluções

meta = 110

for venda in vendas:
    if venda < meta:
        print('A loja não ganha bônus')
        break #'''Para o argumento nessa etapa caso a função acima seja alcançada'''
    print(venda)

vendedores = ['João', 'Julia', 'Ana', 'José', 'Maria']
meta = 130

for venda in vendas:
    if venda < meta:
        continue #'''Continua caso a função acima seja atingida, mostrar apenas os valores que não são menores que a venda valores diferentes do if'''
    print(venda)
