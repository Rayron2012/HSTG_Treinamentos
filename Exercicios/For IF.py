
# for + if
# Estrutura:
# Tipo de célula incompatível Clique duas vezes para inspecionar/editar o conteúdo
# Digamos que a gente esteja analisando a meta de vendas de vários funcionários de uma empresa. A meta de vendas é de 1000 reais em 1 dia.
#
# Temos uma lista com as vendas de todos os funcionários e quero calcular qual o % de pessoas que bateram a meta.


vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
meta = 1000

bateu_meta = 0

for v in vendas:
    if v >= meta:
        bateu_meta += 1

print(f"{bateu_meta} pessoas bateram a meta ")

