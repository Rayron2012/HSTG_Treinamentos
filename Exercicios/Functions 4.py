precos_imoveis = [2.17,1.54,1.45,1.94,2.37,2.3,1.79,1.8,2.25,1.37]
tamanho_imoveis = [207,148,130,203,257,228,160,194,232,147]

fator = 0.1

i = int((1- fator) * len(precos_imoveis))

preco_treino = precos_imoveis[:i]
preco_teste = precos_imoveis[i:]




def separar_listas(lista_valores, lista_atributos, fator=0.1):
    qtde_valores = len(precos_imoveis)
    if qtde_valores == len(tamanho_imoveis):
        i = int(qtde_valores - qtde_valores * fator)
        print(i, qtde_valores)
        lista_valores_treino = lista_valores[:i]
        lista_valores_teste = lista_valores[i:]
        lista_atributos_treino = lista_atributos[:i]
        lista_atributos_teste = lista_atributos[i:]
        return lista_valores_treino, lista_atributos_treino, lista_valores_teste, lista_atributos_teste
    else:
        print('Lista Valores e Lista Atributos de Tamanho diferentes, favor corrigir')
        return


y_treino, x_treino, x_teste, y_teste = separar_listas(precos_imoveis, tamanho_imoveis)
print(x_teste)