tec = ["celular","notebook","computador","alexa jamaicana de dreed"]
qtd = [100, 2, 5, 250]

busca = input("Digite o que deseja saber a quantidade em estoque :")

if busca in tec:
    i = tec.index(busca)
    qi = qtd[i]
    print(f"O item {busca} possui {qi} unidades")

else:
    print(f"O item {busca} não existe em nosso estoque")


