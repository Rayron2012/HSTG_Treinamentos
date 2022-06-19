meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
meta_batida = []

for venda in vendas:
    if venda[1] >= meta:
        meta_batida.append(venda)

# print(meta_batida)
print("{:.0%} dos vendedores bateram a meta".format(len(meta_batida)/len(vendas)))

# ------------------
# cálculo diretamente na lista
qtde_vendedores_acima = 0

for venda in vendas:
    if venda[1] >= meta:
        qtde_vendedores_acima += 1

print('{:.0%} dos vendedores bateram a meta'.format(qtde_vendedores_acima / len(vendas)))