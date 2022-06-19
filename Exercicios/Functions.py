'''
Exercícios
Para fazer um treino simples antes de avançarmos em mais functions, vamos criar uma function que resolve 1 "desafio simples"

1. Function para Cálculo de Carga Tributária
(Lembrando, não se atente ao funcionamento real da carga tributária, é apenas um exemplo imaginário para treinarmos as functions com algo mais prático)

Imagine que você trabalha no setor contábil de uma grande empresa de Varejo.

Crie uma function que calcule qual o % de carga tributária que está sendo aplicado sobre um determinado produto, dado o preço de venda, o "lucro" e os custos (com exceção do imposto) dele.
'''

preco = 1500
custo = 400
lucro = 800

def carga_tributaria(preco, custo, lucro):
    imposto = preco - custo - lucro
    return imposto / preco

print("A carga tributaria foi de {:.0%}".format(carga_tributaria(preco, custo, lucro)))


nome = input("Digite seu primeiro nome: ")
sobrenome1 = input('Digite seu sobrenome: ')
sobrenome2 = input('Digite seu ultimo nome (caso tenha): ')

def nome_completo(nome, sobrenome1, sobrenome2):
    nome_chamada = nome +" "+ sobrenome1
    nome_cheio =nome_chamada +' '+ sobrenome2
    return nome_cheio.upper()

print('O seu nome completo é {}'.format(nome_completo(nome, sobrenome1, sobrenome2)))

