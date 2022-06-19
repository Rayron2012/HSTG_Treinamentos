texto = 'rayron'

print(texto.capitalize())

'''Primeira maiuscula'''
#

print('RAYRON'.casefold())
'''Texto todo em minusculo'''
#

print('rayronfic@fic.com.br'.count("."))
'''Conta quantas vezes o . esta dentro da string'''
#

print('rayronfic@fic.com.br'.endswith("fic.com.br"))
'''Verifica se o final da string termina com o texto ou não, em boleano'''
#

print('rayronfic@fic.com.br'.find("@"))
'''Da a posição de um texto dentro de outro texto'''
#

print('Rayron2012'.isalnum())
'''Verifica se um texto é alfanumerico feito de (letras e numeros) ou de (letras ou de numeros), e retorna em booleano'''
#

print('Rayron'.isalpha())
'''Verifica se um texto é feito de letras, e retorna em booleano'''
#

print('2012'.isnumeric())
'''Verifica se um texto é feito de numeros, e retorna em booleano'''
#

n = '1000.00'
print(n.replace(".",","))
'''Troca os textos - primeiro o texto que vai sair e depois o que vai entrar'''
#

a = 'rayronfic@fic.com.br'
print(a.split("@"))
'''Separa uma string de acordo com um delimitador em varios textos diferentes'''
#

splitline = '''Olá venho por meio deste
efetuar um teste e verificar se o python é mesmo legal
veremos se é mesmo...
'''
print(splitline.splitlines())
'''Separa os textos de acordo com os enter´s, as linhas utilizadas'''
#

print(texto.startswith("ray"))
'''Verifica se o inicio do texto começa com o que tiver no argumento -> ("ray")'''
#

espaço = ' espaço '
print(espaço.strip())
'''Tira caracteres indesejados da string - retira espaços extras'''
#

nome_completo = 'rayron soares candido'

print(nome_completo.title())
'''Coloca a primeira letra de cada palavra em maiuscula'''
#

print(nome_completo.upper())
'''Coloca o texto todo em maiusculo'''