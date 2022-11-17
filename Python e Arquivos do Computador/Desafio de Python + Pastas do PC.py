''''''

import shutil
from pathlib import Path

caminho = Path('/Análise da Dados com o Pandas + Integração Python e Excel/Z_Arquivos_Lojas/')
estados = ['RJ', 'SP', 'MG', 'GO', 'AM']
arquivos = caminho.iterdir()
print(Path.cwd())


for estado in estados:
    if not  Path("Z_Arquivos_Lojas/{}".format(estado)).exists():
        Path("Z_Arquivos_Lojas/{}".format(estado)).mkdir()

# Necessario passar o path novamente
#  o arquivo.name pega apenas os nomes dos arquivos sem o diretorios antes
caminho = Path('Z_Arquivos_Lojas/')
arquivos = caminho.iterdir()
for arquivo in arquivos:
    nome_arquivo = arquivo.name
    if nome_arquivo[-3:] == "csv":
        estado = nome_arquivo[-6:-4]
        print(estado)
        local_final = caminho / Path('{}/{}'.format(estado, nome_arquivo))
        shutil.move(arquivo, local_final )

print("Processo finalizado com sucesso!")




# rj= Path(caminho/'RJ').mkdir()
# sp= Path(caminho/'SP').mkdir()
# mg= Path(caminho/'MG').mkdir()
# go= Path(caminho/'GO').mkdir()
# am= Path(caminho/'AM').mkdir()







# if not Path("Arquivos por estados").exists(): Path("Arquivos por estados").mkdir()



