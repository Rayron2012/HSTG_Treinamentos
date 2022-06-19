# quarto = [["Rayron","cpf:12365478910"],
#          ["Leia","cpf:09876543211"],
#          ["Faris","cpf:39456787501"],
#          ["Neno","cpf:2332478910"],
#          ["Giovanna","cpf:99988877700"]]
#
# qtd_pessoas = int(input("Quantas pessoas terão no quarto? "))
# quarto = []
#
# for i in range(qtd_pessoas):
#     nome = input("Digite o nome da pessoa: ")
#     cpf = int(input("digite o cpf da pessoa {}: ".format(nome)))
#     hospede = [nome, cpf]
#     quarto.append(hospede)
#
# print("Foram alugados {} quartos de solteiro, segue a lista : {} ".format(qtd_pessoas, quarto))

# ----------------------

# meta = 10000
# vendas = [
#     ['João', 15000],
#     ['Julia', 27000],
#     ['Marcus', 9900],
#     ['Maria', 3750],
#     ['Ana', 10300],
#     ['Alon', 7870],
# ]
#
# for i in vendas:
#     if i[1] > meta:
#         print("Parabéns {} você bateu a meta com {} vendas".format(i[0], i[1] ))
#
#-----------------------------



produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]

for i, produtos in enumerate(produtos):
    if vendas2020 > vendas2019:
        print("O produro {} em 2019 vendeu {}, em 2020 vendeu {}, com crescimento de {:.0%}". format(produtos, vendas2019[i], vendas2020[i], (vendas2020[i]/vendas2019[i])-1))
