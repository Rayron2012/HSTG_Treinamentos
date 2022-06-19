nome = input("Digite seu nome: ")
email = input("Digite seu E-mail: ")

# minha solução:
# if nome == "" or email == "":
#     print("Digite um E-mail e um nome!")
#
# elif email.count('@') == 1 and email.endswith(".com"):
#     print(f"""Olá {nome} o E-mail '{email}' foi cadastrado com sucesso!""")
#
# else:
#     print(f"Digite um e-mail valido, o email {email} não é valido!")


#  solução lira:

if nome and email:
    pos_a = email.find("@")
    servidor = email[pos_a:]
    if pos_a != -1 and "." in servidor:
        print("Cadastro concluido!")
    else:
        print("Email invalido! ")
else:
    print("Digite seu nome e email corretamente! ")
