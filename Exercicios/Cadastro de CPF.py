cpf = input('Cadastre seu cpf :')

cpf = cpf.strip()
cpf = cpf.replace(".","")
cpf = cpf.replace("-","")


if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)
else:
    print("Digite seu cpf corretamente")
