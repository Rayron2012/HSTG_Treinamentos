""" ZIP """

"""UTILIZAR O ZIP PARA ELE JUNTA DUAS LISTAS EM FORMAS DE LISTAS DE TUPLAS"""

a_letra = 'a'
b_letra = 'b'
c = 'c'

LIST_ZIPADA = zip(a_letra, b_letra)
'Ao fazer isso o a lista se transforma em um objeto, que pode ser convertido em uma lista posteriormente'

# print(LIST_ZIPADA)
''' se printar vira um objeto "<zip object at 0x000001A6BD617540>", se der um list ele vira uma lista '''

LIST_ZIPADA = list(zip(a_letra, b_letra, c))
print(LIST_ZIPADA)
'''É possivel fazer o unpack dessas informações'''

for l in LIST_ZIPADA:
    unpack = [a_letra,b_letra, c]
    print(unpack)

# for a_letra, b_letra, c in LIST_ZIPADA: